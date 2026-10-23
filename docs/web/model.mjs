/** Pure read-only projection of the reviewed public tracker. No storage or network writes. */
export const REPOSITORY = 'https://github.com/raiinman/Rock-Man-x64';
export const PAGES = ['overview','roadmap','workstreams','findings','history'];
export const STATUSES = ['accepted','in_progress','blocked','pending'];
export const STATUS_LABELS = {accepted:'Accepted',in_progress:'In progress',blocked:'Blocked',pending:'Pending'};
const IDS = ['inspection','observation','loader','s2','boot','roadmap'];
const BLOCKED_CLASSES = new Set(['Source review NO-GO','Source-only NO-GO','Execution blocked; synthetic-only evidence','Blocked visual acceptance']);
const safeId = value => typeof value === 'string' && /^[a-z0-9][a-z0-9-]{0,119}$/.test(value);
const assert = (ok,message) => {if (!ok) throw new Error(message);};
export function validateData(data,state) {
  assert(data?.schema_version === 3 && state?.schema_version === 2,'Unsupported tracker data version.');
  assert(Array.isArray(data.checklists) && data.checklists.length === IDS.length,'Missing reviewed checklists.');
  assert(new Set(data.checklists.map(c=>c.id)).size===IDS.length && data.checklists.every(c=>IDS.includes(c.id)),'Unexpected checklist identity.');
  for (const c of data.checklists) {
    assert(Number.isSafeInteger(c.version)&&c.version>0&&Array.isArray(c.items)&&c.items.length>0,'Invalid checklist definition.');
    assert(new Set(c.items.map(i=>i.id)).size===c.items.length,'Duplicate criterion.');
    for(const i of c.items) {
      assert(safeId(i.id)&&typeof i.done==='boolean','Invalid criterion acceptance.');
      assert(typeof i.label==='string'&&typeof i.criterion==='string'&&typeof i.evidence_class==='string','Missing criterion text.');
      assert(sourceUrl(i.source)!==null,'Unsafe evidence link.');
      assert((i.additional_sources??[]).every(s=>sourceUrl(s)!==null),'Unsafe supporting evidence link.');
      if(i.status!==undefined)assert(STATUSES.includes(i.status)&&(i.done?(i.status==='accepted'):(i.status!=='accepted')),'Status conflicts with reviewed acceptance.');
    }
  }
  const observations=data.observations;
  assert(Array.isArray(observations)&&observations.length>0,'Missing recorded review.');
  const review=data.last_evidence_review;
  assert(review&&typeof review.review_id==='string'&&typeof review.date==='string','Missing evidence attestation.');
  assert(state.evidence_review_id===review.review_id&&state.evidence_review_date===review.date,'Receipt and evidence review disagree.');
  const definitions=new Map(data.checklists.map(c=>[c.id+':'+c.version,{total:c.items.length,ids:new Set(c.items.map(i=>i.id))}]));
  const historicalTotals=new Map();
  for(const observation of observations) {
    assert(typeof observation.review_id==='string'&&typeof observation.date==='string'&&/^[0-9a-f]{40}$/.test(observation.basis_commit),'Invalid historical review.');
    assert(Array.isArray(observation.checklists)&&observation.checklists.length===IDS.length&&new Set(observation.checklists.map(r=>r.id)).size===IDS.length,'Incomplete historical observation.');
    for(const row of observation.checklists) {
      assert(IDS.includes(row.id)&&Number.isSafeInteger(row.version)&&row.version>0&&Number.isSafeInteger(row.total)&&row.total>0,'Invalid historical denominator.');
      assert(Array.isArray(row.completed_ids)&&row.completed_ids.length<=row.total&&row.completed_ids.every(safeId)&&new Set(row.completed_ids).size===row.completed_ids.length,'Invalid historical acceptance.');
      const key=row.id+':'+row.version,definition=definitions.get(key);
      assert(!historicalTotals.has(key)||historicalTotals.get(key)===row.total,'Same-version historical denominators disagree.');
      historicalTotals.set(key,row.total);
      if(definition)assert(row.total===definition.total&&row.completed_ids.every(id=>definition.ids.has(id)),'Historical observation conflicts with the known definition.');
    }
  }
  assert(Array.isArray(data.validation_runs),'Missing bounded validation records.');
  for(const run of data.validation_runs) assert(Number.isSafeInteger(run.passed)&&Number.isSafeInteger(run.total)&&run.total>0&&run.passed>=0&&run.passed<=run.total&&sourceUrl(run.source)!==null,'Invalid bounded validation record.');
  assert(Array.isArray(data.updates)&&data.updates.length>0,'Missing reviewed change entries.');
  for(const update of data.updates) assert(typeof update.capability_changed==='boolean'&&Array.isArray(update.evidence)&&update.evidence.every(s=>sourceUrl(s)!==null),'Invalid reviewed change.');
  assert(Array.isArray(data.findings),'Missing findings.');
  for(const finding of data.findings) assert(safeId(finding.id)&&Array.isArray(finding.sources)&&finding.sources.every(s=>sourceUrl(s)!==null),'Invalid finding.');
  const last=observations.at(-1);
  assert(last.review_id===review.review_id&&last.date===review.date&&last.basis_commit===review.reviewed_through_commit,'Numeric review and evidence review disagree.');
  const latest=new Map(last.checklists.map(r=>[r.id,r]));
  assert(latest.size===IDS.length,'Incomplete numeric observation.');
  for(const c of data.checklists) {
    const row=latest.get(c.id), accepted=c.items.filter(i=>i.done).map(i=>i.id).sort();
    assert(row&&row.version===c.version&&row.total===c.items.length,'Observation denominator mismatch.');
    assert(JSON.stringify([...row.completed_ids].sort())===JSON.stringify(accepted),'Observation acceptance mismatch.');
  }
  assert(/^[0-9a-f]{64}$/.test(state.evidence_data_sha256),'Missing evidence checksum.');
  assert(/^[0-9a-f]{40}$/.test(review.reviewed_through_commit)&&/^[0-9a-f]{40}$/.test(state.latest_repository_change.sha),'Invalid commit identity.');
  return data;
}
export async function verifyDocument(raw,state,subtle=globalThis.crypto?.subtle) {
  assert(subtle,'This browser cannot verify the tracker checksum.');
  const digest=await subtle.digest('SHA-256',new TextEncoder().encode(raw));
  const hash=Array.from(new Uint8Array(digest),b=>b.toString(16).padStart(2,'0')).join('');
  assert(hash===state.evidence_data_sha256,'Tracker data and its review receipt do not match. Please retry after the update finishes.');
  return validateData(JSON.parse(raw),state);
}

