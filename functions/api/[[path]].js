// Original request forwarding preserves origin, cookies and the backend access checks.
import A2 from '../_private169/A2.js';
import placement from '../_private169/placement.js';
import B1 from '../_private169/B1.js';
import B2 from '../_private169/B2.js';
import C1 from '../_private169/C1.js';
import C2 from '../_private169/C2.js';
const levelPacks={A2,B1,B2,C1,C2};
const placementBySource=new Map(placement.map(e=>[e.egyptian,e]));
function patched(response,data){const headers=new Headers(response.headers);headers.delete('Content-Length');headers.delete('Content-Encoding');headers.delete('ETag');headers.set('Cache-Control','private, no-store');return new Response(JSON.stringify(data),{status:response.status,statusText:response.statusText,headers})}
async function route303(context) {
 if(new URL(context.request.url).pathname.startsWith('/api/reminders/'))return context.env.YALLA_PUSH.fetch(context.request);
 const response=await context.env.YALLA_APP.fetch(context.request);
 const route=new URL(context.request.url).pathname;
 if(response.status!==200||!response.headers.get('content-type')?.includes('application/json'))return response;
 const level=route.match(/^\/api\/learning\/level\/(A2|B1|B2|C1|C2)$/);
 if(context.request.method==='GET'&&level&&levelPacks[level[1]]){
  let data;try{data=await response.clone().json()}catch{return response}
  if(!data?.content||data.content.schemaVersion!==2||data.content.level!==level[1]||!Array.isArray(data.content.units))return response;
  return patched(response,{...data,content:{...data.content,arabic169:{domain:'level-'+level[1],entries:levelPacks[level[1]]}}});
 }
 // A visible-only subset, never the placement dictionary or hidden answers.
 if(/^\/api\/placement\/(?:start$|attempt(?:\/|$))/.test(route)){
  let data;try{data=await response.clone().json()}catch{return response}
  if(data?.state!=='active'||!Array.isArray(data.items)||typeof data.attemptId!=='string')return response;
  const sources=new Set(data.items.flatMap(q=>[q.promptAr,q.questionAr]).filter(x=>typeof x==='string'));
  const entries=[...sources].map(s=>placementBySource.get(s)).filter(Boolean);
  if(entries.length)return patched(response,{...data,arabic169:{domain:'placement',entries}});
 }
 return response;
}

export async function onRequest(context){let r;try{r=await route303(context)}catch{r=new Response(JSON.stringify({error:'unavailable'}),{status:503,headers:{'Content-Type':'application/json; charset=utf-8','Cache-Control':'no-store'}})}const h=new Headers(r.headers);h.set('Strict-Transport-Security','max-age=31536000');h.set('X-Content-Type-Options','nosniff');h.set('X-Frame-Options','DENY');h.set('Referrer-Policy','no-referrer');return new Response(r.body,{status:r.status,statusText:r.statusText,headers:h})}
