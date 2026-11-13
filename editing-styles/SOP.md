# SOP Editing Video

> Prosedur standard setiap job editing, untuk **pengguna + Claude**. Claude WAJIB ikut SOP ini dalam setiap session
> (phone/cloud atau desktop/local). Peraturan terperinci: [LEARNINGS.md](LEARNINGS.md) (nombor R/X dirujuk di bawah).
> Jika SOP bercanggah dengan arahan terus pengguna → arahan pengguna menang; kemudian kemas kini SOP.

**Simbol:** 🧑 = tugas pengguna · 🤖 = tugas Claude · ⛔ = **pintu kelulusan** (jangan teruskan tanpa "OK" pengguna)

---

## Gambaran keseluruhan

| Fasa | Apa | Pintu kelulusan |
|---|---|---|
| 0 | Persediaan session | — |
| 1 | Terima job & bahan | ⛔ G1: brief lengkap |
| 2 | Semak teknikal (audio, video) | ⛔ G2: lulus semakan / pengguna setuju teruskan |
| 3 | Transkrip → senarai trim → **PDF transkrip** & cadangan | ⛔ G3a: pilih trim, gaya, hook, warna, BGM · ⛔ G3b: sahkan PDF transkrip |
| 4 | Pelan edit + storyboard + papan layout | ⛔ G4: pengguna lulus pelan |
| 5 | Render PREVIEW + pakej klien | ⛔ G5: pengguna setuju hantar ke klien |
| 6 | Semakan & feedback klien (ulang) | ⛔ G6: klien OK semua |
| 7 | Render FINAL & hantar | — |
| 8 | Arkib & belajar | — |

---

## Fasa 0 — Persediaan session 🤖

1. **Desktop/local:** 🧑 pastikan folder `claude-video1` dibuka dan **Pull** versi terbaru (GitHub Desktop → Fetch → Pull).
2. 🤖 `git pull origin main` (cloud: automatik) supaya guna peraturan terkini.
3. 🤖 `bash tools/setup.sh` — semak/pasang semua tool. Mana-mana ❌ → beritahu pengguna sebelum mula.
4. 🤖 Baca `editing-styles/README.md`, `LEARNINGS.md`, dan SOP ini.

## Fasa 1 — Terima job & bahan 🧑🤖

**🧑 Pengguna hantar (brief job):**

| Perkara | Wajib? | Contoh |
|---|---|---|
| Video raw | ✅ | Link Google Drive (fail atau folder "Anyone with the link") / `input/<job>/` di desktop |
| Nama job | ✅ | `periuk-yana` |
| Jenis video | ✅ | UGC bercakap · faceless · review makanan · unboxing · servis/premis · skit+vlog · highlight acara |
| Platform & format | ✅ | TikTok/Reels **9:16** · YouTube/FB **landscape** · kedua-dua (R30) |
| Nama presenter/produk/brand | ✅ | Ejaan betul (R15) |
| Harga / promo / CTA | Jika ada | "Tekan beg kuning", URL, WhatsApp |
| Gambar produk (PNG), logo | Jika ada | Tiada → Claude potong dari video |
| Gaya rujukan | Pilihan | "Sample 3" / "ikut cadangan Claude" |
| Tarikh siap | Pilihan | Untuk susun keutamaan |

**🤖 Claude:**
1. Muat turun semua fail → **inventori** (nama, durasi, resolusi, HDR?, ringkasan isi) + thumbnail.
2. Senaraikan apa yang **kurang/tak jelas** dan tanya sekali gus.

⛔ **G1:** semua perkara wajib ada. Jika tiada → tanya, jangan teka.

## Fasa 2 — Semak teknikal 🤖

1. `python3 -I tools/audio_check.py <video>` (R23):
   - **BERHENTI** → beritahu pengguna (angka LUFS, puncak, % senyap) dan tunggu keputusan.
   - **AMARAN** → maklumkan; teruskan hanya jika pengguna setuju.
2. Semak video: resolusi rendah (cth. < 1080p → akan lembut bila dibesarkan), HDR (tonemap), goyang/gelap.

