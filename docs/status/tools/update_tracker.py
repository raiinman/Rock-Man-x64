#!/usr/bin/env python3
"""Offline, fixed-output documentation generator. Never infers acceptance from prose."""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
DATA = 'docs/status/dashboard-data.json'
STATE = 'docs/status/tracker-state.json'
OUTPUTS = ('README.md', 'docs/status/dashboard.md', 'docs/status/changes.md',
           'docs/status/visuals/progress-dashboard.svg', STATE)
START = '<!-- ROCK-MAN-TRACKER:START -->'
END = '<!-- ROCK-MAN-TRACKER:END -->'
REPO = 'https://github.com/raiinman/Rock-Man-x64'
STAGES = ('Source review', 'Synthetic/component', 'Linux run', 'Windows run', 'Full app')
SHA = re.compile(r'^[0-9a-f]{40}$')
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')

class Invalid(ValueError):
    pass

def need(condition, message):
    if not condition:
        raise Invalid(message)

def text(value, name, maximum=1200):
    need(isinstance(value, str) and 0 < len(value) <= maximum, f'{name}: invalid text length')
    need(not any(c in value for c in ('\x00', '\r')), f'{name}: control character')
    need(not re.search(r'(?i)(/workspace/|/home/|[A-Z]:\\|sediment://|BEGIN .*PRIVATE KEY|gh[pousr]_[a-z0-9]{20,})', value), f'{name}: private-content pattern')

def source(root, value):
    text(value, 'source', 1000)
    if value.startswith('https://'):
        need(not re.search(r'[<>\s\[\]()`{}]', value), 'invalid external source')
        return
    path = value.split('#', 1)[0]
    need(path and not path.startswith('/') and '..' not in Path(path).parts, 'source escapes repository')
    need((root / path).is_file(), f'missing source: {path}')

def validate(root, data, state):
    def scan(value):
        if isinstance(value, str):
            text(value, 'metadata string', 10000)
        elif isinstance(value, dict):
            for key, item in value.items():
                text(key, 'metadata key', 200); scan(item)
        elif isinstance(value, list):
            for item in value: scan(item)
    scan(data); scan(state)
    need(data.get('schema_version') == 2, 'unsupported evidence schema')
    review = data['last_evidence_review']
    need(DATE.fullmatch(review['date']) is not None, 'invalid review date')
    need(SHA.fullmatch(review['reviewed_through_commit']) is not None, 'invalid review basis')
    text(review['review_id'], 'review_id', 120)
    text(review['summary'], 'review summary')
    for key in ('now', 'changed', 'why', 'next'):
        text(data['overview'][key], f'overview.{key}', 650)
    need(len(data['workstreams']) > 0, 'no workstreams')
    ids = set()
    for w in data['workstreams']:
        need(w['id'] not in ids, 'duplicate workstream ID'); ids.add(w['id'])
        for key in ('name', 'plain_status', 'next', 'detail', 'limit'):
            text(w[key], f'workstream.{key}', 650)
        need(len(w['stages']) == len(STAGES), 'wrong stage count')
        need(all(type(v) is int and v in (0, 1, 2) for v in w['stages']), 'invalid stage state')
        need(all(v != 2 or i == 0 for i, v in enumerate(w['stages'])), 'NO-GO belongs to source review only')
        for i, value in enumerate(w['stages']):
            if value:
                refs = w['stage_evidence'].get(str(i), [])
                need(bool(refs), f'{w["id"]}: filled stage lacks evidence')
                for ref in refs: source(root, ref)
        source(root, w['source'])
    ids = set()
    for entry in data['updates']:
        need(entry['id'] not in ids, 'duplicate update ID'); ids.add(entry['id'])
        need(DATE.fullmatch(entry['date']) is not None, 'invalid update date')
        need(type(entry['capability_changed']) is bool, 'capability_changed must be boolean')
        need(entry['kind'] in ('documentation', 'source-review', 'synthetic-linux', 'windows', 'connected-linux', 'research', 'correction'), 'invalid update kind')
        need(not (entry['kind'] in ('documentation', 'source-review') and entry['capability_changed']), 'documentation/source review cannot claim runtime advancement')
        for key in ('changed', 'why', 'next'): text(entry[key], f'update.{key}', 800)
        need(bool(entry['evidence']), 'update without evidence')
        for ref in entry['evidence']: source(root, ref)
    for finding in data['findings']:
        for key in ('title', 'found', 'why', 'unknown', 'class', 'metric', 'unit'): text(finding[key], f'finding.{key}', 900)
        for ref in finding['sources']: source(root, ref)
    need(state.get('schema_version') == 1, 'unsupported state schema')
    activity = state['latest_repository_change']
    need(SHA.fullmatch(activity['sha']) is not None, 'invalid activity SHA')
    need(re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2})', activity['committed_at']) is not None, 'invalid activity timestamp')
    text(activity['subject'], 'commit subject', 300)
    text(activity['source'], 'activity source', 200)
    for key in ('evidence_data_changed', 'review_id_changed'):
        if key in activity: need(type(activity[key]) is bool, f'{key} must be boolean')
    text(state['trigger_status'], 'trigger status', 400)
    need(re.fullmatch(r'[0-9a-f]{64}', state.get('reviewed_stage_sha256','')) is not None, 'missing prior reviewed-stage receipt')
    text(state.get('evidence_review_id',''), 'prior evidence review ID', 120)
    need(DATE.fullmatch(state.get('evidence_review_date','')) is not None, 'invalid prior evidence review date')

