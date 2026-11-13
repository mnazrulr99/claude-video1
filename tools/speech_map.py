#!/usr/bin/env python3
"""PETA UCAPAN (speech map) — langkah PERTAMA untuk video bercakap/berskrip (SOP Fasa 3).

Dari transkrip VERBATIM + audio, hasilkan:
  A. Senarai TRIM (jangan potong lagi — pengguna pilih): senyap, filled pause (aa/erm), filler words,
     ulang perkataan, ulang frasa / false start (tersasul & ulang semula), jeda tengah ayat, perkataan tak pasti.
  B. Peta PELUANG: di mana sesuai letak motion grafik / animasi / SFX / transition, ikut isi ayat.
  C. Calon HOOK (ranking) — untuk diuji dengan R56.

Guna:
  python3 -I tools/transcribe.py <video> tv.json --verbatim
  python3 -I tools/speech_map.py tv.json <video> [--keywords "Rejuran,toner,beg kuning"] [--json out.json] [--md out.md]
Nota: ini CADANGAN untuk semakan manusia — Whisper boleh terlepas/tersalah dengar (R54).
"""
import argparse, json, re, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument("transcript"); ap.add_argument("video", nargs="?")
ap.add_argument("--keywords", default="", help="nama produk/brand/orang, dipisah koma")
ap.add_argument("--silence-db", type=float, default=-40); ap.add_argument("--silence-min", type=float, default=0.4)
ap.add_argument("--json"); ap.add_argument("--md")
a = ap.parse_args()

segs = json.load(open(a.transcript))
W = []
for si, seg in enumerate(segs):
    for x in seg["words"]:
        raw = x["word"].strip()
        W.append(dict(raw=raw, w=re.sub(r"[^\w-]", "", raw.lower()), s=x["start"], e=x["end"], p=x.get("prob", 1), seg=si))
W = [w for w in W if w["w"]]
KW = [k.strip().lower() for k in a.keywords.split(",") if k.strip()]

# ---------- Kamus (BM santai + English) ----------
FILLED = {"aa", "aaa", "aah", "ah", "ahh", "erm", "em", "emm", "emmm", "uh", "uhh", "um", "umm", "hmm", "hm", "err", "eh", "ehh", "mm"}
FILLER = {"macam", "kan", "tau", "tahu", "so", "like", "basically", "actually", "okay", "ok", "ha", "haa", "lah", "la", "jelah", "kot",
          "you", "know", "kiranya", "maksudnya", "apa", "tu", "ni"}   # hanya ditanda bila berdiri sendiri/berulang
FILLER_PHRASES = [("you", "know"), ("macam", "mana", "eh"), ("apa", "nama"), ("macam", "tu", "lah"), ("so", "basically")]
EMO = {"wow", "best", "gila", "sedap", "murah", "mahal", "terbaik", "cantik", "lawa", "wangi", "jimat", "berbaloi", "worth", "ya", "allah",
       "omg", "serius", "confirm", "power", "rugi", "untung", "terkejut", "pelik", "pedas", "lembut", "glowing", "hilang", "bapak"}
POINT = {"tengok", "nampak", "macam", "ni", "sini", "ini", "lihat", "see", "look", "this"}
CTA = {"grab", "beli", "order", "checkout", "check", "klik", "link", "dm", "whatsapp", "beg", "kuning", "bakul", "follow", "komen", "comment", "try"}
SHIFT = {"next", "lepas", "seterusnya", "pastu", "lepastu", "kedua", "ketiga", "and", "now", "so", "tapi", "but", "yang", "paling", "penting"}
NUM_RE = re.compile(r"^(rm\d|\d|satu|dua|tiga|empat|lima|enam|tujuh|lapan|sembilan|sepuluh|seratus|ribu|ringgit|sen|percent|peratus|%)")

def T(t): return f"{t:6.2f}"
trim, opp = [], []

