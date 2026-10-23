"""Offline artifact checks. These are not browser screenshots or UI acceptance."""
import base64
import hashlib
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

WEB = Path(__file__).resolve().parents[1]
ROOT = WEB.parents[1]
spec = importlib.util.spec_from_file_location('site_build', WEB / 'build_site.py')
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)

class Tags(HTMLParser):
    def __init__(self):
        super().__init__(); self.tags=[]; self.script=[]; self.style=[]; self.current=None
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag,dict(attrs)))
        if tag in ('script','style'): self.current=tag
    def handle_endtag(self, tag):
        if tag==self.current: self.current=None
    def handle_data(self, value):
        if self.current=='script': self.script.append(value)
        if self.current=='style': self.style.append(value)

class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='rockman-web-fixture-'); self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name); self.source=self.base/'repo'; (self.source/'docs/web').mkdir(parents=True); (self.source/'docs/status').mkdir()
        for name in site.ASSETS: shutil.copy2(WEB/name,self.source/'docs/web'/name)
        for name in site.DATA: shutil.copy2(ROOT/'docs/status'/name,self.source/'docs/status'/name)
        self.output=self.base/'artifact'; self.preview=self.base/'preview.html'
    def build(self): return site.build(self.source,self.output,self.preview,'a'*40)
    def test_exact_artifact_allowlist_and_byte_identical_data(self):
        manifest=self.build()
        self.assertEqual(set(p.relative_to(self.output).as_posix() for p in self.output.rglob('*') if p.is_file()),set(site.ASSETS)|{'data/'+n for n in site.DATA}|{'build-manifest.json'})
        for name,sha in manifest['files'].items(): self.assertEqual(hashlib.sha256((self.output/name).read_bytes()).hexdigest(),sha)
        for name in site.DATA: self.assertEqual((self.output/'data'/name).read_bytes(),(self.source/'docs/status'/name).read_bytes())
    def test_existing_output_is_never_replaced(self):
        self.output.mkdir(); (self.output/'keep').write_text('preserve')
        with self.assertRaisesRegex(ValueError,'new path'): self.build()
        self.assertEqual((self.output/'keep').read_text(),'preserve')
    def test_existing_preview_is_never_replaced(self):
        self.preview.write_text('preserve')
        with self.assertRaisesRegex(ValueError,'new path'): self.build()
        self.assertFalse(self.output.exists())
    def test_no_source_output_even_with_parent_traversal(self):
        with self.assertRaisesRegex(ValueError,'outside'): site.build(self.source,self.base/'x/../repo/generated')
        self.assertFalse((self.source/'generated').exists())
    def test_output_symlink_ancestor_rejected(self):
        (self.base/'alias').symlink_to(self.base,target_is_directory=True)
        with self.assertRaisesRegex(ValueError,'symlinks'): site.build(self.source,self.base/'alias/new')
    def test_source_symlink_rejected(self):
        p=self.source/'docs/web/styles.css'; p.unlink(); p.symlink_to(WEB/'styles.css')
        with self.assertRaisesRegex(ValueError,'symlinks'): self.build()
        self.assertFalse(self.output.exists())
    def test_preview_cannot_join_production_artifact(self):
        with self.assertRaisesRegex(ValueError,'separate'): site.build(self.source,self.output,self.output/'preview.html')
    def test_output_cannot_be_inside_preview_file_path(self):
        with self.assertRaisesRegex(ValueError,'separate'): site.build(self.source,self.preview/'site',self.preview)
        self.assertFalse(self.preview.exists())
    def test_checksum_mismatch_does_not_create_output(self):
        with (self.source/'docs/status/dashboard-data.json').open('a') as f: f.write(' ')
        with self.assertRaisesRegex(ValueError,'disagree'): self.build()
        self.assertFalse(self.output.exists())
    def test_receipt_review_mismatch_rejected(self):
        p=self.source/'docs/status/tracker-state.json'; d=json.loads(p.read_text());d['evidence_review_id']='old';p.write_text(json.dumps(d))
        with self.assertRaisesRegex(ValueError,'attestation'): self.build()
    def test_source_revision_must_be_exact_commit(self):
        with self.assertRaisesRegex(ValueError,'40-character'): site.build(self.source,self.output,revision='main')
        self.assertFalse(self.output.exists())
    def test_standalone_has_no_external_dependency_and_exact_csp_hashes(self):
        self.build(); html=self.preview.read_text(); tags=Tags();tags.feed(html)
        self.assertEqual(len([t for t,a in tags.tags if t=='script']),1)
        self.assertEqual(len([t for t,a in tags.tags if t=='style']),1)
        for tag,attrs in tags.tags:
            self.assertNotIn('src',attrs)
            self.assertFalse(tag=='link' and attrs.get('rel')=='stylesheet')
        self.assertNotIn('@import',html)
        self.assertIn('LOCAL PREVIEW · SNAPSHOT, NOT LIVE',html)
        self.assertIn("sourceRevision:'"+'a'*40+"'",html)
        policy=next(a['content'] for t,a in tags.tags if t=='meta' and a.get('http-equiv')=='Content-Security-Policy')
        self.assertIn("connect-src 'none'",policy)
        for body in (''.join(tags.script),''.join(tags.style)):
            sha=base64.b64encode(hashlib.sha256(body.encode()).digest()).decode();self.assertIn("'sha256-"+sha+"'",policy)
        script=self.base/'bundle.mjs';script.write_text(''.join(tags.script));subprocess.run(['node','--check',str(script)],check=True,capture_output=True)
    def test_closing_script_sequences_in_data_cannot_escape(self):
        raw,receipt,data,state=site.read_snapshot(self.source); data['findings'][0]['title']='</script><script>alert(1)</script>\u2028'
        html=site.standalone(self.source/'docs/web',data,state); tags=Tags();tags.feed(html)
        self.assertEqual(len([t for t,a in tags.tags if t=='script']),1)
        self.assertIn('\\u003c/script>',html); self.assertIn('\\u2028',html)
    def test_production_assets_unmodified_by_preview(self):
        before={n:(self.source/'docs/web'/n).read_bytes() for n in site.ASSETS};self.build()
        self.assertEqual(before,{n:(self.output/n).read_bytes() for n in site.ASSETS})
        self.assertNotIn(b'PREVIEW_SNAPSHOT',(self.output/'app.mjs').read_bytes())

if __name__=='__main__': unittest.main(verbosity=2)
