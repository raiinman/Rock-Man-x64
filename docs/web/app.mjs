import {parseRoute,routeHref,verifyDocument,verifyManifest} from './model.mjs';
import {renderShell,renderError} from './views.mjs';
export async function fetchReviewed(fetcher=globalThis.fetch,signal) {
  const base=new URL('./data/',import.meta.url);
  const request=url=>fetcher(url,{cache:'no-cache',credentials:'omit',signal});
  const [evidence,response,built]=await Promise.all([request(new URL('dashboard-data.json',base)),request(new URL('tracker-state.json',base)),request(new URL('./build-manifest.json',import.meta.url))]);
  if(!evidence.ok||!response.ok||!built.ok)throw new Error('The published evidence files are unavailable.');
  const [raw,receiptRaw,manifest]=await Promise.all([evidence.text(),response.text(),built.json()]);
  const state=JSON.parse(receiptRaw),data=await verifyDocument(raw,state);
  await verifyManifest(manifest,raw,receiptRaw);
  if(manifest.evidence_review_id!==data.last_evidence_review.review_id)throw new Error('The deployed manifest and evidence review disagree.');
  return {data,state,sourceRevision:manifest.source_revision};
}
export function startApp(doc,win,loader=fetchReviewed,options={}) {
  const mount=doc.getElementById('app');let snapshot=null,request=0,controller=null,timer=null,pendingQuery=null,lastPage=null,lastItem=null,disposed=false;
  function draw(){if(!snapshot||disposed)return;const route=parseRoute(win.location.hash);const active=doc.activeElement,restore=active?.id==='tracker-search'?{start:active.selectionStart,end:active.selectionEnd}:null;const control=active?.dataset?.route?{key:active.dataset.route,value:active.dataset.value}:null;
    mount.innerHTML=renderShell(snapshot.data,snapshot.state,route,Boolean(options.preview),options.sourceRevision??snapshot.sourceRevision??'');
    doc.title=`Rock Man x64 — ${route.page==='overview'?'Project & progress':route.page[0].toUpperCase()+route.page.slice(1)}`;
    if(restore){const input=doc.getElementById('tracker-search');input?.focus({preventScroll:true});input?.setSelectionRange?.(restore.start,restore.end);}
    else if(lastPage!==null&&lastPage!==route.page){doc.getElementById('page-title')?.focus({preventScroll:true});win.scrollTo?.({top:0,behavior:'instant'});}
    else if(control){[...(mount.querySelectorAll?.('[data-route]')??[])].find(el=>el.dataset.route===control.key&&el.dataset.value===control.value)?.focus({preventScroll:true});}
    if(route.item&&!restore){const prefix={overview:'heat-detail-',roadmap:'milestone-',workstreams:'stream-',findings:'finding-'}[route.page];if(prefix){const target=doc.getElementById(prefix+route.item);target?.scrollIntoView?.({block:'start',behavior:'instant'});(route.page==='overview'?target:(target?.querySelector?.('summary')??target))?.focus?.({preventScroll:true});}}
    if(route.page==='overview'&&!route.item&&lastPage==='overview'&&lastItem&&!restore&&!control)doc.getElementById('heat-cell-'+lastItem)?.focus();
    lastPage=route.page;lastItem=route.item;
  }
  function navigate(changes,replace=false){const current=parseRoute(win.location.hash);const samePage=!changes.page||changes.page===current.page;const query=samePage&&pendingQuery!==null&&!('q' in changes)?{q:pendingQuery}:{};win.clearTimeout(timer);pendingQuery=null;const route={...current,...query,...changes};if(!('item' in changes))route.item='';const next=routeHref(route);if(replace){win.history.replaceState(null,'',next);draw();}else if(win.location.hash===next)draw();else win.location.hash=next;}
  async function load(){const serial=++request;controller?.abort();controller=new AbortController();try{const result=await loader(undefined,controller.signal);if(serial!==request||disposed)return;snapshot=result;draw();}catch(error){if(serial!==request||disposed||error.name==='AbortError')return;snapshot=null;mount.innerHTML=renderError(error.message||'An unknown data error occurred.');}}
  function click(event){if(event.target.closest?.('a[href="#content"]')){event.preventDefault();doc.getElementById('content')?.focus();return;}const retry=event.target.closest?.('[data-retry]');if(retry){load();return;}const control=event.target.closest?.('[data-route]');if(control){const key=control.dataset.route;if(['status','view','group'].includes(key))navigate({[key]:control.dataset.value});}}
  function input(event){if(!event.target.matches?.('[data-search]'))return;win.clearTimeout(timer);const value=event.target.value;pendingQuery=value;timer=win.setTimeout(()=>navigate({q:value},true),150);}
  function keydown(event){const route=parseRoute(win.location.hash);if(event.key==='Escape'&&route.page==='overview'&&route.item){event.preventDefault();navigate({item:''});}}
  function hash(){win.clearTimeout(timer);pendingQuery=null;draw();}
  doc.addEventListener('click',click);doc.addEventListener('keydown',keydown);mount.addEventListener('input',input);win.addEventListener('hashchange',hash);load();
  return {reload:load,navigate,draw,destroy(){disposed=true;request++;controller?.abort();win.clearTimeout(timer);doc.removeEventListener('click',click);doc.removeEventListener('keydown',keydown);mount.removeEventListener('input',input);win.removeEventListener('hashchange',hash);},getSnapshot:()=>snapshot};
}
if(typeof document!=='undefined')startApp(document,window);
