# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))

topic('a1-frecuencia','Adverbios de frecuencia','ظروف التكرار',
 [('Los adverbios de frecuencia dicen cuántas veces hacemos algo: siempre, normalmente, a menudo, a veces, casi nunca, nunca.','تبيّن ظروف التكرار كم مرة نفعل الشيء: siempre وnormalmente وa menudo وa veces وcasi nunca وnunca.'),
  ('Van normalmente antes del verbo. Con nunca, usamos no antes del verbo si nunca va después: Nunca como carne. No como carne nunca.','وتأتي عادةً قبل الفعل، ومع nunca إذا جاءت بعد الفعل وجب وضع no قبله.')],
 {'nohl':1,'head':['','frecuencia','ejemplo'],'rows':[['100%','siempre','Siempre desayuno en casa.'],['70%','normalmente','Normalmente llego temprano.'],['30%','a veces','A veces voy al cine.'],['0%','nunca','Nunca bebo café.']]},
 [('Siempre desayuno en casa.','أتناول الفطور دائمًا في البيت.'),('Normalmente llego temprano.','عادةً أصل مبكرًا.'),('A veces voy al cine.','أحيانًا أذهب إلى السينما.'),('Casi nunca veo la televisión.','نادرًا ما أشاهد التلفاز.'),('Nunca bebo café.','لا أشرب القهوة أبدًا.'),('No bebo café nunca.','لا أشرب القهوة أبدًا.')],
 [('___ desayuno en casa. (todos los días)',['Siempre','Nunca','A veces'],0,'Siempre desayuno en casa.'),
  ('___ bebo café. (0%)',['Siempre','Nunca','Normalmente'],1,'Nunca bebo café.'),
  ('No como carne ___.',['nunca','siempre','a veces'],0,'No como carne nunca.'),
  ('___ voy al cine, una vez al mes.',['A veces','Siempre','Nunca'],0,'A veces voy al cine, una vez al mes.'),
  ('Casi ___ veo la televisión.',['nunca','siempre','todos'],0,'Casi nunca veo la televisión.')])

topic('a2-obligacion','Obligación y necesidad','الإلزام والحاجة',
 [('Tener que + infinitivo expresa una obligación personal: Tengo que estudiar. Hay que + infinitivo expresa una obligación general: Hay que beber agua.','tener que مع المصدر تعبّر عن واجب شخصي، وhay que تعبّر عن واجب عام.'),
  ('Deber + infinitivo aconseja o recuerda un deber: Debes descansar. Necesitar + infinitivo expresa necesidad: Necesito dormir.','deber للنصح أو الواجب، وnecesitar للحاجة.')],
 {'nohl':1,'head':['','estructura','ejemplo'],'rows':[['personal','tener que + inf.','Tengo que estudiar.'],['general','hay que + inf.','Hay que beber agua.'],['consejo','deber + inf.','Debes descansar.'],['necesidad','necesitar + inf.','Necesito dormir.']]},
 [('Tengo que estudiar para el examen.','يجب أن أدرس للامتحان.'),('Hay que beber mucha agua.','يجب شرب الكثير من الماء.'),('Debes descansar un poco.','عليك أن ترتاح قليلًا.'),('Necesito dormir ocho horas.','أحتاج إلى النوم ثماني ساعات.'),('Ella tiene que trabajar mañana.','عليها أن تعمل غدًا.'),('No hay que fumar aquí.','لا يجوز التدخين هنا.')],
 [('Yo ___ que estudiar para el examen.',['tengo','hay','debo'],0,'Yo tengo que estudiar para el examen.'),
  ('___ que beber mucha agua.',['Hay','Tiene','Tienen'],0,'Hay que beber mucha agua.'),
  ('Tú ___ descansar un poco.',['debes','hay','tengo'],0,'Tú debes descansar un poco.'),
  ('Ella ___ que trabajar mañana.',['tiene','tienes','tengo'],0,'Ella tiene que trabajar mañana.'),
  ('Nosotros ___ que salir ya.',['tenemos','tienen','hay'],0,'Nosotros tenemos que salir ya.')])

