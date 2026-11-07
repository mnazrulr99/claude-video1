# CONTOH pelan (job periuk). Masa = masa SUMBER (raw.mp4). Ikut LEARNINGS.md: zoom asas 1.2 (R6), hook B (R5), hitam 0.6 (R12).
HOOK = (10.30, 11.30)            # klip angkat penutup kaca, audio dimatikan, whoosh
SEGMENTS = [  # (mula, tamat, zoom)
    (0.00, 6.22, 1.00),
    (6.45, 8.25, 1.15),
    (8.62, 13.50, 1.00),
    (13.50, 22.05, 1.12),
    (22.80, 30.95, 1.00),
    (30.95, 34.62, 1.15),
    (34.90, 41.75, 1.00),
    (41.98, 48.20, 1.12),
    (48.20, 52.25, 1.00),
]
END_BLACK = 0.6
FIXES = {"selera": "seller", "enak": "Yana", "-mak": "mak", "-kawan": "kawan", "-satu": "satu"}

# Grafik: (src_mula, src_tamat, jenis, teks)
GRAPHICS = [
    (0.00, 3.84, "title", "Periuk Stainless Steel|MURAH!"),
    (4.08, 8.25, "sizes", "16|18|20|22|24"),
    (11.14, 13.50, "check", "Penutup kaca solid"),
    (17.36, 22.05, "badge", "HARGA TURUN!"),
    (24.60, 27.30, "check", "Beli set 5 lagi JIMAT"),
    (32.00, 34.62, "check", "Stainless steel|Warna menarik"),
    (40.34, 41.75, "check", "Ada penutup = hygiene"),
    (42.38, 48.20, "gift", "Sesuai jadi hadiah"),
    (48.26, 52.25, "cta", "Tekan beg kuning"),
]
SIZE_TIMES = [4.08, 4.62, 5.38, 5.76, 6.48]

def src_to_out(t):
    """Masa sumber -> masa output (selepas hook + potongan). None jika dipotong."""
    out = HOOK[1] - HOOK[0]
    for a, b, _ in SEGMENTS:
        if a <= t <= b:
            return round(out + (t - a), 3)
        out += b - a
    return None

def total():
    return (HOOK[1]-HOOK[0]) + sum(b-a for a,b,_ in SEGMENTS) + END_BLACK

# Zon selamat untuk SEMUA tulisan (tidak tutup muka & produk) — dari tools/zones.py
SAFE = dict(x=36, w=440, gfx_top=120, cap_top=520)
