#!/usr/bin/env python3
"""Jana storyboard HTML interaktif (mesra phone) daripada pelan edit JSON — SEBELUM render (R91).

Guna:
  python3 -I tools/storyboard_html.py plan-storyboard.json output/<job>/storyboard-<job>.html

Fail HTML yang terhasil berdiri sendiri (thumbnail dibenam base64), jadi boleh terus
diterbitkan sebagai link Artifact dan dibuka di phone.

Format JSON (contoh: tools/templates/storyboard-plan.example.json):
{
  "title": "Periuk Tekanan",            # nama job (jadi <title>)
  "client": "Kedai X",                   # pilihan
  "format": "9:16",                      # 9:16 | 16:9 | 1:1
  "style": "Sample 3 + R81",             # gaya dipilih (pilihan)
  "arc_note": "Kenapa susunan ni ...",   # ringkasan logik cerita
  "scenes": [
    {
      "src": "raw/IMG_0012.MOV",         # fail footage sebenar
      "in": 12.4, "out": 15.1,           # saat dalam fail asal
      "beat": "hook",                    # hook | masalah | bukti | klimaks | cta | lain
      "visual": "Close-up wap keluar",   # apa yang kelihatan / layout
      "caption": "WAP DIA GILA!",        # cadangan caption / teks atas skrin
      "transition": {"pick": "T1 hard cut", "alts": ["T8 zoom blur", "T3 whip pan"], "why": "..."},
      "sfx": "S2 whoosh",                # pilihan
      "why": "Visual paling dramatik, lulus R56 (< 3 s)",
      "thumbs": [12.6, 13.7, 14.8]       # pilihan: saat untuk thumbnail (lalai 3 frame sekata)
    }
  ]
}
"""
import base64
import html
import json
import os
import subprocess
import sys

BEATS = {
    "hook": ("Hook", "Tarik perhatian < 3 s"),
    "masalah": ("Masalah", "Kenapa penonton patut peduli"),
    "bukti": ("Bukti", "Tunjuk, jangan cerita"),
    "klimaks": ("Klimaks", "Momen paling kuat"),
    "cta": ("CTA", "Apa penonton patut buat"),
    "lain": ("Sambungan", "Jambatan antara babak"),
}
THUMB_W = {"9:16": 270, "16:9": 480, "1:1": 360}


def esc(s):
    return html.escape(str(s or ""), quote=True)


def tc(sec):
    sec = max(0.0, float(sec))
    m = int(sec // 60)
    return f"{m:02d}:{sec - m * 60:04.1f}"


def grab(src, t, width):
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", src, "-frames:v", "1",
           "-vf", f"scale={width}:-2", "-q:v", "5", "-f", "image2", "-c:v", "mjpeg", "pipe:1"]
    try:
        out = subprocess.run(cmd, capture_output=True, check=True, timeout=60).stdout
    except (subprocess.SubprocessError, OSError) as e:
        print(f"  ! thumbnail gagal {src} @ {t:.2f}s: {e}", file=sys.stderr)
        return None
    return "data:image/jpeg;base64," + base64.b64encode(out).decode() if out else None


def build(plan, base_dir):
    fmt = plan.get("format", "9:16")
    width = THUMB_W.get(fmt, 270)
    ratio = fmt.replace(":", " / ")
    scenes, pos = [], 0.0
    for i, s in enumerate(plan["scenes"], 1):
        a, b = float(s["in"]), float(s["out"])
        dur = max(0.05, b - a)
        src = s["src"] if os.path.isabs(s["src"]) else os.path.join(base_dir, s["src"])
        ts = s.get("thumbs") or [a + dur * f for f in (0.15, 0.5, 0.85)]
        thumbs = [u for u in (grab(src, t, width) for t in ts) if u]
        beat = s.get("beat", "lain").lower()
        if beat not in BEATS:
            beat = "lain"
        tr = s.get("transition") or {}
        if isinstance(tr, str):
            tr = {"pick": tr}
        scenes.append(dict(n=i, src=os.path.basename(s["src"]), a=a, b=b, dur=dur,
                           t0=pos, t1=pos + dur, beat=beat, thumbs=thumbs,
                           visual=s.get("visual", ""), caption=s.get("caption", ""),
                           tr_pick=tr.get("pick", "Hard cut"), tr_alts=tr.get("alts", []),
                           tr_why=tr.get("why", ""), sfx=s.get("sfx", ""), why=s.get("why", "")))
        pos += dur
        print(f"  babak {i}: {len(thumbs)} thumbnail", file=sys.stderr)
    return scenes, pos, ratio