⛔ **G2:** lulus, atau pengguna setuju teruskan walaupun ada isu.

## Fasa 3 — Analisis, transkrip & cadangan 🤖 → 🧑

> **Video bercakap/berskrip: TRANSKRIP DULU sebelum apa-apa trim atau rancang grafik (R57).**

1. **Transkrip verbatim:** `python3 -I tools/transcribe.py <video> tv.json --verbatim` (R54).
2. **Peta ucapan:** `python3 -I tools/speech_map.py tv.json <video> --keywords "<produk>,<brand>,<nama>" --md speech-map.md` →
   - **A. Senarai TRIM bernombor** — senyap, filled pause (aa/erm), filler words, ulang perkataan, ulang frasa /
     mula semula (false start), tersasul (perkataan terpotong), jeda tengah/antara ayat, perkataan tak pasti.
     **Jangan potong lagi** (R24) — pengguna pilih nombor.
   - **B. Peta peluang** setiap ayat — di mana letak **motion grafik** (angka/harga), **sticker/logo** (nama produk/brand),
     **punch-in + SFX** (perkataan emosi), **close-up** ("tengok/nampak/macam ni"), **animasi teks** (soalan),
     **CTA**, dan **titik transition / tukar visual** (pertukaran topik, jeda panjang).
   - **C. Calon hook** (ranking) → uji setiap satu dengan R56.
3. **Dengar semula** perkataan "TAK PASTI" & nama (Whisper tersilap dengar, cth. "Yana"→"enak") — R15, R54.
4. Contact sheet (setiap 0.5 s) — padankan peta peluang dengan apa yang **kelihatan** (R37), momen terbaik, ekspresi.
5. `tools/zones.py` — kesan muka & produk (R1).
6. **Bentang cadangan** ikut **Lampiran A** (resepi jenis video) — Claude cadang + sebab, pengguna pilih (R2):
   - Senarai TRIM (A) · 2–3 calon **hook** lulus R56 (lalai punchline R45) · gaya · warna highlight caption ·
     BGM (UGC bercakap lalai **tiada BGM** R55; video senyap → BGM royalty-free + link R4) · perkataan/nama tak pasti.
   - Peta peluang (B) diringkaskan; butiran penuh masuk pelan edit Fasa 4.

⛔ **G3a:** 🧑 pengguna pilih **nombor trim** + gaya, hook, warna, BGM, ejaan nama.

7. **WAJIB: selepas trim dipilih → hantar SATU PDF transkrip dalam chat untuk disemak (R58):**
   `python3 -I tools/transcript_pdf.py tv.json output/<job>/transkrip-<job>.pdf --map speech-map.json --cut <nombor> --title "<job>" --keywords "..." [--fixes fixes.json]`
   — setiap perkataan dengan saat mula, masa asal & selepas trim, bahagian dibuang bergaris merah, perkataan tak pasti
   kuning, lajur "Pembetulan". Pengguna semak & beri pembetulan → kemas kini `fixes.json` → PDF baharu jika perlu.
   Caption mesti ikut transkrip yang sudah disahkan. Satu PDF bagi setiap pusingan (versi baharu: `-v2`, `-v3`).

⛔ **G3b:** 🧑 pengguna sahkan PDF transkrip ("OK" atau senarai pembetulan). **Jangan mula Fasa 4 sebelum PDF disahkan.**

## Fasa 4 — Pelan edit + storyboard + papan layout 🤖 → 🧑

1. **Pelan edit dalam jadual** (R25): `Saat | Layout | Visual | Kenapa` — visual bertukar setiap **2–4 s**;
   isi lajur Visual/Kenapa daripada **peta peluang (B)** selepas trim yang pengguna pilih.