def stage_digest(data):
    payload=[{'id':w.get('id',w['name']), 'stages':w['stages'], 'stage_evidence':w.get('stage_evidence',{})} for w in data['workstreams']]
    return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def md(value):
    value=html.escape(value, quote=False).replace('\n', ' ')
    return re.sub(r'([\\`*_{}\[\]()#+!|])', r'\\\1', value)

def link(ref, from_root=True, label='evidence'):
    if ref.startswith('https://'):
        return f'[{label}]({ref})'
    prefix = '' if from_root else '../../'
    return f'[{label}]({prefix}{ref})'

def activity_lines(data, state):
    review = data['last_evidence_review']; activity = state['latest_repository_change']
    different = activity['sha'] != review['reviewed_through_commit']
    return [
        f'**Last evidence review:** {review["date"]} · `{review["review_id"]}` · [reviewed basis {review["reviewed_through_commit"][:7]}]({REPO}/commit/{review["reviewed_through_commit"]}).',
        f'**Latest repository change observed:** [{activity["sha"][:7]}]({REPO}/commit/{activity["sha"]}) · {activity["committed_at"]} — {md(activity["subject"])}.',
        ('**Authored evidence update supplied:** the evidence file and its review identifier changed in the observed commit. Stages still mean only what the cited reviewed record establishes.' if different and activity.get('evidence_data_changed') and activity.get('review_id_changed') else '**Review pending:** the repository has changed without a newly identified evidence review. The bars do not advance merely because a commit arrived.' if different else '**Evidence boundary:** repository activity and accepted capability are separate. A new push never counts as a native-game pass.'),
    ]

def stage_bar(stages):
    # Five named evidence classes, never a completion ratio or weighted denominator.
    return ''.join('🟨' if x == 2 else '🟦' if x == 1 else '⬜' for x in stages)

def readme_block(data, state):
    o = data['overview']
    rows = ['## Living progress tracker', '', '**Where we are:** '+md(o['now']), '',
            '**What changed:** '+md(o['changed']), '', '**Why it matters:** '+md(o['why']), '',
            '**Next useful step:** '+md(o['next']), ''] + activity_lines(data, state)
    rows += ['', '| Workstream | Evidence bar | In plain English |', '|---|---|---|']
    for w in data['workstreams']:
        rows.append(f'| {md(w["name"])} | {stage_bar(w["stages"])} | {md(w["plain_status"])} |')
    rows += ['', '**Left → right:** source review · synthetic/component · Linux · Windows · full game/IDE. '
             '🟦 bounded evidence · 🟨 completed NO-GO review · ⬜ no acceptance claimed. '
             '**These are evidence classes, not five equal units of work or percent complete.**', '',
             '[What changed / why / next](docs/status/changes.md) · [Exact scopes and discoveries](docs/status/dashboard.md) · [How updates work](docs/status/TRACKER.md)', '',
             '_'+md(state['trigger_status'])+'_']
    return '\n'.join(rows)