topic('b1-subjuntivo-emocion','Subjuntivo con emociones','المضارع المنصوب مع المشاعر',
 [('Con verbos de emoción o gusto usamos que + subjuntivo cuando el sujeto cambia: Me alegra que vengas. Me molesta que fumes aquí.','مع أفعال المشاعر نستعمل que مع المضارع المنصوب عندما يتغير الفاعل.'),
  ('Si el sujeto es el mismo, usamos el infinitivo: Me alegra verte. Espero que tengas suerte. Ojalá que llueva.','وإذا اتحد الفاعل استعملنا المصدر. وبعد espero que وojalá نستعمل المضارع المنصوب.')],
 {'nohl':1,'head':['','mismo sujeto','sujeto distinto'],'rows':[['alegrarse','Me alegra verte.','Me alegra que vengas.'],['molestar','Me molesta esperar.','Me molesta que fumes.'],['esperar','Espero ganar.','Espero que ganes.']]},
 [('Me alegra que vengas a la fiesta.','يسعدني أنك ستأتي إلى الحفلة.'),('Me molesta que fumes aquí.','يزعجني أنك تدخّن هنا.'),('Espero que tengas mucha suerte.','أتمنى أن يكون حظك وفيرًا.'),('Me alegra verte otra vez.','يسعدني أن أراك مرة أخرى.'),('Ojalá que mañana haga sol.','أرجو أن يكون الجو مشمسًا غدًا.'),('Tengo miedo de que llegue tarde.','أخاف أن يصل متأخرًا.')],
 [('Me alegra que ___ a la fiesta.',['vienes','vengas','vendrás'],1,'Me alegra que vengas a la fiesta.'),
  ('Me molesta que tú ___ aquí.',['fumas','fumes','fumaste'],1,'Me molesta que tú fumes aquí.'),
  ('Espero que ___ mucha suerte.',['tienes','tengas','tuviste'],1,'Espero que tengas mucha suerte.'),
  ('Me alegra ___ otra vez.',['verte','que verte','te veas'],0,'Me alegra verte otra vez.'),
  ('Ojalá que mañana ___ sol.',['hace','haga','hizo'],1,'Ojalá que mañana haga sol.')])

topic('a2-ordinales','Números ordinales','الأعداد الترتيبية',
 [('Los ordinales indican el orden: primero, segundo, tercero, cuarto, quinto. Concuerdan en género y número: la primera casa, los segundos platos.','تدل الأعداد الترتيبية على الترتيب، وتطابق الاسم في الجنس والعدد.'),
  ('Primero y tercero pierden la o delante de un nombre masculino singular: el primer día, el tercer piso.','وتفقد primero وtercero حرف o قبل الاسم المذكر المفرد: el primer día وel tercer piso.')],
 {'nohl':1,'head':['','masculino','femenino'],'rows':[['1.º','primero','primera'],['2.º','segundo','segunda'],['3.º','tercero','tercera'],['4.º','cuarto','cuarta'],['5.º','quinto','quinta']]},
 [('Vivo en el primer piso.','أسكن في الطابق الأول.'),('Es la segunda puerta a la derecha.','إنه الباب الثاني على اليمين.'),('Mi oficina está en el tercer piso.','مكتبي في الطابق الثالث.'),('Este es mi cuarto libro.','هذا كتابي الرابع.'),('Ella quedó en quinto lugar.','جاءت في المركز الخامس.'),('El primer día fue difícil.','كان اليوم الأول صعبًا.')],
 [('Vivo en el ___ piso.',['primer','primero','primera'],0,'Vivo en el primer piso.'),
  ('Es la ___ puerta a la derecha.',['segundo','segunda','segundos'],1,'Es la segunda puerta a la derecha.'),
  ('Mi oficina está en el ___ piso.',['tercer','tercero','tercera'],0,'Mi oficina está en el tercer piso.'),
  ('Este es mi ___ libro.',['cuarto','cuarta','cuatro'],0,'Este es mi cuarto libro.'),
  ('El ___ día fue difícil.',['primer','primera','primero'],0,'El primer día fue difícil.')])
