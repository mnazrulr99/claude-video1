# Pembelajaran Berterusan (Continuous Learning)

Fail ini ialah **ingatan pembelajaran** Claude untuk editing video pengguna. Ia dikemas kini oleh:
- `/compare-learnedit` — bila pengguna beri video yang **dia edit sendiri** untuk dibanding & dipelajari;
- `/edit-video` — maklum balas pengguna selepas setiap job (storyboard & video siap);
- `/sample-baru` — pattern baharu daripada sample siap edit.

**Peraturan penggunaan:**
1. `/edit-video` **WAJIB** baca fail ini pada Langkah 0 dan ikut semua **Peraturan Diterima**.
2. **Jangan sekali-kali** guna apa-apa dalam **Ditolak** (walaupun ada dalam sample lama).
3. Jika peraturan bercanggah, yang **lebih baharu** menang; "Catatan citarasa pengguna" dalam `README.md` dan arahan terus pengguna mengatasi semua.
4. Claude **cadang** klasifikasi (boleh belajar / jangan belajar); **pengguna buat keputusan akhir**. Hanya simpan selepas pengguna sahkan.

---

## ✅ Peraturan Diterima (ikut dalam setiap edit)

| ID | Peraturan | Kategori | Sumber | Tarikh |
|---|---|---|---|---|
| R1 | Tulisan (caption, title, badge, label, CTA) **tidak boleh tutup muka**; sedaya upaya **tidak tutup produk**. Letak di ruang kosong; kecilkan tulisan jika perlu. **Pengecualian (R1a, R1b).** | Kedudukan teks | Maklum balas job ujian periuk (badge "HARGA TURUN!" tutup muka) | 2026-11-07 |
| R1a | **Caption boleh diletak atas bahagian BAWAH produk** (cth. ±72–80% dari atas), tetapi **tidak boleh tutup muka**. | Kedudukan teks | /compare-learnedit periuk (item 4) | 2026-11-07 |
| R1b | **Label yang menamakan bahagian produk** (cth. "16CM" pada periuk 16 cm) boleh diletak **terus atas bahagian itu**, muncul ikut masa disebut. | Kedudukan teks | /compare-learnedit periuk (item 3) | 2026-11-07 |
| R2 | Pilihan kreatif (gaya, hook, warna caption, BGM): Claude cadang + sebab, pengguna putuskan. | Proses | Arahan pengguna | 2026-11-07 |
| R3 | Storyboard imej dahulu; render hanya selepas pengguna setuju. | Proses | Arahan pengguna | 2026-11-07 |
| R4 | Video tanpa suara: BGM royalty-free; jika tiada yang sesuai → SFX sahaja (pengguna tambah trending sound di TikTok). | Audio | Arahan pengguna | 2026-11-07 |
| R5 | **(Lalai diganti oleh R45 — kekal sebagai alternatif)** **Hook B**: klip ±1 s momen paling menarik (flash-forward, cth. demo produk) dengan audio dimatikan + whoosh, kemudian cut ke awal video. (Masih cadang alternatif jika jenis video lain.) | Hook | /compare-learnedit periuk (item 1) | 2026-11-07 |
| R6 | **(UGC; acara ≤720p lihat R43)** **Framing asas lebih ketat (±1.2× crop)** supaya muka & produk penuhkan skrin; elak ruang kosong (meja/lantai) yang banyak. Punch-in tambahan di atas itu. | Framing | /compare-learnedit periuk (item 2) | 2026-11-07 |
| R7 | **Punch-in ekstrem pada produk** bila menyebut butiran fizikal (saiz/bahagian), digabung dengan label R1b. | Framing | /compare-learnedit periuk (item 3) | 2026-11-07 |
| R8 | **(Diperhalusi oleh R50/R51)** **Font & warna title ikut produk/mood** (cth. produk pink → font bulat/bubbly pink, outline putih, doodle hati). | Title | /compare-learnedit periuk (item 6) | 2026-11-07 |
| R9 | **Callout dengan doodle sparkle** (garis kecil ✦ di tepi pill) dan diletak **dekat benda yang disebut** (tertakluk R1). Teks pendek boleh condong sedikit. | Grafik | /compare-learnedit periuk (item 7) | 2026-11-07 |
| R10 | **(Diperhalusi oleh R53 — transition kreatif kini pilihan, bukan wajib)** **(UGC)** **Satu transition kreatif di pertengahan video** (cth. paper-rip/koyak kertas + strip B&W + bunyi koyak); selebihnya hard cut. | Transition | /compare-learnedit periuk (item 9) | 2026-11-07 |
| R11 | **Potongan jeda lebih ketat** — buang semua ruang antara ayat (sasaran: rentak sepadat edit pengguna, ±45 s untuk raw 56 s). | Rentak | /compare-learnedit periuk (item 10) | 2026-11-07 |
| R12 | **Tamat dengan skrin hitam** (±0.5–0.7 s) + ding penutup. | Ending | /compare-learnedit periuk (item 11) | 2026-11-07 |
| R13 | **CTA diletak di zon selamat** (tidak tutup muka/produk), cth. pill dengan ikon beg. | CTA | /compare-learnedit periuk (item 12) | 2026-11-07 |
| R14 | **Kelantangan akhir −13 hingga −14 LUFS** (guna loudnorm dua laluan supaya tepat). | Audio | /compare-learnedit periuk (item 13) | 2026-11-07 |
| R15 | **Nama presenter:** bila presenter sebut nama sendiri, tanya/sahkan nama dan tulis dalam caption (cth. **"Yana"**, bukan "akak"). Whisper sering salah dengar nama. | Transkrip | /compare-learnedit periuk (item 14) | 2026-11-07 |
| R16 | **(Saiz diganti oleh R62: ±48 px, geser kiri)** **Gaya caption = versi Claude:** word-by-word ALL CAPS, font tebal (Inter ExtraBold) **±54–60 px** pada 1080 lebar, putih + outline hitam tebal, perkataan aktif **tukar warna teks** (bukan kotak highlight; warna dicadang ikut R2, cth. kuning). Kedudukan ikut R1/R1a. | Caption | /compare-learnedit periuk (item 5: "ikut versi Claude") | 2026-11-07 |
| R17 | **Hook alternatif: POV skit** — teks "Pov: …" gaya TikTok (putih kecil, atas) + aksi presenter tanpa/kurang dialog. Cadang bersama Hook B (R5); pengguna pilih ikut video. | Hook | Sample 6 (P1) | 2026-11-07 |
| R18 | **Label gaya search bar** (pill putih + kursor menaip + ikon ×, teks bertukar berturut) untuk senarai pilihan/lokasi/kegunaan. | Grafik | Sample 6 (P2) | 2026-11-07 |
| R19 | **Label tulisan tangan + sparkle ✦** untuk harga, ciri (✅) dan nama varian **di sebelah produk** (R1b). Warna ikut tema. | Grafik | Sample 6 (P3) | 2026-11-07 |
| R20 | **Satu momen lawak: klip B&W reaksi** (presenter berlakon reaksi orang lain) bila skrip ada punchline. | Effect | Sample 6 (P4) | 2026-11-07 |
| R21 | **Transition kreatif mesti sesuai dengan video** (mood, produk, tema warna) dan **tidak rigid** — contoh dalam sample (kad foto + bintang/reben, paper-rip, splash cecair, brush stroke) hanyalah **alternatif/inspirasi**; Claude bebas guna **kreativiti sendiri** untuk cipta transition yang paling kena. Satu-dua sahaja (R10); terangkan sebab dalam storyboard. | Transition | Sample 6 (P5) + arahan pengguna | 2026-11-07 |
| R22 | **Preview klien sebelum final:** selepas render, beri pengguna **storyboard + video preview 540p dengan SATU watermark "PREVIEW" di tengah** (tiada jalur atas, tiada corak berulang) (`tools/client_preview.py`, juga `--image` untuk storyboard). Storyboard **dua versi**: **A** untuk pengguna (nota teknikal), **B** untuk klien (ringkas, tanpa istilah teknikal, bertanda PREVIEW) — kedua-dua guna frame sebenar dari render. Final render tanpa watermark **hanya selepas klien setuju**. Nama fail: `<job>-PREVIEW-v<n>.mp4`, `<job>-FINAL.mp4`. | Proses | Arahan pengguna | 2026-11-08 |
| R23 | **Semak audio dahulu** (`tools/audio_check.py`) sebelum apa-apa edit. Jika **BERHENTI** (terlalu perlahan < −35 LUFS / puncak < −20 dBFS, atau > 60% senyap, atau tiada audio) → **berhenti dan beritahu pengguna**. AMARAN → maklumkan, teruskan hanya jika pengguna setuju. | Audio | Idea pengguna | 2026-11-09 |
| R24 | **Transkrip + tandakan ayat tersangkut/diulang** (`tools/transcribe.py --verbatim` → `tools/stutter.py`): ulang perkataan, ulang frasa/cuba semula, isian (erm/aa), jeda tengah ayat, perkataan tak pasti. **JANGAN potong dulu** — tunjuk senarai bernombor, pengguna pilih yang dibuang. (Transkrip biasa untuk caption; verbatim untuk semakan sangkut.) | Transkrip | Idea pengguna | 2026-11-09 |
| R25 | **Pelan edit dalam jadual**: lajur **Saat · Layout · Visual · Kenapa**. **Visual bertukar setiap 2–4 saat** (punch-in, sudut, close-up produk, B-roll, grafik). | Perancangan | Idea pengguna | 2026-11-09 |
| R26 | **Papan layout (layout board)** sebelum render: lukis **semua layout dalam SATU papan imej** (semua babak) untuk kelulusan pengguna. Render hanya selepas diluluskan. | Proses | Idea pengguna | 2026-11-09 |
| R27 | **Subtitle 1–3 perkataan** sahaja setiap paparan. **Perkataan penting dibesarkan semasa close-up** (cth. 1.6–2× saiz, warna highlight). | Caption | Idea pengguna | 2026-11-09 |
| R28 | **(DIGANTI oleh R48 — jangan whoosh setiap tukar visual)** **(UGC; untuk acara lihat R36)** **SFX: whoosh LEMBUT** (`tools/sfx/whoosh-soft.wav`, puncak −12 dB) setiap kali visual bertukar. Bunyi lain (ding, pop, sparkle, dll.) **dibenarkan** ikut kesesuaian video. | SFX | Idea pengguna (larangan bunyi magic/dramatik dibuang 2026-11-09) | 2026-11-09 |
| R29 | **Aliran kelulusan (menggantikan susunan dalam R3/R22):** (1) selepas pelan edit → beri **storyboard + papan layout** (sebelum render) → (2) pengguna OK → **render PREVIEW** (540p + satu "PREVIEW" di tengah) + storyboard klien (B) → (3) pengguna bawa kepada klien → feedback → ulang preview → (4) klien OK semua → **render FINAL** (1080×1920 tanpa watermark). Jangan langkau mana-mana pintu kelulusan. | Proses | Arahan pengguna | 2026-11-09 |
| R30 | **Kategori "Highlight Acara"**: **WAJIB tanya pengguna dulu — landscape (1920×1080) atau 9:16 (1080×1920)** (atau kedua-dua). Tiada caption bila tiada suara; logo acara tetap kecil (ikut R1); montaj ±0.5–1.5 s ikut beat BGM. | Format | Sample 7–9 (P6) + arahan pengguna | 2026-11-10 |
| R31 | Highlight acara: **susun babak ikut aturcara acara** (pembuka drone/penjenama → aktiviti → klimaks → penutup); **boleh guna lebih banyak transition kreatif** (ikut R21). R10 (satu transition di tengah) hanya untuk UGC. | Struktur | Sample 7–9 (P7) | 2026-11-10 |
| R32 | **Siri video dari satu acara** guna identiti sama (logo, warna, keluarga BGM) supaya konsisten. | Konsistensi | Sample 7–9 (P8) | 2026-11-10 |
| R33 | **Logo kedai/app + label kempen** (cth. logo + "BACK TO SCHOOL") pop sekali bila brand disebut (ikut R1). | Grafik | Sample 11–13 (P12) | 2026-11-10 |
| R34 | **Genre servis/premis:** voiceover + B-roll lawatan (POV masuk pintu → logo → lokasi/landmark → bilik → rawatan sebenar → bukti: scan/sebelum-selepas/testimoni) → waktu operasi & harga promo dalam **teks skrip elegan** → CTA. | Struktur | Sample 13 (P13) | 2026-11-10 |
| R35 | **Genre skit + vlog shopping:** hook skit masalah (keluarga) + teks tulisan tangan → talking head masalah → logo/kempen → POV masuk kedai → produk + tag harga → kaunter → talking head CTA. | Struktur | Sample 12 (P14) | 2026-11-10 |
| R36 | **Highlight acara: tiada SFX transition** (whoosh/ding) — muzik dominan. R28 (whoosh setiap tukar visual) kini untuk **UGC sahaja**. | SFX | Maklum balas job raya + edit pengguna raya + Sample 7–9 | 2026-11-10 |
| R37 | **Label/caption yang menamakan benda (makanan, produk, lokasi) MESTI sepadan dengan apa yang kelihatan dalam shot itu.** Tiada shot sepadan → jangan namakan (guna label umum, cth. "MENU RAYA"). Semak setiap label dengan frame sebenar sebelum storyboard. | Caption/Grafik | Maklum balas job raya ("makanan tak selari dengan gambar") | 2026-11-10 |
| R38 | **Header tetap nama acara** di bahagian atas (zon siling/kosong, ±8–20% dari atas) **sepanjang video**; muncul perkataan demi perkataan di awal; font serif bubbly/retro warna mesra tema (cth. krim-pic) + outline gelap + bayang; hiasan ★ kecil di kiri-kanan. **Sahkan nama acara dengan klien** (cth. "Majlis Sambutan Aidilfitri", bukan teka). | Title | Edit pengguna raya | 2026-11-10 |
| R39 | **Branding klien kecil tetap** (cth. "Emcee Hafiz" — bila video ialah promosi servis klien): serif italic putih + bayang, tengah bawah, sepanjang video — **dalam zon selamat (±75–80% dari atas), bukan di jalur UI bawah TikTok/Reels**. Tanya nama/brand klien. | Grafik | Edit pengguna raya (kedudukan dilaraskan, lihat X6) | 2026-11-10 |
| R40 | **Highlight acara dengan pengacara:** suara asal boleh dimatikan, muzik penuh; isi percakapan penting disampaikan sebagai **teks dialog ayat pendek** (1–3 baris, cth. soalan game, ucapan terima kasih) **dekat penutur** (tak tutup muka, R1), muncul **typewriter**, serif italic putih + bayang, **saiz ≥ 44 px** pada lebar 1080 (X1, X5). Format ini menggantikan caption karaoke (R16/R27) untuk video acara bermuzik. | Caption | Edit pengguna raya | 2026-11-10 |
| R41 | **Tanya format highlight acara dulu:** (a) **highlight bercerita** — take 5–10 s untuk momen interaksi (pengacara, game, tetamu) + montaj B-roll laju ±0.6–1 s (makanan/hiasan); atau (b) **slideshow** — ±2 s/slide, crossfade lembut 0.4 s, Ken Burns ≤5%, tiada pop-up. (Job raya: slide 3.8 s "terlalu lama"; 2 s diterima.) | Rentak | Edit pengguna raya + maklum balas job raya | 2026-11-10 |
| R42 | **Transition highlight acara:** light leak/flare untuk masuk segmen montaj, **dip ke hitam** antara segmen, hard cut selebihnya, **fade ke hitam** di hujung (menguatkan R31). | Transition | Edit pengguna raya + Sample 7–9 | 2026-11-10 |
| R43 | **Footage acara ≤ 720p: kekal frame penuh** (tiada zoom asas 1.2×; R6 untuk UGC) supaya gambar tajam dan suasana/tetamu nampak. Punch-in hanya sekali-sekala jika perlu. | Framing | Edit pengguna raya | 2026-11-10 |
| R44 | **BGM bertema (cth. lagu raya):** lagu popular berhak cipta — jangan guna/reupload "No Copyright" YouTube tanpa lesen jelas. Pilihan: (a) pengguna sediakan fail berlesen (Pixabay, beli lesen), (b) **muzik asal Claude** (`tools/music_raya.py`, tiada kredit), (c) plugin AI muzik. **Potongan/tukar slide tepat pada beat/bar** muzik. | Audio | Job raya | 2026-11-10 |

