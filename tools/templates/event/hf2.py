# Jana projek HyperFrames (index.html) untuk job raya. Guna: python3 -I hf2.py <dir_skrip> <dir_job>
import sys, os, html, subprocess, shutil, random
sys.path.insert(0, sys.argv[1]); import plan as P, captions as C
J = sys.argv[2]; PROJ = f"{J}/hfproj"; os.makedirs(PROJ, exist_ok=True)
INIT = os.path.join(os.path.dirname(J), "hfinit")
for f in ("hyperframes.json", "meta.json", "package.json"): shutil.copy(f"{INIT}/{f}", PROJ)
REPO = "/home/user/claude-video1"
for name, src in (("base.mp4", f"{J}/base.mp4"), ("sfx", f"{REPO}/tools/sfx")):
    p = f"{PROJ}/{name}"
    if not os.path.lexists(p): os.symlink(src, p)
os.makedirs(f"{PROJ}/fonts", exist_ok=True)
for f in ("/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf", "/usr/share/fonts/opentype/inter/Inter-Black.otf",
          "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf", "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"):
    shutil.copy(f, f"{PROJ}/fonts/")
tl_, TT = P.timeline(); VID = TT - P.END_BLACK
# --- BGM: premix dengan ducking (B-roll kuat, bawah suara perlahan) ---
loud = [(b["name"], a, e) for b, a, e in tl_ if b["audio"] is None]
LO, HI = 0.085, 0.32
expr = f"{LO}"
for _, a, e in loud:
    expr = f"if(between(t,{a-0.4:.2f},{e+0.4:.2f}),{LO}+({HI}-{LO})*min(1,min(t-{a-0.4:.2f},{e+0.4:.2f}-t)/0.4),{expr})"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "0", "-i", f"{J}/bgm/carefree.mp3", "-t", f"{VID:.3f}",
                "-af", f"aresample=48000,adelay=1700|1700,volume='{expr}':eval=frame,afade=t=in:st=1.7:d=0.6,afade=t=out:st={VID-2.2:.2f}:d=2.2",
                "-ac", "2", f"{PROJ}/bgm.wav"], check=True)
els, tl, aud = [], [], []
def sfx(name, t, vol=0.45, dur=1.2):
    dur = min(dur, TT - t - 0.01)
    aud.append(f'<audio id="sfx{len(aud)}" class="clip" src="sfx/{name}.wav" data-start="{t:.3f}" data-duration="{dur:.3f}" data-volume="{vol}"></audio>')
# --- zoom setiap saat (untuk besarkan perkataan masa close-up, R27) ---
SH = []
for b, a, e in tl_:
    used = 0
    for sh in b["shots"]:
        du = sh[3] if sh[3] else round(e - a - used, 3); SH.append((a + used, a + used + du, sh[2])); used += du
zoom = lambda t: next((z for a, e, z in SH if a <= t < e), 1.2)
# whoosh lembut setiap tukar visual (R28)
for a, e, z in SH[1:]: sfx("whoosh-soft", max(0, a - 0.12), 0.5, 0.8)
# --- caption ---
for i, c in enumerate(C.build()):
    big = zoom(c["t"] + 0.05) >= 1.45
    spans = []
    for j, w in enumerate(c["words"]):
        k = big and w["w"].strip("?") in C.KEY
        spans.append(f'<span id="c{i}_{j}" class="{"big" if k else ""}">{html.escape(w["w"])}</span>')
    els.append(f'<div id="cap{i}" class="clip cap" data-start="{c["t"]:.3f}" data-duration="{c["e"]-c["t"]:.3f}">{" ".join(spans)}</div>')
    tl.append(f'tl.from("#cap{i}", {{scale:0.85, opacity:0, duration:0.12, ease:"back.out(2)"}}, {c["t"]:.3f});')
    for j, w in enumerate(c["words"]):
        tl.append(f'tl.set("#c{i}_{j}", {{color:"{P.GOLD}"}}, {w["t"]:.3f});')
        nxt = c["words"][j+1]["t"] if j + 1 < len(c["words"]) else c["e"]
        if not (big and w["w"].strip("?") in C.KEY): tl.append(f'tl.set("#c{i}_{j}", {{color:"#FFFFFF"}}, {nxt:.3f});')