def render(plan, scenes, total, ratio):
    title = plan.get("title", "Storyboard")
    # Arc bar: one segment per scene, width proportional to duration
    arc = "".join(
        f'<a class="seg b-{s["beat"]}" href="#s{s["n"]}" style="flex-grow:{s["dur"]:.2f}" '
        f'aria-label="Babak {s["n"]}, {BEATS[s["beat"]][0]}, {s["dur"]:.1f} saat"></a>'
        for s in scenes)
    used = [k for k in BEATS if any(s["beat"] == k for s in scenes)]
    legend = "".join(
        f'<li><i class="dot b-{k}"></i>{BEATS[k][0]} '
        f'<span>{sum(s["dur"] for s in scenes if s["beat"] == k):.1f}s</span></li>' for k in used)

    cards = []
    for s in scenes:
        imgs = "".join(f'<img src="{u}" alt="Frame {j + 1} babak {s["n"]}"{" hidden" if j else ""}>'
                       for j, u in enumerate(s["thumbs"])) or '<div class="nothumb">Tiada frame</div>'
        dots = "".join(f'<i{" class=on" if j == 0 else ""}></i>' for j in range(len(s["thumbs"]))) \
            if len(s["thumbs"]) > 1 else ""
        opts = [s["tr_pick"]] + list(s["tr_alts"])
        radios = "".join(
            f'<label class="opt"><input type="radio" name="tr{s["n"]}" id="tr{s["n"]}-{j}" value="{j}"'
            f'{" checked" if j == 0 else ""}><span>{esc(o)}{" <em>cadangan</em>" if j == 0 else ""}</span></label>'
            for j, o in enumerate(opts))
        cap = (f'<div class="capov">{esc(s["caption"])}</div>' if s["caption"] else "")
        cards.append(f'''
<article class="scene" id="s{s["n"]}" data-n="{s["n"]}">
  <div class="head">
    <span class="num">{s["n"]:02d}</span>
    <span class="chip b-{s["beat"]}">{BEATS[s["beat"]][0]}</span>
    <span class="tc">{tc(s["t0"])} → {tc(s["t1"])}</span>
    <span class="dur">{s["dur"]:.1f}s</span>
  </div>
  <div class="body">
    <button class="frame" type="button" style="aspect-ratio:{ratio}" aria-label="Tukar frame">{imgs}{cap}<span class="dots">{dots}</span></button>
    <div class="info">
      <p class="visual">{esc(s["visual"])}</p>
      <dl>
        <div><dt>Caption</dt><dd class="captxt">{esc(s["caption"]) or "—"}</dd></div>
        <div><dt>Transition masuk</dt><dd>{esc(s["tr_pick"])}</dd></div>
        {f'<div><dt>SFX</dt><dd>{esc(s["sfx"])}</dd></div>' if s["sfx"] else ""}
        <div><dt>Sumber</dt><dd class="mono">{esc(s["src"])} · {tc(s["a"])}–{tc(s["b"])}</dd></div>
      </dl>
      <p class="why"><b>Kenapa babak ni:</b> {esc(s["why"])}</p>
    </div>
  </div>
  <details>
    <summary>Pilih transition / tambah komen</summary>
    <fieldset><legend>Transition</legend>{radios}</fieldset>
    {f'<p class="trwhy">{esc(s["tr_why"])}</p>' if s["tr_why"] else ""}
    <div class="vote">
      <label><input type="radio" name="v{s["n"]}" id="v{s["n"]}-ok" value="ok"> OK</label>
      <label><input type="radio" name="v{s["n"]}" id="v{s["n"]}-ubah" value="ubah"> Ubah</label>
      <label><input type="radio" name="v{s["n"]}" id="v{s["n"]}-buang" value="buang"> Buang</label>
    </div>
    <textarea id="c{s["n"]}" rows="2" placeholder="Komen untuk babak {s["n"]} (pilihan)"></textarea>
  </details>
</article>''')

    meta = " · ".join(esc(x) for x in [plan.get("client"), plan.get("format", "9:16"),
                                         plan.get("style")] if x)
    return f'''<title>{esc(title)} Storyboard</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">
<style>
/* Layout: satu lajur kad babak macam jalur filem, bar arc cerita melekat di atas; 2 lajur di skrin lebar */
:root {{
  --bg:#f3f4f6; --surface:#ffffff; --fg:#15171c; --muted:#5b6170; --line:#dde0e6; --accent:#0e7c74;
  --hook:#d9480f; --masalah:#a35f00; --bukti:#2b6cb0; --klimaks:#9d2c8f; --cta:#18794e; --lain:#6b7280;
  --display:"Bricolage Grotesque", "Segoe UI", system-ui, sans-serif;
  --text:"Inter", system-ui, -apple-system, sans-serif;
  --mono:"JetBrains Mono", ui-monospace, Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#101216; --surface:#191c22; --fg:#eceef2; --muted:#9aa1ae; --line:#2a2e37; --accent:#3cc7b8;
  --hook:#ff7a45; --masalah:#e8a33d; --bukti:#6aa8ec; --klimaks:#d77ccb; --cta:#4cc38a; --lain:#9aa1ae; color-scheme:dark }} }}
:root[data-theme="dark"] {{
  --bg:#101216; --surface:#191c22; --fg:#eceef2; --muted:#9aa1ae; --line:#2a2e37; --accent:#3cc7b8;
  --hook:#ff7a45; --masalah:#e8a33d; --bukti:#6aa8ec; --klimaks:#d77ccb; --cta:#4cc38a; --lain:#9aa1ae; color-scheme:dark }}
* {{ box-sizing:border-box }}
body {{ background:var(--bg); color:var(--fg); font:15px/1.5 var(--text); margin:0 }}
body::before {{ content:""; position:fixed; inset:0 0 auto; height:env(safe-area-inset-top,0px); z-index:10; background:var(--bg) }}
.wrap {{ max-width:1100px; margin:0 auto; padding-block:20px 120px;
  padding-left:max(16px, env(safe-area-inset-left,0px)); padding-right:max(16px, env(safe-area-inset-right,0px)) }}
header h1 {{ font:800 clamp(26px,6vw,40px)/1.05 var(--display); margin:0 0 6px; text-wrap:balance }}
header .meta {{ color:var(--muted); margin:0 }}
.stats {{ display:flex; flex-wrap:wrap; gap:8px 20px; margin:14px 0 0; font:500 13px var(--mono); color:var(--muted) }}
.stats b {{ color:var(--fg); font-weight:500 }}
.arcbox {{ position:sticky; top:env(safe-area-inset-top,0px); z-index:5; background:var(--bg); padding:12px 0 10px; margin-top:16px; border-bottom:1px solid var(--line) }}
.arc {{ display:flex; gap:3px; height:14px }}
.seg {{ flex-basis:0; min-width:6px; border-radius:3px; background:var(--c); opacity:.9 }}
.seg:hover,.seg:focus-visible {{ opacity:1; outline:2px solid var(--fg); outline-offset:1px }}
.legend {{ display:flex; flex-wrap:wrap; gap:4px 14px; list-style:none; padding:0; margin:8px 0 0; font-size:12.5px; color:var(--muted) }}
.legend span {{ font-family:var(--mono) }}
.dot {{ display:inline-block; width:9px; height:9px; border-radius:50%; background:var(--c); margin-right:5px }}
.b-hook{{--c:var(--hook)}} .b-masalah{{--c:var(--masalah)}} .b-bukti{{--c:var(--bukti)}}
.b-klimaks{{--c:var(--klimaks)}} .b-cta{{--c:var(--cta)}} .b-lain{{--c:var(--lain)}}
.note {{ margin:16px 0 0; padding:12px 14px; border-left:3px solid var(--accent); background:var(--surface); max-width:70ch; color:var(--fg) }}
.note b {{ font-family:var(--display) }}
.grid {{ display:grid; gap:14px; margin-top:18px }}
@media (min-width:860px) {{ .grid {{ grid-template-columns:1fr 1fr }} }}
.scene {{ background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:12px; min-width:0; scroll-margin-top:90px }}
.head {{ display:flex; align-items:center; gap:8px; flex-wrap:wrap }}
.num {{ font:800 22px/1 var(--display); color:var(--muted) }}
.chip {{ font-size:11.5px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--c);
  border:1.5px solid var(--c); border-radius:99px; padding:1px 8px }}
.tc {{ font:500 12.5px var(--mono); color:var(--muted); margin-left:auto }}
.dur {{ font:500 12.5px var(--mono); background:var(--bg); border-radius:5px; padding:1px 6px }}
.body {{ display:grid; grid-template-columns:minmax(0,38%) minmax(0,1fr); gap:12px; margin-top:10px }}
.frame {{ position:relative; display:block; width:100%; max-width:100%; padding:0; border:0; border-radius:7px; overflow:hidden; background:#000; cursor:pointer; align-self:start }}
.frame img {{ width:100%; height:100%; object-fit:cover; display:block }}
.frame:focus-visible {{ outline:3px solid var(--accent); outline-offset:2px }}
.nothumb {{ color:#aaa; display:grid; place-items:center; height:100%; font-size:12px }}
.capov {{ position:absolute; left:6%; right:6%; bottom:22%; text-align:center; font:800 13px/1.15 var(--display);
  color:#fff; text-shadow:0 1px 3px #000, 0 0 8px #000; text-transform:uppercase }}
.dots {{ position:absolute; left:0; right:0; bottom:6px; display:flex; justify-content:center; gap:4px }}
.dots i {{ width:5px; height:5px; border-radius:50%; background:#fff; opacity:.45 }}
.dots i.on {{ opacity:1 }}
.info {{ min-width:0 }}
.visual {{ font-weight:600; margin:0 0 6px }}
dl {{ margin:0; display:grid; gap:4px }}
dl div {{ display:grid; gap:0 }}
dt {{ font-size:11px; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); white-space:nowrap }}
dd {{ margin:0; min-width:0; overflow-wrap:anywhere }}
.mono {{ font:500 12px var(--mono); color:var(--muted) }}
.why {{ margin:8px 0 0; font-size:14px; color:var(--fg) }}
.why b {{ color:var(--accent) }}
details {{ margin-top:10px; border-top:1px solid var(--line); padding-top:8px }}
summary {{ cursor:pointer; font-weight:600; color:var(--accent); font-size:14px; padding:4px 0 }}
fieldset {{ border:0; padding:0; margin:8px 0 0; display:grid; gap:6px }}
legend {{ font-size:11px; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); margin-bottom:4px }}
.opt {{ display:flex; gap:8px; align-items:center; padding:8px 10px; border:1px solid var(--line); border-radius:7px; cursor:pointer }}
.opt:has(input:checked) {{ border-color:var(--accent) }}
.opt em {{ font-style:normal; font-size:11px; color:var(--accent); margin-left:4px }}
.trwhy {{ font-size:13px; color:var(--muted); margin:6px 0 0 }}
.vote {{ display:flex; gap:14px; margin:10px 0 8px; flex-wrap:wrap }}
textarea {{ width:100%; font:inherit; color:var(--fg); background:var(--bg); border:1px solid var(--line); border-radius:7px; padding:8px }}
textarea:focus-visible, input:focus-visible {{ outline:2px solid var(--accent) }}
.bar {{ position:fixed; left:0; right:0; bottom:0; z-index:6; background:var(--surface); border-top:1px solid var(--line);
  padding-block:10px calc(10px + env(safe-area-inset-bottom,0px));
  padding-left:max(16px, env(safe-area-inset-left,0px)); padding-right:max(16px, env(safe-area-inset-right,0px));
  display:flex; gap:10px; align-items:center; justify-content:space-between }}
.bar p {{ margin:0; font-size:13px; color:var(--muted) }}
.bar button {{ font:600 14px var(--text); background:var(--accent); color:var(--surface); border:0; border-radius:8px; padding:10px 14px; cursor:pointer; white-space:nowrap }}
.bar textarea {{ position:absolute; left:-9999px }}
@media (max-width:420px) {{ .body {{ grid-template-columns:minmax(0,42%) minmax(0,1fr) }} .tc {{ margin-left:0 }} }}
@media (prefers-reduced-motion:reduce) {{ html {{ scroll-behavior:auto }} }}
html {{ scroll-behavior:smooth }}
</style>

<div class="wrap">
  <header>
    <h1>{esc(title)}</h1>
    <p class="meta">{meta}</p>
    <div class="stats"><span><b>{len(scenes)}</b> babak</span><span>durasi <b>{tc(total)}</b></span>
      <span>purata <b>{total / max(1, len(scenes)):.1f}s</b>/babak</span><span>status <b>sebelum render</b></span></div>
  </header>
  <div class="arcbox"><nav class="arc" aria-label="Arc cerita">{arc}</nav><ul class="legend">{legend}</ul></div>
  {f'<p class="note"><b>Logik cerita.</b> {esc(plan["arc_note"])}</p>' if plan.get("arc_note") else ""}
  <main class="grid">{"".join(cards)}</main>
</div>
<div class="bar"><p id="sum">Tekan frame untuk tukar gambar. Buka "Pilih transition" untuk ubah.</p>
  <button type="button" id="copy">Salin maklum balas</button><textarea id="fb" aria-hidden="true" tabindex="-1"></textarea></div>

<script>
document.querySelectorAll('.frame').forEach(f => {{
  const imgs = f.querySelectorAll('img'), dots = f.querySelectorAll('.dots i');
  if (imgs.length < 2) return;
  let k = 0;
  f.addEventListener('click', () => {{
    imgs[k].hidden = true; dots[k] && dots[k].classList.remove('on');
    k = (k + 1) % imgs.length;
    imgs[k].hidden = false; dots[k] && dots[k].classList.add('on');
  }});
}});
function feedback() {{
  const lines = [];
  document.querySelectorAll('.scene').forEach(s => {{
    const n = s.dataset.n, parts = [];
    const tr = s.querySelector('input[name="tr' + n + '"]:checked');
    if (tr && tr.value !== '0') parts.push('transition → ' + tr.parentElement.querySelector('span').firstChild.textContent.trim());
    const v = s.querySelector('input[name="v' + n + '"]:checked');
    if (v && v.value !== 'ok') parts.push(v.value.toUpperCase());
    const c = s.querySelector('#c' + n).value.trim();
    if (c) parts.push('"' + c + '"');
    if (parts.length) lines.push('#' + n + ': ' + parts.join(' · '));
  }});
  return lines.length ? 'Storyboard {esc(title)}:\\n' + lines.join('\\n') : 'Storyboard {esc(title)}: semua OK';
}}
function refresh() {{
  const t = feedback(), n = t.split('\\n').length - 1;
  document.getElementById('sum').textContent = n ? n + ' babak ada perubahan' : 'Tiada perubahan lagi (semua ikut cadangan)';
}}
document.addEventListener('change', refresh); document.addEventListener('input', refresh);
document.getElementById('copy').addEventListener('click', async e => {{
  const t = feedback(), btn = e.currentTarget;
  try {{ await navigator.clipboard.writeText(t); btn.textContent = 'Disalin — tampal dalam chat'; }}
  catch (_) {{ const fb = document.getElementById('fb'); fb.value = t; fb.style.position = 'static'; fb.removeAttribute('aria-hidden'); fb.select(); btn.textContent = 'Salin teks di atas'; }}
  setTimeout(() => btn.textContent = 'Salin maklum balas', 2500);
}});
</script>
'''


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    plan_path, out_path = sys.argv[1], sys.argv[2]
    with open(plan_path, encoding="utf-8") as f:
        plan = json.load(f)
    scenes, total, ratio = build(plan, os.path.dirname(os.path.abspath(plan_path)))
    page = render(plan, scenes, total, ratio)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"OK {out_path} ({len(page) / 1e6:.2f} MB, {len(scenes)} babak, {tc(total)})")


if __name__ == "__main__":
    main()
