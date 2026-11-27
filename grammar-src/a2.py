# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))

topic('a2-perfecto','Pretérito perfecto','الماضي القريب (pretérito perfecto)',
 [('Se forma con el presente de haber y el participio: he hablado, has comido, ha vivido.','يتكوّن من مضارع haber مع اسم المفعول: he hablado وhas comido وha vivido.'),
  ('Lo usamos para experiencias y para acciones en un tiempo que todavía no ha terminado: hoy, esta semana, este año. Señales útiles: ya, todavía no, nunca, alguna vez.','نستخدمه للتجارب وللأحداث في زمن لم ينتهِ بعد مثل: hoy وesta semana وeste año. ومن الكلمات الدالة: ya وtodavía no وnunca وalguna vez.')],
 {'head':['','haber','participio'],'rows':[['yo','he','hablado (-ar → -ado)'],['tú','has','comido (-er → -ido)'],['él / ella / usted','ha','vivido (-ir → -ido)'],['nosotros','hemos','hecho (hacer)'],['vosotros','habéis','visto (ver)'],['ellos / ustedes','han','escrito (escribir)']]},
 [('Hoy he trabajado mucho.','اليوم عملت كثيرًا.'),('¿Has estado alguna vez en España?','هل زرت إسبانيا من قبل؟'),('Mi hermana ha comido ya.','أختي أكلت بالفعل.'),('Todavía no hemos visto esa película.','لم نشاهد ذلك الفيلم بعد.'),('Esta semana han escrito tres correos.','هذا الأسبوع كتبوا ثلاث رسائل.'),('Nunca he probado el pulpo.','لم أذق الأخطبوط قط.')],
 [('Yo ___ comido ya.',['he','has','ha'],0,'Yo he comido ya.'),
  ('Tú ___ viajado mucho este año.',['he','has','han'],1,'Tú has viajado mucho este año.'),
  ('Nosotros ___ visto la película.',['hemos','han','habéis'],0,'Nosotros hemos visto la película.'),
  ('Ella ha ___ una carta. (escribir)',['escribido','escrito','escribe'],1,'Ella ha escrito una carta.'),
  ('Hoy he ___ el desayuno. (hacer)',['hacido','hecho','hace'],1,'Hoy he hecho el desayuno.'),
  ('Ellos ___ llegado tarde hoy.',['ha','han','hemos'],1,'Ellos han llegado tarde hoy.')])

topic('a2-indefinido','Pretérito indefinido','الماضي المنتهي (pretérito indefinido)',
 [('Lo usamos para acciones terminadas en un momento del pasado: ayer, el año pasado, en 2020, hace dos días.','نستخدمه للأحداث التي انتهت في لحظة محددة من الماضي: ayer وel año pasado وen 2020 وhace dos días.'),
  ('Los verbos -er e -ir comparten las mismas terminaciones. Ser e ir tienen la misma forma: fui, fuiste, fue.','أفعال -er و-ir لها النهايات نفسها. وللفعلين ser وir الصيغة نفسها: fui وfuiste وfue.')],
 {'head':['','hablar','comer','ser / ir'],'rows':[['yo','hablé','comí','fui'],['tú','hablaste','comiste','fuiste'],['él / ella / usted','habló','comió','fue'],['nosotros','hablamos','comimos','fuimos'],['vosotros','hablasteis','comisteis','fuisteis'],['ellos / ustedes','hablaron','comieron','fueron']]},
 [('Ayer hablé con mi jefe.','أمس تحدثت مع مديري.'),('El sábado comimos en un restaurante.','يوم السبت أكلنا في مطعم.'),('Mi padre llegó a las ocho.','وصل أبي في الثامنة.'),('El año pasado fuimos a Sevilla.','في العام الماضي ذهبنا إلى إشبيلية.'),('¿Qué compraste en el mercado?','ماذا اشتريت من السوق؟'),('Ellos vivieron en París dos años.','عاشوا في باريس سنتين.')],
 [('Ayer yo ___ una película.',['vi','veo','veía'],0,'Ayer yo vi una película.'),
  ('El lunes ella ___ a su madre.',['llamó','llama','llamaba'],0,'El lunes ella llamó a su madre.'),
  ('Anoche nosotros ___ pizza.',['comimos','comemos','comíamos'],0,'Anoche nosotros comimos pizza.'),
  ('El verano pasado ellos ___ a la playa.',['fueron','van','iban'],0,'El verano pasado ellos fueron a la playa.'),
  ('Ayer tú ___ muy tarde.',['llegaste','llegas','llegabas'],0,'Ayer tú llegaste muy tarde.'),
  ('Hace dos días yo ___ un libro.',['compré','compro','compraba'],0,'Hace dos días yo compré un libro.')])

