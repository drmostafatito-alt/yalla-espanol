# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))
def tb(head,rows): return {'nohl':1,'head':head,'rows':rows}

topic('a1-adjetivos','Adjetivos y nacionalidades','الصفات والجنسيات',
 [('El adjetivo concuerda con el nombre en género y número: una casa pequeña, dos casas pequeñas. Normalmente va después del nombre.','تطابق الصفة الاسم في الجنس والعدد، وتأتي عادةً بعد الاسم.'),
  ('Las nacionalidades en -o cambian a -a: chileno, chilena. Las que acaban en consonante añaden -a: español, española. Las que acaban en -e no cambian: canadiense. Bueno y malo pierden la -o delante de un nombre masculino: un buen amigo.','الجنسيات المنتهية بـ o تتحول إلى a، والمنتهية بحرف ساكن تضيف a، والمنتهية بـ e لا تتغير. وتفقد bueno وmalo حرف o قبل اسم مذكر مفرد.')],
 tb(['','masculino','femenino'],[['chileno','chileno','chilena'],['español','español','española'],['canadiense','canadiense','canadiense'],['bueno','un buen amigo','una buena amiga']]),
 [('Tengo una amiga chilena.','عندي صديقة تشيلية.'),('Mi profesor es español.','أستاذي إسباني.'),('Mi profesora es española.','أستاذتي إسبانية.'),('Ellos son canadienses.','هم كنديون.'),('Es un buen amigo.','هو صديق جيد.'),('Tengo dos casas pequeñas.','عندي بيتان صغيران.')],
 [('Tengo una amiga ___.',['chilena','chileno','chilenas'],0,'Tengo una amiga chilena.'),
  ('Es un ___ amigo.',['buen','bueno','buena'],0,'Es un buen amigo.'),
  ('Ellos son ___.',['canadienses','canadiense','canadienso'],0,'Ellos son canadienses.'),
  ('Mi profesora es ___.',['española','español','españoles'],0,'Mi profesora es española.'),
  ('Tengo dos casas ___.',['pequeñas','pequeña','pequeño'],0,'Tengo dos casas pequeñas.')])

topic('a2-todos-algunos','Todos, algunos, otro y ninguno','todos وalgunos وotro وninguno',
 [('Todo concuerda con el nombre: todos los alumnos, toda la clase. Algunos significa una parte: Algunos estudiantes no vinieron. Otro significa uno más o uno diferente: Quiero otro café.','تطابق todo الاسم، وتدل algunos على بعض من الكل، وتدل otro على واحد آخر.'),
  ('Alguno y ninguno pierden la -o delante de un nombre masculino singular: algún libro, ningún problema. Cualquiera pierde la -a delante del nombre: cualquier día.','تفقد alguno وninguno حرف o قبل الاسم المذكر المفرد، وتفقد cualquiera حرف a قبل الاسم.')],
 tb(['','forma','ejemplo'],[['todo','todos, todas','todos los alumnos'],['alguno','algún, algunos','algún libro'],['ninguno','ningún','ningún problema'],['cualquiera','cualquier','cualquier día']]),
 [('Todos los alumnos llegaron.','وصل جميع الطلاب.'),('Algunos estudiantes no vinieron.','بعض الطلاب لم يأتوا.'),('No tengo ningún problema.','ليست عندي أي مشكلة.'),('Necesito otro lápiz, por favor.','أحتاج إلى قلم رصاص آخر من فضلك.'),('Cualquier día es bueno.','أي يوم مناسب.'),('¿Tienes algún libro en español?','هل عندك كتاب بالإسبانية؟')],
 [('___ los alumnos llegaron.',['Todos','Todo','Toda'],0,'Todos los alumnos llegaron.'),
  ('___ estudiantes no vinieron.',['Algunos','Alguno','Algún'],0,'Algunos estudiantes no vinieron.'),
  ('No tengo ___ problema.',['ningún','ninguno','ninguna'],0,'No tengo ningún problema.'),
  ('Necesito ___ lápiz, por favor.',['otro','otra','otros'],0,'Necesito otro lápiz, por favor.'),
  ('___ día es bueno.',['Cualquier','Cualquiera','Cualesquiera'],0,'Cualquier día es bueno.')])

