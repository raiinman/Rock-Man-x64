"""Bounded offline fixture tests; no original inputs, network, game builds or pushes."""
from pathlib import Path
import copy
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

import update_tracker as u
import check_generated_changes as guard

def synthetic_fixture():
    """Explicit test-owned semantics; never derive flags/IDs/history from live data."""
    date='2026-01-01';basis='1'*40;ref='docs/status/fixture-evidence.md'
    plans=(('inspection',7,4),('observation',4,2),('loader',4,3),
           ('s2',4,0),('boot',1,0),('roadmap',20,5))
    checklists=[]
    for cid,total,accepted in plans:
        items=[]
        for n in range(total):
            item={'id':f'{cid}-goal-{n}', 'label':f'Synthetic {cid} goal {n}',
                  'criterion':'Owned synthetic criterion, never a project claim.',
                  'done':n<accepted, 'evidence_class':'Synthetic fixture only', 'source':ref}
            if cid=='roadmap':item['phase']='foundation' if n<5 else 'production'
            items.append(item)
        checklists.append({'id':cid,'title':'Synthetic '+cid,'version':1,'frozen_on':date,
                           'scope':'Owned test definition.','blocker':'Synthetic blocker.',
                           'next':'Synthetic next step.','items':items})
    review={'date':date,'review_id':'fixture-initial-review','reviewed_through_commit':basis,
            'summary':'Owned synthetic baseline, not real acceptance.'}
    observation={'review_id':review['review_id'],'date':date,'basis_commit':basis,
                 'note':'Owned synthetic baseline only.',
                 'checklists':[{'id':c['id'],'version':1,'total':len(c['items']),
                                'completed_ids':[i['id'] for i in c['items'] if i['done']]}
                               for c in checklists]}
    data={'schema_version':3,'last_evidence_review':review,
          'overview':{k:'Synthetic fixture explanation.' for k in ('now','changed','why','next')},
          'workstreams':[{'id':'fixture-stream','name':'Synthetic stream',
                         'plain_status':'Synthetic status.','next':'Synthetic next step.',
                         'detail':'Synthetic bounded evidence.','limit':'Not a real capability.',
                         'stages':[1,1,1,1,0],'source':ref,
                         'stage_evidence':{str(n):[ref] for n in range(4)}}],
          'updates':[{'id':'fixture-update-'+str(n),'date':date,'kind':kind,
                      'capability_changed':False,'changed':'Synthetic change.',
                      'why':'Synthetic reason.','next':'Synthetic next step.','evidence':[ref]}
                     for n,kind in enumerate(('documentation','source-review'))],
          'findings':[{'id':'01','title':'Synthetic finding','found':'Synthetic result.',
                       'why':'Synthetic reason.','unknown':'Not project evidence.',
                       'class':'Synthetic','metric':'1','unit':'fixture','sources':[ref]}],
          'provenance':'Owned synthetic fixture only.','checklists':checklists,
          'validation_runs':[{'title':'Synthetic suite '+str(n),'passed':total,'total':total,
                              'unit':'checks','scope':'Synthetic fixture only.','source':ref}
                             for n,total in enumerate((69,111,50))],
          'observations':[observation]}
    state={'schema_version':2,'latest_repository_change':{
               'sha':basis,'committed_at':date+'T00:00:00Z','subject':'Synthetic fixture',
               'source':'Owned synthetic fixture metadata'},'trigger_status':'Synthetic fixture only.',
           'reviewed_stage_sha256':u.stage_digest(data),'evidence_review_id':review['review_id'],
           'evidence_review_date':date,'reviewed_checklist_definitions':u.definitions(data),
           'recorded_observation_hashes':[u.digest(observation)]}
    return data,state

class TrackerTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='rock-man-tracker-test-')
        self.root=Path(self.tmp.name)/'repo'
        shutil.copytree(u.ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc'))
        # Copy real code/workflow and inert documents, but replace all mutable evidence
        # semantics with an explicit owned fixture before any mutation test runs.
        data,state=synthetic_fixture()
        (self.root/'docs/status/fixture-evidence.md').write_text('# Synthetic evidence\n')
        (self.root/u.DATA).write_text(json.dumps(data,indent=2)+'\n')
        (self.root/u.STATE).write_text(json.dumps(state,indent=2)+'\n')
        u.run(self.root,False)
        self.assertFalse(data['checklists'][0]['items'][4]['done'])
        self.assertTrue(data['checklists'][0]['items'][0]['done'])
        self.assertFalse(data['checklists'][-1]['items'][5]['done'])
        self.assertEqual(len(data['observations']),1)
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
        d=self.data();self.snapshot(d,'fixture-review-02');d['overview']['changed']='Reviewed fixture explanation only.';self.save(d);self.git('add','.');self.git('commit','-qm','authored evidence fixture')
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
        updater=s.split('\n  update:\n',1)[1].split('\n  build-site:\n',1)[0]
        self.assertEqual(updater.count('uses:'),1);self.assertIn('actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683',updater)
        self.assertIn('contents: write',updater);self.assertNotIn('pages: write',updater);self.assertNotIn('id-token: write',updater)
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
        p=self.root/'docs/status/visuals/progress-dashboard.svg';original=p.read_text();mutated=re.sub(r'fill="#[0-9a-fA-F]{6}"','fill="u&#114;l(//example.invalid/x)"',original,count=1);self.assertNotEqual(original,mutated);p.write_text(mutated)
        with self.assertRaisesRegex(u.Invalid,'external parsed SVG'):guard.check(self.root)

    def snapshot(self,d,review_id='fixture-numeric-review-02'):
        d['last_evidence_review']['review_id']=review_id
        d['observations'].append({'review_id':review_id,'date':d['last_evidence_review']['date'],'basis_commit':d['last_evidence_review']['reviewed_through_commit'],'note':'Synthetic documentation fixture, not actual project acceptance.','checklists':[{'id':c['id'],'version':c['version'],'total':len(c['items']),'completed_ids':[i['id'] for i in c['items'] if i['done']]} for c in d['checklists']]})
    def test_32_done_promotion_without_review_refuses_before_write(self):
        d=self.data();d['checklists'][0]['items'][4]['done']=True
        self.snapshot(d,d['last_evidence_review']['review_id']+'-observation');d['last_evidence_review']['review_id']=self.data()['last_evidence_review']['review_id'];self.save(d);before=self.hashes()
        with self.assertRaisesRegex(u.Invalid,'match the evidence review'):u.run(self.root,False)
        self.assertEqual(before,self.hashes())
    def test_33_done_change_without_snapshot_refused(self):
        d=self.data();d['checklists'][0]['items'][4]['done']=True;self.save(d)
        with self.assertRaisesRegex(u.Invalid,'matching recorded observation'):u.run(self.root,False)
    def test_34_denominator_removal_without_version_refused(self):
        d=self.data();d['checklists'][0]['items'].pop();self.snapshot(d);self.save(d)
        with self.assertRaisesRegex(u.Invalid,'historical denominator changed'):u.run(self.root,False)
    def test_35_denominator_inflation_without_version_refused(self):
        d=self.data();i=copy.deepcopy(d['checklists'][0]['items'][0]);i['id']='synthetic-extra';d['checklists'][0]['items'].append(i);self.snapshot(d);self.save(d)
        with self.assertRaisesRegex(u.Invalid,'historical denominator changed'):u.run(self.root,False)
    def test_36_criteria_edit_without_version_refused(self):
        d=self.data();d['checklists'][0]['items'][0]['criterion']='Changed synthetic criterion';self.snapshot(d);self.save(d)
        with self.assertRaisesRegex(u.Invalid,'new checklist version'):u.run(self.root,False)
    def test_37_baseline_history_rewrite_refused(self):
        d=self.data();d['observations'][0]['note']='Rewritten synthetic past';self.snapshot(d);self.save(d)
        with self.assertRaisesRegex(u.Invalid,'append-only'):u.run(self.root,False)
    def test_38_fresh_review_advances_exactly_one_named_goal(self):
        d=self.data();d['checklists'][0]['items'][4]['done']=True;self.snapshot(d);self.save(d);u.run(self.root,False);u.run(self.root,True)
        self.assertEqual(u.numbers(d['checklists'][0]),(5,7,71.4));self.assertEqual(u.delta_label(d,d['checklists'][0]),'Δ +1 goals')
        self.assertIn('5 / 7',(self.root/'docs/status/visuals/progress-dashboard.svg').read_text())
    def test_39_new_version_rebaselines_instead_of_claiming_delta(self):
        d=self.data();d['checklists'][0]['version']=2;d['checklists'][0]['items'].pop();self.snapshot(d);self.save(d);u.run(self.root,False)
        self.assertEqual(u.delta_label(d,d['checklists'][0]),'Δ — rebaseline');self.assertEqual(u.numbers(d['checklists'][0]),(4,6,66.7))
    def test_40_activity_only_preserves_numbers_and_history(self):
        d=self.data();self.git('commit','--allow-empty','-qm','activity only numeric fixture');u.run(self.root,False,refresh=self.git('rev-parse','HEAD'))
        self.assertEqual(d,self.data());self.assertEqual(self.data()['observations'],d['observations']);self.assertIn('Review pending',(self.root/'README.md').read_text())
    def test_41_forged_numeric_receipt_still_fails_git_parent_review_gate(self):
        d=self.data();d['checklists'][0]['items'][4]['done']=True;old_id=d['last_evidence_review']['review_id'];self.snapshot(d,'fixture-forged-observation');d['last_evidence_review']['review_id']=old_id;self.save(d)
        p=self.root/u.STATE;state=json.loads(p.read_text());state['reviewed_stage_sha256']=u.stage_digest(d);state['recorded_observation_hashes']=[u.digest(o) for o in d['observations']];p.write_text(json.dumps(state)+'\n');self.git('add','.');self.git('commit','-qm','forged review fixture')
        with self.assertRaisesRegex(u.Invalid,'without a new evidence review identifier'):u.run(self.root,False,refresh=self.git('rev-parse','HEAD'))
    def test_42_git_parent_rejects_forged_history_receipt(self):
        d=self.data();d['observations'][0]['note']='Forged old fixture';self.snapshot(d);self.save(d)
        p=self.root/u.STATE;state=json.loads(p.read_text());state['recorded_observation_hashes']=[u.digest(o) for o in d['observations']];p.write_text(json.dumps(state)+'\n');self.git('add','.');self.git('commit','-qm','forged history fixture')
        with self.assertRaisesRegex(u.Invalid,'append-only'):u.run(self.root,False,refresh=self.git('rev-parse','HEAD'))
    def test_43_invalid_validation_counts_and_empty_denominator_refused(self):
        for passed,total in [(70,69),(-1,69),(True,69),(0,0)]:
            d=self.data();d['validation_runs'][0].update(passed=passed,total=total);self.save(d)
            with self.assertRaisesRegex(u.Invalid,'invalid validation count'):u.run(self.root,False)
    def test_44_missing_numeric_receipts_refused(self):
        p=self.root/u.STATE;state=json.loads(p.read_text());del state['recorded_observation_hashes'];p.write_text(json.dumps(state))
        with self.assertRaisesRegex(u.Invalid,'prior observation history'):u.run(self.root,False)
    def test_45_chart_default_has_counts_axis_and_no_square_grid(self):
        readme=(self.root/'README.md').read_text();svg=(self.root/'docs/status/visuals/progress-dashboard.svg').read_text()
        self.assertIn('progress-dashboard.svg',readme);self.assertNotIn('🟦',readme)
        for value in ('4 / 7','57.1%','2 / 4','50%','3 / 4','75%','0 / 4','0 / 1','100%','remaining'):self.assertIn(value,svg)
        for c in self.data()['checklists']:self.assertIn(u.delta_label(self.data(),c),svg)
        self.assertIn('game/code/effort finished',svg)
    def test_46_numeric_observation_review_identity_must_match(self):
        original=self.data()
        for key,value in [('review_id','fixture-mismatch'),('date','2026-10-24'),('basis_commit','0'*40)]:
            d=copy.deepcopy(original);d['observations'][-1][key]=value;self.save(d)
            with self.assertRaisesRegex(u.Invalid,'match the evidence review'):u.run(self.root,False)
    def test_47_plain_ids_and_historical_versions_are_validated(self):
        original=self.data()
        for field in ('checklist','criterion','historical-version'):
            d=copy.deepcopy(original)
            if field=='checklist':d['checklists'][0]['id']='[unsafe]'
            elif field=='criterion':d['checklists'][0]['items'][0]['id']='bad id'
            else:d['observations'][0]['checklists'][0]['version']=True
            self.save(d)
            with self.assertRaisesRegex(u.Invalid,'invalid plain identifier|invalid observed checklist version'):u.run(self.root,False)
    def test_48_multiple_inserted_observations_cannot_fabricate_delta(self):
        d=self.data();self.snapshot(d,'fixture-unbound-middle');d['observations'][-1]['checklists'][0]['completed_ids']=[];self.snapshot(d,'fixture-final-review');self.save(d);before=self.hashes()
        with self.assertRaisesRegex(u.Invalid,'only one new numeric observation'):u.run(self.root,False)
        self.assertEqual(before,self.hashes())
        p=self.root/u.STATE;state=json.loads(p.read_text());state['recorded_observation_hashes']=[u.digest(o) for o in d['observations']];state['reviewed_stage_sha256']=u.stage_digest(d);p.write_text(json.dumps(state)+'\n');self.git('add','.');self.git('commit','-qm','fabricated middle observation fixture')
        with self.assertRaisesRegex(u.Invalid,'only one new numeric observation'):u.run(self.root,False,refresh=self.git('rev-parse','HEAD'))
    def test_49_new_review_without_new_acceptance_has_zero_delta(self):
        d=self.data();self.snapshot(d);self.save(d);u.run(self.root,False)
        self.assertEqual(u.delta_label(d,d['checklists'][0]),'Δ +0 goals')
    def test_50_overall_is_its_own_named_milestone_count(self):
        d=self.data();road=next(c for c in d['checklists'] if c['id']=='roadmap');self.assertEqual(u.numbers(road),(5,20,25.0))
        d['checklists'][0]['items'][4]['done']=True;self.snapshot(d);self.save(d);u.run(self.root,False)
        self.assertEqual(u.numbers(road),(5,20,25.0));self.assertIn('5 / 20 milestones accepted',(self.root/'docs/status/visuals/progress-dashboard.svg').read_text())
    def test_51_overall_advance_requires_review_and_updates_only_its_count(self):
        d=self.data();road=next(c for c in d['checklists'] if c['id']=='roadmap');road['items'][5]['done']=True;self.snapshot(d);self.save(d);u.run(self.root,False)
        self.assertEqual(u.numbers(road),(6,20,30.0));self.assertEqual(u.numbers(d['checklists'][0]),(4,7,57.1))
        svg=(self.root/'docs/status/visuals/progress-dashboard.svg').read_text();self.assertIn('5 bounded foundations accepted; 14 production goals remain',svg)
    def test_52_overall_unreviewed_change_and_definition_edit_refused(self):
        original=self.data();d=copy.deepcopy(original);road=next(c for c in d['checklists'] if c['id']=='roadmap');road['items'][5]['done']=True;self.save(d)
        with self.assertRaisesRegex(u.Invalid,'matching recorded observation'):u.run(self.root,False)
        d=copy.deepcopy(original);road=next(c for c in d['checklists'] if c['id']=='roadmap');road['items'][5]['phase']='foundation';self.snapshot(d);self.save(d)
        with self.assertRaisesRegex(u.Invalid,'new checklist version'):u.run(self.root,False)
    def test_53_unknown_layout_id_refused_before_render(self):
        d=self.data();d['checklists'][0]['id']='other';d['observations'][-1]['checklists'][0]['id']='other';self.save(d)
        with self.assertRaisesRegex(u.Invalid,'fixed reviewed checklist IDs'):u.run(self.root,False)

    def test_54_baseline_then_second_zero_delta_preserves_exact_history(self):
        # Owned synthetic fixture bootstrap only; never rewrite the public record.
        d=self.data();d['observations']=[];self.snapshot(d,'fixture-zero-baseline');self.save(d)
        p=self.root/u.STATE;state=json.loads(p.read_text())
        state.update(reviewed_stage_sha256=u.stage_digest(d),evidence_review_id=d['last_evidence_review']['review_id'],evidence_review_date=d['last_evidence_review']['date'],reviewed_checklist_definitions=u.definitions(d),recorded_observation_hashes=[u.digest(o) for o in d['observations']]);p.write_text(json.dumps(state)+'\n')
        u.run(self.root,False);u.run(self.root,True)
        baseline=copy.deepcopy(d['observations']);counts=[u.numbers(c) for c in d['checklists']]
        for c in d['checklists']:self.assertEqual(u.delta_label(d,c),'Δ — first record')
        self.assertIn('FIRST NUMERIC BASELINE',(self.root/'docs/status/visuals/progress-dashboard.svg').read_text())
        self.git('add','.');self.git('commit','-qm','synthetic zero baseline')
        self.snapshot(d,'fixture-second-zero-review');self.save(d)
        self.git('add','.');self.git('commit','-qm','synthetic second unchanged acceptance')
        u.run(self.root,False,refresh=self.git('rev-parse','HEAD'));u.run(self.root,True)
        self.assertEqual(self.data()['observations'][:-1],baseline)
        self.assertEqual(len(self.data()['observations']),len(baseline)+1)
        self.assertEqual([u.numbers(c) for c in self.data()['checklists']],counts)
        for c in d['checklists']:self.assertEqual(u.delta_label(d,c),'Δ +0 goals')
        svg=(self.root/'docs/status/visuals/progress-dashboard.svg').read_text()
        self.assertIn('CHANGES COMPARED WITH THE PREVIOUS RECORDED REVIEW',svg)
        self.assertNotIn('FIRST NUMERIC BASELINE',svg);self.assertNotIn('first record',svg)
        self.assertEqual(svg.count('Δ +0 goals'),len(d['checklists']))

    def test_55_legitimate_plus_one_review_uses_real_git_parent(self):
        d=self.data();prior=copy.deepcopy(d['observations'])
        self.assertFalse(d['checklists'][0]['items'][4]['done'])
        d['checklists'][0]['items'][4]['done']=True
        self.snapshot(d,'fixture-accepted-plus-one');self.save(d)
        self.git('add','.');self.git('commit','-qm','synthetic accepted plus-one review')
        u.run(self.root,False,refresh=self.git('rev-parse','HEAD'));u.run(self.root,True)
        self.assertEqual(self.data()['observations'][:-1],prior)
        self.assertEqual(len(self.data()['observations']),len(prior)+1)
        self.assertEqual(u.numbers(d['checklists'][0]),(5,7,71.4))
        self.assertEqual(u.delta_label(d,d['checklists'][0]),'Δ +1 goals')
        svg=(self.root/'docs/status/visuals/progress-dashboard.svg').read_text()
        self.assertIn('5 / 7',svg);self.assertIn('71.4%',svg)
        self.assertEqual(svg.count('Δ +1 goals'),1)
        self.assertEqual(svg.count('Δ +0 goals'),5)
        self.assertTrue(set(guard.check(self.root))<=set(u.OUTPUTS))

    def test_56_build_plan_state_digest_requires_new_review(self):
        d=self.data();self.save(d);u.run(self.root,False)
        state=json.loads((self.root/u.STATE).read_text());state['reviewed_build_plan_sha256']='0'*64
        (self.root/u.STATE).write_text(json.dumps(state))
        with self.assertRaisesRegex(u.Invalid,'changed build-plan mapping requires a new evidence review identifier'):u.run(self.root,False)

class BuildPlanValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        (self.root/'tasks.md').write_text('## SI-01: First fixture task\n\n**Dependencies:** None.\n\n## SI-02: Second fixture task\n\n**Dependencies:** SI-01.\n')
        (self.root/'evidence.md').write_text('# Owned synthetic evidence\n')
        self.data={'last_evidence_review':{'date':'2026-01-01'},'updates':[{'id':'fixture-check','changed':'Owned synthetic interaction passed.','evidence':['evidence.md']}],
            'build_plan':{'schema_version':1,'reviewed_at':'2026-01-01 01:00:00 UTC','plan_source':'tasks.md',
                'tasks':[{'id':'si-01','label':'First fixture task','state':'planned','dependencies':[],'source':'tasks.md#si-01','state_reason':'Proposal only.','evidence':[]},
                         {'id':'si-02','label':'Second fixture task','state':'planned','dependencies':['si-01'],'source':'tasks.md#si-02','state_reason':'Proposal only.','evidence':[]}],
                'checks':[{'id':'bounded-check','label':'Bounded fixture check','state':'tested','update_id':'fixture-check','limit':'Only synthetic fixture coverage.'}]}}
    def test_build_plan_matches_source_without_reading_checkbox_completion(self):
        with (self.root/'tasks.md').open('a') as f:f.write('\n- [x] An irrelevant checkbox is not evidence.\n')
        u.validate_build_plan(self.root,self.data)
        self.assertTrue(all(t['state']=='planned' for t in self.data['build_plan']['tasks']))
    def test_build_plan_rejects_dependency_drift_and_missing_task(self):
        for change in (lambda d:d['build_plan']['tasks'][1].update(dependencies=[]),lambda d:d['build_plan']['tasks'].pop()):
            d=copy.deepcopy(self.data);change(d)
            with self.assertRaises(u.Invalid):u.validate_build_plan(self.root,d)
    def test_build_plan_rejects_state_promotion_without_evidence(self):
        d=copy.deepcopy(self.data);d['build_plan']['tasks'][0]['state']='implemented'
        with self.assertRaisesRegex(u.Invalid,'requires evidence'):u.validate_build_plan(self.root,d)
    def test_build_plan_rejects_missing_build_evidence(self):
        d=copy.deepcopy(self.data);d['build_plan']['checks'][0]['update_id']='not-recorded'
        with self.assertRaisesRegex(u.Invalid,'requires cited update'):u.validate_build_plan(self.root,d)
    def test_build_plan_rejects_cycles_even_when_source_defines_them(self):
        (self.root/'tasks.md').write_text('## SI-01: First\n**Dependencies:** SI-02.\n## SI-02: Second\n**Dependencies:** SI-01.\n')
        self.data['build_plan']['tasks'][0]['dependencies']=['si-02']
        with self.assertRaisesRegex(u.Invalid,'cycle'):u.validate_build_plan(self.root,self.data)
    def test_build_plan_rejects_wrong_review_day(self):
        self.data['build_plan']['reviewed_at']='2026-01-02 01:00:00 UTC'
        with self.assertRaisesRegex(u.Invalid,'date mismatch'):u.validate_build_plan(self.root,self.data)
    def test_build_plan_ledger_does_not_change_acceptance(self):
        before=copy.deepcopy(self.data);text='\n'.join(u.build_plan_ledger(self.data))
        self.assertIn('First fixture task',text);self.assertIn('Separate from historical acceptance',text)
        self.assertNotIn('%',text);self.assertEqual(self.data,before)

    def test_build_plan_ledger_localizes_display_only(self):
        before=copy.deepcopy(self.data)
        rendered='\n'.join(u.build_plan_ledger(self.data))
        self.assertIn('**Map reviewed:** December 31, 2025, 6:00:00 PM Arizona \\(MST\\).',rendered)
        self.assertEqual(self.data,before)
        u.validate_build_plan(self.root,self.data)
        self.data['build_plan']['reviewed_at']='December 31, 2025, 6:00:00 PM Arizona (MST)'
        with self.assertRaisesRegex(u.Invalid,'invalid build-plan review time'):
            u.validate_build_plan(self.root,self.data)

class ReviewTimeFormattingTests(unittest.TestCase):
    def test_arizona_review_time_boundaries(self):
        cases=(
            ('2026-10-28 17:51:53 UTC','October 28, 2026, 10:51:53 AM Arizona (MST)'),
            ('2026-10-28 07:00:00 UTC','October 28, 2026, 12:00:00 AM Arizona (MST)'),
            ('2026-10-28 19:00:00 UTC','October 28, 2026, 12:00:00 PM Arizona (MST)'),
            ('2026-10-28 06:59:59 UTC','October 27, 2026, 11:59:59 PM Arizona (MST)'),
            ('2026-01-01 06:59:59 UTC','December 31, 2025, 11:59:59 PM Arizona (MST)'),
            ('2024-03-01 06:30:00 UTC','February 29, 2024, 11:30:00 PM Arizona (MST)'),
            ('2026-07-01 19:00:00 UTC','July 1, 2026, 12:00:00 PM Arizona (MST)'),
            ('2026-01-01 19:00:00 UTC','January 1, 2026, 12:00:00 PM Arizona (MST)'),
        )
        for value,expected in cases:
            with self.subTest(value=value):
                self.assertEqual(u.format_review_time(value),expected)

    def test_arizona_review_time_rejects_noncanonical_or_invalid_dates(self):
        for value in (None,{},'', '2026-02-30 12:00:00 UTC','2026-13-01 12:00:00 UTC',
                      '2026-10-28 24:00:00 UTC','2026-10-28T17:51:53Z',
                      'October 28, 2026, 10:51:53 AM Arizona (MST)'):
            with self.subTest(value=value):
                with self.assertRaises(u.Invalid):u.format_review_time(value)

    def test_arizona_review_time_ignores_host_timezone(self):
        code=('import sys;sys.path.insert(0,'+repr(str(Path(u.__file__).parent))+');'
              'import update_tracker as u;print(u.format_review_time("2026-10-28 17:51:53 UTC"))')
        for zone in ('UTC','Asia/Tokyo','America/New_York'):
            with self.subTest(zone=zone):
                actual=subprocess.check_output([sys.executable,'-B','-c',code],
                                              env={**os.environ,'TZ':zone},text=True)
                self.assertEqual(actual.strip(),'October 28, 2026, 10:51:53 AM Arizona (MST)')

class CurrentDatasetTests(unittest.TestCase):
    def test_current_reviewed_data_renders_without_drift_or_mutation(self):
        # Deliberately separate from the synthetic mutation fixture. This reads
        # the real current dataset, whatever its counts/versions/history are.
        paths=(*u.OUTPUTS,u.DATA)
        before={p:(u.ROOT/p).read_bytes() for p in paths}
        self.assertEqual(u.run(u.ROOT,True),[])
        data=json.loads(before[u.DATA]);svg=before['docs/status/visuals/progress-dashboard.svg'].decode()
        for c in data['checklists']:
            accepted=sum(i['done'] for i in c['items']);total=len(c['items'])
            self.assertIn(f'{accepted} / {total}',svg)
            self.assertIn(f'{round(100*accepted/total,1):g}%',svg)
            self.assertIn(u.delta_label(data,c),svg)
        self.assertEqual(before,{p:(u.ROOT/p).read_bytes() for p in paths})

if __name__=='__main__':unittest.main()
