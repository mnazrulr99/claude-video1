---
name: sample-baru
description: Analisis video sample yang SUDAH SIAP diedit (link Google Drive) dan simpan sebagai gaya rujukan baharu "Sample N" dalam editing-styles/. Gunakan bila pengguna hantar video siap edit dan minta Claude belajar gaya editingnya (timing, caption, effect, SFX, transition).
---

# /sample-baru — Belajar gaya dari video sample siap edit

Input: `$ARGUMENTS` (link Google Drive video siap edit; pilihan: nama sample — jika tiada, guna nombor seterusnya).

Balas dalam **Bahasa Melayu santai & mesra**.

## Langkah 0 — Konteks

0. Jalankan `bash tools/setup.sh` dahulu (pasang tool yang tiada dalam container baharu).

1. Baca `editing-styles/README.md` (katalog & Pattern Bersama), `editing-styles/LEARNINGS.md` (peraturan diterima/ditolak) dan sekurang-kurangnya satu `sample-N/README.md` sebagai format rujukan.
2. Tentukan nombor seterusnya: `ls editing-styles` → `sample-<N+1>`.

## Langkah 1 — Muat turun & metadata

```bash
W=<scratchpad>/sample<N>; mkdir -p $W/fr
curl -sSL -o $W/video.mov "https://drive.usercontent.google.com/download?id=<FILE_ID>&export=download&confirm=t"
ffprobe -v error -show_entries format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,pix_fmt,color_transfer -of default=nw=1 $W/video.mov
ffprobe -v error -show_entries format_tags -of default=nw=1 $W/video.mov   # cth. CapCut/Dreamina
```

## Langkah 2 — Ekstrak data analisis

```bash
# Contact sheet bertanda masa (0.5 s)
ffmpeg -i $W/video.mov -vf "fps=2,scale=150:-1,drawtext=text='%{pts\:hms}':fontsize=14:fontcolor=red:box=1:x=2:y=2,tile=12x4,format=yuvj420p" -q:v 3 $W/fr/q%d.jpg
# Spectrogram audio (SFX, BGM, senyap)
ffmpeg -i $W/video.mov -lavfi "showspectrumpic=s=2400x500:legend=1:scale=log" $W/fr/spec.png
# Titik potong
ffmpeg -i $W/video.mov -vf "scale=180:-1,select='gt(scene,0.15)',showinfo" -an -f null - 2>&1 | grep -oE "pts_time:[0-9.]+"
# Loudness setiap 0.2 s (SFX kuat, jeda, BGM, fade)
ffmpeg -i $W/video.mov -af "aresample=44100,asetnsamples=8820,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level" -vn -f null - 2>&1 | grep -oE "RMS_level=[-0-9.inf]+"
# Kecerahan (flash putih, hitam) / saturasi (B&W)
ffmpeg -i $W/video.mov -vf "fps=2,scale=60:-1,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -an -f null - 2>&1 | grep -oE "YAVG=[0-9.]+"
```
Kemudian lihat semua contact sheet + spectrogram, dan ekstrak ~10 **key frames** (360 px, `tile=5x2`) pada momen grafik/transition penting.

## Langkah 3 — Analisis (bahagian wajib dalam README)

Tulis `editing-styles/sample-<N>/README.md` mengikut format sample sedia ada:
1. Tajuk + ringkasan ciri paling ketara + "Cara guna".
2. Pilihan pengguna (salin dari sample lain).
3. Jadual video rujukan (sumber, durasi, format, genre, kamera).
4. **Struktur & Timing** (jadual babak dengan masa) + rentak.
5. **Caption** (gaya, font, highlight, kedudukan % dari atas).
6. **Title & Grafik** (jadual jenis/contoh/gaya/animasi).
7. **Effect & Transition**.
8. **Sound Design** (jadual masa/bunyi/fungsi + BGM). Nyatakan dengan jujur apa yang **kesimpulan** vs disahkan.
9. **Checklist cepat** + bahan yang perlu dari pengguna.

## Langkah 4 — Simpan aset

- Salin `timeline-*.jpg`, `key-frames.jpg`, `audio-spectrogram.jpg` (JPG, bukan PNG 16-bit).
- **Preview video** `preview-540p.mp4`: `scale=540:-2`, libx264 `-crf 30 -preset slow -pix_fmt yuv420p`, AAC 96k, `+faststart`.
  Jika HDR → tonemap dahulu (lihat skill edit-video). Semak satu frame warna normal.

## Langkah 5 — Kemas kini katalog & pattern

Dalam `editing-styles/README.md`:
- Tambah baris dalam jadual katalog.
- Tambah lajur sample baharu dalam **"Pattern Bersama"**, kemas kini lajur Kesimpulan & **Pemerhatian** (pattern berulang = selera pengguna).

## Langkah 5b — Pembelajaran

Jika sample baharu menunjukkan pattern yang bercanggah dengan **Peraturan Diterima** atau mengandungi perkara dalam
**Ditolak**, nyatakan kepada pengguna (jangan terus belajar perkara itu). Cadangan peraturan baharu → masukkan dalam
"🕒 Menunggu keputusan pengguna" dalam `LEARNINGS.md` sehingga disahkan.

## Langkah 6 — Commit & push

Commit dengan mesej jelas, push ke branch kerja **dan** `main` (pengguna sudah benarkan kemas kini `main` untuk pengetahuan editing).

## Langkah 7 — Lapor kepada pengguna

Ringkasan mesra: fakta video, timing, caption, grafik, effect/transition, sound, pattern baharu yang ditemui,
lokasi fail, dan sahkan **preview dah disimpan → video asal boleh dipadam dari Google Drive**.
Akhiri dengan satu soalan penjelasan jika ada perkara yang tidak pasti (cth. BGM).
