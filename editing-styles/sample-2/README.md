# Gaya Editing: **SAMPLE 2** — UGC Iklan Produk (soft-sell)

> Cara guna: *"Edit video ni guna gaya Sample 2."*
>
> Ciri paling ketara: video **review/iklan produk gaya UGC** (selfie, bercakap terus ke kamera sambil pegang produk),
> **caption dengan kotak highlight hijau-kuning** pada perkataan aktif, **pattern interrupt "colour bars TV"** selepas hook,
> dan **banyak grafik label produk** (title elegan, pill label, UI search box, kursor klik, teks marquee, badge).

## Pilihan pengguna (sama seperti semua gaya)

- Claude edit & render terus (ffmpeg). **Storyboard imej dulu → pengguna setuju → baru render.**
- BGM royalty-free (pengguna pilih). Hook wajib ada, gaya ikut jenis video.

## Video rujukan

| Item | Nilai |
|---|---|
| Sumber | https://drive.google.com/file/d/1yjsuVtg7NDZDRxkSmmpv_jfN_RKgK74Q/view |
| Durasi | 53.3 s (52.0 s kandungan + ~1.3 s hitam dengan audio fade-out) |
| Format | 1080×1920 (9:16), **60 fps**, HEVC, AAC |
| Genre | UGC product review / affiliate (TikTok Shop) — produk *Lemon Ginger Detox* |
| Kamera | Selfie kamera depan, handheld, satu lokasi (bilik/wardrobe), Bahasa Melayu santai |

Gambar rujukan: `timeline-*.jpg` (frame setiap 0.5 s), `key-frames.jpg` (10 frame grafik utama),
`frame-color-bars.jpg`, `audio-spectrogram.jpg`.

**Salinan preview video:** `preview-540p.mp4` (540p, H.264, dengan audio) — untuk semakan semula timing, animasi & bunyi selepas video asal dipadam dari Google Drive.

---

## 1. Struktur & Timing (formula iklan: Masalah → Produk → Manfaat → Cara guna → CTA)

| Masa | Bahagian | Apa berlaku |
|---|---|---|
| 0.0–1.4 s | **HOOK** | Terus pegang produk, bercakap ke kamera (tiada intro) |
| 1.5–2.3 s | **Pattern interrupt** | Skrin **colour bars TV (SMPTE)** + bunyi **beep 1 kHz** kuat (−7 dB) — macam "siaran terganggu"/sensor |
| 2.4–8.0 s | **Masalah (pain points)** | *"Untuk mak-mak yang jenis rasa cepat lesu, berangin badan, lenguh, cepat penat…"* — setiap masalah keluar sebagai title tengah + ❌ |
| 8.0–12.0 s | **Perkenal produk** | Label **"Ginger Lemon Detox"** (pill dengan ikon hati) di atas |
| 12.0–22.4 s | Cerita / empati | *"Badan pun rasa penuh angin… pagi rasa lemau…"* — punch-in close-up tangan/muka |
| 22.5–23.4 s | Peralihan | Zoom extreme close-up muka + **light leak/sparkle** di sudut |
| 23.5–26.2 s | **Product reveal** | Title skrip elegan **"Lemon Ginger Detox · mimpi"** + pill **"Traditional Herbal Drink"** + **gambar produk (cutout)** di bawah kanan. *"Ini lah ada solution"* |
| 26.5–29.5 s | Manfaat 1 | **Kotak teks gaya UI editor** menaip "Blo…" → **"Bloated ✅"** |
| 29.5–37.0 s | Rasa & bahan | *"Tak pahit, masam manis, pedas sebab ada ginger"* |
| 37.5–38.5 s | Manfaat 2 | Label **"Natural Ingredients"** + **animasi kursor tangan klik** |
| 38.5–44.5 s | Cara guna | Punch-in besar pada botol (43.5 s) |
| 45.0–47.5 s | **Dos** | Teks besar **"30ml Setiap Pagi"** bergerak **marquee** melintang skrin |
| 48.0–49.0 s | Manfaat 3 | Badge emas **"MUDAH LAWAS"** + garis sparkle |
| 49.0–51.9 s | **CTA** | *"Siapa yang nak, tekan beg kuning sekarang"* (TikTok Shop) |
| 52.0–53.3 s | Ending | Cut ke hitam, **audio fade-out ~1 s** |

**Rentak:**
- Jump cut sangat kerap (kira-kira setiap 1–3 s), buang semua jeda.
- Punch-in/zoom ekstrem pada momen penting: 12.5 s (tangan), 22.5 s (muka), 32 s (jari), 43.5 s (botol).
- Satu grafik/label baharu kira-kira setiap **3–6 s** supaya mata sentiasa ada benda baru.

## 2. Caption (subtitle utama)

