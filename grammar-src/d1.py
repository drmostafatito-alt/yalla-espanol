# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))

topic('a1-irregulares-presente','Presente: verbos irregulares','المضارع: الأفعال الشاذة',
 [('Muchos verbos cambian la vocal de la raíz en yo, tú, él y ellos, pero no en nosotros: querer es quiero, queremos; poder es puedo, podemos.','تغيّر أفعال كثيرة حرف العلة في الجذع مع yo وtú وél وellos، ولا تغيّره مع nosotros.'),
  ('Otros verbos son irregulares solo en yo: tener es tengo, hacer es hago, salir es salgo.','وبعض الأفعال شاذ في yo فقط، مثل tengo وhago وsalgo.')],
 {'nohl':1,'head':['','querer','poder','tener'],'rows':[['yo','quiero','puedo','tengo'],['tú','quieres','puedes','tienes'],['nosotros','queremos','podemos','tenemos'],['ellos','quieren','pueden','tienen']]},
 [('Quiero un café.','أريد قهوة.'),('¿Puedes ayudarme?','هل تستطيع مساعدتي؟'),('Tengo dos hermanos.','لدي أخوان.'),('Nosotros queremos viajar.','نريد أن نسافر.'),('Ella duerme ocho horas.','هي تنام ثماني ساعات.'),('Ellos vuelven a casa a las seis.','هم يعودون إلى البيت في السادسة.')],
 [('Yo ___ un café.',['quiero','queremos','quieres'],0,'Yo quiero un café.'),
  ('Tú ___ ayudarme.',['podemos','puedes','puedo'],1,'Tú puedes ayudarme.'),
  ('Yo ___ dos hermanos.',['tengo','tienes','tenemos'],0,'Yo tengo dos hermanos.'),
  ('Nosotros ___ viajar en verano.',['quieren','quiero','queremos'],2,'Nosotros queremos viajar en verano.'),
  ('Ella ___ ocho horas.',['dormimos','duerme','duermo'],1,'Ella duerme ocho horas.'),
  ('Yo ___ de casa a las ocho.',['salgo','sales','salimos'],0,'Yo salgo de casa a las ocho.')])

topic('a1-demostrativos-posesivos','Demostrativos y posesivos','أسماء الإشارة وصفات الملكية',
 [('Los demostrativos señalan la distancia: este, esta (cerca), ese, esa (a media distancia) y aquel, aquella (lejos). Concuerdan en género y número.','تدل أسماء الإشارة على القرب والبعد: este وesta للقريب، وese وesa للمتوسط، وaquel وaquella للبعيد، وتطابق المسمّى في الجنس والعدد.'),
  ('Los posesivos van antes del nombre: mi, tu, su, nuestro. Concuerdan con lo poseído: mi casa, mis casas, nuestra casa.','تأتي صفات الملكية قبل الاسم وتطابق المملوك: mi casa وmis casas وnuestra casa.')],
 {'nohl':1,'head':['','cerca','lejos'],'rows':[['masculino','este libro','aquel libro'],['femenino','esta casa','aquella casa'],['plural masc.','estos libros','aquellos libros'],['plural fem.','estas casas','aquellas casas']]},
 [('Este libro es interesante.','هذا الكتاب مثير للاهتمام.'),('Esa casa es muy grande.','ذلك البيت كبير جدًا.'),('Aquellos coches son rápidos.','تلك السيارات سريعة.'),('Mi madre trabaja aquí.','أمي تعمل هنا.'),('Nuestra casa es pequeña.','بيتنا صغير.'),('¿Dónde está tu móvil?','أين هاتفك؟')],
 [('___ libro es interesante.',['Este','Esta','Estos'],0,'Este libro es interesante.'),
  ('___ casas son muy bonitas.',['Estas','Estos','Este'],0,'Estas casas son muy bonitas.'),
  ('Aquella montaña está muy ___.',['lejos','cerca','aquí'],0,'Aquella montaña está muy lejos.'),
  ('Yo vivo con ___ padres.',['mi','mis','nuestra'],1,'Yo vivo con mis padres.'),
  ('Nosotros vendemos ___ casa.',['nuestra','nuestro','mi'],0,'Nosotros vendemos nuestra casa.'),
  ('¿Dónde está ___ móvil?',['tu','tus','tuya'],0,'¿Dónde está tu móvil?')])

