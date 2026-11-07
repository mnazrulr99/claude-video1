import numpy as np,wave,json,sys
S=sys.argv[1]
w=wave.open(S+'/audio16k.wav');a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768
hop=160; rms=np.array([np.sqrt(np.mean(a[i:i+320]**2)) for i in range(0,len(a)-320,hop)])
db=20*np.log10(rms+1e-9)
floor=np.percentile(db,10); thr=floor+12
def t2i(t): return int(t*100)
# (label, start, end) whisper times
segs=[
 ("A",7.44,9.32),("A2",9.32,11.08),
 ("B",0.94,4.54),
 ("C",11.08,13.32),("C2",14.08,17.28),
 ("D",21.76,27.42),("D2",27.42,30.78),
 ("E",32.60,36.46),
 ("F",40.88,43.98),("G",43.98,45.86),
 ("H",48.06,49.96),
 ("I",51.74,56.54),
 ("J",59.66,61.94),("K",63.78,64.30),("L",65.04,66.00),
 ("M",69.96,76.74),
 ("N",77.54,81.32),("N2",81.32,83.52),("N3",84.10,85.08),
]
out=[]
for lab,s,e in segs:
    # start: find first voiced frame in [s-0.25, s+0.6]; back off 0.07
    sm=np.convolve(db,np.ones(5)/5,'same')
    i0,i1=t2i(s-0.22),t2i(s+0.04)
    ns=(i0+np.argmin(sm[i0:i1]))/100
    # end: last voiced frame in [e-0.5, e+0.3]; pad 0.10
    j0,j1=t2i(e-0.04),min(t2i(e+0.28),len(db))
    ne=(j0+np.argmin(sm[j0:j1]))/100
    ov={"A":(7.50,None),"F":(40.86,None),"H":(48.03,49.98),"I":(51.76,None),"C2":(None,17.30),"D":(21.80,None)}
    if lab in ov:
        a_,b_=ov[lab]; ns=a_ if a_ else ns; ne=b_ if b_ else ne
    fs,fe=round(ns*30),round(ne*30)
    out.append({"id":lab,"src":[s,e],"f0":fs,"f1":fe})
    print(lab,s,e,'->',fs/30,fe/30)
# merge contiguous (gap<=1 frame)
m=[]
for o in out:
    if m and o["f0"]<=m[-1]["f1"]+1 and o["f0"]>=m[-1]["f0"]: m[-1]["f1"]=max(m[-1]["f1"],o["f1"]); m[-1]["id"]+="+"+o["id"]
    else: m.append(dict(o))
tot=0
for o in m:
    o["out0"]=tot; tot+=o["f1"]-o["f0"]
print("segments",len(m),"total",tot/30)
json.dump(m,open(S+'/work/cuts.json','w'),indent=1)
