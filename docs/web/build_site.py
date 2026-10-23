#!/usr/bin/env python3
"""Build the read-only documentation site; no network, server or deployment."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import re

ASSETS = ('index.html', 'styles.css', 'model.mjs', 'views.mjs', 'app.mjs')
DATA = ('dashboard-data.json', 'tracker-state.json')

def sha256(raw):
    return hashlib.sha256(raw).hexdigest()

def read_snapshot(root):
    status = root / 'docs/status'
    raw = (status / DATA[0]).read_bytes()
    receipt = (status / DATA[1]).read_bytes()
    data, state = json.loads(raw), json.loads(receipt)
    if sha256(raw) != state.get('evidence_data_sha256'):
        raise ValueError('Evidence JSON and generated receipt disagree; regenerate/check the canonical tracker first.')
    review = data['last_evidence_review']
    if state.get('evidence_review_id') != review['review_id'] or state.get('evidence_review_date') != review['date']:
        raise ValueError('Evidence review and receipt attestation disagree.')
    return raw, receipt, data, state

def check_destination(target, source):
    target = Path(target).absolute()
    # A build writes only a fresh output tree, never merges into or removes a tree.
    if target.is_symlink() or target.exists():
        raise ValueError('Output must be a new path; existing files/directories are never replaced.')
    for parent in target.parents:
        if parent.is_symlink():
            raise ValueError('Output ancestors must not be symlinks.')
    target = target.resolve(strict=False)
    if target.is_relative_to(source.resolve()):
        raise ValueError('Build output must stay outside the repository source tree.')
    return target

def standalone(web, data, state, revision=None):
    css = (web / 'styles.css').read_text()
    parts = []
    for name in ('model.mjs', 'views.mjs', 'app.mjs'):
        code = (web / name).read_text()
        code = re.sub(r'^import .*?;\n', '', code, flags=re.M)
        code = re.sub(r'^export ', '', code, flags=re.M)
        code = code.replace("if(typeof document!=='undefined')startApp(document,window);", '')
        parts.append(code)
    snapshot = json.dumps({'data': data, 'state': state}, ensure_ascii=False, separators=(',', ':'))
    snapshot = snapshot.replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    script = '\n'.join(parts) + '\nconst PREVIEW_SNAPSHOT=' + snapshot + ';\n'
    script += "startApp(document,window,async()=>({data:validateData(PREVIEW_SNAPSHOT.data,PREVIEW_SNAPSHOT.state),state:PREVIEW_SNAPSHOT.state}),{preview:true,sourceRevision:'" + (revision or '') + "'});\n"
    digest = lambda s: base64.b64encode(hashlib.sha256(s.encode()).digest()).decode()
    policy = "default-src 'none'; script-src 'sha256-" + digest(script) + "'; style-src 'sha256-" + digest(css) + "'; connect-src 'none'; img-src 'none'; base-uri 'none'; form-action 'none'; object-src 'none'"
    html = (web / 'index.html').read_text()
    html = re.sub(r'<meta http-equiv="Content-Security-Policy" content="[^"]+">', '<meta http-equiv="Content-Security-Policy" content="' + policy + '">', html)
    html = html.replace('<link rel="stylesheet" href="./styles.css">', '<style>' + css + '</style>')
    html = html.replace('<script type="module" src="./app.mjs"></script>', '')
    html = html.replace('</body>', '<script type="module">' + script + '</script>\n</body>')
    return html

def build(root, output, preview=None, revision=None):
    root = Path(root).resolve()
    web = root / 'docs/web'
    output = check_destination(output, root)
    preview = check_destination(preview, root) if preview else None
    if preview and (preview == output or preview.is_relative_to(output) or output.is_relative_to(preview)):
        raise ValueError('Private standalone preview must be separate from the production artifact.')
    if revision is not None and not re.fullmatch(r'[0-9a-f]{40}', revision):
        raise ValueError('Source revision must be an exact 40-character Git commit.')
    for relative in ['docs/web/' + name for name in ASSETS] + ['docs/status/' + name for name in DATA]:
        source = root / relative
        if not source.is_file() or source.is_symlink() or any(parent.is_symlink() for parent in source.parents if parent != root):
            raise ValueError('Build sources must be regular repository files, not symlinks.')
    raw, receipt, data, state = read_snapshot(root)
    contents = {name: (web / name).read_bytes() for name in ASSETS}
    contents.update({'data/' + DATA[0]: raw, 'data/' + DATA[1]: receipt})
    manifest = {'schema_version': 1, 'source_revision': revision, 'evidence_review_id': data['last_evidence_review']['review_id'], 'files': {name: sha256(value) for name, value in contents.items()}}
    preview_html = standalone(web, data, state, revision) if preview else None
    output.mkdir(parents=True)
    for name, value in contents.items():
        dest = output / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(value)
    (output / 'build-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    if preview:
        preview.parent.mkdir(parents=True, exist_ok=True)
        preview.write_text(preview_html)
    return manifest

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--preview-html', type=Path, help='Optional private single-file preview; never part of the production artifact.')
    parser.add_argument('--source-revision')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    print(json.dumps(build(root, args.output, args.preview_html, args.source_revision), indent=2))

if __name__ == '__main__':
    main()
