# Bina base.mp4 1080x1920 daripada BEATS (multi-klip), potong setiap shot/audio berasingan kemudian gabung.
# Guna: python3 -I base.py <dir_skrip> <dir_job>
import sys, subprocess, os
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, sys.argv[1]); import plan as P
J = sys.argv[2]; T = f"{J}/parts"; os.makedirs(T, exist_ok=True)
def vf(z, kx, ky):
    w = int(round(1080*z/2)*2); h = int(round(1920*z/2)*2)
    return (f"scale={w}:{h}:flags=lanczos,crop=1080:1920:'min(max(0,{w}*{kx}-540),{w}-1080)':'min(max(0,{h}*{ky}-960),{h}-1920)',"
            "setsar=1,fps=30,format=yuv420p")
jobs, vlist, alist = [], [], []
tl, TT = P.timeline(); n = 0
for b, t0, t1 in tl:
    d = t1 - t0; used = 0
    for c, s, z, du, kx, ky in b["shots"]:
        du = du if du else round(d - used, 3); used += du
        f = f"{T}/v{n:03d}.mp4"; vlist.append(f); n += 1
        jobs.append(["ffmpeg", "-v", "error", "-y", "-ss", f"{s:.3f}", "-i", f"{J}/v/c{c}.mp4", "-t", f"{du:.3f}", "-an",
                     "-vf", vf(z, kx, ky), "-c:v", "libx264", "-crf", "17", "-preset", "fast", f])
    pieces = b["audio"] or [(b["shots"][0][0], b["shots"][0][1], b["shots"][0][1] + d)]
    vol = 1.0 if b["audio"] else 0.2
    for c, s, e in pieces:
        f = f"{T}/a{n:03d}.wav"; alist.append(f); n += 1
        fd = 0.03 if b["audio"] else 0.2
        jobs.append(["ffmpeg", "-v", "error", "-y", "-ss", f"{s:.3f}", "-i", f"{J}/v/c{c}.mp4", "-t", f"{e-s:.3f}", "-vn",
                     "-af", f"aresample=48000,volume={vol},afade=t=in:d={fd},afade=t=out:st={e-s-fd:.3f}:d={fd}",
                     "-ac", "2", "-ar", "48000", f])
f = f"{T}/vblack.mp4"; vlist.append(f)
jobs.append(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=black:s=1080x1920:r=30:d={P.END_BLACK}",
             "-vf", "format=yuv420p,setsar=1", "-c:v", "libx264", "-crf", "17", "-preset", "fast", f])
f = f"{T}/ablack.wav"; alist.append(f)
jobs.append(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", f"{P.END_BLACK}", f])
with ThreadPoolExecutor(4) as ex: list(ex.map(lambda c: subprocess.run(c, check=True), jobs))
open(f"{T}/v.txt", "w").write("".join(f"file '{x}'\n" for x in vlist))
open(f"{T}/a.txt", "w").write("".join(f"file '{x}'\n" for x in alist))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{T}/v.txt", "-f", "concat", "-safe", "0",
                "-i", f"{T}/a.txt", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                f"{J}/base.mp4"], check=True)
print("ok", round(TT, 2))