topic('a1-interrogativos','Palabras interrogativas','أدوات الاستفهام',
 [('Las palabras interrogativas llevan tilde y van al principio: qué, quién, dónde, cuándo, cómo, cuánto, por qué.','أدوات الاستفهام تحمل علامة التشديد وتأتي في أول الجملة: qué وquién وdónde وcuándo وcómo وcuánto وpor qué.'),
  ('Cuánto concuerda con el nombre: cuánto tiempo, cuánta agua, cuántos años, cuántas personas. Para responder a por qué usamos porque.','تتفق cuánto مع الاسم في الجنس والعدد، وللإجابة عن por qué نستعمل porque.')],
 {'nohl':1,'head':['','pregunta','significa'],'rows':[['qué','¿Qué haces?','ماذا'],['quién','¿Quién es ella?','من'],['dónde','¿Dónde vives?','أين'],['cuándo','¿Cuándo llegas?','متى'],['cómo','¿Cómo estás?','كيف'],['cuánto','¿Cuánto cuesta?','كم']]},
 [('¿Qué haces?','ماذا تفعل؟'),('¿Quién es ella?','من هي؟'),('¿Dónde vives?','أين تسكن؟'),('¿Cuándo llegas?','متى تصل؟'),('¿Cuánto cuesta?','كم يكلّف؟'),('¿Por qué estudias español?','لماذا تدرس الإسبانية؟')],
 [('¿___ vives?',['Dónde','Cuándo','Quién'],0,'¿Dónde vives?'),
  ('¿___ es ella?',['Qué','Quién','Cuánto'],1,'¿Quién es ella?'),
  ('¿___ llegas a casa?',['Cuándo','Dónde','Quién'],0,'¿Cuándo llegas a casa?'),
  ('¿___ años tienes?',['Cuánto','Cuántos','Cuánta'],1,'¿Cuántos años tienes?'),
  ('¿___ estás hoy?',['Cómo','Cuándo','Dónde'],0,'¿Cómo estás hoy?'),
  ('¿___ personas viven aquí?',['Cuántos','Cuántas','Cuánta'],1,'¿Cuántas personas viven aquí?')])

topic('a2-pronombres-objeto','Pronombres de objeto','ضمائر المفعول به',
 [('Los pronombres de objeto directo son lo, la, los, las y van antes del verbo: Compro el pan, lo compro. ¿Ves a María? Sí, la veo.','ضمائر المفعول المباشر هي lo وla وlos وlas، وتوضع قبل الفعل.'),
  ('Los de objeto indirecto son me, te, le, nos, les. Si van juntos, el indirecto va primero y le o les cambia a se: Se lo doy a mi madre.','وضمائر المفعول غير المباشر هي me وte وle وnos وles، وإذا اجتمعت يتقدّم غير المباشر، وتتحول le وles إلى se.')],
 {'nohl':1,'head':['','directo','indirecto'],'rows':[['yo','me','me'],['tú','te','te'],['él, ella','lo, la','le (se)'],['nosotros','nos','nos'],['ellos','los, las','les (se)']]},
 [('Compro el pan y lo como.','أشتري الخبز وآكله.'),('¿Ves a María? Sí, la veo.','هل ترين ماريا؟ نعم أراها.'),('Te doy un regalo.','أعطيك هدية.'),('Se lo doy a mi madre.','أعطيه لأمي.'),('Nos llaman cada día.','يتصلون بنا كل يوم.'),('Les escribo un mensaje.','أكتب لهم رسالة.')],
 [('¿Ves el libro? Sí, ___ veo.',['lo','la','le'],0,'¿Ves el libro? Sí, lo veo.'),
  ('¿Conoces a Ana? Sí, ___ conozco.',['lo','la','les'],1,'¿Conoces a Ana? Sí, la conozco.'),
  ('___ doy un regalo a mi hermano.',['Le','Lo','Los'],0,'Le doy un regalo a mi hermano.'),
  ('¿El libro? Se ___ doy a mi madre.',['lo','la','le'],0,'¿El libro? Se lo doy a mi madre.'),
  ('Ellos ___ llaman a nosotros cada día.',['nos','les','os'],0,'Ellos nos llaman a nosotros cada día.'),
  ('¿Las llaves? ___ tengo aquí.',['Las','Los','Le'],0,'¿Las llaves? Las tengo aquí.')])

