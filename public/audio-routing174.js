/* Resolve recorded text even when an older exercise supplies a different speaker. */
(()=>{
 const key=text=>hintAudioKey(String(text||'').normalize('NFKC').replace(/[\u200B-\u200F\u202A-\u202E\u2066-\u2069\uFEFF]/g,'').replace(/[“”«»]/g,'').replace(/[’‘]/g,"'"));
 const bySpeaker=new Map(),byText=new Map();let size=-1;
 function rebuild(){bySpeaker.clear();byText.clear();for(const [cast,file]of Object.entries(AUDIO_CAST_MAP)){const colon=cast.indexOf(':');if(colon<0)continue;const speaker=cast.slice(0,colon),text=cast.slice(colon+1),item={text,speaker,file},k=key(text);if(!bySpeaker.has(speaker+':'+k))bySpeaker.set(speaker+':'+k,item);if(!byText.has(k))byText.set(k,item)}for(const [text,file]of Object.entries(AUDIO_MAP)){const k=key(text);if(!byText.has(k))byText.set(k,{text,speaker:'',file})}size=Object.keys(AUDIO_CAST_MAP).length+Object.keys(AUDIO_MAP).length}
 const original=hintResolveAudio;hintResolveAudio=function(text,speaker=''){const direct=original(text,speaker);if(direct.file)return direct;if(size!==Object.keys(AUDIO_CAST_MAP).length+Object.keys(AUDIO_MAP).length)rebuild();return bySpeaker.get((speaker||'')+':'+key(text))||byText.get(key(text))||direct};
 rebuild();const fallback=sayFallback;sayFallback=function(text){const r=hintResolveAudio(text,'');if(r.file)return say(r.text,r.speaker);return fallback(text)};
 globalThis.AUDIO_ROUTING174={rebuild};
})();
