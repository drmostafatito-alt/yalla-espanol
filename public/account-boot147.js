/* Final account boot, after catalogue, teaching and progress wrappers are installed. */
window.__reviewBootPending=false;
shortProject143(state);
save(false);
render();
if('serviceWorker'in navigator&&location.protocol!=='file:')navigator.serviceWorker.register('sw.js',{updateViaCache:'none'}).catch(()=>{});
if('speechSynthesis'in window)speechSynthesis.getVoices();
window.__accountReady147=false;
window.__accountInit147=Promise.resolve(initAccount()).finally(()=>{window.__accountReady147=true});