def changes(data):
    lines = ['# What changed, why it matters, and what comes next', '',
             'Generated from reviewed evidence data. Entries describe actual reviewed changes; an unrelated repository push does not add a capability milestone.', '',
             '[Current tracker](../../README.md#living-progress-tracker) · [Maintenance](TRACKER.md)', '']
    for e in data['updates']:
        lines += [f'## {e["date"]} · {e["id"]}', '', f'**Evidence class:** {md(e["kind"])}. **Runtime capability advanced:** {"yes, only within the cited scope" if e["capability_changed"] else "no"}.', '',
                  '**Changed:** '+md(e['changed']), '', '**Why:** '+md(e['why']), '', '**Next:** '+md(e['next']), '',
                  '**Evidence:** '+' · '.join(link(x, False, f'source {i+1}') for i, x in enumerate(e['evidence']))+'.', '']
    return '\n'.join(lines).rstrip()+'\n'

def dashboard(data, state):
    lines=['# Living evidence tracker and findings', '', 'Generated from reviewed evidence data. This is documentation, not a playable game or a public test package.', '']
    lines += activity_lines(data, state)
    lines += ['', '## Current explanation', '', '**Now:** '+md(data['overview']['now']), '', '**Changed:** '+md(data['overview']['changed']), '', '**Why:** '+md(data['overview']['why']), '', '**Next:** '+md(data['overview']['next']), '',
              '[Plain-English change ledger](changes.md) · [Update contract](TRACKER.md) · [Reviewed source data](dashboard-data.json)', '',
              '## Evidence tracks', '', '| Workstream | Source | Synthetic | Linux | Windows | Full app | Scope / next |', '|---|---|---|---|---|---|---|']
    for w in data['workstreams']:
        labels=['NO-GO review' if v==2 else ('Reviewed' if i==0 else 'Bounded evidence') if v else '—' for i,v in enumerate(w['stages'])]
        lines.append('| '+md(w['name'])+' | '+' | '.join(labels)+' | '+md(w['detail'])+'. '+md(w['limit'])+' **Next:** '+md(w['next'])+' '+link(w['source'],False)+' |')
    lines += ['', 'Platform and synthetic cells can describe the same run. They are not additive, equally weighted units or a game-completion percentage. Full app means end-to-end game or complete IDE, not a component integration.', '',
              'The exporter/frozen-viewer row combines **different scopes**: one actual Linux artifact-to-portable-model import and Windows synthetic HWND/command/state checks. It does not establish actual-capture GUI display on Windows. See '+link('docs/status/current-status.md#actual-portable-exportimport-and-bounded-windows-viewer-acceptance',False)+' and '+link('docs/status/current-status.md#separately-approved-windows-viewer-result',False)+'.', '',
              '<details>', '<summary>Generated visual fallback for the same reviewed stages</summary>', '', '![Generated evidence-stage bars](visuals/progress-dashboard.svg)', '', '</details>', '',
              '## Reconstruction findings', '']
    for f in data['findings']:
        if f['id']=='07': lines += ['## Frontier findings', '']
        title='Cancel requested is not work retired' if f['id']=='12' else f['title']
        lines += [f'## {f["id"]} {title}', '', '**Found:** '+md(f['found']), '', '**Why it matters:** '+md(f['why']), '',
                  f'**Evidence:** {md(f["class"])}. {md(f["metric"])} — {md(f["unit"].lower())}.', '', '**Still unknown:** '+md(f['unknown']), '']
        if f['id']=='12':
            lines += ['The newer load and host-I/O findings are source/design reviews only: no implementation, build, synthetic/runtime test or Windows run occurred in those reviews. Cancellation intent, actual I/O completion, resource settlement and execution retirement remain distinct. No product guarantee is revised here; weakening the bounded-close requirement needs an explicit owner decision. Native-owner and provenance gates remain independent.', '']
        refs=[x for x in f['sources'] if not x.startswith('docs/status/dashboard.md#')]
        lines += ['**Sources:** '+' · '.join(link(x,False,f'source {i+1}') for i,x in enumerate(refs))+'.', '']
    lines += ['## Provenance', '', data['provenance'], '', 'Executed emulator research is author-reported reference behavior, not native game boot, physical-console equivalence or implementation clearance. PSX-SPX remains credited to Martin “nocash” Korth and community contributors and is not cleared implementation authority. '+link('research/bios/PROVENANCE-REVIEW.md',False,'Full provenance boundary')+'.', '',
              '<details>', '<summary>Earlier explanatory graphics — dated 2026-10-23, not the live tracker</summary>', '',
              'These archived explanatory boards are secondary references. The reviewed data and generated text above own current status.', '',
              '![Earlier reconstruction findings](visuals/findings-01.svg)', '', '![Earlier frontier findings](visuals/findings-02.svg)', '', '</details>', '']
    return '\n'.join(lines).rstrip()+'\n'