| R45 | **Hook lalai (UGC bercakap) = ayat paling kuat/punchline terus di 0 s** — buang mukadimah ("Korang tahu kan…"); mula dengan kenyataan yang mengejutkan/emosi (cth. "Rejuran ni bapak mahal."). R5 (flash-forward) & R17 (POV) kekal sebagai alternatif. | Hook | /compare-learnedit Rejuran (item 1: pengguna tak suka hook flash-forward) | 2026-11-12 |
| R46 | **Hook interrupt: colour bars (SMPTE) + beep 1 kHz ±1 s** sejurus selepas punchline hook (lawak "siaran rosak" kerana terkejut harga/fakta), kemudian sambung video. Guna bila hook ada punchline. | Hook | /compare-learnedit Rejuran (item 2) + Sample 2 | 2026-11-12 |
| R47 | **(Kini PILIHAN sahaja — lalai diganti oleh R61)** **Percepat suara 1.1–1.15×** (pitch kekal, `atempo`) untuk talking-head UGC supaya rentak bertenaga; digabung dengan potongan jeda ketat (R11). | Rentak | /compare-learnedit Rejuran (item 3: edit pengguna 1.14×) | 2026-11-12 |
| R48 | **(Diperhalusi oleh R65/R66)** **SFX jarang & bermakna (menggantikan R28):** hanya pada grafik/momen penting (title, punch-in penekanan, label/sticker, CTA, ending) — sasaran ±1 SFX setiap 6–8 s (±7 untuk 50 s). **Tiada whoosh pada setiap cut.** | SFX | /compare-learnedit Rejuran (item 4) | 2026-11-12 |
| R49 | **Riser/boing naik** pada punch-in penekanan (cth. zoom ke pori/kulit masa "nampak tak?"). | SFX | /compare-learnedit Rejuran (item 5) | 2026-11-12 |
| R50 | **Gaya title "cute aesthetic":** gabung **skrip italic elegan** (cth. "Berbaloi", "worth it!") + **tulisan bulat tebal** (cth. "Set Rejuran", "duit korang"), hiasan bintang ✦/sparkle, animasi tulis/typewriter; diletak dekat muka (paras bahu/dada, tak tutup muka — R1). | Title | /compare-learnedit Rejuran (item 6) | 2026-11-12 |
| R51 | **Warna grafik mesti KONTRAS dengan produk** (cth. produk lavender → grafik pink/putih), bukan sama warna produk (tenggelam). Memperhalusi R8. | Title/Grafik | /compare-learnedit Rejuran (item 7) | 2026-11-12 |
| R52 | **Sticker nama produk = pill putih kecil, teks warna tema (pink), sedikit condong**, muncul dekat produk masa disebut (R1b), cth. "Toner", "cleansing balm", "ampoule". | Grafik | /compare-learnedit Rejuran (item 8) | 2026-11-12 |
| R53 | **Transition kreatif tidak wajib** — hard cut + punch-in pada momen penting sudah memadai; hook interrupt (R46) boleh jadi satu-satunya "effect". Memperhalusi R10/R21. | Transition | /compare-learnedit Rejuran (item 9) | 2026-11-12 |
| R54 | **Transkrip mesti ikut perkataan SEBENAR:** Whisper `--lang ms` menterjemah slang/English ke BM baku (cth. "worth it"→"berbaloi", "korang"→"anda", "Yana dah"→"yang nak"). Guna transkrip **verbatim** sebagai asas caption, semak dengan telinga/potongan audio, dan betulkan sebelum storyboard. | Transkrip | /compare-learnedit Rejuran (item 11) | 2026-11-12 |
| R56 | **Ujian hook (WAJIB untuk setiap hook):** hook mesti (a) **sangat menarik** — menimbulkan rasa ingin tahu/terkejut/lawak dalam < 3 s, dan (b) **berkait terus dengan isi/janji video** (masalah utama, harga, hasil, punchline). Tujuan hook = buat orang **berhenti scroll dan terus tengok**. Visual cantik tanpa makna (cth. buka kotak tanpa konteks) **tidak lulus**. Dalam cadangan gaya, beri 2–3 calon hook + sebab setiap satu lulus (a) & (b). | Hook | Arahan pengguna (Rejuran) | 2026-11-12 |
| R55 | **UGC bercakap ke kamera: lalai TIADA BGM** — suara + SFX jarang (R48) sahaja; BGM hanya jika pengguna minta. | Audio | /compare-learnedit Rejuran (item 10) + pilihan pengguna | 2026-11-12 |
| R57 | **Video bercakap/berskrip: transkrip dulu** (verbatim) dan jana **peta ucapan** (`tools/speech_map.py`) **sebelum trim atau rancang grafik**: (A) senarai trim — senyap, tersasul, ulang, filler words, filled pauses, disfluency lain (pengguna pilih, R24); (B) peta peluang — di mana letak motion grafik, animasi, SFX, transition; (C) calon hook (uji R56). Pelan edit (R25) dibina daripada peta ini. | Proses | Arahan pengguna | 2026-11-13 |
| R58 | **PDF transkrip untuk semakan** selepas trim dipilih (`tools/transcript_pdf.py`): setiap perkataan + saat mula, masa asal & selepas trim, trim bergaris merah, tak pasti kuning, nama biru, pembetulan hijau, lajur "Pembetulan". Caption guna transkrip yang disahkan pengguna. | Transkrip | Arahan pengguna | 2026-11-13 |
| R59 | **Semua output dihantar dalam chat** (SendUserFile) — tiada muat naik ke Google Drive. (Asalnya: muat naik ke folder Drive; dibatalkan 2026-11-13 kerana connector tak boleh muat naik video besar.) | Penghantaran | Arahan pengguna | 2026-11-13 |
| R60 | **Pemilihan transition & SFX:** dalam pelan edit, senaraikan setiap momen dengan **pilihan Claude + 2 alternatif + sebab**, guna kod katalog (SOP Lampiran D: T1–T18, S1–S12). Pengguna pilih/tukar ikut kod. | Transition/SFX | Arahan pengguna | 2026-11-13 |
| R61 | **Suara ASAL secara lalai** (UGC bercakap): **tiada pengurangan bising & tiada percepat** — hanya potong (trim) + kelantangan −13/−14 LUFS. Denoise/1.1× (R47) hanya jika pengguna minta. | Audio/Rentak | /compare-learnedit herba-headspa (item 1) + maklum balas preview v1 | 2026-11-13 |
| R62 | **Caption zon selamat TikTok:** Inter ExtraBold ALL CAPS **±48 px** (perkataan penting 1.5–2×), **tengah caption digeser ke kiri (cx ≈ 480)** dan lebar baris maks ±820 px supaya teks tak melepasi **x ≈ 900** (butang like/komen/share di kanan). Menggantikan saiz 54–60 px dalam R16. | Caption | /compare-learnedit herba-headspa (item 1) + maklum balas v4 | 2026-11-13 |
| R63 | **Callout/pill/label muncul TEPAT pada masa perkataannya keluar dalam subtitle** (cth. pill "Kulit ✓" pada saat caption "KULIT"), bukan selang masa tetap. | Grafik | /compare-learnedit herba-headspa (item 1) + maklum balas v4 | 2026-11-13 |
| R64 | **Filter warna ringan sahaja** — maksimum ±separuh tahap edit herba (kontras ≈ +2, saturasi ≈ +2 pada skala 0–255, sedikit hangat). Filter kuat ditolak klien ("kurangkan filter"). | Warna | /compare-learnedit herba-headspa (item 2) | 2026-11-13 |
| R65 | **Tempat SFX = title utama + penutup sahaja** (cth. chime/sparkle menaik pada title utama, loceng "ting" di skrin hitam penutup) — ±2 SFX bagi ±24 s. Memperhalusi R48. | SFX | /compare-learnedit herba-headspa (item 4) | 2026-11-13 |
| R66 | **Claude hantar video BERSIH (tanpa SFX & tanpa BGM dibakar)** + **jadual masa** momen untuk SFX (ikut R65) — pengguna tambah SFX/BGM sendiri dalam app. Claude masukkan SFX/BGM hanya jika diminta. | Proses/Audio | /compare-learnedit herba-headspa (item 6) | 2026-11-13 |
| R67 | **Video kenangan / travel / pemandangan:** di G1 **tanya klien foto/video diri mereka** (orang dalam frame = "kenangan"). Footage pemandangan sahaja terasa seperti video stok. | Bahan/Proses | /compare-learnedit kenangan-airterjun (item 1: klien minta tambah gambar) | 2026-11-14 |
| R68 | **Susunan foto klien = bookend bercerita:** kumpulan 1 selepas shot "sampai/pengunjung" (±⅓ video), kumpulan 2 sebelum shot penutup. | Struktur | /compare-learnedit kenangan-airterjun (item 2) | 2026-11-14 |
| R69 | **Foto dalam video:** ±2 s setiap foto + zoom perlahan (Ken Burns ≤5%), 2–3 foto setiap kumpulan (selaras R41). | Rentak | /compare-learnedit kenangan-airterjun (item 3) | 2026-11-14 |
| R70 | **Light leak / flare HANYA untuk masuk & keluar kumpulan foto orang** (tanda peralihan pemandangan → momen peribadi). Babak pemandangan lain: crossfade biasa. | Transition | /compare-learnedit kenangan-airterjun (item 4, 5) | 2026-11-14 |
| R71 | **Video pemandangan tanpa suara + pengguna tambah BGM:** kekalkan bunyi alam asal tetapi **diperlahankan ±−26 LUFS** (−12 dB dari −14) supaya BGM duduk di atas; hasil akhir pengguna −13.2 LUFS (lulus R14). | Audio | /compare-learnedit kenangan-airterjun (item 6) | 2026-11-14 |

