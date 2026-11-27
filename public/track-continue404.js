/* Per-track "continue your lesson". Never shows another path's session inside a track,
   and adds the track's own continue card at the top of the track page. Main path card is untouched. */
(()=>{
 if(typeof render!=='function'||typeof activeJob!=='function'||typeof ALL_LESSONS==='undefined')return;
 const baseRender=render;
 const courseOf=id=>{const l=ALL_LESSONS.find(x=>x.id===id);return l?(l.sectionId||'main'):null};
 function homeIsMain(){
  try{
   const h=(location.hash.slice(1)||'home').split('/')[0];
   if(h==='home'&&activeCourseId!=='main')chooseCourse('main');
  }catch{}
 }
 function guard(){
  try{
   const h=(location.hash.slice(1)||'home').split('/')[0];
   homeIsMain();
   if(h==='lesson'||h==='practice')return;
   const s=state.session;
   if(s&&s.lessonId){
    const c=courseOf(s.lessonId);
    if(c&&c!==activeCourseId){
     state.sessions=state.sessions||{};
     if(!state.sessions[c])state.sessions[c]=s;
     state.session=state.sessions[activeCourseId]||null;
     save(false);
    }
   }
  }catch{}
 }
 function trackCard(){
  try{
   const job=activeJob();if(!job||view.page!=='path')return;
   const root=document.getElementById('app');if(!root||root.querySelector('.track-continue404'))return;
   const list=LESSONS;if(!Array.isArray(list)||!list.length)return;
   let lesson=state.session&&state.session.lessonId?list.find(l=>l.id===state.session.lessonId):null;
   const started=!!lesson||list.some(l=>state.completed&&state.completed[l.id]);
   if(!lesson)lesson=list.find(l=>!(state.completed&&state.completed[l.id]))||null;
   if(!lesson)return;
   const dom=Arabic169.domainForLesson(lesson);
   const sec=document.createElement('section');sec.className='card track-continue404';
   const eb=document.createElement('span');eb.className='eyebrow';eb.textContent=courseTitle();
   const h=document.createElement('h2');h.textContent=arabicTitle171(lesson.title,dom);
   const b=document.createElement('button');b.type='button';b.className='btn full';b.dataset.action='start';b.dataset.id=lesson.id;
   b.textContent=Arabic169.primary(started?'كمّل درسك':'يلا نبدأ','ui')+' ←';
   sec.append(eb,h,b);
   const anchor=root.querySelector('details')||root.querySelector('.card');
   if(anchor)anchor.before(sec);else root.append(sec);
  }catch{}
 }
 document.addEventListener('click',e=>{
  const a=e.target.closest&&e.target.closest('[data-action="course"]');
  if(!a||!a.dataset.id||a.dataset.id==='main'||a.disabled)return;
  e.preventDefault();e.stopImmediatePropagation();
  chooseCourse(a.dataset.id);location.hash='path';render();window.scrollTo(0,0);
 },true);
 render=function(){guard();const r=baseRender.apply(this,arguments);trackCard();return r};
 guard();
 if(((location.hash.slice(1)||'home').split('/')[0])==='home')render();
})();
