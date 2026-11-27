# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))

topic('a2-diminutivos','Diminutivos y superlativo en -ísimo','التصغير والصيغة المبالغة -ísimo',
 [('El diminutivo se forma con -ito o -ita: casa, casita; libro, librito. Si la palabra acaba en -e o en -n, suele llevar -cito: parque, parquecito; camión, camioncito. Expresa tamaño pequeño, cariño o cortesía.','يُصاغ التصغير بإضافة ito أو ita، وإذا انتهت الكلمة بـ e أو n فغالبًا تأخذ cito. ويدل على الصغر أو المودة أو اللطف.'),
  ('El superlativo absoluto se forma con -ísimo, -ísima: bueno, buenísimo; rico, riquísimo; grande, grandísimo. Significa muy, muy.','وتُصاغ صيغة المبالغة بإضافة ísimo أو ísima، وتعني «جدًا جدًا».')],
 {'nohl':1,'head':['','palabra','forma'],'rows':[['casa','casita','diminutivo'],['perro','perrito','diminutivo'],['parque','parquecito','diminutivo'],['rico','riquísimo','superlativo']]},
 [('Vivo en una casita pequeña.','أسكن في بيت صغير.'),('¿Quieres un cafecito?','هل تريد فنجان قهوة صغيرًا؟'),('Mi gatito es muy bueno.','قطي الصغير طيب جدًا.'),('Esta comida está riquísima.','هذا الطعام لذيذ جدًا.'),('Tu casa es grandísima.','بيتك كبير جدًا.'),('Hablamos un ratito, ¿vale?','نتحدث قليلًا، هل هذا مناسب؟')],
 [('Vivo en una ___ pequeña.',['casita','casísima','casa'],0,'Vivo en una casita pequeña.'),
  ('Esta comida está ___.',['riquísima','riquita','ricoísima'],0,'Esta comida está riquísima.'),
  ('Mi ___ es muy bueno. (gato)',['gatito','gatísimo','gato'],0,'Mi gatito es muy bueno.'),
  ('Tu casa es ___. (grande)',['grandísima','grandita','grandecita'],0,'Tu casa es grandísima.'),
  ('¿Quieres un ___? (café)',['cafecito','cafeito','cafito'],0,'¿Quieres un cafecito?')])

topic('a2-estar-participio','Estar + participio','estar + اسم المفعول',
 [('Con estar + participio expresamos el resultado de una acción. El participio concuerda con el sujeto: La puerta está cerrada. Los niños están dormidos.','نستعمل estar مع اسم المفعول لوصف نتيجة فعل، ويطابق اسم المفعول الفاعل في الجنس والعدد.'),
  ('También se usa con encontrarse y verse: Me encuentro cansado. Se vio obligado a salir. La acción es el proceso; el estado es el resultado: Abro la ventana, y ahora la ventana está abierta.','ويُستعمل أيضًا مع encontrarse وverse. الفعل هو العملية، والحال هي النتيجة.')],
 {'nohl':1,'head':['','acción','resultado'],'rows':[['cerrar','Cierro la puerta.','La puerta está cerrada.'],['abrir','Abro la ventana.','La ventana está abierta.'],['terminar','Termino el trabajo.','El trabajo está terminado.'],['dormir','Los niños duermen.','Los niños están dormidos.']]},
 [('La puerta está cerrada.','الباب مغلق.'),('La ventana está abierta.','النافذة مفتوحة.'),('El trabajo ya está terminado.','العمل منتهٍ بالفعل.'),('Los niños están dormidos.','الأطفال نائمون.'),('Las tiendas están cerradas hoy.','المتاجر مغلقة اليوم.'),('Me encuentro muy cansado.','أشعر بتعب شديد.')],
 [('La puerta está ___.',['cerrada','cerrado','cerrar'],0,'La puerta está cerrada.'),
  ('Las tiendas están ___ hoy.',['cerradas','cerrada','cerrados'],0,'Las tiendas están cerradas hoy.'),
  ('Los niños están ___.',['dormidos','dormido','durmiendo'],0,'Los niños están dormidos.'),
  ('El trabajo ya está ___.',['terminado','terminada','terminando'],0,'El trabajo ya está terminado.'),
  ('La ventana está ___.',['abierta','abierto','abrir'],0,'La ventana está abierta.')])