def svg(data):
    rows=data['workstreams']; height=220+len(rows)*70
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{height}" viewBox="0 0 1280 {height}" role="img" aria-labelledby="title desc">',
           '<title id="title">Generated evidence-stage tracker</title><desc id="desc">Five independent evidence classes per workstream, not a completion percentage. Exact evidence and next steps are in the accessible Markdown tracker.</desc>',
           f'<rect width="1280" height="{height}" fill="#10171b"/>']
    def t(x,y,s,size=18,fill='#f1ebdf',bold=False):
        parts.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{fill}">{html.escape(s)}</text>')
    t(40,52,'REVIEWED EVIDENCE — NOT PERCENT COMPLETE',27,bold=True)
    t(40,88,'Last evidence review: '+data['last_evidence_review']['date']+' · activity never promotes a stage',17,'#a9b8bd')
    labels=['SOURCE','SYNTHETIC','LINUX','WINDOWS','FULL APP']; xs=[620,742,864,986,1108]
    for x,l in zip(xs,labels):t(x,135,l,12,'#a9b8bd',True)
    for n,w in enumerate(rows):
        y=157+n*70;t(40,y+22,w['name'],21,bold=True)
        need(len(w['name'])<=43, 'workstream label too long for SVG')
        for i,(x,v) in enumerate(zip(xs,w['stages'])):
            color='#efb765' if v==2 else '#6ed5df' if v else '#26343a'
            parts.append(f'<rect x="{x}" y="{y}" width="110" height="35" rx="4" fill="{color}"/>')
            label='NO-GO' if v==2 else ('REVIEW' if i==0 else 'PASS' if i==1 else 'RUN') if v else '—'
            t(x+22,y+23,label,12,'#10171b' if v else '#a9b8bd',True)
    t(40,height-32,'Evidence classes overlap. Empty means no acceptance claimed. Read the linked scope before interpreting a filled cell.',15,'#a9b8bd')
    return '\n'.join(parts+['</svg>'])+'\n'

def render(root, data, state):
    validate(root,data,state)
    current_stages=stage_digest(data)
    review=data['last_evidence_review']
    if current_stages != state['reviewed_stage_sha256']:
        need(review['review_id'] != state['evidence_review_id'], 'changed stages/citations require a new evidence review identifier')
        need(review['date'] >= state['evidence_review_date'], 'evidence review date regressed')
    readme=(root/'README.md').read_text()
    need(readme.count(START)==1 and readme.count(END)==1, 'README must contain one ordered tracker marker pair')
    before,rest=readme.split(START);old,after=rest.split(END)
    state=dict(state)
    state['evidence_data_sha256']=hashlib.sha256((root/DATA).read_bytes()).hexdigest()
    state['reviewed_stage_sha256']=current_stages
    state['evidence_review_id']=review['review_id']
    state['evidence_review_date']=review['date']
    state['generated_paths']=list(OUTPUTS)
    return {'README.md':before+START+'\n\n'+readme_block(data,state)+'\n\n'+END+after,
            'docs/status/dashboard.md':dashboard(data,state), 'docs/status/changes.md':changes(data),
            'docs/status/visuals/progress-dashboard.svg':svg(data), STATE:json.dumps(state,indent=2,ensure_ascii=False)+'\n'}

