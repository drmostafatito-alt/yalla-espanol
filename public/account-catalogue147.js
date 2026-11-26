/* Authenticated catalogue compatibility. This file grants no level or exam access. */
let accountMainSourceIds147=new Set(shortSourcesByCourse143.get('main').map(l=>l.id));
let accountProjectionRetry147={owner:null,key:null};
function accountRefreshIndexes147(){
 methodKnown141.clear();for(const word of ALL_WORDS){const key=normalize(word.es);if(!methodKnown141.has(key))methodKnown141.set(key,[]);methodKnown141.get(key).push(word.id)}
 hintCastIndex.clear();for(const [key,file] of Object.entries(AUDIO_CAST_MAP)){const colon=key.indexOf(':');if(colon<0)continue;const speaker=key.slice(0,colon),text=key.slice(colon+1),norm=speaker+':'+hintAudioKey(text);if(!hintCastIndex.has(norm))hintCastIndex.set(norm,{text,speaker,file})}
}
function accountRebuildCatalogue147(){
 const raw=[...new Map(MAIN_LESSONS.map(l=>{const source=l.origin143?shortSource143.get(l.origin143):l;if(!source)throw Error('Missing source for short catalogue');return[source.id,source]})).values()],ids=new Set(raw.map(l=>l.id));
 for(const id of accountMainSourceIds147){shortCache143.delete(id);if(ids.has(id))continue;shortSource143.delete(id);shortParts143.delete(id);delete ASSESSMENT_OVERRIDES[id];for(const part of [id+'-s1',id+'-s2']){shortIds143.delete(part);delete ASSESSMENT_OVERRIDES[part]}}
 raw.forEach((l,index)=>{l.index=index;shortSource143.set(l.id,l)});shortSourcesByCourse143.set('main',raw);MAIN_LESSONS.splice(0,MAIN_LESSONS.length,...raw);shortExpand143(MAIN_LESSONS);accountMainSourceIds147=ids;
 const words=[...new Map(raw.flatMap(l=>l.words).map(w=>[w.id,w])).values()];MAIN_WORDS.splice(0,MAIN_WORDS.length,...words);ALL_LESSONS.splice(0,ALL_LESSONS.length,...MAIN_LESSONS,...JOB_COURSES.flatMap(c=>c.lessons));ALL_WORDS.splice(0,ALL_WORDS.length,...new Map(ALL_LESSONS.flatMap(l=>l.words).map(w=>[w.id,w])).values());
 LESSON_ID_SET.clear();for(const l of ALL_LESSONS)LESSON_ID_SET.add(l.id);for(const id of shortSource143.keys())LESSON_ID_SET.add(id);WORD_ID_SET.clear();for(const word of ALL_WORDS)WORD_ID_SET.add(word.id);
 applyCourse(activeCourseId);accountRefreshIndexes147();shortProject143(state);
}
function accountSessionAllowed147(session){if(!session?.lessonId)return false;if(ALL_LESSONS.some(l=>l.id===session.lessonId)||shortSource143.has(session.lessonId))return true;const level=/^(a2|b1|b2|c1|c2)-/.exec(session.lessonId)?.[1]?.toUpperCase();return !!(level&&state.account?.id&&serverLevelAccess?.accountId===state.account.id&&serverLevelAccess.allowedLevels?.includes(level))}
const accountInstallLevel147=installLaterLevel;installLaterLevel=payload=>{accountInstallLevel147(payload);accountRebuildCatalogue147()};
const accountResetCurriculum147=resetLaterCurriculum;resetLaterCurriculum=()=>{
 const owner=state.account?.id||null,oldOwner=curriculumOwner,pending=state.session,ownerChanged=!!oldOwner&&oldOwner!==owner;
 const pendingSessions={...state.sessions};
 accountResetCurriculum147();accountRebuildCatalogue147();
 if(!ownerChanged&&accountSessionAllowed147(pending))state.session=pending;
 else if(ownerChanged){
  if(accountSessionAllowed147(pending)&&! /^(a2|b1|b2|c1|c2)-/.test(pending.lessonId))state.session=pending;
  view={};cardRun=null;storyRun=null;placementRun=null;hintHide();if(audioPlayer)audioPlayer.pause();if(location.hash.startsWith('#lesson/')&&/^(a2|b1|b2|c1|c2)-/.test(location.hash.slice(8)))history.replaceState(null,'','#home');
 }
 for(const [course,session] of Object.entries(pendingSessions||{}))if(session&&/^(a2|b1|b2|c1|c2)-/.test(session.lessonId||'')&&(ownerChanged||!accountSessionAllowed147(session)))delete state.sessions[course];
 if(accountProjectionRetry147.owner!==owner)accountProjectionRetry147={owner,key:null};
};
/* A fresh access check must not replace the current authorized input or question. */
refreshLevelAccess=async()=>{
 const owner=state.account?.id||null,session=state.session,question=view.q,page=view.page,review=view.review;
 await refreshLevelAccessOnly();await loadAuthorizedCurriculum();
 if((state.account?.id||null)===owner&&view.page===page){
  if(page==='lesson'&&state.session===session&&view.q===question&&question&&session&&lessonById(session.lessonId)&&isUnlocked(lessonById(session.lessonId)))return;
  if(page==='practice'&&view.review===review&&question&&view.q===question&&review?.words?.every(w=>WORD_ID_SET.has(w.id)))return;
 }
 render();
};
/* One retry per stable set of derived records, not a retry loop on rejected data. */
function accountScheduleProjection147(remote){
 const owner=state.account?.id||null;if(!owner||!remote)return false;
 const projected=globalThis.ACCOUNT_SHORT_PROJECTION.projectShortLearning(remote,shortAuthorizedSources147());if(!projected.changed)return false;
 const changes={};for(const field of ['completed','words']){changes[field]=Object.entries(projected.data[field]).filter(([id,record])=>JSON.stringify(record)!==JSON.stringify(remote[field]?.[id])).sort(([a],[b])=>a.localeCompare(b))}
 const key=JSON.stringify(changes);if(accountProjectionRetry147.owner===owner&&accountProjectionRetry147.key===key)return false;accountProjectionRetry147={owner,key};return true;
}
accountRefreshIndexes147();

function accountPrepareOwnerChange147(){serverLevelAccess=null;resetLaterCurriculum();view={};cardRun=null;storyRun=null;placementRun=null;hintHide();if(audioPlayer)audioPlayer.pause();if(location.hash.startsWith('#lesson/'))history.replaceState(null,'','#home')}