topic('a2-soler','Soler + infinitivo','soler + المصدر',
 [('Soler + infinitivo expresa una costumbre: Suelo levantarme a las siete. Solo se usa en presente y en imperfecto: suelo, solía.','تعبّر soler مع المصدر عن العادة، وتُستعمل في المضارع والماضي المستمر فقط.'),
  ('Soler es irregular como poder: o cambia a ue. También decimos lo normal es + infinitivo: Lo normal es cenar tarde.','وهي شاذة مثل poder، إذ تتحول o إلى ue. ونقول أيضًا lo normal es مع المصدر.')],
 {'nohl':1,'head':['','presente','imperfecto'],'rows':[['yo','suelo','solía'],['tú','sueles','solías'],['él','suele','solía'],['nosotros','solemos','solíamos']]},
 [('Suelo levantarme a las siete.','عادةً أستيقظ في السابعة.'),('Mis padres suelen cenar tarde.','والداي عادةً يتعشيان متأخرين.'),('Solemos viajar en verano.','عادةً نسافر في الصيف.'),('Antes solía jugar en el parque.','في الماضي كنت أعتاد اللعب في الحديقة.'),('¿Sueles comer fuera?','هل تعتاد الأكل خارج البيت؟'),('Lo normal es cenar a las nueve.','المعتاد أن نتعشى في التاسعة.')],
 [('Yo ___ levantarme a las siete.',['suelo','solo','sueño'],0,'Yo suelo levantarme a las siete.'),
  ('Mis padres ___ cenar tarde.',['suelen','soléis','suele'],0,'Mis padres suelen cenar tarde.'),
  ('Nosotros ___ viajar en verano.',['solemos','suelemos','suelen'],0,'Nosotros solemos viajar en verano.'),
  ('Antes ___ jugar en el parque.',['solía','suelo','suele'],0,'Antes solía jugar en el parque.'),
  ('¿___ comer fuera?',['Sueles','Soles','Solías a'],0,'¿Sueles comer fuera?')])

topic('a2-indefinidos','Alguien, nadie, algo y nada','alguien وnadie وalgo وnada',
 [('Alguien y nadie se refieren a personas; algo y nada, a cosas. No cambian de forma: ¿Hay alguien en casa? No hay nadie. ¿Quieres algo? No quiero nada.','تشير alguien وnadie إلى الأشخاص، وalgo وnada إلى الأشياء، ولا تتغير صيغها.'),
  ('Con nadie y nada, si van detrás del verbo, necesitamos no: No veo a nadie. Si van delante, no ponemos no: Nadie habla.','وإذا جاءت nadie أو nada بعد الفعل نضع no قبل الفعل، وإذا جاءت قبله فلا نضع no.')],
 {'nohl':1,'head':['','afirmativo','negativo'],'rows':[['persona','alguien','nadie'],['cosa','algo','nada'],['con verbo','Veo a alguien.','No veo a nadie.'],['delante','Algo pasa.','Nada pasa.']]},
 [('¿Hay alguien en casa?','هل يوجد أحد في البيت؟'),('No hay nadie en la oficina.','لا يوجد أحد في المكتب.'),('¿Quieres algo de beber?','هل تريد شيئًا لتشربه؟'),('No quiero nada, gracias.','لا أريد شيئًا، شكرًا.'),('Nadie sabe la respuesta.','لا أحد يعرف الجواب.'),('No conozco a nadie aquí.','لا أعرف أحدًا هنا.')],
 [('¿Hay ___ en casa?',['alguien','algo','nada'],0,'¿Hay alguien en casa?'),
  ('No quiero ___, gracias.',['nada','algo','alguien'],0,'No quiero nada, gracias.'),
  ('___ sabe la respuesta.',['Nadie','No nadie','Nada'],0,'Nadie sabe la respuesta.'),
  ('No conozco a ___ aquí.',['nadie','alguien','nada'],0,'No conozco a nadie aquí.'),
  ('¿Quieres ___ de beber?',['algo','nada','nadie'],0,'¿Quieres algo de beber?')])

