/* Isolated matching mechanic prototype. No live deployment or scoring model changes. */
const pairContexts134=new WeakMap();
function pairMeaning134(w){const source=activeCourseId==='main'&&lessonById('u1l3')?.words.some(x=>x.id===w.id);if(source&&normalize(w.es)==='buenas tardes')return Arabic169.primary("مساء الخير (بعد الضهر)","ui");if(source&&normalize(w.es)==='buenas noches')return Arabic169.primary("مساء الخير (بالليل)","ui");return w.ar}
function pairPrepare134(q,forUnit=false){
 if(pairContexts134.has(q))return pairContexts134.get(q);
 const seenEs=new Set(),seenAr=new Set(),words=[];
 const add=w=>{if(!w?.es||!w?.ar)return;const es=normalize(w.es),ar=pairMeaning134(w).trim();if(seenEs.has(es)||seenAr.has(ar))return;seenEs.add(es);seenAr.add(ar);words.push(w)};
 const original=q.words.slice();original.forEach(add);
 // Ambiguous authored labels stay on the existing renderer, pending a content decision.
 if(words.length!==original.length){const blocked={blocked:true};pairContexts134.set(q,blocked);return blocked}
 if(words.length<5){
  const priorIds=new Set(LESSONS.filter(l=>state.completed[l.id]).flatMap(l=>l.words.map(w=>w.id)));
  const completedWords=new Map(LESSONS.filter(l=>state.completed[l.id]).flatMap(l=>l.words.map(w=>[w.id,state.completed[l.id]?.at||0])));
  const eligible=!forUnit&&view.page==='practice'?(view.review?.words||[]):WORDS.filter(w=>state.words[w.id]||priorIds.has(w.id)).sort((a,b)=>(state.words[b.id]?.at||completedWords.get(b.id)||0)-(state.words[a.id]?.at||completedWords.get(a.id)||0)||WORDS.indexOf(b)-WORDS.indexOf(a));
  for(const w of eligible){if(words.length>=5)break;add(w)}
 }
 q.words=words;
 const context={blocked:false,page:view.page,flow:view.page==='practice'?view.review:state.session,batchStart:0,hit:new Set(),fault:[],busy:false,finalizing:false};
 pairContexts134.set(q,context);pairOrder134(q,context);return context;
}
function pairOrder134(q,c){const indices=q.words.map((_,i)=>i).slice(c.batchStart,c.batchStart+5);c.left=shuffled(indices);c.right=shuffled(indices);if(indices.length>1&&c.left.every((x,i)=>c.right[i]===x))c.right.push(c.right.shift())}
function pairActive134(q,c){return view.q===q&&view.page===c.page&&(view.page==='practice'?view.review:state.session)===c.flow}
function pairTile134(q,c,index,side){const w=q.words[index],done=view.matched.includes(index),hit=c.hit.has(index),wrong=c.fault.includes(side+':'+index),selected=(side==='left'?view.matchLeft:view.matchRight)===index,es=side==='left';return `<button type="button" class="pair-tile134 ${es?'pair-spanish134':''} ${hit?'pair-hit134':done?'pair-done134':''} ${wrong?'pair-wrong134':''} ${selected&&!wrong?'pair-selected134':''}" data-action="pair-select134" data-side="${side}" data-index="${index}" ${done?'disabled':''} ${es?'lang="es" dir="ltr"':'lang="ar" dir="rtl"'} aria-pressed="${selected&&!done}" aria-label="${esc(es?w.es:pairMeaning134(w))}">${es?esc(w.es):arabicLearning169(pairMeaning134(w))}</button>`}
function pairHydrate134(){const q=view.q;if(!q||q.type!=='match')return;const c=pairPrepare134(q);if(c.blocked)return;const old=app.querySelector('.match-grid');if(!old)return;const grid=document.createElement('div');grid.className='pair-grid134';grid.setAttribute('role','group');grid.setAttribute('aria-label',Arabic169.primary("توصيل الكلمات بمعانيها","ui"));grid.innerHTML=c.left.map((n,row)=>pairTile134(q,c,n,'left')+pairTile134(q,c,c.right[row],'right')).join('');old.replaceWith(grid);grid.closest('.lesson-shell')?.classList.add('pair-lesson134');const p=grid.previousElementSibling;if(p?.tagName==='P')p.textContent=Arabic169.primary("اختار كلمة ومعناها. اضغط على الإسباني عشان تسمعه.","ui");const status=document.createElement('p');status.className='pair-status134';status.setAttribute('role','status');status.setAttribute('aria-live','polite');status.textContent=Arabic169.template("f938f59f47ab5f5e")`${ArabicCount169.format(view.matched.length)} من ${ArabicCount169.selected(q.words.length,"pair",q.words.length)} أزواج`;grid.after(status);const checkButton=app.querySelector('.lesson-actions [data-action="check"]');if(checkButton){checkButton.disabled=true;checkButton.setAttribute('aria-disabled','true');checkButton.textContent=Arabic169.primary("بتكمل لوحدها بعد آخر زوج","ui")}
}
const pairBaseRenderExercise134=renderExercise;renderExercise=()=>{pairBaseRenderExercise134();pairHydrate134()};
function pairRepaint134(){renderExercise()}
function pairAdvance134(q,c){
 if(c.finalizing)return;c.finalizing=true;
 setTimeout(()=>{if(!pairActive134(q,c))return;
  if(view.matched.length<q.words.length){c.batchStart+=5;c.hit.clear();c.finalizing=false;pairOrder134(q,c);pairRepaint134();return}
  // Use the existing check/round ledger exactly once. Do not replay the final success cue.
  const previous=playFeedback;playFeedback=()=>{};
  try{check()}finally{playFeedback=previous}
  if(pairActive134(q,c)&&view.feedback?.ok)nextQuestion();
 },570);
}
document.addEventListener('click',event=>{
 const tile=event.target.closest('[data-action="pair-select134"]');if(!tile)return;
 event.preventDefault();event.stopImmediatePropagation();
 const q=view.q,c=q&&pairContexts134.get(q);if(!q||!c||c.blocked||tile.disabled||c.busy||c.finalizing||view.feedback)return;
 const index=Number(tile.dataset.index),side=tile.dataset.side;if(view.matched.includes(index))return;
 if(side==='left')say(q.words[index].es,q.words[index].speaker);
 const field=side==='left'?'matchLeft':'matchRight';view[field]=view[field]===index?null:index;
 if(view.matchLeft===null||view.matchRight===null){pairRepaint134();return}
 const left=view.matchLeft,right=view.matchRight;view.matchLeft=null;view.matchRight=null;
 if(left===right){view.matched.push(left);c.hit.add(left);playFeedback(true);pairRepaint134();setTimeout(()=>{if(!pairActive134(q,c))return;c.hit.delete(left);pairRepaint134()},235);if(c.left.every(i=>view.matched.includes(i)))pairAdvance134(q,c)}
 else {view.hadError=true;c.busy=true;c.fault=['left:'+left,'right:'+right];playFeedback(false);pairRepaint134();setTimeout(()=>{if(!pairActive134(q,c))return;c.fault=[];c.busy=false;pairRepaint134()},390)}
},true);
const pairUnitAudioFiles134=unitAudioFiles;unitAudioFiles=ui=>{const files=pairUnitAudioFiles134(ui);for(const lesson of LESSONS.filter(l=>l.unit===ui))for(const q of exercises(lesson).filter(q=>q.type==='match')){const c=pairPrepare134(q,true);if(c.blocked)continue;for(const word of q.words){const file=hintResolveAudio(word.es,word.speaker).file;if(file)files.push(file)}}return [...new Set(files)]};
pairHydrate134();