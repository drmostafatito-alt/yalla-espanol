/* Pronounce the Spanish option or word tile without delaying selection. */
(()=>{
 const actions=new Set(['choose','pick','unpick','match','exam-choice','exam-token','formative-choice','formative-token','mock-answer','writing-model']);
 globalThis.CHOICE_AUDIO182={taps:0,missing:[]};
 document.addEventListener('click',event=>{
  const button=event.target.closest('[data-action]');if(!button||!app.contains(button)||button.disabled||!actions.has(button.dataset.action))return;
  if(button.dataset.action==='match')return; // The paired exercise already speaks its Spanish side once.
  if(view.feedback&&['choose','pick','unpick'].includes(button.dataset.action))return;
  const text=String(button.dataset.reviewEs||button.getAttribute('aria-label')||button.closest('.option')?.querySelector('[data-review-es]')?.dataset.reviewEs||button.textContent||'').trim();
  if(!text||/[\u0600-\u06ff]/.test(text)||!/[a-záéíóúüñ0-9]/i.test(text))return;
  event.choiceAudio182=true;let spoken=text,speaker=hintSpeaker(text,button);
  if(view.q?.type==='spell'&&['pick','unpick'].includes(button.dataset.action)){
   const letter=text.toLocaleLowerCase('es').normalize('NFD').replace(/[\u0300-\u036f]/g,'');const item=ALPHABET_AUDIO.find(a=>a.letter===letter);if(item){spoken=item.text;speaker=item.speaker}
  }
  const resolved=hintResolveAudio(spoken,speaker);CHOICE_AUDIO182.taps++;CHOICE_AUDIO182.last={text,spoken,file:resolved.file};
  if(!resolved.file&&!CHOICE_AUDIO182.missing.includes(spoken))CHOICE_AUDIO182.missing.push(spoken);
  say(spoken,speaker);
 },true);
})();
