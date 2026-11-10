# Muzik raya ASAL (ciptaan Claude, tiada hak cipta pihak ketiga): kompang + gendang + akordion + bass + seruling.
# 120 BPM, 4/4, 1 bar = 2.0 s. Guna: python3 -I music.py <out.wav>
import sys, numpy as np, wave
SR = 44100; BPM = 120; BEAT = 60 / BPM; BAR = 4 * BEAT
NBARS = 18; TOTAL = 36.0
rng = np.random.default_rng(1447)
L = np.zeros(int(TOTAL * SR)); R = np.zeros_like(L)
def add(sig, t, pan=0.0, gain=1.0):
    i = int(max(0, t) * SR); n = min(len(sig), len(L) - i)
    if n <= 0: return
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    L[i:i+n] += sig[:n] * gain * l * 1.414; R[i:i+n] += sig[:n] * gain * r * 1.414
def tt(d): return np.arange(int(d * SR)) / SR
def lp(x, fc):  # penapis lowpass satu kutub (dua kali)
    a = np.exp(-2 * np.pi * fc / SR); y = np.empty_like(x); s = 0.0
    for _ in range(2):
        s = 0.0
        for i in range(len(x)): s = (1 - a) * x[i] + a * s; y[i] = s
        x = y.copy()
    return y
def hp(x, fc): return x - lp(x, fc)
mtof = lambda m: 440 * 2 ** ((m - 69) / 12)
hum = lambda: rng.normal(0, 0.004)
# ---------- perkusi ----------
NOISE = rng.standard_normal(SR)
BUNG = None; PAK = None; DUM = None; TAK = None; SHK = None
def mk_perc():
    global BUNG, PAK, DUM, TAK, SHK
    t = tt(0.35)
    f = 200 * (1 + 0.6 * np.exp(-t * 40)); ph = 2 * np.pi * np.cumsum(f) / SR
    BUNG = (np.sin(ph) * np.exp(-t * 14) + 0.25 * hp(NOISE[:len(t)], 800) * np.exp(-t * 60)) * 0.8
    t = tt(0.12)
    PAK = (hp(NOISE[:len(t)], 1500) * np.exp(-t * 55) + 0.5 * np.sin(2 * np.pi * 520 * t) * np.exp(-t * 70)) * 0.55
    t = tt(0.6)
    f = 85 * (1 + 0.8 * np.exp(-t * 30)); ph = 2 * np.pi * np.cumsum(f) / SR
    DUM = np.sin(ph) * np.exp(-t * 7) * 0.9
    t = tt(0.15)
    TAK = (hp(NOISE[2000:2000+len(t)], 1000) * np.exp(-t * 45) + 0.6 * np.sin(2 * np.pi * 330 * t) * np.exp(-t * 50)) * 0.5
    t = tt(0.06)
    SHK = hp(NOISE[5000:5000+len(t)], 5000) * np.exp(-t * 70) * 0.25
mk_perc()
def drums(bar, fill=False, shaker=False, final=False):
    t0 = bar * BAR
    if final:
        add(DUM, t0, 0, 1.2); add(BUNG, t0, -0.3, 1.1); add(BUNG, t0 + 0.01, 0.3, 1.1); return
    bung = [0, 3, 4, 6]; pak = [1, 2, 5, 7]
    for s in bung: add(BUNG, t0 + s * BEAT / 2 + hum(), -0.35, (1.0 if s in (0, 4) else 0.75) * rng.uniform(0.85, 1.0))
    for s in pak: add(PAK, t0 + s * BEAT / 2 + hum(), 0.35, rng.uniform(0.7, 0.95))
    add(DUM, t0 + hum(), 0, 1.0); add(DUM, t0 + 2 * BEAT + hum(), 0, 0.85)
    add(TAK, t0 + 3 * BEAT + hum(), 0.1, 0.8)
    if fill:
        for k in range(4): add(PAK, t0 + 3 * BEAT + k * BEAT / 4, 0.35 - k * 0.2, 0.6 + 0.1 * k)
    if shaker:
        for k in range(16): add(SHK, t0 + k * BEAT / 4 + hum(), 0.5, 0.9 if k % 2 else 0.5)
# ---------- akordion ----------
def accord_note(m, d):
    t = tt(d); f = mtof(m); out = np.zeros_like(t)
    for det in (-6, 0, 7):  # tiga 'reed' sedikit sumbang = bunyi akordion
        ff = f * 2 ** (det / 1200); ph = 2 * np.pi * ff * t
        out += 2 * (ph / (2 * np.pi) % 1) - 1  # sawtooth
    out = lp(out / 3, 2600) * (1 + 0.08 * np.sin(2 * np.pi * 5.5 * t))
    env = np.minimum(1, t / 0.015) * np.minimum(1, (d - t) / 0.05).clip(0, 1)
    return out * env
CH = dict(G=[55, 59, 62, 67], C=[55, 60, 64, 67], D=[57, 62, 66, 69], D7=[57, 60, 62, 66], Em=[55, 59, 64, 67])
ROOT = dict(G=(43, 50), C=(48, 43), D=(50, 45), D7=(50, 45), Em=(40, 47))
CHORDS = ["G", "G", "G", "C", "D", "G", "G", "C", "D7", "G", "Em", "C", "D", "D7", "C", "G", "D7", "G"]
cache = {}
def chord_stab(name, d):
    k = (name, d)
    if k not in cache: cache[k] = sum(accord_note(m, d) for m in CH[name]) / 4
    return cache[k]
