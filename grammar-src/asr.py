import sys,difflib,re,unicodedata
from faster_whisper import WhisperModel
def N(s):
    s=unicodedata.normalize('NFD',s.lower());s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9 ]','',s).split()
m=WhisperModel('small',device='cpu',compute_type='int8')
bad=0
for l in open('todo.tsv'):
    h,sp,es=l.rstrip('\n').split('\t')
    segs,_=m.transcribe(f'out/{h}.mp3',language='es',beam_size=5)
    hyp=' '.join(s.text for s in segs)
    r=difflib.SequenceMatcher(None,' '.join(N(es)),' '.join(N(hyp))).ratio()
    ok=N(es)==N(hyp)
    if not ok:bad+=1
    print('OK ' if ok else 'DIF',round(r,2),h,'|',es,'|',hyp.strip(),flush=True)
print('nonexact',bad)
