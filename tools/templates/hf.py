import sys, json, html
sys.path.insert(0, sys.argv[1]); import plan as P
W = sys.argv[2]; PROJ = f"{W}/hfproj"
words = [w for s in json.load(open(f"{W}/transcript.json")) for w in s["words"]]
def fix(w): w = w.strip(",.?"); return P.FIXES.get(w, w).upper()
o = P.src_to_out
VID_DUR = round((P.HOOK[1]-P.HOOK[0]) + sum(b-a for a,b,_ in P.SEGMENTS), 3)
TOTAL = round(VID_DUR + P.END_BLACK, 3)

# --- caption pages (maks 3 perkataan; pecah bila jarak > 0.35s) ---
ws = [dict(t=fix(w["word"]), s=o(w["start"]), e=o(min(w["end"], w["start"]+1.2))) for w in words]
ws = [w for w in ws if w["s"] is not None and w["e"] is not None and w["t"]]
pages, cur = [], []
for w in ws:
    if cur and (len(cur) == 3 or w["s"] - cur[-1]["e"] > 0.35): pages.append(cur); cur = []
    cur.append(w)
if cur: pages.append(cur)
els, tl, aud = [], [], []
for i, pg in enumerate(pages):
    s = pg[0]["s"]; e = pages[i+1][0]["s"] if i+1 < len(pages) and pages[i+1][0]["s"] - pg[-1]["e"] < 0.6 else pg[-1]["e"] + 0.25
    e = min(e, VID_DUR); 
    spans = "".join(f'<span id="w{i}_{j}">{html.escape(w["t"])}</span> ' for j, w in enumerate(pg))
    els.append(f'<div class="clip cap" data-start="{s:.3f}" data-duration="{e-s:.3f}">{spans.strip()}</div>')
    for j, w in enumerate(pg):
        tl.append(f'tl.set("#w{i}_{j}", {{color:"#FFE600"}}, {w["s"]:.3f});')
        nxt = pg[j+1]["s"] if j+1 < len(pg) else e
        tl.append(f'tl.set("#w{i}_{j}", {{color:"#FFFFFF"}}, {nxt:.3f});')

def sfx(name, t, vol=0.35, dur=1.0):
    dur = min(dur, TOTAL - t)
    aud.append(f'<audio id="sfx{len(aud)}" class="clip" src="sfx/{name}.wav" data-start="{t:.3f}" data-duration="{dur:.3f}" data-volume="{vol}"></audio>')

CHECK_SVG = '<span class="box"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
GIFT_SVG = '<span class="box gift"><svg viewBox="0 0 24 24"><rect x="3" y="10" width="18" height="11" rx="1.5" fill="#fff"/><rect x="2" y="7" width="20" height="4" rx="1" fill="#fff"/><rect x="11" y="7" width="2" height="14" fill="#E0457B"/><path d="M12 7c-2-4-6-4-6-1.5S10 7 12 7zm0 0c2-4 6-4 6-1.5S14 7 12 7z" fill="#fff"/></svg></span>'
BAG_SVG = '<svg class="bag" viewBox="0 0 24 24"><path d="M7 8V7a5 5 0 0110 0v1" fill="none" stroke="#fff" stroke-width="2.4"/><rect x="3.5" y="8" width="17" height="13" rx="2.5" fill="#fff"/></svg>'

