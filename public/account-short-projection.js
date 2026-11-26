/* Generated from the local learning contract. Do not edit by hand. Source SHA256: 66a101f47d517171de8daae28647cca501801592feaf509a12a2929889de4dc7 */
(()=>{
"use strict";
const {sanitizeShortLedger,mergeCompletions,shortPart}=globalThis.LEARNING_PROGRESS_CONTRACT;
/* Pure local-learning projection. Callers supply only their currently authorized catalogue. */
function projectShortLearning(input,sources,{now=Date.now()}={}){
 const completed={...input.completed},words={...input.words},ledger=sanitizeShortLedger(input.short143,{now});
 for(const [id,r] of Object.entries(ledger))Object.assign(completed,mergeCompletions({[id]:completed[id]},{[id]:{at:r.at,score:r.score}}));
 const seen=new Set();
 for(const source of sources||[]){
  if(!source||typeof source.id!=='string'||seen.has(source.id)||!shortPart(source.id+'-s1')||shortPart(source.id))continue;
  seen.add(source.id);const ids=[source.id+'-s1',source.id+'-s2'],records=ids.map(id=>ledger[id]);
  if(records.every(Boolean)){
   const old=completed[source.id],score=Math.round(records.reduce((n,r)=>n+r.correct,0)/records.reduce((n,r)=>n+r.graded,0)*100),at=old?.at??Math.max(...records.map(r=>r.at));
   completed[source.id]={at,score:Math.max(old?.score||0,score)};
   for(const word of source.words||[]){const id=typeof word==='string'?word:word?.id;if(typeof id!=='string'||!id.startsWith(source.id+'w')||!/^\d+$/.test(id.slice(source.id.length+1))||Object.hasOwn(words,id))continue;words[id]={stage:0,at,due:at+86400000}}
  }
  const old=completed[source.id];if(old)for(const id of ids)if(!completed[id])completed[id]={at:old.at,score:old.score,inherited143:true};
 }
 const data={...input,completed,words,short143:ledger};
 return {data,changed:JSON.stringify(completed)!==JSON.stringify(input.completed||{})||JSON.stringify(words)!==JSON.stringify(input.words||{})};
}

globalThis.ACCOUNT_SHORT_PROJECTION=Object.freeze({projectShortLearning});
})();
