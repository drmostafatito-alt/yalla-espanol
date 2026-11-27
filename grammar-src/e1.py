# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))

topic('a2-preposiciones-lugar','Preposiciones de lugar','حروف الجر للمكان',
 [('Las preposiciones de lugar indican dónde está algo: en, sobre, debajo de, delante de, detrás de, al lado de, entre, cerca de, lejos de.','تبيّن حروف الجر للمكان موضع الشيء: en وsobre وdebajo de وdelante de وdetrás de وal lado de وentre وcerca de وlejos de.'),
  ('Con a + el usamos al, y con de + el usamos del: Voy al banco. Está cerca del parque.','وعند اجتماع a مع el نقول al، وعند اجتماع de مع el نقول del.')],
 {'nohl':1,'head':['','preposición','ejemplo'],'rows':[['sobre','sobre la mesa','El libro está sobre la mesa.'],['debajo de','debajo de la silla','El gato está debajo de la silla.'],['al lado de','al lado del banco','La tienda está al lado del banco.'],['entre','entre A y B','El parque está entre la casa y la escuela.']]},
 [('El libro está sobre la mesa.','الكتاب على الطاولة.'),('El gato está debajo de la silla.','القط تحت الكرسي.'),('La tienda está al lado del banco.','المتجر بجانب البنك.'),('El parque está entre la casa y la escuela.','الحديقة بين البيت والمدرسة.'),('Mi casa está cerca del centro.','بيتي قريب من الوسط.'),('Voy al banco por la mañana.','أذهب إلى البنك صباحًا.')],
 [('El libro está ___ la mesa.',['sobre','debajo','entre'],0,'El libro está sobre la mesa.'),
  ('El gato está ___ de la silla.',['debajo','sobre','entre'],0,'El gato está debajo de la silla.'),
  ('La tienda está al ___ del banco.',['lado','lejos','cerca'],0,'La tienda está al lado del banco.'),
  ('Mi casa está cerca ___ centro.',['del','al','el'],0,'Mi casa está cerca del centro.'),
  ('Voy ___ banco por la mañana.',['al','del','a'],0,'Voy al banco por la mañana.')])

topic('b1-participio','El participio como adjetivo','اسم المفعول في الإسبانية',
 [('El participio puede funcionar como adjetivo y concuerda en género y número: la puerta cerrada, los libros abiertos.','يمكن أن يعمل اسم المفعول عمل الصفة، ويطابق الموصوف في الجنس والعدد.'),
  ('Con estar expresa el resultado de una acción: La puerta está cerrada. Algunos participios son irregulares: abierto, escrito, hecho, roto, visto.','ومع estar يدل على نتيجة فعل: la puerta está cerrada. ومن الأسماء الشاذة: abierto وescrito وhecho وroto وvisto.')],
 {'nohl':1,'head':['','masculino','femenino'],'rows':[['singular','cerrado','cerrada'],['plural','cerrados','cerradas'],['irregular','abierto','abierta'],['irregular','roto','rota']]},
 [('La puerta está cerrada.','الباب مغلق.'),('Las ventanas están abiertas.','النوافذ مفتوحة.'),('Los libros están escritos en español.','الكتب مكتوبة بالإسبانية.'),('El vaso está roto.','الكوب مكسور.'),('La cena está hecha.','العشاء جاهز.'),('Estoy cansado después del viaje.','أنا متعب بعد السفر.')],
 [('La puerta está ___.',['cerrada','cerrado','cerrar'],0,'La puerta está cerrada.'),
  ('Las ventanas están ___.',['abiertas','abierto','abiertos'],0,'Las ventanas están abiertas.'),
  ('El vaso está ___.',['rompido','roto','rota'],1,'El vaso está roto.'),
  ('Los libros están ___ en español.',['escribidos','escritos','escrito'],1,'Los libros están escritos en español.'),
  ('La cena está ___.',['hecha','hacida','hecho'],0,'La cena está hecha.')])

topic('b2-estilo-indirecto-preguntas','Estilo indirecto: preguntas','الكلام المنقول: الأسئلة',
 [('Para repetir una pregunta con respuesta sí o no usamos si: ¿Vienes? Me preguntó si venía. Con palabras interrogativas las mantenemos: ¿Dónde vives? Me preguntó dónde vivía.','لنقل سؤال جوابه نعم أو لا نستعمل si، ومع أدوات الاستفهام نُبقيها: me preguntó dónde vivía.'),
  ('Si el verbo que introduce está en pasado, el tiempo retrocede: vives pasa a vivías, viniste pasa a había venido. No usamos signos de interrogación.','إذا كان فعل النقل ماضيًا تراجع زمن الفعل المنقول، ولا نستعمل علامات الاستفهام.')],
 {'nohl':1,'head':['','directo','indirecto'],'rows':[['sí o no','¿Vienes?','Preguntó si venía.'],['dónde','¿Dónde vives?','Preguntó dónde vivía.'],['qué','¿Qué haces?','Preguntó qué hacía.'],['cuándo','¿Cuándo llegas?','Preguntó cuándo llegaba.']]},
 [('Me preguntó si venía a la fiesta.','سألني إن كنت آتي إلى الحفلة.'),('Me preguntó dónde vivía.','سألني أين أسكن.'),('Preguntó qué hacía yo allí.','سأل ماذا كنت أفعل هناك.'),('Quería saber cuándo llegaba el tren.','أراد أن يعرف متى يصل القطار.'),('Me preguntó cuánto costaba el billete.','سألني كم تكلّف التذكرة.'),('Nos preguntaron si teníamos tiempo.','سألونا إن كان عندنا وقت.')],
 [('Me preguntó ___ venía a la fiesta.',['si','qué','que'],0,'Me preguntó si venía a la fiesta.'),
  ('Me preguntó dónde ___.',['vivía','vivo','viviré'],0,'Me preguntó dónde vivía.'),
  ('Preguntó ___ hacía yo allí.',['qué','si','cuándo'],0,'Preguntó qué hacía yo allí.'),
  ('Quería saber cuándo ___ el tren.',['llega','llegaba','llegue'],1,'Quería saber cuándo llegaba el tren.'),
  ('Nos preguntaron si ___ tiempo.',['tenemos','teníamos','tendremos'],1,'Nos preguntaron si teníamos tiempo.')])

