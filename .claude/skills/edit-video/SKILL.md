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
3. Baca `editing-styles/LEARNINGS.md` — ikut **semua Peraturan Diterima**, dan **jangan guna** apa-apa dalam **Ditolak**.
4. Ikut **"Catatan citarasa pengguna"** — ia (dan LEARNINGS.md) mengatasi lalai dalam skill ini.

## ⛔ Urutan WAJIB terkini (R23–R28) — ikut sebelum langkah lain

0. **Format:** tanya pengguna landscape (1920×1080) atau 9:16 jika job highlight acara/footage landscape (R30).
1. **Semak audio dahulu:** `python3 -I tools/audio_check.py <video>` → jika **BERHENTI**, berhenti & beritahu pengguna
   (nyatakan angka: LUFS, puncak, % senyap). AMARAN → maklumkan & tanya. (R23)
2. **Transkrip:** biasa (`tools/transcribe.py`, untuk caption) + verbatim (`--verbatim`) → `python3 -I tools/stutter.py transcript-verbatim.json`
   → tunjuk **senarai bernombor** ayat tersangkut/ulang/isian/jeda. **Jangan potong** — pengguna pilih nombor yang dibuang. (R24)
3. **Pelan edit dalam jadual** `Saat | Layout | Visual | Kenapa`, visual bertukar setiap **2–4 s**. (R25)
4. **Papan layout:** SATU imej mengandungi semua layout/babak (grid) — tunggu kelulusan sebelum render. (R26)
5. Caption **1–3 perkataan**; perkataan penting **dibesarkan masa close-up**. (R27)
6. SFX: **`whoosh-soft.wav`** setiap tukar visual (`data-volume` ±0.5); bunyi lain dibenarkan ikut kesesuaian. (R28)
7. **Aliran kelulusan (R29):** storyboard + papan layout (sebelum render) → pengguna OK → render **PREVIEW** (Langkah 4b) →
   klien semak → feedback/ulang → klien OK → render **FINAL**. Jangan langkau pintu kelulusan.

## Langkah 0.5 — Semak persekitaran (cloud atau komputer pengguna)

Pengguna bertukar-tukar antara **session cloud** dan **Claude Code di komputer sendiri**. Semak tool yang ada dahulu:

```bash
node -v; ffmpeg -version | head -1
python3 -c "import faster_whisper" 2>/dev/null && echo faster-whisper || (which whisper && echo openai-whisper)
npx -y hyperframes --version; ls node_modules/.bin/remotion 2>/dev/null || echo "remotion: guna projek sendiri"
```
- **Cloud:** Node 22 & ffmpeg sedia ada. Pasang yang tiada: `pip install -q faster-whisper` (±1–2 min, model medium ±1.5 GB);
  HyperFrames & Remotion jalan melalui `npx` / `npm i` (diuji: hyperframes 0.9.20 dan remotion render berjaya di cloud).
- **Komputer pengguna (local):** pengguna sudah pasang Node LTS, ffmpeg, Whisper, HyperFrames & Remotion. Guna yang ada;
  jika `tools/transcribe.py` gagal kerana tiada `faster_whisper`, guna CLI `whisper <fail> --language ms --model medium --word_timestamps True --output_format json`.
  Simpan video siap dalam folder yang pengguna boleh buka (cth. `output/` dalam repo — **jangan commit**).
- Nyatakan kepada pengguna persekitaran mana yang sedang digunakan.

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

### Banyak fail (video raw + gambar dari customer)

Jumlah fail tak tentu (ikut customer). Cara terima, ikut keutamaan:
1. **Link folder Google Drive** ("Anyone with the link can view"): `pip install -q gdown` →
   `gdown --folder "<link>" -O $W/input` (had ±50 fail/folder; jika lebih, minta pengguna pecah folder atau guna cara 2).
   **BELUM DIUJI** — jika gagal (folder private/had/ralat), beritahu pengguna dan guna cara 2.
2. **Senarai link fail satu-satu** (+ nota ringkas setiap fail) — terbukti berfungsi (curl `drive.usercontent.google.com`).
3. **Session di komputer pengguna:** fail dalam `input/<job>/` dalam repo (diabaikan git).

Selepas terima: **inventori** (jadual: nama, jenis, durasi/resolusi, HDR?, ringkasan isi) + **contact sheet thumbnail**
semua fail → analisis setiap video (transkrip, momen terbaik) → **cadang susunan** (hook, klip utama, B-roll, gambar mana
di-overlay pada babak mana & kenapa) dalam peringkat cadangan/storyboard. Gambar produk: semak resolusi & latar
(PNG lutsinar lebih baik); overlay ikut R1 (tak tutup muka).

## Langkah 2 — Analisis & CADANG gaya (jangan edit lagi)

