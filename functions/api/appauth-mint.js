// Android app sign-in handoff, step 1 (runs in the system browser after normal Google sign-in).
// Validates the browser session with the backend, then stores it encrypted under a one-time code (60 s).
const H={'Content-Type':'application/json; charset=utf-8','Cache-Control':'no-store','X-Content-Type-Options':'nosniff','X-Robots-Tag':'noindex'};
const out=(o,s=200)=>new Response(JSON.stringify(o),{status:s,headers:H});
const SCHEMA='CREATE TABLE IF NOT EXISTS appauth(id TEXT PRIMARY KEY, sh TEXT NOT NULL, exp INTEGER NOT NULL, blob TEXT NOT NULL)';
const enc=new TextEncoder();
const hex=b=>[...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('');
const b64=b=>btoa(String.fromCharCode(...new Uint8Array(b)));
const sha=async s=>hex(await crypto.subtle.digest('SHA-256',enc.encode(s)));
export async function onRequestPost({request,env}){
  try{
    const url=new URL(request.url);
    if(request.headers.get('origin')!==url.origin||request.headers.get('x-yalla-app-handoff')!=='1')return out({error:'forbidden'},403);
    if(!env.STATS_DB||!env.YALLA_APP)return out({error:'unavailable'},503);
    const len=Number(request.headers.get('content-length')||0);if(len>300)return out({error:'bad request'},400);
    let body;try{body=await request.json()}catch{return out({error:'bad request'},400)}
    const state=String(body?.state||'');if(!/^[a-f0-9]{32}$/.test(state))return out({error:'bad state'},400);
    const cookie=request.headers.get('cookie')||'';if(!cookie)return out({error:'no session'},401);
    const r=await env.YALLA_APP.fetch(new Request(new URL('/api/me',request.url),{headers:{cookie,accept:'application/json'}}));
    if(r.status!==200)return out({error:'no session'},401);
    let m;try{m=await r.json()}catch{return out({error:'no session'},401)}
    if(!m||!m.user||!m.user.id)return out({error:'no session'},401);
    const raw=crypto.getRandomValues(new Uint8Array(32));const code=hex(raw);
    const id=await sha('id|'+code);
    const key=await crypto.subtle.importKey('raw',await crypto.subtle.digest('SHA-256',enc.encode('key|'+code)),'AES-GCM',false,['encrypt']);
    const iv=crypto.getRandomValues(new Uint8Array(12));
    const ct=await crypto.subtle.encrypt({name:'AES-GCM',iv},key,enc.encode(cookie));
    const now=Date.now();
    await env.STATS_DB.prepare(SCHEMA).run();
    await env.STATS_DB.prepare('DELETE FROM appauth WHERE exp<?').bind(now).run();
    await env.STATS_DB.prepare('INSERT INTO appauth(id,sh,exp,blob) VALUES(?,?,?,?)').bind(id,await sha('state|'+state),now+60000,b64(iv)+'.'+b64(ct)).run();
    return out({code,expiresIn:60});
  }catch{return out({error:'failed'},500)}
}
export const onRequest=c=>c.request.method==='POST'?onRequestPost(c):new Response('Not found',{status:404,headers:H});
