# Gaya Editing: **SAMPLE 27** — Tutorial CapCut "Freeze Frame Character Intro" (EN) — kenalkan watak dengan freeze + cut-out outline putih + nama

> Cara guna: *"Guna effect character intro Sample 27 untuk kenalkan presenter/klien."*
>
> Kreator (studio gelap, mikrofon, neon "LOVE") mengajar cara buat **effect kenalan watak**: video berjalan → **freeze frame** →
> subjek **dipotong keluar dengan outline putih tebal** atas **latar halftone/kotak kelabu**, dengan **nama ALL CAPS tebal + jawatan kecil**
> ("CHRISTIAN / Social Media Manager") → video bersambung. Bahagian tengah (12–155 s) ialah **rakaman skrin CapCut** dalam mockup telefon
> atas latar kertas renyuk dengan **anak panah merah** menunjuk butang. **Nilai utama = teknik effect**, bukan gaya keseluruhan.

## Pilihan pengguna

- Ikut `editing-styles/LEARNINGS.md` (Peraturan Diterima mengatasi apa-apa dalam sample ini).
- Effect ini → **R85 (a)** (tanya ikut job, Claude cadang dulu).

Gambar rujukan: `timeline-1.jpg` … `timeline-8.jpg` (**setiap 0.5 s**), `key-frames.jpg` (10 momen), `audio-spectrogram.jpg`.
**Salinan preview video:** `preview-540p.mp4` (540p, H.264, kad akhir TikTok dibuang).

## Video rujukan

| Item | Nilai |
|---|---|
| Sumber | https://drive.google.com/file/d/1MCSaVpVM3M01WbM218f5eofqgC9LN4SC/view (folder `1OfFviyqvOR45oq_iOwwc4XFs5seswRij`) |
| Durasi / format | **186.9 s** (182.9 s kandungan + kad akhir TikTok) · 576×1024 (9:16, repost TikTok) · 30 fps · H.264 · AAC |
| Genre | Tutorial CapCut (English) |
| Kamera | Presenter studio gelap (medium dekat + mikrofon) · contoh video stok lelaki bertelefon · rakaman skrin telefon |
| Audio | Suara + kemungkinan BGM perlahan (kesimpulan); **−15.4 LUFS**, puncak 0.0 dBFS |
| Watermark | TikTok @dueknoel? (tak jelas) — bukan gaya |

## Struktur & Timing

| Masa | Bahagian | Visual |
|---|---|---|
| 0–3.5 s | Hook "This is how to freeze frame character like this" | Presenter + caption 1 perkataan |
| 3.5–10 s | **Hasil effect** | Video stok → freeze ±5 s: cut-out outline putih + latar halftone + "CHRISTIAN / Social Media Manager" → sambung |
| 10–12 s | "CapCut… free" | Logo CapCut pop |
| 12–155 s | **Langkah demi langkah** | Mockup telefon atas kertas renyuk, anak panah merah: split → freeze → overlay → remove background → stroke putih → latar (filter/kelabu) → teks + animasi |
| 155–162 s | Hasil sekali lagi | Effect penuh |
| 162–183 s | CTA "follow for more" | Presenter |

## Caption

- **1 perkataan ALL CAPS putih tebal** (≈ Montserrat ExtraBold), ±55% dari atas (dada), tiada highlight. Hanya pada presenter.

## Title & Grafik

| Jenis | Contoh | Gaya | Animasi |
|---|---|---|---|
| **Kad nama watak** | "CHRISTIAN" + "Social Media Manager" | ALL CAPS hitam-putih tebal (outline) + baris kecil putih, bawah kiri ±70% | Pop/taip masa freeze |
| **Cut-out outline** | Subjek + stroke putih tebal (±12 px) | Atas latar halftone/kotak kelabu (subjek asal dikelabukan) | Masuk masa freeze |
| Logo app | CapCut | Putih | Pop |
| Penunjuk tutorial | Anak panah merah | Atas mockup telefon | Pop |

## Effect & Transition

- **Freeze frame** ±5 s + cut-out + latar ditukar → **kembali ke video** (hard cut). Selebihnya hard cut.

## Sound Design (kesimpulan — tidak disahkan)

| Masa | Bunyi | Fungsi |
|---|---|---|
| Sepanjang | Suara dominan, BGM sangat perlahan (mungkin) | Isi |
| Freeze | Kemungkinan "hit"/whoosh | Penanda effect |

## Checklist cepat (cara Claude buat effect ini dengan ffmpeg/rembg)

1. Pilih frame ekspresi bagus → `tpad`/`loop` freeze ±2–3 s (sample 5 s — terlalu panjang untuk video klien).
2. `rembg` frame itu → mask → dilate ±12 px → stroke putih.
3. Latar: frame asal dikelabukan + overlay halftone/kotak.
4. Kad nama ALL CAPS + jawatan (ejaan disahkan R15), bawah kiri dalam zon selamat (X6), tak tutup muka (R1).
5. Hard cut kembali ke video.

**Bahan dari pengguna/klien:** nama + jawatan setiap orang yang diperkenalkan; footage dengan subjek jelas (latar tak terlalu sibuk).
