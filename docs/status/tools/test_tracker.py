"""Bounded offline fixture tests; no original inputs, network, game builds or pushes."""
from pathlib import Path
import copy
import hashlib
import json
import shutil
import subprocess
import tempfile
import unittest

import update_tracker as u
import check_generated_changes as guard

class TrackerTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='rock-man-tracker-test-')
        self.root=Path(self.tmp.name)/'repo'
        shutil.copytree(u.ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc'))
        self.git('init','-q','-b','main');self.git('config','user.name','Fixture');self.git('config','user.email','fixture@example.invalid')
        self.git('add','.');self.git('commit','-qm','fixture baseline')
    def tearDown(self):self.tmp.cleanup()
    def git(self,*args):return subprocess.run(['git',*args],cwd=self.root,check=True,capture_output=True,text=True).stdout.strip()
    def data(self):return json.loads((self.root/u.DATA).read_text())
    def save(self,d): (self.root/u.DATA).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
    def hashes(self):return {str(p.relative_to(self.root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.rglob('*') if p.is_file() and '.git' not in p.parts}
    def test_01_idempotent_check_and_write(self):
        u.run(self.root,False);a=self.hashes();self.assertEqual(u.run(self.root,False),[]);self.assertEqual(a,self.hashes());u.run(self.root,True)
    def test_02_drift_is_rejected(self):
        p=self.root/'docs/status/changes.md';p.write_text(p.read_text()+'drift\n')
        with self.assertRaisesRegex(u.Invalid,'stale'):u.run(self.root,True)
    def test_03_missing_evidence_refuses_before_write(self):
        d=self.data();d['workstreams'][0]['stages'][4]=1;self.save(d);before=self.hashes()
        with self.assertRaisesRegex(u.Invalid,'lacks evidence'):u.run(self.root,False)
        self.assertEqual(before,self.hashes())
    def test_04_invalid_stage_and_boolean_rejected(self):
        for value in (True,3,-1,'1'):
            d=self.data();d['workstreams'][0]['stages'][0]=value;self.save(d)
            with self.assertRaises(u.Invalid):u.run(self.root,False)
    def test_05_source_only_update_cannot_claim_runtime_advance(self):
        d=self.data();d['updates'][1]['capability_changed']=True;self.save(d)
        with self.assertRaisesRegex(u.Invalid,'cannot claim runtime'):u.run(self.root,False)
    def test_06_broken_source_refused(self):
        d=self.data();d['workstreams'][0]['stage_evidence']['0']=['docs/not-present.md'];self.save(d)
        with self.assertRaisesRegex(u.Invalid,'missing source'):u.run(self.root,False)
    def test_07_missing_readme_marker_refuses_before_write(self):
        p=self.root/'README.md';p.write_text(p.read_text().replace(u.START,''));before=self.hashes()
        with self.assertRaisesRegex(u.Invalid,'marker'):u.run(self.root,False)
        self.assertEqual(before,self.hashes())
    def test_08_symlink_output_is_refused(self):
        target=self.root/'docs/status/changes.md';outside=Path(self.tmp.name)/'outside.md';outside.write_text('untouched');target.unlink();target.symlink_to(outside)
        with self.assertRaisesRegex(u.Invalid,'symlink'):u.run(self.root,False)
        self.assertEqual(outside.read_text(),'untouched')
    def test_09_activity_only_commit_does_not_move_stages(self):
        before=copy.deepcopy(self.data()['workstreams']);p=self.root/'research/README.md';p.write_text(p.read_text()+'\nFixture research update.\n');self.git('add','.');self.git('commit','-qm','research-only fixture')
        sha=self.git('rev-parse','HEAD');u.run(self.root,False,refresh=sha)
        self.assertEqual(before,self.data()['workstreams']);self.assertIn('**Review pending:**',(self.root/'README.md').read_text())
        a=json.loads((self.root/u.STATE).read_text())['latest_repository_change'];self.assertFalse(a['evidence_data_changed']);self.assertFalse(a['review_id_changed']);u.run(self.root,True)
    def test_10_authored_review_is_identified_not_inferred(self):
        d=self.data();d['last_evidence_review']['review_id']='fixture-review-02';d['overview']['changed']='Reviewed fixture explanation only.';self.save(d);self.git('add','.');self.git('commit','-qm','authored evidence fixture')
        u.run(self.root,False,refresh=self.git('rev-parse','HEAD'))
        self.assertIn('**Authored evidence update supplied:**',(self.root/'README.md').read_text())
        self.assertFalse(any(w['stages'][4] for w in self.data()['workstreams']))
    def test_11_data_edit_without_new_review_remains_pending(self):
        d=self.data();d['overview']['changed']='Editorial fixture change without a new review.';self.save(d);self.git('add','.');self.git('commit','-qm','editorial fixture')
        u.run(self.root,False,refresh=self.git('rev-parse','HEAD'));self.assertIn('**Review pending:**',(self.root/'README.md').read_text())
    def test_12_malicious_commit_subject_is_not_shell_or_html(self):
        self.git('commit','--allow-empty','-qm','<script>alert(1)</script> | $(touch SHOULD_NOT_EXIST)')
        u.run(self.root,False,refresh=self.git('rev-parse','HEAD'));s=(self.root/'README.md').read_text();self.assertNotIn('<script>',s);self.assertIn('&lt;script&gt;',s);self.assertFalse((self.root/'SHOULD_NOT_EXIST').exists())
    def test_13_invalid_sha_refused(self):
        with self.assertRaisesRegex(u.Invalid,'full commit SHA'):u.run(self.root,False,refresh='HEAD; false')
    def test_14_private_metadata_pattern_rejected(self):
        d=self.data();d['unexpected_note']='/workspace/private/original.bin';self.save(d)
        with self.assertRaisesRegex(u.Invalid,'private-content'):u.run(self.root,False)
    def test_15_check_never_refreshes_or_writes(self):
        before=self.hashes()
        with self.assertRaisesRegex(u.Invalid,'cannot refresh'):u.run(self.root,True,refresh='0'*40)
        self.assertEqual(before,self.hashes())
    def test_16_guard_rejects_extra_tracked_and_untracked_changes(self):
        for path in ['DOX-LICENSE','unexpected.txt']:
            p=self.root/path;old=p.read_bytes() if p.exists() else None;p.write_text('changed')
            with self.assertRaisesRegex(u.Invalid,'unauthorized dirty'):guard.check(self.root)
            p.write_bytes(old) if old is not None else p.unlink()
    def test_17_guard_preserves_readme_outside_marker(self):
        p=self.root/'README.md';p.write_text('outside modification\n'+p.read_text())
        with self.assertRaisesRegex(u.Invalid,'outside generated block'):guard.check(self.root)
    def test_18_guard_allows_only_actual_generated_outputs(self):
        self.git('commit','--allow-empty','-qm','activity fixture');u.run(self.root,False,refresh=self.git('rev-parse','HEAD'));paths=guard.check(self.root)
        self.assertTrue(paths);self.assertTrue(set(paths)<=set(u.OUTPUTS));self.git('add','--',*u.OUTPUTS);guard.check(self.root)
    def test_19_unchanged_workstreams_and_archived_art_are_preserved(self):
        before=self.hashes();u.run(self.root,False);after=self.hashes()
        self.assertTrue({p for p in before if before[p]!=after[p]}<=set(u.OUTPUTS))
    def test_20_duplicate_entry_is_rejected(self):
        d=self.data();d['updates'].append(d['updates'][0]);self.save(d)
        with self.assertRaisesRegex(u.Invalid,'duplicate update'):u.run(self.root,False)
    def test_21_hostile_source_path_is_rejected(self):
        d=self.data();d['workstreams'][0]['source']='../outside';self.save(d)
        with self.assertRaisesRegex(u.Invalid,'escapes'):u.run(self.root,False)
    def test_22_fixture_fast_forward_race_rejects_stale_commit(self):
        # Local branch simulation: two children of the same expected head cannot fast-forward each other.
        base=self.git('rev-parse','HEAD');self.git('branch','other',base);self.git('commit','--allow-empty','-qm','generated child');generated=self.git('rev-parse','HEAD');self.git('checkout','-q','other');self.git('commit','--allow-empty','-qm','new user child')
        result=subprocess.run(['git','merge-base','--is-ancestor','HEAD',generated],cwd=self.root,capture_output=True)
        self.assertEqual(result.returncode,1);self.assertNotEqual(self.git('rev-parse','HEAD'),base)
    def test_23_workflow_has_narrow_trigger_permissions_and_pinned_action(self):
        s=(self.root/'.github/workflows/update-progress.yml').read_text()
        self.assertIn('branches: [main]',s);self.assertNotIn('pull_request',s);self.assertNotIn('workflow_dispatch',s)
        self.assertEqual(s.count('uses:'),1);self.assertIn('actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683',s)
        self.assertIn('persist-credentials: false',s);self.assertIn('cancel-in-progress: false',s);self.assertNotIn('--force',s)
        self.assertIn('test "$remote_head" = "$TRIGGER_SHA"',s);self.assertIn('github.actor !=',s)
    def test_24_same_review_id_cannot_promote_a_stage(self):
        d=self.data();w=d['workstreams'][0];w['stages'][4]=1;w['stage_evidence']['4']=[w['source']];self.save(d);before=self.hashes()
        with self.assertRaisesRegex(u.Invalid,'new evidence review identifier'):u.run(self.root,False)
        self.assertEqual(before,self.hashes())
    def test_25_git_parent_catches_forged_previous_stage_receipt(self):
        d=self.data();w=d['workstreams'][0];w['stages'][4]=1;w['stage_evidence']['4']=[w['source']];self.save(d)
        p=self.root/u.STATE;s=json.loads(p.read_text());s['reviewed_stage_sha256']=u.stage_digest(d);p.write_text(json.dumps(s)+'\n');self.git('add','.');self.git('commit','-qm','same-review promotion fixture')
        with self.assertRaisesRegex(u.Invalid,'without a new evidence review identifier'):u.run(self.root,False,refresh=self.git('rev-parse','HEAD'))
    def test_26_remote_image_commit_subject_stays_literal(self):
        self.git('commit','--allow-empty','-qm','![remote image](https://example.invalid/pixel.png)');u.run(self.root,False,refresh=self.git('rev-parse','HEAD'))
        s=(self.root/'README.md').read_text();self.assertNotIn('![remote image](',s);self.assertIn(r'\!\[remote image\]\(',s)
    def test_27_guard_rejects_external_svg_style(self):
        p=self.root/'docs/status/visuals/progress-dashboard.svg';p.write_text(p.read_text().replace('<rect ', '<rect style="fill:url(https://example.invalid/external.svg)" ',1))
        with self.assertRaisesRegex(u.Invalid,'external/entity SVG'):guard.check(self.root)
    def test_28_guard_checks_staged_readme_not_only_worktree(self):
        p=self.root/'README.md';original=p.read_text();p.write_text('staged outside-marker change\n'+original);self.git('add','README.md');p.write_text(original)
        with self.assertRaisesRegex(u.Invalid,'outside generated block'):guard.check(self.root)
    def test_29_guard_checks_staged_svg_not_only_worktree(self):
        p=self.root/'docs/status/visuals/progress-dashboard.svg';original=p.read_text();p.write_text(original.replace('<rect ', '<rect style="fill:url(https://example.invalid/external.svg)" ',1));self.git('add',str(p.relative_to(self.root)));p.write_text(original)
        with self.assertRaisesRegex(u.Invalid,'external/entity SVG'):guard.check(self.root)
    def test_30_missing_prior_review_receipt_refused(self):
        p=self.root/u.STATE;s=json.loads(p.read_text());del s['reviewed_stage_sha256'];p.write_text(json.dumps(s))
        with self.assertRaisesRegex(u.Invalid,'prior reviewed-stage receipt'):u.run(self.root,False)
    def test_31_guard_rejects_encoded_external_svg_paint(self):
        p=self.root/'docs/status/visuals/progress-dashboard.svg';p.write_text(p.read_text().replace('fill="#10171b"','fill="u&#114;l(//example.invalid/x)"',1))
        with self.assertRaisesRegex(u.Invalid,'external parsed SVG'):guard.check(self.root)

if __name__=='__main__':unittest.main()