2. **Storyboard** (versi A untuk pengguna, dengan nota teknikal) + **papan layout** (SATU imej semua babak) (R26).
3. **Senarai transition & SFX** ikut **Lampiran D3**: setiap momen → **pilihan Claude + 2 alternatif + sebab** (kod T/S dari katalog D1/D2) (R60).
4. Ikut **Lampiran B** (spesifikasi) untuk saiz, zon & rentak. Semakan kendiri 🤖 sebelum hantar:
   - [ ] Tulisan tak tutup muka; produk sedaya upaya (R1, R1a, R1b, R13)
   - [ ] Caption 1–3 perkataan, ±54–60 px, tukar warna teks (R16, R27; X1)
   - [ ] Label sepadan dengan shot (R37); ejaan semua teks betul (X8)
   - [ ] Tiada teks dalam jalur UI bawah TikTok (> ±85% dari atas) (X6)
   - [ ] Hook lulus ujian R56; SFX jarang & bermakna (R48); tamat hitam (R12)

⛔ **G4:** 🧑 pengguna "OK" pelan (termasuk pilihan transition & SFX — boleh tukar ikut kod, cth. "#2 guna Alternatif 1"). Komen → betulkan → hantar semula. **Jangan render sebelum OK** (R29).

## Fasa 5 — Render PREVIEW + pakej klien 🤖

1. Render penuh (ffmpeg + HyperFrames); kelantangan **−13 hingga −14 LUFS** (R14).
2. **QC wajib: Lampiran C1** — semua kotak mesti ditanda sebelum preview dihantar.
3. **Pakej klien** (R22) dalam `output/<job>/`:
   - `<job>-PREVIEW-v1.mp4` — 540p, satu "PREVIEW" di tengah
   - `storyboard-klien-<k>-PREVIEW.jpg` — versi B (ringkas, tiada istilah teknikal)
4. Hantar kepada pengguna (bukan fail penuh resolusi).

⛔ **G5:** 🧑 pengguna setuju hantar kepada klien (atau minta ubah dulu → kembali ke Fasa 4/5).

## Fasa 6 — Semakan & feedback klien 🧑 ↔ 🤖

1. 🧑 Hantar pakej preview kepada klien; kumpul feedback.
2. 🧑 Bawa feedback kepada Claude (boleh salin terus mesej klien).
3. 🤖 Tukar feedback kepada **senarai pembetulan bernombor** (masa · apa · tindakan) → pengguna sahkan → betulkan →
   `<job>-PREVIEW-v2.mp4` (+ storyboard klien baharu jika babak berubah).
4. Ulang sehingga klien OK.
5. 🤖 Catat setiap round dalam `output/<job>/feedback.md` (round, tarikh, item, status).
6. Feedback yang boleh jadi peraturan umum → cadang untuk `LEARNINGS.md` (pengguna putuskan).

> Had round semakan & urusan dengan klien: **diuruskan oleh pengguna** (bukan skop SOP ini).

⛔ **G6:** 🧑 pengguna sahkan "klien OK semua".

## Fasa 7 — Render FINAL & hantar 🤖

1. Final **tanpa watermark**: 9:16 1080×1920 (atau 1920×1080 landscape), 30/60 fps, H.264 crf 18, AAC 192k,
   `+faststart`, −13 hingga −14 LUFS. Guna render penuh sedia ada jika tiada perubahan selepas preview terakhir.
2. Nama fail: `<job>-FINAL.mp4` (dua format → `<job>-FINAL-9x16.mp4`, `<job>-FINAL-16x9.mp4`).
3. **QC wajib: Lampiran C2.**
4. Hantar kepada pengguna + **teks kredit BGM** (jika guna muzik yang perlukan kredit).

## Fasa 8 — Arkib & belajar 🤖

1. **Jangan commit video job klien** ke repo (privasi; `output/` & `input/` diabaikan git).
2. Ringkasan job dalam log `LEARNINGS.md` (tarikh, job, gaya, isu, pembelajaran).
3. Jika pengguna edit sendiri versi lain → cadang `/compare-learnedit`.
4. Commit & push pengetahuan baharu ke `main` (bukan video). Desktop: 🧑 **Push** dalam GitHub Desktop.

---

## Lampiran A — Resepi ikut jenis video (lalai)

