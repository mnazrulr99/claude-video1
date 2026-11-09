#!/usr/bin/env python3
"""Tandakan ayat TERSANGKUT / DIULANG daripada transkrip (R24). TIDAK memotong apa-apa — hanya senarai untuk pengguna.

Guna: python3 -I tools/stutter.py <transcript.json> [--fix fix.json]
Kesan: (1) perkataan diulang berturut ("aku aku"), (2) frasa 2–4 perkataan diulang dalam ±6 s (ulang ayat / cuba semula),
(3) perkataan isian (erm, emm, aa, eh, uh, hmm), (4) jeda panjang di tengah ayat (>0.8 s), (5) perkataan keyakinan rendah (Whisper prob < 0.3).
"""
import json, re, sys
t = json.load(open(sys.argv[1]))
ws = [dict(w=re.sub(r"[^\w-]", "", x["word"].lower()), raw=x["word"], s=x["start"], e=x["end"], p=x.get("prob", 1)) for seg in t for x in seg["words"]]
ws = [w for w in ws if w["w"]]
FILL = {"erm","emm","em","aa","aaa","eh","uh","um","hmm","err","ah","ahh"}
out = []
for i, w in enumerate(ws):
    if i and w["w"] == ws[i-1]["w"] and w["s"] - ws[i-1]["e"] < 1.0:
        out.append((ws[i-1]["s"], w["e"], "ULANG perkataan", f'"{ws[i-1]["raw"].strip()} {w["raw"].strip()}"'))
    if w["w"] in FILL: out.append((w["s"], w["e"], "ISIAN", f'"{w["raw"].strip()}"'))
    if w["p"] < 0.3: out.append((w["s"], w["e"], "TAK PASTI (Whisper)", f'"{w["raw"].strip()}" (prob {w["p"]})'))
    if i and 0.8 < w["s"] - ws[i-1]["e"] < 3 and not re.search(r"[.?!,]$", ws[i-1]["raw"].strip()):
        out.append((ws[i-1]["e"], w["s"], "JEDA tengah ayat", f'{w["s"]-ws[i-1]["e"]:.1f}s antara "{ws[i-1]["raw"].strip()}" & "{w["raw"].strip()}"'))
for n in (4, 3, 2):
    for i in range(len(ws) - n):
        g = [x["w"] for x in ws[i:i+n]]
        for j in range(i + n, min(len(ws) - n + 1, i + n + 12)):
            if [x["w"] for x in ws[j:j+n]] == g and ws[j]["s"] - ws[i]["s"] < 6:
                out.append((ws[i]["s"], ws[j+n-1]["e"], f"ULANG frasa ({n} perkataan)", '"' + " ".join(x["raw"].strip() for x in ws[i:i+n]) + '" ×2'))
                break
seen, res = set(), []
for o in sorted(out):
    k = (round(o[0], 1), o[2].split()[0])
    if k in seen: continue
    seen.add(k); res.append(o)
print(f"{'#':>3} | {'Masa (s)':>13} | {'Jenis':<22} | Butiran")
for n, (a, b, k, d) in enumerate(res, 1): print(f"{n:>3} | {a:6.2f}–{b:6.2f} | {k:<22} | {d}")
if not res: print("Tiada ayat tersangkut/ulang dikesan.")