# ---------- A1. Senyap (audio sebenar) ----------
dur = None
if a.video:
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", a.video, "-vn", "-af",
                          f"silencedetect=noise={a.silence_db}dB:d={a.silence_min}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", err)]
    en = [(float(x), float(d)) for x, d in re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", err)]
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    if m: dur = int(m[1])*3600 + int(m[2])*60 + float(m[3])
    if len(st) > len(en) and dur: en.append((dur, dur - st[-1]))
    for (e, d) in en:
        s0 = max(0.0, e - d)
        where = "awal video" if s0 < 0.3 else ("hujung video" if dur and e > dur - 0.3 else "antara ayat")
        trim.append((s0, e, "SENYAP", f"{d:.1f}s ({where})", "buang / pendekkan ke ±0.1 s"))

# ---------- A2. Disfluency dari transkrip ----------
for i, w in enumerate(W):
    prev = W[i-1] if i else None
    if w["w"] in FILLED:
        trim.append((w["s"], w["e"], "FILLED PAUSE", f'"{w["raw"]}"', "buang"))
    elif w["w"] in FILLER and (prev and prev["w"] == w["w"]):
        trim.append((prev["s"], w["e"], "FILLER berulang", f'"{prev["raw"]} {w["raw"]}"', "buang satu"))
    if prev and w["w"] == prev["w"] and w["w"] not in FILLED and w["s"] - prev["e"] < 1.0 and not re.match(r"^\w+-\w+$", w["raw"]):
        trim.append((prev["s"], w["e"], "ULANG perkataan", f'"{prev["raw"]} {w["raw"]}"', "buang yang pertama"))
    if w["p"] < 0.3 and w["w"] not in FILLED:
        trim.append((w["s"], w["e"], "TAK PASTI", f'"{w["raw"]}" (prob {w["p"]:.2f}) — dengar semula', "semak (R54)"))
    if prev and 0.7 < w["s"] - prev["e"] < 3 and not re.search(r"[.?!]$", prev["raw"]):
        trim.append((prev["e"], w["s"], "JEDA tengah ayat", f'{w["s"]-prev["e"]:.1f}s "{prev["raw"]} … {w["raw"]}"', "rapatkan"))
    # perkataan terpotong (tersasul): sangat pendek & diikuti perkataan bermula sama
    if prev and len(prev["w"]) <= 3 and w["w"].startswith(prev["w"]) and w["w"] != prev["w"] and prev["e"] - prev["s"] < 0.25:
        trim.append((prev["s"], prev["e"], "TERSASUL (terpotong)", f'"{prev["raw"]}" → "{w["raw"]}"', "buang serpihan"))
for ph in FILLER_PHRASES:
    n = len(ph)
    for i in range(len(W) - n + 1):
        if tuple(x["w"] for x in W[i:i+n]) == ph:
            trim.append((W[i]["s"], W[i+n-1]["e"], "FILLER frasa", '"' + " ".join(x["raw"] for x in W[i:i+n]) + '"', "pertimbang buang"))
# ulang frasa / false start (ayat dimulakan semula)
for n in (5, 4, 3, 2):
    for i in range(len(W) - n):
        g = [x["w"] for x in W[i:i+n]]
        if all(x in FILLED for x in g): continue
        for j in range(i + 1, min(len(W) - n + 1, i + n + 10)):
            if [x["w"] for x in W[j:j+n]] == g and W[j]["s"] - W[i]["s"] < 8:
                trim.append((W[i]["s"], W[j]["s"], f"ULANG FRASA / mula semula ({n})",
                             '"' + " ".join(x["raw"] for x in W[i:j]) + '" → diulang', "buang cubaan pertama"))
                break

# jeda ANTARA ayat dari transkrip (tangkap jeda walaupun ada bunyi latar)
for i in range(1, len(W)):
    g = W[i]["s"] - W[i-1]["e"]
    if g >= 0.5 and re.search(r"[.?!,]$", W[i-1]["raw"]) and not any(o[2] == "SENYAP" and o[0] <= W[i-1]["e"] + 0.2 and o[1] >= W[i]["s"] - 0.2 for o in trim):
        trim.append((W[i-1]["e"], W[i]["s"], "JEDA antara ayat", f'{g:.1f}s selepas "{W[i-1]["raw"]}"', "rapatkan ke ±0.1 s"))

# dedup (jenis + masa hampir sama)
seen, T_ = set(), []
for o in sorted(trim):
    k = (round(o[0], 1), o[2].split()[0])
    if k in seen: continue
    seen.add(k); T_.append(o)
trim = T_

# ---------- B. Peta peluang (setiap ayat) ----------
sent = []
for si, seg in enumerate(segs):
    ws = [w for w in W if w["seg"] == si and w["w"] not in FILLED]
    if not ws: continue
    sent.append(dict(s=ws[0]["s"], e=ws[-1]["e"], text=" ".join(w["raw"] for w in ws), ws=ws))
for k, se in enumerate(sent):
    ids = [w["w"] for w in se["ws"]]; text = se["text"]; tips = []
    NUMW = {"satu","dua","tiga","empat","lima","enam","tujuh","lapan","sembilan","sepuluh","seratus"}
    UNIT = {"ringgit","rm","sen","ribu","peratus","percent","cm","ml","kg","gram","biji","set","pcs","helai","saiz","size"}
    nums = []
    for j, w in enumerate(se["ws"]):
        nb = [x["w"] for x in se["ws"][max(0,j-1):j+2] if x is not w]
        if re.match(r"^(rm)?\d", w["w"]) or w["w"] in ("ringgit","peratus","percent") or (w["w"] in NUMW and any(x in UNIT or x in NUMW or re.match(r"^\d", x) for x in nb)):
            nums.append(w)
    if nums:
        tips.append(("MOTION GRAFIK", f'label angka/harga pada "{nums[0]["raw"]}" @ {nums[0]["s"]:.2f}s (pop + SFX pop) — R19/R1b'))
    kws = [w for w in se["ws"] if any(kw in w["w"] or w["w"] in kw.split() for kw in KW)] if KW else []
    if kws:
        tips.append(("STICKER/LOGO", f'nama "{kws[0]["raw"]}" @ {kws[0]["s"]:.2f}s → sticker produk (R52) / logo brand (R33)'))
    emo = [w for w in se["ws"] if w["w"] in EMO]
    if emo:
        tips.append(("PUNCH-IN + SFX", f'emosi "{emo[0]["raw"]}" @ {emo[0]["s"]:.2f}s → punch-in, perkataan dibesarkan (R27), riser/boing (R49)'))
    if any(w in POINT for w in ids) and any(x in ids for x in ("tengok", "nampak", "macam", "lihat", "see", "look")):
        p = next(w for w in se["ws"] if w["w"] in POINT)
        tips.append(("CLOSE-UP", f'tunjuk sesuatu @ {p["s"]:.2f}s → close-up/punch-in produk (R7) + label bahagian (R1b)'))
    if text.strip().endswith("?") or (ids and ids[-1] in ("tak", "kan", "ke", "eh")):
        tips.append(("ANIMASI TEKS", f'soalan @ {se["s"]:.2f}s → teks soalan/emoji pop'))
    if any(w in CTA for w in ids):
        tips.append(("CTA", f'@ {se["s"]:.2f}s → grafik CTA zon selamat (R13) + SFX pop'))
    gap = se["s"] - sent[k-1]["e"] if k else 0
    if k and (gap > 0.7 or (ids and ids[0] in SHIFT)):
        tips.append(("TRANSITION / TUKAR VISUAL", f'pertukaran topik @ {se["s"]:.2f}s (jeda {gap:.1f}s / "{se["ws"][0]["raw"]}") → tukar sudut/B-roll; transition hanya jika sesuai (R53)'))
    se["tips"] = tips
    # skor hook
    sc = 2*len(emo) + 2*len(nums) + (2 if text.strip().endswith(("?", "!")) else 0) + 2*len(kws)
    n = len(ids); sc += 2 if 3 <= n <= 12 else (-2 if n > 18 else 0)
    if ids and ids[0] in ("hai", "hi", "assalamualaikum", "okay", "ok", "so", "korang", "guys"): sc -= 2   # mukadimah (R45)
    se["hook"] = sc
for k in range(1, len(sent)):
    if sent[k]["s"] - sent[k-1]["e"] <= 0.7 and not any(t[0].startswith("TRANSITION") for t in sent[k]["tips"]) and k % 3 == 0:
        sent[k]["tips"].append(("TUKAR VISUAL", f'@ {sent[k]["s"]:.2f}s → kekalkan visual bertukar setiap 2–4 s (R25)'))

hooks = sorted(sent, key=lambda x: -x["hook"])[:3]

# ---------- Output ----------
L = ["## A. Senarai TRIM (belum dipotong — pilih nombor yang dibuang)", "",
     "| # | Masa (s) | Jenis | Butiran | Cadangan |", "|---|---|---|---|---|"]
for n, (s, e, k, d, c) in enumerate(trim, 1): L.append(f"| {n} | {T(s)}–{T(e)} | {k} | {d} | {c} |")
if not trim: L.append("| – | – | – | Tiada dikesan | – |")
tot = sum(e - s for s, e, k, *_ in trim if k in ("SENYAP", "FILLED PAUSE", "JEDA tengah ayat", "JEDA antara ayat"))
L += ["", f"_Anggaran masa boleh dijimatkan (senyap + filled pause + jeda): ±{tot:.1f}s_", "",
      "## B. Peta peluang (motion grafik · animasi · SFX · transition)", "",
      "| Masa (s) | Ayat | Peluang |", "|---|---|---|"]
for se in sent:
    tips = "<br>".join(f"**{a_}**: {b_}" for a_, b_ in se["tips"]) or "—"
    L.append(f"| {T(se['s'])}–{T(se['e'])} | {se['text'][:70]} | {tips} |")
L += ["", "## C. Calon HOOK (uji dengan R56: menarik < 3 s + berkait dengan isi)", ""]
for n, h in enumerate(hooks, 1): L.append(f"{n}. **{h['s']:.2f}–{h['e']:.2f}s** — \"{h['text']}\" (skor {h['hook']})")
md = "\n".join(L)
print(md)
if a.md: open(a.md, "w").write(md)
if a.json:
    json.dump(dict(trim=[dict(start=s, end=e, type=k, detail=d, action=c) for s, e, k, d, c in trim],
                   sentences=[dict(start=x["s"], end=x["e"], text=x["text"], tips=x["tips"], hook_score=x["hook"]) for x in sent],
                   hooks=[dict(start=h["s"], end=h["e"], text=h["text"]) for h in hooks]), open(a.json, "w"), ensure_ascii=False, indent=1)
