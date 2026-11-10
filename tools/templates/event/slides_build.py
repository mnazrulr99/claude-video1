# Potong shot (ffmpeg) + jana projek HyperFrames slideshow. Guna: python3 -I slides_build.py <dir_skrip> <dir_job>
import sys, os, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, sys.argv[1]); import slides as S, plan as P
J = sys.argv[2]; PROJ = f"{J}/hfslides"; os.makedirs(f"{PROJ}/shots", exist_ok=True)
INIT = os.path.join(os.path.dirname(J), "hfinit")
for f in ("hyperframes.json", "meta.json", "package.json"): shutil.copy(f"{INIT}/{f}", PROJ)
shutil.copy(f"{J}/bgm/raya-asal.wav", f"{PROJ}/raya-asal.wav")
if not os.path.lexists(f"{PROJ}/sfx"): os.symlink("/home/user/claude-video1/tools/sfx", f"{PROJ}/sfx")
os.makedirs(f"{PROJ}/fonts", exist_ok=True)
for f in ("/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf", "/usr/share/fonts/opentype/inter/Inter-Black.otf",
          "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf"):
    shutil.copy(f, f"{PROJ}/fonts/")
def vf(z, kx, ky):
    w = int(round(1080*z/2)*2); h = int(round(1920*z/2)*2)
    return (f"scale={w}:{h}:flags=lanczos,crop=1080:1920:'min(max(0,{w}*{kx}-540),{w}-1080)':'min(max(0,{h}*{ky}-960),{h}-1920)',"
            "setsar=1,fps=30,format=yuv420p")
jobs = []
for i, (c, s, d, kx, ky, _) in enumerate(S.SHOTS):
    jobs.append(["ffmpeg", "-v", "error", "-y", "-ss", f"{s:.3f}", "-i", f"{J}/v/c{c}.mp4", "-t", f"{d:.3f}", "-an",
                 "-vf", vf(S.BASEZ, kx, ky), "-c:v", "libx264", "-crf", "16", "-preset", "fast", f"{PROJ}/shots/s{i:02d}.mp4"])
with ThreadPoolExecutor(4) as ex: list(ex.map(lambda c: subprocess.run(c, check=True), jobs))
st, END = S.starts(); TT = END + S.END_BLACK
els, tl, aud = [], [], []
def sfx(name, t, vol, dur=1.0):
    aud.append(f'<audio id="sfx{len(aud)}" class="clip" src="sfx/{name}.wav" data-start="{t:.3f}" data-duration="{min(dur, TT-t-0.01):.3f}" data-volume="{vol}"></audio>')
for i, ((c, s, d, kx, ky, dirn), t0) in enumerate(zip(S.SHOTS, st)):
    els.append(f'<video id="v{i}" class="clip shot" src="shots/s{i:02d}.mp4" data-start="{t0:.3f}" data-duration="{d:.3f}" data-volume="0" muted style="z-index:{i+1}"></video>')
    a, b = (1.0, 1.05) if dirn == "in" else (1.05, 1.0)
    tl.append(f'tl.fromTo("#v{i}", {{scale:{a}}}, {{scale:{b}, duration:{d:.3f}, ease:"none"}}, {t0:.3f});')
    if i: tl.append(f'tl.fromTo("#v{i}", {{opacity:0}}, {{opacity:1, duration:{S.XF}, ease:"sine.inOut"}}, {t0:.3f});')
