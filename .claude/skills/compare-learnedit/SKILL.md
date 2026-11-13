---
name: compare-learnedit
description: Banding video yang pengguna EDIT SENDIRI dengan cara Claude edit (versi Claude bagi raw yang sama, atau gaya dalam editing-styles/), kenal pasti apa yang patut dipelajari dan apa yang tidak, dan simpan ke editing-styles/LEARNINGS.md untuk pembelajaran berterusan. Gunakan bila pengguna hantar video hasil edit sendiri untuk Claude banding & belajar.
---

# /compare-learnedit — Banding edit pengguna & belajar secara berterusan

Input: `$ARGUMENTS` — link Google Drive video yang **pengguna edit sendiri**. Pilihan: link/nama video raw atau job Claude
yang sama (cth. "job periuk" → `output/test1/periuk-final-v2.mp4`), dan nota pengguna (apa yang dia suka/tak suka).

Balas dalam **Bahasa Melayu santai & mesra**. Ikut prinsip: **Claude cadang, pengguna putuskan** — tiada apa disimpan
sebagai peraturan sebelum pengguna sahkan.

## Langkah 0 — Konteks

0. Jalankan `bash tools/setup.sh` dahulu (pasang tool yang tiada dalam container baharu).

1. Baca `editing-styles/LEARNINGS.md` (peraturan diterima, ditolak, menunggu) dan `editing-styles/README.md`
   (katalog, Pattern Bersama, citarasa).
2. Tentukan **asas perbandingan** (tanya pengguna jika tak jelas):
   - **A. Raw yang sama** — ada versi Claude (fail dalam `output/<job>/` atau link) → banding terus, babak demi babak.
   - **B. Tiada versi Claude** — banding dengan gaya Sample paling hampir + Pattern Bersama + Peraturan Diterima.

## Langkah 1 — Analisis video pengguna

Ikut Langkah 1–2 skill `sample-baru` (muat turun, metadata, contact sheet 0.5 s, spectrogram, titik potong, loudness,
kecerahan, key frames). Tambah:
- Transkrip (`tools/transcribe.py`) jika ada suara — untuk banding potongan & caption.
- `tools/zones.py` untuk semak sama ada tulisan pengguna menutup muka/produk.

## Langkah 2 — Perbandingan (jadual)

Jika asas A, jana **contact sheet sebelah-menyebelah** (versi pengguna | versi Claude, masa yang sepadan) — contohnya
`ffmpeg -i user.mp4 -i claude.mp4 -filter_complex "[0]fps=1,scale=180:-1[a];[1]fps=1,scale=180:-1[b];[a][b]hstack,tile=6x5"`.

Banding mengikut kategori: **Struktur & hook · Rentak/potongan · Framing/zoom · Caption (font, warna, kedudukan, saiz,
jumlah perkataan) · Title & grafik · Kedudukan teks vs muka/produk · Effect & transition · SFX · BGM & audio · Ending · CTA**.

Untuk setiap perbezaan, cadangkan satu klasifikasi dengan sebab:
- ✅ **Boleh belajar** — lebih baik/konsisten dengan citarasa (bukti: pattern berulang, kebolehbacaan, tak tutup muka,
  zon selamat TikTok, rentak, kejelasan CTA, kelantangan).
- ❌ **Jangan belajar** — kesilapan atau tak sesuai (cth. teks terkeluar/terpotong, typo, tutup muka/produk,
  bertentangan dengan Peraturan Diterima, audio clipping, teks dalam zon UI TikTok, perkara khusus satu produk sahaja).
- ❓ **Tak pasti** — tanya pengguna (cth. pilihan kreatif yang sah dua-dua cara).

Juga senaraikan **apa yang Claude buat lebih baik** (jika ada) — jujur, berdasarkan bukti, tanpa memihak.

## Langkah 3 — Bentang & tunggu keputusan

Tunjuk kepada pengguna:
1. Imej perbandingan (SendUserFile, display render).
2. Jadual: kategori · versi pengguna · versi Claude/gaya · cadangan (✅/❌/❓) · sebab.
3. Minta pengguna sahkan setiap item (cth. "1 ✅, 2 ❌, 3 ✅ …"). **Jangan simpan apa-apa sebelum disahkan.**
   Item yang belum dijawab → masukkan dalam "🕒 Menunggu keputusan pengguna".

## Langkah 4 — Simpan pembelajaran (selepas pengguna sahkan)

Dalam `editing-styles/LEARNINGS.md`:
- ✅ → tambah baris **Peraturan Diterima** (ID baharu `R<n>`, peraturan yang boleh diambil tindakan, kategori, sumber, tarikh).
  Jika ia menggantikan peraturan lama, tandakan peraturan lama sebagai "(diganti oleh R<n>)".
- ❌ → tambah baris **Ditolak** (ID `X<n>`, perkara, sebab).
- Tambah satu baris dalam **Log perbandingan**.
Jika pembelajaran mengubah gaya tertentu, kemas kini juga `editing-styles/sample-N/README.md` atau "Pattern Bersama".
Jika ia mengubah cara render (cth. saiz font lalai, kedudukan caption), kemas kini `tools/templates/` dan nota dalam
`.claude/skills/edit-video/SKILL.md`.

Simpan juga bahan rujukan kecil: `editing-styles/comparisons/<tarikh>-<nama>/` (contact sheet perbandingan JPG +
`preview-540p.mp4` video pengguna) — supaya boleh semak semula; pengguna boleh padam video asal di Google Drive.

## Langkah 5 — Commit & push

Commit dengan mesej jelas; push ke branch kerja **dan** `main` (pengguna sudah benarkan kemas kini `main` untuk
pengetahuan editing). Lapor kepada pengguna: apa yang dipelajari, apa yang ditolak, dan bagaimana ia akan mengubah edit akan datang.
