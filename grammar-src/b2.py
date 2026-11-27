# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))

topic('b2-subj-imperfecto','Imperfecto de subjuntivo','الماضي الافتراضي',
 [('Se forma con la tercera persona del plural del indefinido: quitamos -ron y añadimos -ra, -ras, -ra, -ramos, -rais, -ran. Hablaron: hablara. Comieron: comiera.','يُصاغ من الغائبين بصيغة الجمع في الماضي المنتهي: نحذف -ron ونضيف -ra و-ras و-ra و-ramos و-rais و-ran.'),
  ('Lo usamos cuando el verbo principal está en pasado y pide subjuntivo: Quería que vinieras. También con si para cosas irreales: Si tuviera tiempo, viajaría.','نستعمله حين يكون الفعل الرئيسي في الماضي ويتطلب المضارع المنصوب، وكذلك مع si للأمور غير الواقعية.')],
 {'head':['','hablar','comer','ir / ser'],'rows':[['yo','hablara','comiera','fuera'],['tú','hablaras','comieras','fueras'],['él / ella / usted','hablara','comiera','fuera'],['nosotros','habláramos','comiéramos','fuéramos'],['vosotros','hablarais','comierais','fuerais'],['ellos / ustedes','hablaran','comieran','fueran']]},
 [('Quería que vinieras a mi casa.','كنت أريد أن تأتي إلى بيتي.'),('Mi madre pidió que habláramos más despacio.','طلبت أمي أن نتحدث ببطء أكثر.'),('Si tuviera más tiempo, viajaría mucho.','لو كان لدي وقت أكثر لسافرت كثيرًا.'),('No creía que fuera tan difícil.','لم أكن أظن أنه صعب إلى هذا الحد.'),('Esperaba que me llamaran ayer.','كنت آمل أن يتصلوا بي أمس.'),('Si yo fuera tú, estudiaría más.','لو كنت مكانك لدرست أكثر.')],
 [('Quería que tú ___ conmigo.',['vienes','vinieras','vengas'],1,'Quería que tú vinieras conmigo.'),
  ('Si ___ más dinero, compraría una casa.',['tengo','tuviera','tendré'],1,'Si tuviera más dinero, compraría una casa.'),
  ('Ella pidió que nosotros ___ en silencio.',['trabajamos','trabajáramos','trabajemos'],1,'Ella pidió que trabajáramos en silencio.'),
  ('No pensaba que ellos ___ tan tarde.',['llegan','llegaran','lleguen'],1,'No pensaba que llegaran tan tarde.'),
  ('Si yo ___ rico, ayudaría a todos.',['soy','fuera','seré'],1,'Si yo fuera rico, ayudaría a todos.'),
  ('Mi jefe quería que yo ___ el informe hoy.',['terminara','termino','termine'],0,'Mi jefe quería que yo terminara el informe hoy.')])

topic('b2-condicionales','Oraciones condicionales','جمل الشرط',
 [('Condición posible: si + presente. El resultado va en presente, futuro o imperativo. Si llueve, me quedo en casa. Si estudias, aprobarás.','شرط ممكن: si + المضارع، والنتيجة في المضارع أو المستقبل أو الأمر.'),
  ('Condición irreal en el presente: si + imperfecto de subjuntivo, y el resultado en condicional. Si tuviera tiempo, viajaría.','شرط غير واقعي في الحاضر: si + الماضي الافتراضي، والنتيجة في الشرطي.'),
  ('Condición imposible en el pasado: si + pluscuamperfecto de subjuntivo, y el resultado en condicional compuesto. Si hubiera sabido, habría venido.','شرط مستحيل في الماضي: si + الماضي البعيد الافتراضي، والنتيجة في الشرطي التام.')],
 {'nohl':1,'head':['','condición','resultado'],'rows':[['posible','si + presente','presente o futuro'],['irreal ahora','si + imperfecto de subjuntivo','condicional'],['imposible en el pasado','si + pluscuamperfecto de subjuntivo','condicional compuesto']]},
 [('Si llueve mañana, me quedo en casa.','إذا أمطرت غدًا فسأبقى في البيت.'),('Si estudias, aprobarás el examen.','إن درست فستنجح في الامتحان.'),('Si tuviera un coche, iría en coche al trabajo.','لو كان عندي سيارة لذهبت بها إلى العمل.'),('Si hubiera sabido la respuesta, te la habría dicho.','لو عرفت الجواب لقلته لك.'),('Si no comes, tendrás hambre.','إن لم تأكل فسوف تجوع.'),('Si viviéramos en el mar, nadaríamos cada día.','لو عشنا عند البحر لسبحنا كل يوم.')],
 [('Si tú ___, te ayudaré.',['pides','pidieras','hubieras pedido'],0,'Si tú pides, te ayudaré.'),
  ('Si yo ___ tiempo, leería más.',['tengo','tuviera','tendré'],1,'Si yo tuviera tiempo, leería más.'),
  ('Si ella ___ antes, habría llegado a tiempo.',['saliera','salió','hubiera salido'],2,'Si ella hubiera salido antes, habría llegado a tiempo.'),
  ('Si hace sol, ___ a la playa.',['iríamos','iremos','hubiéramos ido'],1,'Si hace sol, iremos a la playa.'),
  ('Si nosotros ___ más jóvenes, correríamos más.',['somos','fuéramos','seremos'],1,'Si nosotros fuéramos más jóvenes, correríamos más.'),
  ('Si no ___ tanto, no estarías cansado.',['trabajaras','trabajas','trabajaste'],0,'Si no trabajaras tanto, no estarías cansado.')])

