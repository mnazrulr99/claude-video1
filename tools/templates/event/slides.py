# v4: muzik raya asal 120 BPM, tukar slide tepat pada bar (crossfade berpusat pada garis bar). v3: tiada SFX transition, 2.2 s/slide. v2: SLIDESHOW senyap (maklum balas pengguna): 3-5 s/shot, crossfade 0.5 s, Ken Burns, SFX lembut, title + kad akhir sahaja.
# SHOTS: (klip, mula_src, durasi, kx, ky, arah_zoom) ; susunan ikut aturcara majlis
SHOTS = [
 (3, 0.0, 4.2, 0.50, 0.45, "in"),    # gerbang, tetamu tiba (title)
 (3, 4.2, 2.4, 0.42, 0.45, "out"),   # ibu & anak
 (2, 0.3, 2.4, 0.50, 0.42, "in"),    # tetamu bersalaman
 (4, 0.0, 2.4, 0.50, 0.50, "in"),    # kuih-muih
 (4, 4.0, 2.4, 0.50, 0.50, "out"),   # puding & kek coklat
 (4, 8.0, 2.4, 0.50, 0.50, "in"),    # menara puding
 (4, 14.0, 2.4, 0.50, 0.50, "in"),   # roti jala & kari
 (1, 10.0, 2.4, 0.45, 0.40, "in"),   # pengacara
 (10, 1.0, 2.4, 0.50, 0.50, "out"),  # tetamu menjamu selera
 (9, 2.0, 2.4, 0.50, 0.45, "in"),    # photobooth
 (5, 13.7, 2.4, 0.42, 0.40, "out"),  # pengacara + sampul raya
 (8, 38.6, 2.4, 0.38, 0.40, "in"),   # tetamu baca soalan
 (8, 51.3, 2.4, 0.42, 0.40, "out"),  # tetamu ketawa
 (7, 24.6, 2.4, 0.62, 0.36, "in"),   # ucapan raya
 (1, 30.4, 5.7, 0.36, 0.40, "in"),   # pengacara berdua (kad penutup)
]
XF = 0.4          # crossfade
END_BLACK = 0.5
BASEZ = 1.2       # zoom asas (R6); Ken Burns +8%
def starts():
    t, out = 0.0, []
    for s in SHOTS: out.append(t); t += s[2] - XF
    return out, t + XF   # tamat shot terakhir
