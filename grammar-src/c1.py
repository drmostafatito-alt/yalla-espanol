# -*- coding: utf-8 -*-
T=[]
def topic(id,es,ar,rule,table,ex,exe):
    T.append(dict(id=id,es=es,ar=ar,rule=rule,table=table,ex=ex,exe=exe))

topic('c1-futuro-probabilidad','Futuro y condicional de probabilidad','المستقبل والشرطي للتخمين',
 [('El futuro simple sirve para suponer algo en el presente: Serán las ocho. Con el futuro compuesto suponemos algo que ya pasó: Habrá llegado ya.','يُستعمل المستقبل البسيط لافتراض أمر في الحاضر، والمستقبل التام لافتراض أمر انتهى.'),
  ('El condicional hace lo mismo cuando hablamos del pasado: Serían las nueve cuando salió. Habría perdido el tren.','ويؤدي الشرطي المعنى نفسه حين نتحدث عن الماضي.')],
 {'nohl':1,'head':['','presente','pasado'],'rows':[['futuro','Estará en casa.','Habrá llegado ya.'],['condicional','Estaría en casa.','Habría llegado ya.']]},
 [('Serán las ocho.','لعلها الثامنة.'),('Ahora estará durmiendo.','لعله نائم الآن.'),('Habrá perdido el tren.','لعله فاته القطار.'),('Tendrá unos treinta años.','عمره نحو ثلاثين سنة على ما أظن.'),('Serían las nueve cuando llegó.','كانت الساعة نحو التاسعة حين وصل.'),('No contestó; estaría ocupado.','لم يجب؛ ربما كان مشغولًا.')],
 [('Ahora mismo ___ en la oficina.',['estará','estuvo','estaría'],0,'Ahora mismo estará en la oficina.'),
  ('Ya no está; ___ salido.',['habrá','habré','hubo'],0,'Ya no está; habrá salido.'),
  ('Cuando lo vi, ___ unos veinte años.',['tendrá','tendría','tuvo'],1,'Cuando lo vi, tendría unos veinte años.'),
  ('Son las tres; ___ comiendo.',['estarán','estaban','estarían'],0,'Son las tres; estarán comiendo.'),
  ('No contestó el teléfono; ___ durmiendo.',['estará','estaría','estuvo'],1,'No contestó el teléfono; estaría durmiendo.'),
  ('Hoy no ha venido; ___ enfermo.',['estará','estaría','estaba'],0,'Hoy no ha venido; estará enfermo.')])

topic('c1-subj-perfecto','Subjuntivo perfecto y pluscuamperfecto','المضارع المنصوب التام والماضي البعيد المنصوب',
 [('Pretérito perfecto de subjuntivo: haya, hayas, haya, hayamos, hayáis, hayan + participio. Lo usamos para una acción terminada: Espero que hayas dormido bien.','المضارع المنصوب التام: haya وتصريفاتها مع اسم المفعول، ويدل على فعل مكتمل.'),
  ('Pluscuamperfecto de subjuntivo: hubiera + participio. Lo usamos para lo irreal en el pasado: Ojalá hubiera venido. Si lo hubiera sabido, te habría avisado.','الماضي البعيد المنصوب: hubiera مع اسم المفعول، ويدل على ما لم يحدث في الماضي.')],
 {'head':['','perfecto','pluscuamperfecto'],'rows':[['yo','haya hablado','hubiera hablado'],['tú','hayas hablado','hubieras hablado'],['él / ella','haya hablado','hubiera hablado'],['nosotros','hayamos hablado','hubiéramos hablado'],['vosotros','hayáis hablado','hubierais hablado'],['ellos','hayan hablado','hubieran hablado']]},
 [('Espero que hayas dormido bien.','آمل أنك نمت جيدًا.'),('Es posible que ya hayan llegado.','من الممكن أنهم وصلوا بالفعل.'),('No creo que lo haya visto.','لا أظن أنه رآه.'),('Ojalá hubiera venido más gente.','يا ليت جاء ناس أكثر.'),('Me alegro de que hayas aprobado.','يسعدني أنك نجحت.'),('Si lo hubiera sabido, te habría avisado.','لو علمت لأخبرتك.')],
 [('Me alegro de que tú ___ aprobado.',['has','hayas','hubieras'],1,'Me alegro de que tú hayas aprobado.'),
  ('No creo que ellos ya ___ salido.',['han','hayan','hubieran'],1,'No creo que ellos ya hayan salido.'),
  ('Ojalá ___ más tiempo ayer.',['tengo','hubiera tenido','haya tenido'],1,'Ojalá hubiera tenido más tiempo ayer.'),
  ('Si ___ estudiado, habrías aprobado.',['has','hubieras','habrías'],1,'Si hubieras estudiado, habrías aprobado.'),
  ('Es posible que mi hermano ___ perdido las llaves.',['ha','haya','hubo'],1,'Es posible que mi hermano haya perdido las llaves.'),
  ('Dudo que ellos ___ terminado todavía.',['hayan','han','habrán'],0,'Dudo que ellos hayan terminado todavía.')])