topic('a2-cuantificadores','Mucho, poco, bastante y demasiado','mucho وpoco وbastante وdemasiado',
 [('Mucho, poco, bastante, demasiado y suficiente concuerdan con el nombre: demasiada gente, pocos libros, suficientes sillas.','تطابق هذه الكلمات الاسم في الجنس والعدد: demasiada gente وpocos libros وsuficientes sillas.'),
  ('Con un verbo no cambian: Comes demasiado. Trabajo poco. Bastante significa un poco más de lo normal o suficiente.','ومع الفعل لا تتغير: Comes demasiado. Trabajo poco.')],
 tb(['','con nombre','con verbo'],[['demasiado','demasiada gente','Comes demasiado.'],['poco','poco tiempo','Trabajo poco.'],['bastante','bastantes sillas','Duermo bastante.'],['suficiente','suficientes libros','Estudio lo suficiente.']]),
 [('Hay demasiada gente aquí.','يوجد ناس كثيرون جدًا هنا.'),('Tengo poco tiempo.','عندي وقت قليل.'),('No tienes suficientes libros.','ليست عندك كتب كافية.'),('Comes demasiado.','تأكل أكثر من اللازم.'),('Hay bastantes sillas.','توجد كراسٍ كافية.'),('Hoy hay poca gente.','اليوم الناس قليلون.')],
 [('Hay ___ gente aquí.',['demasiada','demasiado','demasiados'],0,'Hay demasiada gente aquí.'),
  ('Tengo ___ tiempo.',['poco','poca','pocos'],0,'Tengo poco tiempo.'),
  ('No tienes ___ libros.',['suficientes','suficiente','suficienta'],0,'No tienes suficientes libros.'),
  ('Comes ___.',['demasiado','demasiada','demasiados'],0,'Comes demasiado.'),
  ('Hay ___ sillas.',['bastantes','bastante','bastanta'],0,'Hay bastantes sillas.')])

topic('a1-articulo-usos','Usos del artículo definido','استعمالات أداة التعريف',
 [('Usamos el artículo definido con los días, las horas y las fechas: el lunes, las cinco, el seis de enero. También con instrumentos y deportes: tocar la guitarra, jugar al fútbol.','نستعمل أداة التعريف مع الأيام والساعات والتواريخ، ومع الآلات الموسيقية والرياضات.'),
  ('Con los títulos usamos el artículo si hablamos de la persona: El señor Alonso no está. Si hablamos con ella, no: Señor Alonso, ¿cómo está? Con una profesión después de ser no usamos artículo: Soy médico.','ومع الألقاب نستعمل الأداة حين نتحدث عن الشخص، ولا نستعملها حين نخاطبه. ومع المهنة بعد ser لا نستعمل أداة.')],
 tb(['','con artículo','sin artículo'],[['día','El lunes tengo clase.',''],['música','Toco la guitarra.',''],['título','El señor Alonso no está.','Señor Alonso, ¿cómo está?'],['profesión','','Soy médico.']]),
 [('Toco la guitarra.','أعزف الغيتار.'),('El lunes tengo clase.','يوم الإثنين عندي حصة.'),('Juego al fútbol los sábados.','ألعب كرة القدم أيام السبت.'),('El señor Alonso no está.','السيد ألونسو غير موجود.'),('Soy médico.','أنا طبيب.'),('Son las cinco de la tarde.','الساعة الخامسة مساءً.')],
 [('Toco ___ guitarra.',['la','una','el'],0,'Toco la guitarra.'),
  ('___ lunes tengo clase.',['El','Un','En'],0,'El lunes tengo clase.'),
  ('Juego ___ fútbol los sábados.',['al','el','en'],0,'Juego al fútbol los sábados.'),
  ('___ señor Alonso no está.',['El','Un','Al'],0,'El señor Alonso no está.'),
  ('Son ___ cinco de la tarde.',['las','los','unas'],0,'Son las cinco de la tarde.')])