# --- grafik ---
for k, (a, e, kind, txt, y) in enumerate(P.GFX):
    gid = f"g{k}"; d = e - a
    if kind in ("title", "end"):
        l1, l2 = txt.split("|")
        stars = "".join(f'<span class="st" style="left:{x}px;top:{yy}px;font-size:{s}px">✦</span>' for x, yy, s in
                        ((110, -40, 60), (930, -30, 50), (80, 190, 44), (960, 200, 56), (520, -90, 36)))
        if kind == "title":
            chars = "".join(f'<span class="ch">{html.escape(ch)}</span>' for ch in l1)
            inner = f'<div class="t1">{chars}</div><div class="t2">{html.escape(l2)}</div>'
        else:
            inner = f'<div class="e1">{html.escape(l1)}</div><div class="e2">{html.escape(l2)}</div>'
        els.append(f'<div id="{gid}" class="clip gfx {kind}" style="top:{y-130}px" data-start="{a:.3f}" data-duration="{d:.3f}">{stars}{inner}</div>')
        if kind == "title":
            tl.append(f'tl.from("#{gid} .ch", {{opacity:0, y:30, duration:0.18, stagger:0.04, ease:"back.out(2)"}}, {a+0.05:.3f});')
            tl.append(f'tl.from("#{gid} .t2", {{scale:0, opacity:0, duration:0.45, ease:"back.out(2)"}}, {a+0.65:.3f});')
            sfx("sparkle", a, 0.5); sfx("pop", a + 0.65, 0.45)
        else:
            tl.append(f'tl.from("#{gid} .e1", {{opacity:0, scale:0.6, duration:0.5, ease:"back.out(1.8)"}}, {a+0.05:.3f});')
            tl.append(f'tl.from("#{gid} .e2", {{opacity:0, y:30, duration:0.35}}, {a+0.55:.3f});')
            sfx("chime", a + 0.05, 0.45)
        tl.append(f'tl.from("#{gid} .st", {{scale:0, rotation:-90, duration:0.4, stagger:0.06, ease:"back.out(3)"}}, {a+0.2:.3f});')
        tl.append(f'tl.to("#{gid} .st", {{scale:0.6, opacity:0.6, duration:0.5, yoyo:true, repeat:{max(1,int(d/0.5)-2)}, stagger:0.1}}, {a+0.7:.3f});')
        tl.append(f'tl.to("#{gid}", {{opacity:0, duration:0.25}}, {e-0.25:.3f});')
    elif kind == "pill":
        emo, label = txt.split(" ", 1)
        els.append(f'<div id="{gid}" class="clip gfx pillw" style="top:{y-45}px" data-start="{a:.3f}" data-duration="{d:.3f}"><div class="pill"><span class="emo">{emo}</span><span>{html.escape(label)}</span><span class="sp">✦</span><span class="sp2">✦</span></div></div>')
        tl.append(f'tl.from("#{gid} .pill", {{scale:0, rotation:-8, duration:0.35, ease:"back.out(2.4)"}}, {a:.3f});')
        tl.append(f'tl.from("#{gid} .sp, #{gid} .sp2", {{scale:0, duration:0.3, stagger:0.1, ease:"back.out(3)"}}, {a+0.3:.3f});')
        tl.append(f'tl.to("#{gid} .pill", {{scale:0, opacity:0, duration:0.2}}, {e-0.2:.3f});')
        sfx("pop", a, 0.5)
    elif kind == "sparkle":   # transition kilauan emas
        random.seed(7)
        st = "".join(f'<span class="bs" style="left:{random.randint(40,1040)}px;top:{random.randint(80,1840)}px;font-size:{random.randint(40,140)}px">✦</span>' for _ in range(34))
        els.append(f'<div id="{gid}" class="clip burst" data-start="{a-0.25:.3f}" data-duration="{d+0.25:.3f}"><div class="flash"></div>{st}</div>')
        tl.append(f'tl.fromTo("#{gid} .flash", {{opacity:0}}, {{opacity:0.75, duration:0.22, yoyo:true, repeat:1, ease:"sine.inOut"}}, {a-0.25:.3f});')
        tl.append(f'tl.fromTo("#{gid} .bs", {{scale:0, rotation:-60}}, {{scale:1, rotation:30, duration:0.35, stagger:0.008, ease:"back.out(2)"}}, {a-0.25:.3f});')
        tl.append(f'tl.to("#{gid} .bs", {{scale:0, opacity:0, duration:0.3, stagger:0.006}}, {a+0.25:.3f});')
        sfx("sparkle", a - 0.25, 0.55)
