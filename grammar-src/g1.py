# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))

topic('a2-muy-mucho','Muy y mucho','muy وmucho',
 [('Muy va antes de un adjetivo o de un adverbio y no cambia: muy alto, muy bien. Mucho acompaña a un verbo o a un nombre.','تأتي muy قبل صفة أو ظرف ولا تتغير، أما mucho فتصحب فعلًا أو اسمًا.'),
  ('Con un nombre, mucho concuerda: mucho tiempo, mucha agua, muchos amigos, muchas casas. Con un verbo no cambia: Trabajo mucho.','ومع الاسم تطابقه في الجنس والعدد، أما مع الفعل فلا تتغير.')],
 {'nohl':1,'head':['','uso','ejemplo'],'rows':[['muy + adjetivo','muy cansado','Estoy muy cansado.'],['muy + adverbio','muy bien','Hablas muy bien.'],['verbo + mucho','trabajar mucho','Trabajo mucho.'],['mucho + nombre','muchos amigos','Tengo muchos amigos.']]},
 [('Estoy muy cansado.','أنا متعب جدًا.'),('Hablas muy bien español.','تتكلم الإسبانية جيدًا جدًا.'),('Trabajo mucho en verano.','أعمل كثيرًا في الصيف.'),('Tengo muchos amigos.','عندي أصدقاء كثيرون.'),('Hay mucha gente en la calle.','يوجد ناس كثيرون في الشارع.'),('Esta casa es muy grande.','هذا البيت كبير جدًا.')],
 [('Estoy ___ cansado.',['muy','mucho','muchos'],0,'Estoy muy cansado.'),
  ('Trabajo ___ en verano.',['muy','mucho','muchos'],1,'Trabajo mucho en verano.'),
  ('Tengo ___ amigos.',['muchos','muy','mucha'],0,'Tengo muchos amigos.'),
  ('Hay ___ gente en la calle.',['mucho','muchas','mucha'],2,'Hay mucha gente en la calle.'),
  ('Esta casa es ___ grande.',['muy','mucho','mucha'],0,'Esta casa es muy grande.')])

topic('a2-saber-conocer','Saber y conocer','saber وconocer',
 [('Saber significa tener información o una habilidad: Sé la respuesta. Sé nadar. Conocer significa tener contacto con personas o lugares: Conozco a Ana. Conozco Madrid.','saber تعني معرفة معلومة أو إتقان مهارة، وconocer تعني معرفة شخص أو مكان.'),
  ('Las dos son irregulares en yo: sé y conozco. Con una persona usamos a: Conozco a tu hermano.','والفعلان شاذان مع yo: sé وconozco. وقبل الشخص نضع a.')],
 {'nohl':1,'head':['','saber','conocer'],'rows':[['yo','sé','conozco'],['tú','sabes','conoces'],['nosotros','sabemos','conocemos'],['uso','información, habilidad','personas, lugares']]},
 [('Sé la respuesta.','أعرف الجواب.'),('Yo sé nadar muy rápido.','أعرف السباحة بسرعة.'),('Conozco a tu hermano.','أعرف أخاك.'),('Conozco Madrid.','أعرف مدريد.'),('¿Sabes dónde vive Ana?','هل تعرف أين تسكن آنا؟'),('No conozco este barrio.','لا أعرف هذا الحي.')],
 [('Yo ___ la respuesta.',['sé','conozco','conoce'],0,'Yo sé la respuesta.'),
  ('Yo ___ a tu hermano.',['sé','conozco','sabes'],1,'Yo conozco a tu hermano.'),
  ('¿___ nadar?',['Sabes','Conoces','Conozco'],0,'¿Sabes nadar?'),
  ('No ___ este barrio.',['sé','conozco','sabes'],1,'No conozco este barrio.'),
  ('¿___ dónde vive Ana?',['Conoces','Sabes','Conozco'],1,'¿Sabes dónde vive Ana?')])

topic('b1-imperativo-pronombres','Imperativo con pronombres','الأمر مع الضمائر',
 [('En el imperativo afirmativo, los pronombres van detrás del verbo y unidos a él: Dímelo. Siéntate. Cómpralo. Si hace falta, se añade tilde.','في الأمر المثبت تلتصق الضمائر بآخر الفعل: dímelo وsiéntate وcómpralo، وقد نضيف علامة التشديد.'),
  ('En el imperativo negativo, los pronombres van delante: No me lo digas. No te sientes. No lo compres.','وفي الأمر المنفي تأتي الضمائر قبل الفعل.')],
 {'nohl':1,'head':['','afirmativo','negativo'],'rows':[['decir','Dímelo.','No me lo digas.'],['sentarse','Siéntate.','No te sientes.'],['comprar','Cómpralo.','No lo compres.'],['dar','Dámelo.','No me lo des.']]},
 [('Dímelo ahora.','قله لي الآن.'),('No me lo digas.','لا تقله لي.'),('Siéntate aquí, por favor.','اجلس هنا من فضلك.'),('No te sientes ahí.','لا تجلس هناك.'),('Cómpralo hoy.','اشتره اليوم.'),('No lo compres todavía.','لا تشتره بعد.')],
 [('___ aquí, por favor. (sentarse, tú)',['Siéntate','Te sientas','Sientate'],0,'Siéntate aquí, por favor.'),
  ('No ___ digas. (me lo)',['me lo','dímelo','lo me'],0,'No me lo digas.'),
  ('___ hoy. (comprarlo, tú)',['Cómpralo','Lo compra','Compralo'],0,'Cómpralo hoy.'),
  ('No ___ compres todavía.',['lo','le','te'],0,'No lo compres todavía.'),
  ('___ ahora. (decirme, tú, lo)',['Dímelo','Medílo','Me lo di'],0,'Dímelo ahora.')])

