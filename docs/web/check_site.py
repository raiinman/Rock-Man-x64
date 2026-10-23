#!/usr/bin/env python3
"""Fail closed on any extra path or mismatched byte in the public site artifact."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from build_site import ASSETS, DATA

FILES = set(ASSETS) | {'data/' + name for name in DATA} | {'build-manifest.json'}

def need(condition, message):
    if not condition:
        raise ValueError(message)

def check(path, revision):
    path = Path(path)
    need(re.fullmatch(r'[0-9a-f]{40}', revision) is not None, 'Exact source revision required.')
    need(path.is_dir() and not path.is_symlink(), 'Artifact root must be a real directory.')
    found = set()
    total_bytes = 0
    for target in path.rglob('*'):
        relative = target.relative_to(path).as_posix()
        need(not target.is_symlink(), 'Artifact symlink refused.')
        if target.is_dir():
            need(relative == 'data', 'Unexpected artifact directory.')
        else:
            need(target.is_file() and target.stat().st_nlink == 1, 'Artifact entries must be ordinary unlinked files.')
            found.add(relative)
            total_bytes += target.stat().st_size
    need(found == FILES, 'Artifact must contain exactly the fixed public file list.')
    need(total_bytes <= 2 * 1024 * 1024, 'Documentation artifact exceeds its bounded size.')
    manifest = json.loads((path / 'build-manifest.json').read_text())
    need(manifest.get('schema_version') == 1 and manifest.get('source_revision') == revision, 'Artifact revision mismatch.')
    need(set(manifest.get('files', {})) == FILES - {'build-manifest.json'}, 'Manifest file list mismatch.')
    for name, expected in manifest['files'].items():
        need(re.fullmatch(r'[0-9a-f]{64}', expected) is not None, 'Invalid manifest hash.')
        need(hashlib.sha256((path / name).read_bytes()).hexdigest() == expected, 'Artifact byte mismatch: ' + name)
    data = json.loads((path / 'data/dashboard-data.json').read_text())
    state = json.loads((path / 'data/tracker-state.json').read_text())
    review = data['last_evidence_review']
    need(state['evidence_data_sha256'] == manifest['files']['data/dashboard-data.json'], 'Evidence checksum mismatch.')
    need(manifest['evidence_review_id'] == state['evidence_review_id'] == review['review_id'], 'Artifact evidence-review mismatch.')
    need(state['evidence_review_date'] == review['date'], 'Artifact review-date mismatch.')
    return manifest

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    parser.add_argument('--source-revision', required=True)
    args = parser.parse_args()
    manifest = check(args.path, args.source_revision)
    print('SITE ARTIFACT CHECK PASS: ' + manifest['source_revision'])

if __name__ == '__main__':
    main()
