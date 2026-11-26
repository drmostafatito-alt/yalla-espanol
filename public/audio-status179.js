/* A tap reports whether media started, was blocked, or failed. Device volume is not observable. */
(()=>{
 let sequence=0,cleanPrevious=()=>{};const prior=say;globalThis.AUDIO_STATUS179={};
 function status(text,bad=false,file=''){let node=document.querySelector('.audio-status179');if(!node){node=document.createElement('div');node.className='audio-status179';node.role='status';(document.querySelector('.lesson-actions')||document.querySelector('#app')).append(node)}node.classList.toggle('bad',bad);node.textContent=text;if(file&&bad){const native=document.createElement('audio');native.controls=true;native.src=file;native.preload='metadata';node.append(native)}return node}
 say=function(text,speaker=''){
  cleanPrevious();const token=++sequence,resolved=hintResolveAudio(text,speaker);globalThis.AUDIO_STATUS179={text,file:resolved.file,state:'requested'};
  if(!resolved.file){status('لا يوجد تسجيل لهذا التعبير. استخدم بديل القراءة.',true);return}
  prior(text,speaker);let elapsed=0,played=false;
  const fail=event=>{if(token!==sequence)return;clearInterval(timer);cleanPrevious();globalThis.AUDIO_STATUS179.state='blocked';status(event.detail.reason,true,resolved.file);window.removeEventListener('yalla-audio-error179',fail)};window.addEventListener('yalla-audio-error179',fail,{once:true});cleanPrevious=()=>window.removeEventListener('yalla-audio-error179',fail);const timer=setInterval(()=>{if(token!==sequence){clearInterval(timer);cleanPrevious();return}elapsed+=100;const player=audioPlayer;if(player?.currentTime>.015&&!played){played=true;globalThis.AUDIO_STATUS179.state='playing';document.querySelector('.audio-status179')?.remove();clearInterval(timer);cleanPrevious();return}if(player?.error){const reason={1:'أُلغي التشغيل',2:'تعذّر تحميل الصوت من الشبكة',3:'تعذّر فك ترميز التسجيل',4:'صيغة التسجيل غير مدعومة'}[player.error.code]||'تعذّر التشغيل';globalThis.AUDIO_STATUS179={...globalThis.AUDIO_STATUS179,state:'error',reason};status(reason+'، جرّب المشغّل المباشر أدناه.',true,resolved.file);clearInterval(timer);cleanPrevious();return}if(elapsed>=4500){globalThis.AUDIO_STATUS179.state='not-started';status('المتصفح لم يبدأ التشغيل. اضغط تشغيل في المشغّل المباشر أدناه.',true,resolved.file);clearInterval(timer)}},100);
 };
 // The top speaker controls encouragement only, not Spanish recordings.
 const previous=reviewMuteButton;reviewMuteButton=function(){return previous().replace('title="أصوات التشجيع"','title="أصوات التشجيع فقط، النطق له زر منفصل"')};
})();
