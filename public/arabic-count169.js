/* Numeric labels avoid fragile case endings around dynamic counters. */
const ArabicCount169=(()=>{
 const nouns={learningStep:['خطوة تعلّم واحدة','خطوتا تعلّم','خطوات تعلّم','خطوة تعلّم','خطوة تعلّم'],day:['يوم واحد','يومان','أيام','يومًا','يوم'],segment:['مقطع واحد','مقطعان','مقاطع','مقطعًا','مقطع'],expression:['تعبير واحد','تعبيران','تعبيرات','تعبيرًا','تعبير'],lesson:['درس واحد','درسان','دروس','درسًا','درس'],step:['خطوة واحدة','خطوتان','خطوات','خطوة','خطوة'],unit:['وحدة واحدة','وحدتان','وحدات','وحدة','وحدة'],situation:['موقف واحد','موقفان','مواقف','موقفًا','موقف'],file:['ملف واحد','ملفان','ملفات','ملفًا','ملف'],minute:['دقيقة واحدة','دقيقتان','دقائق','دقيقة','دقيقة'],question:['سؤال واحد','سؤالان','أسئلة','سؤالًا','سؤال'],pair:['زوج واحد','زوجان','أزواج','زوجًا','زوج']};
 const number=new Intl.NumberFormat('ar-EG',{useGrouping:false});
 function label(n,type){if(!Number.isInteger(n)||n<0||!nouns[type])throw Error('Invalid Arabic counter');const forms=nouns[type],mod=n%100;if(n===0)return '٠ '+forms[2];if(n===1)return forms[0];if(n===2)return type==='learningStep'&&typeof Arabic169!=='undefined'&&Arabic169.getMode()==='egyptian'?'خطوتين تعلّم':forms[1];const form=mod>=3&&mod<=10?forms[2]:mod>=11&&mod<=99?forms[3]:forms[4];return number.format(n)+' '+form}
 // These labels deliberately use a heading plus a colon, so suffix adjectives do not acquire incorrect number agreement.
 function contextual(n,type,context){const titles={waiting:'بانتظارك',review:'للمراجعة',availableA1:'المتاح ضمن A1',basic:'التدريب الأساسي',duration:'مدة الاختبار',count:'العدد'};if(!titles[context])throw Error('Invalid counter context');return context==='count'||context==='duration'?label(n,type):titles[context]+': '+label(n,type)}
 function selected(n,type,egyptian,context='count'){return typeof Arabic169==='undefined'||Arabic169.getMode()==='egyptian'?(typeof egyptian==='number'?number.format(egyptian):egyptian):contextual(n,type,context)}
 function format(n){if(typeof n!=='number'||!Number.isFinite(n))throw Error('Invalid display number');return number.format(n)}
 return Object.freeze({label,contextual,selected,format});
})();
