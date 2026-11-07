---
name: edit-video
description: Edit video mentah pengguna mengikut gaya rujukan (Sample 1, 2, 3, …) dalam editing-styles/. Gunakan bila pengguna hantar video raw (link Google Drive atau fail) dan minta edit. Prosedur wajib - analisis, cadang gaya, storyboard imej, tunggu setuju, baru render dengan ffmpeg.
---

# /edit-video — Edit video mentah pengguna

Input: `$ARGUMENTS` (link Google Drive / laluan fail video raw, pilihan: nama gaya, gambar produk).

Balas dalam **Bahasa Melayu santai & mesra**. Pengguna **tidak guna sebarang app editing** — Claude render terus.

## Langkah 0 — Baca rujukan dahulu (WAJIB)

1. Baca `editing-styles/README.md` (katalog gaya, aliran kerja, Pattern Bersama, citarasa pengguna, senarai BGM).
2. Baca `editing-styles/sample-N/README.md` untuk gaya yang berkaitan (lihat juga `key-frames.jpg`).
3. Ikut **"Catatan citarasa pengguna"** — ia mengatasi lalai dalam skill ini.

## Langkah 1 — Muat turun & semak video raw

```bash
W=<scratchpad>/job-<nama>; mkdir -p $W/fr
# Google Drive: ambil FILE_ID dari /file/d/<FILE_ID>/view
curl -sSL -o $W/raw.bin "https://drive.usercontent.google.com/download?id=<FILE_ID>&export=download&confirm=t"
ffprobe -v error -show_entries format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,pix_fmt,color_transfer -of default=nw=1 $W/raw.bin
```
- Jika `color_transfer=arib-std-b67` / `smpte2084` → video **HDR** (iPhone): tonemap ke SDR bt709 semasa proses
  (`zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p`).
- Gambar produk daripada pengguna: simpan dalam `$W/assets/`. Jika tiada, maklumkan bahawa Claude akan potong dari video.

## Langkah 2 — Analisis & CADANG gaya (jangan edit lagi)

1. Contact sheet: `fps=2,scale=150:-1,drawtext(timestamp),tile=12x4` → lihat isi video.
2. Transkrip **dengan masa setiap perkataan** (perlu untuk caption karaoke):
   `pip install faster-whisper` (atau `openai-whisper`), model `small`/`medium`, bahasa `ms`, `word_timestamps=True`.
   Semak ejaan Bahasa Melayu santai secara manual.
3. Kenal pasti: jenis video (bercakap ke kamera vs faceless tanpa suara; edukasi vs produk), mood, kualiti audio, jeda/silap.
4. Bentangkan kepada pengguna:
   - **Gaya dicadang** (Sample mana / gabungan) + sebab.
   - **Hook** dicadang (ikut jenis video — bukan semestinya sama dengan sample).
   - **Warna highlight caption**: 2–3 pilihan + sebab (padan brand/produk vs warna sample).
   - **BGM**: 3–5 pilihan royalty-free dengan link YouTube untuk didengar (sumber rasmi: bensound.com, incompetech.com,
     YouTube Audio Library; nyatakan keperluan kredit). Video tanpa suara: jika tiada yang sesuai → SFX sahaja.
   - Bahan yang masih diperlukan (logo, gambar produk, CTA, dsb.).
5. **Tunggu pengguna pilih.** Untuk semua pilihan kreatif: Claude cadang, pengguna putuskan.

## Langkah 3 — STORYBOARD imej (jangan render lagi)

Hasilkan imej storyboard (PNG/JPG, satu atau beberapa halaman) — setiap babak satu panel:
- Frame sebenar dari video (dengan mock-up caption/title/sticker dilukis atas frame jika boleh).
- Label: **masa mula–tamat**, teks caption, title/grafik, zoom/punch-in, effect, transition, SFX, BGM.
Hantar kepada pengguna (SendUserFile, display render). **Tunggu komen; ulang sehingga pengguna kata setuju.**

## Langkah 4 — Render (selepas setuju sahaja)

- Output: **1080×1920, 9:16**, 30 fps (atau 60 jika sumber 60), H.264 `-crf 18 -preset slow -pix_fmt yuv420p`, AAC 192k, `+faststart`.
- Potong jeda/silap (jump cut) mengikut transkrip; punch-in dengan `crop`+`scale` per segmen.
- Caption karaoke: jana fail **ASS** (word-by-word, ALL CAPS, highlight warna/kotak dipilih) dan bakar dengan `subtitles=`/`ass=`.
- Title/callout: ASS (animasi typewriter = `\k`/beberapa event) atau overlay PNG; sticker/emoji = overlay PNG.
- SFX pada setiap grafik baru; BGM perlahan (≈ −20 dB di bawah suara, `sidechaincompress` atau volume tetap), fade-out hujung.
- Ending: cut/fade ke hitam ±0.5–1 s.
- Semak hasil: ambil beberapa frame & semak loudness sebelum hantar. Hantar video siap + teks kredit BGM (jika perlu).

## Nota

- Simpan fail kerja dalam scratchpad; **jangan commit video job pengguna** ke repo.
- Jika pengguna beri komen baharu tentang citarasa, kemas kini "Catatan citarasa pengguna" dalam `editing-styles/README.md`,
  commit & push ke branch kerja dan `main` (dengan izin pengguna yang telah diberi).
