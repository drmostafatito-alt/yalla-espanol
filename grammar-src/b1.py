# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))

topic('b1-contraste','Indefinido o imperfecto','الفرق بين المنتهي والمستمر في الماضي',
 [('El imperfecto describe el fondo: hábitos, personas, el tiempo y las acciones en curso. El indefinido cuenta los hechos que avanzan la historia.','يصف الماضي المستمر الخلفية: العادات والأشخاص والطقس والأفعال الجارية. أما المنتهي فيروي الأحداث التي تتقدم بها القصة.'),
  ('Cuando una acción en curso se interrumpe, el imperfecto va con la acción larga y el indefinido con la acción corta: Dormía cuando sonó el teléfono.','حين يقطع حدثٌ فعلًا جاريًا، نستعمل المستمر للفعل الطويل والمنتهي للفعل القصير: Dormía cuando sonó el teléfono.')],
 {'head':['imperfecto','indefinido'],'rows':[['hábito: Iba al gimnasio cada día.','hecho único: Ayer fui al gimnasio.'],['descripción: Hacía sol.','cambio: De pronto empezó a llover.'],['acción en curso: Leía un libro.','acción corta: Sonó el timbre.'],['edad, hora, estado: Eran las ocho.','secuencia: Entré, saludé y me senté.']]},
 [('Cuando llegué, mis amigos cenaban.','حين وصلت كان أصدقائي يتعشون.'),('Hacía frío, así que cerré la puerta.','كان الجو باردًا فأغلقت الباب.'),('Mientras estudiaba, sonó el teléfono.','بينما كنت أدرس رنّ الهاتف.'),('De niña, visitaba a su abuela cada verano.','حين كانت طفلة كانت تزور جدتها كل صيف.'),('Ayer salí del trabajo a las seis.','أمس خرجت من العمل في السادسة.'),('Eran las diez y todavía trabajábamos.','كانت الساعة العاشرة وكنا لا نزال نعمل.')],
 [('Cuando entré, ella ___ la televisión.',['veía','vio','ve'],0,'Cuando entré, ella veía la televisión.'),
  ('Ayer ___ al cine con mis primos.',['íbamos','fuimos','vamos'],1,'Ayer fuimos al cine con mis primos.'),
  ('De niño ___ en un pueblo.',['viví','vivía','vivo'],1,'De niño vivía en un pueblo.'),
  ('Mientras comíamos, ___ el timbre.',['sonaba','sonó','suena'],1,'Mientras comíamos, sonó el timbre.'),
  ('___ muy tarde y estábamos cansados.',['Fue','Era','Es'],1,'Era muy tarde y estábamos cansados.'),
  ('El año pasado ___ a Italia.',['viajé','viajaba','viajo'],0,'El año pasado viajé a Italia.')])

topic('b1-pluscuamperfecto','Pretérito pluscuamperfecto','الماضي البعيد (pluscuamperfecto)',
 [('Se forma con el imperfecto de haber y el participio: había hablado, habías comido, había vivido.','يتكوّن من الماضي المستمر للفعل haber مع اسم المفعول: había hablado وhabías comido وhabía vivido.'),
  ('Expresa una acción anterior a otra acción pasada: Cuando llegué, la película ya había empezado.','يعبّر عن فعل سبق فعلًا آخر في الماضي: Cuando llegué, la película ya había empezado.')],
 {'head':['','haber (imperfecto)','participio'],'rows':[['yo','había','hablado'],['tú','habías','comido'],['él / ella / usted','había','vivido'],['nosotros','habíamos','hecho'],['vosotros','habíais','visto'],['ellos / ustedes','habían','escrito']]},
 [('Cuando llegué, el tren ya había salido.','حين وصلت كان القطار قد غادر.'),('No sabía que ellos se habían mudado.','لم أكن أعلم أنهم انتقلوا إلى بيت آخر.'),('Ya habíamos cenado cuando llamaste.','كنا قد تعشينا حين اتصلت.'),('Nunca había visto el mar.','لم أكن قد رأيت البحر قط.'),('Ella me dijo que había terminado el informe.','قالت لي إنها أنهت التقرير.'),('¿Habías estado antes en Madrid?','هل كنت قد زرت مدريد من قبل؟')],
 [('Cuando llegué, ellos ya ___ comido.',['había','habían','han'],1,'Cuando llegué, ellos ya habían comido.'),
  ('Yo nunca ___ visto nieve.',['había','habías','hube'],0,'Yo nunca había visto nieve.'),
  ('Nosotros ya ___ salido de casa.',['habíamos','habíais','hemos'],0,'Nosotros ya habíamos salido de casa.'),
  ('Tú ya habías ___ la cena. (hacer)',['hacido','hecho','hace'],1,'Tú ya habías hecho la cena.'),
  ('Ella había ___ una carta. (escribir)',['escribido','escrito','escribe'],1,'Ella había escrito una carta.'),
  ('Antes de ese viaje, yo no ___ viajado en avión.',['había','habías','habían'],0,'Antes de ese viaje, yo no había viajado en avión.')])

