# Caption 1-3 perkataan (R27) dari transkrip verbatim, dipetakan ke timeline output.
import json, re, os
import plan as P
TR = os.environ.get("TRDIR", "/tmp/claude-0/-home-user-claude-video1/d5755f05-4ed3-55d8-b207-48cc5aabe1ba/scratchpad/job1/tr")
KEY = {"RENDANG", "LEMANG", "SATE", "LONTONG", "SELERA", "MESRA", "QR", "SAMPUL", "DAPUR", "OOTD", "HARGAI", "AIDILFITRI", "SOFT", "HARD", "BERJUMPA"}
DROP = {"BAWA", "OK,", "OKAY", "SO,", "OKEY,", "OKEY"}   # tak pasti / isian
def words(c):
    return [w for s in json.load(open(f"{TR}/c{c}-verb.json")) for w in s["words"]]
def norm(w):
    x = w.upper().strip()
    x = x.replace("AYDIN", "AIDIL").replace("SAMPO", "SAMPUL").replace("KHUSRALAH", "MESRA").replace("BERLAMA", "BERAMAH")
    x = x.replace("-MENU", "@@").replace("SATI", "SATE").replace("LEMAK", "LEMANG").replace("REKAN", "RENDANG")
    return x
# bilangan perkataan setiap paparan (1-3), ikut frasa semula jadi
PHRASES = dict(HOOK=[2, 3], MENU=[2, 2, 1, 1, 1, 2, 2, 2, 2, 3, 2, 3, 2, 3],
               BOOTH=[3, 2, 2, 2, 2, 2, 2], SAMPUL=[3, 3, 3, 1, 2, 2, 1, 2, 2, 2],
               SOALAN=[3, 1, 3, 3, 1, 2], JAWAB=[2, 3, 2, 3, 2, 3], UCAP=[3, 1, 2], TESTI=[2, 2, 1, 3])
def build():
    tl, T = P.timeline(); caps = []
    for b, t0, t1 in tl:
        if not b["audio"]: continue
        off = t0
        ws = []
        for c, s, e in b["audio"]:
            for w in words(c):
                if s - 0.05 <= w["start"] and w["end"] <= e + 0.1:
                    ws.append(dict(t=off + w["start"] - s, e=off + min(w["end"], e) - s, w=norm(w["word"])))
            off += e - s
        if b["name"] == "MENU":   # piece 1: caption makanan sahaja (Whisper tak pasti 'ada/tak ada')
            ws = [x for x in ws if not (x["t"] < t0 + 6.6 and re.sub(r"\W", "", x["w"]) in {"KITA", "TAK", "ADA"})]
        ws = [x for x in ws if x["w"] not in DROP and re.sub(r"[^\w]", "", x["w"]) not in {"AA", "ERM", "AH"}]
        # gabung "AIDIL"+"FITRI" & "RENDANG"+"DAGING"
        out = []
        for x in ws:
            if out and out[-1]["w"].rstrip(".,") == "AIDIL" and x["w"].startswith(("FITRI", "LICI")):
                out[-1]["w"] = "AIDILFITRI"; out[-1]["e"] = x["e"]; continue
            if x["w"].startswith("@@") and out: out[-1]["w"] = "MENU-MENU"; out[-1]["e"] = x["e"]; continue
            out.append(x)
        out = [x for x in out if re.sub(r"[^\w&?!]", "", x["w"])]
        for x in out: x["c"] = re.sub(r"[^\w&?!-]", "", x["w"])
        k = 0
        for n in PHRASES[b["name"]]:
            caps.append(out[k:k+n]); k += n
        if k != len(out): print("!!", b["name"], k, len(out), [x["c"] for x in out])
    res = []
    for i, g in enumerate(caps):
        end = g[-1]["e"] + 0.25
        if i + 1 < len(caps): end = min(end, caps[i+1][0]["t"])
        res.append(dict(t=round(g[0]["t"], 2), e=round(end, 2), words=[dict(w=x["c"], t=round(x["t"], 2)) for x in g]))
    return res
if __name__ == "__main__":
    for c in build(): print(f'{c["t"]:6.2f}-{c["e"]:6.2f}', " ".join(w["w"] for w in c["words"]))