topic('c1-relativas-subj','Relativas con subjuntivo','جمل الصلة مع المضارع المنصوب',
 [('Si la persona o la cosa existe y la conocemos, usamos indicativo: Tengo un amigo que habla ruso.','إذا كان الشخص أو الشيء موجودًا ومعروفًا نستعمل المضارع المعتاد.'),
  ('Si no sabemos si existe, o buscamos algo que quizá no exista, usamos subjuntivo: Busco un amigo que hable ruso. No hay nadie que lo sepa.','وإذا لم نعرف هل هو موجود، أو نفينا وجوده، نستعمل المضارع المنصوب.')],
 {'nohl':1,'head':['','indicativo','subjuntivo'],'rows':[['existe','Tengo un libro que explica todo.','Busco un libro que explique todo.'],['negación','Hay alguien que sabe.','No hay nadie que sepa.'],['pregunta','Conozco a alguien que vive aquí.','¿Conoces a alguien que viva aquí?']]},
 [('Busco un piso que tenga balcón.','أبحث عن شقة فيها شرفة.'),('Tengo un piso que tiene balcón.','عندي شقة فيها شرفة.'),('No hay nadie que lo sepa.','لا يوجد من يعرف ذلك.'),('Necesito una persona que hable inglés.','أحتاج إلى شخص يتحدث الإنجليزية.'),('Conozco a alguien que vive en Sevilla.','أعرف شخصًا يسكن في إشبيلية.'),('¿Hay alguien que pueda ayudarme?','هل من أحد يستطيع مساعدتي؟')],
 [('Busco una casa que ___ jardín.',['tiene','tenga','tuvo'],1,'Busco una casa que tenga jardín.'),
  ('Tengo un vecino que ___ la guitarra.',['toca','toque','tocara'],0,'Tengo un vecino que toca la guitarra.'),
  ('No conozco a nadie que ___ chino.',['habla','hable','hablaba'],1,'No conozco a nadie que hable chino.'),
  ('Busco un coche que ___ barato.',['es','sea','fue'],1,'Busco un coche que sea barato.'),
  ('Vivo en una calle que ___ muy tranquila.',['es','sea','fuera'],0,'Vivo en una calle que es muy tranquila.'),
  ('Necesito un médico que ___ de noche.',['trabaja','trabaje','trabajó'],1,'Necesito un médico que trabaje de noche.')])

