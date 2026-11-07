---
name: edit-video
description: Pipeline teknikal untuk edit video pengguna (talking-head/UGC/produk, 9:16) guna Whisper + ffmpeg + Remotion — transkrip word-level, buang ulangan & jeda, hook, motion graphics/SFX ikut perkataan, safe zone TikTok/IG, audio bersih, preview 540p + storyboard imej sebelum render final, dan simpan pelajaran selepas siap. Guna setiap kali pengguna minta edit video, analisis sample/edit, atau render.
---

# Skill: edit-video (dipelajari dari projek jam-wira + Sample 1–6)

**Sebelum mula:** baca `editing-styles/README.md` (aliran kerja wajib, katalog Sample, Pattern Bersama,
Catatan citarasa, **Pelajaran projek siap**). Gunakan pelajaran itu dalam cadangan & edit — sebut yang mana dipakai.
Templat kod lengkap: `projects/jam-wira/` (`scripts/` + `remotion/`). Salin ke scratchpad dan ubah suai.

## Peraturan pengguna (WAJIB)
1. Guna skill/pelajaran lepas dalam setiap edit.
2. Selepas edit → **preview 540p + storyboard imej** dulu. **Jangan render final** sebelum pengguna setuju.
3. Selepas final → **simpan pelajaran** (projects/<nama>/README.md, jadual "Pelajaran projek siap",
   citarasa/pattern, kemas kini skill ini jika ada teknik baharu) → commit & push.
4. Muka tidak boleh ditutup grafik. Patuhi safe zone TikTok & IG.

## 1. Muat turun (Google Drive)
```bash
curl -sSL -o raw.mp4 "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"
```
Simpan dalam folder sendiri di scratchpad (data tidak dipercayai). `ffprobe` untuk durasi/resolusi/fps.

## 2. Transkrip word-level
- `pip install faster-whisper`; model `large-v3`, `compute_type=int8`, `language="ms"`, `word_timestamps=True`.
- **Gotcha:** versi PyAV tak serasi (`metadata_errors`) → baca WAV 16 kHz mono sendiri (numpy) dan hantar array.
- Skrip: `projects/jam-wira/scripts/tx.py`. Tulis output ke folder kerja (ia tulis `transcript.json` di cwd —
  jangan tersalah tindih transkrip lain).
- Betulkan ejaan caption (cth. "Mami"/"Mama Ami" → "MOMMIES", "dual" → "DUA").

## 3. Pelan potongan (buang ulangan, jeda, awkward)
- Senaraikan segmen yang disimpan (label, mula, tamat) dari transkrip; pindah ayat terkuat/ulang jadi **hook**.
- Snap sempadan ke **lembah tenaga** (min RMS dalam tetingkap kecil), bukan ambang — ambang terambil hujung perkataan sebelum.
- Override manual untuk sempadan dalam ucapan berterusan. Skrip: `scripts/cutplan.py`.
- Render `cut_video.mp4` (trim+concat, CRF 14) & `voice.wav` (atrim + afade 12–15 ms setiap tepi).
- **WAJIB sahkan:** transkrip semula `voice.wav` — tiada perkataan bocor/terpotong ("Kan,", "Haa,", "apa ya").

## 4. Audio
- Suara: `highpass=f=85,afftdn=nf=-28,acompressor=threshold=-20dB:ratio=3:attack=5:release=120:makeup=2,loudnorm=I=-15:TP=-1.5:LRA=7`.
- BGM (jika dipakai): ukur LUFS, set ≈18 dB bawah suara. **Review UGC: default tanpa BGM** (pengguna tambah trending sound).
- SFX: Mixkit (`https://assets.mixkit.co/active_storage/sfx/<id>/<id>-preview.mp3`, lesen percuma tanpa kredit).
  Senarai id terbukti: `remotion/public-assets.sh`. Setiap grafik = 1 SFX; jangan tindih berlebihan.