for k, (a, b, kind, txt) in enumerate(P.GRAPHICS):
    s, e = o(a), o(b); d = e - s; gid = f"g{k}"
    if kind == "title":
        l1, l2 = txt.split("|")
        chars = "<br>".join("".join(f'<span class="ch">{html.escape(c)}</span>' for c in part) for part in l1.split(" ", 1))
        els.append(f'<div id="{gid}" class="clip gfx title" data-start="{s:.3f}" data-duration="{d:.3f}"><div class="t1">{chars}</div><div class="t2">{html.escape(l2)}</div></div>')
        tl.append(f'tl.from("#{gid} .ch", {{opacity:0, duration:0.01, stagger:0.035}}, {s+0.05:.3f});')
        tl.append(f'tl.from("#{gid} .t2", {{scale:0, opacity:0, duration:0.35, ease:"back.out(2.2)"}}, {s+0.85:.3f});')
        sfx("sparkle", s, 0.45); sfx("pop", s+0.85, 0.5)
    elif kind == "sizes":
        circ = "".join(f'<div class="sz" id="{gid}_{j}">{n}</div>' for j, n in enumerate(txt.split("|")))
        els.append(f'<div id="{gid}" class="clip gfx sizes" data-start="{s:.3f}" data-duration="{d:.3f}"><div class="row">{circ}</div><div class="cm">SAIZ (cm)</div></div>')
        for j, st in enumerate(P.SIZE_TIMES):
            t = o(st); tl.append(f'tl.from("#{gid}_{j}", {{scale:0, duration:0.3, ease:"back.out(2.5)"}}, {t:.3f});'); sfx("pop", t, 0.45)
        tl.append(f'tl.from("#{gid} .cm", {{opacity:0, y:20, duration:0.25}}, {s:.3f});')
    elif kind in ("check", "gift"):
        lines = txt.split("|"); rows = ""
        for j, ln in enumerate(lines):
            icon = GIFT_SVG if kind == "gift" else CHECK_SVG
            rows += f'<div class="pill" id="{gid}_{j}">{icon}<span>{html.escape(ln)}</span></div>'
        els.append(f'<div id="{gid}" class="clip gfx checks" data-start="{s:.3f}" data-duration="{d:.3f}">{rows}</div>')
        for j in range(len(lines)):
            t = s + j*0.9
            tl.append(f'tl.from("#{gid}_{j}", {{x:-300, opacity:0, duration:0.35, ease:"power3.out"}}, {t:.3f});')
            tl.append(f'tl.from("#{gid}_{j} .box", {{scale:0, duration:0.25, ease:"back.out(3)"}}, {t+0.3:.3f});')
            sfx("chime" if kind == "gift" else "ding", t+0.3, 0.4)
    elif kind == "badge":
        els.append(f'<div id="{gid}" class="clip gfx badge" data-start="{s:.3f}" data-duration="{d:.3f}"><div class="bb">{html.escape(txt)}</div></div>')
        tl.append(f'tl.from("#{gid} .bb", {{scale:2.4, opacity:0, duration:0.3, ease:"power4.in"}}, {s:.3f});')
        tl.append(f'tl.to("#{gid} .bb", {{scale:1.06, duration:0.5, yoyo:true, repeat:{max(1,int(d/0.5)-2)}, ease:"sine.inOut"}}, {s+0.35:.3f});')
        sfx("impact", s+0.25, 0.6)
    elif kind == "cta":
        els.append(f'<div id="{gid}" class="clip gfx cta" data-start="{s:.3f}" data-duration="{min(d, VID_DUR-s):.3f}"><div class="cp"><span class="ic">{BAG_SVG}</span><span>{html.escape(txt)}</span></div></div>')
        tl.append(f'tl.from("#{gid} .cp", {{x:-300, opacity:0, duration:0.4, ease:"back.out(1.8)"}}, {s:.3f});')
        tl.append(f'tl.to("#{gid} .cp", {{scale:1.07, duration:0.4, yoyo:true, repeat:{max(1,int(d/0.4)-2)}, ease:"sine.inOut"}}, {s+0.5:.3f});')
        sfx("pop", s, 0.5)

sfx("whoosh", 0.0, 0.35); sfx("whoosh", (P.HOOK[1]-P.HOOK[0]) - 0.25, 0.45); sfx("ding", VID_DUR + 0.05, 0.4)