1. Contact sheet: `fps=2,scale=150:-1,drawtext(timestamp),tile=12x4` → lihat isi video.
2. Transkrip **dengan masa setiap perkataan** (perlu untuk caption karaoke):
   `python3 -I tools/transcribe.py <video> $W/transcript.json` (lalai: model `medium`, bahasa `ms`).
   - Jika `faster_whisper` belum dipasang: `pip install -q faster-whisper` (model ±1.5 GB dimuat turun kali pertama).
   - Tool ini nyahkod audio dengan ffmpeg (elak isu versi PyAV). `medium` ≈ 1.5× tempoh video pada CPU; `small` lebih laju tapi kurang tepat.
   - Semak & betulkan ejaan Bahasa Melayu santai secara manual (cth. "Korang", istilah English/jenama).
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

**Pembahagian tool:**
| Tugas | Tool |
|---|---|
| Potong jeda/jump cut, crop/punch-in, tonemap HDR, normalisasi audio, gabung akhir | **ffmpeg** |
| Transkrip masa setiap perkataan | **Whisper** (`tools/transcribe.py` atau CLI whisper) |
| Caption karaoke, title typewriter, label/pill/badge, checklist ✅, sticker, marquee, transition grafik | **HyperFrames** (lalai — HTML/CSS + animasi boleh-seek) |
| Animasi kompleks / berasaskan data, atau bila HyperFrames tidak sesuai | **Remotion** (React) |

**Aliran lalai:**
1. ffmpeg: hasilkan `base.mp4` 1080×1920 yang sudah dipotong (jump cut ikut transkrip, punch-in per segmen, SDR bt709, 30/60 fps).
2. Laraskan masa transkrip kepada timeline `base.mp4` (selepas potongan).
3. HyperFrames: `npx -y hyperframes init edit --example blank --resolution portrait --non-interactive --skip-skills --skip-transcribe`
   → komposisi `index.html` dengan `base.mp4` sebagai trek video + lapisan caption/title/sticker + trek SFX & BGM.
   Guna `npx hyperframes lint` / `check`, `snapshot` untuk semak frame, kemudian `npx hyperframes render`.
   (`npx hyperframes docs` untuk rujukan; `hyperframes add <block>` untuk blok sedia ada seperti transition.)
4. Alternatif Remotion: projek `npm i remotion @remotion/cli react react-dom`, `<OffthreadVideo src=base.mp4>` + lapisan,
   `npx remotion render src/index.ts <Comp> out.mp4`. (Lesen Remotion: percuma untuk individu/syarikat kecil — rujuk remotion.dev/license.)
5. ffmpeg akhir: pastikan H.264 `-crf 18 -pix_fmt yuv420p`, AAC 192k, `+faststart`; BGM ≈ −20 dB di bawah suara, fade-out hujung.

**Spesifikasi:** 1080×1920, 9:16; SFX pada setiap grafik baru; ending cut/fade ke hitam ±0.5–1 s.
**Semak sebelum hantar:** beberapa frame (caption tak terpotong, dalam zon selamat TikTok), loudness, sync caption.
Hantar video siap + teks kredit BGM (jika perlu).

## Langkah 4b — Preview untuk klien (WAJIB, R22)

1. Selepas render (dan semakan dalaman), hasilkan pakej klien dalam `output/<job>/`:
   - `python3 -I tools/client_preview.py <render>.mp4 output/<job>/<job>-PREVIEW-v<n>.mp4` (540p, watermark SATU perkataan "PREVIEW" di tengah sahaja, ±4 MB/50 s)
   - Storyboard **dua versi** dengan frame SEBENAR dari render: `python3 -I storyboard.py <dir_skrip> <dir_job> output/<job> <render.mp4>`
     → **A** `storyboard-<k>.jpg` (untuk pengguna, nota teknikal: SFX, punch-in, dll.) dan
     **B** `storyboard-klien-<k>.jpg` (untuk klien, ringkas: masa + apa yang dilihat, tiada istilah teknikal; isi lajur ke-4 `PANELS`).
   - Watermark versi B sahaja: `python3 -I tools/client_preview.py --image storyboard-klien-<k>.jpg output/<job>/storyboard-klien-<k>-PREVIEW.jpg`
2. Hantar kepada pengguna (SendUserFile) — **jangan** hantar fail resolusi penuh tanpa watermark pada peringkat ini.
3. Pengguna bawa balik feedback klien → betulkan → preview baharu `-PREVIEW-v<n+1>`. Ulang.
4. Bila pengguna kata klien setuju → **final**: render penuh 1080×1920 tanpa watermark, loudnorm (R14) →
   `output/<job>/<job>-FINAL.mp4`. Simpan render penuh dalam scratchpad supaya final tak perlu render semula jika tiada perubahan.
5. Feedback klien yang boleh jadi peraturan umum → cadang kepada pengguna untuk `LEARNINGS.md` (Langkah 5).

## Pengajaran dari job ujian pertama (periuk, 52 s) — WAJIB ikut