> Titik mula sahaja. Pengguna boleh ubah apa-apa di G3. Pilihan kreatif tetap dicadang + pengguna putuskan (R2).
> Semua jenis: tulisan tak tutup muka (R1), label sepadan dengan shot (R37), ejaan betul (X8), tamat hitam (R12), −13/−14 LUFS (R14).

| Jenis video | Sample rujukan | Hook lalai | Caption / teks | Audio | SFX | Transition | Struktur |
|---|---|---|---|---|---|---|---|
| **UGC bercakap (review/jual produk)** | S1, S2, S3, S6 | Punchline di 0 s (R45) + colour bars/beep jika ada punchline (R46); alternatif flash-forward (R5) / POV (R17) | Karaoke 1–3 perkataan (R16, R27) | Suara dipercepat 1.1–1.15× (R47); **tiada BGM** (R55) | Jarang, ±1 setiap 6–8 s (R48); riser pada punch-in (R49) | Hard cut + punch-in; kreatif tidak wajib (R53) | Masalah → produk → ciri/bukti → harga → CTA |
| **Faceless / tanpa suara** | S5 | Unboxing/aksi paling menarik + header nama produk | Header tetap + label/checklist ✅, tiada karaoke | **BGM royalty-free** (R4) atau SFX sahaja untuk trending sound | Pada label/checklist | Splash/kreatif sesuai produk (R21) | Unboxing → guna → manfaat → proses → hasil |
| **Review makanan** | S10 | Shot makanan paling menggoda + title soalan | Karaoke + label nama menu dekat makanan (R1b, R37) | Suara; BGM hanya jika diminta (R55) | Jarang (R48) | Hard cut | Hook → lokasi/logo → rasa (close-up) → menu lain → CTA (URL/order) |
| **Unboxing / haul** | S11 | Teaser item paling menarik (R5) | Karaoke + sticker nama produk (R52) | Suara (R55) | Jarang (R48) | Hard cut | Hook → title + logo app/kedai (R33) → item demi item (buka → tunjuk → harga → reaksi) → penutup |
| **Servis / premis** | S13 | Soalan + POV masuk pintu | Karaoke + teks skrip elegan untuk waktu & harga (R34) | **Voiceover**; BGM lembut boleh dicadang | Jarang | Hard cut | Pintu → logo → lokasi → bilik → rawatan → bukti → waktu/harga → CTA (R34) |
| **Skit + vlog shopping** | S12 | Skit masalah + teks tulisan tangan | Karaoke + logo/kempen (R33) | Suara (R55) | Jarang | POV masuk kedai sebagai peralihan | Skit → talking head → logo/kempen → kedai → produk + harga → kaunter → CTA (R35) |
| **Highlight acara** | S7–S9 | Drone/penjenama/momen VIP | Tiada karaoke; header nama acara (R38), teks dialog ≥44 px dekat penutur (R40), branding klien (R39) | **Muzik penuh** berlesen/asal (R44); suara asal boleh dimatikan | **Tiada SFX transition** (R36) | Light leak masuk montaj, dip hitam antara segmen, fade hitam akhir (R42) | **Tanya dulu:** format 9:16/landscape (R30) & bercerita/slideshow (R41); ikut aturcara (R31) |

**Hook (semua jenis):** beri 2–3 calon, setiap satu lulus ujian R56 (menarik < 3 s **dan** berkait terus dengan isi).

---

## Lampiran B — Spesifikasi teknikal standard

### Output

| Item | 9:16 (UGC/TikTok/Reels) | Landscape (YouTube/FB) |
|---|---|---|
| Resolusi | 1080×1920 | 1920×1080 |
| FPS | 30 (atau 60 jika sumber 60) | 30 |
| Video | H.264, `-crf 18 -preset slow -pix_fmt yuv420p`, `+faststart` | sama |
| Audio | AAC 192 kbps, 48 kHz | sama |
| Kelantangan | **−13 hingga −14 LUFS**, puncak ≤ −1.5 dBTP, loudnorm dua laluan (R14; X4) | sama |
| HDR (iPhone) | Tonemap ke SDR bt709 sebelum apa-apa | sama |
| Footage ≤ 720p | UGC: zoom asas 1.2× (R6); acara: frame penuh (R43) | frame penuh |
| Preview klien | 540p, satu "PREVIEW" di tengah (R22) | 540p tinggi |

