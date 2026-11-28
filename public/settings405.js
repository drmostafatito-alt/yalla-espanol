/* Settings additions: auto-read switch and per-level progress reset (with a confirm step).
   Wraps settings() like the earlier settings layers. Existing handlers and values stay as they are. */
(()=>{'use strict';
if(typeof settings!=='function')return;
let pending=null;
const prev=settings;
const NUM=n=>Number(n).toLocaleString('ar-EG');
function levels(){const m={};for(const l of LESSONS){const k=l.level||'A1';(m[k]=m[k]||[]).push(l)}return m}
function stats(level){const ls=levels()[level]||[];let done=0,words=0;for(const l of ls){if(state.completed&&state.completed[l.id])done++;for(const w of l.words||[])if(state.words&&state.words[w.id])words++}return{lessons:ls.length,done,words}}
function autoOn(){return !(state.settings&&state.settings.autoread===false)}
function resetCard(){
  const lv=levels(),keys=Object.keys(lv).filter(k=>stats(k).done>0||stats(k).words>0);
  const sec=document.createElement('section');sec.className='card settings405-danger';
  let h='<h2><span class="settings405-ico" aria-hidden="true">!</span>منطقة الحذر</h2><p class="settings228-caption">حاجات مفيش رجوع فيها</p>';
  if(state.account){
    h+='<p class="small">حسابك متزامن، وتقدمك بيرجع من الحساب بعد المزامنة. علشان كده مسح مستوى مش متاح وإنت داخل بحسابك. اخرج من الحساب الأول لو عايز تبدأ مستوى من الأول على الجهاز.</p>';
  }else if(!keys.length){
    h+='<p class="small">لسه ما خلصتش دروس تتمسح. لما تبدأ هتلاقي هنا إمكانية تبدأ أي مستوى من الأول.</p>';
  }else{
    h+='<div class="setting"><label for="reset-level405">ابدأ مستوى من الأول</label><select id="reset-level405" data-reset-level405>'+keys.map(k=>'<option value="'+k+'"'+(pending===k?' selected':'')+'>'+k+'</option>').join('')+'</select><p class="small">بيمسح دروسك المخلصة وتقدّم كلماتك في المستوى ده بس. نقاطك وسلسلة أيامك وباقي المستويات مش بتتأثر.</p>';
    if(pending){const s=stats(pending);h+='<div class="settings405-confirm" role="alertdialog" aria-live="assertive"><p><strong>متأكد؟</strong> هيتمسح تقدمك في مستوى '+pending+': '+NUM(s.done)+' درس مخلص و'+NUM(s.words)+' كلمة في المراجعة. مفيش رجوع.</p><div class="rowgap"><button class="btn danger405" data-reset405="confirm">أيوه، امسح</button><button class="btn secondary" data-reset405="cancel">إلغاء</button></div></div>'}
    else h+='<button class="btn secondary danger405-outline" data-reset405="ask">امسح تقدم المستوى</button>';
    h+='</div>';
  }
  sec.innerHTML=h;return sec;
}
settings=function(){
  const t=document.createElement('template');t.innerHTML=prev();
  const controls=t.content.querySelector('.settings170-controls');
  if(controls){const d=document.createElement('div');d.className='setting setting405-auto';
    d.innerHTML='<label class="switch405"><span>اقرأ بصوت عالي أول ما السؤال يظهر</span><input type="checkbox" role="switch" data-set405="autoread"'+(autoOn()?' checked':'')+'><i aria-hidden="true"></i></label><p class="small">في تمارين السمع والكتابة بيتنطق النص لوحده أول ما يظهر. تقدر تضغط السماعة تسمعه تاني، وتقفل ده من هنا.</p>';
    controls.prepend(d)}
  const grid=t.content.querySelector('.settings170-grid');
  if(grid){const sec=document.createElement('section');sec.className='settings301-group settings405-group';sec.append(resetCard());grid.append(sec)}
  return t.innerHTML;
};
document.addEventListener('change',e=>{
  const el=e.target;
  if(el&&el.matches&&el.matches('[data-set405="autoread"]')){state.settings=state.settings||{};state.settings.autoread=!!el.checked;save();}
  else if(el&&el.matches&&el.matches('[data-reset-level405]')){pending=pending?el.value:null}
});
document.addEventListener('click',e=>{
  const b=e.target.closest&&e.target.closest('[data-reset405]');if(!b)return;
  const a=b.dataset.reset405,sel=document.querySelector('[data-reset-level405]');
  if(a==='ask'&&sel){pending=sel.value;render();const c=document.querySelector('.settings405-confirm');if(c)c.scrollIntoView({block:'center'})}
  else if(a==='cancel'){pending=null;render()}
  else if(a==='confirm'&&pending&&!state.account){
    const level=pending;const ls=levels()[level]||[];
    for(const l of ls){delete state.completed[l.id];if(state.short143)delete state.short143[l.id];for(const w of l.words||[])delete state.words[w.id]}
    if(state.formative){const pre=level.toLowerCase()+'-';for(const k of Object.keys(state.formative))if(k.startsWith(pre))delete state.formative[k]}
    pending=null;save();render();
    if(typeof toast==='function')toast('اتمسح تقدم مستوى '+level+'. تقدر تبدأ من الأول.');
  }
});
if(location.hash==='#settings')render();
})();
