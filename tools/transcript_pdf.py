#!/usr/bin/env python3
"""Transkrip PDF untuk semakan pengguna — setiap perkataan dengan masa (durasi), bahagian yang di-trim ditanda.

Guna:
  python3 -I tools/transcript_pdf.py tv.json out.pdf --map speech-map.json --cut 1,2,3,7-12 \
      [--title "Periuk Stainless Steel"] [--keywords "periuk,Yana"] [--fixes fixes.json]
  tv.json        : transkrip verbatim (tools/transcribe.py --verbatim)
  --map/--cut    : JSON dari tools/speech_map.py --json, dan nombor trim yang pengguna pilih untuk dibuang
  --fixes        : (pilihan) {"perkataan asal": "pembetulan"} — dipaparkan sebagai pembetulan
Isi PDF: ringkasan durasi asal → selepas trim, legenda, jadual ayat (masa ASAL & masa SELEPAS TRIM, setiap perkataan
bertanda masa mula), baris kosong "Pembetulan" untuk ditulis, dan senarai trim (dibuang / dikekalkan).
"""
import argparse, json, re, html
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ap = argparse.ArgumentParser()
ap.add_argument("transcript"); ap.add_argument("out")
ap.add_argument("--map"); ap.add_argument("--cut", default="")
ap.add_argument("--title", default="Transkrip"); ap.add_argument("--keywords", default="")
ap.add_argument("--fixes")
a = ap.parse_args()

for name, f in (("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"), ("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")):
    pdfmetrics.registerFont(TTFont(name, f))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DVB", italic="DV", boldItalic="DVB")

segs = json.load(open(a.transcript))
fixes = json.load(open(a.fixes)) if a.fixes else {}
KW = [k.strip().lower() for k in a.keywords.split(",") if k.strip()]

# ---- trim yang dipilih ----
trims, chosen = [], set()
for part in [p for p in a.cut.split(",") if p.strip()]:
    if "-" in part: x, y = part.split("-"); chosen |= set(range(int(x), int(y) + 1))
    else: chosen.add(int(part))
if a.map:
    m = json.load(open(a.map))
    for n, t in enumerate(m["trim"], 1):
        trims.append(dict(n=n, s=t["start"], e=t["end"], type=t["type"], detail=t["detail"], cut=n in chosen))
cut_ranges = sorted((t["s"], t["e"]) for t in trims if t["cut"])
merged = []
for s, e in cut_ranges:
    if merged and s <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], e)
    else: merged.append([s, e])

def is_cut(s, e):
    return any(s >= a0 - 0.02 and e <= b0 + 0.02 for a0, b0 in merged)
def new_t(t):
    return t - sum(max(0, min(e, t) - s) for s, e in merged)

raw_end = max(w["end"] for sg in segs for w in sg["words"]) if segs else 0
removed = sum(e - s for s, e in merged)

# ---- gaya ----
S = lambda **k: ParagraphStyle("x", **{"fontName": "DV", **k})
st_title = S(fontSize=16, leading=20, fontName="DVB")
st_small = S(fontSize=8, leading=11, textColor=colors.HexColor("#555555"))
st_body = S(fontSize=9.5, leading=17)
st_cell = S(fontSize=8, leading=10)

def word_html(w):
    raw = w["word"].strip(); key = re.sub(r"[^\w-]", "", raw.lower())
    t = html.escape(raw)
    if key in {k.lower() for k in fixes}:
        fix = next(v for k, v in fixes.items() if k.lower() == key)
        t = f'<strike>{t}</strike> <font color="#1a7f37"><b>{html.escape(fix)}</b></font>'
    elif any(k in key or key in k.split() for k in KW):
        t = f'<font color="#0b57d0"><b>{t}</b></font>'
    if w.get("prob", 1) < 0.5:
        t = f'<font backColor="#fff3b0">{t}</font>'
    if is_cut(w["start"], w["end"]):
        t = f'<font color="#c62828"><strike>{t}</strike></font>'
    return f'{t}<font size="6" color="#8a8a8a"> {w["start"]:.1f}</font>'

