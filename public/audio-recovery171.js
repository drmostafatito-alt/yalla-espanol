/* Recover a failed recorded clip once, without depending on installed speech voices. */
(()=>{
 let request=0,blobUrl=null;
 const unavailable=()=>toast('الصوت ما اشتغلش. جرّب تاني وأنت متصل بالإنترنت.');
 const stopped=()=>{document.documentElement.dataset.audioActive='false';document.querySelector('.listen-scene')?.classList.remove('playing');document.querySelectorAll('img[src$="#talk"]').forEach(i=>i.src=i.src.split('#')[0])};
 const active=()=>{document.documentElement.dataset.audioActive='true';document.querySelector('.listen-scene')?.classList.add('playing');document.querySelectorAll('.listen-fox,.stage .mascot,.dialogline img').forEach(i=>{if(/(fox|luna-flat|paco-flat)\.svg/.test(i.src))i.src=i.src.split('#')[0]+'#talk'})};
 function connect(player){player.onplay=active;player.onended=player.onpause=stopped;player.preservesPitch=true;player.playbackRate=state.settings.speed===.65?.8:state.settings.speed===1?1.1:1;return player}
 say=function(text,speaker=''){
  const token=++request;if(audioPlayer){audioPlayer.pause();audioPlayer=null}window.speechSynthesis?.cancel();if(blobUrl){URL.revokeObjectURL(blobUrl);blobUrl=null}
  if(hintUnavailable149(text,speaker)){toast(Arabic169.primary('النطق المسجّل للتعبير ده لسه مش متاح. النص ظاهر للتعلّم بالقراءة، مش تدريب استماع.','ui'));return}
  const resolved=hintResolveAudio(text,speaker),file=resolved.file;if(!file){sayFallback(text);return}
  hintStopOtherAudio();const player=audioPlayer=connect(new Audio(file));let retrying=false;
  async function recover(error){if(token!==request||retrying)return;if(error?.name==='AbortError')return;if(error?.name==='NotAllowedError'){window.dispatchEvent(new CustomEvent('yalla-audio-error179',{detail:{reason:'المتصفح منع تشغيل الصوت. اضغط تشغيل في المشغّل أدناه.'}}));return}retrying=true;stopped();try{const url=new URL(file,location.href);url.searchParams.set('audio-retry171',Date.now());const response=await fetch(url,{cache:'no-store'});if(!response.ok||!/^audio\//i.test(response.headers.get('Content-Type')||''))throw Error('Audio unavailable');const blob=await response.blob();if(blob.size<100)throw Error('Audio empty');if(token!==request)return;blobUrl=URL.createObjectURL(blob);const replacement=audioPlayer=connect(new Audio(blobUrl));await replacement.play();if(window.caches){const media=await caches.open('yalla-espanol-media-v1');await media.put(new URL(file,location.href).href,new Response(blob,{headers:{'Content-Type':blob.type||'audio/mpeg'}})).catch(()=>{})}replacement.onerror=()=>{if(token===request)unavailable()}}catch(e){if(token===request){stopped();unavailable()}}}
  player.onerror=()=>recover(player.error);player.play().catch(recover);
 };
 sayFallback=function(text){
  const token=request,synth=window.speechSynthesis;if(!synth){unavailable();return}let timer=null,done=false;
  const speak=()=>{if(done||token!==request)return;const voices=synth.getVoices(),voice=voices.find(v=>v.lang.toLowerCase()==='es-es')||voices.find(v=>/^es(?:-|$)/i.test(v.lang));if(!voice)return false;done=true;clearTimeout(timer);synth.removeEventListener?.('voiceschanged',speak);const utterance=new SpeechSynthesisUtterance(text);utterance.voice=voice;utterance.lang=voice.lang;utterance.rate=state.settings.speed;utterance.onstart=active;utterance.onend=stopped;utterance.onerror=e=>{stopped();if(e.error!=='canceled'&&e.error!=='interrupted')unavailable()};synth.speak(utterance);return true};
  if(speak())return;synth.addEventListener?.('voiceschanged',speak);timer=setTimeout(()=>{if(done)return;done=true;synth.removeEventListener?.('voiceschanged',speak);if(token===request)toast('مفيش صوت إسباني متاح على الجهاز. جرّب زر تعبير مسجّل، أو ثبّت صوت إسباني من إعدادات الجهاز.')},1500);
 };
})();