topic('a1-pronombres-preposicion','Pronombres con preposición','الضمائر بعد حروف الجر',
 [('Después de una preposición usamos mí, ti, él, ella, nosotros, vosotros, ellos: para mí, para ti, con ellos. Solo mí y ti son diferentes de los pronombres de sujeto.','بعد حرف الجر نستعمل mí وti وél… وهما الوحيدان المختلفان عن ضمائر الفاعل.'),
  ('Con yo y tú usamos formas especiales: conmigo y contigo. No decimos con mí ni con ti. Después de entre y según se usa tú y yo: entre tú y yo.','ومع yo وtú نقول conmigo وcontigo، ولا نقول con mí ولا con ti.')],
 tb(['','sujeto','con preposición'],[['yo','yo','para mí'],['tú','tú','para ti'],['con yo','','conmigo'],['con tú','','contigo']]),
 [('Este regalo es para ti.','هذه الهدية لك.'),('Ven conmigo al cine.','تعال معي إلى السينما.'),('Voy contigo.','سأذهب معك.'),('Pienso mucho en ti.','أفكر فيك كثيرًا.'),('Esto es para mí.','هذا لي.'),('Vivo con ellos.','أسكن معهم.')],
 [('Este regalo es para ___.',['ti','tú','te'],0,'Este regalo es para ti.'),
  ('Ven ___ al cine.',['conmigo','con mí','con yo'],0,'Ven conmigo al cine.'),
  ('Voy ___.',['contigo','con ti','con tú'],0,'Voy contigo.'),
  ('Pienso mucho en ___.',['ti','tú','te'],0,'Pienso mucho en ti.'),
  ('Esto es para ___.',['mí','yo','me'],0,'Esto es para mí.')])

topic('a1-numeros-cardinales','Números cardinales','الأعداد الأصلية',
 [('De 31 a 99 usamos y: treinta y uno, cuarenta y cinco. Delante de un nombre, uno pierde la -o: treinta y un años. Cien se usa solo; con otro número usamos ciento: ciento diez.','من 31 إلى 99 نضع y بين العشرات والآحاد. وتفقد uno حرف o أمام الاسم. ونقول cien وحدها، وciento مع بقية الأعداد.'),
  ('Los cientos concuerdan con el nombre: doscientas sillas, trescientos euros. Mil no cambia: dos mil. Con millón usamos de: un millón de personas.','وتطابق المئات الاسم: doscientas sillas. أما mil فلا تتغير. ومع millón نضع de.')],
 tb(['','número','cifra'],[['treinta y uno','treinta y un años','31'],['cien','cien personas','100'],['ciento diez','ciento diez personas','110'],['doscientos','doscientas sillas','200']]),
 [('Tengo treinta y un años.','عمري واحد وثلاثون عامًا.'),('Hay cien personas.','يوجد مئة شخص.'),('Hay ciento diez personas.','يوجد مئة وعشرة أشخاص.'),('Compré doscientas sillas.','اشتريت مئتي كرسي.'),('Mil euros no es mucho dinero.','ألف يورو ليست مبلغًا كبيرًا.'),('En la ciudad viven un millón de personas.','يعيش في المدينة مليون شخص.')],
 [('Tengo treinta y ___ años.',['un','uno','una'],0,'Tengo treinta y un años.'),
  ('Hay ___ personas.',['cien','ciento','cientos'],0,'Hay cien personas.'),
  ('Hay ___ diez personas.',['ciento','cien','cientos'],0,'Hay ciento diez personas.'),
  ('Compré ___ sillas.',['doscientas','doscientos','doscientas de'],0,'Compré doscientas sillas.'),
  ('Viven un millón ___ personas.',['de','en','con'],0,'Viven un millón de personas.')])

topic('a2-prep-tiempo','Preposiciones de tiempo','حروف الجر الزمنية',
 [('Usamos a con la hora: a las cinco. Usamos por con partes del día: por la mañana, por la tarde, por la noche. Usamos en con meses, estaciones y años: en enero, en verano, en 2020.','نستعمل a مع الساعة، وpor مع أجزاء اليوم، وen مع الأشهر والفصول والسنوات.'),
  ('Para un periodo usamos de… a… o desde… hasta…: de lunes a viernes, desde las nueve hasta las cinco.','وللمدة نستعمل de… a… أو desde… hasta….')],
 tb(['','preposición','ejemplo'],[['hora','a','a las cinco'],['parte del día','por','por la mañana'],['mes, estación, año','en','en verano'],['periodo','de… a…','de lunes a viernes']]),
 [('La clase empieza a las cinco.','تبدأ الحصة في الخامسة.'),('Estudio por la mañana.','أدرس في الصباح.'),('Nací en verano.','وُلدت في الصيف.'),('Trabajo de lunes a viernes.','أعمل من الإثنين إلى الجمعة.'),('Trabajo desde las nueve hasta las cinco.','أعمل من التاسعة حتى الخامسة.'),('Nos vemos en enero.','نلتقي في يناير.')],
 [('La clase empieza ___ las cinco.',['a','en','por'],0,'La clase empieza a las cinco.'),
  ('Estudio ___ la mañana.',['por','a','en'],0,'Estudio por la mañana.'),
  ('Nací ___ verano.',['en','por','a'],0,'Nací en verano.'),
  ('Trabajo de lunes ___ viernes.',['a','en','por'],0,'Trabajo de lunes a viernes.'),
  ('Trabajo desde las nueve ___ las cinco.',['hasta','por','en'],0,'Trabajo desde las nueve hasta las cinco.')])