topic('b2-pasiva','La voz pasiva','المبني للمجهول',
 [('Pasiva con ser: ser + participio. El participio concuerda con el sujeto, y quien hace la acción va con por. La casa fue construida por mi abuelo.','المبني للمجهول مع ser: ser + اسم المفعول، ويتفق مع الفاعل النحوي، ويأتي المنفِّذ بعد por.'),
  ('Pasiva refleja: se + verbo en tercera persona. Se usa cuando no importa quién hace la acción. Se vende un piso. Se venden pisos.','المبني للمجهول بـ se: se + الفعل في الغائب، ونستعمله حين لا يهم من يقوم بالفعل.')],
 {'nohl':1,'head':['','activa','con ser','refleja'],'rows':[['presente','Cierran la puerta.','La puerta es cerrada.','Se cierra la puerta.'],['pasado','Cerraron la puerta.','La puerta fue cerrada.','Se cerró la puerta.'],['plural','Venden los coches.','Los coches son vendidos.','Se venden los coches.']]},
 [('La catedral fue construida en el siglo doce.','شُيّدت الكاتدرائية في القرن الثاني عشر.'),('El libro fue escrito por un profesor.','كُتب الكتاب على يد أستاذ.'),('Se habla español en muchos países.','تُتحدث الإسبانية في بلدان كثيرة.'),('Se venden pisos en el centro.','تُباع شقق في الوسط.'),('Las cartas fueron enviadas ayer.','أُرسلت الرسائل أمس.'),('Aquí no se permite fumar.','لا يُسمح بالتدخين هنا.')],
 [('La puerta fue ___ por el viento.',['abierta','abierto','abrió'],0,'La puerta fue abierta por el viento.'),
  ('Se ___ frutas en el mercado.',['vende','venden','vendemos'],1,'Se venden frutas en el mercado.'),
  ('Los libros fueron ___ en mil novecientos noventa.',['publicados','publicado','publicamos'],0,'Los libros fueron publicados en mil novecientos noventa.'),
  ('Aquí se ___ español.',['habla','hablan','hablamos'],0,'Aquí se habla español.'),
  ('La cena fue ___ por mi hermano.',['preparado','preparada','preparaba'],1,'La cena fue preparada por mi hermano.'),
  ('En esta tienda se ___ ropa barata.',['vende','venden','vendes'],0,'En esta tienda se vende ropa barata.')])

topic('b2-indirecto','Estilo indirecto','الكلام المنقول',
 [('Para contar lo que alguien dijo usamos decir que + oración. Si el verbo de decir está en pasado, el tiempo suele retroceder: «Estoy cansado» se convierte en Dijo que estaba cansado.','لنقل كلام شخص نستعمل decir que + جملة. وإذا كان فعل القول في الماضي يرجع زمن الجملة غالبًا خطوة إلى الوراء.'),
  ('También cambian las palabras de tiempo y lugar: hoy pasa a ese día, mañana a al día siguiente, aquí a allí. Las preguntas se cuentan con si: Preguntó si venía.','وتتغير كلمات الزمان والمكان أيضًا، ويُنقل السؤال بـ si: Preguntó si venía.')],
 {'nohl':1,'head':['','directo','indirecto'],'rows':[['presente','«Trabajo mucho.»','Dijo que trabajaba mucho.'],['indefinido','«Compré un coche.»','Dijo que había comprado un coche.'],['futuro','«Llegaré tarde.»','Dijo que llegaría tarde.'],['perfecto','«He visto la película.»','Dijo que había visto la película.']]},
 [('Me dijo que estaba muy cansado.','قال لي إنه متعب جدًا.'),('Ella explicó que vivía en Madrid.','شرحت أنها تعيش في مدريد.'),('Mi amigo dijo que llegaría tarde.','قال صديقي إنه سيصل متأخرًا.'),('Preguntó si queríamos café.','سأل إن كنا نريد قهوة.'),('Nos dijeron que el tren había salido.','قالوا لنا إن القطار قد غادر.'),('Le pregunté dónde trabajaba.','سألته أين يعمل.')],
 [('Marta dijo que ___ en una oficina.',['trabaja','trabajaba','trabajó'],1,'Marta dijo que trabajaba en una oficina.'),
  ('Me dijo que ___ mañana.',['vendrá','vendría','viene'],1,'Me dijo que vendría mañana.'),
  ('Preguntó ___ teníamos tiempo.',['que','si','como'],1,'Preguntó si teníamos tiempo.'),
  ('Juan dijo que ya ___ la cena.',['hace','había hecho','hará'],1,'Juan dijo que ya había hecho la cena.'),
  ('Ellos dijeron que ___ pronto.',['llegarían','llegan','llegaron'],0,'Ellos dijeron que llegarían pronto.'),
  ('Le pregunté ___ vivía.',['dónde','que','cuál'],0,'Le pregunté dónde vivía.')])

