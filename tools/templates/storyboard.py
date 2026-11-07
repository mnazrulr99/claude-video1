import sys, json, subprocess, io
sys.path.insert(0, sys.argv[1]); import plan as P
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W = sys.argv[2]; RAW = f"{W}/raw.mp4"
FB = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
FXB = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
FR = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
FS = "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf"
f = lambda p, s: ImageFont.truetype(p, s)
PW, PH = 360, 640
words = [w for s in json.load(open(f"{W}/transcript.json")) for w in s["words"]]
def fix(w): w = w.strip(",.?"); return P.FIXES.get(w, w).upper()

def frame(t, zoom):
    png = subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",RAW,"-frames:v","1","-f","image2pipe","-vcodec","png","-"],capture_output=True).stdout
    im = Image.open(io.BytesIO(png)).convert("RGB")
    im = im.resize((PW, round(im.height*PW/im.width)), Image.LANCZOS)
    top = (im.height-PH)//2; im = im.crop((0, top, PW, top+PH))
    if zoom > 1:
        cw, ch = PW/zoom, PH/zoom; x, y = (PW-cw)/2, (PH-ch)/2.6
        im = im.crop((int(x), int(y), int(x+cw), int(y+ch))).resize((PW, PH), Image.LANCZOS)
    return im

def outline_text(d, xy, txt, font, fill, stroke=(0,0,0), sw=3, anchor="mm"):
    d.text(xy, txt, font=font, fill=fill, stroke_width=sw, stroke_fill=stroke, anchor=anchor)

def caption(d, t):
    # 3 perkataan sekitar t, perkataan aktif kuning
    idx = min(range(len(words)), key=lambda i: abs(words[i]["start"]-t))
    s = max(0, idx-1); grp = words[s:s+3]
    font = f(FXB, 19); parts = [fix(w["word"]) for w in grp]
    widths = [d.textlength(p+" ", font=font) for p in parts]; x = PW/2 - sum(widths)/2; y = PH*0.70
    for p, wdt, w in zip(parts, widths, grp):
        col = (255,230,0) if w is words[idx] else (255,255,255)
        d.text((x, y), p, font=font, fill=col, stroke_width=3, stroke_fill=(0,0,0), anchor="lm"); x += wdt

def check_item(d, y, txt):
    font = f(FXB, 17); tw = d.textlength(txt, font=font)
    d.rounded_rectangle((18, y-17, 18+tw+52, y+17), 17, fill=(255,255,255))
    d.rounded_rectangle((24, y-12, 48, y+12), 6, fill=(46,184,92))
    d.line([(29,y),(35,y+6),(44,y-7)], fill="white", width=4)
    d.text((56, y), txt, font=font, fill=(30,30,30), anchor="lm")

