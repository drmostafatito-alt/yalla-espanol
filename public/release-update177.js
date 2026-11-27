/* Keep an open app on the current release without clearing learning or media. */
(()=>{
 const release='402';globalThis.YALLA_RELEASE=release;let checking=false,reloading=false,registration;
 let pending=false;const reload=()=>{if(reloading)return;if(['lesson','practice','placement','formative'].includes(view.page)){pending=true;return;}reloading=true;try{save(false)}catch{}location.reload()};
 navigator.serviceWorker?.addEventListener('message',event=>{if(event.data?.type!=='yalla-release-ready')return;event.ports?.[0]?.postMessage({ready:true});if(event.data.release!==release)reload()});
 navigator.serviceWorker?.addEventListener('controllerchange',()=>{if(registration?.active)registration.active.postMessage({type:'yalla-release-query'})});
 async function check(){if(checking||!navigator.onLine||document.visibilityState==='hidden')return;checking=true;try{registration=await navigator.serviceWorker?.getRegistration();if(registration)await registration.update();const response=await fetch('release.json?check='+Date.now(),{cache:'no-store'});if(response.ok){const latest=await response.json();if(latest.release&&latest.release!==release)reload()}}catch{}finally{checking=false}}
 window.addEventListener('hashchange',()=>{if(pending&&!['lesson','practice','placement','formative'].includes(view.page))reload()});window.addEventListener('focus',check);window.addEventListener('online',check);document.addEventListener('visibilitychange',()=>{if(!document.hidden)check()});setInterval(check,300000);setTimeout(check,1000);
})();
