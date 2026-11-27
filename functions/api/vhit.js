// Counts one visitor per device per day (Cairo day). No IP, no cookies, no personal data stored.
const BOT=/bot|crawl|spider|slurp|headless|lighthouse|pagespeed|preview|facebookexternalhit|curl|wget|python|node-fetch/i;
const cairoDay=(d=new Date())=>new Intl.DateTimeFormat('en-CA',{timeZone:'Africa/Cairo',year:'numeric',month:'2-digit',day:'2-digit'}).format(d);
export async function onRequestPost({request,env}){
  const h={'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'};
  try{
    if(BOT.test(request.headers.get('user-agent')||''))return new Response(null,{status:204,headers:h});
    const len=Number(request.headers.get('content-length')||0);if(len>200)return new Response(null,{status:204,headers:h});
    const body=await request.json();const id=String(body?.id||'');
    if(!/^[a-f0-9]{16,40}$/.test(id)||!env.STATS_DB)return new Response(null,{status:204,headers:h});
    const now=Date.now();
    if(!body.hb)await env.STATS_DB.prepare('INSERT OR IGNORE INTO visits(day,vid) VALUES(?,?)').bind(cairoDay(),id).run();
    await env.STATS_DB.prepare('INSERT INTO online(vid,ts) VALUES(?,?) ON CONFLICT(vid) DO UPDATE SET ts=excluded.ts').bind(id,now).run();
    if(Math.random()<0.01)await env.STATS_DB.prepare('DELETE FROM online WHERE ts<?').bind(now-3600000).run();
  }catch{}
  return new Response(null,{status:204,headers:h});
}
export const onRequest=async c=>c.request.method==='POST'?onRequestPost(c):new Response('Not found',{status:404,headers:{'Cache-Control':'no-store'}});
