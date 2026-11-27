/* Reviewed-only dictionary meanings. The extended dictionary is machine-derived and not reviewed, so its raw
   senses are no longer shown. Meanings come from the lesson words and a short list of checked entries. */
(()=>{
  if(window.__dict403)return;window.__dict403=1;
  const N=s=>String(s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f\u064b-\u065f\u0670]/g,'').replace(/[أإآ]/g,'ا').replace(/ى/g,'ي').replace(/\s+/g,' ').trim();
  const clean=s=>N(s).replace(/[^a-z\u0621-\u064a\s]/g,' ').replace(/\s+/g,' ').trim();
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const CHECKED=new Set(['genial','estupendo','maravilloso','bonito / bonita','hermoso / hermosa','guapo / guapa','grande','pequeño / pequeña','comer','escribir','libro','agua','casa','coche / automóvil','quiero'].map(x=>x.toLowerCase()));
  function install(){
    const D=globalThis.DIRECT305;if(!D||D.__d403)return false;
    const orig=D.lookup;
    let tk=0;
    D.lookup=async function(v){
      const my=++tk;
      const r=await orig.apply(this,arguments);
      if(my===tk){try{post(v)}catch(e){}}
      return r;
    };
    D.__d403=1;return true;
  }
  function post(v){
    const app=document.getElementById('app'),box=app&&app.querySelector('#direct305');if(!box)return;
    const q=clean(v);if(!q)return;
    const arabic=/[\u0600-\u06ff]/.test(q);
    const entries=(globalThis.LEARNING248&&globalThis.LEARNING248.index&&globalThis.LEARNING248.index().entries)||[];
    const lesson=entries.filter(e=>e.kind==='word'&&(arabic?clean(e.ar)===q:clean(e.es)===q));
    const keep=[];const seen=new Set();
    const add=(es,ar)=>{const k=clean(es);if(!seen.has(k)){seen.add(k);keep.push([es,ar])}};
    lesson.forEach(e=>add(e.es,e.ar));
    const B1=globalThis.B1VOCAB404||[];
    if(B1.length){const qw=q.split(' ');B1.forEach(r=>{const ce=clean(r[0]),ca=clean(r[1]);if(arabic?(ca===q||ca.split(' ').includes(q)||(qw.length>1&&ca.includes(q))):(ce===q||ce.split(' ').includes(q)||(qw.length>1&&ce.includes(q))))add(r[0],r[1])})}
    if(arabic){box.querySelectorAll('.direct305-row').forEach(row=>{const es=(row.querySelector('strong')||{}).textContent||'';const ar=(row.querySelector('p')||{}).textContent||'';if(CHECKED.has(es.toLowerCase()))add(es,ar)})}
    if(!keep.length){
      box.innerHTML='<section class="card direct305"><h2>'+(arabic?'بالإسبانية':'المعاني بالعربية')+'</h2><p>مفيش معنى مراجَع للكلمة دي لسه.</p><p class="small">بنعرض بس المعاني اللي اتراجعت. المعجم بيكبر مع كل تحديث، وممكن تدوّر في الدروس تحت.</p></section>';return}
    
    box.innerHTML='<section class="card direct305"><h2>'+(arabic?'بالإسبانية':'المعاني بالعربية')+'</h2>'+keep.map(r=>{const a='<button type="button" class="audio" data-action="audio" data-text="'+esc(r[0].split(' / ')[0])+'" data-speaker="" aria-label="اسمع النطق" title="اسمع النطق">◖))</button>';return '<div class="direct305-row"><div><strong lang="es" dir="ltr">'+esc(r[0])+'</strong><p>'+esc(r[1])+'</p></div>'+a+'</div>'}).join('')+'<p class="small">معاني مراجَعة من الدروس.</p></section>';
  }
  let n=0;const t=setInterval(()=>{if(install()||++n>100)clearInterval(t)},100);
})();
