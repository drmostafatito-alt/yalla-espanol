(()=>{
 const st=document.getElementById('st'),say=t=>{st.textContent=t};
 const state=new URLSearchParams(location.search).get('state')||'';
 if(!/^[a-f0-9]{32}$/.test(state)){say('الرابط ده مش صالح. افتح الدخول من التطبيق.');return}
 const J={'Content-Type':'application/json','X-Yalla-Bounded-Sync':'1'};
 const post=async(p,b,h)=>{const r=await fetch(p,{method:'POST',credentials:'same-origin',headers:h||J,body:JSON.stringify(b)});let j={};try{j=await r.json()}catch{}if(!r.ok)throw Error(j.error||'failed');return j};
 function loadGsi(){return globalThis.google?.accounts?.id?Promise.resolve():new Promise((ok,no)=>{const s=document.createElement('script');s.src='https://accounts.google.com/gsi/client';s.async=true;s.onload=ok;s.onerror=()=>no(Error('google'));document.head.append(s)})}
 async function finish(){
  say('بنرجعك للتطبيق…');
  const m=await post('api/appauth-mint',{state},{'Content-Type':'application/json','X-Yalla-App-Handoff':'1'});
  const link='yallaespanol://auth?code='+m.code;const a=document.getElementById('back');a.href=link;a.style.display='inline-block';document.getElementById('google-btn').replaceChildren();say('تم الدخول. دوس على الزر لو التطبيق ما اتفتحش لوحده.');
  try{location.href=link}catch{}
 }
 (async()=>{try{
  const ch=await post('api/google/challenge',{},{'Content-Type':'application/json'});
  await loadGsi();
  google.accounts.id.initialize({client_id:ch.clientId,nonce:ch.nonce,auto_select:false,ux_mode:'popup',callback:async resp=>{
   say('بنتحقق من Google…');
   try{const r=await post('api/google/login',{id:ch.id,credential:resp.credential});if(!r.user)throw Error('incomplete');await finish()}catch(e){say('الدخول ما اكتملش. جرّب تاني.')}}});
  google.accounts.id.renderButton(document.getElementById('google-btn'),{theme:'outline',size:'large',text:'continue_with',locale:'ar',width:280});
  say('اختار حسابك من زر Google.');
 }catch(e){say('خدمة Google ما فتحتش. جرّب تاني وإنت متصل.')}})();
})();