### Kedudukan (9:16, % dari atas)

| Zon | Julat | Kegunaan |
|---|---|---|
| Atas | 8–20% | Header nama acara/produk (R38), title |
| Tengah | 20–70% | Biasanya muka/produk — **elak** kecuali label atas produk (R1b) |
| Caption | 60–80% | Caption karaoke; boleh atas bahagian bawah produk, jauh dari muka (R1a) |
| Branding klien | 75–80% | Teks branding kecil tetap (R39) |
| **Larangan** | **> 85%** | Jalur UI TikTok/Reels (deskripsi, butang) — **tiada teks** (X6) |
| Sisi kanan | 85–100% lebar | Butang like/komen TikTok — elak teks penting |

### Teks

| Jenis | Saiz (lebar 1080) | Gaya |
|---|---|---|
| Caption karaoke | **54–60 px**; perkataan penting 1.6–2× masa close-up | Inter ExtraBold ALL CAPS, putih + outline hitam, perkataan aktif tukar warna teks (R16, R27) |
| Teks dialog acara | **≥ 44 px** | Serif italic putih + bayang, typewriter (R40) |
| Title | 64–150 px | Skrip italic + bulat tebal, ✦ (R50); warna **kontras** dengan produk (R51) |
| Sticker produk | 34–40 px | Pill putih, teks warna tema, condong (R52) |
| **Minimum mutlak** | **≥ 40 px** | Bawah ini terlalu kecil (X1, X5, X7) |

### Rentak & bunyi

| Item | Nilai |
|---|---|
| Visual bertukar | Setiap 2–4 s (R25); montaj acara 0.6–1.5 s ikut beat |
| Jeda antara ayat | Dibuang (R11) — kecuali isian natural jika pengguna mahu (P16, menunggu) |
| Kelajuan suara (UGC) | 1.1–1.15×, pitch kekal (R47) |
| SFX | ±1 setiap 6–8 s, hanya momen penting (R48); acara: tiada (R36) |
| Ending | Hitam 0.5–0.7 s + ding (R12); acara: fade hitam (R42) |

---

## Lampiran C — QC checklist

### C1. Sebelum hantar PREVIEW (Fasa 5)

**Visual**
- [ ] Tiada tulisan menutup muka di mana-mana frame (semak snapshot setiap babak + `zones.py`) (R1)
- [ ] Produk tidak tertutup kecuali label bahagian (R1b) / caption bawah (R1a); CTA di zon selamat (R13; X2)
- [ ] Tiada teks dalam zon > 85% atau sisi kanan butang TikTok (X6)
- [ ] Visual bertukar setiap 2–4 s; tiada babak statik terlalu lama (R25)
- [ ] Tiada frame hitam/kosong/beku yang tak sengaja; transition tidak terpotong

**Teks**
- [ ] Ejaan semua title/label/caption betul (X8); nama presenter/produk/brand tepat (R15)
- [ ] Caption ikut perkataan sebenar, bukan terjemahan Whisper (R54); sync dengan suara (±0.1 s)
- [ ] Caption 1–3 perkataan, ≥ 54 px (R16, R27); semua teks ≥ 40 px (X1)
- [ ] Label sepadan dengan apa yang kelihatan dalam shot (R37)
- [ ] Animasi typewriter/pop sudah lengkap sebelum teks hilang

**Audio**
- [ ] Kelantangan −13 hingga −14 LUFS, puncak ≤ −1.5 dBTP, tiada clipping (R14)
- [ ] Ayat yang pengguna pilih untuk dibuang memang sudah dibuang; tiada potongan memotong perkataan
- [ ] SFX tidak terlalu kerap (R48) / tiada SFX transition untuk acara (R36)
- [ ] BGM (jika ada) tidak tenggelamkan suara; berlesen / muzik asal (R44)

