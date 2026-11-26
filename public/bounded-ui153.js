/* Local candidate153 feature flag;not enabled on the hosted site. */
const oldApi153=api;
 api=async(path,data)=>{if(!['me','login'].includes(path))return oldApi153(path,data);const r=await fetch('api/'+path,{method:data?'POST':'GET',credentials:'same-origin',headers:{'X-Yalla-Bounded-Sync':'1',...(data?{'Content-Type':'application/json'}:{})},...(data?{body:JSON.stringify(data)}:{})});const body=await r.json();if(!r.ok){const e=Error(body.error||Arabic169.primary("الاتصال ما اكتملش","ui"));e.status=r.status;throw e}return body};
if(globalThis.YALLA_BOUNDED153&&navigator.locks){
 let boundedClient153=null;
 function client153(owner){if(boundedClient153?.owner===owner&&!boundedClient153.closed)return boundedClient153;boundedClient153?.close();const x=YALLA_BOUNDED153;boundedClient153=new x.BoundedBrowserSync({owner,store:localStorage,empty:x.fresh,merge:x.merge,Outbox:x.DeltaOutbox,isActive:id=>state.account?.id===id,lock:(name,fn)=>navigator.locks.request(name,fn),transport:async(type,body)=>{const post=type==='push',qs=post?'':'?'+new URLSearchParams(Object.entries(body).filter(([k,v])=>v!==null&&v!==undefined));const r=await fetch('api/delta148/'+type+qs,{method:post?'POST':'GET',credentials:'same-origin',headers:{'X-Yalla-Owner':owner,...(post?{'Content-Type':'application/json'}:{})},...(post?{body:JSON.stringify(body)}:{})});const data=await r.json();if(!r.ok){const e=Error(data.error||Arabic169.primary("المزامنة ما اكتملتش","ui"));e.status=r.status;e.revision=data.revision;e.migrationRequired=data.migrationRequired;throw e}return data}});return boundedClient153}
 const oldOwnerChange153=accountPrepareOwnerChange147;accountPrepareOwnerChange147=()=>{boundedClient153?.close();boundedClient153=null;return oldOwnerChange153()};
 syncAccount=async()=>{if(!state.account)return;if(!navigator.onLine){syncMessage=Arabic169.primary("مفيش نت. تقدمك محفوظ على الجهاز.","ui");return}if(syncBusy){syncAgain=true;return}syncBusy=true;const owner=state.account.id;try{const r=await client153(owner).sync(validData(state));if(state.account?.id!==owner)return;const merged=mergeLearning(state,r.state);for(const f of['completed','words','events','placement','activity','formative','short143'])state[f]=merged[f];if(accountScheduleProjection147(r.state))syncAgain=true;save(false);syncMessage=Arabic169.primary("آخر مزامنة: ","ui")+new Date().toLocaleTimeString('ar-EG');if(['settings','home','path','progress','review','courses'].includes(view.page))render()}catch(e){syncMessage=e.migrationRequired?Arabic169.primary("الحساب محتاج نقل آمن للتقدم. تقدم الجهاز محفوظ.","ui"):e.message;if(e.status===401)needsReauth=true;if(view.page==='settings')authStatus(syncMessage)}finally{syncBusy=false;if(syncAgain){syncAgain=false;syncAccount()}}};
}

if(globalThis.YALLA_BOUNDED153&&!navigator.locks){syncAccount=async()=>{syncMessage=Arabic169.primary("المتصفح ده محتاج تحديث عشان المزامنة الآمنة. تقدمك محفوظ على الجهاز.","ui");if(view.page==='settings')authStatus(syncMessage)};}
/* Automatic catch-up while an already-open device is idle. No background polling. */
(()=>{
 const baseSync157=syncAccount;let lastStart157=0;
 async function catchUp157(){if(document.hidden||!navigator.onLine||!state.account||needsReauth||Date.now()-lastStart157<15000)return;lastStart157=Date.now();await baseSync157()}
 window.addEventListener('focus',catchUp157);
 setInterval(catchUp157,300000);
})();
