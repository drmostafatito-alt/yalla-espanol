// Opt-in leaderboard. Identity comes from the existing session (checked by the backend). Score = lessons completed, read from the learner's synced progress.
const H={'Content-Type':'application/json; charset=utf-8','Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff','X-Robots-Tag':'noindex'};
const out=(o,s=200)=>new Response(JSON.stringify(o),{status:s,headers:H});
const SCHEMA='CREATE TABLE IF NOT EXISTS lb403(uid TEXT PRIMARY KEY, name TEXT NOT NULL, score INTEGER NOT NULL DEFAULT 0, updated_at INTEGER NOT NULL)';
async function who(request,env){
  const cookie=request.headers.get('cookie')||'';if(!cookie)return null;
  const r=await env.YALLA_APP.fetch(new Request(new URL('/api/me',request.url),{headers:{cookie,accept:'application/json'}}));
  if(r.status!==200)return null;let m;try{m=await r.json()}catch{return null}
  if(!m||!m.user||!m.user.id)return null;
  const c=m.progress&&typeof m.progress.completed==='object'&&m.progress.completed?Object.keys(m.progress.completed).length:0;
  return {uid:String(m.user.id),score:Math.min(c,100000)};
}
const cleanName=s=>{s=String(s||'').normalize('NFKC').replace(/\s+/g,' ').trim();if(s.length<2||s.length>20)return null;if(!/^[\p{L}\p{N} ._-]+$/u.test(s))return null;if(/@|https?:|www\./i.test(s))return null;return s};
async function board(db,me){
  const top=(await db.prepare('SELECT uid,name,score FROM lb403 ORDER BY score DESC, updated_at ASC LIMIT 20').all()).results||[];
  let mine=null;
  if(me){const r=await db.prepare('SELECT name,score FROM lb403 WHERE uid=?').bind(me.uid).first();
    if(r){const rank=((await db.prepare('SELECT COUNT(*) n FROM lb403 WHERE score>? OR (score=? AND updated_at<(SELECT updated_at FROM lb403 WHERE uid=?))').bind(r.score,r.score,me.uid).first())?.n||0)+1;mine={name:r.name,score:r.score,rank}}}
  return {top:top.map((r,i)=>({rank:i+1,name:r.name,score:r.score,me:!!(me&&r.uid===me.uid)})),mine,signedIn:!!me,myScore:me?me.score:null};
}
export async function onRequest({request,env}){
  try{
    if(!env.STATS_DB)return out({error:'not-configured'},503);
    const db=env.STATS_DB;await db.prepare(SCHEMA).run();
    const me=await who(request,env);
    if(request.method==='GET'){
      if(me)await db.prepare('UPDATE lb403 SET score=?,updated_at=? WHERE uid=? AND score<>?').bind(me.score,Date.now(),me.uid,me.score).run();
      return out(await board(db,me));
    }
    if(request.method==='POST'){
      if(!me)return out({error:'signin'},401);
      if((request.headers.get('origin')||'')&&new URL(request.headers.get('origin')).host!==new URL(request.url).host)return out({error:'origin'},403);
      let b;try{b=await request.json()}catch{return out({error:'bad'},400)}
      if(b&&b.leave===true){await db.prepare('DELETE FROM lb403 WHERE uid=?').bind(me.uid).run();return out(await board(db,me))}
      const name=cleanName(b&&b.name);if(!name)return out({error:'name'},400);
      const taken=await db.prepare('SELECT uid FROM lb403 WHERE lower(name)=lower(?) AND uid<>?').bind(name,me.uid).first();
      if(taken)return out({error:'taken'},409);
      await db.prepare('INSERT INTO lb403(uid,name,score,updated_at) VALUES(?,?,?,?) ON CONFLICT(uid) DO UPDATE SET name=excluded.name,score=excluded.score,updated_at=excluded.updated_at').bind(me.uid,name,me.score,Date.now()).run();
      return out(await board(db,me));
    }
    return new Response('Not found',{status:404,headers:{'Cache-Control':'no-store'}});
  }catch(e){return out({error:'unavailable'},503)}
}