**Struktur**
- [ ] Hook lulus ujian R56 dalam < 3 s
- [ ] CTA jelas dan betul (harga, "beg kuning", URL)
- [ ] Tamat dengan hitam (R12/R42)

**Fail**
- [ ] `<job>-PREVIEW-v<n>.mp4` 540p dengan satu "PREVIEW" di tengah; storyboard klien versi B bertanda PREVIEW (R22)

### C2. Sebelum hantar FINAL (Fasa 7)

- [ ] Semua item feedback klien dalam `feedback.md` berstatus **selesai**
- [ ] Resolusi penuh (1080×1920 / 1920×1080), fps betul, **TIADA watermark**
- [ ] Ulang semakan pantas C1 (frame awal, tengah, akhir; kelantangan; ejaan)
- [ ] Durasi sama dengan preview terakhir yang klien luluskan (kecuali pembetulan yang diminta)
- [ ] Fail boleh dimainkan dari awal hingga akhir (`ffprobe` tiada ralat; `+faststart`)
- [ ] Nama fail `<job>-FINAL.mp4` (atau `-FINAL-9x16` / `-FINAL-16x9`)
- [ ] Teks kredit BGM disertakan jika perlu

---

## Lampiran D — Katalog transition & SFX

> Dalam setiap pelan edit (Fasa 4), Claude WAJIB senaraikan **pilihan Claude + 2 alternatif** untuk setiap momen
> transition/SFX (lihat format di bawah). Pengguna boleh tukar dengan menyebut kod (cth. "T3 guna T7", "S5 buang").

### D1. Transition

| Kod | Transition | Sesuai untuk | Cara buat |
|---|---|---|---|
| T1 | **Hard cut** | Lalai UGC — pantas, bersih (R53) | ffmpeg concat |
| T2 | **Punch-in cut** (zoom 1.15–1.8× pada cut) | Penekanan, nombor, produk (R7) | crop+scale |
| T3 | **Jump cut + whoosh lembut** | Tukar topik dalam talking head | cut + `whoosh-soft` |
| T4 | **Dip to black** (0.2–0.4 s) | Antara segmen acara (R42), selepas skit | xfade `fadeblack` |
| T5 | **Crossfade** (0.3–0.5 s) | Slideshow, montaj lembut (R41) | xfade `fade` |
| T6 | **Flash putih** (2–4 frame) | Momen teruja, reveal produk | xfade `fadewhite` |
| T7 | **Whip pan / slide** | Tukar lokasi, tenaga tinggi | xfade `slideleft`/`smoothleft` |
| T8 | **Zoom blur / zoom-in transition** | Reveal, masuk close-up (S3, S4) | xfade `zoomin` / HyperFrames |
| T9 | **Light leak / flare** | Masuk montaj, mood hangat/acara (R42) | overlay light-leak (HyperFrames) |
| T10 | **Glitch RGB + B&W** | Hook VIP, lawak "rosak" (S8) | HyperFrames/CSS filter |
| T11 | **Colour bars + beep** (±1 s) | Hook interrupt selepas punchline (R46) | jana SMPTE + `beep-1khz` |
| T12 | **Paper rip / koyak kertas** | Tukar babak santai, comel (edit pengguna) | HyperFrames mask + `paper-rip` |
| T13 | **Splash cecair** | Produk buih/cecair (S3, S5) | HyperFrames mask |
| T14 | **Kad foto berpusing** + bintang/reben | Selepas hook, feminin/rumah (S6) | HyperFrames |
| T15 | **Brush stroke** | Aesthetic, lifestyle (S6) | HyperFrames mask |
| T16 | **Film strip / bingkai foto / kolaj** | Highlight acara, nostalgia (S7) | HyperFrames |
| T17 | **Ken Burns** (≤5%) | Gambar statik / slideshow (R41) | zoompan |
| T18 | **POV masuk pintu / berjalan** | Lawatan premis/kedai (R34, R35) | footage sebenar |