topic('a2-adverbios-lugar-tiempo','Adverbios de lugar y de tiempo','ظروف المكان والزمان',
 [('Los adverbios de lugar no cambian: aquí está cerca de mí, ahí cerca de ti y allí lejos de los dos. También: arriba, abajo, dentro, fuera, delante, detrás.','ظروف المكان لا تتغير: aquí قريب مني، وahí قريب منك، وallí بعيد عنا. ومنها arriba وabajo وdentro وfuera.'),
  ('De tiempo: hoy, ayer, mañana, luego, entonces. Ya significa que algo ocurrió o ocurre: Ya terminé. Todavía no significa que aún no ocurrió: Todavía no he comido.','ومن ظروف الزمان: hoy وayer وmañana وluego. وتدل ya على حدوث الفعل، وtodavía no على أنه لم يحدث بعد.')],
 tb(['','adverbio','ejemplo'],[['lugar','aquí, ahí, allí','Mi casa está aquí.'],['lugar','arriba, abajo','Los libros están arriba.'],['tiempo','ayer, hoy, luego','Ayer fui al médico.'],['tiempo','ya, todavía no','Todavía no he comido.']]),
 [('Mi casa está aquí.','بيتي هنا.'),('Los libros están arriba.','الكتب في الأعلى.'),('Ayer fui al médico.','ذهبت أمس إلى الطبيب.'),('Luego te llamo.','سأتصل بك لاحقًا.'),('Todavía no he comido.','لم آكل بعد.'),('Ya terminé el trabajo.','لقد أنهيت العمل.')],
 [('Mi casa está ___.',['aquí','ayer','luego'],0,'Mi casa está aquí.'),
  ('Los libros están ___.',['arriba','hoy','ya'],0,'Los libros están arriba.'),
  ('___ fui al médico.',['Ayer','Mañana','Allí'],0,'Ayer fui al médico.'),
  ('___ te llamo.',['Luego','Ayer','Allí'],0,'Luego te llamo.'),
  ('___ no he comido.',['Todavía','Ya','Ayer'],0,'Todavía no he comido.')])

topic('a2-tambien-tampoco','También, tampoco y nunca','también وtampoco وnunca',
 [('Para estar de acuerdo con una frase afirmativa decimos también: Yo también soy estudiante. Con una frase negativa decimos tampoco: Yo tampoco hablo francés.','للموافقة على جملة مثبتة نقول también، وعلى جملة منفية نقول tampoco.'),
  ('Nunca y jamás son negativas. Si van delante del verbo, no usamos no: Nunca como carne. Si van detrás, usamos no: No he estado nunca en Roma.','وnunca وjamás للنفي. إن جاءتا قبل الفعل فلا نضع no، وإن جاءتا بعده وضعنا no.')],
 tb(['','afirmativo','negativo'],[['coincidencia','también','tampoco'],['siempre','siempre','nunca'],['delante','Nunca como carne.',''],['detrás','','No he estado nunca en Roma.']]),
 [('Yo también soy estudiante.','أنا أيضًا طالب.'),('Yo tampoco hablo francés.','أنا أيضًا لا أتكلم الفرنسية.'),('A mí también me gusta el café.','وأنا أيضًا أحب القهوة.'),('Nunca como carne.','لا آكل اللحم أبدًا.'),('No he estado nunca en Roma.','لم أذهب إلى روما قط.'),('Jamás he visto algo así.','لم أرَ شيئًا كهذا قط.')],
 [('Yo ___ soy estudiante.',['también','tampoco','nunca'],0,'Yo también soy estudiante.'),
  ('Yo ___ hablo francés.',['tampoco','también','siempre'],0,'Yo tampoco hablo francés.'),
  ('___ como carne.',['Nunca','Siempre no','También'],0,'Nunca como carne.'),
  ('No he estado ___ en Roma.',['nunca','siempre','ya'],0,'No he estado nunca en Roma.'),
  ('Jamás he ___ algo así.',['visto','ver','veo'],0,'Jamás he visto algo así.')])

