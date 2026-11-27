/* Reads the question aloud once when it opens. Tapping the speaker replays it.
   Only runs inside a lesson, only once per question, never before the user has tapped the page,
   and can be turned off with state.settings.autoread=false. */
(()=>{
  let lastQ=null,timer=0;
  const pick=(app,q)=>{
    const t=q&&q.type;
    if(!['spell','bank','review','gap','dialoggap','dialog','dialogreply'].includes(t))return null;
    /* Only the audio of the text the question itself shows or plays. Never an option or the answer. */
    const want=t==='spell'?q.answer:q.source;
    if(!want)return null;
    for(const b of app.querySelectorAll('button[data-action="audio"],.listen-speech')){
      if(b.closest('.options,.option'))continue;
      if(b.dataset.text===want)return b;
    }
    return null;
  };
  function check(){
    timer=0;
    const app=document.getElementById('app');
    if(typeof view==='undefined'||typeof state==='undefined')return;
    if(!app||!app.querySelector('.lesson-shell')||!view.q){lastQ=null;return}
    const q=view.q;
    if(q===lastQ)return;
    lastQ=q;
    if(state.settings&&state.settings.autoread===false)return;
    if(document.hidden)return;
    if(navigator.userActivation&&!navigator.userActivation.hasBeenActive)return;
    if(view.feedback)return;
    const b=pick(app,q);
    if(b&&!b.disabled)b.click();
  }
  function schedule(){if(timer)clearTimeout(timer);timer=setTimeout(check,350)}
  function start(){
    const app=document.getElementById('app');
    if(!app)return setTimeout(start,300);
    new MutationObserver(schedule).observe(app,{childList:true,subtree:true});
    schedule();
  }
  start();
})();