topic('a2-imperfecto','Pretérito imperfecto','الماضي المستمر (pretérito imperfecto)',
 [('Describe hábitos del pasado, situaciones y personas. No dice cuándo empezó ni terminó la acción.','يصف عادات الماضي والمواقف والأشخاص، ولا يحدد متى بدأ الفعل أو انتهى.'),
  ('Solo hay tres verbos irregulares: ser (era), ir (iba) y ver (veía). Señales: antes, de niño, siempre, todos los días.','لا توجد إلا ثلاثة أفعال شاذة: ser (era) وir (iba) وver (veía). ومن الكلمات الدالة: antes وde niño وsiempre وtodos los días.')],
 {'head':['','hablar','comer / vivir','ser'],'rows':[['yo','hablaba','comía','era'],['tú','hablabas','comías','eras'],['él / ella / usted','hablaba','comía','era'],['nosotros','hablábamos','comíamos','éramos'],['vosotros','hablabais','comíais','erais'],['ellos / ustedes','hablaban','comían','eran']]},
 [('De niño vivía en un pueblo pequeño.','حين كنت طفلًا كنت أعيش في قرية صغيرة.'),('Todos los días jugábamos en la calle.','كل يوم كنا نلعب في الشارع.'),('Mi abuela siempre cocinaba los domingos.','كانت جدتي تطبخ دائمًا أيام الأحد.'),('Antes era muy tímido.','كنت خجولًا جدًا من قبل.'),('Cuando era joven, iba al cine cada semana.','حين كنت شابًا كنت أذهب إلى السينما كل أسبوع.'),('Hacía frío y llovía.','كان الجو باردًا وكانت تمطر.')],
 [('De niño yo ___ mucho fútbol.',['jugaba','jugué','juego'],0,'De niño yo jugaba mucho fútbol.'),
  ('Antes nosotros ___ en el campo.',['vivíamos','vivimos','vivieron'],0,'Antes nosotros vivíamos en el campo.'),
  ('Cuando era pequeña, ella ___ muy tímida.',['era','fue','es'],0,'Cuando era pequeña, ella era muy tímida.'),
  ('Todos los veranos ellos ___ a la playa.',['iban','fueron','van'],0,'Todos los veranos ellos iban a la playa.'),
  ('Mi padre siempre ___ el periódico.',['leía','leyó','lee'],0,'Mi padre siempre leía el periódico.'),
  ('Yo ___ a mis abuelos cada domingo.',['veía','vi','veo'],0,'Yo veía a mis abuelos cada domingo.')])

topic('a2-gerundio','Estar + gerundio','الاستمرار: estar + gerundio',
 [('Para una acción que ocurre ahora, usamos estar y el gerundio: estoy hablando, estás comiendo, está escribiendo.','للتعبير عن فعل يحدث الآن نستخدم estar مع الجيرونديو: estoy hablando وestás comiendo وestá escribiendo.'),
  ('El gerundio termina en -ando (verbos -ar) o -iendo (verbos -er e -ir). Algunos cambian: leer → leyendo, dormir → durmiendo.','ينتهي الجيرونديو بـ -ando (أفعال -ar) أو -iendo (أفعال -er و-ir). وبعضها يتغير: leer → leyendo وdormir → durmiendo.')],
 {'head':['infinitivo','gerundio'],'rows':[['hablar','hablando'],['comer','comiendo'],['vivir','viviendo'],['leer','leyendo'],['dormir','durmiendo'],['decir','diciendo']]},
 [('Ahora estoy estudiando español.','الآن أنا أدرس الإسبانية.'),('¿Qué estás haciendo?','ماذا تفعل الآن؟'),('Mi madre está cocinando.','أمي تطبخ الآن.'),('Estamos esperando el autobús.','نحن ننتظر الحافلة.'),('Los niños están durmiendo.','الأطفال نائمون الآن.'),('Está lloviendo mucho.','تمطر كثيرًا.')],
 [('Yo estoy ___ la televisión. (ver)',['viendo','vendo','veyendo'],0,'Yo estoy viendo la televisión.'),
  ('Ella está ___ una carta. (escribir)',['escribiendo','escribando','escribido'],0,'Ella está escribiendo una carta.'),
  ('Nosotros estamos ___ café. (beber)',['bebiendo','bebando','bebemos'],0,'Nosotros estamos bebiendo café.'),
  ('Tú ___ comiendo muy rápido.',['estoy','estás','está'],1,'Tú estás comiendo muy rápido.'),
  ('Los niños ___ jugando en el parque.',['están','estamos','estás'],0,'Los niños están jugando en el parque.'),
  ('El bebé está ___ . (dormir)',['durmiendo','dormiendo','dormido'],0,'El bebé está durmiendo.')])