topic('a2-conjunciones','Conjunciones: y, o, pero, sino','أدوات العطف: y وo وpero وsino',
 [('Y une cosas parecidas: pan y queso. Delante de i o hi, y cambia a e: padre e hijo. O une alternativas: té o café. Delante de o u ho, o cambia a u: siete u ocho.','تربط y بين أمور متشابهة، وتصبح e قبل i أو hi. وتعبّر o عن البدائل، وتصبح u قبل o أو ho.'),
  ('Pero expresa contraste: Quiero ir, pero no puedo. Sino corrige una frase negativa: No es rojo, sino azul.','وتعبّر pero عن التعارض، وتُستعمل sino لتصحيح جملة منفية.')],
 tb(['','conjunción','ejemplo'],[['y / e','padre e hijo','Padre e hijo viven aquí.'],['o / u','siete u ocho','Tengo siete u ocho libros.'],['pero','contraste','Quiero ir, pero no puedo.'],['sino','corrección','No es rojo, sino azul.']]),
 [('Padre e hijo viven aquí.','الأب والابن يسكنان هنا.'),('Tengo siete u ocho libros.','عندي سبعة أو ثمانية كتب.'),('Quiero ir, pero no puedo.','أريد الذهاب لكنني لا أستطيع.'),('No es rojo, sino azul.','ليس أحمر بل أزرق.'),('Como pan y queso.','آكل الخبز والجبن.'),('¿Prefieres leche o agua?','هل تفضّل الحليب أم الماء؟')],
 [('Padre ___ hijo viven aquí.',['e','y','o'],0,'Padre e hijo viven aquí.'),
  ('Tengo siete ___ ocho libros.',['u','o','e'],0,'Tengo siete u ocho libros.'),
  ('Quiero ir, ___ no puedo.',['pero','sino','y'],0,'Quiero ir, pero no puedo.'),
  ('No es rojo, ___ azul.',['sino','pero','y'],0,'No es rojo, sino azul.'),
  ('Como pan ___ queso.',['y','e','u'],0,'Como pan y queso.')])

topic('b1-quizas-ojala','Quizás, tal vez y ojalá','quizás وtal vez وojalá',
 [('Quizás y tal vez expresan duda. Con subjuntivo, la duda es mayor: Quizás llueva mañana. Con indicativo, la persona está más segura: Quizás tiene razón.','تعبّر quizás وtal vez عن الاحتمال. ومع المضارع المنصوب يكون الشك أكبر، ومع صيغة الإخبار يكون أقل.'),
  ('Ojalá expresa un deseo y siempre lleva subjuntivo: Ojalá tengas suerte. Con imperfecto de subjuntivo el deseo es poco probable: Ojalá pudiera viajar más.','وتعبّر ojalá عن أمنية، وتأتي دائمًا مع المضارع المنصوب. ومع الماضي الافتراضي تكون الأمنية بعيدة الحدوث.')],
 tb(['','estructura','ejemplo'],[['quizás','+ subjuntivo','Quizás llueva mañana.'],['tal vez','+ subjuntivo','Tal vez Ana venga hoy.'],['ojalá','+ presente','Ojalá tengas suerte.'],['ojalá','+ imperfecto','Ojalá pudiera viajar más.']]),
 [('Quizás llueva mañana.','ربما تمطر غدًا.'),('Tal vez Ana venga hoy.','ربما تأتي آنا اليوم.'),('Ojalá tengas suerte.','أتمنى لك الحظ.'),('Ojalá apruebes el examen.','أتمنى أن تنجح في الامتحان.'),('Ojalá pudiera viajar más.','ليتني أستطيع السفر أكثر.'),('Quizás vayamos al cine.','ربما نذهب إلى السينما.')],
 [('Quizás ___ mañana.',['llueva','llueve','lloverá'],0,'Quizás llueva mañana.'),
  ('Tal vez Ana ___ hoy.',['venga','viene','vendrá'],0,'Tal vez Ana venga hoy.'),
  ('Ojalá ___ suerte.',['tengas','tienes','tendrás'],0,'Ojalá tengas suerte.'),
  ('Ojalá ___ el examen.',['apruebes','apruebas','aprobarás'],0,'Ojalá apruebes el examen.'),
  ('Ojalá ___ viajar más.',['pudiera','puedo','podré'],0,'Ojalá pudiera viajar más.')])

