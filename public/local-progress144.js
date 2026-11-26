/* Review-only: reconcile completed learning between tabs without replacing an active exercise. */
const localLearningFields144=['completed','words','events','formative','placement','activity','short143'];
let localLastRaw144=null,localLastData144=null,localRepairTimer144=0;
function localEqual144(a,b){if(a===b)return true;if(!a||!b||typeof a!=='object'||typeof b!=='object')return false;if(Array.isArray(a)!==Array.isArray(b))return false;const aa=Object.keys(a),bb=Object.keys(b);return aa.length===bb.length&&aa.every(k=>Object.hasOwn(b,k)&&localEqual144(a[k],b[k]))}
function localRead144(){try{return localStorage.getItem(STORE)}catch(error){return null}}
function localRemember144(raw){localLastRaw144=raw;try{localLastData144=raw?JSON.parse(raw):null}catch(error){localLastData144=null}}
localRemember144(localRead144());
function localReconcile144(raw){
 if(!raw||raw===localLastRaw144||state.account)return {changed:false,repair:false};
 let incoming,clean,merged;try{incoming=JSON.parse(raw);if(incoming.account)return {changed:false,repair:false};clean=validData(incoming);merged=mergeLearning(state,clean)}catch(error){return {changed:false,repair:false}}
 const changed=localLearningFields144.some(k=>!localEqual144(state[k],merged[k])),repair=localLearningFields144.some(k=>!localEqual144(clean[k],merged[k]));
 for(const key of localLearningFields144)state[key]=merged[key];
 const sessions={...incoming.sessions,...state.sessions};for(const [id,session] of Object.entries(incoming.sessions||{})){if(id!==activeCourseId&&localEqual144(state.sessions?.[id],localLastData144?.sessions?.[id]))sessions[id]=session}
 state.sessions=sessions;
 if(view.page!=='lesson'&&localEqual144(state.session,localLastData144?.sessions?.[activeCourseId]??localLastData144?.session??null))state.session=incoming.sessions?.[activeCourseId]??(incoming.activeCourseId===activeCourseId?incoming.session:null)??null;
 localRemember144(raw);return {changed,repair};
}
const localSave144=save;save=(sync=true)=>{localReconcile144(localRead144());localSave144(sync);localRemember144(localRead144())};
function localRefresh144(raw){const result=localReconcile144(raw);if(result.repair&&!localRepairTimer144)localRepairTimer144=setTimeout(()=>{localRepairTimer144=0;save(false)},0);if(result.changed&&['home','progress','review','courses'].includes(view.page))render()}
window.addEventListener('storage',event=>{if(event.key===STORE&&event.newValue)localRefresh144(event.newValue)});
window.addEventListener('focus',()=>localRefresh144(localRead144()));
document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')localRefresh144(localRead144())});