topic('b1-opinion-creer','Creer que y no creer que','creer que وno creer que',
 [('Con creo que, pienso que y me parece que usamos indicativo: Creo que tiene razón.','مع creo que وpienso que وme parece que نستعمل صيغة الإخبار: Creo que tiene razón.'),
  ('Con no creo que y no pienso que usamos subjuntivo: No creo que tenga razón. La duda o la negación piden subjuntivo.','ومع no creo que وno pienso que نستعمل المضارع المنصوب، لأن الشك والنفي يتطلبانه.')],
 {'nohl':1,'head':['','indicativo','subjuntivo'],'rows':[['creer','Creo que viene.','No creo que venga.'],['pensar','Pienso que es bueno.','No pienso que sea bueno.'],['parecer','Me parece que sabe.','No me parece que sepa.'],['ser','Creo que es verdad.','No creo que sea verdad.']]},
 [('Creo que tiene razón.','أعتقد أنه محق.'),('No creo que tenga razón.','لا أعتقد أنه محق.'),('Pienso que el examen es fácil.','أظن أن الامتحان سهل.'),('No pienso que el examen sea fácil.','لا أظن أن الامتحان سهل.'),('Me parece que Ana viene hoy.','يبدو لي أن آنا تأتي اليوم.'),('No creo que Ana venga hoy.','لا أعتقد أن آنا تأتي اليوم.')],
 [('Creo que ___ razón.',['tiene','tenga','tuviera'],0,'Creo que tiene razón.'),
  ('No creo que ___ razón.',['tiene','tenga','tendrá'],1,'No creo que tenga razón.'),
  ('Pienso que el examen ___ fácil.',['es','sea','fuera'],0,'Pienso que el examen es fácil.'),
  ('No pienso que el examen ___ fácil.',['es','sea','será'],1,'No pienso que el examen sea fácil.'),
  ('No creo que Ana ___ hoy.',['viene','venga','vendrá'],1,'No creo que Ana venga hoy.')])

topic('b1-consejos','Dar consejos y recomendar','تقديم النصائح والتوصيات',
 [('Para dar un consejo usamos deberías + infinitivo, tendrías que + infinitivo o habría que + infinitivo: Deberías dormir más.','لتقديم نصيحة نستعمل deberías أو tendrías que أو habría que مع المصدر.'),
  ('Con recomendar, aconsejar y sugerir usamos que + presente de subjuntivo: Te recomiendo que vayas al médico. Si el sujeto es el mismo, usamos infinitivo: Te aconsejo descansar.','ومع recomendar وaconsejar وsugerir نستعمل que مع المضارع المنصوب. وإن كان الفاعل واحدًا استعملنا المصدر.')],
 {'nohl':1,'head':['','estructura','ejemplo'],'rows':[['deberías','+ infinitivo','Deberías dormir más.'],['tendrías que','+ infinitivo','Tendrías que descansar.'],['te recomiendo que','+ subjuntivo','Te recomiendo que vayas.'],['te aconsejo','+ infinitivo','Te aconsejo descansar.']]},
 [('Deberías dormir más.','ينبغي لك أن تنام أكثر.'),('Tendrías que ir al médico.','يجب عليك أن تذهب إلى الطبيب.'),('Te recomiendo que visites Sevilla.','أنصحك بأن تزور إشبيلية.'),('Te aconsejo que estudies más.','أنصحك بأن تدرس أكثر.'),('Te aconsejo descansar un poco.','أنصحك بأن ترتاح قليلًا.'),('Habría que hablar con el jefe.','ينبغي أن نتحدث مع المدير.')],
 [('___ dormir más.',['Deberías','Debes que','Debieras de'],0,'Deberías dormir más.'),
  ('Te recomiendo que ___ Sevilla.',['visites','visitas','visitar'],0,'Te recomiendo que visites Sevilla.'),
  ('Te aconsejo que ___ más.',['estudies','estudias','estudiar'],0,'Te aconsejo que estudies más.'),
  ('Te aconsejo ___ un poco.',['descansar','que descansar','descansas'],0,'Te aconsejo descansar un poco.'),
  ('Habría que ___ con el jefe.',['hablar','hablas','hable'],0,'Habría que hablar con el jefe.')])

