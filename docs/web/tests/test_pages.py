"""Offline Pages artifact/sequence controls. Never deploy or use network origins."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

WEB = Path(__file__).resolve().parents[1]
ROOT = WEB.parents[1]
spec = importlib.util.spec_from_file_location('site_build', WEB/'build_site.py')
builder = importlib.util.module_from_spec(spec); spec.loader.exec_module(builder)
# Local sibling import only; no dependencies or downloads.
import sys
sys.path.insert(0, str(WEB))
from check_site import check

WORKFLOW = ROOT/'.github/workflows/update-progress.yml'

def job_text(name):
    text = WORKFLOW.read_text()
    start = text.index('\n  '+name+':\n')
    stop = text.find('\n  ',start+3)
    # Job headers have exactly two spaces, unlike nested fields.
    import re
    match = re.search(r'\n  [a-z][a-z-]*:\n',text[start+3:])
    return text[start:] if match is None else text[start:start+3+match.start()]

def current_shell():
    text=job_text('deploy-site')
    block=text.split('        run: |\n',1)[1].split('      - name:',1)[0]
    return '\n'.join(line[10:] for line in block.splitlines())+'\n'

class PagesChecks(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='rockman-pages-fixture-'); self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name)
    def artifact(self):
        output=self.base/'site';builder.build(ROOT,output,revision='a'*40);return output
    def test_exact_artifact_and_revision(self):
        output=self.artifact();self.assertEqual(check(output,'a'*40)['source_revision'],'a'*40)
        with self.assertRaisesRegex(ValueError,'revision mismatch'):check(output,'b'*40)
    def test_unlisted_private_path_fails_before_upload(self):
        output=self.artifact();(output/'unexpected.txt').write_text('synthetic fixture')
        with self.assertRaisesRegex(ValueError,'fixed public file list'):check(output,'a'*40)
    def test_empty_extra_directory_is_also_refused(self):
        output=self.artifact();(output/'extra').mkdir()
        with self.assertRaisesRegex(ValueError,'directory'):check(output,'a'*40)
    def test_symlink_and_hardlink_are_not_pages_inputs(self):
        for kind in ['symbolic','hard']:
            with self.subTest(kind=kind):
                output=self.base/kind;builder.build(ROOT,output,revision='a'*40);target=output/'styles.css';original=self.base/(kind+'.css');target.rename(original)
                if kind=='symbolic':target.symlink_to(original)
                else:os.link(original,target)
                with self.assertRaisesRegex(ValueError,'symlink|unlinked'):check(output,'a'*40)
    def test_byte_tamper_or_manifest_extra_path_refused(self):
        output=self.artifact();(output/'app.mjs').write_text('/* modified fixture */')
        with self.assertRaisesRegex(ValueError,'byte mismatch'):check(output,'a'*40)
        manifest=json.loads((output/'build-manifest.json').read_text());manifest['files']['private.bin']='b'*64;(output/'build-manifest.json').write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError,'file list mismatch'):check(output,'a'*40)
    def test_workflow_permissions_are_job_local_and_narrow(self):
        text=WORKFLOW.read_text();update=job_text('update');build=job_text('build-site');deploy=job_text('deploy-site')
        self.assertIn('branches: [main]',text);self.assertNotIn('workflow_dispatch',text);self.assertNotIn('pull_request',text)
        self.assertEqual(text.count('contents: write'),1);self.assertIn('contents: write',update)
        self.assertNotIn('pages: write',build);self.assertNotIn('id-token: write',build)
        self.assertIn('pages: write',deploy);self.assertIn('id-token: write',deploy);self.assertNotIn('contents: write',deploy)
        self.assertIn('needs: update',build);self.assertIn('needs: build-site',deploy)
        self.assertIn("if: needs.update.outputs.snapshot != ''",build);self.assertIn("if: needs.build-site.outputs.snapshot != ''",deploy)
        self.assertNotIn('configure-pages',text);self.assertNotIn('enablement:',text);self.assertNotIn('secrets.',text)
    def test_updater_exports_only_successful_noop_or_verified_push(self):
        text=job_text('update');self.assertEqual(text.count('>> "$GITHUB_OUTPUT"'),2)
        self.assertIn('snapshot=$TRIGGER_SHA',text)
        self.assertIn('test "$(git ls-remote --exit-code origin refs/heads/main | cut -f1)" = "$(git rev-parse HEAD)"\n          echo "snapshot=$(git rev-parse HEAD)"',text)
        self.assertIn('cancel-in-progress: false',WORKFLOW.read_text());self.assertNotIn('--force',text)
    def test_official_actions_are_exactly_pinned(self):
        import re
        uses=re.findall(r'uses: ([^\s]+)',WORKFLOW.read_text())
        self.assertEqual(set(uses),{'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683','actions/upload-pages-artifact@7b1f4a764d45c48632c6b24a0339c27f5614fb0b','actions/deploy-pages@d6db90164ac5ed86f2b6aed7e0febac5b3c0c03e'})
    def test_build_checks_exact_snapshot_and_fixed_artifact_before_upload(self):
        text=job_text('build-site');self.assertIn('ref: ${{ needs.update.outputs.snapshot }}',text)
        self.assertIn('persist-credentials: false',text);self.assertIn('docs/status/tools/update_tracker.py --check',text)
        self.assertLess(text.index('docs/web/check_site.py'),text.index('uses: actions/upload-pages-artifact'))
        self.assertIn('path: ${{ runner.temp }}/rockman-site',text);self.assertNotIn('preview-html',text)
    def run_current(self,current,exit_code=0):
        bin=self.base/'bin';bin.mkdir(exist_ok=True);gh=bin/'gh';gh.write_text('#!/bin/sh\nprintf "%s\\n" "$FAKE_HEAD"\nexit "$FAKE_EXIT"\n');gh.chmod(0o700)
        output=self.base/'output';env={**os.environ,'PATH':str(bin)+os.pathsep+os.environ['PATH'],'SNAPSHOT_SHA':'a'*40,'REPOSITORY':'fixture/repo','GH_TOKEN':'synthetic-not-a-credential','FAKE_HEAD':current,'FAKE_EXIT':str(exit_code),'GITHUB_OUTPUT':str(output)}
        result=subprocess.run(['bash','-c',current_shell()],env=env,capture_output=True,text=True)
        return result,output.read_text() if output.exists() else ''
    def test_exact_deploy_gate_shell_accepts_current_snapshot(self):
        result,output=self.run_current('a'*40);self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(output,'ready=true\n')
    def test_exact_deploy_gate_shell_skips_superseded_snapshot(self):
        result,output=self.run_current('b'*40);self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(output,'')
    def test_exact_deploy_gate_shell_refuses_api_failure(self):
        result,output=self.run_current('',1);self.assertNotEqual(result.returncode,0);self.assertEqual(output,'')

    def git_fixture(self):
        repo=self.base/'repo'; shutil.copytree(ROOT,repo,ignore=shutil.ignore_patterns('.git','__pycache__'))
        def git(*args,input=None):
            return subprocess.run(['git',*args],cwd=repo,input=input,capture_output=True,text=True,check=True).stdout.strip()
        git('init','-q','-b','main');git('config','user.name','Synthetic fixture');git('config','user.email','fixture@example.invalid')
        git('add','.');git('commit','-qm','synthetic initial public fixture');git('commit','--allow-empty','-qm','synthetic documentation activity')
        bare=self.base/'origin.git';subprocess.run(['git','init','--bare','-q',str(bare)],check=True)
        git('remote','add','origin',str(bare));git('push','-q','origin','HEAD:refs/heads/main');trigger=git('rev-parse','HEAD')
        subprocess.run([sys.executable,'-B','docs/status/tools/update_tracker.py','--write','--refresh-activity',trigger],cwd=repo,check=True,capture_output=True)
        text=job_text('update').split('      - name: Commit only generated documentation if the triggering head is still current',1)[1].split('        run: |\n',1)[1]
        shell='\n'.join(line[10:] for line in text.splitlines())+'\n'
        def publish(sha):
            output=self.base/'publish-output'
            if output.exists(): output.unlink()
            env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','TRIGGER_SHA':sha,'GH_TOKEN':'synthetic-not-a-credential','GITHUB_OUTPUT':str(output)}
            result=subprocess.run(['bash','-c',shell],cwd=repo,env=env,capture_output=True,text=True)
            return result,output.read_text() if output.exists() else ''
        return git,publish,trigger
    def test_exact_updater_shell_exports_verified_generated_child(self):
        git,publish,trigger=self.git_fixture();result,output=publish(trigger)
        self.assertEqual(result.returncode,0,result.stderr);head=git('rev-parse','HEAD');self.assertNotEqual(head,trigger)
        self.assertEqual(git('rev-parse','HEAD^'),trigger);self.assertEqual(output,'snapshot='+head+'\n')
        self.assertEqual(git('ls-remote','origin','refs/heads/main').split()[0],head)
        self.assertEqual(git('status','--porcelain'),'')
    def test_exact_updater_shell_exports_current_noop(self):
        git,publish,trigger=self.git_fixture();first,_=publish(trigger);self.assertEqual(first.returncode,0,first.stderr)
        current=git('rev-parse','HEAD');result,output=publish(current)
        self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(output,'snapshot='+current+'\n');self.assertEqual(git('rev-parse','HEAD'),current)
    def test_exact_updater_shell_exports_nothing_when_superseded(self):
        git,publish,trigger=self.git_fixture();new=git('commit-tree','HEAD^{tree}','-p',trigger,input='synthetic newer update\n');git('push','-q','origin',new+':refs/heads/main')
        result,output=publish(trigger);self.assertEqual(result.returncode,0,result.stderr);self.assertEqual(output,'')
        self.assertEqual(git('ls-remote','origin','refs/heads/main').split()[0],new);self.assertEqual(git('rev-parse','HEAD'),trigger)

if __name__=='__main__':unittest.main(verbosity=2)