topic('a2-ir-a','Ir a + infinitivo','المستقبل القريب: ir a + مصدر',
 [('Para planes y futuro cercano usamos el presente de ir, la preposición a y un infinitivo: voy a comer, vas a salir.','للخطط والمستقبل القريب نستخدم مضارع ir مع حرف الجر a ثم المصدر: voy a comer وvas a salir.'),
  ('Se usa mucho con mañana, esta noche, el próximo mes y la semana que viene.','ويكثر استعماله مع mañana وesta noche وel próximo mes وla semana que viene.')],
 {'head':['','ir','+ a + infinitivo'],'rows':[['yo','voy','a viajar'],['tú','vas','a comer'],['él / ella / usted','va','a llamar'],['nosotros','vamos','a salir'],['vosotros','vais','a estudiar'],['ellos / ustedes','van','a vivir']]},
 [('Mañana voy a visitar a mi tía.','غدًا سأزور عمتي.'),('Esta noche vamos a cenar fuera.','الليلة سنتعشى في الخارج.'),('¿Vas a venir a la fiesta?','هل ستأتي إلى الحفلة؟'),('Mis amigos van a viajar en verano.','سيسافر أصدقائي في الصيف.'),('Voy a comprar pan.','سأشتري خبزًا.'),('La semana que viene va a llover.','الأسبوع القادم ستمطر.')],
 [('Mañana yo ___ a estudiar.',['voy','va','vamos'],0,'Mañana yo voy a estudiar.'),
  ('Esta noche tú ___ a cocinar.',['voy','vas','van'],1,'Esta noche tú vas a cocinar.'),
  ('Nosotros ___ a salir pronto.',['vamos','van','vais'],0,'Nosotros vamos a salir pronto.'),
  ('Ellos van ___ viajar en agosto.',['a','de','en'],0,'Ellos van a viajar en agosto.'),
  ('Ella va a ___ a su madre. (llamar)',['llama','llamar','llamó'],1,'Ella va a llamar a su madre.'),
  ('Vosotros ___ a comer con nosotros.',['vais','van','vamos'],0,'Vosotros vais a comer con nosotros.')])

topic('a2-futuro','Futuro simple','المستقبل البسيط',
 [('Para el futuro regular añadimos las terminaciones al infinitivo completo: hablaré, comerás, vivirá.','في المستقبل المنتظم نضيف النهايات إلى المصدر كاملًا: hablaré وcomerás وvivirá.'),
  ('Las terminaciones son las mismas para -ar, -er e -ir. Algunos verbos cambian la raíz: tener → tendré, hacer → haré, poder → podré, venir → vendré.','النهايات واحدة لأفعال -ar و-er و-ir. وبعض الأفعال يتغير جذرها: tener → tendré وhacer → haré وpoder → podré وvenir → vendré.')],
 {'head':['','hablar','tener'],'rows':[['yo','hablaré','tendré'],['tú','hablarás','tendrás'],['él / ella / usted','hablará','tendrá'],['nosotros','hablaremos','tendremos'],['vosotros','hablaréis','tendréis'],['ellos / ustedes','hablarán','tendrán']]},
 [('Mañana hablaré con el director.','غدًا سأتحدث مع المدير.'),('El próximo año viviremos en otra ciudad.','في العام القادم سنعيش في مدينة أخرى.'),('¿Vendrás a mi casa el sábado?','هل ستأتي إلى بيتي يوم السبت؟'),('Mi hermano tendrá un bebé en mayo.','سيرزق أخي بمولود في مايو.'),('Haré la tarea esta noche.','سأنجز الواجب الليلة.'),('Mañana hará calor.','غدًا سيكون الجو حارًا.')],
 [('Mañana yo ___ en casa.',['estaré','estoy','estuve'],0,'Mañana yo estaré en casa.'),
  ('El año próximo tú ___ veinte años.',['tendrás','tienes','tuviste'],0,'El año próximo tú tendrás veinte años.'),
  ('Nosotros ___ el examen en junio.',['haremos','hacemos','hicimos'],0,'Nosotros haremos el examen en junio.'),
  ('Ellos ___ a la fiesta mañana.',['vendrán','vienen','vinieron'],0,'Ellos vendrán a la fiesta mañana.'),
  ('Ella ___ muy contenta con el regalo.',['estará','está','estuvo'],0,'Ella estará muy contenta con el regalo.'),
  ('Yo ___ a mis abuelos el domingo.',['visitaré','visito','visité'],0,'Yo visitaré a mis abuelos el domingo.')])

