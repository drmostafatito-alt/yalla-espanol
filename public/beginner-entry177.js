/* Main A1 is the beginner route. Optional tracks keep their own saved progress. */
(()=>{
 const key='yalla-beginner-entry177';if(!localStorage.getItem(key)){localStorage.setItem(key,'done');const basicsStarted=MAIN_LESSONS.slice(0,6).some(l=>state.completed[l.id]);const explicit=new URL(location.href).searchParams.has('track');if(!basicsStarted&&activeCourseId==='everyday-core'&&!explicit){chooseCourse('main');history.replaceState(null,'',location.pathname+location.search+'#home')}}
 const oldHome=home;home=function(){const html=oldHome();if(activeCourseId==='main')return html;const t=document.createElement('template');t.innerHTML=html;const welcome=t.content.querySelector('.home122-welcome');if(welcome){const box=document.createElement('section');box.className='card';box.innerHTML='<h2>تبدأ الإسبانية من الصفر؟</h2><p>ابدأ بالتحية والتعارف في المسار الأساسي A1. هذا مسار إضافي مستقل.</p><button class="btn full" data-action="beginner-main177">ابدأ الأساسيات A1</button>';welcome.after(box)}return t.innerHTML};
 app.addEventListener('click',e=>{if(!e.target.closest('[data-action="beginner-main177"]'))return;chooseCourse('main');location.hash='home';render()},true);
})();
