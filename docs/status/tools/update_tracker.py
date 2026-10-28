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
import textwrap
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

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
CHECKLIST_IDS = ('inspection','observation','loader','s2','boot','roadmap')

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

PLAN_STATES = ('planned', 'implemented', 'tested', 'blocked')

def validate_build_plan(root, data):
    plan = data.get('build_plan')
    if plan is None:
        return
    need(plan.get('schema_version') == 1, 'unsupported build-plan schema')
    need(re.fullmatch(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC', plan.get('reviewed_at', '')) is not None, 'invalid build-plan review time')
    need(plan['reviewed_at'].startswith(data['last_evidence_review']['date']), 'build-plan review date mismatch')
    source(root, plan['plan_source'])
    need(not plan['plan_source'].startswith('https:') and '#' not in plan['plan_source'], 'build-plan definitions must be a repository file')
    definitions = {}
    raw = (root / plan['plan_source']).read_text()
    for match in re.finditer(r'^## (SI-\d{2}): [^\n]+\n(.*?)(?=^## SI-\d{2}:|\Z)', raw, re.M | re.S):
        row = re.search(r'^\*\*Dependencies:\*\*([^\n]+)', match[2], re.M)
        need(row is not None, 'task definition lacks dependencies')
        definitions[match[1].lower()] = sorted(set(v.lower() for v in re.findall(r'SI-\d{2}', row[1])))
    tasks = plan['tasks']
    need(isinstance(tasks, list) and 0 < len(tasks) <= 200, 'invalid build-plan task list')
    ids = [t['id'] for t in tasks]
    need(len(set(ids)) == len(ids) and set(ids) == set(definitions), 'build-plan task IDs differ from definitions')
    for task in tasks:
        need(task['state'] in PLAN_STATES, 'invalid build-plan task state')
        text(task['label'], 'plan label', 150); text(task['state_reason'], 'plan state reason', 650)
        need(task['source'] == plan['plan_source'] + '#' + task['id'], 'build-plan task source mismatch')
        source(root, task['source'])
        deps = task['dependencies']
        need(isinstance(deps, list) and len(set(deps)) == len(deps) and sorted(deps) == definitions[task['id']], 'build-plan dependencies differ from definitions')
        need(task['id'] not in deps and all(v in ids for v in deps), 'unknown/self plan dependency')
        need(isinstance(task['evidence'], list), 'invalid plan evidence')
        for ref in task['evidence']: source(root, ref)
        need(task['state'] == 'planned' or bool(task['evidence']), 'nonplanned task state requires evidence')
    by_id = {t['id']: t for t in tasks}; visited = set(); active = set()
    def visit(id):
        need(id not in active, 'build-plan dependency cycle')
        if id in visited: return
        active.add(id)
        for dep in by_id[id]['dependencies']: visit(dep)
        active.remove(id); visited.add(id)
    for id in ids: visit(id)
    checks = plan['checks']; updates = {u['id']: u for u in data['updates']}
    need(isinstance(checks, list) and len({c['id'] for c in checks}) == len(checks), 'invalid build-plan checks')
    for check in checks:
        need(re.fullmatch(r'[a-z0-9][a-z0-9-]{0,119}', check['id']) is not None and check['id'] not in ids, 'invalid build check ID')
        need(check['state'] in PLAN_STATES, 'invalid build check state')
        text(check['label'], 'build check label', 150); text(check['limit'], 'build check limit', 650)
        need(check['update_id'] in updates and bool(updates[check['update_id']]['evidence']), 'build check requires cited update')

def format_review_time(value):
    """Display a recorded UTC instant in America/Phoenix; never refresh it."""
    need(isinstance(value, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC', value) is not None,
         'invalid canonical UTC review time')
    try:
        local = datetime.strptime(value, '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc).astimezone(ZoneInfo('America/Phoenix'))
    except (ValueError, OverflowError) as error:
        raise Invalid('invalid canonical UTC review time') from error
    months = ('January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December')
    return (f'{months[local.month - 1]} {local.day}, {local.year}, '
            f'{local.hour % 12 or 12}:{local.minute:02d}:{local.second:02d} '
            f'{"AM" if local.hour < 12 else "PM"} Arizona ({local.tzname()})')

def build_plan_ledger(data):
    plan = data.get('build_plan')
    if plan is None: return []
    lines = ['', '## Build and specification plan', '',
             'Separate from historical acceptance. Explicit reviewed states, not task-checkbox inference, equal effort or game completion.', '',
             '**Map reviewed:** ' + md(format_review_time(plan['reviewed_at'])) + '.', '',
             '[Open the separate heatmap](https://raiinman.github.io/Rock-Man-x64/#build-plan) · ' + link(plan['plan_source'], False, 'Full task definitions'), '']
    updates = {u['id']: u for u in data['updates']}
    for check in plan['checks']:
        update = updates[check['update_id']]
        lines += ['### ' + md(check['label']), '', '**Recorded state:** ' + check['state'] + '.', '', md(update['changed']), '', md(check['limit']), '',
                  '**Evidence:** ' + ' · '.join(link(ref, False) for ref in update['evidence']), '']
    lines += ['| Task | Recorded state | Task prerequisites | State explanation |', '|---|---|---|---|']
    for task in plan['tasks']:
        lines.append('| ' + link(task['source'], False, task['id'].upper() + ': ' + task['label']) + ' | ' + task['state'] + ' | ' + (', '.join(v.upper() for v in task['dependencies']) or 'None listed') + ' | ' + md(task['state_reason']) + ' |')
    return lines

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
    need(data.get('schema_version') == 3, 'unsupported evidence schema')
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
    validate_numbers(root, data)
    validate_build_plan(root, data)
    need(state.get('schema_version') == 2, 'unsupported state schema')
    need(isinstance(state.get('reviewed_checklist_definitions'),dict) and set(state['reviewed_checklist_definitions'])==set(CHECKLIST_IDS),'missing prior checklist definitions')
    need(isinstance(state.get('recorded_observation_hashes'),list) and bool(state['recorded_observation_hashes']),'missing prior observation history')
    for value in state['recorded_observation_hashes']:
        need(re.fullmatch(r'[0-9a-f]{64}',value) is not None,'invalid observation receipt')
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

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def definitions(data):
    return {c['id']:{'version':c['version'],'sha256':digest({'title':c['title'],'scope':c['scope'],'items':[{k:i[k] for k in ('id','label','criterion','phase') if k in i} for i in c['items']]})} for c in data.get('checklists',[])}

def check_numeric_transition(prior,data):
    current=definitions(data)
    for cid,old in prior.get('reviewed_checklist_definitions',{}).items():
        need(cid in current,'recorded checklist cannot silently disappear')
        new=current[cid]
        need(new['version']>=old['version'],'checklist version regressed')
        need(new['sha256']==old['sha256'] or new['version']>old['version'],'changed denominator/criteria require a new checklist version')
    hashes=[digest(o) for o in data['observations']];old=prior.get('recorded_observation_hashes',[])
    need(hashes[:len(old)]==old,'recorded numeric history is append-only')
    need(len(hashes)<=len(old)+1,'only one new numeric observation is allowed per review transition')

def validate_numbers(root,data):
    need(bool(data.get('checklists')),'missing named checklists');ids=set()
    def safe_id(value):
        need(isinstance(value,str) and re.fullmatch(r'[a-z0-9][a-z0-9-]{0,119}',value) is not None,'invalid plain identifier')
    for c in data['checklists']:
        safe_id(c['id'])
        need(c['id'] not in ids,'duplicate checklist ID');ids.add(c['id'])
        need(type(c['version']) is int and c['version']>0,'invalid checklist version')
        need(DATE.fullmatch(c['frozen_on']) is not None,'invalid checklist freeze date')
        for k in ('title','scope','blocker','next'):text(c[k],'checklist.'+k,700)
        need(0<len(c['items'])<=100,'invalid checklist denominator');itemids=set()
        for i in c['items']:
            safe_id(i['id'])
            need(i['id'] not in itemids,'duplicate criterion ID');itemids.add(i['id'])
            need(type(i['done']) is bool,'criterion done must be boolean')
            if c['id']=='roadmap':need(i.get('phase') in ('foundation','production'),'invalid roadmap phase')
            for k in ('label','criterion','evidence_class'):text(i[k],'criterion.'+k,700)
            source(root,i['source'])
            for ref in i.get('additional_sources',[]):source(root,ref)
    need(bool(data.get('observations')),'missing recorded baseline');reviews=set();lastdate=''
    for o in data['observations']:
        safe_id(o['review_id'])
        need(o['review_id'] not in reviews,'duplicate numeric review ID');reviews.add(o['review_id'])
        need(DATE.fullmatch(o['date']) is not None and o['date']>=lastdate,'numeric observation date regressed');lastdate=o['date']
        need(SHA.fullmatch(o['basis_commit']) is not None,'invalid observation basis')
        seen=set()
        for row in o['checklists']:
            safe_id(row['id'])
            need(type(row['version']) is int and row['version']>0,'invalid observed checklist version')
            for completed_id in row['completed_ids']:safe_id(completed_id)
            need(row['id'] not in seen,'duplicate observed checklist');seen.add(row['id'])
            need(type(row['total']) is int and row['total']>0,'invalid observed denominator')
            need(len(set(row['completed_ids']))==len(row['completed_ids'])<=row['total'],'invalid observed completion')
            current=next((c for c in data['checklists'] if c['id']==row['id']),None)
            if current and current['version']==row['version']:
                need(row['total']==len(current['items']),'historical denominator changed without version')
                need(set(row['completed_ids'])<={i['id'] for i in current['items']},'unknown completed criterion')
    last=data['observations'][-1];review=data['last_evidence_review']
    need(last['review_id']==review['review_id'] and last['date']==review['date'] and last['basis_commit']==review['reviewed_through_commit'],'latest numeric observation must match the evidence review identity/date/basis')
    latest={r['id']:r for r in last['checklists']}
    need(set(latest)==ids,'latest observation must cover current checklists')
    for c in data['checklists']:
        row=latest[c['id']]
        need(row['version']==c['version'] and row['total']==len(c['items']),'latest observation definition mismatch')
        need(set(row['completed_ids'])=={i['id'] for i in c['items'] if i['done']},'checklist change needs a matching recorded observation')
    need(ids==set(CHECKLIST_IDS),'chart requires the fixed reviewed checklist IDs')
    need(len(data['validation_runs'])==3,'chart layout requires three labeled validation runs')
    for v in data['validation_runs']:
        need(type(v['passed']) is int and type(v['total']) is int and 0<=v['passed']<=v['total'] and v['total']>0,'invalid validation count')
        source(root,v['source'])

def numbers(c):
    done=sum(i['done'] for i in c['items']);total=len(c['items'])
    return done,total,round(done*100/total,1)

def scope_short(cid):
    return {'inspection':'bounded Linux / Windows delivery','observation':'data-only components, not a controller','loader':'selected native-policy checkpoints only','s2':'necessary gates, not a sufficiency proof','boot':'one acceptance gate, not implementation %'}[cid]

def previous_observation(data,c):
    for o in reversed(data['observations'][:-1]):
        for row in o['checklists']:
            if row['id']==c['id'] and row['version']==c['version']:return row
    return None

def delta_label(data,c):
    prior=previous_observation(data,c)
    if prior is None:
        older=any(row['id']==c['id'] for o in data['observations'][:-1] for row in o['checklists'])
        return 'Δ — rebaseline' if older else 'Δ — first record'
    change=numbers(c)[0]-len(prior['completed_ids'])
    return f'Δ {change:+d} goals'

def numeric_change(data):
    if len(data['observations'])==1:return 'First recorded baseline. No earlier numeric observation exists, so no progress delta is invented.'
    return '; '.join(c['title']+': '+delta_label(data,c) for c in data['checklists'])+'.'

def numeric_history(data):
    lines=['', '## Numeric review history', '', 'Only recorded observations appear here. The first entry is a baseline, not a newly completed runtime milestone. A new checklist version starts a new comparison basis.', '', '| Recorded review | Checklist version | Completed / total | Change note |','|---|---|---|---|']
    for o in data['observations']:
        for row in o['checklists']:
            lines.append(f'| {o["date"]} · `{o["review_id"]}` | {row["id"]} v{row["version"]} | {len(row["completed_ids"])} / {row["total"]} | {md(o["note"])} |')
    return lines+['']

def checklist_ledger(data):
    lines=['## Named checklists', '', 'The overall roadmap is a separately defined whole-project milestone plan. Its percentage counts unequal-sized accepted milestones, not game/code/effort completion; effort-weighted completion is unknown. The five local checklists overlap it and are never added or averaged into the overall score. Test pass rates are separate.', '', '**Latest numeric change:** '+md(numeric_change(data)), '']
    for c in sorted(data['checklists'],key=lambda c:c['id']!='roadmap'):
        done,total,pct=numbers(c)
        lines += [f'### {c["id"]} — {c["title"]}', '',f'**{done} / {total} accepted · {pct}% · {total-done} remaining · {delta_label(data,c)}.** Definition v{c["version"]}, frozen {c["frozen_on"]}.', '',md(c['scope']), '', '**Blocker:** '+md(c['blocker']), '', '**Next:** '+md(c['next']), '', '| Accepted? | Named criterion and exact done condition | Evidence class / source |','|---|---|---|']
        for i in c['items']:
            lines.append('| '+('YES' if i['done'] else 'NO — pending')+' | **'+md(i['label'])+'** — '+md(i['criterion'])+' | '+md(i['evidence_class'])+' · '+' · '.join(link(ref,False) for ref in [i['source']]+i.get('additional_sources',[]))+' |')
        lines+=['']
    lines += ['### Validation pass rates — separate measurement', '', '| Specific run | Passed / total | Pass rate | Scope |','|---|---|---|']
    for v in data['validation_runs']:lines.append(f'| {md(v["title"])} | {v["passed"]} / {v["total"]} | {round(100*v["passed"]/v["total"],1)}% | {md(v["scope"])} '+link(v['source'],False)+' |')
    return lines+numeric_history(data)

def stage_digest(data):
    payload=[{'id':w.get('id',w['name']), 'stages':w['stages'], 'stage_evidence':w.get('stage_evidence',{})} for w in data['workstreams']]
    return digest({'stages':payload,'checklists':data.get('checklists',[]),'observations':data.get('observations',[]),'validation_runs':data.get('validation_runs',[])})

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
    lines=['## Progress, in numbers', '',
           '[![Completed and remaining goals in five named checklists](docs/status/visuals/progress-dashboard.svg)](docs/status/dashboard.md#named-checklists)', '',
           '**This chart updates from reviewed data after eligible GitHub pushes.** The top bar counts accepted milestones in the named overall roadmap—not code, effort or how much of the game is finished. Local checklists and test pass rates remain separate.', '',
           '**Where we are:** '+md(data['overview']['now']), '',
           '**Next useful step:** '+md(data['overview']['next']), '',
           '**Change since previous numeric review:** '+md(numeric_change(data)), '',
           '[Exact done criteria and evidence](docs/status/dashboard.md#named-checklists) · [Recorded changes](docs/status/changes.md#numeric-review-history) · [12 important discoveries](docs/status/dashboard.md#reconstruction-findings) · [How this stays current](docs/status/TRACKER.md)', '']
    lines+=activity_lines(data,state)
    return '\n'.join(lines)

def changes(data):
    lines = ['# What changed, why it matters, and what comes next', '',
             'Generated from reviewed evidence data. Entries describe actual reviewed changes; an unrelated repository push does not add a capability milestone.', '',
             '[Current tracker](../../README.md#progress-in-numbers) · [Maintenance](TRACKER.md)', '']
    for e in data['updates']:
        lines += [f'## {e["date"]} · {e["id"]}', '', f'**Evidence class:** {md(e["kind"])}. **Runtime capability advanced:** {"yes, only within the cited scope" if e["capability_changed"] else "no"}.', '',
                  '**Changed:** '+md(e['changed']), '', '**Why:** '+md(e['why']), '', '**Next:** '+md(e['next']), '',
                  '**Evidence:** '+' · '.join(link(x, False, f'source {i+1}') for i, x in enumerate(e['evidence']))+'.', '']
    lines+=numeric_history(data)
    return '\n'.join(lines).rstrip()+'\n'

def dashboard(data, state):
    lines=['# Living evidence tracker and findings', '', 'Generated from reviewed evidence data. This is documentation, not a playable game or a public test package.', '']
    lines += activity_lines(data, state)
    lines += ['', '![Milestone checklist completion](visuals/progress-dashboard.svg)', ''] + checklist_ledger(data)
    lines += build_plan_ledger(data)
    lines += ['', '## Current explanation', '', '**Now:** '+md(data['overview']['now']), '', '**Changed:** '+md(data['overview']['changed']), '', '**Why:** '+md(data['overview']['why']), '', '**Next:** '+md(data['overview']['next']), '',
              '[Plain-English change ledger](changes.md) · [Update contract](TRACKER.md) · [Reviewed source data](dashboard-data.json)', '',
              '## Evidence tracks', '', '| Workstream | Source | Synthetic | Linux | Windows | Full app | Scope / next |', '|---|---|---|---|---|---|---|']
    for w in data['workstreams']:
        labels=['NO-GO review' if v==2 else ('Reviewed' if i==0 else 'Bounded evidence') if v else '—' for i,v in enumerate(w['stages'])]
        lines.append('| '+md(w['name'])+' | '+' | '.join(labels)+' | '+md(w['detail'])+'. '+md(w['limit'])+' **Next:** '+md(w['next'])+' '+link(w['source'],False)+' |')
    lines += ['', 'Platform and synthetic cells can describe the same run. They are not additive, equally weighted units or a game-completion percentage. Full app means end-to-end game or complete IDE, not a component integration.', '',
              'The exporter/frozen-viewer row combines **different scopes**: one actual Linux artifact-to-portable-model import and Windows synthetic HWND/command/state checks. It does not establish actual-capture GUI display on Windows. See '+link('docs/status/current-status.md#actual-portable-exportimport-and-bounded-windows-viewer-acceptance',False)+' and '+link('docs/status/current-status.md#separately-approved-windows-viewer-result',False)+'.', '',
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
    width,height=1440,1720
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
           '<title id="title">Milestones completed: counts, remaining goals and checklist percentages</title>',
           '<desc id="desc">A separately defined overall roadmap and five local checklists, not code or effort completion. Separate validation pass rates and exact done criteria are available in the linked Markdown ledger.</desc>']
    def rect(x,y,w,h,fill,rx=0):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"/>')
    def t(x,y,value,size=18,fill='#fff2dd',bold=False):parts.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{fill}">{html.escape(str(value))}</text>')
    rect(0,0,width,height,'#101116')
    # Original layered vector panels: literal colors only, no filters/gradients/resources.
    rect(18,17,1404,171,'#090b10',12);rect(24,20,1392,164,'#34151f',10)
    for yy,hh,color in [(21,3,'#dd4561'),(24,5,'#a82e49'),(29,9,'#79243b'),(38,13,'#551c2c')]:rect(27,yy,1386,hh,color,4)
    rect(24,55,6,122,'#f24763');rect(31,59,2,112,'#651c32')
    rect(34,180,1368,2,'#6e263a');rect(0,0,6,height,'#d32c4c')
    parts.append('<path d="M 1374 184 L 1416 142 L 1416 184 Z" fill="#101116"/>')
    for n in range(6):
        xx=1190+n*31
        parts.append(f'<path d="M {xx} 64 L {xx+25} 64 L {xx+19} 80 L {xx-6} 80 Z" fill="{"#f25b74" if n<4 else "#5c2939"}"/>')
    t(48,50,'ROCK MAN x64  /  LIVE CHECKLIST TRACKER',17,'#ffbdc5',True)
    t(48,103,'Project progress, in numbers',43,bold=True)
    t(48,139,'Accepted roadmap milestones + named delivery checklists.',19,'#c9c1bf')
    obs=data['observations'][-1]
    t(48,175,'Reviewed '+obs['date']+'  /  '+('FIRST NUMERIC BASELINE — no earlier delta recorded' if len(data['observations'])==1 else 'CHANGES COMPARED WITH THE PREVIOUS RECORDED REVIEW'),15,'#ffc36d',True)
    overall=next(c for c in data['checklists'] if c['id']=='roadmap')
    accepted,total,pct=numbers(overall)
    foundations=sum(i['done'] for i in overall['items'] if i['phase']=='foundation')
    production_remaining=sum(not i['done'] for i in overall['items'] if i['phase']=='production')
    rect(25,207,1390,208,'#080a0f',10);rect(28,210,1384,202,'#291c28',8)
    rect(32,211,1376,3,'#f16a84');rect(32,215,1376,5,'#8e2c49');rect(32,221,1376,7,'#542237')
    t(48,258,'OVERALL ROADMAP',19,'#ffbdc5',True)
    t(48,300,f'{accepted} / {total} milestones accepted',35,bold=True)
    t(1188,298,f'{pct:g}%',51,'#fff2dd',True)
    rect(48,320,1316,28,'#080a0f',5);rect(51,323,1310,22,'#40303e',3)
    fillw=1310*accepted/total
    if accepted:
        rect(51,323,fillw,22,'#c3294b',3);rect(52,324,fillw-2,2,'#ffadbd',2)
        rect(52,327,fillw-2,5,'#f56381');rect(52,340,fillw-2,4,'#8e1d3b')
    t(48,376,f'{foundations} bounded foundations accepted; {production_remaining} production goals remain.',22,'#fff2dd',True)
    t(48,400,'Unequal-size milestones — NOT '+f'{pct:g}'+'% of game/code/effort finished. Effort-weighted progress is unknown.',15,'#c9c1bf')
    t(1145,376,delta_label(data,overall),14,'#ffc36d')
    x,bw=48,1050
    for tick in (0,25,50,75,100):t(x+bw*tick/100,451,str(tick)+'%',13,'#9c929b')
    locals_only=[c for c in data['checklists'] if c['id']!='roadmap']
    for n,c in enumerate(locals_only):
        y=485+n*170;done,total,percent=numbers(c);color='#fff2dd' if done else '#ffc36d'
        rect(25,y-33,1390,168,'#090b10',9);rect(28,y-30,1384,164,'#1c2028',8)
        rect(33,y-29,1374,2,'#50515b');rect(34,y-26,1369,2,'#30323e')
        rect(28,y-21,4,137,'#c82c4b' if done else '#9e6335');rect(33,y-20,2,134,'#502131')
        rect(1118,y-15,1,133,'#49404b')
        t(48,y,c['title'],25,bold=True)
        t(48,y+28,f'{total} named criteria · version {c["version"]} · '+scope_short(c['id']),14,'#b1abb0')
        rect(x-3,y+41,bw+6,28,'#080a0f',6);rect(x,y+44,bw,22,'#34313b',4)
        rect(x+3,y+45,bw-6,1,'#73636e')
        if done:
            fillw=bw*done/total
            rect(x-1,y+43,fillw+2,24,'#5e1329',5)
            rect(x,y+44,fillw,22,'#bd2142',4)
            rect(x+1,y+45,fillw-2,2,'#ff91a2',2)
            rect(x+1,y+47,fillw-2,4,'#f65370',2)
            rect(x+1,y+51,fillw-2,5,'#dd3455')
            rect(x+1,y+61,fillw-2,4,'#8b1733',2)
            rect(x+4,y+48,max(0,fillw-8),1,'#ffbdc8')
        for tick in (25,50,75):rect(x+bw*tick/100,y+44,1,22,'#70515f')
        t(1145,y+2,f'{done} / {total}',36,color,True)
        t(1145,y+39,f'{percent:g}%',27,color,True)
        t(1145,y+64,f'{total-done} remaining',15,'#c9c1bf')
        t(1145,y+91,delta_label(data,c),14,'#ffc36d')
        t(48,y+94,'BLOCKER  '+c['blocker'],16,'#e2c29a')
        next_lines=textwrap.wrap('NEXT  '+c['next'],width=112)
        for j,line in enumerate(next_lines[:2]):t(48,y+119+j*20,line,16,'#b1abb0')
    t(48,1368,'VALIDATION RUNS',17,'#ff8095',True)
    t(272,1368,'Pass rates for specific suites — not milestone or game completion',16,'#b1abb0')
    for n,v in enumerate(data['validation_runs']):
        xx=48+n*448;rect(xx-3,1387,430,216,'#080a0f',11);rect(xx,1390,424,210,'#20222b',9)
        rect(xx+4,1391,416,2,'#69616b');rect(xx+4,1394,416,4,'#3b303c')
        rect(xx+1,1398,422,35,'#42202e',3);rect(xx+1,1398,422,2,'#bf415b')
        rect(xx+22,1580,380,3,'#76203a');rect(xx+22,1579,380,1,'#f15a74')
        t(xx+22,1424,v['title'],19,bold=True)
        rate=round(100*v['passed']/v['total'],1)
        t(xx+22,1470,f'{v["passed"]} / {v["total"]}',34,'#fff2dd',True)
        t(xx+267,1470,f'{rate:g}%',27,'#fff2dd',True)
        t(xx+22,1498,v['unit']+' passed',16,'#c6d1d3')
        for j,line in enumerate(textwrap.wrap(v['scope'],width=43)):t(xx+22,1526+j*19,line,14,'#b1abb0')
    t(48,1640,'READ THE CRITERIA',15,'#ffc36d',True)
    t(48,1668,'Checklist goals have different sizes. Do not add these percentages. A checked goal means only its cited scope passed.',16,'#c9c1bf')
    t(48,1694,'Native boot remains unestablished. S2 is NO-GO. The chart is regenerated by the approved documentation workflow.',15,'#c9c1bf')
    return '\n'.join(parts+['</svg>'])+'\n'

def render(root, data, state):
    validate(root,data,state)
    current_stages=stage_digest(data)
    review=data['last_evidence_review']
    if current_stages != state['reviewed_stage_sha256']:
        need(review['review_id'] != state['evidence_review_id'], 'changed stages/citations require a new evidence review identifier')
        need(review['date'] >= state['evidence_review_date'], 'evidence review date regressed')
    check_numeric_transition(state, data)
    if digest(data.get('build_plan')) != state.get('reviewed_build_plan_sha256', digest(None)):
        need(review['review_id'] != state['evidence_review_id'], 'changed build-plan mapping requires a new evidence review identifier')
    readme=(root/'README.md').read_text()
    need(readme.count(START)==1 and readme.count(END)==1, 'README must contain one ordered tracker marker pair')
    before,rest=readme.split(START);old,after=rest.split(END)
    state=dict(state)
    state['evidence_data_sha256']=hashlib.sha256((root/DATA).read_bytes()).hexdigest()
    state['reviewed_stage_sha256']=current_stages
    state['reviewed_build_plan_sha256']=digest(data.get('build_plan'))
    state['evidence_review_id']=review['review_id']
    state['evidence_review_date']=review['date']
    state['generated_paths']=list(OUTPUTS)
    state['reviewed_checklist_definitions']=definitions(data)
    state['recorded_observation_hashes']=[digest(o) for o in data['observations']]
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
    if old.get('checklists'):
        check_numeric_transition({'reviewed_checklist_definitions':definitions(old),'recorded_observation_hashes':[digest(o) for o in old['observations']]},current)
    else:
        need(len(current['observations'])==1,'initial numeric migration must contain one baseline only')
    if digest(old.get('build_plan')) != digest(current.get('build_plan')):
        need(old.get('last_evidence_review',{}).get('review_id') != current.get('last_evidence_review',{}).get('review_id'), 'commit changes build-plan mapping without a new review identifier')
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
