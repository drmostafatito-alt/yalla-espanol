# -*- coding: utf-8 -*-
# Original A1 grammar content. Spanish primary; Arabic (fusha) optional.
T=[]
def topic(id,es,ar,rule,table,ex,exe,tip=None):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe,tip=tip))

topic('a1-presente','Presente de indicativo: verbos regulares','المضارع المرفوع: الأفعال المنتظمة',
 [('Los verbos regulares terminan en -ar, -er o -ir. Quitamos esa terminación y añadimos la de cada persona.','الأفعال المنتظمة تنتهي بـ -ar أو -er أو -ir. نحذف هذه النهاية ونضيف نهاية كل ضمير.'),
  ('Usamos el presente para hablar de hábitos, de hechos y de lo que pasa ahora.','نستخدم المضارع للعادات والحقائق وما يحدث الآن.')],
 {'head':['','hablar','comer','vivir'],'rows':[['yo','hablo','como','vivo'],['tú','hablas','comes','vives'],['él / ella / usted','habla','come','vive'],['nosotros','hablamos','comemos','vivimos'],['vosotros','habláis','coméis','vivís'],['ellos / ustedes','hablan','comen','viven']]},
 [('Yo hablo español todos los días.','أتحدث الإسبانية كل يوم.'),('Ana come fruta por la mañana.','تأكل آنا الفاكهة في الصباح.'),('Vivimos en una ciudad grande.','نعيش في مدينة كبيرة.'),('¿Tú trabajas aquí?','هل تعمل هنا؟'),('Mis padres beben té con leche.','يشرب والداي الشاي بالحليب.'),('Escribo un mensaje a mi amigo.','أكتب رسالة إلى صديقي.')],
 [('Yo ___ en una oficina.',['trabajo','trabajas','trabaja'],0,'Yo trabajo en una oficina.'),
  ('Tú ___ pan con queso.',['como','comes','come'],1,'Tú comes pan con queso.'),
  ('Nosotros ___ en Madrid.',['vivo','vive','vivimos'],2,'Nosotros vivimos en Madrid.'),
  ('Ellos ___ mucho café.',['bebe','beben','bebes'],1,'Ellos beben mucho café.'),
  ('Ella ___ una carta.',['escribe','escribes','escribo'],0,'Ella escribe una carta.'),
  ('Vosotros ___ español en clase.',['habláis','hablan','hablamos'],0,'Vosotros habláis español en clase.')])

topic('a1-ser-estar','Ser, estar y hay','ser وestar وhay',
 [('Ser expresa identidad, origen, profesión y características. Estar expresa lugar y estado del momento.','يعبّر ser عن الهوية والأصل والمهنة والصفات الثابتة، ويعبّر estar عن المكان والحالة المؤقتة.'),
  ('Hay indica que algo existe en un lugar. No cambia con el plural: hay un libro, hay dos libros.','تدل hay على وجود شيء في مكان ما، ولا تتغيّر مع الجمع: hay un libro، hay dos libros.')],
 {'head':['','ser','estar'],'rows':[['yo','soy','estoy'],['tú','eres','estás'],['él / ella / usted','es','está'],['nosotros','somos','estamos'],['vosotros','sois','estáis'],['ellos / ustedes','son','están']]},
 [('Soy estudiante y soy de Egipto.','أنا طالب وأنا من مصر.'),('Mi hermana es muy simpática.','أختي لطيفة جدًا.'),('El café está caliente.','القهوة ساخنة.'),('Estamos en casa hoy.','نحن في البيت اليوم.'),('Hay una farmacia cerca de aquí.','توجد صيدلية قريبة من هنا.'),('Hay tres sillas en la cocina.','توجد ثلاثة كراسي في المطبخ.')],
 [('Yo ___ médico.',['soy','estoy','hay'],0,'Yo soy médico.'),
  ('Hoy ___ cansado.',['soy','estoy','hay'],1,'Hoy estoy cansado.'),
  ('___ un parque en mi barrio.',['Es','Está','Hay'],2,'Hay un parque en mi barrio.'),
  ('Ellos ___ de México.',['son','están','hay'],0,'Ellos son de México.'),
  ('El libro ___ en la mesa.',['es','está','hay'],1,'El libro está en la mesa.'),
  ('Nosotros ___ amigos.',['somos','estamos','hay'],0,'Nosotros somos amigos.')])

