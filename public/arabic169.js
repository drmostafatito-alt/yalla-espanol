/* Translation-only 170. UI uses the live 169 default; saved register values migrate without touching progress. */
const Arabic169=(()=>{
 const KEY='yalla-arabic-display169',maps=new Map(),templates=new Map(),sourceAliases=new Map(),missing=new Set();const mode='egyptian';
 try{localStorage.setItem(KEY,'msa')}catch{}
 const escape=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 function install(domain,entries){const map=new Map();for(const e of entries){if(typeof e.egyptian!=='string'||typeof e.msa!=='string'||!e.msa.trim()||e.reviewStatus!=='approved')throw Error('Unreviewed Arabic pack: '+domain);const existing=map.get(e.egyptian);if(existing&&existing!==e.msa)throw Error('Conflicting Arabic pack: '+domain);map.set(e.egyptian,e.msa)}maps.set(domain,map);const aliases=entries.filter(e=>typeof e.displayEgyptian169==='string');if(aliases.length)sourceAliases.set(domain,new Map(aliases.map(e=>[e.egyptian,e.displayEgyptian169])))}
 function find(text,domain){text=String(text??'');if(!/[\u0600-\u06ff]/.test(text))return text;const value=maps.get(domain)?.get(text);if(value!==undefined)return value;missing.add(domain+'\0'+text);return text}
 function has(text,domain){return maps.get(domain)?.has(String(text??''))||false}
 function primary(text,domain='ui'){return mode==='egyptian'?(sourceAliases.get(domain)?.get(String(text??''))??String(text??'')):find(text,domain)}
 function learning(text,domain){return '<span class="ar169-single" lang="ar">'+escape(find(String(text??''),domain))+'</span>'}
 function installTemplates(entries){for(const e of entries){if(e.reviewStatus!=='approved'||!Array.isArray(e.quasis)||!Array.isArray(e.msaQuasis)||e.quasis.length!==e.msaQuasis.length)throw Error('Unreviewed UI template');templates.set(e.key,e)}}
 function template(key){return (strings,...values)=>{const entry=templates.get(key);if(!entry)missing.add('ui-template\0'+key);const parts=mode==='egyptian'||!entry?strings:entry.msaQuasis;return parts.reduce((out,p,i)=>out+p+(i<values.length?String(values[i]):''),'')}}
 function setMode(){try{localStorage.setItem(KEY,'msa')}catch{}document.documentElement.dataset.arabicDisplay169='msa'}
 function domainForLesson(lesson){if(lesson?.sectionId&&lesson.sectionId!=='main')return 'track-'+lesson.sectionId;return /^A[2]$|^[BC][12]$/.test(lesson?.level||'')?'level-'+lesson.level:'main-A1'}
 document.documentElement.dataset.arabicDisplay169='msa';
 function installSourceAliases(domain,entries){sourceAliases.set(domain,new Map([...(sourceAliases.get(domain)||[]),...entries.map(e=>[e.original,e.display])]))}
 return Object.freeze({has,formal:find,install,installSourceAliases,installTemplates,template,primary,learning,setMode,domainForLesson,getMode:()=>mode,missing:()=>[...missing],clearProtected:()=>{for(const key of maps.keys())if(key.startsWith('level-')||key==='placement')maps.delete(key);for(const key of sourceAliases.keys())if(key.startsWith('level-')||key==='placement')sourceAliases.delete(key)}})
})();
