/* Visitor count: one anonymous ping per device per day, plus an owner-only card in the owner panel. */
(()=>{'use strict';
try{
  if(!navigator.webdriver&&!/^\/admin254/.test(location.pathname)){
    const day=new Intl.DateTimeFormat('en-CA',{timeZone:'Africa/Cairo',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
    let id=localStorage.getItem('yvid');
    if(!/^[a-f0-9]{16,40}$/.test(id||'')){const a=new Uint8Array(12);crypto.getRandomValues(a);id=[...a].map(b=>b.toString(16).padStart(2,'0')).join('');localStorage.setItem('yvid',id)}
    if(localStorage.getItem('yvday')!==day){
      fetch('/api/vhit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id}),keepalive:true,cache:'no-store'})
        .then(r=>{if(r.ok)localStorage.setItem('yvday',day)}).catch(()=>{});
    }
  }
  const hb=()=>{if(document.visibilityState==='hidden')return;const id=localStorage.getItem('yvid');if(!/^[a-f0-9]{16,40}$/.test(id||''))return;fetch('/api/vhit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id,hb:true}),keepalive:true,cache:'no-store'}).catch(()=>{})};
  if(!navigator.webdriver&&!/^\/admin254/.test(location.pathname)){setTimeout(hb,4000);setInterval(hb,120000);document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')hb()})}
}catch{}
const n=v=>Number(v||0).toLocaleString('ar-EG');
function mount(root){
  try{
    const host=root.querySelector('[data-admin-section258="overview"]');
    if(!host||host.querySelector('.visits403'))return;
    const box=document.createElement('div');box.className='visits403';
    const h=document.createElement('h3');h.textContent='زوار الموقع';
    const note=document.createElement('p');note.className='note';note.textContent='كل جهاز بيتحسب مرة واحدة في اليوم (بتوقيت القاهرة). بدون أي بيانات شخصية.';
    const live=document.createElement('div');live.className='metric';const liveN=document.createElement('strong');liveN.textContent='…';const liveL=document.createElement('span');liveL.textContent='على الموقع دلوقتي (آخر ٥ دقايق)';live.append(liveN,liveL);
    const grid=document.createElement('div');grid.className='metrics';grid.append(live);
    const extra=document.createElement('div');
    box.append(h,note,grid,extra);host.append(box);
    const metric=(label,value)=>{const d=document.createElement('div');d.className='metric';const b=document.createElement('strong');b.textContent=n(value);const s=document.createElement('span');s.textContent=label;d.append(b,s);return d};
    const table=(title,rows)=>{const w=document.createElement('div');const t=document.createElement('h4');t.textContent=title;w.append(t);for(const[a,b]of rows){const p=document.createElement('p');p.textContent=a+' · '+n(b)+' زائر';w.append(p)}return w};
    let last=0,busy=false;
    async function load(){
      if(busy||Date.now()-last<60000)return;const panel=root.querySelector('#panel');if(!panel||panel.hidden)return;
      busy=true;try{
        const r=await fetch('/api/vstats',{cache:'no-store',credentials:'same-origin'});
        if(!r.ok)return;const d=await r.json();last=Date.now();
        liveN.textContent=n(d.online);grid.replaceChildren(live,metric('اليوم',d.today),metric('امبارح',d.yesterday),metric('آخر ٧ أيام',d.last7),metric('آخر ٣٠ يوم',d.last30),metric('الإجمالي (أجهزة مختلفة)',d.total));
        extra.replaceChildren(
          table('حسب اليوم (آخر ١٤ يوم)',d.days.map(x=>[x.day,x.visitors])),
          table('حسب الأسبوع (بداية الأسبوع الاثنين)',d.weeks.map(x=>[x.weekStart,x.visitors])),
          table('حسب الشهر',d.months.map(x=>[x.month,x.visitors])));
      }catch{}finally{busy=false}
    }
    async function pollLive(){const panel=root.querySelector('#panel');if(!panel||panel.hidden||document.visibilityState==='hidden')return;try{const r=await fetch('/api/vstats?live=1',{cache:'no-store',credentials:'same-origin'});if(r.ok){const d=await r.json();liveN.textContent=n(d.online)}}catch{}}
    const t=setInterval(()=>{if(!host.isConnected){clearInterval(t);clearInterval(t2);return}load()},2000);const t2=setInterval(pollLive,10000);load();setTimeout(pollLive,1500);
    root.querySelector('#refresh')?.addEventListener('click',()=>{last=0;setTimeout(load,300)});
  }catch{}
}
let real=globalThis.mountOwner300;
const wrap=f=>function(root){const r=f.apply(this,arguments);try{let tries=0;const w=setInterval(()=>{mount(root);if(root.querySelector('.visits403')||++tries>120)clearInterval(w)},1000)}catch{}return r};
if(typeof real==='function')real=wrap(real);
Object.defineProperty(globalThis,'mountOwner300',{configurable:true,get:()=>real,set:v=>{real=typeof v==='function'?wrap(v):v}});
})();
