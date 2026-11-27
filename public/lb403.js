/* Leaderboard card on the home page. Opt-in with a chosen display name. No email is ever shown. */
(()=>{
  if(window.__lb403)return;window.__lb403=1;
  const app=document.getElementById('app');if(!app)return;
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  let data=null,loading=false,msg='',last=0;
  async function api(opts){const r=await fetch('/api/lb403',Object.assign({credentials:'same-origin',headers:{'Content-Type':'application/json'}},opts||{}));let j=null;try{j=await r.json()}catch(e){}return {ok:r.ok,status:r.status,j}}
  async function load(){if(loading)return;loading=true;try{const r=await api();if(r.ok){data=r.j;last=Date.now()}}catch(e){}loading=false;draw()}
  function html(){
    let h='<h2>لوحة المتصدرين</h2><p class="small">الترتيب بعدد الدروس اللي خلّصتها. الانضمام اختياري، وبيظهر الاسم المستعار بس، مش الإيميل.</p>';
    if(!data)return h+'<p class="small" role="status">بنحمّل اللوحة…</p>';
    if(data.top.length){h+='<ol class="lb403-list" style="list-style:none;padding:0;margin:8px 0">'+data.top.slice(0,10).map(r=>'<li style="display:flex;justify-content:space-between;gap:8px;padding:4px 0;'+(r.me?'font-weight:700':'')+'"><span>'+r.rank+'. '+esc(r.name)+'</span><span>'+r.score+' درس</span></li>').join('')+'</ol>'}
    else h+='<p class="small">لسه محدّش انضم. كن أول واحد!</p>';
    if(!data.signedIn)h+='<p class="small">سجّل دخول (زر دخول / حساب) عشان تنضم للّوحة.</p>';
    else if(data.mine)h+='<p class="small">ترتيبك: '+data.mine.rank+' باسم «'+esc(data.mine.name)+'» ('+data.mine.score+' درس)</p><button type="button" class="plain" data-lb403="leave">اخرج من اللوحة</button>';
    else h+='<label class="small" for="lb403-name">اختار اسم مستعار (٢ إلى ٢٠ حرف)</label><div style="display:flex;gap:8px;margin-top:4px;align-items:stretch;max-width:100%"><input id="lb403-name" maxlength="20" autocomplete="off" style="flex:1 1 0;min-width:0;width:100%;box-sizing:border-box"><button type="button" class="plain" style="flex:0 0 auto" data-lb403="join">انضم</button></div><p class="small">درسك المكتملة: '+(data.myScore||0)+'</p>';
    if(msg)h+='<p class="small" role="status">'+esc(msg)+'</p>';
    return h;
  }
  function draw(){const c=app.querySelector('#lb403');if(c)c.innerHTML=html()}
  function inject(){
    if(app.querySelector('#lb403'))return;
    if(location.hash&&location.hash!=='#'&&location.hash!=='#home')return;
    const t=[...app.querySelectorAll('h1,h2,h3,p,span,div')].find(e=>e.children.length===0&&/من التعلّم للحياة/.test(e.textContent||''));
    if(!t)return;
    let host=t;while(host.parentElement&&host.parentElement!==app&&host.parentElement.parentElement!==app)host=host.parentElement;
    const sec=document.createElement('section');sec.id='lb403';sec.className='card';sec.style.margin='12px 0';sec.innerHTML=html();
    host.parentElement.insertBefore(sec,host);
    if(!data||Date.now()-last>60000)load();
  }
  app.addEventListener('click',async e=>{
    const b=e.target.closest('[data-lb403]');if(!b)return;e.stopPropagation();
    if(b.dataset.lb403==='leave'){const r=await api({method:'POST',body:JSON.stringify({leave:true})});if(r.ok){data=r.j;msg='خرجت من اللوحة.'}else msg='حصلت مشكلة، جرّب تاني.';draw();return}
    const name=(app.querySelector('#lb403-name')||{}).value||'';
    const r=await api({method:'POST',body:JSON.stringify({name})});
    if(r.ok){data=r.j;msg='اتضفت للوحة.'}else msg=r.status===409?'الاسم ده مستخدم، اختار غيره.':r.status===400?'الاسم لازم يكون ٢ إلى ٢٠ حرف، من غير روابط أو إيميلات.':r.status===401?'سجّل دخول الأول.':'حصلت مشكلة، جرّب تاني.';
    draw();
  },true);
  let pend=false;new MutationObserver(()=>{if(pend)return;pend=true;setTimeout(()=>{pend=false;inject()},80)}).observe(app,{childList:true,subtree:true});
  inject();
})();
