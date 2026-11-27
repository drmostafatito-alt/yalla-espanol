import a1,a2,b1,json,hashlib
levels=[dict(id='A1',desc='Lo básico: presente, ser y estar, género y número, artículos, pronombres, gustar, reflexivos e imperativo.',ar='الأساسيات: المضارع وser وestar والمذكر والمؤنث والأدوات والضمائر وgustar والانعكاسي والأمر.',topics=[]),dict(id='A2',desc='Pasado, futuro y comparaciones: perfecto, indefinido, imperfecto, estar + gerundio, ir a, futuro, comparativos, por y para.',ar='الماضي والمستقبل والمقارنة: الماضي القريب والمنتهي والمستمر والاستمرار وir a والمستقبل والمقارنة وpor وpara.',topics=[]),dict(id='B1',desc='Más precisión: contraste de pasados, pluscuamperfecto, condicional, subjuntivo, imperativo negativo y relativos.',ar='مزيد من الدقة: التمييز بين أزمنة الماضي والماضي البعيد والشرطي والمضارع المنصوب والنهي وجمل الصلة.',topics=[])]
for lv in 'B2 C1 C2'.split():
    levels.append(dict(id=lv,desc='Próximamente.',ar='قريبًا.',topics=[]))
GROUPS={'a1-presente':('Presente','المضارع'),'a1-ser-estar':('Presente','المضارع'),'a1-gustar':('Presente','المضارع'),'a1-reflexivos':('Presente','المضارع'),'a1-genero-numero':('Nombres y artículos','الأسماء والأدوات'),'a1-articulos':('Nombres y artículos','الأسماء والأدوات'),'a1-pronombres':('Nombres y artículos','الأسماء والأدوات'),'a1-imperativo':('Imperativo','الأمر'),
'a2-perfecto':('Pasado','الماضي'),'a2-indefinido':('Pasado','الماضي'),'a2-imperfecto':('Pasado','الماضي'),'a2-gerundio':('Presente y futuro','الحاضر والمستقبل'),'a2-ir-a':('Presente y futuro','الحاضر والمستقبل'),'a2-futuro':('Presente y futuro','الحاضر والمستقبل'),'a2-comparativos':('Comparar y relacionar','المقارنة والربط'),'a2-por-para':('Comparar y relacionar','المقارنة والربط'),
'b1-contraste':('Pasado','الماضي'),'b1-pluscuamperfecto':('Pasado','الماضي'),'b1-condicional':('Condicional y subjuntivo','الشرطي والمضارع المنصوب'),'b1-subjuntivo':('Condicional y subjuntivo','الشرطي والمضارع المنصوب'),'b1-imp-negativo':('Imperativo','الأمر'),'b1-relativas':('Oraciones','الجمل')}
for lv in levels:pass
audio={};i=0;seen=set()
for t in a1.T+a2.T+(b1.T if __import__('os').environ.get('B1') else []):
    levels[{'a1':0,'a2':1,'b1':2}[t['id'][:2]]]['topics'].append(dict(group=GROUPS[t['id']][0],groupAr=GROUPS[t['id']][1],id=t['id'],es=t['es'],ar=t['ar'],rule=t['rule'],table=t['table'],ex=t['ex'],exe=[[e[0],e[1],e[2],e[3]] for e in t['exe']]))
    for s in [e[0] for e in t['ex']]+[e[3] for e in t['exe']]:
        if s in seen: continue
        seen.add(s);sp='paco' if i%2==0 else 'luna';i+=1
        audio[s]='assets/audio/g403-'+hashlib.sha1((sp+':'+s).encode()).hexdigest()[:20]+'.mp3'
# sortgroups: keep topics of one group together
for lv in levels:
    order=[]
    for t in lv['topics']:
        if t['group'] not in order: order.append(t['group'])
    lv['topics'].sort(key=lambda t:order.index(t['group']))
js=open('tmpl.js').read().replace('__DATA__',json.dumps({'levels':levels},ensure_ascii=False)).replace('__AUDIO__',json.dumps(audio,ensure_ascii=False))
open('gram403.js','w').write(js);print(len(audio))