topic('b1-condicional','Condicional simple','الشرطي البسيط (condicional)',
 [('Se forma como el futuro: infinitivo más -ía, -ías, -ía, -íamos, -íais, -ían. Los verbos irregulares usan la misma raíz que en el futuro: tendría, haría, podría.','يتكوّن مثل المستقبل: المصدر مع النهايات -ía وغيرها. والأفعال الشاذة تستعمل الجذر نفسه الذي في المستقبل: tendría وharía وpodría.'),
  ('Lo usamos para cortesía, consejos y deseos: ¿Podría ayudarme? Yo estudiaría más. Me gustaría viajar.','نستعمله للمجاملة والنصائح والأمنيات: ¿Podría ayudarme? Yo estudiaría más. Me gustaría viajar.')],
 {'head':['','hablar','tener'],'rows':[['yo','hablaría','tendría'],['tú','hablarías','tendrías'],['él / ella / usted','hablaría','tendría'],['nosotros','hablaríamos','tendríamos'],['vosotros','hablaríais','tendríais'],['ellos / ustedes','hablarían','tendrían']]},
 [('¿Podría usted repetir la pregunta?','هل يمكنك إعادة السؤال من فضلك؟'),('Me gustaría tomar un café.','أود أن أشرب قهوة.'),('Yo, en tu lugar, hablaría con el jefe.','لو كنت مكانك لتحدثت مع المدير.'),('Con más dinero, viajaríamos por el mundo.','بمزيد من المال كنا سنسافر حول العالم.'),('¿Te importaría cerrar la puerta?','هل تمانع في إغلاق الباب؟'),('Ella dijo que vendría mañana.','قالت إنها ستأتي غدًا.')],
 [('¿___ usted ayudarme, por favor?',['Podría','Puede','Pudo'],0,'¿Podría usted ayudarme, por favor?'),
  ('Yo en tu lugar ___ más.',['estudiaría','estudio','estudié'],0,'Yo en tu lugar estudiaría más.'),
  ('Nosotros ___ una casa grande.',['tendríamos','tendremos','teníamos'],0,'Nosotros tendríamos una casa grande.'),
  ('Me ___ vivir cerca del mar.',['gustaría','gusta','gustó'],0,'Me gustaría vivir cerca del mar.'),
  ('Ella dijo que ___ a la fiesta.',['vendría','vendrá','viene'],0,'Ella dijo que vendría a la fiesta.'),
  ('Tú ___ más feliz con otro trabajo.',['serías','eres','fuiste'],0,'Tú serías más feliz con otro trabajo.')])

topic('b1-subjuntivo','Presente de subjuntivo','المضارع المنصوب والمجزوم (presente de subjuntivo)',
 [('Para formarlo, tomamos la forma yo del presente, quitamos la -o y ponemos la vocal contraria: hablo → hable, como → coma, vivo → viva.','لتكوينه نأخذ صيغة yo من المضارع ونحذف -o ونضع حرف العلة المخالف: hablo → hable وcomo → coma وvivo → viva.'),
  ('Lo usamos después de querer que, esperar que, es importante que, para que y ojalá, sobre todo cuando cambia el sujeto: Quiero que vengas.','نستعمله بعد querer que وesperar que وes importante que وpara que وojalá، خاصة حين يتغير الفاعل: Quiero que vengas.')],
 {'head':['','hablar','comer','vivir'],'rows':[['yo','hable','coma','viva'],['tú','hables','comas','vivas'],['él / ella / usted','hable','coma','viva'],['nosotros','hablemos','comamos','vivamos'],['vosotros','habléis','comáis','viváis'],['ellos / ustedes','hablen','coman','vivan']]},
 [('Quiero que vengas a mi fiesta.','أريد أن تأتي إلى حفلتي.'),('Espero que haga buen tiempo.','آمل أن يكون الطقس جميلًا.'),('Es importante que comas bien.','من المهم أن تأكل جيدًا.'),('Te llamo para que sepas la hora.','أتصل بك لتعرف الموعد.'),('Ojalá ganemos el partido.','أتمنى أن نفوز بالمباراة.'),('Mi madre quiere que estudie medicina.','تريد أمي أن أدرس الطب.')],
 [('Quiero que tú ___ conmigo.',['vienes','vengas','vendrás'],1,'Quiero que tú vengas conmigo.'),
  ('Espero que ella ___ pronto.',['llegue','llega','llegará'],0,'Espero que ella llegue pronto.'),
  ('Es importante que nosotros ___ temprano.',['salimos','salgamos','salíamos'],1,'Es importante que nosotros salgamos temprano.'),
  ('Mi padre quiere que yo ___ inglés.',['hablo','hable','hablaré'],1,'Mi padre quiere que yo hable inglés.'),
  ('Ojalá ___ sol mañana.',['hace','haga','hará'],1,'Ojalá haga sol mañana.'),
  ('Te doy el libro para que ___ .',['lees','leas','leerás'],1,'Te doy el libro para que leas.')])