topic('b1-condiciones-requisitos','Condiciones y requisitos','الشروط والمتطلبات',
 [('Con solo si, siempre que y siempre y cuando expresamos una condición necesaria. Llevan subjuntivo: Voy contigo siempre que tú conduzcas.','تعبّر solo si وsiempre que وsiempre y cuando عن شرط لازم، وتأتي مع المضارع المنصوب في أغلب الأحوال.'),
  ('Con a menos que, salvo que y en caso de que expresamos una excepción o una posibilidad. Llevan subjuntivo: Iremos, a menos que llueva. En caso de que llegues tarde, llámame.','وتعبّر a menos que وsalvo que وen caso de que عن استثناء أو احتمال، وتأتي مع المضارع المنصوب.')],
 {'nohl':1,'head':['','conector','ejemplo'],'rows':[['siempre que','+ subjuntivo','Voy si tú conduces.'],['solo si','+ indicativo o subjuntivo','Solo si me avisas.'],['a menos que','+ subjuntivo','Iremos, a menos que llueva.'],['en caso de que','+ subjuntivo','En caso de que llegues tarde.']]},
 [('Iremos, a menos que llueva.','سنذهب إلا إذا أمطرت.'),('Te presto el coche siempre que lo cuides.','أعيرك السيارة بشرط أن تعتني بها.'),('En caso de que llegues tarde, llámame.','إذا تأخرت، اتصل بي.'),('Saldremos salvo que haga mucho frío.','سنخرج إلا إذا كان البرد شديدًا.'),('Puedes venir siempre y cuando seas puntual.','يمكنك أن تأتي بشرط أن تكون دقيقًا في الموعد.'),('No saldré a menos que me llames.','لن أخرج ما لم تتصل بي.')],
 [('Iremos, a menos que ___.',['llueva','llueve','lloverá'],0,'Iremos, a menos que llueva.'),
  ('Te presto el coche siempre que lo ___.',['cuides','cuidas','cuidar'],0,'Te presto el coche siempre que lo cuides.'),
  ('En caso de que ___ tarde, llámame.',['llegues','llegas','llegarás'],0,'En caso de que llegues tarde, llámame.'),
  ('Saldremos salvo que ___ mucho frío.',['haga','hace','hará'],0,'Saldremos salvo que haga mucho frío.'),
  ('No saldré a menos que me ___.',['llames','llamas','llamarás'],0,'No saldré a menos que me llames.')])

topic('b1-se-involuntario','Se involuntario','se غير الإرادية',
 [('Para decir que algo ocurrió sin querer usamos se + me, te, le, nos, os, les + verbo. El verbo concuerda con la cosa: Se me ha caído el móvil. Se me han olvidado las llaves.','لنقول إن أمرًا حدث دون قصد نستعمل se مع الضمير me أو te أو le… ثم الفعل، ويطابق الفعل الشيء المتأثر.'),
  ('La persona no es la culpable: Se me olvidó la cita, no Olvidé la cita. Los verbos más frecuentes son caer, olvidar, perder, romper y acabar.','وفي هذا التركيب لا يُنسب الفعل إلى الشخص. وأكثر الأفعال استعمالًا: caer وolvidar وperder وromper وacabar.')],
 {'nohl':1,'head':['','singular','plural'],'rows':[['caer','Se me cae el vaso.','Se me caen los vasos.'],['olvidar','Se me olvida la cita.','Se me olvidan las citas.'],['perder','Se te ha perdido la llave.','Se te han perdido las llaves.'],['romper','Se nos rompió el plato.','Se nos rompieron los platos.']]},
 [('Se me ha caído el móvil.','سقط مني الهاتف.'),('Se me han olvidado las llaves.','نسيت المفاتيح.'),('Se nos rompió el plato.','انكسر منا الصحن.'),('Se te ha perdido la cartera.','ضاعت منك المحفظة.'),('Se le acabó la batería.','نفدت بطارية هاتفه.'),('Se me olvidó la cita.','نسيت الموعد.')],
 [('Se me ha ___ el móvil.',['caído','caído a','caer'],0,'Se me ha caído el móvil.'),
  ('Se me han ___ las llaves.',['olvidado','olvidada','olvidar'],0,'Se me han olvidado las llaves.'),
  ('Se nos ___ el plato.',['rompió','rompieron','rompí'],0,'Se nos rompió el plato.'),
  ('Se te ha ___ la cartera.',['perdido','perdida','perder'],0,'Se te ha perdido la cartera.'),
  ('Se le ___ la batería.',['acabó','acabé','acabaron'],0,'Se le acabó la batería.')])

