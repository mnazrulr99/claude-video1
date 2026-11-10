# Pelan job raya (multi-klip). Masa sumber per klip cN.mp4. Output 1080x1920.
# BEATS: audio = senarai (klip, a, b) suara (None = B-roll, BGM sahaja, durasi 'dur').
#        shots = senarai (klip, mula_src, zoom, durasi) ; durasi None = baki beat. kx,ky = pusat crop (0..1)
BEATS = [
 dict(name="HOOK", audio=[(8, 51.25, 52.95)], shots=[(8, 51.25, 1.35, None, 0.42, 0.40)], why="Punchline lawak terus (Hook A)"),
 dict(name="TIBA", audio=None, dur=6.4, shots=[(3, 0.2, 1.2, 2.1, 0.5, 0.45), (3, 4.3, 1.25, 2.1, 0.4, 0.45), (3, 6.4, 1.2, None, 0.5, 0.45)],
      why="Pembuka acara: tetamu tiba + title"),
 dict(name="MENU", audio=[(1, 0.15, 6.66), (1, 11.10, 13.40), (1, 15.95, 23.66)],
      shots=[(1, 0.15, 1.35, 1.4, 0.45, 0.40), (4, 13.4, 1.2, 1.3, 0.5, 0.5), (4, 0.0, 1.2, 1.2, 0.5, 0.5), (4, 7.4, 1.2, 1.3, 0.5, 0.5),
             (4, 15.0, 1.2, 1.31, 0.5, 0.5), (1, 11.10, 1.5, 2.3, 0.42, 0.38), (10, 0.0, 1.25, 2.3, 0.5, 0.5), (4, 3.3, 1.2, 1.95, 0.5, 0.5),
             (2, 0.3, 1.2, None, 0.5, 0.4)],
      why="Suara pengacara, visual tukar ikut makanan disebut"),
 dict(name="BOOTH", audio=[(9, 2.00, 5.50), (9, 5.95, 8.20)], shots=[(9, 2.0, 1.2, 3.5, 0.5, 0.45), (9, 5.95, 1.4, None, 0.55, 0.40)],
      why="Photobooth + scan QR (aktiviti)"),
 dict(name="SAMPUL", audio=[(5, 13.70, 16.24), (8, 0.0, 2.82), (8, 9.16, 10.25), (8, 11.10, 12.30), (8, 22.68, 23.75)],
      shots=[(5, 13.7, 1.4, 2.54, 0.40, 0.40), (8, 0.0, 1.3, 2.82, 0.62, 0.40), (8, 9.16, 1.45, 1.09, 0.62, 0.42), (8, 11.10, 1.25, 1.2, 0.62, 0.42), (8, 22.68, 1.5, None, 0.62, 0.42)],
      why="Bina suspen game sampul raya (transition kilauan emas masuk)"),
 dict(name="SOALAN", audio=[(8, 38.59, 45.51)], shots=[(8, 38.59, 1.3, 3.41, 0.38, 0.40), (8, 42.0, 1.55, None, 0.33, 0.40)],
      why="Soalan game dibaca - klimaks"),
 dict(name="JAWAB", audio=[(8, 51.29, 56.13)], shots=[(8, 51.29, 1.35, 2.4, 0.42, 0.40), (8, 53.69, 1.6, None, 0.36, 0.40)],
      why="Punchline penuh (bayar hook)"),
 dict(name="UCAP", audio=[(7, 24.80, 26.52), (7, 30.60, 31.80)], shots=[(7, 24.8, 1.35, 1.72, 0.65, 0.35), (7, 30.6, 1.5, None, 0.62, 0.35)],
      why="Ucapan raya tetamu"),
 dict(name="TESTI", audio=[(10, 33.32, 36.16)], shots=[(10, 33.32, 1.35, None, 0.5, 0.45)], why="Testimoni: jemputan dihargai"),
 dict(name="TUTUP", audio=None, dur=4.2, shots=[(1, 24.4, 1.2, 2.0, 0.45, 0.40), (6, 3.0, 1.2, None, 0.5, 0.40)],
      why="Montaj penutup + ucapan Selamat Hari Raya"),
]
END_BLACK = 0.6
FIXES = {"aydin": "AIDIL", "fitri.": "FITRI", "lici": "FITRI", "sampo": "SAMPUL", "khusralah,": "MESRA", "berlama": "BERAMAH"}
SKIPWORDS = {"kita", "tak", "ada", "aa,", "okey?", "rekan"}   # dalam MENU: caption makanan sahaja (Whisper tak pasti 'ada/tak ada')
FOODFIX = {"rekan daging": "RENDANG DAGING", "lemak": "LEMANG", "sati": "SATE", "lontong": "LONTONG"}
TITLE = ("RUMAH TERBUKA", "Aidilfitri")
END_TEXT = ("Selamat Hari Raya", "MAAF ZAHIR & BATIN")
GOLD = "#F5C542"

def beat_dur(b):
    return b["dur"] if b["audio"] is None else sum(e - s for _, s, e in b["audio"])

def timeline():
    t, out = 0.0, []
    for b in BEATS:
        d = beat_dur(b); out.append((b, t, t + d)); t += d
    return out, t + END_BLACK

# Zon selamat (dari zones.py: muka di y~960-1440 kebanyakan shot; atas = siling kosong)
CAP_Y = 400          # pusat caption (px dari atas, 1080x1920) - bawah zon UI TikTok, atas muka
# Grafik: (out_mula, out_tamat, jenis, teks, y_pusat)
GFX = [
    (1.80, 8.00, "title", "RUMAH TERBUKA|Aidilfitri", 1560),
    (24.70, 27.60, "pill", "📸 PHOTOBOOTH", 600),
    (30.40, 30.90, "sparkle", "", 960),            # transition kilauan emas (R21)
    (32.20, 35.00, "pill", "🧧 SAMPUL RAYA", 600),
    (39.10, 42.40, "pill", "❓ SOALAN RAYA", 600),
    (56.70, 60.80, "end", "Selamat Hari Raya|MAAF ZAHIR & BATIN", 1560),
]