SX, SW, GT, CT = P.SAFE['x'], P.SAFE['w'], P.SAFE['gfx_top'], P.SAFE['cap_top']
doc = f'''<!doctype html>
<html lang="ms" data-resolution="portrait">
<head>
<meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>
@font-face {{ font-family:"InterBlack"; src:url("fonts/Inter-Black.otf"); }}
@font-face {{ font-family:"InterXB"; src:url("fonts/Inter-ExtraBold.otf"); }}
@font-face {{ font-family:"SerifBI"; src:url("fonts/LiberationSerif-BoldItalic.ttf"); }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:1080px; height:1920px; overflow:hidden; background:#000; }}
#root {{ position:relative; width:1080px; height:1920px; }}
#base {{ position:absolute; inset:0; width:1080px; height:1920px; object-fit:cover; z-index:0; }}
#endblack {{ position:absolute; inset:0; background:#000; z-index:50; }}
.cap {{ position:absolute; left:{SX}px; width:{SW}px; top:{CT}px; text-align:left; z-index:20;
  font-family:"InterXB"; font-size:54px; line-height:1.12; color:#fff; letter-spacing:0.3px;
  -webkit-text-stroke:9px #000; paint-order:stroke fill; text-shadow:0 5px 12px rgba(0,0,0,.45); }}
.gfx {{ position:absolute; left:{SX}px; width:{SW}px; top:{GT}px; z-index:10; text-align:left; }}
.title .t1 {{ font-family:"SerifBI"; font-size:64px; line-height:1.05; color:#fff; -webkit-text-stroke:8px #2a0a1a; paint-order:stroke fill; }}
.title .t2 {{ display:inline-block; font-family:"InterBlack"; font-size:118px; line-height:1.05; color:#FFE600; -webkit-text-stroke:12px #000; paint-order:stroke fill; transform-origin:left center; }}
.sizes .row {{ display:flex; gap:10px; }}
.sz {{ width:80px; height:80px; border-radius:50%; background:#fff; border:7px solid #FFE600; display:flex; align-items:center; justify-content:center;
  font-family:"InterBlack"; font-size:34px; color:#D6287A; box-shadow:0 6px 14px rgba(0,0,0,.3); }}
.sizes .cm {{ margin-top:12px; font-family:"InterXB"; font-size:44px; color:#fff; -webkit-text-stroke:8px #000; paint-order:stroke fill; }}
.checks {{ display:flex; flex-direction:column; gap:18px; align-items:flex-start; }}
.pill {{ display:flex; align-items:center; gap:14px; background:#fff; border-radius:60px; padding:12px 26px 12px 12px; box-shadow:0 8px 20px rgba(0,0,0,.28);
  font-family:"InterXB"; font-size:34px; color:#1e1e1e; white-space:nowrap; }}
.box {{ width:56px; height:56px; border-radius:14px; background:#2EB85C; display:flex; align-items:center; justify-content:center; flex:none; }}
.box.gift {{ background:#E0457B; }}
.box svg {{ width:42px; height:42px; }}
.badge .bb {{ display:inline-block; transform:rotate(-5deg); transform-origin:left center; background:#E61E32; color:#FFE600; font-family:"InterBlack"; font-size:62px; padding:16px 34px;
  border-radius:30px; -webkit-text-stroke:5px #78000a; paint-order:stroke fill; box-shadow:0 10px 24px rgba(0,0,0,.35); white-space:nowrap; }}
.cta .cp {{ display:inline-flex; align-items:center; gap:16px; background:#FFD600; border-radius:70px; padding:16px 34px 16px 16px; font-family:"InterBlack"; font-size:46px; color:#141414; box-shadow:0 10px 24px rgba(0,0,0,.35); white-space:nowrap; transform-origin:left center; }}
.cta .ic {{ width:70px; height:70px; border-radius:18px; background:#FF8A00; display:flex; align-items:center; justify-content:center; }}
.cta .bag {{ width:48px; height:48px; }}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
<video id="base" class="clip" src="base.mp4" data-start="0" data-duration="{VID_DUR}" data-has-audio="true" data-volume="1"></video>
<div id="endblack" class="clip" data-start="{VID_DUR}" data-duration="{TOTAL-VID_DUR:.3f}"></div>
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
print("pages", len(pages), "els", len(els), "audio", len(aud), "dur", TOTAL)
