// Owner-only visitor numbers. Access is the existing admin session, checked against the backend.
const headers={'Content-Type':'application/json; charset=utf-8','Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff','X-Robots-Tag':'noindex'};
const day=(d=new Date())=>new Intl.DateTimeFormat('en-CA',{timeZone:'Africa/Cairo',year:'numeric',month:'2-digit',day:'2-digit'}).format(d);
const shift=(s,n)=>{const d=new Date(s+'T12:00:00Z');d.setUTCDate(d.getUTCDate()+n);return d.toISOString().slice(0,10)};
export async function onRequestGet({request,env}){
  const deny=()=>new Response(JSON.stringify({error:'unauthorized'}),{status:401,headers});
  try{
    const cookie=request.headers.get('cookie')||'';
    if(!cookie)return deny();
    const me=await env.YALLA_APP.fetch(new Request(new URL('/api/admin254/me',request.url),{headers:{cookie,accept:'application/json'}}));
    if(me.status!==200)return deny();
    let m;try{m=await me.json()}catch{return deny()}
    if(!m||typeof m!=='object'||m.error)return deny();
    if(!env.STATS_DB)return new Response(JSON.stringify({error:'not-configured'}),{status:503,headers});
    const t=day(),db=env.STATS_DB;
    const online=(await db.prepare('SELECT COUNT(*) n FROM online WHERE ts>=?').bind(Date.now()-300000).first())?.n||0;
    if(new URL(request.url).searchParams.get('live')==='1')return new Response(JSON.stringify({online}),{headers});
    const one=async(sql,...b)=>(await db.prepare(sql).bind(...b).first())?.n||0;
    const since=n=>one('SELECT COUNT(DISTINCT vid) n FROM visits WHERE day>=?',shift(t,-n));
    const [today,yesterday,last7,last30,total,days,weeks,months]=await Promise.all([
      one('SELECT COUNT(*) n FROM visits WHERE day=?',t),one('SELECT COUNT(*) n FROM visits WHERE day=?',shift(t,-1)),
      since(6),since(29),one('SELECT COUNT(DISTINCT vid) n FROM visits'),
      db.prepare('SELECT day,COUNT(*) n FROM visits WHERE day>=? GROUP BY day ORDER BY day DESC').bind(shift(t,-13)).all(),
      db.prepare("SELECT date(day,'-6 days','weekday 1') w,COUNT(DISTINCT vid) n FROM visits WHERE day>=? GROUP BY w ORDER BY w DESC").bind(shift(t,-56)).all(),
      db.prepare('SELECT substr(day,1,7) mth,COUNT(DISTINCT vid) n FROM visits WHERE day>=? GROUP BY mth ORDER BY mth DESC').bind(shift(t,-180)).all()]);
    return new Response(JSON.stringify({asOf:t,online,today,yesterday,last7,last30,total,
      days:days.results.map(r=>({day:r.day,visitors:r.n})),weeks:weeks.results.map(r=>({weekStart:r.w,visitors:r.n})),months:months.results.map(r=>({month:r.mth,visitors:r.n}))}),{headers});
  }catch{return new Response(JSON.stringify({error:'unavailable'}),{status:503,headers})}
}
export const onRequest=c=>c.request.method==='GET'?onRequestGet(c):new Response('Not found',{status:404,headers:{'Cache-Control':'no-store'}});
