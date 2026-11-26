/* Generated from the local learning contract. Do not edit by hand. Source SHA256: 3294cc3973db046f0ab91c5509f46be22f642810b29c5937757929dc27f5ab6c */
(()=>{
"use strict";
/* Local learning progress only. This module grants no exam or level awards. */
const LESSON_ID_SHAPE=/^(?:u\d+l\d+|(?:cc|tw|iv|a2|b1|b2|c1|c2|p0)-[a-z0-9][a-z0-9-]{0,44})(?:-s[12])?$/;
const SOURCE_ID_SHAPE=/^(?:u\d+l\d+|(?:cc|tw|iv|a2|b1|b2|c1|c2|p0)-[a-z0-9][a-z0-9-]{0,44})$/;
const WORD_ID_SHAPE=/^(?:u\d+l\d+w\d+|(?:cc|tw|iv|a2|b1|b2|c1|c2|p0)-[a-z0-9][a-z0-9-]{0,40}w\d+)$/;
const dayShape=/^\d{4}-\d{2}-\d{2}$/;
const safeKey=k=>!k.startsWith('__')&&k!=='constructor'&&k!=='prototype';
function shortPart(id){const m=/^(.*)-s([12])$/.exec(id);return m&&SOURCE_ID_SHAPE.test(m[1])?{source:m[1],part:Number(m[2])}:null}
function sourceLesson(id){return shortPart(id)?.source||id}
function normalizeLearningEvents(input){
 const out={};
 for(const [key,value] of Object.entries(input||{})){
  if(!safeKey(key)||!dayShape.test(value?.day||''))continue;
  const first=/^first:(.+)$/.exec(key),practice=/^practice:(.+):(\d{4}-\d{2}-\d{2})$/.exec(key);let canonical=key,xp=null;
  if(first&&LESSON_ID_SHAPE.test(first[1]))xp=shortPart(first[1])?10:20;
  else if(practice&&LESSON_ID_SHAPE.test(practice[1])&&practice[2]===value.day){canonical='practice:'+sourceLesson(practice[1])+':'+value.day;xp=5}
  else if(key==='review:'+value.day)xp=10;
  else if(/^story:[a-z0-9][a-z0-9-]{0,40}$/.test(key)||key==='cards:'+value.day||['lesson','story','cards'].some(id=>key==='quest:'+id+':'+value.day))xp=5;
  if(xp!==null){const prior=out[canonical];out[canonical]={day:prior&&prior.day<value.day?prior.day:value.day,xp}}
 }
 // An old client's whole-lesson award replaces, rather than adds to, part awards.
 for(const key of Object.keys(out)){const m=/^first:(.+)$/.exec(key),part=m&&shortPart(m[1]);if(part&&Object.hasOwn(out,'first:'+part.source))delete out[key]}
 return out;
}
function mergeLearningEvents(a,b){const out=normalizeLearningEvents(a);for(const [key,event] of Object.entries(normalizeLearningEvents(b))){const prior=out[key];out[key]=prior&&prior.day<event.day?prior:event}return normalizeLearningEvents(out)}
function sanitizeShortLedger(input,{now=Date.now(),limit=50000}={}){
 const out={};if(!input||typeof input!=='object'||Array.isArray(input))return out;
 if(Object.keys(input).length>limit)throw Error('Short-lesson progress is too large.');
 for(const [id,value] of Object.entries(input)){
  const part=shortPart(id);if(!part||!LESSON_ID_SHAPE.test(id)||!safeKey(id)||!Number.isFinite(value?.at)||!Number.isInteger(value.correct)||!Number.isInteger(value.graded)||value.graded<1||value.graded>30||value.correct<0||value.correct>value.graded)continue;
  const wordResults={};for(const [word,result] of Object.entries(value.wordResults||{}))if(WORD_ID_SHAPE.test(word)&&safeKey(word)&&word.startsWith(part.source+'w')&&/^\d+$/.test(word.slice(part.source.length+1))&&typeof result==='boolean')wordResults[word]=result;
  out[id]={at:Math.min(value.at,now+300000),correct:value.correct,graded:value.graded,score:Math.round(value.correct/value.graded*100),wordResults};
 }
 return out;
}
function mergeShortLedger(a,b){const out={...a};for(const [id,record] of Object.entries(b||{})){const prior=out[id];if(!prior||record.score>prior.score||record.score===prior.score&&record.at>prior.at)out[id]=record}return out}
function mergeCompletions(a,b){const out={...a};for(const [id,record] of Object.entries(b||{})){const prior=out[id];out[id]=!prior?record:{at:Math.max(prior.at,record.at),score:Math.max(prior.score,record.score),...(prior.inherited143&&record.inherited143?{inherited143:true}:{})}}return out}

globalThis.LEARNING_PROGRESS_CONTRACT=Object.freeze({LESSON_ID_SHAPE,shortPart,sourceLesson,normalizeLearningEvents,mergeLearningEvents,sanitizeShortLedger,mergeShortLedger,mergeCompletions});
})();