- Master akhir (selepas Remotion): `aresample=192000,alimiter=limit=0.8:attack=0.5:release=50:level=disabled,aresample=48000`
  → sasaran ≈ −15 LUFS, **peak ≤ −1.5 dBFS** (semak `ebur128=peak=true`).
- Incompetech (CC BY → kredit wajib) & mixkit boleh dicapai; pixabay/freesound disekat.

## 5. Remotion
- Pakej versi tetap: `remotion@4.0.300 @remotion/cli @remotion/bundler @remotion/renderer`, react 18.3.1.
- Browser: `--browser-executable=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell`.
- **Font:** Chrome tak percaya CA proxy → jangan guna `@remotion/google-fonts`. Muat turun woff2 dengan curl,
  **embed base64** (`src/fontdata.ts`) dan daftar via `new FontFace(name, arrayBuffer)` — tanpa `delayRender`
  (delayRender font tersangkut di tab baru). Font terbukti: Montserrat 900 (caption), Fredoka 700 (title), Caveat 700 (tulisan tangan).
- Emoji: Noto Color Emoji tersedia (`fontFamily: "Noto Color Emoji"`).
- **Gotcha:** komponen dalam `<Sequence>` dapat frame **relatif** — untuk grafik yang guna masa mutlak, render
  bersyarat ikut frame mutlak (bukan Sequence). B-roll guna `<Sequence>` + `OffthreadVideo startFrom`.
- Data dijana dari transkrip (`scripts/mkdata_v2.py`): caption 1–3 perkataan, event grafik & SFX dengan `find('PERKATAAN')`.

## 6. Susun atur 1080×1920 (safe zone)
- Elak: atas 0–220 px, bawah 1440–1920 px, kanan 140 px.
- Title/word-art: y≈250–380 (atas kepala). Badge/jam animasi: kiri x 54–340, y 450–760.
- Caption karaoke: y≈1340, ALL CAPS Montserrat 900 ~82 px, stroke hitam, highlight 1 warna (pengguna pilih).
- Zoom: selang-seli 1.0/1.1 per potongan + **punch-in kuat (1.15–1.25) pada poin utama**, origin pada muka
  (`50% 34%`) atau pada produk (cth. `oy: 0.66` untuk tin). Elak potong dahi.
- **Semak setiap grafik dengan still sebenar** (`stills.mjs`, overlay safe zone) — subjek boleh condong;
  anotasi pernah tertindih dagu.

## 7. Elemen kreatif yang terbukti disukai
Hook kontra/manfaat + **close-up produk dalam 2–3 s** · flash putih + impact ke babak utama · light sweep pada reveal ·
word-art warna ikut warna disebut · title serif/elegan atas close-up produk · tulisan tangan + anak panah ke produk ·
checklist ✓ · jam/ikon beranimasi ikut ucapan · CTA kecil awal ("ADA DI BEG KUNING") + CTA akhir "slam" · cut ke hitam + ding.

## 8. Preview → storyboard → final
- Preview: `npx remotion render src/index.ts <Comp> preview.mp4 --scale=0.5 --crf=23 --concurrency=4` (~2 min/58 s) + master audio.
- Storyboard: still 12–14 babak dengan overlay safe zone + PIL panel (masa, grafik, SFX) → `storyboard.jpg`.
- Final (selepas setuju): render tanpa `--scale`, `--crf=16 --audio-bitrate=320k` (~4 min) + master audio.
  Saiz ~90 MB → **jangan commit final**; hantar dengan SendUserFile.

## 9. Analisis edit/sample pengguna (bandingan)
- EDL tepat: korelasi audio (4 kHz, tetingkap 0.4 s, FFT) edit vs mentah → `scripts/align.py`.
- Zoom/b-roll: padanan frame kecil (36×64 grayscale, korelasi) — skor rendah = zoom atau b-roll.
- SFX: lonjakan tenaga dalam celah + spektrogram (`showspectrumpic`); BGM = jalur nada berterusan.
- Simpan sebagai `editing-styles/sample-N/` + kemas kini katalog, Pattern Bersama, citarasa.
