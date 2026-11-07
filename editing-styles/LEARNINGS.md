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
| R5 | **Hook lalai = Hook B**: klip ±1 s momen paling menarik (flash-forward, cth. demo produk) dengan audio dimatikan + whoosh, kemudian cut ke awal video. (Masih cadang alternatif jika jenis video lain.) | Hook | /compare-learnedit periuk (item 1) | 2026-11-07 |
| R6 | **Framing asas lebih ketat (±1.2× crop)** supaya muka & produk penuhkan skrin; elak ruang kosong (meja/lantai) yang banyak. Punch-in tambahan di atas itu. | Framing | /compare-learnedit periuk (item 2) | 2026-11-07 |
| R7 | **Punch-in ekstrem pada produk** bila menyebut butiran fizikal (saiz/bahagian), digabung dengan label R1b. | Framing | /compare-learnedit periuk (item 3) | 2026-11-07 |
| R8 | **Font & warna title ikut produk/mood** (cth. produk pink → font bulat/bubbly pink, outline putih, doodle hati). | Title | /compare-learnedit periuk (item 6) | 2026-11-07 |
| R9 | **Callout dengan doodle sparkle** (garis kecil ✦ di tepi pill) dan diletak **dekat benda yang disebut** (tertakluk R1). Teks pendek boleh condong sedikit. | Grafik | /compare-learnedit periuk (item 7) | 2026-11-07 |
| R10 | **Satu transition kreatif di pertengahan video** (cth. paper-rip/koyak kertas + strip B&W + bunyi koyak); selebihnya hard cut. | Transition | /compare-learnedit periuk (item 9) | 2026-11-07 |
| R11 | **Potongan jeda lebih ketat** — buang semua ruang antara ayat (sasaran: rentak sepadat edit pengguna, ±45 s untuk raw 56 s). | Rentak | /compare-learnedit periuk (item 10) | 2026-11-07 |
| R12 | **Tamat dengan skrin hitam** (±0.5–0.7 s) + ding penutup. | Ending | /compare-learnedit periuk (item 11) | 2026-11-07 |
| R13 | **CTA diletak di zon selamat** (tidak tutup muka/produk), cth. pill dengan ikon beg. | CTA | /compare-learnedit periuk (item 12) | 2026-11-07 |
| R14 | **Kelantangan akhir −13 hingga −14 LUFS** (guna loudnorm dua laluan supaya tepat). | Audio | /compare-learnedit periuk (item 13) | 2026-11-07 |
| R15 | **Nama presenter:** bila presenter sebut nama sendiri, tanya/sahkan nama dan tulis dalam caption (cth. **"Yana"**, bukan "akak"). Whisper sering salah dengar nama. | Transkrip | /compare-learnedit periuk (item 14) | 2026-11-07 |
| R16 | **Saiz caption mesti mudah dibaca dalam telefon** (±54–60 px pada 1080 lebar; jangan kecil seperti ±30 px). Warna highlight dicadang ikut R2. | Caption | /compare-learnedit periuk (item 5: "ikut R1") | 2026-11-07 |

## ❌ Ditolak (JANGAN belajar / jangan guna)

| ID | Perkara | Sebab | Sumber | Tarikh |
|---|---|---|---|---|
| X1 | Caption terlalu kecil (sukar dibaca di telefon) | Kebolehbacaan | /compare-learnedit periuk (item 5) | 2026-11-07 |
| X2 | CTA / teks besar yang **menutup produk** (cth. teks skrip "Tengok dekat beg kuning" atas periuk) | Bercanggah R1 | /compare-learnedit periuk (item 12) | 2026-11-07 |

## 📝 Nota (bukan peraturan)

- **Jumlah grafik fleksibel** — pengguna suka dua-dua (±5 grafik/45 s atau ±9 grafik/52 s). Claude tentukan ikut kandungan dan tunjuk dalam storyboard. (/compare-learnedit periuk item 8)
- **Presenter dikenali:** "Yana" (video periuk stainless steel pink, bilik dinding pink).

## 🕒 Menunggu keputusan pengguna

_(Cadangan dari `/compare-learnedit` yang belum disahkan — jangan guna sehingga disahkan.)_

---

## Log perbandingan & maklum balas

| Tarikh | Jenis | Video | Ringkasan | Hasil |
|---|---|---|---|---|
| 2026-11-07 | Maklum balas job | Ujian periuk stainless steel (v1 → v2) | Badge & tulisan tutup muka/produk → semua tulisan dipindah ke zon kosong | R1 diterima |
| 2026-11-07 | /compare-learnedit | Periuk stainless steel — edit pengguna (45.7 s) vs Claude v2 (52.1 s) | 14 item dibanding; perbandingan dalam `comparisons/2026-11-07-periuk/` | R1a, R1b, R5–R16 diterima; X1, X2 ditolak; item 8 = nota |