topic('c1-gerundio-participio','Gerundio y participio absoluto','الحال والمشتق في بداية الجملة',
 [('El gerundio puede expresar modo, condición o algo que pasa a la vez: Salió corriendo. Practicando cada día, mejorarás.','قد يعبّر الحال (gerundio) عن الكيفية أو الشرط أو حدث متزامن.'),
  ('El participio absoluto presenta algo ya terminado antes de la acción principal: Terminada la clase, salimos. Dicho esto, se fue.','ويعرض اسم المفعول المستقل حدثًا انتهى قبل الفعل الرئيسي.')],
 {'nohl':1,'head':['','forma','ejemplo'],'rows':[['modo','gerundio','Salió corriendo.'],['condición','gerundio','Practicando, mejorarás.'],['antes','participio','Terminada la clase, salimos.']]},
 [('Salió de casa corriendo.','خرج من البيت يركض.'),('Practicando cada día, mejorarás.','بالتمرين كل يوم ستتحسن.'),('Terminada la clase, salimos al patio.','بعد انتهاء الدرس خرجنا إلى الساحة.'),('Dicho esto, se fue.','بعد أن قال هذا ذهب.'),('Ana volvió a casa cantando.','عادت آنا إلى البيت وهي تغني.'),('Hecho el trabajo, descansamos.','بعد إنجاز العمل استرحنا.')],
 [('___ cada día, mejorarás.',['Practicando','Practicado','Practicar'],0,'Practicando cada día, mejorarás.'),
  ('___ la cena, nos fuimos a dormir.',['Terminando','Terminada','Terminar'],1,'Terminada la cena, nos fuimos a dormir.'),
  ('Llegó a casa ___.',['corriendo','corrido','correr'],0,'Llegó a casa corriendo.'),
  ('Vi a mi hermano ___ del banco.',['saliendo','salido','salgo'],0,'Vi a mi hermano saliendo del banco.'),
  ('Dicho esto, ___ de la sala.',['salió','saliendo','salido'],0,'Dicho esto, salió de la sala.')])

topic('c1-registro','Registro formal y cortesía','الأسلوب الرسمي واللباقة',
 [('En situaciones formales usamos usted, el condicional de cortesía y el subjuntivo en las peticiones: ¿Podría ayudarme? Le agradecería que me respondiera.','في المواقف الرسمية نستعمل usted والشرطي للتأدب والمضارع المنصوب في الطلبات.'),
  ('Fórmulas útiles: Estimado señor, Le ruego que, Quedo a su disposición, Atentamente.','عبارات مفيدة في الرسائل الرسمية للافتتاح والطلب والختام.')],
 {'nohl':1,'head':['','informal','formal'],'rows':[['pedir','¿Me ayudas?','¿Podría ayudarme?'],['agradecer','Gracias por venir.','Le agradezco su visita.'],['despedirse','Un abrazo.','Atentamente.'],['saludar','Hola, Ana.','Estimada señora:']]},
 [('¿Podría ayudarme, por favor?','هل يمكنك مساعدتي من فضلك؟'),('Le agradecería que me respondiera pronto.','سأكون ممتنًا لو رددت علي قريبًا.'),('Quedo a su disposición.','أنا تحت أمركم.'),('Le ruego que me disculpe.','أرجو أن تعذرني.'),('Estimado señor, le escribo por el pedido.','سيدي العزيز، أكتب إليك بخصوص الطلب.'),('¿Le importaría esperar un momento?','هل تمانع في الانتظار لحظة؟')],
 [('Con una persona mayor decimos: ¿___ ayudarme?',['Podría','Puedes','Puedo'],0,'Con una persona mayor decimos: ¿Podría ayudarme?'),
  ('Le ___ que me disculpe.',['ruego','ruegas','rogué'],0,'Le ruego que me disculpe.'),
  ('Le agradecería que me ___ pronto.',['responda','respondiera','responde'],1,'Le agradecería que me respondiera pronto.'),
  ('Al final de una carta formal escribimos: ___.',['Atentamente','Un beso','Chao'],0,'Al final de una carta formal escribimos: Atentamente.'),
  ('Quedo a su ___.',['disposición','dispuesto','disponer'],0,'Quedo a su disposición.'),
  ('Al inicio de una carta formal decimos: ___ señor.',['Estimado','Hola','Oye'],0,'Al inicio de una carta formal decimos: Estimado señor.')])
