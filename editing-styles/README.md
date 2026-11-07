# Katalog Gaya Editing

Semua editing dibuat & dirender terus oleh Claude (ffmpeg) — pengguna tak guna sebarang app editing.

## Aliran kerja WAJIB (setiap job editing)

1. Pengguna hantar **video mentah** (+ gambar produk PNG jika ada; jika tiada, pengguna akan maklumkan
   → Claude potong gambar produk dari video sebagai alternatif).
2. **Analisis dulu, jangan terus edit.** Claude analisis video mentah (durasi, kandungan, transkrip,
   jenis video: edukasi/sembang vs iklan produk, mood, kualiti audio) dan beri **cadangan gaya**
   (Sample mana yang paling sesuai + sebab + apa yang perlu diubah suai, cadangan hook & BGM).
3. Pengguna pilih/setuju gaya.
4. Claude hasilkan **STORYBOARD dalam bentuk imej**
   (frame setiap babak + masa, teks caption, title callout, zoom, effect, SFX, BGM, jenis hook).
5. **JANGAN render** sebelum pengguna setuju. Ulang storyboard ikut komen pengguna sehingga setuju.
6. Baru render video akhir 1080×1920 dan hantar kepada pengguna.

## Belajar berterusan

- Pengguna akan terus beri **video sample siap edit**. Setiap sample baharu → analisis penuh,
  simpan sebagai `sample-N/README.md`, tambah ke katalog, dan **kemas kini "Pattern Bersama" di bawah**.
- Cari pattern yang berulang merentas sample → itulah "selera" pengguna; utamakan pattern ini dalam setiap edit.
- Komen pengguna semasa semakan storyboard juga ialah data pembelajaran → catat di "Catatan citarasa pengguna".

## Pattern Bersama (dikemas kini setiap sample baharu)

_Berdasarkan Sample 1 & Sample 2:_

| Pattern | Sample 1 | Sample 2 | Kesimpulan |
|---|---|---|---|
| Format | 9:16, 1080×1920 | 9:16, 1080×1920 | **Sentiasa vertical 9:16** |
| Hook | Flash + B&W, soalan | Pegang produk + colour bars/beep | **Hook < 2.5 s dengan pattern interrupt visual + SFX** |
| Potongan | Jump cut, jeda ≤0.3 s | Jump cut setiap 1–3 s | **Buang semua jeda, rentak laju** |
| Zoom | Punch-in setiap 2–4 s | Punch-in ekstrem 4× | **Punch-in pada momen penting** |
| Caption | Word-by-word, ALL CAPS, teks kuning | Word-by-word, ALL CAPS, kotak lime | **Karaoke word-by-word, ALL CAPS, highlight kuning/lime** |
| Title/grafik | Title atas + ❌/‼️ | Title tengah + ❌/✅ + banyak label | **Poin utama = title + emoji ❌/✅/‼️, animasi typewriter** |
| SFX | Pop/ding/impact pada setiap title | Beep/chime/click/ding pada setiap grafik | **Setiap grafik baru = satu SFX** |
| Transition | Hard cut sahaja | Hard cut + 2 transition khas | **Hard cut dominan, transition khas jarang** |
| BGM | Tiada | Perlahan berterusan | **Ikut jenis video** (edukasi: tiada/perlahan; iklan: ada) |
| Ending | Cut ke hitam | Cut ke hitam + audio fade | **Akhiri dengan cut ke hitam** |

## Catatan citarasa pengguna

- Tidak mahu buka sebarang app editing — Claude render terus.
- BGM royalty-free sahaja; pengguna pilih dari senarai.
- Hook wajib, tapi gaya hook mesti kena dengan jenis video.

## BGM (royalty-free) — senarai pendek untuk pengguna pilih

Muat turun dari sumber rasmi (bensound.com / incompetech.com / YouTube Audio Library), bukan dari reupload.
Kebanyakan perlukan **kredit artis dalam caption/deskripsi**.

| Mood | Lagu | Dengar |
|---|---|---|
| Motivasi / korporat | Bensound – Inspire | https://www.youtube.com/watch?v=FE92y5AZOdc |
| Motivasi / bertenaga | Bensound – Elevate | https://www.youtube.com/watch?v=NFcGmLyOh4w |
| Bisnes / upbeat ringan | Bensound – Perception | https://www.youtube.com/watch?v=6hf1Pq9yUdc |
| Motivasi | Kevin MacLeod – Motivator | https://www.youtube.com/watch?v=7NdrWtef_M0 |
| Ceria / santai | Kevin MacLeod – Carefree | https://youtube.com/watch?v=ueb-fGzZa2s |
| Tenang / refleksi | Kevin MacLeod – Gymnopedie No. 1 | https://www.youtube.com/watch?v=UjFFPoPYV-A |
| Chill / lofi | Chill Lofi Hip Hop (No Copyright) | https://www.youtube.com/watch?v=hQT6WMJ-Fco |

Pilihan pengguna: _(belum dipilih)_

| Nama gaya | Ringkasan | Rujukan |
|---|---|---|
| **Sample 1** | Talking-head 9:16, hook ikut jenis video, caption karaoke highlight kuning, punch-in zoom tiap 2–4 s, title callout atas + ❌/‼️, SFX pop/ding/impact, BGM pilihan, hard cut ke hitam | [sample-1/](sample-1/README.md) |
| **Sample 2** | UGC iklan produk 9:16 selfie, hook pegang produk + colour bars/beep, caption kotak highlight lime, title pain-point ❌, product reveal elegan + packshot, grafik pelbagai (UI box ✅, kursor klik, marquee, badge emas), BGM perlahan, CTA beg kuning | [sample-2/](sample-2/README.md) |