topic('a2-hace-desde','Hace, desde y desde hace','hace وdesde وdesde hace',
 [('Hace + tiempo indica cuánto tiempo pasó desde un hecho: Llegué hace dos horas. Desde hace + tiempo indica una acción que continúa: Vivo aquí desde hace tres años.','hace مع مدة زمنية تبيّن كم مضى على حدث منتهٍ، وdesde hace تبيّن فعلًا مستمرًّا حتى الآن.'),
  ('Desde + punto en el tiempo indica el inicio: Estudio español desde enero. Para preguntar usamos ¿Cuánto tiempo hace que…?','وdesde مع نقطة زمنية تبيّن بداية الفعل، وللسؤال نقول: ¿Cuánto tiempo hace que…؟')],
 {'nohl':1,'head':['','estructura','ejemplo'],'rows':[['hecho pasado','hace + tiempo','Llegué hace dos horas.'],['continúa','desde hace + tiempo','Vivo aquí desde hace tres años.'],['inicio','desde + momento','Estudio desde enero.']]},
 [('Vivo aquí desde hace tres años.','أسكن هنا منذ ثلاث سنوات.'),('Llegué hace dos horas.','وصلت قبل ساعتين.'),('Estudio español desde enero.','أدرس الإسبانية منذ يناير.'),('¿Cuánto tiempo hace que vives aquí?','منذ متى تسكن هنا؟'),('Hace un año que trabajo aquí.','أعمل هنا منذ سنة.'),('No lo veo desde ayer.','لم أره منذ أمس.')],
 [('Vivo aquí ___ hace tres años.',['desde','por','en'],0,'Vivo aquí desde hace tres años.'),
  ('Llegué ___ dos horas.',['desde','hace','en'],1,'Llegué hace dos horas.'),
  ('Estudio español ___ enero.',['desde','hace','por'],0,'Estudio español desde enero.'),
  ('No lo veo ___ ayer.',['desde','hace','en'],0,'No lo veo desde ayer.'),
  ('¿Cuánto tiempo ___ que vives aquí?',['hace','desde','hacer'],0,'¿Cuánto tiempo hace que vives aquí?')])

