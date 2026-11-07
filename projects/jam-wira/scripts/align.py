import numpy as np,wave,sys
def load(p):
    w=wave.open(p);a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
    return a[::4]  # 4 kHz
raw=load(sys.argv[1]); usr=load(sys.argv[2])
sr=4000; win=int(0.4*sr); hop=int(0.2*sr)
N=1<<int(np.ceil(np.log2(len(raw)+win)))
R=np.fft.rfft(raw,N)
cs=np.concatenate([[0],np.cumsum(raw.astype(np.float64)**2)])
e=np.sqrt(cs[win:]-cs[:-win]+1e-9)
res=[]
for st in range(0,len(usr)-win,hop):
    x=usr[st:st+win]
    if np.sqrt(np.mean(x**2))<0.003: res.append((st/sr,None,0));continue
    c=np.fft.irfft(R*np.conj(np.fft.rfft(x,N)),N)[:len(e)]/(e*np.linalg.norm(x)+1e-9)
    k=int(np.argmax(c)); res.append((st/sr,k/sr,float(c[k])))
segs=[]
for t,s,q in res:
    if s is None or q<0.5: continue
    off=round(s-t,2)
    if segs and abs(off-segs[-1][2])<0.08 and t-segs[-1][1]<0.45: segs[-1][1]=t+0.4
    else: segs.append([t,t+0.4,off])
for a,b,o in segs:
    if b-a>0.5: print(f"out {a:6.2f}-{b:6.2f}  <- raw {a+o:6.2f}-{b+o:6.2f}  (len {b-a:.2f})")
print("low-match:",[(round(t,1),round(q,2)) for t,s,q in res if s is not None and q<0.5])
print("silent:",[round(t,1) for t,s,q in res if s is None])