sfx("ding", VID + 0.02, 0.5)
doc = f'''<!doctype html>
<html lang="ms" data-resolution="portrait">
<head>
<meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>
@font-face {{ font-family:"InterXB"; src:url("fonts/Inter-ExtraBold.otf"); }}
@font-face {{ font-family:"InterBlack"; src:url("fonts/Inter-Black.otf"); }}
@font-face {{ font-family:"SerifBI"; src:url("fonts/LiberationSerif-BoldItalic.ttf"); }}
@font-face {{ font-family:"Emoji"; src:url("fonts/NotoColorEmoji.ttf"); }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1080px; height:1920px; overflow:hidden; background:#000; }}
#root {{ position:relative; width:1080px; height:1920px; }}
#base {{ position:absolute; inset:0; width:1080px; height:1920px; object-fit:cover; z-index:0; }}
.cap {{ position:absolute; left:40px; width:1000px; top:{P.CAP_Y-60}px; height:130px; display:flex; align-items:center; justify-content:center; gap:0 18px; flex-wrap:nowrap;
  z-index:20; font-family:"InterXB"; font-size:58px; color:#fff; letter-spacing:0.5px; white-space:nowrap;
  -webkit-text-stroke:10px #000; paint-order:stroke fill; text-shadow:0 5px 12px rgba(0,0,0,.45); }}
.cap .big {{ font-size:104px; color:{P.GOLD}; }}
.gfx {{ position:absolute; left:0; width:1080px; z-index:10; text-align:center; }}
.st {{ position:absolute; color:{P.GOLD}; font-family:"InterXB"; text-shadow:0 0 18px rgba(255,210,90,.9); }}
.title .t1 {{ font-family:"InterBlack"; font-size:96px; color:{P.GOLD}; -webkit-text-stroke:12px #3a2400; paint-order:stroke fill; letter-spacing:2px; }}
.title .t2 {{ display:inline-block; font-family:"SerifBI"; font-size:124px; color:#fff; -webkit-text-stroke:9px #7a5000; paint-order:stroke fill; margin-top:-6px; }}
.end .e1 {{ font-family:"SerifBI"; font-size:118px; color:{P.GOLD}; -webkit-text-stroke:9px #3a2400; paint-order:stroke fill; }}
.end .e2 {{ font-family:"InterXB"; font-size:62px; color:#fff; -webkit-text-stroke:10px #000; paint-order:stroke fill; margin-top:6px; letter-spacing:2px; }}
.pillw {{ height:100px; }}
.pill {{ position:relative; display:inline-flex; align-items:center; gap:14px; background:#FFF8E6; border:6px solid {P.GOLD}; border-radius:60px; padding:10px 38px 10px 22px;
  font-family:"InterXB"; font-size:48px; color:#5A3B00; box-shadow:0 8px 22px rgba(0,0,0,.3); white-space:nowrap; }}
.pill .emo {{ font-family:"Emoji"; font-size:50px; }}
.pill .sp, .pill .sp2 {{ position:absolute; color:{P.GOLD}; font-size:44px; text-shadow:0 0 10px rgba(255,210,90,.9); }}
.pill .sp {{ right:-34px; top:-36px; }} .pill .sp2 {{ right:-54px; top:8px; font-size:28px; }}
.burst {{ position:absolute; inset:0; z-index:30; pointer-events:none; }}
.burst .flash {{ position:absolute; inset:0; background:radial-gradient(circle at 50% 50%, rgba(255,236,170,1), rgba(245,197,66,.6) 55%, rgba(245,197,66,0) 80%); }}
.bs {{ position:absolute; color:{P.GOLD}; font-family:"InterXB"; text-shadow:0 0 20px rgba(255,220,120,1); transform:translate(-50%,-50%); }}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TT:.3f}" data-width="1080" data-height="1920">
<video id="base" class="clip" src="base.mp4" data-start="0" data-duration="{TT:.3f}" data-has-audio="true" data-volume="1"></video>
<audio id="bgm" class="clip" src="bgm.wav" data-start="0" data-duration="{VID:.3f}" data-volume="1"></audio>
{chr(10).join(els)}
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
print("els", len(els), "audio", len(aud), "dur", round(TT, 2))