# tamat: pudar ke hitam
tl.append(f'tl.to("#fade", {{opacity:1, duration:0.5, ease:"sine.in"}}, {END-0.5:.3f});')
aud.append(f'<audio id="bgm" class="clip" src="raya-asal.wav" data-start="0" data-duration="{TT:.3f}" data-volume="1"></audio>')
GOLD = P.GOLD
stars = lambda: "".join(f'<span class="st" style="left:{x}px;top:{y}px;font-size:{z}px">✦</span>' for x, y, z in ((110,-40,60),(930,-30,50),(80,190,44),(960,200,56),(520,-90,36)))
ta, te = 0.4, S.SHOTS[0][2] + S.SHOTS[1][2] - S.XF - 0.3
els.append(f'<div id="title" class="clip gfx" data-start="{ta:.3f}" data-duration="{te-ta:.3f}" style="top:1430px">{stars()}<div class="t1">{"".join(f"<span class=ch>{ch}</span>" for ch in "RUMAH TERBUKA")}</div><div class="t2">Aidilfitri</div></div>')
tl.append(f'tl.from("#title .ch", {{opacity:0, y:30, duration:0.25, stagger:0.05, ease:"back.out(2)"}}, {ta+0.05:.3f});')
tl.append(f'tl.from("#title .t2", {{opacity:0, scale:0.6, duration:0.6, ease:"back.out(1.8)"}}, {ta+0.8:.3f});')
tl.append(f'tl.from("#title .st", {{scale:0, rotation:-90, duration:0.5, stagger:0.08, ease:"back.out(3)"}}, {ta+0.3:.3f});')
tl.append(f'tl.to("#title", {{opacity:0, duration:0.5}}, {te-0.5:.3f});')
ea = st[-1] + 0.5; ee = END
els.append(f'<div id="endc" class="clip gfx" data-start="{ea:.3f}" data-duration="{ee-ea:.3f}" style="top:1430px">{stars()}<div class="e1">Selamat Hari Raya</div><div class="e2">MAAF ZAHIR &amp; BATIN</div></div>')
tl.append(f'tl.from("#endc .e1", {{opacity:0, scale:0.7, duration:0.7, ease:"back.out(1.6)"}}, {ea+0.05:.3f});')
tl.append(f'tl.from("#endc .e2", {{opacity:0, y:30, duration:0.5}}, {ea+0.7:.3f});')
tl.append(f'tl.from("#endc .st", {{scale:0, rotation:-90, duration:0.5, stagger:0.08, ease:"back.out(3)"}}, {ea+0.4:.3f});')
doc = f'''<!doctype html>
<html lang="ms" data-resolution="portrait">
<head>
<meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>
@font-face {{ font-family:"InterXB"; src:url("fonts/Inter-ExtraBold.otf"); }}
@font-face {{ font-family:"InterBlack"; src:url("fonts/Inter-Black.otf"); }}
@font-face {{ font-family:"SerifBI"; src:url("fonts/LiberationSerif-BoldItalic.ttf"); }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1080px; height:1920px; overflow:hidden; background:#000; }}
#root {{ position:relative; width:1080px; height:1920px; overflow:hidden; background:#000; }}
.shot {{ position:absolute; inset:0; width:1080px; height:1920px; object-fit:cover; transform-origin:50% 45%; }}
#fade {{ position:absolute; inset:0; background:#000; opacity:0; z-index:90; }}
.gfx {{ position:absolute; left:0; width:1080px; z-index:80; text-align:center; }}
.st {{ position:absolute; color:{GOLD}; font-family:"InterXB"; text-shadow:0 0 18px rgba(255,210,90,.9); }}
.t1 {{ font-family:"InterBlack"; font-size:96px; color:{GOLD}; -webkit-text-stroke:12px #3a2400; paint-order:stroke fill; letter-spacing:2px; }}
.t2 {{ display:inline-block; font-family:"SerifBI"; font-size:124px; color:#fff; -webkit-text-stroke:9px #7a5000; paint-order:stroke fill; margin-top:-6px; }}
.e1 {{ font-family:"SerifBI"; font-size:118px; color:{GOLD}; -webkit-text-stroke:9px #3a2400; paint-order:stroke fill; }}
.e2 {{ font-family:"InterXB"; font-size:62px; color:#fff; -webkit-text-stroke:10px #000; paint-order:stroke fill; margin-top:6px; letter-spacing:2px; }}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TT:.3f}" data-width="1080" data-height="1920">
{chr(10).join(els)}
<div id="fade"></div>
{chr(10).join(aud)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tl)}
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body>
</html>'''
open(f"{PROJ}/index.html", "w").write(doc)
print("shots", len(S.SHOTS), "dur", round(TT, 2))