def git_activity(root, sha):
    need(SHA.fullmatch(sha) is not None, 'refresh requires a full commit SHA')
    result=subprocess.run(['git','show','-s','--format=%H%x00%cI%x00%s',sha],cwd=root,capture_output=True,text=True,check=True)
    got,date,subject=result.stdout.rstrip('\n').split('\x00')
    need(got==sha,'git resolved a different commit')
    new = subprocess.run(['git','show',f'{sha}:{DATA}'],cwd=root,capture_output=True,text=True,check=True).stdout
    prior = subprocess.run(['git','show',f'{sha}^:{DATA}'],cwd=root,capture_output=True,text=True)
    old = json.loads(prior.stdout) if prior.returncode == 0 else {}
    current = json.loads(new)
    review_changed=old.get('last_evidence_review',{}).get('review_id') != current.get('last_evidence_review',{}).get('review_id')
    if old.get('workstreams') and stage_digest(old) != stage_digest(current):
        need(review_changed, 'commit changes stages/citations without a new evidence review identifier')
    return {'sha':got,'committed_at':date,'subject':subject,'source':'Exact local Git commit metadata; no prose-based capability inference',
            'evidence_data_changed':prior.returncode != 0 or prior.stdout != new,
            'review_id_changed':review_changed}

def run(root, check=True, refresh=None, activity_json=None):
    root=Path(root).resolve();data=json.loads((root/DATA).read_text());state=json.loads((root/STATE).read_text())
    need(not (check and (refresh or activity_json)), '--check cannot refresh metadata')
    need(not (refresh and activity_json), 'choose one activity input')
    if refresh:state['latest_repository_change']=git_activity(root,refresh)
    if activity_json:state['latest_repository_change']=json.loads(Path(activity_json).read_text())
    outputs=render(root,data,state)
    need(set(outputs)==set(OUTPUTS),'unexpected output target')
    changed=[p for p,s in outputs.items() if not (root/p).exists() or (root/p).read_text()!=s]
    for relative in OUTPUTS:
        target=root/relative
        need(not target.is_symlink(),'refusing symlink output')
        need(target.resolve().is_relative_to(root),'output escapes repository')
    if check:
        if changed:raise Invalid('generated files are stale: '+', '.join(changed))
    else:
        # Render/validate every output before any mutation, then atomic per-file replacement.
        for relative in changed:
            target=root/relative;target.parent.mkdir(parents=True,exist_ok=True)
            fd,name=tempfile.mkstemp(prefix='.tracker-',dir=target.parent)
            try:
                with os.fdopen(fd,'w',encoding='utf-8',newline='\n') as f:f.write(outputs[relative])
                os.replace(name,target)
            finally:
                if os.path.exists(name):os.unlink(name)
    return changed

def main():
    p=argparse.ArgumentParser(description=__doc__);g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--check',action='store_true');g.add_argument('--write',action='store_true')
    p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--refresh-activity',metavar='FULL_SHA')
    p.add_argument('--activity-json',type=Path,help='exact commit metadata supplied by the authorized GitHub connector path')
    args=p.parse_args()
    try:
        changed=run(args.root,args.check,args.refresh_activity,args.activity_json)
    except (Invalid,KeyError,ValueError,OSError,subprocess.CalledProcessError) as e:
        print('TRACKER REFUSED: '+str(e),file=sys.stderr);return 1
    print('TRACKER CHECK PASS' if args.check else 'TRACKER WRITE: '+(', '.join(changed) or 'already current'))
    return 0

if __name__=='__main__':sys.exit(main())