topic('a1-genero-numero','Género y número','المذكر والمؤنث والجمع',
 [('Los sustantivos son masculinos o femeninos. Muchos masculinos terminan en -o y muchos femeninos en -a.','الأسماء إما مذكرة أو مؤنثة. كثير من المذكر ينتهي بـ -o وكثير من المؤنث ينتهي بـ -a.'),
  ('Para el plural añadimos -s si termina en vocal y -es si termina en consonante. El adjetivo concuerda con el sustantivo.','للجمع نضيف -s إذا انتهت الكلمة بحرف علة و -es إذا انتهت بحرف ساكن. ويتطابق الصفة مع الاسم.')],
 {'head':['singular','plural'],'rows':[['el niño','los niños'],['la casa','las casas'],['el papel','los papeles'],['la ciudad','las ciudades'],['un coche rojo','unos coches rojos'],['una mesa blanca','unas mesas blancas']]},
 [('El niño es alto.','الولد طويل.'),('La casa es blanca.','البيت أبيض.'),('Los libros son nuevos.','الكتب جديدة.'),('Las ciudades son grandes.','المدن كبيرة.'),('Tengo dos hermanas simpáticas.','لدي أختان لطيفتان.'),('Compro tres papeles azules.','أشتري ثلاث أوراق زرقاء.')],
 [('La casa es ___.',['blanco','blanca','blancas'],1,'La casa es blanca.'),
  ('Los coches son ___.',['rojo','roja','rojos'],2,'Los coches son rojos.'),
  ('Plural de «ciudad»: las ___.',['ciudads','ciudades','ciudad'],1,'Las ciudades son bonitas.'),
  ('Plural de «papel»: los ___.',['papels','papeles','papeleses'],1,'Los papeles están en la mesa.'),
  ('Mi hermana es ___.',['simpático','simpática','simpáticos'],1,'Mi hermana es simpática.'),
  ('Las mesas son ___.',['nuevas','nuevos','nueva'],0,'Las mesas son nuevas.')])

topic('a1-articulos','Artículos definidos e indefinidos','أدوات التعريف والتنكير',
 [('Los artículos definidos son el, la, los, las. Los usamos cuando hablamos de algo conocido.','أدوات التعريف هي el وla وlos وlas، ونستخدمها حين نتحدث عن شيء معروف.'),
  ('Los artículos indefinidos son un, una, unos, unas. Los usamos para algo nuevo o no específico.','أدوات التنكير هي un وuna وunos وunas، ونستخدمها لشيء جديد أو غير محدد.')],
 {'head':['','masculino','femenino'],'rows':[['definido singular','el','la'],['definido plural','los','las'],['indefinido singular','un','una'],['indefinido plural','unos','unas']]},
 [('El libro está en la mesa.','الكتاب على الطاولة.'),('Tengo un perro y una gata.','لدي كلب وقطة.'),('Las flores son rojas.','الزهور حمراء.'),('Necesito unas gafas nuevas.','أحتاج إلى نظارات جديدة.'),('Los niños juegan en el parque.','الأطفال يلعبون في الحديقة.'),('Quiero una manzana.','أريد تفاحة.')],
 [('___ casa es grande.',['El','La','Los'],1,'La casa es grande.'),
  ('Tengo ___ amigo en Madrid.',['un','una','las'],0,'Tengo un amigo en Madrid.'),
  ('___ niños comen pan.',['Los','Las','Un'],0,'Los niños comen pan.'),
  ('Quiero ___ café, por favor.',['un','una','unas'],0,'Quiero un café, por favor.'),
  ('___ mesas son nuevas.',['Los','Las','El'],1,'Las mesas son nuevas.'),
  ('Compro ___ zapatos.',['unos','unas','una'],0,'Compro unos zapatos.')])