topic('a2-acentuacion','Reglas de acentuación','قواعد وضع علامة التشديد',
 [('Las palabras agudas llevan el acento en la última sílaba y tienen tilde si acaban en vocal, n o s: café, canción, inglés. Las llanas llevan el acento en la penúltima sílaba y tienen tilde si no acaban en vocal, n ni s: árbol, fácil.','الكلمات الحادّة ينصبّ نبرها على المقطع الأخير، وتحمل علامة إن انتهت بحرف علة أو n أو s. والكلمات الرزينة ينصبّ نبرها على ما قبل الأخير، وتحمل علامة إن لم تنتهِ بحرف علة ولا n ولا s.'),
  ('Las esdrújulas llevan el acento en la antepenúltima sílaba y siempre tienen tilde: médico, teléfono. Una palabra como casa es llana y acaba en vocal, así que no lleva tilde.','والكلمات الإسدرُخولا ينصبّ نبرها على المقطع الثالث من الآخر، وتحمل العلامة دائمًا: médico وteléfono. أما casa فرزينة وتنتهي بحرف علة فلا علامة عليها.')],
 tb(['','acento','ejemplo'],[['aguda','última sílaba','café, canción'],['llana','penúltima sílaba','árbol, casa'],['esdrújula','antepenúltima','médico, teléfono'],['regla','siempre tilde','médico']]),
 [('La palabra café es aguda.','كلمة café حادّة.'),('La palabra árbol es llana.','كلمة árbol رزينة.'),('La palabra teléfono es esdrújula.','كلمة teléfono إسدرُخولا.'),('La palabra canción lleva tilde.','كلمة canción تحمل علامة.'),('La palabra casa no lleva tilde.','كلمة casa لا تحمل علامة.'),('La palabra inglés lleva tilde.','كلمة inglés تحمل علامة.')],
 [('La palabra ___ es aguda.',['café','cafe','cáfe'],0,'La palabra café es aguda.'),
  ('La palabra ___ es llana.',['árbol','arbol','arból'],0,'La palabra árbol es llana.'),
  ('La palabra ___ es esdrújula.',['teléfono','telefono','telefóno'],0,'La palabra teléfono es esdrújula.'),
  ('La palabra ___ lleva tilde.',['canción','cancion','cancíon'],0,'La palabra canción lleva tilde.'),
  ('La palabra ___ no lleva tilde.',['casa','cása','casá'],0,'La palabra casa no lleva tilde.')])

topic('b2-voseo','El voseo','التخاطب بـ vos',
 [('En muchos países de América se usa vos en lugar de tú: Argentina, Uruguay y partes de Centroamérica. El presente cambia: vos hablás, vos comés, vos vivís. El verbo ser es vos sos.','يُستعمل vos بدل tú في كثير من دول أمريكا اللاتينية، مثل الأرجنتين وأوروغواي. ويتغير المضارع: hablás وcomés وvivís، ويصبح ser: sos.'),
  ('En el imperativo se quita la -d del vosotros: hablá, comé, viví, vení. En España no se usa el voseo.','وفي الأمر تُحذف d من صيغة vosotros: hablá وcomé وviví وvení. ولا يُستعمل voseo في إسبانيا.')],
 tb(['','tú','vos'],[['hablar','hablas','hablás'],['tener','tienes','tenés'],['ser','eres','sos'],['venir (imperativo)','ven','vení']]),
 [('Vos sos de Argentina.','أنت من الأرجنتين.'),('¿Querés venir conmigo?','هل تريد أن تأتي معي؟'),('Vos tenés razón.','أنت محق.'),('Vení acá, por favor.','تعال إلى هنا من فضلك.'),('Vos hablás muy bien.','أنت تتكلم جيدًا جدًا.'),('Comé algo.','كُل شيئًا.')],
 [('¿De dónde ___? (vos)',['sos','eres','es'],0,'¿De dónde sos?'),
  ('Vos ___ razón.',['tenés','tienes','tengo'],0,'Vos tenés razón.'),
  ('¿___ venir conmigo? (vos)',['Querés','Quieres','Quiere'],0,'¿Querés venir conmigo?'),
  ('___ acá, por favor. (vos)',['Vení','Ven','Viene'],0,'Vení acá, por favor.'),
  ('Vos ___ muy bien.',['hablás','hablas','habla'],0,'Vos hablás muy bien.')])
