/* Gramática y tiempos verbales: original lessons, Spanish first. Optional Arabic (fusha) toggle, off by default.
   Own wording. Not reviewed by a native speaker. Opens as an overlay so the app re-render never resets it. */
(()=>{
  if(window.__gram403)return;window.__gram403=1;
  const D=__DATA__,A=__AUDIO__;
  const app=document.getElementById('app');if(!app)return;
  const B=window.__back403;
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  // Arabic text with Latin words: each Latin run is isolated so the order never flips.
  const arh=s=>esc(s).replace(/[A-Za-zÀ-ÿ¿¡][A-Za-zÀ-ÿ'’.,¿?¡!+\-]*(?: [A-Za-zÀ-ÿ¿¡'’.,¿?¡!+\-]+)*/g,m=>'<bdi dir="ltr" lang="es">'+m+'</bdi>');
  const ARB=t=>st.ar&&t?'<span class="g4-ar" dir="rtl" lang="ar">'+arh(t)+'</span>':'';
  let st={}; try{st=JSON.parse(localStorage.getItem('gram403')||'{}')}catch(e){}
  const save=()=>{try{localStorage.setItem('gram403',JSON.stringify(st))}catch(e){}};
  st.done=st.done||{};st.ar=!!st.ar;
  const PAL={'Presente':['#087b79','🌞'],'Nombres y artículos':['#b8860b','🏷️'],'Imperativo':['#d6546a','📣'],'Pasado':['#d9772b','⏪'],'Presente y futuro':['#2f86c8','🚀'],'Comparar y relacionar':['#3f9a6b','⚖️'],'Condicional y subjuntivo':['#7256af','✨'],'Oraciones':['#8b5fbf','🧩']};
  const pal=g=>PAL[g]||['#087b79','📘'];
  const hex2rgba=(h,a)=>{const n=parseInt(h.slice(1),16);return 'rgba('+(n>>16)+','+((n>>8)&255)+','+(n&255)+','+a+')'};
  const pick=a=>a[Math.floor(Math.random()*a.length)];
  const OKS=['برافو! إجابة صح.','ممتاز! كمّل كده.','إيه الحلاوة دي!','صح! إنت بتتقدّم.','تمام يا بطل!','حلو أوي!'];
  const NOS=['مش مشكلة، الغلط بيعلّم.','قربت! بص على الصح.','ولا يهمك، ركّز في الجملة.','هتظبطها المرة الجاية!'];
  const fox=(pose,extra)=>{try{return '<span class="review-fox '+(extra||'')+'" data-pose="'+pose+'" role="img" aria-label="توتو">'+foxMarkup(pose)+'</span>'}catch(e){return ''}};
  let streak=0;
  const sfxOn=()=>{try{return state.settings.sfx!==false}catch(e){return true}};
  function sfx(ok){if(!sfxOn())return;try{const a=ok?J_CORRECT_PLAYERS[Math.max(0,Math.min(4,streak-1))]:J_WRONG_PLAYER;a.pause();a.currentTime=0;a.volume=1;a.play().catch(()=>{})}catch(e){}}
  function cheer(){if(!sfxOn())return;try{const a=reviewCues.complete;a.pause();a.currentTime=0;a.volume=1;a.play().catch(()=>{})}catch(e){}}
  const bubble=(txt,pose,cls)=>'<div class="g4-fx '+(cls||'')+'">'+fox(pose||'idle','g4-fox')+'<div class="g4-bub" dir="rtl" lang="ar">'+esc(txt)+'</div></div>';
  let ov=null,view={top:null},ans={},cur=null;
  const topic=id=>{for(const l of D.levels){const t=l.topics.find(x=>x.id===id);if(t)return t}return null};
  const levelOf=id=>D.levels.find(l=>l.topics.some(t=>t.id===id));
  function foxSay(on){try{const f=document.querySelector('#gram403 .g4-fx .review-fox');if(f)foxPose(f,on?'speaking':'idle')}catch(e){}}
  function play(es,btn){const f=A[es];if(!f)return;try{if(cur){cur.pause()}document.querySelectorAll('#gram403 .g4-play.on').forEach(x=>x.classList.remove('on'));cur=new Audio(f);const done=()=>{if(btn)btn.classList.remove('on');foxSay(false)};if(btn)btn.classList.add('on');foxSay(true);cur.onended=done;cur.play().catch(done)}catch(e){}}
  function css(){
    if(document.getElementById('gram403css'))return;
    const s=document.createElement('style');s.id='gram403css';
    s.textContent=`
#gram403{--g4:var(--teal247,#087b79);--g4line:rgba(128,128,128,.28);--g4bg:rgba(128,128,128,.07);font-size:16px;line-height:1.5}
#gram403 *{box-sizing:border-box}
#gram403 .g4-bar{position:sticky;top:-14px;z-index:2;margin:-14px -14px 12px;padding:10px 14px;display:flex;align-items:center;gap:10px;background:var(--g4bgc,#fff);border-bottom:1px solid var(--g4line)}
#gram403 .g4-bar h1{font-size:17px;margin:0;flex:1;min-width:0;line-height:1.25;font-weight:700}
#gram403 .g4-ic{flex:0 0 auto;width:40px;height:40px;border-radius:50%;border:1px solid var(--g4line);background:transparent;color:inherit;font-size:20px;line-height:1;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;padding:0}
#gram403 .g4-card{border:1px solid var(--g4line);background:var(--g4bg);border-radius:18px;padding:16px;margin:0 0 14px}
#gram403 .g4-card h2{font-size:13px;letter-spacing:.06em;text-transform:uppercase;margin:0 0 10px;color:var(--g4);font-weight:800}
#gram403 .g4-intro{margin:0 0 12px;opacity:.85}
#gram403 .g4-tog{display:flex;align-items:center;justify-content:space-between;gap:12px;width:100%;padding:12px 14px;border:1px solid var(--g4line);border-radius:14px;background:transparent;color:inherit;font:inherit;cursor:pointer;margin:0 0 14px;text-align:start}
#gram403 .g4-sw{flex:0 0 auto;width:44px;height:26px;border-radius:13px;background:rgba(128,128,128,.4);position:relative;transition:background .15s}
#gram403 .g4-sw::after{content:"";position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff;transition:transform .15s}
#gram403 .g4-tog[aria-checked=true] .g4-sw{background:var(--g4)}
#gram403 .g4-tog[aria-checked=true] .g4-sw::after{transform:translateX(18px)}
#gram403 .g4-ar{display:block;margin-top:2px;font-size:.92em;opacity:.85;text-align:right;line-height:1.7}
#gram403 .g4-lvh{display:flex;align-items:center;justify-content:space-between;gap:10px;margin:0 0 6px}
#gram403 .g4-lvh h2{margin:0;font-size:20px;letter-spacing:0;text-transform:none;color:inherit}
#gram403 .g4-badge{font-size:12px;font-weight:700;padding:3px 10px;border-radius:99px;border:1px solid var(--g4line)}
#gram403 .g4-bar-p{height:8px;border-radius:4px;background:rgba(128,128,128,.25);overflow:hidden;margin:8px 0 4px}
#gram403 .g4-bar-p i{display:block;height:100%;background:var(--g4);border-radius:4px}
#gram403 .g4-sub{font-size:13px;opacity:.75;margin:0}
#gram403 .g4-grp{font-size:12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;opacity:.7;margin:14px 0 6px}
#gram403 .g4-row{display:flex;align-items:center;gap:12px;width:100%;padding:11px 12px;margin:0 0 8px;border:1px solid var(--g4line);border-radius:14px;background:transparent;color:inherit;font:inherit;text-align:start;cursor:pointer}
#gram403 .g4-row:active{background:var(--g4bg)}
#gram403 .g4-num{flex:0 0 auto;width:32px;height:32px;border-radius:50%;background:var(--g4bg);border:1px solid var(--g4line);display:inline-flex;align-items:center;justify-content:center;font-weight:700;font-size:14px}
#gram403 .g4-row.done .g4-num{background:var(--g4);border-color:var(--g4);color:#fff}
#gram403 .g4-tx{flex:1;min-width:0;display:block}
#gram403 .g4-tx b{display:block;font-weight:700;line-height:1.3}
#gram403 .g4-go{flex:0 0 auto;opacity:.5}
#gram403 .g4-soon{opacity:.6}
#gram403 .g4-rule p{margin:0 0 8px}
#gram403 .g4-tbl{overflow-x:auto;margin:10px 0 0;border:1px solid var(--g4line);border-radius:12px}
#gram403 table{border-collapse:collapse;width:100%;font-size:14px}
#gram403 th{text-align:start;padding:8px 8px;background:var(--g4bg);font-weight:700;white-space:nowrap}
#gram403 td{padding:8px 8px;border-top:1px solid var(--g4line)}
#gram403 td:first-child{opacity:.75}
#gram403 td+td{font-weight:600}
#gram403 .g4-ex{display:flex;gap:10px;align-items:flex-start;padding:10px 0;border-top:1px solid var(--g4line)}
#gram403 .g4-ex:first-of-type{border-top:0}
#gram403 .g4-play{flex:0 0 auto;width:40px;height:40px;border-radius:50%;border:0;background:var(--g4);color:#fff;font-size:15px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;padding:0}
#gram403 .g4-play.on{outline:3px solid rgba(8,123,121,.35)}
#gram403 .g4-ex .g4-tx{padding-top:1px}
#gram403 .g4-q{margin:0 0 14px;padding-bottom:14px;border-bottom:1px solid var(--g4line)}
#gram403 .g4-q:last-of-type{border-bottom:0;margin-bottom:6px}
#gram403 .g4-qt{font-weight:600;margin:0 0 8px}
#gram403 .g4-opts{display:grid;grid-template-columns:1fr;gap:8px}
#gram403 .g4-opt{padding:11px 14px;border-radius:12px;border:1.5px solid var(--g4line);background:transparent;color:inherit;font:inherit;text-align:start;cursor:pointer}
#gram403 .g4-opt[disabled]{cursor:default;opacity:1}
#gram403 .g4-opt.ok{border-color:#2fb37a;background:rgba(47,179,122,.15)}
#gram403 .g4-opt.no{border-color:#e5586a;background:rgba(229,88,106,.14)}
#gram403 .g4-fb{margin:8px 0 0;font-size:14px}
#gram403 .g4-score{text-align:center;padding:12px 0 4px;font-weight:700}
#gram403 .g4-fx{display:flex;align-items:center;gap:10px;margin:0 0 14px}
#gram403 .g4-fox{width:64px;height:72px;flex:0 0 auto}
#gram403 .g4-bub{position:relative;flex:1;padding:10px 14px;border-radius:16px;background:var(--g4tint,var(--g4bg));border:1px solid var(--g4line);font-weight:600;line-height:1.6}
#gram403 .g4-bub::before{content:"";position:absolute;right:100%;top:50%;margin-top:-7px;border:7px solid transparent;border-left-color:transparent;border-right-color:var(--g4line)}
#gram403 .g4-hero{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:16px;background:var(--g4tint);border:1px solid var(--g4line);margin:0 0 12px}
#gram403 .g4-hero .g4-emo{font-size:26px;line-height:1}
#gram403 .g4-fb2{display:flex;align-items:center;gap:10px;margin:10px 0 0;padding:10px 12px;border-radius:14px}
#gram403 .g4-fb2.good{background:rgba(47,179,122,.15);border:1px solid #2fb37a}
#gram403 .g4-fb2.bad{background:rgba(229,88,106,.13);border:1px solid #e5586a}
#gram403 .g4-fb2 .g4-fox{width:48px;height:54px}
#gram403 .g4-fb2 h3{margin:0 0 2px;font-size:15px}
#gram403 .g4-fb2 p{margin:0;font-size:14px}
#gram403 .g4-done{text-align:center;padding:14px 8px 6px;border-radius:16px;background:var(--g4tint);border:1px solid var(--g4line)}
#gram403 .g4-done .g4-fox{width:130px;height:140px}
#gram403 .g4-done h3{margin:6px 0 2px;font-size:19px}
#gram403 .g4-stars{font-size:24px;letter-spacing:4px;margin:4px 0 8px}
#gram403 .g4-act{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:10px}
#gram403 .g4-btn.fill{background:var(--g4);color:#fff}
#gram403 .g4-gdot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-inline-end:6px;vertical-align:middle}
#gram403 .g4-btn{padding:11px 18px;border-radius:12px;border:1.5px solid var(--g4);background:transparent;color:var(--g4);font:inherit;font-weight:700;cursor:pointer}
`;
    document.head.appendChild(s);
  }
  const btn=(c,a,txt,extra)=>'<button type="button" class="'+c+'" data-g="'+a+'" '+(extra||'')+'>'+txt+'</button>';
  function tog(){return '<button type="button" class="g4-tog" role="switch" aria-checked="'+(st.ar?'true':'false')+'" data-g="ar"><span><b>Traducción al árabe</b><span class="g4-ar" dir="rtl" lang="ar" style="opacity:.75">الترجمة العربية (فصحى)</span></span><span class="g4-sw" aria-hidden="true"></span></button>'}
  function bar(title,back){return '<div class="g4-bar">'+btn('g4-ic',back,back==='close'?'✕':'←','aria-label="'+(back==='close'?'Cerrar':'Volver')+'"')+'<h1>'+esc(title)+'</h1>'+(back==='close'?'':btn('g4-ic','close','✕','aria-label="Cerrar"'))+'</div>'}
  function home(){
    let h=bar('Gramática y tiempos','close');
    h+='<p class="g4-intro">Reglas, tablas de conjugación, ejemplos con audio y ejercicios. Del nivel A1 al C2.</p>'+tog()+bubble(pick(['أهلاً! أنا توتو. اختار مستواك وتعالَ نتعلّم القواعد سوا.','يلا نبدأ! كل درس قصير وفيه تمارين حلوة.']),'idle');
    for(const l of D.levels){
      const n=l.topics.length,d=l.topics.filter(t=>st.done[t.id]).length;
      h+='<section class="g4-card'+(n?'':' g4-soon')+'"><div class="g4-lvh"><h2>Nivel '+l.id+'</h2><span class="g4-badge">'+(n?d+' / '+n:'Próximamente')+'</span></div><p class="g4-sub">'+esc(l.desc)+'</p>'+ARB(l.ar);
      if(n){
        h+='<div class="g4-bar-p" role="progressbar" aria-valuemin="0" aria-valuemax="'+n+'" aria-valuenow="'+d+'"><i style="width:'+Math.round(100*d/n)+'%"></i></div>';
        let i=0;const groups=[];
        l.topics.forEach(t=>{let g=groups.find(x=>x.es===t.group);if(!g){g={es:t.group,ar:t.groupAr,items:[]};groups.push(g)}g.items.push(t)});
        for(const g of groups){
          h+='<div class="g4-grp"><i class="g4-gdot" style="background:'+pal(g.es)[0]+'"></i>'+pal(g.es)[1]+' '+esc(g.es)+(st.ar&&g.ar?' · <span dir="rtl" lang="ar">'+arh(g.ar)+'</span>':'')+'</div>';
          for(const t of g.items){i=l.topics.indexOf(t)+1;
            h+='<button type="button" style="--g4:'+pal(t.group)[0]+'" class="g4-row'+(st.done[t.id]?' done':'')+'" data-g="open" data-id="'+t.id+'"><span class="g4-num">'+(st.done[t.id]?'✓':i)+'</span><span class="g4-tx"><b>'+esc(t.es)+'</b>'+ARB(t.ar)+'</span><span class="g4-go" aria-hidden="true">›</span></button>';
          }
        }
      }
      h+='</section>';
    }
    return h;
  }
  function table(tb){
    return '<div class="g4-tbl"><table><thead><tr>'+tb.head.map(x=>'<th>'+esc(x)+'</th>').join('')+'</tr></thead><tbody>'+tb.rows.map(r=>'<tr>'+r.map(c=>'<td>'+esc(c)+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>';
  }
  function topicView(t){
    const lv=levelOf(t.id),num=lv.topics.indexOf(t)+1;
    const P=pal(t.group);let h='<div style="--g4:'+P[0]+';--g4tint:'+hex2rgba(P[0],.12)+'">'+bar(t.es,'home');
    h+='<div class="g4-hero"><span class="g4-emo">'+P[1]+'</span><b>'+esc(t.group)+'</b></div>'+bubble(pick(['شوف القاعدة الأول، وبعدين اسمع الأمثلة.','ركّز في الجدول، هو أهم حاجة هنا!','مستعد؟ يلا نشوف الدرس.']),'idle');
    h+='<p class="g4-sub" style="margin:0 0 12px"><span class="g4-badge">'+lv.id+' · Tema '+num+' de '+lv.topics.length+'</span></p>'+ARB(t.ar)+(st.ar?'<div style="height:10px"></div>':'');
    h+='<section class="g4-card g4-rule"><h2>Regla</h2>'+t.rule.map(r=>'<p>'+esc(r[0])+ARB(r[1])+'</p>').join('')+table(t.table)+'</section>';
    h+='<section class="g4-card"><h2>Ejemplos</h2>'+t.ex.map(e=>'<div class="g4-ex"><button type="button" class="g4-play" data-g="play" data-es="'+esc(e[0])+'" aria-label="Escuchar: '+esc(e[0])+'">▶</button><span class="g4-tx">'+esc(e[0])+ARB(e[1])+'</span></div>').join('')+'</section>';
    const n=t.exe.length,k=t.exe.filter((e,i)=>ans[t.id+i]!==undefined).length,ok=t.exe.filter((e,i)=>ans[t.id+i]===e[2]).length;
    h+='<section class="g4-card"><h2>Ejercicios · '+k+' de '+n+'</h2><p class="g4-sub" style="margin:0 0 12px">Elige la forma correcta. Al contestar oirás la frase completa.</p>'+
      t.exe.map((e,i)=>{const a=ans[t.id+i];return '<div class="g4-q"><p class="g4-qt">'+(i+1)+'. '+esc(e[0]).replace('___','<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>')+'</p><div class="g4-opts">'+
        e[1].map((o,j)=>{let c='g4-opt';if(a!==undefined){if(j===e[2])c+=' ok';else if(j===a)c+=' no'}
          return '<button type="button" class="'+c+'" data-g="ans" data-t="'+t.id+'" data-i="'+i+'" data-j="'+j+'" '+(a!==undefined?'disabled':'')+'>'+esc(o)+'</button>'}).join('')+'</div>'+
        (a!==undefined?'<div class="g4-fb2 '+(a===e[2]?'good':'bad')+'" role="status">'+fox(a===e[2]?'correct':'tryagain','g4-fox')+'<div><h3>'+(a===e[2]?pick(OKS):pick(NOS))+'</h3><p>'+(a===e[2]?'✓ Correcto. ':'✗ La respuesta es «'+esc(e[1][e[2]])+'». ')+esc(e[3])+'</p></div></div>':'')+'</div>'}).join('');
    if(k===n){const r=ok/n,stars=r>=.9?3:r>=.6?2:1;h+='<div class="g4-done" role="status">'+fox('complete','g4-fox')+'<div class="g4-stars" aria-hidden="true">'+'⭐'.repeat(stars)+'</div><h3>'+(r>=.6?'¡Terminaste el tema!':'¡Buen intento!')+'</h3><p dir="rtl" lang="ar" style="margin:0">'+(r>=.6?'عاش يا بطل! خلّصت الدرس.':'كمّل وحاول تاني، هتبقى أحسن.')+'</p><p class="g4-score" style="margin:6px 0">Resultado: '+ok+' de '+n+'</p><div class="g4-act">'+btn('g4-btn','retry','Repetir')+btn('g4-btn fill','home','Volver a los temas')+'</div></div>'}
    h+='</section></div>';
    return h;
  }
  function draw(){if(!ov)return;ov.querySelector('.g403body').innerHTML=view.top?topicView(topic(view.top)):home()}
  function open(){
    if(ov)return;css();
    const cs=getComputedStyle(document.body);
    ov=document.createElement('div');ov.id='gram403';ov.setAttribute('role','dialog');ov.setAttribute('aria-label','Gramática y tiempos');
    ov.style.setProperty('--g4bgc',cs.backgroundColor);ov.style.cssText='--g4bgc:'+cs.backgroundColor+';position:fixed;inset:0;z-index:9999;overflow:auto;-webkit-overflow-scrolling:touch;background:'+cs.backgroundColor+';color:'+cs.color+';padding:14px;';
    ov.innerHTML='<div class="g403body" dir="ltr" lang="es" style="max-width:720px;margin:0 auto;padding-bottom:60px"></div>';
    document.body.appendChild(ov);draw();ov.scrollTop=0;B&&B.open('g-root',()=>close(true));
    ov.addEventListener('click',onClick);
  }
  function close(fromBack){if(!fromBack&&B&&B.closeAll('g-'))return;if(cur){try{cur.pause()}catch(e){}}if(ov){ov.remove();ov=null}view={top:null}}
  function onClick(e){
    const b=e.target.closest('[data-g]');if(!b)return;e.stopPropagation();
    const a=b.dataset.g;
    if(a==='close')return close();
    if(a==='home'){if(view.top&&B&&B.depth())return B.back('g-topic');view.top=null;draw();ov.scrollTop=0;return}
    if(a==='open'){view.top=b.dataset.id;draw();ov.scrollTop=0;B&&B.open('g-topic',()=>{view.top=null;if(ov){draw();ov.scrollTop=0}});return}
    if(a==='play')return play(b.dataset.es,b);
    if(a==='ar'){st.ar=!st.ar;save();const y=ov.scrollTop;draw();ov.scrollTop=y;return}
    if(a==='retry'){const t=topic(view.top);t.exe.forEach((x,i)=>delete ans[t.id+i]);draw();ov.scrollTop=0;return}
    if(a==='ans'){
      const t=topic(b.dataset.t),i=+b.dataset.i,j=+b.dataset.j;ans[t.id+i]=j;const okk=j===t.exe[i][2];streak=okk?streak+1:0;sfx(okk);const fin=t.exe.every((x,k)=>ans[t.id+k]!==undefined);setTimeout(()=>{play(t.exe[i][3]);if(fin)setTimeout(cheer,1800)},650);
      if(t.exe.every((x,k)=>ans[t.id+k]!==undefined)){st.done[t.id]=1;save()}
      const y=ov.scrollTop;draw();ov.scrollTop=y;
    }
  }
  const AD=n=>String(n).replace(/\d/g,d=>'٠١٢٣٤٥٦٧٨٩'[d]);
  function inject(){
    if(app.querySelector('#gram403card'))return;
    const grid=app.querySelector('.track-grid166');if(!grid)return;
    const lv=D.levels.filter(l=>l.topics.length).length,tp=D.levels.reduce((n,l)=>n+l.topics.length,0),ex=D.levels.reduce((n,l)=>n+l.topics.reduce((m,t)=>m+t.exe.length,0),0);
    const c=document.createElement('button');c.type='button';c.id='gram403card';c.className='track-card166';c.setAttribute('data-g403','open');
    c.innerHTML='<img src="assets/features166/grammar.svg" alt=""><span class="track-copy166"><strong>قواعد وأزمنة</strong><span>قواعد الإسبانية وأزمنتها بجداول تصريف وأمثلة صوتية وتمارين.</span><small>'+(lv===2?'مستويان':AD(lv)+' مستويات')+' · '+AD(tp)+' موضوعًا · '+AD(ex)+' تمرينًا</small><b>افتح القسم ←</b></span>';
    grid.appendChild(c);
  }
  app.addEventListener('click',e=>{const b=e.target.closest('[data-g403]');if(!b)return;e.stopPropagation();e.preventDefault();open()},true);
  new MutationObserver(inject).observe(app,{childList:true,subtree:true});
  inject();
})();
