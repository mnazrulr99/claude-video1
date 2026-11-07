# Gaya Editing: **SAMPLE 1**

> Cara guna: *"Edit video ni guna gaya Sample 1."*
>
> Ciri paling ketara: caption karaoke dengan **highlight kuning** pada perkataan aktif, dan
> **punch-in zoom** (jump cut + tukar saiz frame) setiap kali ayat bertukar.

## Pilihan pengguna (WAJIB ikut)

1. **Claude edit & render terus** (ffmpeg dalam session). Pengguna tak buka sebarang app/software editing.
   Pengguna hanya hantar video mentah (link/fail) → Claude hantar balik video siap.
2. **BGM: pilihan.** Video rujukan tiada BGM, tapi pengguna kadang-kadang nak BGM yang sesuai dengan
   mood video. Bila guna BGM: perlahan di bawah suara (duck ~−20 dB bawah dialog), ikut mood topik.
3. **Hook: sentiasa ada, tapi gayanya ikut jenis video.** Hitam-putih + colour pop hanya satu pilihan
   (sesuai untuk nada serius/refleksi). Pilih treatment hook yang kena dengan kandungan
   (contoh: freeze-frame, zoom laju, teks soalan besar, SFX sting, dll.).
   Kalau tak pasti, tanya pengguna dulu.

## Video rujukan

| Item | Nilai |
|---|---|
| Sumber | https://drive.google.com/file/d/1uchyhCrJ13eETx5menUYGZdT188XLCuW/view |
| Durasi | 23.2 s (22.4 s kandungan + 0.7 s skrin hitam) |
| Format | 1080×1920 (9:16 vertical), 30 fps, HEVC, AAC 44.1 kHz stereo |
| Editor | CapCut / Dreamina (metadata `DreaminaMetaInfo`) |
| Genre | Talking-head, satu orang, satu lokasi (setup trading), Bahasa Melayu santai |
| Topik | "7 tahun dalam dunia trading — apa yang aku stop buat" |

Gambar rujukan dalam folder ini:
`timeline-0-12s.jpg`, `timeline-12-23s.jpg` (frame setiap 0.25 s), `frame-bw-hook.jpg`,
`frame-title-callout.jpg`, `frame-money-rain.jpg`, `audio-spectrogram.jpg`.

**Salinan preview video:** `preview-540p.mp4` (540p, H.264, dengan audio) — untuk semakan semula timing, animasi & bunyi selepas video asal dipadam dari Google Drive.

---

## 1. Struktur & Timing (beat sheet)

| Masa | Bahagian | Apa berlaku di skrin |
|---|---|---|
| 0.0–0.2 s | **Flash in** | Frame pertama terlebih terang (luma ~770 vs normal ~480) → kesan flash putih masuk |
| 0.2–2.4 s | **HOOK (hitam-putih)** | Video desaturate penuh (B&W). Soalan hook: *"Korang rasa berapa tahun dah aku dalam dunia trading?"* |
| 2.4 s | **Colour pop** | Warna kembali serentak pada perkataan **"TRADING"** |
| 3.2–3.8 s | **Punch-in kuat** | Close-up besar ketika tunjuk 7 jari *"Aku dah 7 tahun"* + SFX impact |
| 4.0–6.6 s | Setup | Frame normal: *"Dan makin lama aku trade, makin banyak benda yang aku stop buat"* |
| 6.8–9.6 s | Poin 1 & 2 | Title atas: **OVERTRADE ❌**, **REVENGE TRADE DURING LOST ❌** |
| 10.2–12.0 s | Poin 3 | Title atas: **PAKSA ENTRY ❌** |
| 12.2–17.0 s | Poin 4 (paling penting) | *"Dan paling penting…"* → title **STOP IKUT ENTRY ORANG ‼️** + SFX paling kuat |
| 17.0–19.2 s | Twist | *"Aku ingat makin banyak entry, makin banyak peluang nak profit…"* |
| 19.2–20.0 s | **Money rain** | Overlay duit USD $100 jatuh pada perkataan **"PROFIT"** |
| 20.0–22.4 s | Payoff | Punch-in → *"Rupa-rupanya sebaliknya"* (gesture angkat bahu) |
| 22.4–23.2 s | **Ending** | Hard cut ke skrin hitam + senyap (~0.7 s) — tiada CTA/outro |

**Rentak:**
- Jump cut buang semua jeda; jeda senyap paling panjang ≈ 0.2–0.3 s.
- Tukar framing (zoom/crop) setiap **~2–4 s**, selalu di sempadan ayat/poin baru.
- Senarai poin bergerak laju: satu poin ≈ **1.5–3 s**.
- Struktur: **Hook soalan → kredibiliti (7 tahun) → senarai "stop" → twist → punchline → cut hitam.**

## 2. Caption (subtitle utama)

