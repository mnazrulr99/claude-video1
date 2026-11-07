# Gaya Editing: **SAMPLE 6** — Review UGC Talking-head (edit pengguna sendiri, "Jam Wira")

> Cara guna: *"Edit video ni guna gaya Sample 6."*
>
> Ciri paling ketara: **hook = manfaat produk** ("water resistant") sambil produk di tangan, **flash + impact**
> masuk ke cerita, cerita **ikut kronologi asal**, **tiada BGM** (suara + SFX sahaja), caption **kecil** highlight **kuning**,
> **word-art warna** (PINK/PUTIH/GREEN), **title serif elegan + skrip** atas close-up produk, **anotasi tulisan tangan + anak panah**,
> **"✓ MATERIAL SILICONE"**, CTA cop **"CHECKOUT SEKARANG!"**.
>
> Istimewa: sample ini **diedit oleh pengguna sendiri daripada video mentah yang sama** dengan projek
> [`projects/jam-wira`](../../projects/jam-wira/README.md) — jadi ia boleh dibanding terus dengan edit Claude (lihat §7).

## Video rujukan

| Item | Nilai |
|---|---|
| Sumber | https://drive.google.com/file/d/1kXLmzPgq4A4ZKd60aAoJKkWsH_eW2eAN/view |
| Video mentah | https://drive.google.com/file/d/1us7ccW34K1LIIPguMhJArHhN4SRlxKKU/view (87.5 s, 720×1280) |
| Durasi | 55.8 s (≈55.0 s kandungan + hujung) |
| Format | 1080×1920 (9:16), 30 fps, HEVC, AAC 44.1 kHz (.MOV) |
| Genre | Review produk UGC (jam analog budak) — affiliate TikTok Shop, bercakap ke kamera dalam kereta |
| Watermark | Handle kreator kecil (serif, putih pudar) di bawah tengah |

Gambar rujukan: `timeline-*.jpg` (frame setiap 0.5 s), `key-frames.jpg`, `audio-spectrogram.jpg`.
**Salinan preview video:** `preview-540p.mp4`.

Kaedah analisis: transkrip Whisper + **korelasi audio dengan video mentah** (setiap 0.2 s) → EDL tepat;
padanan frame (imej kecil) untuk kesan zoom/b-roll; spektrogram + tenaga celah untuk kesan SFX/BGM.

---

## 1. Struktur & timing (EDL — masa output ← masa video mentah)

| Output | Mentah | Ucapan / apa berlaku |
|---|---|---|
| 0.0–2.0 | 34.6–36.7 | **HOOK:** "Yang ini dia water resistant tau" — tangan pegang tali jam, **punch-in** |
| 2.0–2.8 | (≈0.0–0.9 visual) | **Flash putih + impact** (lonjakan bunyi broadband) → jam dalam kotak |
| 2.8–8.0 | 0.9–7.1 | "Haa ni dia, si Wira, dia sibuk nak jam jugak. Tapi itulah, sekarang banyak jam smartwatch kan" — **punch-in kuat** pada 6.8–7.6 |
| 8.6–16.8 | 7.8–17.4 | "Saya tak nak beli dia smartwatch… pergi sekolah… jumpa satu seller… macam-macam jenis" — punch-in 9.2–11.2, 13.6, 16.0 |
| ≈17.0 | — | **Chime** (harmonik tinggi) masuk babak produk |
| 17.6–25.2 | 20.3–28.6 | "Dalam TikTok saya jumpa ye, cantik comel, dua colour… pink… putih… suka green". **Close-up jam** + title serif **"Water Resistant / *Watch*"** + tag kuning **"Tengok Beg Kuning!"** (17.5–20); **blur transition** ≈20.0–20.8; word-art **PINK** (22.0), **PUTIH** (23.0), **GREEN** (25.3) + chime setiap satu |
| 25.8–32.8 | 41.0–48.7 | "Size dia pun ngam-ngam… very good… nampak tak… dia ada tulis" — **zoom ke pergelangan** 26–31.6 |
| 32.8–38.6 | 49.4–56.8 | "Ada nombor… so senang tengok time… baru belajar" — **anotasi tulisan tangan "senang tengok waktu" + anak panah** (33.5–36) |
| 38.6–43.0 | 60.0–66.5 | "Jarum kecil, jarum panjang, silikon, cantik lah perfect" — **"✓ MATERIAL SILICONE"** (40.8–42) + chime |
| 43.4–47.8 | 69.3–76.0 | "Kalau mummy… kalau you beli dapat sekali bekas tin… nak bagi present" — **punch-in pada bekas tin** 46–48.4 |
| 48.0–49.2 | — | **SFX nada menurun** (sweep ≈900→250 Hz) dalam celah |
| 49.4–55.0 | 77.9–85.5 | CTA "So mummy kalau cari jam… tengok dalam bag… pink pun ada comel" — **"CHECKOUT SEKARANG!"** cop senget (52.5–55) + chime 53.5 |
| 55.0–55.8 | — | Tamat + SFX penutup |

