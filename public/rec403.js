/* Learner voice recording. Local only: the recording never leaves the device and is not saved.
   Adds a record button next to the lesson sound button. Tap to start, tap to stop (auto stop after 10 s),
   then the model clip plays followed by the learner's recording. Hidden when the browser cannot record. */
(()=>{
  if(window.__rec403)return;window.__rec403=1;
  if(!navigator.mediaDevices||!navigator.mediaDevices.getUserMedia||typeof MediaRecorder==='undefined')return;
  const app=document.getElementById('app');if(!app)return;
  let rec=null,chunks=[],stream=null,timer=null,url=null,mode='rec',msg='',clipKey='',busy=false;
  const T={rec:'🎙 سجّل صوتك',stop:'⏹ وقّف التسجيل',play:'▶ اسمع نفسك',again:'🔁 سجّل تاني',denied:'محتاج تسمح بالميكروفون عشان التسجيل.',fail:'التسجيل مش شغال على الجهاز ده.'};
  function mime(){for(const m of ['audio/webm;codecs=opus','audio/mp4','audio/webm','audio/ogg;codecs=opus']){try{if(MediaRecorder.isTypeSupported(m))return m}catch(e){}}return ''}
  function cleanup(){clearTimeout(timer);if(stream){stream.getTracks().forEach(t=>t.stop());stream=null}}
  function paint(){
    const b=app.querySelector('.rec403');if(!b)return;
    b.textContent=T[mode];b.dataset.state=mode;
    let r=app.querySelector('.rec403b');
    if(mode==='play'&&!r){r=document.createElement('button');r.type='button';r.className='plain rec403b';r.textContent=T.again;r.addEventListener('click',e=>{e.stopPropagation();mode='rec';msg='';start()});b.insertAdjacentElement('afterend',r)}
    if(mode!=='play'&&r)r.remove();
    let n=app.querySelector('.rec403-note');
    if(msg){if(!n){n=document.createElement('span');n.className='rec403-note small';n.setAttribute('role','status');b.parentNode.appendChild(n)}n.textContent=msg}else if(n)n.remove();
  }
  function playBoth(){
    const model=app.querySelector('button[data-action=audio]');
    const go=()=>{new Audio(url).play().catch(()=>{msg=T.fail;paint()})};
    if(model){try{model.click()}catch(e){}setTimeout(go,1800)}else go();
  }
  async function start(){
    if(busy)return;busy=true;
    try{stream=await navigator.mediaDevices.getUserMedia({audio:true})}catch(e){busy=false;msg=T.denied;mode='rec';paint();return}
    try{
      const m=mime();rec=m?new MediaRecorder(stream,{mimeType:m}):new MediaRecorder(stream);chunks=[];
      rec.ondataavailable=e=>{if(e.data&&e.data.size)chunks.push(e.data)};
      rec.onstop=()=>{busy=false;cleanup();if(url)URL.revokeObjectURL(url);url=chunks.length?URL.createObjectURL(new Blob(chunks,{type:rec.mimeType||m||'audio/mp4'})):null;mode=url?'play':'rec';if(!url)msg=T.fail;paint()};
      rec.start();mode='stop';msg='';paint();
      timer=setTimeout(()=>{if(rec&&rec.state==='recording')rec.stop()},10000);
    }catch(e){busy=false;cleanup();msg=T.fail;mode='rec';paint()}
  }
  function onClick(e){
    e.stopPropagation();
    if(mode==='stop'){if(rec&&rec.state==='recording')rec.stop();return}
    if(mode==='play'){playBoth();return}
    start();
  }
  function inject(){
    const a=app.querySelector('button[data-action=audio]');
    if(!a)return;
    if(!/تعبير جديد|تعرّف على كلمة/.test(app.innerText||''))return;
    const key=a.dataset.text||'';
    if(key!==clipKey&&mode!=='stop'){clipKey=key;mode='rec';msg='';if(url){URL.revokeObjectURL(url);url=null}}
    if(!app.querySelector('.rec403')){
      const b=document.createElement('button');b.type='button';b.className='plain rec403';b.addEventListener('click',onClick);
      a.insertAdjacentElement('afterend',b);
    }
    paint();
  }
  let pend=false;
  new MutationObserver(()=>{if(pend)return;pend=true;setTimeout(()=>{pend=false;inject()},50)}).observe(app,{childList:true,subtree:true});
  inject();
})();