topic('a2-comparativos','Comparativos y superlativos','المقارنة وصيغة التفضيل',
 [('Comparamos con más … que, menos … que y tan … como. Para cantidades: más de y menos de con números.','نقارن بـ más … que وmenos … que وtan … como. وللأعداد نستخدم más de وmenos de.'),
  ('Cuatro comparativos son irregulares: bueno → mejor, malo → peor, grande → mayor, pequeño → menor. El superlativo: el más alto, la menos cara.','أربع صيغ مقارنة شاذة: bueno → mejor وmalo → peor وgrande → mayor وpequeño → menor. وصيغة التفضيل: el más alto وla menos cara.')],
 {'head':['forma','ejemplo'],'rows':[['más … que','Pedro es más alto que Luis.'],['menos … que','Este libro es menos caro que ese.'],['tan … como','Ana es tan simpática como Eva.'],['mejor / peor','Mi coche es mejor que el tuyo.'],['el más …','Es el más rápido de la clase.']]},
 [('Mi hermano es más alto que yo.','أخي أطول مني.'),('Este café es menos caro que aquel.','هذه القهوة أرخص من تلك.'),('Ella es tan inteligente como su madre.','هي ذكية مثل أمها.'),('La comida de hoy es mejor que la de ayer.','طعام اليوم أفضل من طعام الأمس.'),('Madrid es la ciudad más grande de España.','مدريد هي أكبر مدينة في إسبانيا.'),('Tengo menos de diez euros.','معي أقل من عشرة يوروهات.')],
 [('Mi casa es ___ grande que la tuya.',['más','tan','muy'],0,'Mi casa es más grande que la tuya.'),
  ('Él es ___ simpático como su padre.',['tan','más','mejor'],0,'Él es tan simpático como su padre.'),
  ('Esta película es ___ que la otra. (bueno)',['más buena','mejor','buenísimo'],1,'Esta película es mejor que la otra.'),
  ('Este libro es ___ interesante que ese.',['menos','tan','mejor'],0,'Este libro es menos interesante que ese.'),
  ('Es la ___ cara de la tienda.',['más','mejor','tan'],0,'Es la más cara de la tienda.'),
  ('Tengo ___ de veinte años.',['más','muy','tan'],0,'Tengo más de veinte años.')])

topic('a2-por-para','Por y para','الفرق بين por وpara',
 [('Para expresa objetivo, destino, plazo y destinatario: un regalo para ti, salgo para Madrid, es para el lunes.','تعبّر para عن الهدف والوجهة والموعد النهائي والمستفيد: un regalo para ti وsalgo para Madrid وes para el lunes.'),
  ('Por expresa causa, medio, lugar de paso, duración y cambio: gracias por todo, hablo por teléfono, paseo por el parque, trabajo por la mañana.','تعبّر por عن السبب والوسيلة ومكان المرور والمدة والمقابل: gracias por todo وhablo por teléfono وpaseo por el parque وtrabajo por la mañana.')],
 {'head':['para','por'],'rows':[['objetivo: estudio para aprender','causa: lo hago por ti'],['destino: voy para casa','lugar de paso: paso por tu calle'],['plazo: para mañana','medio: por correo'],['destinatario: para mi madre','tiempo: por la tarde']]},
 [('Este regalo es para mi madre.','هذه الهدية لأمي.'),('Estudio español para trabajar en España.','أدرس الإسبانية لأعمل في إسبانيا.'),('Gracias por tu ayuda.','شكرًا على مساعدتك.'),('Hablamos por teléfono.','نتحدث عبر الهاتف.'),('Camino por el parque por la mañana.','أمشي في الحديقة في الصباح.'),('Necesito el informe para el viernes.','أحتاج إلى التقرير بحلول الجمعة.')],
 [('Este regalo es ___ ti.',['por','para','de'],1,'Este regalo es para ti.'),
  ('Gracias ___ todo.',['por','para','en'],0,'Gracias por todo.'),
  ('Estudio ___ ser médico.',['por','para','a'],1,'Estudio para ser médico.'),
  ('Hablo con mi familia ___ teléfono.',['por','para','de'],0,'Hablo con mi familia por teléfono.'),
  ('Salgo ___ Madrid mañana.',['por','para','en'],1,'Salgo para Madrid mañana.'),
  ('Trabajo ___ la mañana.',['por','para','a'],0,'Trabajo por la mañana.')])
