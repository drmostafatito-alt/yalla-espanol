/* Safari and iOS audio helper. Does nothing on other browsers.
   1) On the first tap, a silent clip is played so the page audio session is unlocked for later clips in a sequence.
   2) If play() fails for a reason other than the tap rule, the clip is fetched as a blob and played from an object URL. */
(()=>{
  const ua=navigator.userAgent||'';
  const ios=/iP(hone|ad|od)/.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
  const safari=/^((?!chrome|crios|fxios|android|edg).)*safari/i.test(ua);
  if(!(ios||safari)||window.__ios403)return;
  window.__ios403=1;
  const NativeAudio=window.Audio;
  const nativePlay=HTMLMediaElement.prototype.play;
  let started=false;
  function silentUrl(){
    const n=800,b=new ArrayBuffer(44+n*2),v=new DataView(b);
    const w=(o,s)=>{for(let i=0;i<s.length;i++)v.setUint8(o+i,s.charCodeAt(i))};
    w(0,'RIFF');v.setUint32(4,36+n*2,true);w(8,'WAVE');w(12,'fmt ');v.setUint32(16,16,true);v.setUint16(20,1,true);v.setUint16(22,1,true);
    v.setUint32(24,8000,true);v.setUint32(28,16000,true);v.setUint16(32,2,true);v.setUint16(34,16,true);w(36,'data');v.setUint32(40,n*2,true);
    return URL.createObjectURL(new Blob([b],{type:'audio/wav'}));
  }
  function unlock(){
    if(started)return;started=true;
    try{
      const src=silentUrl();
      for(let i=0;i<4;i++){
        const a=new NativeAudio();a.src=src;a.preload='auto';
        const p=nativePlay.call(a);
        if(p&&p.then)p.then(()=>{a.pause()}).catch(()=>{});
      }
    }catch(e){}
  }
  ['pointerdown','touchend','click','keydown'].forEach(t=>window.addEventListener(t,unlock,{once:false,passive:true,capture:true}));
  HTMLMediaElement.prototype.play=function(){
    const el=this;
    const r=nativePlay.apply(el,arguments);
    if(!r||typeof r.catch!=='function')return r;
    return r.catch(async err=>{
      if(!err||err.name==='NotAllowedError'||err.name==='AbortError')throw err;
      const src=el.currentSrc||el.src;
      if(!src||/^blob:/.test(src)||el.__blobTried)throw err;
      el.__blobTried=true;
      const resp=await fetch(src);
      if(!resp.ok)throw err;
      const blob=await resp.blob();
      el.src=URL.createObjectURL(new Blob([blob],{type:'audio/mpeg'}));
      return nativePlay.call(el);
    });
  };
})();
