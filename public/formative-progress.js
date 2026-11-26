function sanitizeFormative(input={}){
 const out={};
 if(!input||typeof input!=='object'||Array.isArray(input))return out;
 for(const [id,v]of Object.entries(input).slice(0,2000)){
  if(!/^(?:a1|a2|b1|b2|c1|c2)-(?:ut-u\d+|checkpoint-\d+)$/.test(id)||!v||!Number.isFinite(v.at)||![10,20].includes(v.count)||!Number.isInteger(v.bestCorrect)||v.bestCorrect<0||v.bestCorrect>v.count)continue;
  const seen=Array.isArray(v.seen)?v.seen.filter(x=>typeof x==='string'&&/^[a-z0-9-]{1,90}$/.test(x)).slice(0,30):[];
  out[id]={at:Math.min(v.at,Date.now()+300000),count:v.count,bestCorrect:v.bestCorrect,seen};
 }
 return out;
}
function mergeFormative(a,b){const out=sanitizeFormative(a);for(const[k,v]of Object.entries(sanitizeFormative(b))){const old=out[k];out[k]=old?{...(old.at>v.at?old:v),bestCorrect:Math.max(old.bestCorrect,v.bestCorrect)}:v}return out}