topic('a1-pronombres','Pronombres personales sujeto','ضمائر الفاعل',
 [('Los pronombres sujeto son yo, tú, él, ella, usted, nosotros, vosotros, ellos y ustedes.','ضمائر الفاعل هي yo وtú وél وella وusted وnosotros وvosotros وellos وustedes.'),
  ('En español muchas veces no los usamos, porque la terminación del verbo ya indica la persona. Los usamos para aclarar o para dar énfasis.','في الإسبانية كثيرًا ما نحذف الضمير لأن نهاية الفعل تدل على الشخص. ونستخدمه للتوضيح أو للتأكيد.')],
 {'head':['persona','pronombre'],'rows':[['1.ª singular','yo'],['2.ª singular','tú'],['3.ª singular','él / ella / usted'],['1.ª plural','nosotros / nosotras'],['2.ª plural','vosotros / vosotras'],['3.ª plural','ellos / ellas / ustedes']]},
 [('Yo soy Karim y tú eres Laura.','أنا كريم وأنت لورا.'),('Ella trabaja en un banco.','هي تعمل في بنك.'),('Nosotros estudiamos juntos.','نحن ندرس معًا.'),('Hablo inglés, pero ella habla francés.','أتحدث الإنجليزية لكنها تتحدث الفرنسية.'),('Usted es el director, ¿verdad?','أنت المدير، أليس كذلك؟'),('Ellos viven cerca de nosotros.','هم يسكنون قرب منا.')],
 [('___ soy de El Cairo.',['Yo','Tú','Ella'],0,'Yo soy de El Cairo.'),
  ('___ eres muy amable.',['Yo','Tú','Nosotros'],1,'Tú eres muy amable.'),
  ('___ estudiamos español.',['Ellos','Usted','Nosotros'],2,'Nosotros estudiamos español.'),
  ('Ana es mi amiga. ___ vive aquí.',['Él','Ella','Yo'],1,'Ana es mi amiga. Ella vive aquí.'),
  ('Con una persona mayor decimos ___.',['tú','usted','yo'],1,'Con una persona mayor decimos usted.'),
  ('Carlos y Pedro son amigos. ___ juegan al fútbol.',['Ellos','Ellas','Nosotros'],0,'Carlos y Pedro son amigos. Ellos juegan al fútbol.')])

topic('a1-gustar','El verbo gustar','الفعل gustar',
 [('Con gustar, lo que nos gusta es el sujeto. Por eso el verbo concuerda con la cosa: gusta (una cosa) y gustan (varias cosas).','مع gustar يكون الشيء المحبوب هو الفاعل، لذلك يتطابق الفعل معه: gusta للمفرد وgustan للجمع.'),
  ('Antes del verbo ponemos me, te, le, nos, os o les, según quién siente el gusto.','قبل الفعل نضع me أو te أو le أو nos أو os أو les بحسب من يشعر بالإعجاب.')],
 {'head':['a quién','+ una cosa','+ varias cosas'],'rows':[['me','me gusta el té','me gustan los libros'],['te','te gusta la playa','te gustan los gatos'],['le','le gusta el cine','le gustan las flores'],['nos','nos gusta cantar','nos gustan las fiestas'],['os','os gusta el fútbol','os gustan los coches'],['les','les gusta la música','les gustan los viajes']]},
 [('Me gusta el café con leche.','تعجبني القهوة بالحليب.'),('No me gustan los lunes.','لا تعجبني أيام الاثنين.'),('¿Te gusta bailar?','هل تحب الرقص؟'),('A mi madre le gusta la cocina.','أمي تحب الطبخ.'),('Nos gustan las películas de aventuras.','نحب أفلام المغامرات.'),('A ellos les gusta viajar en tren.','هم يحبون السفر بالقطار.')],
 [('Me ___ el chocolate.',['gusta','gustan','gusto'],0,'Me gusta el chocolate.'),
  ('Me ___ los libros.',['gusta','gustan','gustas'],1,'Me gustan los libros.'),
  ('A ti ___ gusta el cine.',['me','te','le'],1,'A ti te gusta el cine.'),
  ('A mi hermano ___ gustan los coches.',['le','les','nos'],0,'A mi hermano le gustan los coches.'),
  ('A nosotros ___ gusta cantar.',['nos','os','les'],0,'A nosotros nos gusta cantar.'),
  ('A mis padres ___ gusta el campo.',['le','les','me'],1,'A mis padres les gusta el campo.')])