topic('a2-exclamativos','Frases exclamativas','جمل التعجّب',
 [('Para exclamar usamos qué + adjetivo o nombre: ¡Qué bonito! ¡Qué pena! Con un nombre y un adjetivo usamos tan o más: ¡Qué día tan bonito!','للتعجّب نستعمل qué مع صفة أو اسم، ومع اسم وصفة معًا نضيف tan أو más.'),
  ('Cuánto y cómo se usan con verbos y nombres: ¡Cómo llueve! ¡Cuánta gente! Las exclamaciones llevan signos de apertura y cierre.','وتُستعمل cuánto وcómo مع الأفعال والأسماء، وتُكتب علامتا التعجّب في أول الجملة وآخرها.')],
 {'nohl':1,'head':['','estructura','ejemplo'],'rows':[['qué + adjetivo','¡Qué…!','¡Qué bonito!'],['qué + nombre','¡Qué…!','¡Qué pena!'],['cuánto + nombre','¡Cuánto…!','¡Cuánta gente!'],['cómo + verbo','¡Cómo…!','¡Cómo llueve!']]},
 [('¡Qué bonito!','ما أجمل هذا!'),('¡Qué día tan bonito!','يا له من يوم جميل!'),('¡Qué pena!','يا للأسف!'),('¡Cuánta gente!','كم من الناس!'),('¡Cómo llueve!','كم تمطر!'),('¡Qué rico está!','ما ألذّه!')],
 [('¡___ bonito!',['Qué','Cómo','Cuánta'],0,'¡Qué bonito!'),
  ('¡___ gente!',['Cuánta','Cuánto','Qué'],0,'¡Cuánta gente!'),
  ('¡___ llueve!',['Cómo','Qué','Cuánta'],0,'¡Cómo llueve!'),
  ('¡Qué día ___ bonito!',['tan','mucho','muy'],0,'¡Qué día tan bonito!'),
  ('¡___ pena!',['Qué','Cómo','Cuánto'],0,'¡Qué pena!')])

topic('a2-adverbios-mente','Adverbios en -mente','الظروف المنتهية بـ -mente',
 [('Muchos adverbios se forman con el adjetivo en femenino más -mente: lento es lentamente, claro es claramente, rápido es rápidamente.','تُشتق ظروف كثيرة من الصفة بصيغة المؤنث مع إضافة -mente.'),
  ('Si el adjetivo termina en consonante o en -e, solo añadimos -mente: fácil es fácilmente, normal es normalmente.','وإذا انتهت الصفة بحرف ساكن أو بحرف e أضفنا -mente مباشرة. وتبقى علامة التشديد إن كانت في الصفة.')],
 {'nohl':1,'head':['','adjetivo','adverbio'],'rows':[['-o','lento','lentamente'],['-o','claro','claramente'],['consonante','fácil','fácilmente'],['consonante','normal','normalmente'],['-e','tranquilo','tranquilamente']]},
 [('Habla lentamente, por favor.','تكلّم ببطء من فضلك.'),('Ella conduce rápidamente.','هي تقود بسرعة.'),('Normalmente cenamos a las nueve.','عادةً نتعشّى في التاسعة.'),('Lo entiendo fácilmente.','أفهمه بسهولة.'),('Explícalo claramente.','اشرحه بوضوح.'),('Vivo tranquilamente.','أعيش بهدوء.')],
 [('Habla ___, por favor. (lento)',['lentamente','lentamenta','lenta'],0,'Habla lentamente, por favor.'),
  ('Ella conduce ___. (rápido)',['rápidamente','rápida','rápidomente'],0,'Ella conduce rápidamente.'),
  ('___ cenamos a las nueve. (normal)',['Normalmente','Normalmento','Normales'],0,'Normalmente cenamos a las nueve.'),
  ('Lo entiendo ___. (fácil)',['fácilmente','facilmente','fácilmento'],0,'Lo entiendo fácilmente.'),
  ('Hablo ___ con mi madre. (frecuente)',['frecuente','frecuentemente','frecuentamente'],1,'Hablo frecuentemente con mi madre.')])