- **Word-by-word**, 2–4 perkataan sebaris, maksimum 2 baris, **HURUF BESAR**.
- **Font:** sans-serif bold, putih dengan shadow/outline hitam nipis, **saiz kecil**.
- **Highlight:** perkataan aktif diberi **kotak latar hijau-kuning (lime, ~#D4F53C)** dengan teks hitam — bukan tukar warna teks (beza dengan Sample 1).
- **Kedudukan:** tengah, kira-kira **75–78% dari atas** (lebih rendah dari Sample 1), di bawah produk.
- Tukar halaman serta-merta (cut).

## 3. Grafik & Title (pelbagai jenis — ini "identiti" Sample 2)

| Jenis | Contoh | Gaya | Animasi |
|---|---|---|---|
| Pain point | "Cepat Lesu ❌", "Berangin Badan ❌", "Cepat Penat ❌" | Serif bold, **putih/pink-lilac**, tengah skrin (~40%) + ❌ merah | Typewriter |
| Nama produk | "Ginger Lemon Detox" | Serif pink dalam **pill krim** dengan ikon hati ♥ di kiri-kanan | Typewriter |
| Product reveal | "Lemon Ginger Detox · mimpi" | **Skrip/serif elegan** putih besar di atas | Fade/typewriter |
| Tag kategori | "Traditional Herbal Drink" | Pill krim kecil bawah kiri | Pop |
| Packshot | Gambar botol (cutout PNG) | Bawah kanan | Pop/slide masuk |
| Manfaat ✅ | "Bloated ✅" | **Kotak teks gaya UI editor** (border biru + titik handle) | Taip huruf demi huruf |
| Manfaat klik | "Natural Ingredients" | Pill kuning kecil + **ikon kursor tangan** | Kursor gerak & klik |
| Dos | "30ml Setiap Pagi" | Font rounded bold putih, besar, sedikit condong | **Marquee** kanan → kiri |
| Badge | "MUDAH LAWAS" | Kotak **emas** teks putih + garis sparkle | Wipe/sparkle |

## 4. Effect & Grading

- **Colour bars TV + beep** sebagai pattern interrupt selepas hook (0.8 s).
- **Light leak / sparkle** sebagai peralihan sebelum product reveal.
- **Punch-in ekstrem** (close-up sangat dekat) — hampir macam "camera shake" zoom.
- Grade natural, warm, kulit cerah; warna **kuning/oren produk** jadi fokus. Imej selfie *mirror* (tak dibalikkan).
- 60 fps — gerakan grafik lebih licin.

## 5. Sound Design

| Masa | Bunyi | Fungsi |
|---|---|---|
| 1.5–2.3 s | **Beep 1 kHz** (paling kuat, −7 dB) | Colour bars / "sensor" pattern interrupt |
| ~8.9 s | Ding/chime | Label nama produk |
| ~23.5–24.5 s | Chime/sparkle (nada tinggi 6–12 kHz) | Product reveal |
| ~28.5 s | Typing/click | "Bloated ✅" |
| ~37.5 s | Click | Kursor klik "Natural Ingredients" |
| ~45 s | Swoosh riser | Teks marquee "30ml Setiap Pagi" |
| ~48.3 s | Ding | Badge "MUDAH LAWAS" |

- **BGM: ada, perlahan berterusan** — aras bunyi semasa jeda tak pernah jatuh ke senyap (≥ −35 dB) dan audio **fade-out ~1 s selepas visual cut ke hitam** (ekor muzik).
- Suara dominan (−10 hingga −25 dB RMS), BGM jauh di bawah.

## 6. Transition

- Kebanyakan **hard jump cut** + punch-in.
- Transition khas hanya 2: **colour bars glitch** (selepas hook) dan **light leak/sparkle** (sebelum product reveal).
- Ending: cut ke hitam + audio fade-out.

---

## Checklist cepat — "Edit gaya Sample 2"

1. 9:16, 1080×1920, 60 fps (atau 30 fps jika sumber 30). Sasaran 40–60 s.
2. Susun ikut formula: **Hook → Pattern interrupt → Masalah ❌ → Produk → Manfaat ✅ → Cara guna/dos → CTA**.
3. Hook 0–1.5 s pegang produk; ikut dengan pattern interrupt (colour bars + beep, atau alternatif yang sesuai).
4. Jump cut ketat; punch-in ekstrem 3–4 kali pada momen penting.
5. Caption ALL CAPS putih kecil, perkataan aktif dalam **kotak lime**, posisi ~76% dari atas.
6. Setiap pain point → title serif tengah + ❌ (typewriter).
7. Product reveal → title elegan + pill kategori + packshot cutout + sparkle SFX.
8. Manfaat → variasi grafik (UI text box ✅, kursor klik, badge emas) supaya tak berulang.
9. Dos/info penting → teks marquee besar.
10. CTA jelas di hujung (cth. "tekan beg kuning"), cut ke hitam, BGM fade-out ~1 s.
11. SFX pada setiap grafik baru; BGM perlahan berterusan.

**Bahan yang perlu dari pengguna untuk gaya ini:** nama produk/brand, gambar produk (PNG tanpa latar jika ada),
senarai manfaat & dos, jenis CTA (TikTok Shop / link bio / WhatsApp).