**Yang dibuang dari mentah:** "So I grab warna green ni", "Tengok… See dia cantik", "Haa water resistant" (ulangan — baris asal
**dipindah jadi hook**), "So korang tengok", "Haa sekejap lagi kita nak bagi dia pakai", jeda panjang.
**Yang dikekalkan (walaupun ulang):** "Dalam TikTok saya jumpa ye", "nampak tak", "dia ada tulis", "tengok dia ada nombor".

## 2. Caption
- ALL CAPS sans bold, **kecil** (tinggi huruf ≈40 px pada 1080p), 2–3 perkataan, **putih + highlight kuning** pada perkataan aktif.
- Kedudukan **≈77–78 % dari atas (y≈1490 px)** — rendah, kurang menutup produk; berada di pinggir zon UI bawah TikTok.

## 3. Grafik / teks
| Jenis | Contoh | Gaya |
|---|---|---|
| Title produk elegan | "Water Resistant *Watch*" + tag "Tengok Beg Kuning!" | Serif krim + skrip italic, atas close-up produk (bukan atas muka) |
| Word-art warna | **PINK**, **PUTIH**, **GREEN** | Huruf bubbly besar, warna ikut warna disebut, garis "sparkle" |
| Anotasi | "senang tengok waktu" + anak panah | Tulisan tangan putih, menunjuk ke jam |
| Checklist | "✓ MATERIAL SILICONE" | Italic condensed putih, tanda ✓ hijau |
| CTA | "CHECKOUT SEKARANG!" | Teks putih tebal + jalur kuning, senget, animasi masuk |
- **Jumlah grafik sedikit (~7)** — setiap satu untuk poin utama sahaja.

## 4. Zoom / transition
- **Punch-in kuat & jarang** (±1.2–1.4×, potong terus tanpa ramp), kadang-kadang dahi terpotong.
- **Flash putih + impact** (hook → cerita), **blur zoom** selepas close-up produk. Selebihnya hard cut.
- **Tiada b-roll luar** — semua visual sync dengan suara; close-up produk datang dari momen yang sama.

## 5. Audio
- **Tiada BGM** (spektrogram: tiada jalur nada berterusan).
- ≈8 SFX jelas: impact/flash, chime, nada menurun, ding penutup — **agak kuat** (puncak celah ≈ −12 hingga −16 dB RMS, lebih kuat dari suara).
- Loudness: **−19.5 LUFS**, LRA 9 LU, **peak +0.5 dBFS** (ada risiko clipping).

## 6. Ringkasan "selera" pengguna dari sample ini
1. Hook boleh jadi **manfaat produk + produk dalam tangan**, bukan semestinya soalan.
2. **Pindah baris** yang diulang ke depan (jadi hook) dan bukannya padam terus.
3. Grafik **sedikit tapi bergaya**: serif elegan, word-art warna, tulisan tangan.
4. **CTA awal kecil** ("Tengok Beg Kuning!") pada 17 s + CTA akhir besar.
5. Caption kecil, highlight kuning, rendah.
6. Tiada BGM — suara + SFX sahaja (trending sound mungkin ditambah di TikTok).

## 7. Perbandingan dengan edit Claude (projek jam-wira V1)
| Aspek | Pengguna (S6) | Claude V1 |
|---|---|---|
| Durasi | 55.8 s | 58.4 s |
| Hook | Manfaat ("water resistant") + produk di tangan | Kontra ("tak nak smartwatch") + stamp ❌ |
| Produk kelihatan jelas | 0 s (tali jam), close-up 17.5 s | 0 s (kotak), close-up tiada |
| Susunan | Hook dipindah, selebihnya kronologi | Hook dipindah, selebihnya kronologi |
| Ulangan | Sebahagian dikekalkan | Hampir semua dibuang |
| Zoom | Punch-in kuat, jarang | Selang-seli 1.0/1.1 setiap potongan + 2 punch-in |
| Transition | Flash+impact, blur | Crash zoom awal, hard cut |
| Grafik | ~7, elegan/organik | ~16, kotak "sticker" seragam |
| Caption | Kecil, kuning, y≈1490 | Besar, hijau mint, y≈1340 |
| BGM | Tiada | Carefree, −18 dB bawah suara |
| SFX | ~8, kuat | ~28, sederhana |
| Loudness | −19.5 LUFS, peak +0.5 dBFS | −14.9 LUFS, peak −1.3 dBFS |
