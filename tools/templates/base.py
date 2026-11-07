import sys, subprocess
sys.path.insert(0, sys.argv[1]); import plan as P
W = sys.argv[2]; RAW = f"{W}/raw.mp4"; OUT = f"{W}/base.mp4"
def vf(z):
    # skala ke 1080 lebar, crop 1080x1920; punch-in = skala lebih besar, crop sedikit ke atas (muka+produk)
    w = int(round(1080*z/2)*2)
    h = int(round(1974*z/2)*2)
    return f"scale={w}:{h}:flags=lanczos,crop=1080:1920:(iw-1080)/2:(ih-1920)/2.4,setsar=1,fps=30,format=yuv420p"
parts=[]; i=0; fc=[]
clips=[(P.HOOK[0],P.HOOK[1],1.0,True)]+[(a,b,z,False) for a,b,z in P.SEGMENTS]
for a,b,z,mute in clips:
    fc.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS,{vf(z)}[v{i}]")
    if mute: fc.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{b-a}[a{i}]")
    else: fc.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:d=0.02,afade=t=out:st={b-a-0.03:.3f}:d=0.03[a{i}]")
    parts.append(f"[v{i}][a{i}]"); i+=1
fc.append("".join(parts)+f"concat=n={i}:v=1:a=1[v][a]")
cmd=["ffmpeg","-v","error","-y","-i",RAW,"-filter_complex",";".join(fc),"-map","[v]","-map","[a]",
     "-c:v","libx264","-crf","16","-preset","medium","-c:a","aac","-b:a","192k",OUT]
subprocess.run(cmd,check=True); print("ok")