topic('b1-temporales','Oraciones temporales','الجمل الزمنية',
 [('Con cuando, antes de que, después de que, en cuanto y hasta que usamos indicativo para hechos habituales o pasados, y subjuntivo para el futuro: Cuando llego, ceno. Cuando llegue, cenaré.','مع cuando وen cuanto وhasta que نستعمل المضارع المعتاد للعادة والماضي، والمضارع المنصوب للمستقبل.'),
  ('Antes de que siempre lleva subjuntivo: Antes de que salgas, llámame. Si el sujeto es el mismo, usamos antes de + infinitivo.','أما antes de que فتأتي دائمًا مع المضارع المنصوب، وإذا اتحد الفاعل نستعمل antes de مع المصدر.')],
 {'nohl':1,'head':['','habitual','futuro'],'rows':[['cuando','Cuando llego, ceno.','Cuando llegue, cenaré.'],['en cuanto','En cuanto termino, salgo.','En cuanto termine, saldré.'],['hasta que','Espero hasta que llega.','Esperaré hasta que llegue.']]},
 [('Cuando llego a casa, ceno.','عندما أصل إلى البيت أتعشّى.'),('Cuando llegue a casa, cenaré.','عندما أصل إلى البيت سأتعشّى.'),('Antes de que salgas, llámame.','قبل أن تخرج اتصل بي.'),('En cuanto termine, te llamo.','حالما أنتهي أتصل بك.'),('Espera hasta que vuelva.','انتظر حتى أعود.'),('Mientras estudio, escucho música.','بينما أدرس أستمع إلى الموسيقى.')],
 [('Cuando ___ a casa, te llamaré. (llegar)',['llego','llegue','llegué'],1,'Cuando llegue a casa, te llamaré.'),
  ('Antes de que ___, cierra la puerta. (salir)',['sales','salgas','saldrás'],1,'Antes de que salgas, cierra la puerta.'),
  ('Voy a esperar hasta que ___ mi madre.',['llega','llegue','llegó'],1,'Voy a esperar hasta que llegue mi madre.'),
  ('Cada vez que ___ a Madrid, visito el museo.',['voy','vaya','iré'],0,'Cada vez que voy a Madrid, visito el museo.'),
  ('En cuanto ___ el trabajo, descansaré.',['termino','termine','terminé'],1,'En cuanto termine el trabajo, descansaré.')])

topic('b1-causales-finales','Causa y finalidad','السبب والغاية',
 [('Para dar la causa usamos porque, como y ya que. Como va al principio de la frase: Como llovía, nos quedamos. Porque va después: Nos quedamos porque llovía.','للتعبير عن السبب نستعمل porque وcomo وya que. وتأتي como في أول الجملة، وporque في وسطها.'),
  ('Para la finalidad usamos para + infinitivo si el sujeto es el mismo, y para que + subjuntivo si cambia: Estudio para aprender. Abro la ventana para que entre aire.','وللغاية نستعمل para مع المصدر إن اتحد الفاعل، وpara que مع المضارع المنصوب إن اختلف.')],
 {'nohl':1,'head':['','conector','ejemplo'],'rows':[['causa','porque','No salí porque estaba cansado.'],['causa','como','Como llovía, nos quedamos.'],['finalidad','para + infinitivo','Estudio para aprender.'],['finalidad','para que + subjuntivo','Abro para que entre aire.']]},
 [('Como llovía, nos quedamos en casa.','لأنها كانت تمطر بقينا في البيت.'),('No salí porque estaba cansado.','لم أخرج لأنني كنت متعبًا.'),('Estudio para aprender.','أدرس لكي أتعلم.'),('Abro la ventana para que entre aire.','أفتح النافذة ليدخل الهواء.'),('Te lo explico para que lo entiendas mejor.','أشرحه لك لتفهمه أفضل.'),('Trabaja mucho para ganar dinero.','يعمل كثيرًا ليكسب المال.')],
 [('___ llovía, nos quedamos en casa.',['Como','Porque','Para'],0,'Como llovía, nos quedamos en casa.'),
  ('No salí ___ estaba cansado.',['porque','para que','como'],0,'No salí porque estaba cansado.'),
  ('Abro la ventana para que ___ aire.',['entra','entre','entró'],1,'Abro la ventana para que entre aire.'),
  ('Estudio ___ aprender.',['para','para que','porque'],0,'Estudio para aprender.'),
  ('Te lo explico para que lo ___.',['entiendes','entiendas','entendiste'],1,'Te lo explico para que lo entiendas.')])