topic('b1-futuro-perfecto','Futuro perfecto y condicional compuesto','المستقبل التام والشرطي التام',
 [('El futuro perfecto se forma con habré, habrás, habrá… + participio. Expresa una acción terminada antes de un momento futuro: Mañana a las ocho ya habré terminado.','يتكوّن المستقبل التام من habré وhabrás… مع اسم المفعول، ويدل على فعل ينتهي قبل لحظة في المستقبل.'),
  ('El condicional compuesto se forma con habría, habrías… + participio. Habla de lo que no ocurrió: Yo habría ido, pero no pude.','ويتكوّن الشرطي التام من habría وhabrías… مع اسم المفعول، ويتحدث عمّا لم يحدث.')],
 {'nohl':1,'head':['','futuro perfecto','condicional compuesto'],'rows':[['yo','habré hablado','habría hablado'],['tú','habrás hablado','habrías hablado'],['él','habrá hablado','habría hablado'],['nosotros','habremos hablado','habríamos hablado']]},
 [('Mañana a las ocho ya habré terminado.','غدًا في الثامنة سأكون قد انتهيت.'),('Para el viernes habremos acabado el trabajo.','بحلول الجمعة سنكون قد أنهينا العمل.'),('Yo habría ido, pero no pude.','كنت سأذهب لكنني لم أستطع.'),('Ella habría comprado la casa.','كانت ستشتري البيت.'),('¿Habrás cenado ya?','هل تكون قد تعشّيت؟'),('Nosotros habríamos venido antes.','كنا سنأتي قبل ذلك.')],
 [('Mañana ya ___ terminado.',['habré','habría','he'],0,'Mañana ya habré terminado.'),
  ('Para el viernes ___ acabado el trabajo.',['habremos','habríamos','hemos'],0,'Para el viernes habremos acabado el trabajo.'),
  ('Yo ___ ido, pero no pude.',['habría','habré','había'],0,'Yo habría ido, pero no pude.'),
  ('Ella ___ comprado la casa.',['habría','habrá','habré'],0,'Ella habría comprado la casa.'),
  ('Nosotros ___ venido antes.',['habríamos','habremos','habíamos'],0,'Nosotros habríamos venido antes.')])

topic('b2-verbos-cambio','Verbos de cambio','أفعال التحوّل',
 [('Para hablar de un cambio usamos ponerse, volverse, hacerse y quedarse. Ponerse expresa un cambio temporal de estado: Se puso nervioso. Quedarse expresa un resultado: Se quedó sordo.','لوصف التحوّل نستعمل ponerse وvolverse وhacerse وquedarse. تدل ponerse على تغيّر مؤقت في الحال، وquedarse على نتيجة.'),
  ('Hacerse expresa un cambio voluntario o de profesión: Se hizo médico. Volverse expresa un cambio profundo y a veces repentino: Se volvió muy tímido.','وتدل hacerse على تحوّل إرادي أو مهني، وvolverse على تحوّل عميق وأحيانًا مفاجئ.')],
 {'nohl':1,'head':['','verbo','cambio'],'rows':[['ponerse','Se puso nervioso.','temporal'],['quedarse','Se quedó sordo.','resultado'],['hacerse','Se hizo médico.','voluntario'],['volverse','Se volvió tímido.','profundo']]},
 [('Se puso nervioso antes del examen.','أصابه التوتر قبل الامتحان.'),('Se quedó sordo después del accidente.','أصبح أصمّ بعد الحادث.'),('Mi hermano se hizo médico.','أخي أصبح طبيبًا.'),('Con la edad se volvió muy tímido.','مع التقدم في العمر صار خجولًا جدًا.'),('Me puse rojo de vergüenza.','احمرّ وجهي من الخجل.'),('Ella se quedó viuda joven.','ترمّلت وهي شابة.')],
 [('Se ___ nervioso antes del examen.',['puso','hizo','volvió'],0,'Se puso nervioso antes del examen.'),
  ('Mi hermano se ___ médico.',['puso','hizo','quedó'],1,'Mi hermano se hizo médico.'),
  ('Se ___ sordo después del accidente.',['quedó','hizo','puso'],0,'Se quedó sordo después del accidente.'),
  ('Me ___ rojo de vergüenza.',['hice','puse','volví'],1,'Me puse rojo de vergüenza.'),
  ('Con la edad se ___ muy tímido.',['volvió','puso','hizo'],0,'Con la edad se volvió muy tímido.')])