def bass_note(m, d=0.45):
    t = tt(d); f = mtof(m)
    s = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)
    return s * np.exp(-t * 5) * np.minimum(1, t / 0.005)
# ---------- seruling ----------
def flute(m, d, nxt=None):
    t = tt(d + 0.08); f = mtof(m)
    vib = 1 + 0.006 * np.sin(2 * np.pi * 5.6 * t) * np.minimum(1, t / 0.35)
    fr = f * vib
    if nxt is not None:  # luncur kecil ke nota seterusnya
        g = np.clip((t - (d - 0.05)) / 0.06, 0, 1); fr = fr * (mtof(nxt) / f) ** g
    ph = 2 * np.pi * np.cumsum(fr) / SR
    s = np.sin(ph) + 0.18 * np.sin(2 * ph) + 0.06 * np.sin(3 * ph)
    breath = lp(NOISE[:len(t)] if len(t) <= SR else np.resize(NOISE, len(t)), 3000) * 0.12
    env = np.minimum(1, t / 0.04) * np.clip((d + 0.08 - t) / 0.1, 0, 1)
    return (s + breath) * env * 0.5
MEL = {  # bar: [(midi atau None, rentak)]
 2: [(None, 2), (74, .5), (76, .5), (74, .5), (71, .5)],
 3: [(67, 1), (71, .5), (74, .5), (76, 1), (74, 1)],
 4: [(72, 1), (76, .5), (74, .5), (72, 1), (71, .5), (69, .5)],
 5: [(69, 1), (74, 1), (78, .5), (76, .5), (74, 1)],
 6: [(71, 1.5), (69, .5), (67, 2)],
 7: [(74, 1), (76, .5), (79, .5), (76, 1), (74, 1)],
 8: [(76, 1), (72, .5), (76, .5), (74, 1), (72, 1)],
 9: [(71, .5), (72, .5), (74, 1), (69, 1), (72, 1)],
 10: [(71, 1), (69, .5), (71, .5), (67, 2)],
 11: [(76, 1.5), (79, .5), (76, 1), (74, 1)],
 12: [(72, 1), (76, 1), (79, 1), (76, 1)],
 13: [(74, 1), (78, .5), (76, .5), (74, 1), (69, 1)],
 14: [(72, 1), (71, .5), (69, .5), (69, 1), (74, 1)],
 15: [(76, 1), (74, .5), (72, .5), (76, 1), (79, 1)],
 16: [(74, 1.5), (71, .5), (67, 1), (71, 1)],
 17: [(69, 1), (72, 1), (71, .5), (69, .5), (66, .5), (69, .5)],
 18: [(67, 4)],
}
notes = []
for bar in sorted(MEL):
    t = (bar - 1) * BAR
    for m, b in MEL[bar]:
        if m is not None: notes.append((t, m, b * BEAT))
        t += b * BEAT
for i, (t, m, d) in enumerate(notes):
    nxt = notes[i + 1][1] if i + 1 < len(notes) and abs(notes[i + 1][0] - (t + d)) < 1e-6 and d <= 0.5 else None
    dd = d if d < 1.9 else 3.0
    add(flute(m, dd, nxt), t + hum(), 0.25, 0.55)
    if m >= 76 and d <= 0.5 and rng.random() < 0.0: pass
# ---------- susun ----------
for bar in range(1, NBARS + 1):
    t0 = (bar - 1) * BAR; ch = CHORDS[bar - 1]
    if bar == NBARS:  # pukulan penutup
        drums(bar - 1, final=True)
        add(chord_stab(ch, 2.6) * np.exp(-tt(2.6) * 1.3), t0, -0.25, 0.9)
        add(bass_note(ROOT[ch][0], 2.0) , t0, 0, 1.0)
        continue
    drums(bar - 1, fill=bar in (2, 10, 14, 17), shaker=bar >= 11)
    if bar >= 2:
        r1, r2 = ROOT[ch]
        add(bass_note(r1), t0 + hum(), 0, 0.9); add(bass_note(r2), t0 + 2 * BEAT + hum(), 0, 0.8)
        for k in (0.5, 1.5, 2.5, 3.5):  # chord offbeat gaya joget
            add(chord_stab(ch, 0.28), t0 + k * BEAT + hum(), -0.25, 0.42)
    else:  # intro: akordion panjang perlahan
        add(chord_stab(ch, 1.9) * 0.6, t0, -0.25, 0.5)
# ---------- reverb ringkas + master ----------
ir_t = tt(0.9); ir = rng.standard_normal(len(ir_t)) * np.exp(-ir_t * 6); ir /= np.sqrt((ir ** 2).sum())
def rev(x): return np.fft.irfft(np.fft.rfft(x, len(x) + len(ir)) * np.fft.rfft(ir, len(x) + len(ir)))[:len(x)]
L2 = L + 0.18 * rev(L); R2 = R + 0.18 * rev(R)
fade = np.ones_like(L2); n = int(0.4 * SR); fade[-n:] = np.linspace(1, 0, n)
st = np.stack([L2, R2], 1) * fade[:, None]
st = np.tanh(st / np.abs(st).max() * 1.4) * 0.89
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())
print("ok", TOTAL, "s")