- **Templat sedia guna** dalam `tools/templates/` (salin ke scratchpad, sunting `plan.py` untuk job baru):
  `plan.py` (HOOK, SEGMENTS+zoom, FIXES ejaan, GRAPHICS, SIZE_TIMES, `src_to_out`) →
  `storyboard.py <dir_skrip> <dir_job> <dir_output>` (PIL, 2 halaman × 5 panel) →
  `base.py <dir_skrip> <dir_job>` (ffmpeg: hook senyap + potongan + punch-in → `base.mp4`) →
  `hf.py <dir_skrip> <dir_job>` (jana `hfproj/index.html`: video + caption karaoke + grafik GSAP + SFX).
  Projek HyperFrames: salin `hyperframes.json`, `meta.json`, `package.json` dari `npx hyperframes init`, symlink `base.mp4`,
  `sfx/` (dari `tools/sfx/`) dan `fonts/` (Inter-Black, Inter-ExtraBold, LiberationSerif-BoldItalic).
- **Kedudukan tulisan (citarasa pengguna — WAJIB):** jangan tutup **muka**; sedaya upaya jangan tutup **produk**.
  Sebelum storyboard: jalankan `python3 -I tools/zones.py base.mp4 <mula:tamat ...> --hsv <julat warna produk>`
  (YuNet untuk muka, model dalam `tools/models/`; perlu `pip install opencv-python-headless`) → peta grid F/P/. bagi setiap babak.
  Pilih zon kosong (cth. dinding kiri atas) dan set `SAFE` dalam `plan.py` (x, w, gfx_top, cap_top); semua grafik & caption
  diletak dalam zon itu (kecilkan saiz jika perlu). Jika latar sama warna dengan produk, naikkan `smin` dalam `--hsv`.
  Storyboard mesti tunjuk kedudukan sebenar; semak semula dengan `hyperframes snapshot` sebelum render.
- **Dari /compare-learnedit periuk (lihat LEARNINGS.md R1a–R16):**
  - `base.py`: zoom asas **1.2×** (bukan 1.0) untuk setiap segmen (R6); punch-in ekstrem (1.5–1.8×) pada produk masa sebut saiz/bahagian (R7).
  - Hook lalai = klip flash-forward ±1 s (R5). Tamat dengan hitam 0.5–0.7 s + ding (R12). Potong jeda ketat (R11).
  - Caption **gaya versi Claude** (R16): ALL CAPS Inter ExtraBold ±54–60 px, putih + outline hitam, perkataan aktif tukar warna teks (bukan kotak);  boleh di bahagian bawah produk ±72–80% dari atas tapi **jauh dari muka** (R1a) — semak `zones.py`.
  - Label bahagian produk (cth. "16CM") terus atas bahagian itu (R1b). Title font/warna ikut produk (R8). Callout + doodle sparkle dekat benda disebut (R9).
  - Satu transition kreatif di tengah (R10, cth. paper-rip). CTA di zon selamat (R13; X2 = jangan tutup produk).
  - Kelantangan: **loudnorm dua laluan** ke −14 LUFS (R14):
    `ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null -` → guna nilai measured_* dalam laluan kedua (`linear=true`).
  - Nama presenter: tanya/sahkan; jangan teka "akak" (R15).
- **SFX:** `tools/sfx/` (whoosh, pop, ding, sparkle, impact, chime — disintesis ffmpeg, puncak −6 dB, guna `data-volume` 0.35–0.6).
- **HyperFrames:** setiap `<audio>`/`<video>` **mesti ada `id`** (tanpa id → SENYAP dalam render). Klip audio tak boleh melepasi
  `data-duration` root. Amaran `nested_structure_needs_subcomposition` boleh diabaikan.
- Semak dengan `npx hyperframes lint` (0 error) dan `npx hyperframes snapshot --at ...` (lihat contact sheet) **sebelum** render.
- Masa render cloud: ±3.5 min untuk 52 s (1080×1920, CPU). Fail render ±70 MB.
- Akhir: `loudnorm=I=-14:TP=-1.5:LRA=11`, libx264 crf 18, AAC 192k, `+faststart` → `output/<job>/<nama>-final.mp4`.
- Video raw resolusi rendah (cth. 464×848) akan lembut bila dibesarkan — maklumkan pengguna awal.
- Whisper keliru nama/sapaan (cth. "seller"→"selera", "akak"→"enak") — senaraikan tekaan dan minta pengguna sahkan.

## Langkah 5 — Belajar dari maklum balas (pembelajaran berterusan)

- Setiap komen pengguna pada storyboard atau video siap = data pembelajaran. Selepas membetulkan, cadangkan satu
  peraturan umum (cth. "tulisan tak boleh tutup muka") dan tanya pengguna sama ada mahu simpan sebagai peraturan tetap.
- Bila disahkan: tambah ke `editing-styles/LEARNINGS.md` (Peraturan Diterima / Ditolak + Log), kemas kini templat/skill
  jika perlu, commit & push ke branch kerja dan `main`.
- Jika pengguna kemudian edit sendiri video yang sama, cadangkan `/compare-learnedit` untuk banding & belajar.

## Nota

- Simpan fail kerja dalam scratchpad; **jangan commit video job pengguna** ke repo.
- Jika pengguna beri komen baharu tentang citarasa, kemas kini "Catatan citarasa pengguna" dalam `editing-styles/README.md`,
  commit & push ke branch kerja dan `main` (dengan izin pengguna yang telah diberi).