- **Gaya:** word-by-word / karaoke. **2–3 perkataan sebaris**, maksimum 2 baris.
- **Font:** sans-serif tebal (ExtraBold/Black), **HURUF BESAR SEMUA**, saiz kecil-sederhana (~4–5% tinggi frame).
- **Warna:** putih, dengan outline/shadow hitam nipis.
- **Highlight:** perkataan yang sedang disebut bertukar **kuning (#FFE600 lebih kurang)**. Highlight bergerak ikut audio.
- **Kedudukan:** tengah-bawah, kira-kira **60–65% dari atas** (atas paras lutut/tangan, bukan di paling bawah — elak UI TikTok/Reels).
- **Animasi:** tiada bounce besar; tukar halaman serta-merta (cut), highlight sahaja yang animate.
- Caption ikut ejaan sebutan santai ("korang", "aku", "rupa rupanya", "lost").

## 3. Title Callout (teks atas — poin utama)

- **Kedudukan:** bahagian atas skrin (~15–20% dari atas), tengah.
- **Font:** display tebal **italic/condensed** gaya "comic/impact", **kuning dengan outline coklat/hitam tebal** + drop shadow.
- **Emoji di hujung:** ❌ untuk perkara yang di-"stop", ‼️ untuk poin paling penting.
- **Animasi masuk:** **typewriter** (huruf keluar satu-satu, ±0.25 s — contoh frame "OV…", "PA…").
- **Durasi:** kekal sepanjang poin itu dihuraikan (≈1.5–3 s), kemudian diganti terus dengan title seterusnya.
- Caption bawah tetap berjalan serentak dengan title atas (dua lapis teks).

## 4. Effect & Grading

| Effect | Bila digunakan | Nota |
|---|---|---|
| Flash putih | 0–0.2 s | Pembukaan, tarik perhatian |
| Black & White | Hook (0.2–2.4 s) | Beri rasa "flashback/serius"; warna kembali pada kata kunci |
| Punch-in / zoom crop | Setiap 2–4 s | Selang-seli: medium → close-up → wide. Close-up paling besar untuk momen emosi/nombor ("7 tahun", "rupa-rupanya") |
| Overlay sticker/VFX | Kata "PROFIT" | Money rain (duit $100 jatuh, ±0.8 s) — visual literal kepada kata kunci |
| Grade | Sepanjang video | Natural-warm, saturation sederhana (warna kuning kerusi menonjol), tiada LUT berat |

Tiada B-roll, tiada split screen — **100% talking head**, semua visual tambahan datang dari teks, zoom dan sticker.

## 5. Sound Design

Dari analisis spectrogram & loudness (RMS):

| Masa | Bunyi | Fungsi |
|---|---|---|
| 0.0–1.1 s | SFX tonal / chime-riser (banyak harmonik) | Intro sting bersama flash + B&W |
| ~3.3 s | Whoosh/impact (−14 dB, lebih kuat dari suara) | Tekankan punch-in "7 tahun" |
| ~7.3 s | Pop/click | Title "OVERTRADE" muncul |
| ~8.6 s | Ding (nada ~3.1k/6.2k/9.4k Hz) | Title "REVENGE TRADE" muncul |
| ~10.1 s | Pop/click | Title "PAKSA ENTRY" muncul |
| ~14.5–14.7 s | **Impact paling kuat** (−8 dB) | Poin utama "STOP IKUT ENTRY ORANG" |
| ~16.3 s | Ding | Tekan "faham kenapa dulu" |
| ~19.3 s | Ding/cash SFX | Money rain "PROFIT" |
| ~20.4–20.9 s | Swoosh/noise | Peralihan ke punchline |

- **Tiada background music yang ketara** — semasa jeda, aras bunyi jatuh ke ~−45 dB (hanya noise bilik). Fokus penuh pada suara.
- Suara bersih, lavalier mic (nampak klip mic di baju), dinormalkan sekitar −20 hingga −28 dB RMS.
- Peraturan: **setiap title callout baru = satu SFX**; poin paling penting = SFX paling kuat.

## 6. Transition

- **Tiada transition "fancy"** (tiada slide/spin/glitch). Semua **hard jump cut**.
- "Transition" dibuat oleh **perubahan zoom** antara klip + SFX whoosh.
- Pembukaan: flash putih. Penutup: hard cut ke hitam.

---

## Checklist cepat — "Edit gaya Sample 1"

1. Format 9:16, 1080×1920, 30 fps. Sasaran durasi 20–40 s.
2. Buang semua jeda/silap (jeda ≤0.3 s).
3. Hook 1–2 s pertama yang **sesuai dengan jenis video** (hitam-putih + colour pop hanya satu pilihan).
4. Punch-in/zoom crop setiap 2–4 s; close-up besar pada nombor/emosi.
5. Caption word-by-word, ALL CAPS, putih + highlight **kuning**, 2–3 perkataan, posisi ~62% dari atas.
6. Setiap poin utama → **title callout atas** kuning italic outline tebal, typewriter in, + ❌ / ‼️.
7. Satu SFX (pop/ding/whoosh) setiap kali title atau zoom besar; poin terpenting = impact paling kuat.
8. Sticker/VFX literal pada kata kunci (cth. money rain untuk "profit").
9. BGM **pilihan** — jika guna, pilih ikut mood & duck bawah suara; suara kekal fokus.
10. Akhiri dengan punchline + hard cut ke hitam ~0.5–0.7 s.