export async function verifyManifest(manifest,raw,receiptRaw,subtle=globalThis.crypto?.subtle) {
  const expected=['index.html','styles.css','model.mjs','views.mjs','app.mjs','data/dashboard-data.json','data/tracker-state.json'];
  assert(manifest?.schema_version===1&&/^[0-9a-f]{40}$/.test(manifest.source_revision),'Missing deployed snapshot revision.');
  assert(manifest.files&&Object.keys(manifest.files).length===expected.length&&expected.every(p=>/^[0-9a-f]{64}$/.test(manifest.files[p])),'Invalid deployed artifact manifest.');
  assert(subtle,'This browser cannot verify the deployed snapshot.');
  for(const [name,value] of [['data/dashboard-data.json',raw],['data/tracker-state.json',receiptRaw]]) {
    const digest=await subtle.digest('SHA-256',new TextEncoder().encode(value));
    const hash=Array.from(new Uint8Array(digest),b=>b.toString(16).padStart(2,'0')).join('');
    assert(hash===manifest.files[name],'The deployed snapshot files do not match. Retry after publication finishes.');
  }
  return manifest;
}

export function counts(checklist) {
  const accepted=checklist.items.filter(i=>i.done).length,total=checklist.items.length;
  return {accepted,total,remaining:total-accepted,percent:Math.round(1000*accepted/total)/10};
}
export function statusOf(item) {
  if(item.done===true)return 'accepted';
  if(item.status&&STATUSES.includes(item.status)&&item.status!=='accepted')return item.status;
  return BLOCKED_CLASSES.has(item.evidence_class)?'blocked':'pending';
}
export function sourceUrl(ref) {
  if(typeof ref!=='string'||/[\x00-\x20<>"'`\\]/.test(ref))return null;
  if(ref.startsWith('https://')) {try{const u=new URL(ref);return u.protocol==='https:'&&!u.username&&!u.password?u.href:null;}catch{return null;}}
  if(ref.startsWith('/')||ref.startsWith('#')||ref.includes('?')||ref.includes(':'))return null;
  const [path,fragment]=ref.split('#');
  if(!path||path.split('/').some(p=>!p||p==='.'||p==='..'))return null;
  return `${REPOSITORY}/blob/main/${path.split('/').map(encodeURIComponent).join('/')}${fragment?'#'+encodeURIComponent(fragment):''}`;
}
export function parseRoute(hash='') {
  const raw=hash.replace(/^#/,'');const [page,query='']=raw.split('?');const p=new URLSearchParams(query);
  return {page:PAGES.includes(page)?page:'overview',status:STATUSES.includes(p.get('status'))?p.get('status'):'all',view:p.get('view')==='board'?'board':'list',q:(p.get('q')??'').slice(0,120),item:safeId(p.get('item'))?p.get('item'):'',group:['reconstruction','frontier'].includes(p.get('group'))?p.get('group'):'all'};
}
export function routeHref(route) {
  const p=new URLSearchParams();for(const key of ['status','view','q','item','group'])if(route[key]&&route[key]!=='all'&&!(key==='view'&&route[key]==='list'))p.set(key,route[key]);
  return '#'+(PAGES.includes(route.page)?route.page:'overview')+(p.size?'?'+p.toString():'');
}
export function filteredItems(items,route) {
  const q=route.q.trim().toLocaleLowerCase();return items.filter(i=>(route.status==='all'||statusOf(i)===route.status)&&(!q||[i.label,i.criterion,i.evidence_class].join(' ').toLocaleLowerCase().includes(q)));
}
export function deltaFor(data,checklist) {
  for(const observation of data.observations.slice(0,-1).reverse()) {
    const old=observation.checklists.find(c=>c.id===checklist.id);
    if(old?.version===checklist.version)return {kind:'delta',value:counts(checklist).accepted-old.completed_ids.length};
    if(old)return {kind:'rebaseline',value:null};
  }
  return {kind:'baseline',value:null};
}
export function deltaText(delta) {return delta.kind==='delta'?`${delta.value>0?'+':''}${delta.value} accepted since previous review`:delta.kind==='rebaseline'?'New definition · rebaseline':'First recorded baseline';}
export function filterFindings(findings,route) {const q=route.q.toLowerCase();return findings.filter(f=>(route.group==='all'||(Number(f.id)<=6?'reconstruction':'frontier')===route.group)&&(!q||[f.title,f.found,f.why,f.class].join(' ').toLowerCase().includes(q)));}
export const checklistById=(data,id)=>data.checklists.find(c=>c.id===id);