topic('b2-perifrasis','Perífrasis verbales','الأفعال المركّبة',
 [('Una perífrasis une un verbo auxiliar con otro verbo en infinitivo o gerundio. Juntos expresan obligación, acción reciente, repetición o continuidad.','تجمع العبارة الفعلية بين فعل مساعد وفعل آخر في المصدر أو الحال، وتعبّر عن الوجوب أو الحدث القريب أو التكرار أو الاستمرار.'),
  ('Tener que + infinitivo es obligación. Acabar de + infinitivo es algo que pasó hace muy poco. Volver a + infinitivo es repetir. Seguir + gerundio es continuar.','tener que للوجوب، وacabar de لما حدث قبل قليل، وvolver a للتكرار، وseguir مع الحال للاستمرار.')],
 {'nohl':1,'head':['','perífrasis','ejemplo'],'rows':[['obligación','tener que + infinitivo','Tengo que estudiar.'],['acción reciente','acabar de + infinitivo','Acabo de llegar.'],['repetición','volver a + infinitivo','Vuelvo a intentarlo.'],['continuidad','seguir + gerundio','Sigo trabajando.']]},
 [('Tengo que estudiar para el examen.','يجب أن أدرس من أجل الامتحان.'),('Acabo de llegar a casa.','وصلت إلى البيت للتو.'),('Voy a volver a llamarte mañana.','سأعاود الاتصال بك غدًا.'),('Mi hermano sigue durmiendo.','لا يزال أخي نائمًا.'),('Ellos acaban de salir.','لقد خرجوا للتو.'),('Hay que lavarse las manos.','ينبغي غسل اليدين.')],
 [('Acabo ___ comer.',['de','a','que'],0,'Acabo de comer.'),
  ('Tengo ___ trabajar hoy.',['que','de','a'],0,'Tengo que trabajar hoy.'),
  ('Ella sigue ___ en la misma empresa.',['trabajar','trabajando','trabajado'],1,'Ella sigue trabajando en la misma empresa.'),
  ('Vamos a ___ a jugar.',['volver','volvemos','volviendo'],0,'Vamos a volver a jugar.'),
  ('Mi padre ___ de llegar.',['acaba','acabo','acaban'],0,'Mi padre acaba de llegar.'),
  ('Hay ___ llamar al médico.',['que','de','a'],0,'Hay que llamar al médico.')])

topic('b2-conectores','Conectores con subjuntivo','أدوات الربط مع المضارع المنصوب',
 [('Después de para que, antes de que y sin que usamos siempre subjuntivo. Te llamo para que no te preocupes.','بعد para que وantes de que وsin que نستعمل المضارع المنصوب دائمًا.'),
  ('Con aunque y cuando hay dos opciones. Indicativo para algo real o habitual, subjuntivo para algo futuro o incierto. Aunque llueva, saldré. Cuando llegues, llámame.','مع aunque وcuando خياران: المضارع المعتاد للأمر الواقعي أو المتكرر، والمنصوب للأمر المستقبلي أو غير المؤكد.')],
 {'nohl':1,'head':['','conector','modo'],'rows':[['siempre subjuntivo','para que, antes de que, sin que','Estudia para que lo entiendas.'],['depende','aunque','Aunque llueva, saldré.'],['depende','cuando','Cuando llegues, llámame.']]},
 [('Te llamo para que no te preocupes.','أتصل بك كي لا تقلق.'),('Quiero salir antes de que llueva.','أريد الخروج قبل أن تمطر.'),('Aunque llueva, iremos al parque.','حتى لو أمطرت سنذهب إلى الحديقة.'),('Cuando llegues, llámame.','حين تصل اتصل بي.'),('Entró sin que nadie lo viera.','دخل دون أن يراه أحد.'),('Cuando llego a casa, ceno.','حين أصل إلى البيت أتعشى.')],
 [('Te explico para que lo ___.',['entiendes','entiendas','entendías'],1,'Te explico para que lo entiendas.'),
  ('Mañana, cuando ___ a casa, te llamaré.',['llego','llegue','llegaré'],1,'Mañana, cuando llegue a casa, te llamaré.'),
  ('Voy a salir antes de que ___ la lluvia.',['empieza','empiece','empezó'],1,'Voy a salir antes de que empiece la lluvia.'),
  ('Sale de casa sin que nadie lo ___.',['ve','vea','vio'],1,'Sale de casa sin que nadie lo vea.'),
  ('Estudia para que sus padres ___ orgullosos.',['están','estén','estaban'],1,'Estudia para que sus padres estén orgullosos.'),
  ('Aunque ___ mañana, iremos al campo.',['llueve','llueva','llovió'],1,'Aunque llueva mañana, iremos al campo.')])
