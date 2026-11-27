// Android app sign-in handoff, step 2 (called by the app's WebView): one-time code + state -> session cookie.
const H={'Content-Type':'application/json; charset=utf-8','Cache-Control':'no-store','X-Content-Type-Options':'nosniff','X-Robots-Tag':'noindex'};
const out=(o,s=200,x)=>{const h=new Headers(H);if(x)for(const c of x)h.append('Set-Cookie',c);return new Response(JSON.stringify(o),{status:s,headers:h})};
const SCHEMA='CREATE TABLE IF NOT EXISTS appauth(id TEXT PRIMARY KEY, sh TEXT NOT NULL, exp INTEGER NOT NULL, blob TEXT NOT NULL)';
const enc=new TextEncoder();
const hex=b=>[...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('');
const unb64=s=>Uint8Array.from(atob(s),c=>c.charCodeAt(0));
const sha=async s=>hex(await crypto.subtle.digest('SHA-256',enc.encode(s)));
export async function onRequestPost({request,env}){
  try{
    const url=new URL(request.url);
    if(request.headers.get('origin')!==url.origin||request.headers.get('x-yalla-app-handoff')!=='1')return out({error:'forbidden'},403);
    if(!env.STATS_DB)return out({error:'unavailable'},503);
    const len=Number(request.headers.get('content-length')||0);if(len>300)return out({error:'bad request'},400);
    let body;try{body=await request.json()}catch{return out({error:'bad request'},400)}
    const code=String(body?.code||''),state=String(body?.state||'');
    if(!/^[a-f0-9]{64}$/.test(code)||!/^[a-f0-9]{32}$/.test(state))return out({error:'bad code'},400);
    const id=await sha('id|'+code),now=Date.now();
    await env.STATS_DB.prepare(SCHEMA).run();
    // Atomic single use: the row is deleted by the first request that reads it.
    const row=await env.STATS_DB.prepare('DELETE FROM appauth WHERE id=? RETURNING sh,exp,blob').bind(id).first();
    if(!row||row.exp<now||row.sh!==await sha('state|'+state))return out({error:'invalid or expired'},400);
    const [iv,ct]=row.blob.split('.');
    const key=await crypto.subtle.importKey('raw',await crypto.subtle.digest('SHA-256',enc.encode('key|'+code)),'AES-GCM',false,['decrypt']);
    const cookie=new TextDecoder().decode(await crypto.subtle.decrypt({name:'AES-GCM',iv:unb64(iv)},key,unb64(ct)));
    const set=[];
    for(const pair of cookie.split(/;\s*/)){const i=pair.indexOf('=');if(i<1)continue;const n=pair.slice(0,i),v=pair.slice(i+1);if(!/^[A-Za-z0-9_.-]{1,64}$/.test(n)||/[\s;,"\\]/.test(v)||v.length>2048)continue;set.push(`${n}=${v}; Path=/; Max-Age=2592000; HttpOnly; Secure; SameSite=Lax`)}
    if(!set.length)return out({error:'invalid'},400);
    return out({ok:true},200,set);
  }catch{return out({error:'failed'},500)}
}
export const onRequest=c=>c.request.method==='POST'?onRequestPost(c):new Response('Not found',{status:404,headers:H});
