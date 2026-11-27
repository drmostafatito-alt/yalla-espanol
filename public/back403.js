/* Back button support for overlays. App screens already use hash routes (each one is a history entry).
   Overlays (grammar section, sign-in invite) push one history entry per layer, so Back closes the top layer
   and only leaves the site from the home screen. */
(()=>{
  if(window.__back403)return;
  const stack=[];let dropping=false;
  function open(id,fn){stack.push({id,fn});try{history.pushState({b403:stack.length},'')}catch(e){}}
  function top(){return stack[stack.length-1]}
  function back(id){const t=top();if(t&&t.id===id)history.back()}
  function closeAll(prefix){let n=0;for(let i=stack.length-1;i>=0&&String(stack[i].id).startsWith(prefix);i--)n++;if(n)history.go(-n);return n}
  function drop(id){const t=top();if(t&&t.id===id){dropping=true;history.back()}}
  window.addEventListener('popstate',e=>{
    const d=(e.state&&e.state.b403)||0;
    while(stack.length>d){const it=stack.pop();if(dropping){dropping=false;continue}try{it.fn()}catch(x){}}
  });
  window.__back403={open,back,closeAll,drop,depth:()=>stack.length};
  // Landing straight on an inner screen (installed app, shared link): put the home screen underneath once.
  try{
    const h=location.hash;
    if(h&&h!=='#'&&h!=='#home'&&history.length<=2&&!history.state){
      const base=location.pathname+location.search;
      history.replaceState(null,'',base+'#home');history.pushState(null,'',base+h);
    }
  }catch(e){}
  // Sign-in invite dialog: Back dismisses it like the "continue as guest" button.
  let inv=null;
  new MutationObserver(()=>{
    const el=document.querySelector('.google-invite-card154');
    if(el&&!inv){inv=el;open('invite',()=>{const g=document.querySelector('.google-invite-guest154')||document.querySelector('.google-invite-close154');if(g)g.click()})}
    else if(!el&&inv){inv=null;drop('invite')}
  }).observe(document.body,{childList:true,subtree:true});
})();