story = [Paragraph(html.escape(a.title) + " — Transkrip untuk semakan", st_title), Spacer(1, 4)]
story.append(Paragraph(
    f"Durasi ucapan asal: <b>{raw_end:.1f}s</b> · Dibuang (trim dipilih): <b>{removed:.1f}s</b> · "
    f"Anggaran selepas trim: <b>{raw_end - removed:.1f}s</b>", st_small))
story.append(Spacer(1, 3))
story.append(Paragraph(
    'Legenda: <font color="#c62828"><strike>merah bergaris</strike></font> = dibuang · '
    '<font backColor="#fff3b0">kuning</font> = Whisper tak pasti (sila semak) · '
    '<font color="#0b57d0"><b>biru</b></font> = nama/produk · '
    '<strike>asal</strike> <font color="#1a7f37"><b>hijau</b></font> = pembetulan · '
    'nombor kecil kelabu = saat mula perkataan (masa asal).', st_small))
story.append(Spacer(1, 8))

rows = [[Paragraph("<b>#</b>", st_cell), Paragraph("<b>Masa asal</b>", st_cell), Paragraph("<b>Selepas trim</b>", st_cell),
         Paragraph("<b>Ayat (setiap perkataan + saat)</b>", st_cell), Paragraph("<b>Pembetulan</b>", st_cell)]]
ev = []  # gabung ayat + senyap yang dibuang ikut masa
for i, sg in enumerate(segs):
    if sg["words"]: ev.append(("seg", sg["words"][0]["start"], sg))
for t in trims:
    if t["cut"] and t["type"] in ("SENYAP", "JEDA antara ayat"): ev.append(("sil", t["s"], t))
ev.sort(key=lambda x: x[1])
n = 0; style_cmds = []
for kind, _, obj in ev:
    if kind == "sil":
        rows.append(["", Paragraph(f'{obj["s"]:.2f}–{obj["e"]:.2f}', st_cell), Paragraph("—", st_cell),
                     Paragraph(f'<font color="#c62828"><i>[{obj["type"].lower()} {obj["e"]-obj["s"]:.1f}s — dibuang]</i></font>', st_cell), ""])
        continue
    n += 1; ws = obj["words"]
    s0, e0 = ws[0]["start"], ws[-1]["end"]
    alive = [w for w in ws if not is_cut(w["start"], w["end"])]
    nt = f'{new_t(alive[0]["start"]):.2f}–{new_t(alive[-1]["end"]):.2f}' if alive else "dibuang"
    rows.append([Paragraph(str(n), st_cell), Paragraph(f"{s0:.2f}–{e0:.2f}", st_cell), Paragraph(nt, st_cell),
                 Paragraph(" ".join(word_html(w) for w in ws), st_body), ""])
tbl = Table(rows, colWidths=[8*mm, 24*mm, 24*mm, 96*mm, 34*mm], repeatRows=1)
tbl.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cfcfcf")),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f0f0f0")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
]))
story.append(tbl)

if trims:
    story += [PageBreak(), Paragraph("Senarai trim (dari peta ucapan)", st_title), Spacer(1, 6)]
    tr = [[Paragraph(f"<b>{h}</b>", st_cell) for h in ("#", "Masa asal", "Jenis", "Butiran", "Status")]]
    for t in trims:
        status = '<font color="#c62828"><b>DIBUANG</b></font>' if t["cut"] else '<font color="#1a7f37">dikekalkan</font>'
        tr.append([Paragraph(str(t["n"]), st_cell), Paragraph(f'{t["s"]:.2f}–{t["e"]:.2f}', st_cell),
                   Paragraph(html.escape(t["type"]), st_cell), Paragraph(html.escape(t["detail"]), st_cell), Paragraph(status, st_cell)])
    t2 = Table(tr, colWidths=[8*mm, 24*mm, 38*mm, 82*mm, 30*mm], repeatRows=1)
    t2.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cfcfcf")),
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f0f0f0")), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(t2)

def footer(c, d):
    c.setFont("DV", 7); c.setFillColor(colors.grey)
    c.drawRightString(A4[0] - 12*mm, 8*mm, f"Halaman {d.page}")
SimpleDocTemplate(a.out, pagesize=A4, leftMargin=12*mm, rightMargin=12*mm, topMargin=12*mm, bottomMargin=14*mm,
                  title=f"{a.title} — Transkrip").build(story, onFirstPage=footer, onLaterPages=footer)
print("ok", a.out)