## ❌ Ditolak (JANGAN belajar / jangan guna)

| ID | Perkara | Sebab | Sumber | Tarikh |
|---|---|---|---|---|
| X1 | Caption terlalu kecil (sukar dibaca di telefon) | Kebolehbacaan | /compare-learnedit periuk (item 5) | 2026-11-07 |
| X2 | CTA / teks besar yang **menutup produk** (cth. teks skrip "Tengok dekat beg kuning" atas periuk) | Bercanggah R1 | /compare-learnedit periuk (item 12) | 2026-11-07 |
| X4 | Kelantangan **−7.3 LUFS** (terlalu kuat; platform akan normalisasi & bunyi pecah) | Bercanggah R14 | /compare-learnedit raya | 2026-11-10 |
| X5 | Teks dialog/caption **±30 px** pada lebar 1080 (terlalu kecil di telefon) — konsep R40 diterima, saiz ini tidak | Kebolehbacaan (X1) | /compare-learnedit raya | 2026-11-10 |
| X7 | Caption **±30 px 2 baris** (edit Rejuran) dan kelantangan **−8.9 LUFS / puncak +0.6 dBFS** — mengulangi X5 & X4 | Kebolehbacaan / clipping | /compare-learnedit Rejuran (item 12, 14) | 2026-11-12 |
| X8 | Typo dalam title (cth. "lebih hygine!") — semak ejaan setiap teks grafik | Kualiti | /compare-learnedit Rejuran (item 15) | 2026-11-12 |
| X6 | Branding/teks tetap di **±89% dari atas** (jalur UI bawah TikTok/Reels — tertutup deskripsi & butang) | Zon selamat | /compare-learnedit raya | 2026-11-10 |
| X9 | Kelantangan **−6.3 LUFS / puncak +1.8 dBFS** (edit herba-headspa) — clipping, mengulangi X4/X7 | Bercanggah R14 | /compare-learnedit herba-headspa (item 5) | 2026-11-13 |
| X10 | **Light leak terlalu kerap** (±9 dalam 58 s, termasuk babak pemandangan biasa) dan **tint pink-cyan** yang menukar warna air terjun — hadkan ikut R70 | Rentak visual / warna | /compare-learnedit kenangan-airterjun (item 5) | 2026-11-14 |
| X11 | **Eksport HEVC 60 fps** sebagai standard — sesetengah phone/PC lama & WhatsApp Web tak boleh main; standard Claude kekal H.264 30 fps | Keserasian | /compare-learnedit kenangan-airterjun (item 7) | 2026-11-14 |

