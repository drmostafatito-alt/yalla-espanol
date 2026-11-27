# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))

topic('c2-ser-estar-adj','Ser y estar: cambio de sentido','ser وestar وتغيّر المعنى',
 [('Algunos adjetivos cambian de significado según el verbo. Con ser hablamos del carácter o de una cualidad permanente. Con estar hablamos de un estado o de algo que cambia.','بعض الصفات يتغير معناها بحسب الفعل: مع ser نصف الطبع أو الصفة الدائمة، ومع estar نصف الحالة العارضة.'),
  ('Ser listo es ser inteligente, pero estar listo es estar preparado. Ser aburrido es ser poco interesante, y estar aburrido es sentir aburrimiento.','ser listo تعني ذكيًا، وestar listo تعني جاهزًا؛ وser aburrido تعني مملًّا، وestar aburrido تعني أشعر بالملل.')],
 {'nohl':1,'head':['','ser','estar'],'rows':[['listo','inteligente','preparado'],['aburrido','poco interesante','con aburrimiento'],['abierto','sociable','no cerrado'],['malo','de mala calidad','enfermo']]},
 [('Mi primo es muy listo.','ابن عمي ذكي جدًا.'),('La cena ya está lista.','العشاء جاهز الآن.'),('Este libro es aburrido.','هذا الكتاب مملّ.'),('Hoy estoy aburrido.','أنا اليوم أشعر بالملل.'),('El niño está malo.','الولد مريض.'),('La tienda está abierta.','المتجر مفتوح.')],
 [('Ana ___ muy lista; resuelve todo rápido.',['es','está','estaba'],0,'Ana es muy lista; resuelve todo rápido.'),
  ('¿Ya ___ lista la comida?',['es','está','son'],1,'¿Ya está lista la comida?'),
  ('Mi vecino ___ muy abierto con todos.',['es','está','fue'],0,'Mi vecino es muy abierto con todos.'),
  ('La puerta ___ abierta.',['es','está','fue'],1,'La puerta está abierta.'),
  ('Hoy no voy al colegio porque ___ malo.',['soy','estoy','estaré'],1,'Hoy no voy al colegio porque estoy malo.'),
  ('Esta película ___ muy aburrida.',['es','estás','estamos'],0,'Esta película es muy aburrida.')])

topic('c2-concesivas','Oraciones concesivas','الجمل التنازلية',
 [('Aunque, a pesar de que y aun cuando expresan una dificultad que no impide la acción. Con indicativo hablamos de un hecho real: Aunque estoy cansado, voy. Con subjuntivo, de algo posible o sin importancia: Aunque esté cansado, iré.','تعبّر عن عائق لا يمنع الفعل. مع المضارع المعتاد نتكلم عن واقع، ومع المنصوب عن احتمال أو أمر لا يهم.'),
  ('Por mucho que, por más que y por muy… que llevan subjuntivo: Por mucho que estudie, no lo entiende. Por muy difícil que sea, lo intentaré.','عبارات المبالغة مثل por mucho que وpor más que تأتي مع المضارع المنصوب.')],
 {'nohl':1,'head':['','conector','modo'],'rows':[['hecho real','aunque, a pesar de que','indicativo'],['posible','aunque, aun cuando','subjuntivo'],['intensidad','por mucho que, por más que','subjuntivo']]},
 [('Aunque estoy cansado, voy a la fiesta.','مع أنني متعب سأذهب إلى الحفلة.'),('Aunque esté cansado, iré a la fiesta.','حتى لو كنت متعبًا سأذهب إلى الحفلة.'),('A pesar de que llovía, salimos.','رغم أنها كانت تمطر خرجنا.'),('Por mucho que estudie, no lo entiende.','مهما درس فهو لا يفهمه.'),('Por más que lo intento, no puedo.','مهما حاولت لا أستطيع.'),('Aun cuando lo sepas, no lo digas.','حتى وإن كنت تعرفه فلا تقله.')],
 [('Por mucho que ___, no adelgaza.',['come','coma','comió'],1,'Por mucho que coma, no adelgaza.'),
  ('A pesar de que ___ frío, salimos.',['hacía','hiciera','haga'],0,'A pesar de que hacía frío, salimos.'),
  ('Aun cuando ___ la verdad, no hablaré.',['sé','sepa','supe'],1,'Aun cuando sepa la verdad, no hablaré.'),
  ('Aunque ya ___ las seis, sigue trabajando.',['son','sean','fueran'],0,'Aunque ya son las seis, sigue trabajando.'),
  ('Por muy difícil que ___, lo intentaré.',['es','sea','fue'],1,'Por muy difícil que sea, lo intentaré.')])