topic('b1-se-impersonal','Se impersonal y pasiva refleja','se غير الشخصية والمبني للمجهول',
 [('Con se + verbo en tercera persona hablamos en general, sin decir quién actúa: Se habla español aquí. En España se cena tarde.','نستعمل se مع الفعل في الغائب للكلام العام دون ذكر الفاعل.'),
  ('Si el nombre es plural, el verbo va en plural: Se venden casas. Se necesita camarero.','وإذا كان الاسم جمعًا جاء الفعل بالجمع: se venden casas، وبالمفرد مع المفرد: se necesita camarero.')],
 {'nohl':1,'head':['','singular','plural'],'rows':[['vender','Se vende una casa.','Se venden casas.'],['hablar','Se habla español.','Se hablan dos idiomas.'],['necesitar','Se necesita camarero.','Se necesitan camareros.']]},
 [('Aquí se habla español.','هنا تُتكلَّم الإسبانية.'),('Se venden casas.','تُباع بيوت.'),('En España se cena tarde.','في إسبانيا يتعشّون متأخرين.'),('No se puede fumar aquí.','لا يجوز التدخين هنا.'),('Se necesita camarero.','مطلوب نادل.'),('Se dice que mañana lloverá.','يُقال إنها ستمطر غدًا.')],
 [('Aquí ___ español.',['se habla','se hablan','habla'],0,'Aquí se habla español.'),
  ('Se ___ casas.',['vende','venden','vendo'],1,'Se venden casas.'),
  ('En España ___ cena tarde.',['se','le','lo'],0,'En España se cena tarde.'),
  ('No se ___ fumar aquí.',['puede','pueden','puedo'],0,'No se puede fumar aquí.'),
  ('Se ___ camareros.',['necesita','necesitan','necesito'],1,'Se necesitan camareros.')])

topic('b1-verbos-preposicion','Verbos con preposición','أفعال مع حروف الجر',
 [('Algunos verbos siempre llevan una preposición: pensar en, soñar con, depender de, acordarse de, insistir en, casarse con.','بعض الأفعال تلزمها حروف جر معيّنة: pensar en وsoñar con وdepender de وacordarse de وinsistir en وcasarse con.'),
  ('Después de la preposición usamos un nombre, un pronombre o un infinitivo: Sueño con viajar. Pienso en ti.','وبعد حرف الجر يأتي اسم أو ضمير أو مصدر.')],
 {'nohl':1,'head':['','verbo + prep.','ejemplo'],'rows':[['en','pensar en','Pienso en ti.'],['con','soñar con','Sueño con viajar.'],['de','depender de','Depende de ti.'],['de','acordarse de','Me acuerdo de ti.']]},
 [('Pienso en ti.','أفكّر فيك.'),('Sueño con viajar.','أحلم بالسفر.'),('Insiste en pagar.','يصرّ على الدفع.'),('Me acuerdo de ti.','أتذكّرك.'),('Depende de ti.','الأمر يعتمد عليك.'),('Se casó con una médica.','تزوّج من طبيبة.')],
 [('Pienso ___ ti.',['en','de','con'],0,'Pienso en ti.'),
  ('Sueño ___ viajar.',['con','de','en'],0,'Sueño con viajar.'),
  ('Depende ___ ti.',['de','en','con'],0,'Depende de ti.'),
  ('Insiste ___ pagar.',['de','en','a'],1,'Insiste en pagar.'),
  ('Me acuerdo ___ ti.',['de','en','con'],0,'Me acuerdo de ti.')])