## 📝 Nota (bukan peraturan)

- **Kreativiti Claude digalakkan:** gaya dalam Sample 1–6 ialah rujukan, bukan templat tegar. Selagi Peraturan Diterima (terutama R1, R13, R16, R21) dipatuhi, Claude boleh cadang idea grafik/transition/effect baharu yang sesuai dengan video — tunjuk dalam storyboard untuk keputusan pengguna (R2/R3).

- **Jumlah grafik fleksibel** — pengguna suka dua-dua (±5 grafik/45 s atau ±9 grafik/52 s). Claude tentukan ikut kandungan dan tunjuk dalam storyboard. (/compare-learnedit periuk item 8)
- **Presenter dikenali:** "Yana" (video periuk stainless steel pink, bilik dinding pink); **"Emcee Hafiz"** (pengacara lelaki baju Melayu biru kotak, majlis raya — klien servis pengacara; rakan pengacara wanita tudung teal, nama belum disahkan).

## 🕒 Menunggu keputusan pengguna

| # | Cadangan | Sumber |
|---|---|---|
| P9 | **Warna highlight caption berselang** (merah → hijau → kuning) sebagai pilihan selain satu warna (R16 masih: tukar warna teks, bukan kotak). Claude cadang, pengguna pilih (R2). | Sample 10–13 |
| P10 | **Emoji kecil di atas caption** ikut maksud perkataan (😯 📦 🛒 🏫), jarang-jarang. | Sample 11–13 |
| P15 | **Highlight caption = kotak warna di belakang perkataan aktif** (edit Rejuran) vs tukar warna teks (R16, kekal lalai buat masa ini). | /compare-learnedit Rejuran (item 13) |
| P16 | **Kekalkan isian natural** (cth. "Aa," sebelum ayat) vs buang semua (R11, kekal lalai buat masa ini). | /compare-learnedit Rejuran (item 16) |
| P11 | **Bukti harga sebagai screenshot/poster pop** di sebelah produk semasa harga disebut (kad halaman produk, poster promo, tag harga) — ikut R1. | Sample 10–12 |

