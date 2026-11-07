import json,sys
from faster_whisper import WhisperModel
m=WhisperModel("large-v3",device="cpu",compute_type="int8")
import numpy as np,wave
wf=wave.open(sys.argv[1]);a=np.frombuffer(wf.readframes(wf.getnframes()),np.int16).astype(np.float32)/32768
segs,info=m.transcribe(a,language="ms",word_timestamps=True,vad_filter=False,beam_size=5)
out=[]
for s in segs:
    d={"start":s.start,"end":s.end,"text":s.text,"words":[{"w":w.word,"s":w.start,"e":w.end,"p":w.probability} for w in s.words]}
    out.append(d); print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text}",flush=True)
json.dump(out,open("transcript.json","w"),ensure_ascii=False,indent=1)