Prinsip: **R21** (mesti sesuai dengan video, tidak rigid) · **R53** (transition kreatif tidak wajib) ·
UGC: hard cut dominan, 0–1 transition kreatif · Acara: lebih banyak dibenarkan (R31), tiada SFX transition (R36).

### D2. Sound effect (pustaka `tools/sfx/`)

| Kod | Fail | Bunyi | Sesuai untuk |
|---|---|---|---|
| S1 | `whoosh-soft.wav` | Whoosh lembut | Tukar visual penting, masuk grafik |
| S2 | `whoosh.wav` | Whoosh kuat | Hook flash-forward, transition laju |
| S3 | `pop.wav` | Pop pendek | Label/sticker/pill muncul, angka/harga |
| S4 | `ding.wav` | Ding | Checklist ✅, poin penting, ding penutup (R12) |
| S5 | `chime.wav` | Chime dua nada | Hadiah, reveal lembut |
| S6 | `sparkle.wav` | Sparkle/magic | Title cute, produk kecantikan, reveal |
| S7 | `riser.wav` | Riser naik | Punch-in penekanan, sebelum reveal (R49) |
| S8 | `boing.wav` | Boing | Lawak, reaksi terkejut (R49) |
| S9 | `impact.wav` | Impact/boom | Badge "HARGA TURUN!", punchline kuat |
| S10 | `beep-1khz.wav` | Beep 1 kHz | Colour bars hook interrupt (R46) |
| S11 | `click.wav` | Klik | Kursor/search-bar (R18), typewriter |
| S12 | `paper-rip.wav` | Koyak kertas | Transition paper rip (T12) |
| S13 | `tinggg.wav` | Loceng nyaring "Tinggg!!" (C7, dengung ±1 s) | Penutup ganti ding (job herba-headspa); beri hitam ±0.9 s |

Prinsip: **R48** — SFX jarang & bermakna (±1 setiap 6–8 s), tiada whoosh pada setiap cut · Acara: tiada SFX transition (R36).
SFX disintesis sendiri (asas). Jika pengguna ada pustaka SFX berlesen, letak dalam `tools/sfx/` dan tambah dalam jadual ini.

### D3. Format wajib dalam pelan edit (Fasa 4)

| # | Masa | Momen | **Pilihan Claude** | Alternatif 1 | Alternatif 2 | Kenapa pilihan Claude |
|---|---|---|---|---|---|---|
| 1 | 0.0 s | Hook punchline → colour bars | T11 + S10 | T6 + S9 | T1 (tiada) | Punchline harga mengejutkan (R46) |
| 2 | 5.1 s | Sebut "saiz 16" | T2 + S3 | T8 + S7 | T1 + S3 | Tunjuk saiz dekat (R7) |
| … | | | | | | |

Ringkasan akhir: jumlah transition kreatif & jumlah SFX (semak R48: ±1 SFX / 6–8 s).

---

## Destinasi output (WAJIB)

**Semua output dihantar terus dalam chat** (SendUserFile): storyboard, papan layout, PDF transkrip, preview, final.
Salinan tempatan kekal dalam `output/<job>/` (tidak masuk git). **Tiada muat naik ke Google Drive** (R59, dikemas kini
2026-11-13 — connector Drive tak boleh muat naik video besar).

## Struktur folder job

```
input/<job>/          ← bahan raw (desktop) — tidak masuk git
output/<job>/         ← tidak masuk git
  storyboard-<k>.jpg              (A — pengguna)
  papan-layout.jpg
  storyboard-klien-<k>-PREVIEW.jpg (B — klien)
  <job>-PREVIEW-v<n>.mp4
  <job>-FINAL.mp4
  feedback.md
```

## Arahan pantas (skill)

| Arahan | Bila |
|---|---|
| `/edit-video <link>` | Job baharu (Fasa 0–8) |
| `/sample-baru <link>` | Belajar gaya dari video siap edit orang lain |
| `/compare-learnedit <link>` | Banding edit pengguna sendiri vs Claude, belajar |