topic('b2-consecutivas','Oraciones consecutivas','جمل النتيجة',
 [('Para expresar una consecuencia usamos así que, por eso, de modo que y tan o tanto… que. Con indicativo: Hacía frío, así que me puse el abrigo.','للتعبير عن النتيجة نستعمل así que وde modo que وtan أو tanto مع que، ومع المضارع المعتاد.'),
  ('Tan va con adjetivos y adverbios, y tanto con verbos: Estaba tan cansado que se durmió. De ahí que lleva subjuntivo: Llovió mucho; de ahí que cancelaran el partido.','tan مع الصفات والظروف وtanto مع الأفعال. أما de ahí que فتأتي مع المضارع المنصوب.')],
 {'nohl':1,'head':['','conector','modo'],'rows':[['así que','Hacía frío, así que me abrigué.','indicativo'],['tan… que','Estaba tan cansado que se durmió.','indicativo'],['de ahí que','Llovió; de ahí que cancelaran.','subjuntivo']]},
 [('Hacía frío, así que me puse el abrigo.','كان الجو باردًا، لذلك لبست المعطف.'),('Estaba tan cansado que se durmió.','كان متعبًا جدًا حتى نام.'),('Habla tan rápido que nadie lo entiende.','يتكلم بسرعة حتى لا يفهمه أحد.'),('Se levantó tarde, de modo que perdió el tren.','استيقظ متأخرًا فضاع منه القطار.'),('Llovió mucho; de ahí que cancelaran el partido.','أمطرت كثيرًا؛ ومن ثَمّ أُلغيت المباراة.'),('Come tanto que está enfermo.','يأكل كثيرًا حتى مرض.')],
 [('Hacía frío, ___ me puse el abrigo.',['así que','aunque','porque'],0,'Hacía frío, así que me puse el abrigo.'),
  ('Estaba ___ cansado que se durmió.',['tan','tanto','muy'],0,'Estaba tan cansado que se durmió.'),
  ('Come ___ que está enfermo.',['tan','tanto','tantos'],1,'Come tanto que está enfermo.'),
  ('Llovió mucho; de ahí que ___ el partido.',['cancelaron','cancelaran','cancelan'],1,'Llovió mucho; de ahí que cancelaran el partido.'),
  ('Se levantó tarde, de ___ que perdió el tren.',['modo','forma','cosa'],0,'Se levantó tarde, de modo que perdió el tren.')])

topic('b2-comparativas-avanzadas','Comparaciones avanzadas','المقارنات المتقدمة',
 [('Para comparar con una oración usamos más o menos + de lo que: Es más fácil de lo que pensaba. Habla menos de lo que crees.','للمقارنة مع جملة كاملة نستعمل más أو menos مع de lo que.'),
  ('Cuanto más… más… expresa un cambio paralelo: Cuanto más estudio, más aprendo. Cada vez más expresa aumento: Cada vez hace más frío.','وcuanto más… más… تعبّر عن تغيّر متوازٍ، وcada vez más تعبّر عن زيادة مستمرة.')],
 {'nohl':1,'head':['','estructura','ejemplo'],'rows':[['más… de lo que','más fácil de lo que pensaba','Es más fácil de lo que pensaba.'],['cuanto más… más','Cuanto más estudio, más aprendo.','paralelo'],['cada vez más','Cada vez hace más frío.','aumento'],['tanto… como','Tiene tantos libros como yo.','igualdad']]},
 [('Es más fácil de lo que pensaba.','إنه أسهل مما كنت أظن.'),('Cuanto más estudio, más aprendo.','كلما درست أكثر تعلّمت أكثر.'),('Cada vez hace más frío.','يزداد البرد يومًا بعد يوم.'),('Tiene tantos libros como yo.','عنده كتب بقدر ما عندي.'),('Habla menos de lo que crees.','يتكلم أقل مما تظن.'),('Cuanto antes, mejor.','كلما كان أبكر كان أفضل.')],
 [('Es más fácil ___ lo que pensaba.',['de','que','como'],0,'Es más fácil de lo que pensaba.'),
  ('Cuanto más estudio, ___ aprendo.',['más','tan','menos'],0,'Cuanto más estudio, más aprendo.'),
  ('Cada ___ hace más frío.',['vez','día','hora'],0,'Cada vez hace más frío.'),
  ('Tiene tantos libros ___ yo.',['como','que','de'],0,'Tiene tantos libros como yo.'),
  ('Habla menos de lo que ___.',['crees','creer','creo'],0,'Habla menos de lo que crees.')])