topic('c2-hendidas','Oraciones hendidas','الجمل المشقوقة للتأكيد',
 [('Para destacar una parte de la frase usamos ser + elemento + que, quien, donde o cuando: Fue Ana quien llamó. Es en Madrid donde vivo.','للتأكيد على جزء من الجملة نستعمل ser + العنصر + que أو quien أو donde أو cuando.'),
  ('El verbo ser sigue el tiempo de la acción: Fue ayer cuando lo vi. Con el sujeto en plural, usamos quienes: Fueron ellos quienes ganaron.','يتبع الفعل ser زمن الحدث، ومع الجمع نستعمل quienes.')],
 {'nohl':1,'head':['','neutra','hendida'],'rows':[['sujeto','Ana llamó.','Fue Ana quien llamó.'],['lugar','Vivo en Madrid.','Es en Madrid donde vivo.'],['tiempo','Lo vi ayer.','Fue ayer cuando lo vi.'],['objeto','Quiero agua.','Lo que quiero es agua.']]},
 [('Fue Ana quien llamó.','آنا هي التي اتصلت.'),('Es en Madrid donde vivo.','في مدريد أسكن.'),('Fue ayer cuando lo vi.','أمس هو الوقت الذي رأيته فيه.'),('Lo que quiero es agua.','ما أريده هو الماء.'),('Soy yo quien lo dice.','أنا من يقول ذلك.'),('Fueron ellos quienes ganaron.','هم الذين فازوا.')],
 [('___ Ana quien llamó.',['Fue','Fui','Fuimos'],0,'Fue Ana quien llamó.'),
  ('Lo que quiero ___ agua.',['es','son','fue'],0,'Lo que quiero es agua.'),
  ('Fueron ellos ___ ganaron.',['quien','quienes','donde'],1,'Fueron ellos quienes ganaron.'),
  ('Es aquí ___ trabajo.',['donde','quien','cuando'],0,'Es aquí donde trabajo.'),
  ('Fue ayer ___ lo vi.',['donde','cuando','quien'],1,'Fue ayer cuando lo vi.'),
  ('Soy yo ___ lo dice.',['quien','donde','cuando'],0,'Soy yo quien lo dice.')])