def overlay(im, g, t):
    d = ImageDraw.Draw(im); kind, txt = g[2], g[3]
    if kind == "title":
        a, b = txt.split("|")
        outline_text(d, (PW/2, 78), a, f(FS, 30), "white", sw=3)
        outline_text(d, (PW/2, 120), b, f(FB, 46), (255,230,0), sw=4)
    elif kind == "sizes":
        n = sum(1 for s in P.SIZE_TIMES if s <= t + 0.01) or 5
        font = f(FB, 22); x = 22
        for s in txt.split("|")[:n]:
            d.ellipse((x, 205, x+56, 261), fill=(255,255,255), outline=(255,230,0), width=4)
            d.text((x+28, 233), s, font=font, fill=(214,40,120), anchor="mm"); x += 64
        outline_text(d, (PW/2, 285), "SAIZ (cm)", f(FXB, 18), "white", sw=3)
    elif kind == "check":
        for i, line in enumerate(txt.split("|")): check_item(d, 250 + i*46, line)
    elif kind == "badge":
        b = Image.new("RGBA", (240, 66), (0,0,0,0)); bd = ImageDraw.Draw(b)
        bd.rounded_rectangle((0,0,239,65), 14, fill=(230,30,50)); bd.text((120,33), txt, font=f(FB, 27), fill=(255,230,0), anchor="mm", stroke_width=2, stroke_fill=(120,0,10))
        b = b.rotate(-6, expand=True, resample=Image.BICUBIC); im.paste(b, ((PW-b.width)//2 - 40, 110), b)
    elif kind == "gift":
        check_item(d, 250, "🎁 " .replace("🎁 ","") + txt)
    elif kind == "cta":
        font = f(FB, 22); tw = d.textlength(txt, font=font)
        d.rounded_rectangle((PW/2-tw/2-46, 520, PW/2+tw/2+24, 566), 23, fill=(255,214,0))
        d.rounded_rectangle((PW/2-tw/2-36, 533, PW/2-tw/2-10, 558), 4, fill=(255,140,0))
        d.arc((PW/2-tw/2-30, 524, PW/2-tw/2-16, 540), 180, 360, fill=(255,140,0), width=3)
        d.text((PW/2-tw/2, 543), txt, font=font, fill=(20,20,20), anchor="lm")

PANELS = [  # (src_t_for_frame, hook?, nota)
    (10.70, True,  "HOOK (klip 1s): angkat penutup kaca|Audio asal dimatikan · SFX whoosh di cut|Tiada caption"),
    (0.80,  False, "Title: Periuk Stainless Steel MURAH!|(serif putih + MURAH! kuning tebal, typewriter)|SFX: sparkle"),
    (6.60,  False, "Saiz 16·18·20·22·24 pop satu-satu|ikut masa disebut · SFX pop setiap saiz|Punch-in 1.15× (6.45s src)"),
    (11.80, False, "✓ Penutup kaca solid (pill putih)|SFX: ding"),
    (17.90, False, "Badge HARGA TURUN! (merah/kuning)|Punch-in 1.12× · SFX: impact"),
    (25.00, False, "✓ Beli set 5 lagi JIMAT|SFX: ding"),
    (33.60, False, "✓ Stainless steel  ✓ Warna menarik|ditanda satu-satu · Punch-in 1.15×|SFX: ding ×2"),
    (40.90, False, "✓ Ada penutup = hygiene|SFX: ding"),
    (43.60, False, "✓ Sesuai jadi hadiah (ikon hadiah)|Punch-in 1.12× · SFX: chime"),
    (50.00, False, "CTA: Tekan beg kuning (pill kuning)|SFX: pop · kemudian cut ke hitam 0.6s|+ ding penutup"),
]
def zoom_at(t):
    for a, b, z in P.SEGMENTS:
        if a <= t <= b: return z
    return 1.0

cards = []
for i, (t, hook, note) in enumerate(PANELS, 1):
    im = frame(t, 1.0 if hook else zoom_at(t))
    if hook:
        d = ImageDraw.Draw(im)
    else:
        for g in P.GRAPHICS:
            if g[0] <= t <= g[1]: overlay(im, g, t)
        caption(ImageDraw.Draw(im), t)
    o0 = 0.0 if hook else P.src_to_out(t)
    # cari had babak
    card = Image.new("RGB", (PW, PH+150), (24,24,28)); card.paste(im, (0,0)); d = ImageDraw.Draw(card)
    if hook: rng = "0.0 – 1.0s"
    else:
        g = next((g for g in P.GRAPHICS if g[0] <= t <= g[1]), None)
        rng = f"{P.src_to_out(g[0]):.1f} – {P.src_to_out(g[1]):.1f}s" if g else f"{o0:.1f}s"
    d.rounded_rectangle((8, PH+8, 70, PH+38), 8, fill=(255,230,0)); d.text((39, PH+23), f"#{i}", font=f(FB,18), fill="black", anchor="mm")
    d.text((80, PH+23), rng, font=f(FB,20), fill="white", anchor="lm")
    for j, line in enumerate(note.split("|")):
        d.text((10, PH+54+j*28), line, font=f(FR,15), fill=(220,220,220), anchor="lm")
    cards.append(card)

for p in range(2):
    sheet = Image.new("RGB", (5*PW+6*16, PH+150+90), (14,14,16)); d = ImageDraw.Draw(sheet)
    d.text((16, 45), f"STORYBOARD — Periuk Stainless Steel (Ujian)  ·  halaman {p+1}/2  ·  Gaya: Sample 3 + Sample 2  ·  Caption kuning  ·  Tiada BGM  ·  ±52s", font=f(FB,26), fill="white", anchor="lm")
    for k, c in enumerate(cards[p*5:(p+1)*5]): sheet.paste(c, (16 + k*(PW+16), 80))
    sheet.save(f"{sys.argv[3]}/storyboard-{p+1}.jpg", quality=90)
print("ok")