topic('b1-imp-negativo','Imperativo negativo','النهي (imperativo negativo)',
 [('Para decir que no a un tú, usamos no más la forma tú del subjuntivo: no hables, no comas, no escribas.','للنهي مع tú نستعمل no مع صيغة tú من المضارع المنصوب: no hables وno comas وno escribas.'),
  ('Con usted también usamos el subjuntivo: no hable, no coma. Los pronombres van antes del verbo: no te sientes, no lo hagas.','ومع usted نستعمل المضارع المنصوب أيضًا: no hable وno coma. وتأتي الضمائر قبل الفعل: no te sientes وno lo hagas.')],
 {'head':['afirmativo (tú)','negativo (tú)'],'rows':[['habla','no hables'],['come','no comas'],['escribe','no escribas'],['haz','no hagas'],['ven','no vengas'],['siéntate','no te sientes']]},
 [('No hables tan rápido, por favor.','لا تتحدث بسرعة كبيرة من فضلك.'),('No comas antes de dormir.','لا تأكل قبل النوم.'),('No lo hagas ahora.','لا تفعل ذلك الآن.'),('No vengas muy tarde, por favor.','لا تأتِ متأخرًا جدًا من فضلك.'),('No se preocupe, señor.','لا تقلق يا سيدي.'),('No te sientes ahí.','لا تجلس هناك.')],
 [('No ___ tan rápido. (tú, hablar)',['hables','habla','hable'],0,'No hables tan rápido.'),
  ('No ___ más café. (tú, beber)',['bebes','bebas','bebe'],1,'No bebas más café.'),
  ('No ___ muy tarde, por favor. (tú, venir)',['vengas','vienes','ven'],0,'No vengas muy tarde, por favor.'),
  ('No ___ , señora. (usted, preocuparse)',['te preocupes','se preocupe','te preocupas'],1,'No se preocupe, señora.'),
  ('No lo ___ ahora. (tú, hacer)',['haces','hagas','haz'],1,'No lo hagas ahora.'),
  ('No ___ la puerta. (tú, abrir)',['abres','abras','abre'],1,'No abras la puerta.')])

topic('b1-relativas','Oraciones de relativo','جمل الصلة (oraciones de relativo)',
 [('Que es el relativo más frecuente y sirve para personas y cosas: El libro que compré es muy bueno. Quien se usa para personas, sobre todo después de una preposición: La chica con quien hablé.','que هو أكثر أدوات الصلة استعمالًا ويصلح للأشخاص والأشياء. وتُستعمل quien للأشخاص، خاصة بعد حرف الجر.'),
  ('Donde indica lugar. Lo que se refiere a una idea: No entiendo lo que dices. El cual y la cual aparecen sobre todo en textos formales.','تدل donde على المكان، وتشير lo que إلى فكرة. أما el cual وla cual فتظهران غالبًا في النصوص الرسمية.')],
 {'head':['relativo','uso','ejemplo'],'rows':[['que','personas y cosas','El chico que vive aquí.'],['quien / quienes','personas','Ana, quien trabaja conmigo.'],['donde','lugar','La ciudad donde nací.'],['lo que','una idea','Lo que dices es verdad.'],['cuyo / cuya','posesión','Un amigo cuya casa es grande.']]},
 [('El libro que compré es muy interesante.','الكتاب الذي اشتريته مثير جدًا.'),('La chica con quien hablé es mi vecina.','الفتاة التي تحدثت معها هي جارتي.'),('Esta es la ciudad donde nací.','هذه هي المدينة التي ولدت فيها.'),('No entiendo lo que dices.','لا أفهم ما تقوله.'),('Tengo un amigo cuya casa es enorme.','لدي صديق بيته ضخم.'),('Los vecinos que viven arriba son simpáticos.','الجيران الذين يسكنون في الأعلى لطفاء.')],
 [('El café ___ bebo es muy fuerte.',['que','donde','quien'],0,'El café que bebo es muy fuerte.'),
  ('Esta es la casa ___ vivo.',['que','donde','lo que'],1,'Esta es la casa donde vivo.'),
  ('La señora con ___ hablé es médica.',['que','quien','donde'],1,'La señora con quien hablé es médica.'),
  ('No sé ___ quieres decir.',['que','lo que','donde'],1,'No sé lo que quieres decir.'),
  ('Tengo un amigo ___ padre es piloto.',['cuyo','que','donde'],0,'Tengo un amigo cuyo padre es piloto.'),
  ('Los libros ___ leo son interesantes.',['que','donde','cuyo'],0,'Los libros que leo son interesantes.')])