topic('b2-infinitivo-preposiciones','El infinitivo con preposición','المصدر مع حروف الجر',
 [('Después de una preposición usamos el infinitivo: sin + infinitivo, antes de + infinitivo, después de + infinitivo, al + infinitivo.','بعد حرف الجر نستعمل المصدر: sin وantes de وdespués de وal مع المصدر.'),
  ('Al + infinitivo significa cuando: Al llegar, llamé a mi madre. Sin + infinitivo significa que algo no ocurre: Salió sin decir nada.','وتعني al مع المصدر «عندما»، أما sin فتعني نفي الحدث: Salió sin decir nada: خرج دون أن يقول شيئًا.')],
 {'nohl':1,'head':['','estructura','ejemplo'],'rows':[['al + inf.','cuando','Al llegar, llamé a mi madre.'],['sin + inf.','no hacer','Salió sin decir nada.'],['antes de + inf.','antes','Lávate antes de comer.'],['después de + inf.','después','Después de cenar, salimos.']]},
 [('Al llegar, llamé a mi madre.','عندما وصلت اتصلت بأمي.'),('Salió sin decir nada.','خرج دون أن يقول شيئًا.'),('Lávate las manos antes de comer.','اغسل يديك قبل الأكل.'),('Después de cenar, salimos a pasear.','بعد العشاء خرجنا للتنزه.'),('Se fue sin despedirse.','ذهب دون أن يودّع.'),('Piensa bien antes de hablar.','فكّر جيدًا قبل أن تتكلم.')],
 [('___ llegar, llamé a mi madre.',['Al','Del','En'],0,'Al llegar, llamé a mi madre.'),
  ('Salió ___ decir nada.',['sin','con','para'],0,'Salió sin decir nada.'),
  ('Lávate las manos ___ de comer.',['antes','después','sin'],0,'Lávate las manos antes de comer.'),
  ('___ de cenar, salimos a pasear.',['Después','Antes','Sin'],0,'Después de cenar, salimos a pasear.'),
  ('Piensa bien antes de ___.',['hablar','hablas','hablé'],0,'Piensa bien antes de hablar.')])

topic('b1-relativas-explicativas','Relativas explicativas','الجمل الموصولة التوضيحية',
 [('Las oraciones explicativas añaden información extra y van entre comas: Mi padre, que está de vacaciones, llega mañana.','تضيف الجملة التوضيحية معلومة إضافية وتُكتب بين فاصلتين.'),
  ('Podemos usar que, quien, el cual, la cual: Mi hermana, quien vive en Madrid, es médica. Con preposición usamos el que o el cual: La casa en la que vivo es vieja.','يمكن استعمال que وquien وel cual، ومع حرف الجر نستعمل el que أو el cual.')],
 {'nohl':1,'head':['','tipo','ejemplo'],'rows':[['explicativa','con comas','Mi padre, que está de vacaciones, llega mañana.'],['especificativa','sin comas','El hombre que habla es mi padre.'],['con preposición','en la que','La casa en la que vivo es vieja.']]},
 [('Mi padre, que está de vacaciones, llega mañana.','أبي، وهو في إجازة، سيصل غدًا.'),('Mi hermana, quien vive en Madrid, es médica.','أختي، التي تسكن في مدريد، طبيبة.'),('Madrid, que es la capital, tiene muchos museos.','مدريد، وهي العاصمة، فيها متاحف كثيرة.'),('La casa en la que vivo es vieja.','البيت الذي أسكن فيه قديم.'),('El libro que compré es muy bueno.','الكتاب الذي اشتريته جيد جدًا.'),('Ana, con quien trabajo, es muy simpática.','آنا، التي أعمل معها، لطيفة جدًا.')],
 [('Mi padre, ___ está de vacaciones, llega mañana.',['que','donde','cuyo'],0,'Mi padre, que está de vacaciones, llega mañana.'),
  ('Mi hermana, ___ vive en Madrid, es médica.',['quien','donde','cual'],0,'Mi hermana, quien vive en Madrid, es médica.'),
  ('La casa en ___ vivo es vieja.',['la que','lo que','el que'],0,'La casa en la que vivo es vieja.'),
  ('Ana, con ___ trabajo, es muy simpática.',['quien','que','donde'],0,'Ana, con quien trabajo, es muy simpática.'),
  ('El libro ___ compré es muy bueno.',['que','quien','cuando'],0,'El libro que compré es muy bueno.')])