topic('b2-como-si','Como si + subjuntivo','como si مع المضارع المنصوب',
 [('Como si introduce una comparación irreal. Va con imperfecto de subjuntivo cuando habla del presente: Habla como si fuera el jefe.','تقدّم como si مقارنة غير واقعية، وتأتي مع الماضي الافتراضي حين نتحدث عن الحاضر: Habla como si fuera el jefe.'),
  ('Con pluscuamperfecto de subjuntivo habla de algo anterior: Me miró como si no me hubiera visto nunca. Nunca lleva indicativo ni presente de subjuntivo.','ومع الماضي التام الافتراضي نتحدث عن أمر سابق. ولا تأتي بعدها صيغة الإخبار ولا المضارع المنصوب أبدًا.')],
 {'nohl':1,'head':['','tiempo','ejemplo'],'rows':[['presente','como si + imperfecto','Habla como si fuera el jefe.'],['pasado','como si + pluscuamperfecto','Me miró como si no me hubiera visto.'],['ser','fuera','como si fuera'],['tener','tuviera','como si tuviera']]},
 [('Habla como si fuera el jefe.','يتكلم كأنه المدير.'),('Me trata como si fuera un niño.','يعاملني كأنني طفل.'),('Corre como si tuviera prisa.','يركض كأن لديه عجلة.'),('Me miró como si no me hubiera visto nunca.','نظر إليّ كأنه لم يرني قط.'),('Gasta dinero como si fuera rico.','ينفق المال كأنه غني.'),('Hace como si no supiera nada.','يتصرف كأنه لا يعرف شيئًا.')],
 [('Habla como si ___ el jefe.',['fuera','es','sea'],0,'Habla como si fuera el jefe.'),
  ('Corre como si ___ prisa.',['tuviera','tiene','tenga'],0,'Corre como si tuviera prisa.'),
  ('Me trata como si ___ un niño.',['fuera','soy','sea'],0,'Me trata como si fuera un niño.'),
  ('Gasta dinero como si ___ rico.',['fuera','es','será'],0,'Gasta dinero como si fuera rico.'),
  ('Hace como si no ___ nada.',['supiera','sabe','sepa'],0,'Hace como si no supiera nada.')])

