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
| 3 | Analisis, transkrip & cadangan | ⛔ G3: pengguna pilih gaya, hook, warna, BGM, ayat dibuang |
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

1. Contact sheet (setiap 0.5 s) — fahami isi, momen terbaik, produk, ekspresi.
2. Transkrip **verbatim** (`tools/transcribe.py --verbatim`, R54) → `tools/stutter.py` → **senarai bernombor** ayat
   tersangkut/ulang/isian/jeda/tak pasti. **Jangan potong lagi** (R24).
3. `tools/zones.py` — kesan muka & produk (R1).
4. **Bentang cadangan** (Claude cadang + sebab, pengguna pilih — R2):
   - Gaya (Sample mana / gabungan) · **Hook** (lulus ujian hook R56; lalai punchline R45) · warna highlight caption ·
     BGM (UGC bercakap lalai **tiada BGM** R55; video senyap → BGM royalty-free + link R4) · perkataan/nama tak pasti.

⛔ **G3:** 🧑 pengguna jawab: gaya, hook, warna, BGM, **nombor ayat yang dibuang**, ejaan nama.

## Fasa 4 — Pelan edit + storyboard + papan layout 🤖 → 🧑

1. **Pelan edit dalam jadual** (R25): `Saat | Layout | Visual | Kenapa` — visual bertukar setiap **2–4 s**.
2. **Storyboard** (versi A untuk pengguna, dengan nota teknikal) + **papan layout** (SATU imej semua babak) (R26).
3. Semakan kendiri 🤖 sebelum hantar:
   - [ ] Tulisan tak tutup muka; produk sedaya upaya (R1, R1a, R1b, R13)
   - [ ] Caption 1–3 perkataan, ±54–60 px, tukar warna teks (R16, R27; X1)
   - [ ] Label sepadan dengan shot (R37); ejaan semua teks betul (X8)
   - [ ] Tiada teks dalam jalur UI bawah TikTok (> ±85% dari atas) (X6)
   - [ ] Hook lulus ujian R56; SFX jarang & bermakna (R48); tamat hitam (R12)

⛔ **G4:** 🧑 pengguna "OK" pelan. Komen → betulkan → hantar semula. **Jangan render sebelum OK** (R29).

## Fasa 5 — Render PREVIEW + pakej klien 🤖

1. Render penuh (ffmpeg + HyperFrames); kelantangan **−13 hingga −14 LUFS** (R14).
2. Semak dalaman: snapshot beberapa frame, sync caption, bunyi.
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

> **Had round semakan:** _(belum ditetapkan — pengguna tentukan, cth. 2 round termasuk dalam harga)_

⛔ **G6:** 🧑 pengguna sahkan "klien OK semua".

## Fasa 7 — Render FINAL & hantar 🤖

1. Final **tanpa watermark**: 9:16 1080×1920 (atau 1920×1080 landscape), 30/60 fps, H.264 crf 18, AAC 192k,
   `+faststart`, −13 hingga −14 LUFS. Guna render penuh sedia ada jika tiada perubahan selepas preview terakhir.
2. Nama fail: `<job>-FINAL.mp4` (dua format → `<job>-FINAL-9x16.mp4`, `<job>-FINAL-16x9.mp4`).
3. Semakan akhir: tonton frame awal/tengah/akhir, kelantangan, tiada watermark, ejaan.
4. Hantar kepada pengguna + **teks kredit BGM** (jika guna muzik yang perlukan kredit).

## Fasa 8 — Arkib & belajar 🤖

1. **Jangan commit video job klien** ke repo (privasi; `output/` & `input/` diabaikan git).
2. Ringkasan job dalam log `LEARNINGS.md` (tarikh, job, gaya, isu, pembelajaran).
3. Jika pengguna edit sendiri versi lain → cadang `/compare-learnedit`.
4. Commit & push pengetahuan baharu ke `main` (bukan video). Desktop: 🧑 **Push** dalam GitHub Desktop.

---

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
