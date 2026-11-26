/* Measured phone screens. Keep complete choice groups together; page long reference material. */
const screenMemory140=new WeakMap();let screenFontRevision140=0;
function screenBounds140(ex){const r=ex.getBoundingClientRect(),nodes=[...ex.children].filter(n=>getComputedStyle(n).display!=='none');return Math.max(ex.scrollHeight-ex.clientHeight,r.top-Math.min(r.top,...nodes.map(n=>n.getBoundingClientRect().top)),Math.max(r.bottom,...nodes.map(n=>n.getBoundingClientRect().bottom))-r.bottom)}
function screenRestore140(ex){if(!ex._screenOriginal140)return;const fields=[...ex.querySelectorAll('input,textarea,select')],nodes=ex._screenOriginal140.map(node=>{const rootField=fields.find(f=>f.id&&f.id===node.id);if(rootField)return rootField;for(const f of fields)if(f.id)node.querySelector('#'+CSS.escape(f.id))?.replaceWith(f);return node});ex.replaceChildren(...nodes);delete ex._screenOriginal140;delete ex._screenShow140}
function screenRestoreFeedback146(ex,footer){const feedback=ex.querySelector('.screen-feedback146');if(feedback){feedback.classList.remove('screen-feedback146');footer.prepend(feedback)}}
function screenFeedbackPage146(ex,footer){const feedback=footer.querySelector('.feedback');if(!view.feedback||view.q?.type==='match'||!feedback)return;feedback.classList.add('screen-feedback146');ex.append(feedback)}
function screenFit140(){
 const h=window.visualViewport?.height||innerHeight;updateVisibleHeight307();const shell=app.querySelector('.exercise-layout');if(!shell)return;
 const ex=shell.querySelector('.exercise'),footer=shell.querySelector('.lesson-actions');if(!ex||!footer)return;
 if(innerWidth>=1000){screenRestore140(ex);screenRestoreFeedback146(ex,footer);delete ex._screenLayout140;shell.classList.remove('screen-lesson140');delete shell.dataset.screenFit;return}
 const focusedId=ex.contains(document.activeElement)?document.activeElement.id:'';
 const getSignature=()=>[screenFontRevision140,innerWidth,h,getComputedStyle(document.documentElement).fontSize,!!ex.querySelector('.pair-grid134'),ex.querySelectorAll('.review-option-expression').length,Math.round(footer.getBoundingClientRect().height*100)/100,[...ex.querySelectorAll('.statusline')].map(n=>n.textContent).join('|')].join(':');
 const signature=getSignature();if(ex._screenLayout140===signature)return;screenRestore140(ex);screenRestoreFeedback146(ex,footer);
 shell.classList.add('screen-lesson140');shell.dataset.question=view.q?.type||'';shell.dataset.screenEmptyPrefix=String(view.q?.type==='dialoggap'&&!view.q.prefix);shell.dataset.screenFit='true';delete shell.dataset.screenPages;delete shell.dataset.screenScroll;
 const pairIntro=ex.querySelector('.pair-grid134')?.previousElementSibling;if(pairIntro?.tagName==='P')pairIntro.textContent=Arabic169.primary("اضغط الإسباني عشان تسمعه.","ui");
 const shortHeading={dialoggap:Arabic169.primary("كمّل الحوار","ui"),dialogreply:Arabic169.primary("اختار الرد المناسب","ui"),dialog:Arabic169.primary("اختار الرد المناسب","ui")}[view.q?.type];if(shortHeading&&ex.querySelector('h1'))ex.querySelector('h1').textContent=shortHeading;
 for(const options of ex.querySelectorAll('.options'))options.classList.toggle('screen-short140',!!view.q?.options?.every(t=>t.length<=28&&t.trim().split(/\s+/).length<=4));
 let fit=false,overflow=0;for(let level=0;level<=3;level++){shell.dataset.screenCompact=level;overflow=screenBounds140(ex);fit=overflow<=2&&shell.getBoundingClientRect().bottom<=h+2;if(fit)break}
 if(!fit){screenFeedbackPage146(ex,footer);screenPaginate140(shell,ex);}
 else {shell.dataset.screenOverflow=0;shell.dataset.screenFit='true'}
 ex._screenLayout140=getSignature();if(focusedId){const field=ex.querySelector('#'+CSS.escape(focusedId)),page=field?.closest('.screen-step140');if(page)ex._screenShow140?.([...page.parentElement.children].indexOf(page));field?.focus({preventScroll:true})}
}
function screenPaginate140(shell,ex){
 const original=[...ex.children];ex._screenOriginal140=original.map(n=>n.cloneNode(true));const title=original.filter(n=>n.matches('.lesson-sub,h1')),content=original.filter(n=>!title.includes(n)&&getComputedStyle(n).display!=='none');
 const deck=document.createElement('div');deck.className='screen-deck140';const nav=document.createElement('nav');nav.className='screen-pager140';nav.setAttribute('aria-label',Arabic169.primary("أجزاء السؤال","ui"));
 ex.replaceChildren(...title,deck,nav);let pages=[],page,scroll=false;
 function fresh(){page=document.createElement('div');page.className='screen-step140';deck.append(page);pages.push(page)}
 function over(){const rects=[...page.children].filter(n=>getComputedStyle(n).display!=='none').map(n=>n.getBoundingClientRect());return rects.length&&Math.max(...rects.map(r=>r.bottom))-Math.min(...rects.map(r=>r.top))>deck.clientHeight-14}
 function makeScroll(el){el.classList.add('screen-internal140');page.classList.add('screen-has-internal140');scroll=true}
 function add(el,depth=0){
  page.append(el);if(over()&&page.children.length>1){el.remove();fresh();page.append(el)}
  if(!over())return;
  if(el.matches('.options,.screen-bank-group140,.method-input141,input,textarea,button')){makeScroll(el);return}
  if(el.matches('.pair-grid134')){const left=[...el.querySelectorAll('[data-side=left]')],right=[...el.querySelectorAll('[data-side=right]')];el.remove();let offset=0;while(offset<left.length){if(offset)fresh();let count=Math.min(3,left.length-offset),grid;while(count){grid=el.cloneNode(false);const batch=left.slice(offset,offset+count),ids=new Set(batch.map(n=>n.dataset.index)),r=right.filter(n=>ids.has(n.dataset.index));for(let k=0;k<count;k++)grid.append(batch[k],r[k]);page.append(grid);if(!over()||count===1)break;grid.remove();count--}if(over())makeScroll(grid);offset+=count}return}
  if(el.matches('.tiles')){el.remove();let group=el.cloneNode(false);page.append(group);for(const child of [...el.children]){group.append(child);if(over()&&group.children.length>1){child.remove();fresh();group=el.cloneNode(false);page.append(group);group.append(child)}}return}
  if(el.matches('p,.tip,.notice,.definition,.es,small')&&!el.querySelector('button,input,textarea,select,a')){
   const words=el.textContent.trim().split(/\s+/);if(words.length<2){makeScroll(el);return}el.remove();let fragment=el.cloneNode(false);if(fragment.dataset.reviewEs){fragment.classList.add('screen-text-part140');fragment.setAttribute('aria-label',Arabic169.primary("اسمع النص كامل","ui"))}
   page.append(fragment);for(const word of words){const previous=fragment.textContent;fragment.textContent+=(previous?' ':'')+word;if(over()&&previous){fragment.textContent=previous;fresh();fragment=fragment.cloneNode(false);fragment.textContent=word;page.append(fragment)}}return;
  }
  if(el.children.length>1&&depth<8&&!el.matches('.answerline')){el.remove();for(const child of [...el.children])add(child,depth+1);return}
  makeScroll(el)
 }
 const groups=[];for(let k=0;k<content.length;k++){const node=content[k];if(node.matches('.answerline')&&content[k+1]?.matches('.tiles')){const group=document.createElement('div');group.className='screen-bank-group140';group.append(node,content[++k]);groups.push(group)}else groups.push(node)}fresh();for(const node of groups)add(node);
 for(let i=pages.length-1;i>=0;i--)if(!pages[i].children.length){pages[i].remove();pages.splice(i,1)}
 const memory=view.q&&screenMemory140.get(view.q),feedbackMemory=ex._screenFeedbackPage146;let at=view.feedback?(feedbackMemory?.feedback===view.feedback?Math.min(feedbackMemory.at,pages.length-1):pages.length-1):Math.min(memory||0,pages.length-1);if(view.q?.type==='match'){const hit=pages.findIndex(p=>p.querySelector('.pair-hit134')),pending=pages.findIndex(p=>p.querySelector('.pair-spanish134:not(:disabled)'));if(hit>=0)at=hit;else if(pending>=0)at=pending}
 nav.innerHTML=Arabic169.primary("<button type=\"button\" class=\"screen-prev140\">السابق</button><span role=\"status\"></span><button type=\"button\" class=\"screen-next140\">التالي</button>","ui");
 const prev=nav.querySelector('.screen-prev140'),next=nav.querySelector('.screen-next140'),status=nav.querySelector('span');
 function show(n){at=Math.max(0,Math.min(pages.length-1,n));for(let k=0;k<pages.length;k++)pages[k].hidden=k!==at;prev.disabled=at===0;next.disabled=at===pages.length-1;if(view.q?.type==='match')status.textContent=view.matched.length+Arabic169.primary(" من ","ui")+ArabicCount169.selected(view.q.words.length,'pair',view.q.words.length+' أزواج');else{const fraction=document.createElement('bdi');fraction.dir='ltr';fraction.textContent=(at+1)+' / '+pages.length;status.replaceChildren(document.createTextNode(Arabic169.primary("جزء ","ui")),fraction)}if(view.q?.type==='match'){prev.hidden=true;next.hidden=true}if(view.q)screenMemory140.set(view.q,at);if(view.feedback)ex._screenFeedbackPage146={feedback:view.feedback,at};const check=shell.querySelector('[data-action="check"]');if(check&&!shell.classList.contains('pair-lesson134'))check.disabled=at<pages.length-1||(!view.feedback&&!isReady());shell.dataset.screenPage=at+1;}
 ex._screenShow140=show;prev.addEventListener('click',()=>show(at-1));next.addEventListener('click',()=>show(at+1));show(at);
 shell.dataset.screenFit='true';shell.dataset.screenPages=pages.length;shell.dataset.screenScroll=String(scroll);shell.dataset.screenOverflow=0;
}
let screenFrame140=0;function scheduleScreen140(){if(!screenFrame140)screenFrame140=requestAnimationFrame(()=>{screenFrame140=0;screenFit140()})}
fitScreen=scheduleScreen140;new MutationObserver(scheduleScreen140).observe(app,{childList:true,subtree:true});window.addEventListener('resize',scheduleScreen140);window.visualViewport?.addEventListener('resize',scheduleScreen140);document.fonts?.ready.then(()=>{screenFontRevision140++;scheduleScreen140()});document.fonts?.addEventListener('loadingdone',()=>{screenFontRevision140++;scheduleScreen140()});scheduleScreen140();
