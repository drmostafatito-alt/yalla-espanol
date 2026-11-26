let visibleHeight307=window.__visibleHeight307||'';function updateVisibleHeight307(force=false){if(visibleHeight307&&!force)return;const h=(window.visualViewport?.height||innerHeight)+'px';if(h!==visibleHeight307){visibleHeight307=h;document.documentElement.style.setProperty('--visible-height',h)}}
/* Reflow content into explicitly numbered screens. Never hide overflowing lesson text. */
let fitBusy=false;
function fitScreen(){
 updateVisibleHeight307();
 if(fitBusy)return;const shell=document.querySelector('.exercise-layout');if(!shell)return;fitBusy=true;
 try{
 const ex=shell.querySelector('.exercise');if(!ex)return;const focusedId=ex.contains(document.activeElement)?document.activeElement.id:'';
 const old=ex.querySelector('.fit-deck');if(old){const fields=[...ex.querySelectorAll('input,textarea,select')];ex.innerHTML=old._originalHTML||'';for(const field of fields)if(field.id&&ex.querySelector('#'+CSS.escape(field.id)))ex.querySelector('#'+CSS.escape(field.id)).replaceWith(field)}
 delete shell.dataset.fitPages;delete shell.dataset.fitPage;return;
 if(innerWidth>=1000){delete shell.dataset.fitPages;delete shell.dataset.fitPage;return}
 const kids=[...ex.children];if(!kids.length)return;const snapshot=ex.innerHTML;
 const key=[state.session?.lessonId||'review',state.session?.at??view.review?.at,view.q?.type,view.typed?'typed':'voice',view.revealed?'read':'hear'].join(':');
 const changed=view.fitKey!==key;if(changed){view.fitKey=key;view.fitPage=0}
 shell.dataset.question=view.q?.type||'';
 // Pair each matching tile with its own sound button in one touch-friendly row.
 ex.querySelectorAll('.match-col').forEach(col=>{if(col.querySelector('.match-item'))return;[...col.children].forEach(el=>{if(!el.matches('.tile'))return;const next=el.nextElementSibling;if(next?.matches('.audio')){const row=document.createElement('div');row.className='match-item';el.before(row);row.append(el,next)}})});
 const title=document.createElement('div');title.className='fit-title';
 if(kids[0]?.classList.contains('lesson-sub'))title.append(kids.shift());
 const hi=kids.findIndex(el=>el.tagName==='H1');if(hi>=0){if(innerHeight<421&&innerWidth<450){const heading=kids.splice(hi,1)[0];kids.unshift(heading)}else title.append(kids.splice(hi,1)[0])}
 const feedback=shell.querySelector('.lesson-actions .feedback')||ex.querySelector('.feedback');if(feedback&&!kids.includes(feedback))kids.push(feedback);
 const original=[...title.children,...kids.filter(el=>el!==feedback)];
 const deck=document.createElement('div');deck.className='fit-deck';deck._originalHTML=snapshot+(feedback&&!ex.contains(feedback)?feedback.outerHTML:'');
 const controls=document.createElement('nav');controls.className='fit-pages';controls.setAttribute('aria-label',Arabic169.primary("أجزاء الشاشة","ui"));controls.textContent=' '; 
 ex.replaceChildren(title,deck,controls);
 const pages=[];let page;
 function newPage(){page=document.createElement('div');page.className='fit-page';deck.append(page);pages.push(page);return page}
 function over(){return page.scrollHeight>deck.clientHeight+1}
 function add(el){
  if(el.classList.contains('exercise-coach')){el.classList.add('fit-decoration')}
  page.append(el);
  if(over()&&page.children.length>1){el.remove();newPage();page.append(el)}
  if(over()&&el.matches('.stage,.dialogline')){el.remove();const bubble=el.querySelector('.bubble');if(bubble){for(const child of [...bubble.children]){if(child.matches('span.es,div.es,small')){const block=document.createElement('p');block.className=child.className;block.lang=child.lang;block.dir=child.dir;block.innerHTML=child.innerHTML;add(block)}else add(child)}return}page.append(el)}
  if(over()&&el.matches('.feedback')){
   el.remove();const nodes=[...el.childNodes];let group=el.cloneNode(false);page.append(group);
   for(const node of nodes){group.append(node);if(over()&&group.childNodes.length>1){node.remove();newPage();group=el.cloneNode(false);page.append(group);group.append(node)}}return
  }
  if(over()&&el.matches('.tip,.notice,p')&&!el.querySelector('button,input,a')){
   el.remove();const words=el.textContent.trim().split(/\s+/);let block=el.cloneNode(false);page.append(block);
   for(const word of words){const prev=block.textContent;block.textContent+=(prev?' ':'')+word;if(over()&&prev){block.textContent=prev;newPage();block=el.cloneNode(false);block.textContent=word;page.append(block)}}return
  }
  if(over()&&el.matches('.options,.tiles,.match-grid')){
   el.remove();
   if(el.matches('.match-grid')){
    const cols=[...el.children],rows=cols.map(col=>[...col.children]);let grid=el.cloneNode(false),dest=cols.map(col=>{const c=col.cloneNode(false);grid.append(c);return c});page.append(grid);
    for(let i=0;i<Math.max(...rows.map(r=>r.length));i++){
     const pair=rows.map(r=>r[i]).filter(Boolean);pair.forEach((child,j)=>dest[j].append(child));
     if(over()&&i>0){pair.forEach(child=>child.remove());newPage();grid=el.cloneNode(false);dest=cols.map(col=>{const c=col.cloneNode(false);grid.append(c);return c});page.append(grid);pair.forEach((child,j)=>dest[j].append(child))}
    }return
   }
   const children=[...el.children];let group=el.cloneNode(false);page.append(group);
   for(const child of children){group.append(child);if(over()&&group.children.length>1){child.remove();newPage();group=el.cloneNode(false);page.append(group);group.append(child)}}
  }
 }
 newPage();for(const el of kids)add(el);
 // Remove empty fragments, never content.
 for(let i=pages.length-1;i>=0;i--)if(!pages[i].children.length){pages[i].remove();pages.splice(i,1)}
 if(feedback)view.fitPage=pages.length-1;else if((changed&&view.typed)||focusedId){const at=pages.findIndex(p=>p.querySelector('#typed'));if(at>=0)view.fitPage=at}
 let at=Math.min(view.fitPage||0,pages.length-1);
 function show(i){at=Math.max(0,Math.min(pages.length-1,i));view.fitPage=at;pages.forEach((p,j)=>p.hidden=j!==at);controls.innerHTML=pages.length>1?Arabic169.template("c435ac0d2a2411fc")`<button class="fit-prev" type="button" ${at===0?'disabled':''}>السابق</button><span role="status">جزء <bdi>${at+1} / ${pages.length}</bdi></span><button class="fit-next" type="button" ${at===pages.length-1?'disabled':''}>التالي</button>`:'';
 controls.querySelector('.fit-prev')?.addEventListener('click',()=>show(at-1));controls.querySelector('.fit-next')?.addEventListener('click',()=>show(at+1));
 shell.classList.toggle('has-fit-pages',pages.length>1);
 const btn=shell.querySelector('[data-action="check"]');if(btn&&['teach','teachdialog','alphabet','skillread','skilllisten','skillwrite'].includes(view.q?.type))btn.disabled=at<pages.length-1||(view.q?.type==='skillwrite'&&!view.writingModel);
 shell.dataset.fitPages=pages.length;shell.dataset.fitPage=at+1;
 }
 show(at);if(focusedId)document.getElementById(focusedId)?.focus({preventScroll:true});
 }finally{fitBusy=false}
}
window.addEventListener('resize',()=>{updateVisibleHeight307(true);fitScreen()});
if(window.visualViewport)visualViewport.addEventListener('resize',()=>{updateVisibleHeight307(true);fitScreen();if(typeof fitRoute==='function')fitRoute()});
fitScreen();
let routeBusy=false;
function fitRoute(){
 updateVisibleHeight307();
 if(routeBusy)return;const route=document.querySelector('.route122'),home=document.querySelector('.home122');if(!route&&!home)return;
 if(home){const holder=home.querySelector('.home122-paged');if(holder){const d=holder.querySelector('.route-deck');if(d)holder.outerHTML=d._sourceHTML}return;}
 routeBusy=true;
 try{
 const root=route||home,isHome=!!home;
 let source=isHome?home.querySelector('.home122-paged'):root.querySelector('.route122-source');
 if(isHome&&!source){source=document.createElement('section');source.className='home122-paged';const items=[...home.children].filter(el=>!el.matches('.home122-top,.mobile-nav'));home.querySelector('.home122-top').after(source);source.append(...items)}
 if(!source)return;
 const formNodes=[...source.querySelectorAll('input,select,textarea')],focused=source.contains(document.activeElement)?document.activeElement:null;const old=source.querySelector('.route-deck');if(old){source.innerHTML=old._sourceHTML;for(const el of formNodes)if(el.id)source.querySelector('#'+CSS.escape(el.id))?.replaceWith(el)}
 root.classList.toggle('formative-question-route',!!source.querySelector('.formative-question'));
 root.classList.add('scroll-route');delete root.dataset.routeParts;delete root.dataset.routePart;return;
 if(innerWidth>=1000){root.classList.add('desktop-route');delete root.dataset.routeParts;delete root.dataset.routePart;return}
 root.classList.remove('desktop-route');
 const sourceHTML=source.innerHTML;
 let parts=[...source.children];if(parts.length===1&&parts[0].matches('.reading,.dashboard'))parts=[...parts[0].children];
 let title=parts.find(n=>n.tagName==='H1');if(!title)title=parts.find(n=>n.matches('.sectionhead')&&n.querySelector('h1'));
 if(innerHeight<420&&innerWidth<450)title=null;const head=document.createElement('div');head.className='route122-heading';if(title){parts=parts.filter(n=>n!==title);head.append(title)}
 const deck=document.createElement('div');deck.className='route-deck';deck._sourceHTML=sourceHTML;
 const pager=document.createElement('nav');pager.className='fit-pages route-pages';pager.setAttribute('aria-label',Arabic169.primary("أجزاء الصفحة","ui"));pager.textContent=' ';
 source.replaceChildren(head,deck,pager);const pages=[];let page;
 function fresh(){page=document.createElement('div');page.className='route-part';deck.append(page);pages.push(page)}
 function over(){return page.scrollHeight>deck.clientHeight+1}
 function add(el,depth=0){
  page.append(el);
  if(over()&&page.children.length>1){el.remove();fresh();page.append(el)}
  if(over()&&el.matches('p,.notice,.tip')&&!el.querySelector('button,input,a,textarea')){el.remove();const words=el.textContent.trim().split(/\s+/);let block=el.cloneNode(false);page.append(block);for(const word of words){const prev=block.textContent;block.textContent+=(prev?' ':'')+word;if(over()&&prev){block.textContent=prev;fresh();block=el.cloneNode(false);block.textContent=word;page.append(block)}}return;}
  if(over()&&el.children.length>1&&depth<10&&!el.matches('button,a,input,select,label,.word,.mode-card,.home122-unit,.home122-tools')){
   el.remove();for(const child of [...el.children])add(child,depth+1)
  }
 }
 fresh();parts.forEach(el=>add(el));for(let i=pages.length-1;i>=0;i--)if(!pages[i].textContent.trim()&&!pages[i].querySelector('input,img,button')){pages[i].remove();pages.splice(i,1)}
 const key=view.page+':'+(view.pathPage||0)+':'+(view.courseLevel||'');if(view.routeFitKey!==key){view.routeFitKey=key;view.routeFitPage=0}
 function show(at){at=Math.max(0,Math.min(pages.length-1,at));view.routeFitPage=at;pages.forEach((el,i)=>el.hidden=i!==at);pager.innerHTML=pages.length>1?Arabic169.template("38fce2fc96092f01")`<button type="button" class="fit-prev" ${!at?'disabled':''}>السابق</button><span role="status">صفحة <bdi>${at+1} / ${pages.length}</bdi></span><button type="button" class="fit-next" ${at===pages.length-1?'disabled':''}>التالي</button>`:'';pager.querySelector('.fit-prev')?.addEventListener('click',()=>show(at-1));pager.querySelector('.fit-next')?.addEventListener('click',()=>show(at+1));root._showPart=show;root.dataset.routeParts=pages.length;root.dataset.routePart=at+1}
 show(view.routeFitPage||0);if(focused?.id){revealFitElement(document.getElementById(focused.id));document.getElementById(focused.id)?.focus({preventScroll:true})}
 }finally{routeBusy=false}
}
window.addEventListener('resize',()=>fitRoute());fitRoute();

function revealFitElement(el){if(!el)return;const page=el.closest('.route-part');const root=el.closest('.route122,.home122');if(page&&root?._showPart)root._showPart([...root.querySelectorAll('.route-part')].indexOf(page))}

if(document.fonts)document.fonts.ready.then(()=>{fitScreen();fitRoute()});