---

## Log perbandingan & maklum balas

| Tarikh | Jenis | Video | Ringkasan | Hasil |
|---|---|---|---|---|
| 2026-11-07 | Maklum balas job | Ujian periuk stainless steel (v1 → v2) | Badge & tulisan tutup muka/produk → semua tulisan dipindah ke zon kosong | R1 diterima |
| 2026-11-07 | /compare-learnedit | Periuk stainless steel — edit pengguna (45.7 s) vs Claude v2 (52.1 s) | 14 item dibanding; perbandingan dalam `comparisons/2026-11-07-periuk/` | R1a, R1b, R5–R16 diterima; X1, X2 ditolak; item 8 = nota |
| 2026-11-07 | /sample-baru | Sample 6 — IDECO Smart Diffuser (BettyRahmad) | Caption kotak lime bercanggah R16; −9.9 LUFS bercanggah R14 (tidak dipelajari). 5 cadangan P1–P5 | R17–R21 diterima (P5: transition mesti sesuai dengan video) |
| 2026-11-09 | Idea pengguna | Penambahbaikan proses | Semak audio dulu, senarai sangkut tanpa potong, pelan jadual, papan layout, subtitle 1–3 perkataan, whoosh lembut | R23–R28, X3 diterima |
| 2026-11-09 | Arahan pengguna | Kemas kini peraturan | X3 (larangan bunyi magic/dramatik) DIBUANG; R28 dikemas kini; R29 aliran kelulusan storyboard+papan layout → preview → klien → final | X3 dibuang, R29 diterima |
| 2026-11-10 | /sample-baru | Sample 7, 8, 9 — highlight Karnival Insolvensi MITC Melaka (landscape) | Kategori baharu; −7 hingga −9 LUFS bercanggah R14 (tidak dipelajari); P6–P8 | R30–R32 diterima (tanya landscape/9:16 dulu) |
| 2026-11-10 | /sample-baru | Sample 10–13 (food review, unboxing, skit+vlog, premis) | Kelantangan −7 hingga −21 LUFS bercanggah R14; S11 tanpa hitam & S13 pudar putih bercanggah R12 (tidak dipelajari). P12–P14 → R33–R35 diterima; P9–P11 masih menunggu | Sebahagian |
| 2026-11-12 | /compare-learnedit | Rejuran (Yana) — edit pengguna (50.7 s: hook punchline + colour bars/beep, suara 1.14×, ±7 SFX, title skrip+bulat pink, tiada BGM) vs Claude PREVIEW v1 (61.3 s) | Perbandingan dalam `comparisons/2026-11-12-rejuran/`; pengguna tak suka hook flash-forward | R45–R55 diterima (R5 lalai & R28 diganti, R8/R10 diperhalusi); X7, X8 ditolak; P15, P16 menunggu |
| 2026-11-13 | Maklum balas job | herba-headspa — UGC vlog kedai herba (raw 34.9 s → FINAL 24.2 s, 6 preview) | Tiada hook (pilihan pengguna); caption magenta (kontras terbaik atas hud kelabu & rak hijau); transkrip dibanding dengan caption CapCut (Whisper tukar "I"→"saya", "kita"→"dia"). Maklum balas: suara ASAL (tiada denoise, tiada 1.12×); buang title "heaven"; "Serbuk" huruf besar; callout mesti muncul tepat ikut subtitle; caption 58→48 px & geser kiri elak butang TikTok; akhirnya SEMUA SFX dibuang (pengguna tambah sendiri) | Calon peraturan diputuskan dalam /compare-learnedit herba-headspa → R61–R66 |
| 2026-11-13 | /compare-learnedit | herba-headspa — edit pengguna (FINAL Claude + filter + BGM + 2 SFX, −6.3 LUFS) vs Claude FINAL v6 | Frame selari tepat; pengguna kekalkan visual/caption Claude; klien minta kurangkan filter → versi 50% diluluskan klien. Perbandingan dalam `comparisons/2026-11-13-herba-headspa/` | R61–R66 diterima (R47 jadi pilihan, R16 saiz diganti, R48 diperhalusi); X9 ditolak; R55 (tiada BGM) KEKAL |
| 2026-11-10 | /compare-learnedit | Majlis raya — edit pengguna (59.9 s, take panjang + header tetap + teks dialog + muzik) vs Claude FINAL v4 (slideshow 36 s) | Perbandingan dalam `comparisons/2026-11-10-raya/`; pengguna serahkan keputusan kepada Claude | R36–R44 diterima; X4–X6 ditolak |
| 2026-11-14 | /compare-learnedit | kenangan-airterjun (Sukali Waterfall, Myanmar) — edit pengguna (58.8 s: + 5 foto klien, ±9 light leak, BGM, −13.2 LUFS) vs Claude FINAL v2 (48.6 s: 10 babak crossfade, intro poskad, bunyi air −26 LUFS) | Jenis job baharu: video kenangan pemandangan tanpa suara. Perbandingan dalam `comparisons/2026-11-14-kenangan-airterjun/` (muka klien di-blur, tiada video) | R67–R71 diterima; X10, X11 ditolak |
