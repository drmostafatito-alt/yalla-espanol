/* Settings redesign (preview): welcome fox, search, live preview, titled sections with icons, account + danger zones.
   Wraps settings() on top of the earlier layers. No data or storage format changes except a local text-size key. */
(()=>{'use strict';
if(typeof settings!=='function')return;
const prev=settings,FSKEY='yalla.fontsize406',SIZES=[['١','عادي',1],['٢','كبير',1.12],['٣','كبير جدًا',1.25]];
const sizeIdx=()=>{const v=Number(localStorage.getItem(FSKEY));return v>=0&&v<3?v:0};
function applySize(i){document.documentElement.style.setProperty('--fs406',String(SIZES[i][2]));document.documentElement.classList.toggle('fs406-on',i>0)}
applySize(sizeIdx());
const SVG={'user': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/></svg>', 'target': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/></svg>', 'phone': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/></svg>', 'info': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><circle cx="12" cy="7.8" r=".6"/></svg>', 'eye': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>'};
const ICONS={'حسابك وبياناتك':SVG.user,'التعلّم على راحتك':SVG.target,'على جهازك':SVG.phone,'عن الموقع والمساعدة':SVG.info};
const speedLabel=()=>{const sel=document.getElementById('speed');if(sel&&sel.selectedOptions[0])return sel.selectedOptions[0].textContent.trim();return ''};
function nameOf(){const e=state.account&&state.account.email;return e?e.split('@')[0]:''}
function hero(){
  const n=nameOf(),fox=typeof foxMarkup==='function'?foxMarkup('idle'):'';
  return '<section class="s406-hero" aria-live="polite"><div class="s406-fox" id="s406-fox">'+fox+'</div><div><strong id="s406-msg">'+(n?'أهلاً يا '+n+'!':'أهلاً بيك!')+'</strong><span>اظبط يلا أسباني على مزاجك. أي تغيير بيتحفظ لوحده.</span></div></section>'+
  '<div class="s406-search"><input id="s406-q" type="search" placeholder="دوّر في الإعدادات" aria-label="دوّر في الإعدادات" autocomplete="off"></div><p class="s406-empty" id="s406-empty" hidden>مفيش إعداد بالاسم ده.</p>';
}
function preview(){
  const i=sizeIdx();
  return '<section class="card s406-preview" data-s406="preview"><h2><span class="s406-ico" aria-hidden="true">'+SVG.eye+'</span>معاينة مباشرة</h2>'+
  '<div class="s406-sample" id="s406-sample"><div class="s406-es" lang="es" dir="ltr">Hola, ¿cómo estás hoy?</div><div class="s406-ar">أهلاً، إزيك النهارده؟</div>'+
  '<button class="btn secondary s406-play" data-action="audio" data-text="Hola, ¿cómo estás hoy?" aria-label="شغّل الجملة">◖)) <span id="s406-speed">سرعة النطق</span></button></div>'+
  '<div class="s406-seg" role="group" aria-label="حجم الخط">'+SIZES.map((s,k)=>'<button type="button" class="s406-size" data-s406size="'+k+'" aria-pressed="'+(k===i)+'"><b>'+(k===0?'أ':k===1?'أ':'أ')+'</b><span>'+s[1]+'</span></button>').join('')+'</div></section>';
}
settings=function(){
  const t=document.createElement('template');t.innerHTML=prev();const root=t.content;
  const h1=root.querySelector('h1');
  if(h1){const holder=document.createElement('div');holder.innerHTML=hero();let anchor=h1.nextElementSibling&&h1.nextElementSibling.tagName==='P'?h1.nextElementSibling:h1;while(holder.lastChild)anchor.after(holder.lastChild)}
  root.querySelectorAll('.settings301-group-title').forEach(el=>{const k=el.textContent.trim();if(ICONS[k]&&!el.querySelector('.s406-gico'))el.insertAdjacentHTML('afterbegin','<span class="s406-gico" aria-hidden="true">'+ICONS[k]+'</span>')});
  // account header
  const acc=root.querySelector('#account-box');
  if(acc&&state.account){const e=state.account.email||'';acc.insertAdjacentHTML('afterbegin','<div class="s406-who"><span class="s406-avatar" aria-hidden="true">'+(e[0]||'?').toUpperCase()+'</span><div><strong>'+nameOf()+'</strong><small dir="ltr">'+e+'</small></div></div>')}
  // preview card goes after the audio card
  const audio=root.querySelector('.settings170-audio');
  if(audio){const d=document.createElement('div');d.innerHTML=preview();audio.after(d.firstChild)}
  // danger zone: gather delete-account into the reset card
  const danger=root.querySelector('.settings405-danger'),del=acc&&acc.querySelector('details');
  if(danger){danger.classList.add('s406-danger');if(del){const w=document.createElement('div');w.className='s406-delwrap';w.appendChild(del);danger.appendChild(w)}}
  return t.innerHTML;
};
function filter(q){
  const root=document.querySelector('#app');if(!root)return;q=q.trim().toLowerCase();let any=false;
  root.querySelectorAll('.settings301-group').forEach(g=>{let vis=0;g.querySelectorAll('.card').forEach(c=>{const m=!q||c.textContent.toLowerCase().includes(q)||g.querySelector('.settings301-group-title')?.textContent.toLowerCase().includes(q)&&false;c.hidden=!m;if(m)vis++});g.hidden=!vis;if(vis)any=true});
  const e=document.getElementById('s406-empty');if(e)e.hidden=any||!q;
}
let tm=0;
function react(msg){
  const f=document.getElementById('s406-fox'),m=document.getElementById('s406-msg');if(!f||!m)return;
  const n=f.firstElementChild;if(n&&typeof foxPose==='function')foxPose(n,'correct');m.textContent=msg;
  clearTimeout(tm);tm=setTimeout(()=>{const n2=document.getElementById('s406-fox')?.firstElementChild;if(n2&&typeof foxPose==='function')foxPose(n2,'idle');const m2=document.getElementById('s406-msg');if(m2)m2.textContent=nameOf()?'أهلاً يا '+nameOf()+'!':'أهلاً بيك!'},2200);
}
document.addEventListener('input',e=>{if(e.target&&e.target.id==='s406-q')filter(e.target.value)});
document.addEventListener('change',e=>{
  const el=e.target;if(!el||!el.matches)return;
  if(el.matches('[data-setting],[data-set405]')){
    if(el.id==='speed'||el.dataset.setting==='speed'){setTimeout(()=>{const s=document.getElementById('s406-speed');if(s)s.textContent='سرعة النطق: '+speedLabel()},50)}
    react('تمام، اتحفظ ✓');
  }
});
document.addEventListener('click',e=>{
  const b=e.target.closest&&e.target.closest('[data-s406size]');if(!b)return;
  const i=Number(b.dataset.s406size);localStorage.setItem(FSKEY,String(i));applySize(i);
  document.querySelectorAll('[data-s406size]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));react('تمام، الخط بقى '+SIZES[i][1]);
});
document.addEventListener('DOMContentLoaded',()=>{});
new MutationObserver(()=>{const s=document.getElementById('s406-speed');if(s&&!s.dataset.set){s.dataset.set=1;const l=speedLabel();if(l)s.textContent='سرعة النطق: '+l}}).observe(document.documentElement,{childList:true,subtree:true});
if(location.hash==='#settings'&&typeof render==='function')render();
})();
