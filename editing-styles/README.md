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

_Berdasarkan Sample 1, 2 & 3:_

| Pattern | Sample 1 (edukasi) | Sample 2 (iklan) | Sample 3 (iklan feminin) | Kesimpulan |
|---|---|---|---|---|
| Format | 9:16 | 9:16, 60 fps | ≈9:16 (1050×1920) | **Sentiasa vertical 9:16, 1080×1920** |
| Hook | Flash + B&W, soalan | Pegang produk + colour bars/beep | Title soalan masalah + sticker emoji + sparkle | **Hook < 3.5 s: soalan/masalah + elemen visual luar biasa + SFX** |
| Potongan | Jump cut, jeda ≤0.3 s | Jump cut setiap 1–3 s | Jump cut, take lebih panjang semasa demo | **Buang jeda; rentak laju, boleh perlahan sedikit masa demo** |
| Zoom/framing | Punch-in setiap 2–4 s | Punch-in ekstrem 4× | Produk digerak rapat ke lensa + shot wide | **Variasi framing setiap beberapa saat** |
| Caption | Word-by-word, ALL CAPS, teks kuning | Word-by-word, ALL CAPS, kotak lime | Word-by-word, ALL CAPS condensed, teks pink | **Karaoke word-by-word, ALL CAPS, putih + highlight 1 warna (ikut mood/brand)**, posisi 60–78% dari atas |
| Title/grafik | Title atas + ❌/‼️ | Title + ❌/✅ + banyak label | Serif + skrip italic, 🎀 ✅, sticker | **Poin utama = title + emoji (❌/✅/‼️/🎀), animasi typewriter** |
| SFX | Pop/ding/impact | Beep/chime/click/ding | Sparkle + pop sama diulang + ASMR | **Setiap title/grafik baru = satu SFX** |
| Transition | Hard cut sahaja | Hard cut + 2 khas | Hard cut + 3 khas (blur, mirror, splash) | **Hard cut dominan; 0–3 transition khas di pertukaran bahagian** |
| BGM | Tiada | Perlahan berterusan | Perlahan berterusan | **Iklan: BGM perlahan; edukasi: tiada/perlahan** |
| Struktur iklan | – | Masalah → Produk → Manfaat → Dos → CTA | Masalah → Punca → Varian → Demo → Manfaat → CTA + bukti | **Formula iklan: Masalah → Produk → Manfaat/Demo → CTA "beg kuning"** |
| Ending | Cut ke hitam | Cut ke hitam + fade | Cut ke hitam + ding + fade | **Akhiri dengan cut ke hitam (+ fade audio)** |

**Pemerhatian:** 2 daripada 3 sample ialah **iklan produk UGC untuk TikTok Shop** — kemungkinan besar ini jenis job utama pengguna.
Warna highlight caption nampaknya dipilih **ikut warna produk/brand/mood** (kuning, lime, pink).

## Catatan citarasa pengguna

- Tidak mahu buka sebarang app editing — Claude render terus.
- BGM royalty-free sahaja; pengguna pilih dari senarai.
- Hook wajib, tapi gaya hook mesti kena dengan jenis video.
- **Warna highlight caption:** Claude cadangkan pilihan (cth. padan warna produk/brand vs warna dari sample) berserta sebab dalam peringkat cadangan gaya/storyboard; **pengguna yang buat keputusan akhir**.
- Secara umum: untuk pilihan kreatif (gaya, hook, BGM, warna), Claude beri cadangan + sebab, pengguna pilih.

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
| **Sample 3** | UGC iklan produk feminin, hook soalan + sticker 🍑, caption condensed highlight pink, title serif + skrip italic 🎀 ✅, demo produk close-up + ASMR, transition zoom blur/mirror/splash cecair, poster bukti, BGM perlahan, CTA beg kuning | [sample-3/](sample-3/README.md) |
