import a1,a2,b1,hashlib,json,subprocess,os
os.makedirs('out',exist_ok=True)
items=[];seen=set();i=0
for t in a1.T+a2.T+b1.T:
    ss=[e[0] for e in t['ex']]+[e[3] for e in t['exe']]
    for s in ss:
        if s in seen: continue
        seen.add(s);sp='paco' if i%2==0 else 'luna';i+=1
        h=hashlib.sha1((sp+':'+s).encode()).hexdigest()[:20]
        items.append((h,sp,s))
open('todo.tsv','w').write(''.join(f"{h}\t{sp}\t{s}\n" for h,sp,s in items))
for h,sp,s in items:
    if os.path.exists(f'out/{h}.mp3'): continue
    spk='0' if sp=='paco' else '1'
    subprocess.run(['/tmp/ttsenv/bin/piper','-m','/downloads/work/tts/es_ES-sharvard-medium.onnx','--speaker',spk,'-f','/tmp/g.wav'],input=s.encode(),capture_output=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i','/tmp/g.wav','-af','loudnorm=I=-18:TP=-4','-ar','24000','-ac','1','-b:a','96k',f'out/{h}.mp3'])
print(len(items))