topic('c2-discurso','Conectores del discurso','أدوات الربط في الخطاب',
 [('Los conectores organizan las ideas. Sirven para añadir, contrastar, explicar la causa o concluir: además, sin embargo, ya que, por eso, en definitiva.','تنظّم أدوات الربط الأفكار: للإضافة والمقابلة وبيان السبب والاستنتاج.'),
  ('Suelen ir al principio de la frase o después de punto y coma, y llevan coma detrás: Estudió mucho; sin embargo, no aprobó.','تأتي غالبًا في بداية الجملة أو بعد فاصلة منقوطة، وتتبعها فاصلة.')],
 {'nohl':1,'head':['','conector','ejemplo'],'rows':[['añadir','además','Es rápido; además, es barato.'],['contrastar','sin embargo','Estudió; sin embargo, suspendió.'],['causa','ya que','Voy, ya que me invitaste.'],['consecuencia','por eso','Llovía; por eso, nos quedamos.']]},
 [('Es barato; además, es muy cómodo.','إنه رخيص؛ إضافةً إلى ذلك مريح جدًا.'),('Estudió mucho; sin embargo, no aprobó.','درس كثيرًا؛ ومع ذلك لم ينجح.'),('Iré, ya que me lo pediste.','سأذهب لأنك طلبت مني ذلك.'),('Llovía mucho; por eso, nos quedamos.','كانت تمطر كثيرًا؛ لذلك بقينا.'),('No obstante, el plan es bueno.','ومع ذلك فالخطة جيدة.'),('En definitiva, fue un buen viaje.','باختصار كانت رحلة جميلة.')],
 [('Estudió mucho; ___, no aprobó.',['por eso','sin embargo','además'],1,'Estudió mucho; sin embargo, no aprobó.'),
  ('Hacía mucho frío; ___, nos quedamos en casa.',['por eso','sin embargo','no obstante'],0,'Hacía mucho frío; por eso, nos quedamos en casa.'),
  ('Es barato; ___, es muy bonito.',['además','sin embargo','por consiguiente'],0,'Es barato; además, es muy bonito.'),
  ('Iré a la fiesta, ___ me invitaste.',['ya que','sin embargo','aunque'],0,'Iré a la fiesta, ya que me invitaste.'),
  ('Para terminar decimos: ___, fue un buen viaje.',['En definitiva','Sin embargo','Además'],0,'Para terminar decimos: En definitiva, fue un buen viaje.'),
  ('Hacía frío; ___, salimos a correr.',['por eso','no obstante','ya que'],1,'Hacía frío; no obstante, salimos a correr.')])

topic('c2-tiempo-idiomatico','Expresiones de tiempo','تعابير الزمن',
 [('Hay expresiones de tiempo muy frecuentes: de vez en cuando es a veces, cada dos por tres es muy a menudo, de repente es sin aviso, a la larga es con el tiempo.','هناك تعابير زمنية شائعة: de vez en cuando بمعنى أحيانًا، وcada dos por tres بمعنى كثيرًا جدًا، وde repente بمعنى فجأة، وa la larga بمعنى على المدى البعيد.'),
  ('Se usan con el tiempo verbal normal: De repente empezó a llover. A la larga, merece la pena.','وتُستعمل مع الأزمنة العادية للفعل.')],
 {'nohl':1,'head':['','expresión','ejemplo'],'rows':[['a veces','de vez en cuando','Voy al cine de vez en cuando.'],['muy a menudo','cada dos por tres','Pierde las llaves cada dos por tres.'],['sin aviso','de repente','De repente, se fue la luz.'],['con el tiempo','a la larga','A la larga, merece la pena.']]},
 [('Voy al cine de vez en cuando.','أذهب إلى السينما بين الحين والآخر.'),('Pierde las llaves cada dos por tres.','يضيّع المفاتيح كل لحظة.'),('De repente, se fue la luz.','فجأة انقطعت الكهرباء.'),('A la larga, merece la pena.','على المدى البعيد يستحق العناء.'),('Cambió de trabajo de un día para otro.','غيّر عمله بين ليلة وضحاها.'),('Hoy en día casi todos tienen móvil.','في أيامنا هذه يملك الجميع تقريبًا هاتفًا.')],
 [('Voy al gimnasio ___ en cuando.',['de vez','cada vez','a veces'],0,'Voy al gimnasio de vez en cuando.'),
  ('___, empezó a llover.',['De repente','De vez en cuando','A la larga'],0,'De repente, empezó a llover.'),
  ('Pierde el móvil cada ___ por tres.',['dos','uno','cien'],0,'Pierde el móvil cada dos por tres.'),
  ('A la ___, merece la pena.',['larga','corta','pronta'],0,'A la larga, merece la pena.'),
  ('Hoy en ___ casi todos tienen móvil.',['día','tiempo','hora'],0,'Hoy en día casi todos tienen móvil.'),
  ('Cambió de casa de un día para ___.',['otro','el otro','ayer'],0,'Cambió de casa de un día para otro.')])