topic('b2-cuanto-mas','Cuanto más… más','كلما… ازداد',
 [('Con cuanto más… más expresamos que dos cosas aumentan a la vez: Cuanto más estudias, más aprendes. Para disminuir usamos cuanto menos… menos.','نعبّر بـ cuanto más… más عن أمرين يزدادان معًا. وللتناقص نقول cuanto menos… menos.'),
  ('También podemos mezclar: Cuanto más duermo, menos cansado estoy. Delante de un nombre, cuanto concuerda: Cuantos más amigos tienes, más fiestas hay.','ويمكن الخلط بينهما. وأمام الاسم تطابق cuanto الاسم في الجنس والعدد.')],
 {'nohl':1,'head':['','estructura','ejemplo'],'rows':[['más… más','sube y sube','Cuanto más estudias, más aprendes.'],['menos… menos','baja y baja','Cuanto menos comes, menos fuerza tienes.'],['más… menos','sube y baja','Cuanto más duermo, menos cansado estoy.'],['con nombre','concuerda','Cuantos más amigos, más fiestas.']]},
 [('Cuanto más estudias, más aprendes.','كلما درست أكثر تعلمت أكثر.'),('Cuanto más duermo, menos cansado estoy.','كلما نمت أكثر قلّ تعبي.'),('Cuanto menos comes, menos fuerza tienes.','كلما أكلت أقل قلّت قوتك.'),('Cuanto antes llegues, mejor.','كلما وصلت أبكر كان أفضل.'),('Cuantos más amigos tienes, más fiestas hay.','كلما زاد أصدقاؤك زادت الحفلات.'),('Cuanto más lo pienso, menos lo entiendo.','كلما فكرت فيه أكثر فهمته أقل.')],
 [('Cuanto más estudias, ___ aprendes.',['más','menos','mucho'],0,'Cuanto más estudias, más aprendes.'),
  ('Cuanto más duermo, ___ cansado estoy.',['menos','más','tan'],0,'Cuanto más duermo, menos cansado estoy.'),
  ('Cuanto ___ comes, menos fuerza tienes.',['menos','más','poco'],0,'Cuanto menos comes, menos fuerza tienes.'),
  ('Cuanto ___ llegues, mejor.',['antes','más','pronto'],0,'Cuanto antes llegues, mejor.'),
  ('Cuantos ___ amigos tienes, más fiestas hay.',['más','menos','mucho'],0,'Cuantos más amigos tienes, más fiestas hay.')])

topic('b2-ir-venir-llevar-traer','Ir y venir, llevar y traer','ir وvenir وllevar وtraer',
 [('Ir indica movimiento hacia un lugar lejos de quien habla: Voy al cine. Venir indica movimiento hacia quien habla o hacia el lugar donde está: ¿Vienes a mi casa?','تدل ir على الحركة بعيدًا عن المتكلم، وvenir على الحركة نحو المتكلم أو نحو المكان الذي هو فيه.'),
  ('Llevar es ir con algo hacia otro lugar: Llevo el libro a clase. Traer es venir con algo hacia aquí: Trae el libro a clase, por favor.','وllevar تعني الذهاب بشيء إلى مكان آخر، وtraer تعني المجيء بشيء إلى هنا.')],
 {'nohl':1,'head':['','alejarse','acercarse'],'rows':[['movimiento','ir','venir'],['con objeto','llevar','traer'],['ejemplo 1','Voy a tu casa.','Vengo a tu casa.'],['ejemplo 2','Llevo el pan.','Traigo el pan.']]},
 [('Mañana voy al cine con Ana.','غدًا أذهب إلى السينما مع آنا.'),('¿Vienes a mi casa esta noche?','هل تأتي إلى بيتي الليلة؟'),('Llevo el libro a clase.','آخذ الكتاب إلى الصف.'),('Trae el libro a clase, por favor.','أحضر الكتاب إلى الصف من فضلك.'),('Voy a llevar a los niños al colegio.','سآخذ الأطفال إلى المدرسة.'),('¿Puedes traerme un vaso de agua?','هل تستطيع أن تحضر لي كأس ماء؟')],
 [('¿___ a mi casa esta noche?',['Vienes','Vas','Traes'],0,'¿Vienes a mi casa esta noche?'),
  ('Mañana ___ al cine con Ana.',['voy','vengo','traigo'],0,'Mañana voy al cine con Ana.'),
  ('___ el libro a clase, por favor.',['Trae','Lleva','Ven'],0,'Trae el libro a clase, por favor.'),
  ('Voy a ___ a los niños al colegio.',['llevar','traer','venir'],0,'Voy a llevar a los niños al colegio.'),
  ('¿Puedes ___ un vaso de agua?',['traerme','llevarme','irme'],0,'¿Puedes traerme un vaso de agua?')])