topic('a1-reflexivos','Verbos reflexivos','الأفعال الانعكاسية',
 [('Un verbo reflexivo lleva me, te, se, nos, os o se. La acción vuelve al mismo sujeto: yo me levanto.','الفعل الانعكاسي يأخذ me أو te أو se أو nos أو os، ويعود الفعل على الفاعل نفسه: yo me levanto.'),
  ('El pronombre va antes del verbo conjugado. Muchos verbos de la rutina diaria son reflexivos.','يأتي الضمير قبل الفعل المصرَّف. وكثير من أفعال الروتين اليومي انعكاسية.')],
 {'head':['','levantarse','ducharse'],'rows':[['yo','me levanto','me ducho'],['tú','te levantas','te duchas'],['él / ella / usted','se levanta','se ducha'],['nosotros','nos levantamos','nos duchamos'],['vosotros','os levantáis','os ducháis'],['ellos / ustedes','se levantan','se duchan']]},
 [('Me levanto a las siete.','أستيقظ في الساعة السابعة.'),('Te duchas por la mañana.','تستحم في الصباح.'),('Mi padre se afeita todos los días.','أبي يحلق كل يوم.'),('Nos acostamos tarde los sábados.','ننام متأخرين أيام السبت.'),('Los niños se lavan las manos.','الأطفال يغسلون أيديهم.'),('Ella se llama Marta.','اسمها مارتا.')],
 [('Yo ___ levanto temprano.',['me','te','se'],0,'Yo me levanto temprano.'),
  ('Tú ___ duchas por la noche.',['me','te','se'],1,'Tú te duchas por la noche.'),
  ('Ella ___ llama Sara.',['me','te','se'],2,'Ella se llama Sara.'),
  ('Nosotros ___ acostamos a las once.',['nos','se','os'],0,'Nosotros nos acostamos a las once.'),
  ('Mis hijos ___ lavan los dientes.',['nos','se','te'],1,'Mis hijos se lavan los dientes.'),
  ('Yo me ___ a las seis.',['levanto','levantas','levanta'],0,'Yo me levanto a las seis.')])

topic('a1-imperativo','Imperativo afirmativo','فعل الأمر المثبت',
 [('Para dar una orden o un consejo a una persona con tú, usamos la forma de él/ella del presente: habla, come, escribe.','لإعطاء أمر أو نصيحة لشخص نخاطبه بـ tú نستخدم صيغة él/ella من المضارع: habla وcome وescribe.'),
  ('Con usted cambiamos la vocal: hable, coma, escriba. Los pronombres van pegados al verbo: siéntate.','مع usted نغيّر حرف العلة: hable وcoma وescriba. وتلتصق الضمائر بالفعل: siéntate.')],
 {'head':['infinitivo','tú','usted'],'rows':[['hablar','habla','hable'],['comer','come','coma'],['escribir','escribe','escriba'],['abrir','abre','abra'],['esperar','espera','espere'],['sentarse','siéntate','siéntese']]},
 [('Habla más despacio, por favor.','تحدّث ببطء أكثر من فضلك.'),('Come una fruta.','كُل فاكهة.'),('Abre la ventana.','افتح النافذة.'),('Espera un momento.','انتظر لحظة.'),('Escriba su nombre aquí, por favor.','اكتب اسمك هنا من فضلك.'),('Siéntate, estás cansado.','اجلس، أنت متعب.')],
 [('___ la puerta, por favor. (tú, abrir)',['Abre','Abres','Abra'],0,'Abre la puerta, por favor.'),
  ('___ más despacio. (tú, hablar)',['Habla','Hablas','Hable'],0,'Habla más despacio.'),
  ('___ el pan con queso, por favor. (tú, comer)',['Comes','Come','Coma'],1,'Come el pan con queso, por favor.'),
  ('___ aquí, señor. (usted, escribir)',['Escribe','Escribes','Escriba'],2,'Escriba aquí, señor.'),
  ('___ un momento. (tú, esperar)',['Espera','Esperas','Esperar'],0,'Espera un momento.'),
  ('___ , por favor. (tú, sentarse)',['Siéntate','Te sientas','Siéntese'],0,'Siéntate, por favor.')])
