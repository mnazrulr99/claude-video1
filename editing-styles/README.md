# Katalog Gaya Editing

Semua editing dibuat & dirender terus oleh Claude (ffmpeg) — pengguna tak guna sebarang app editing.

## Aliran kerja WAJIB (setiap job editing)

0. **Guna skill yang dah dipelajari:** baca katalog, Pattern Bersama, Catatan citarasa & **Pelajaran projek siap**
   di bawah, dan ikut skill teknikal `edit-video` (`.claude/skills/edit-video/SKILL.md`).
1. Pengguna hantar **video mentah** (+ gambar produk PNG jika ada; jika tiada, pengguna akan maklumkan
   → Claude potong gambar produk dari video sebagai alternatif).
2. **Analisis dulu, jangan terus edit.** Claude analisis video mentah (durasi, kandungan, **transkrip word-level**,
   jenis video: edukasi/sembang vs iklan produk, mood, kualiti audio, kedudukan muka/produk) dan beri **cadangan gaya**
   (Sample mana yang paling sesuai + sebab + apa yang perlu diubah suai, cadangan hook & BGM).
   Jika pengguna kata "ikut kreativiti kau", Claude terus pilih dan teruskan ke langkah 4.
3. Pengguna pilih/setuju gaya.
4. Claude edit dan hasilkan **PREVIEW 540p + STORYBOARD dalam bentuk imej**
   (frame setiap babak + masa, teks caption, title callout, zoom, effect, SFX, BGM, jenis hook, zon safe-zone).
5. **JANGAN render final** sebelum pengguna setuju. Ulang preview + storyboard ikut komen pengguna sehingga setuju.
6. Baru render video akhir 1080×1920 (30 fps, kecuali diminta lain) dan hantar kepada pengguna.
7. **Simpan pelajaran** (wajib setiap kali editing habis): `projects/<nama>/README.md`, baris baharu dalam
   **"Pelajaran projek siap"**, kemas kini citarasa/pattern & skill `edit-video` jika perlu → commit & push.

## Pelajaran projek siap (skill yang dipelajari dari setiap edit)

| Projek | Jenis | Gaya dipakai | Keputusan akhir pengguna | Pelajaran untuk edit akan datang |
|---|---|---|---|---|
| [jam-wira](../projects/jam-wira/README.md) (Nov 2026) | Review UGC talking-head, jam budak, 87.5 s → 58.4 s | S1 + S2/S3, kemudian belajar dari S6 (edit pengguna sendiri) | V3: hook kontra "tak nak smartwatch ❌" + **b-roll close-up produk dalam 2 s**, flash+impact, punch-in kuat pada poin utama, word-art warna, tulisan tangan + anak panah, CTA kecil awal + CTA slam, caption **besar mint**, ~15 grafik, **tanpa BGM** | (1) Tunjuk produk close-up dalam 2–3 s pertama. (2) Pindah ayat ulang/terkuat jadi hook, bukan padam. (3) Grafik tidak semua kotak seragam — campur serif/word-art/tulisan tangan. (4) Semak setiap grafik dengan still sebenar — anotasi pernah tertindih dagu bila subjek condong. (5) Review UGC: default **tanpa BGM**. (6) Audio: loudnorm −15 LUFS + limiter oversampled (peak ≤ −1.5 dBFS). (7) Sahkan potongan dengan transkrip semula. (8) **Silap yang pengguna kesan selepas final:** caption "SEE DIA CANTIK" patutnya **"SERIOUS CANTIK"** (Whisper p=0.89), dan suara pada 22–23 s tenggelam sebab ekor chime "confirm" (1.33 s) bertindih dengan perkataan + jeda 0.48 s tertinggal → kini semak perkataan ragu-ragu, elak/duck SFX yang bertindih suara, imbas jeda dalam segmen. |

## Belajar berterusan

- Setiap sample disimpan bersama **salinan preview `preview-540p.mp4`** (540p, ~1.5–7 MB) dalam folder sample — video asal di Google Drive boleh dipadam oleh pengguna.

- Pengguna akan terus beri **video sample siap edit**. Setiap sample baharu → analisis penuh,
  simpan sebagai `sample-N/README.md`, tambah ke katalog, dan **kemas kini "Pattern Bersama" di bawah**.
- Cari pattern yang berulang merentas sample → itulah "selera" pengguna; utamakan pattern ini dalam setiap edit.
- Komen pengguna semasa semakan storyboard juga ialah data pembelajaran → catat di "Catatan citarasa pengguna".

## Pattern Bersama (dikemas kini setiap sample baharu)

_Berdasarkan Sample 1–6:_

| Pattern | S1 (edukasi) | S2 (iklan UGC) | S3 (iklan feminin) | S4 (skit brand) | S5 (showcase senyap) | S6 (review UGC, edit pengguna) | Kesimpulan |
|---|---|---|---|---|---| --- |---|
| Format | 9:16 | 9:16, 60 fps | ≈9:16 | ≈9:16 | 9:16 | 9:16, 30 fps | **Sentiasa vertical 9:16, 1080×1920** |
| Hook | Flash + B&W, soalan | Produk + colour bars/beep | Title soalan + sticker emoji | Makan ASMR tanpa caption | Unboxing + header + sparkle | Manfaat produk + produk di tangan, flash+impact | **Hook < 3.5 s: visual luar biasa/menarik + SFX; soalan atau aksi** |
| Potongan | Jump cut laju | Jump cut 1–3 s | Take lebih panjang masa demo | Take lakonan 2–4 s | Klip 2–12 s ikut proses | Kronologi; baris ulang dipindah jadi hook | **Buang jeda; laju, perlahan sedikit masa demo** |
| Framing | Punch-in 2–4 s | Punch-in ekstrem | Produk rapat ke lensa + wide | Medium + top-down + crash zoom | Close-up tangan, top-down, split 3 panel | Punch-in kuat & jarang (1.2–1.4×) | **Variasi framing kerap** |
| Caption | ALL CAPS, teks kuning | ALL CAPS, kotak lime | ALL CAPS condensed, teks pink | ALL CAPS, kotak biru | Tiada (tiada suara) | ALL CAPS kecil, highlight kuning, y≈77% | **Jika ada suara:** karaoke word-by-word, ALL CAPS, putih + 1 warna highlight (teks/kotak) ikut brand/mood, 60–78% dari atas. **Tiada suara:** tiada caption, guna teks callout |
| Title/grafik | Title + ❌/‼️ | Title + ❌/✅ + label pelbagai | Serif + skrip, 🎀 ✅, sticker | Title gaya brand + doodle animasi | Header tetap + checklist ✅ + sticker sudut | Serif+skrip atas close-up, word-art warna, tulisan tangan + anak panah, ✓ checklist | **Title poin utama + emoji/doodle; gaya title ikut brand/mood** |
| SFX | Pop/ding/impact | Beep/chime/click/ding | Sparkle + pop berulang + ASMR | Whoosh/ding + ASMR + foley | Sparkle/ding sahaja, selebihnya senyap | ~8 SFX kuat (impact, chime) | **Setiap grafik = SFX; kekalkan bunyi ASMR/foley produk** |
| Transition | Hard cut | + 2 khas | + 3 khas (blur, mirror, splash) | + whip/zoom blur, crash zoom | Splash cecair putih/hitam, split screen | Flash putih + blur zoom | **Hard cut dominan; blur-type transition di pertukaran babak** |
| BGM | Tiada | Perlahan | Perlahan | Sangat perlahan / mungkin tiada | Tiada dalam eksport (trending sound di TikTok) | Tiada | **Suara sentiasa dominan; BGM perlahan atau tiada. Video tanpa suara: BGM royalty-free; jika tiada yang sesuai → SFX sahaja (pengguna tambah trending sound di TikTok)** |
| Struktur | Hook → senarai → twist | Masalah → Produk → Manfaat → CTA | Masalah → Punca → Demo → CTA | Masalah (lakonan) → Produk → Kempen → CTA | Unboxing → Guna → Manfaat → Proses | Manfaat → Cerita → Ciri → Bonus → CTA | **Masalah → Produk/solusi → Bukti/demo → CTA** |
| Ending | Cut hitam | Cut hitam + fade | Cut hitam + ding | Impact + cut hitam | Splash hitam + ding | CTA cop "CHECKOUT SEKARANG!" + SFX | **Cut ke hitam (+ SFX/fade)** |

**Pemerhatian:**
- **4 daripada 5 sample ialah kandungan produk/brand** — jenis job utama pengguna. Ada 2 sub-jenis:
  (a) **bercakap ke kamera** (S2, S3, S4) → caption karaoke; (b) **faceless tanpa suara** (S5) → header tetap + teks callout, tiada caption.
- Transition **splash cecair** muncul dalam S3 & S5; **ding penutup yang sama** dalam S3 & S5 → kemungkinan aset CapCut kegemaran.
- Warna highlight caption sentiasa **ikut warna produk/brand/mood** (kuning, lime, pink, biru).
- Grafik maklumat (poster, infografik) diletak di atas **video yang di-blur** atau dipop masuk sebagai bukti (S3, S4).
- Bunyi semula jadi produk (buih, sedut mi, taip) **dikekalkan** sebagai ASMR.
- **S6 (edit pengguna sendiri)** = rujukan paling tepat untuk citarasa pengguna: grafik **sedikit tapi bergaya** (serif elegan, word-art warna, tulisan tangan), **CTA kecil awal** + CTA akhir, **tiada BGM**, caption kecil kuning. Highlight **kuning** kini muncul dalam S1 & S6.

## Catatan citarasa pengguna

- Tidak mahu buka sebarang app editing — Claude render terus.
- BGM royalty-free sahaja; pengguna pilih dari senarai.
- Hook wajib, tapi gaya hook mesti kena dengan jenis video.
- **Warna highlight caption:** Claude cadangkan pilihan (cth. padan warna produk/brand vs warna dari sample) berserta sebab dalam peringkat cadangan gaya/storyboard; **pengguna yang buat keputusan akhir**.
- Secara umum: untuk pilihan kreatif (gaya, hook, BGM, warna), Claude beri cadangan + sebab, pengguna pilih.
- **Video tanpa suara (gaya Sample 5):** masukkan **BGM royalty-free** — Claude cadangkan beberapa pilihan (link untuk didengar) ikut mood. Jika tiada yang sesuai, render dengan **SFX sahaja tanpa BGM** supaya pengguna boleh tambah trending sound sendiri dalam TikTok.

- **Remotion (Nov 2026, projek `projects/jam-wira/`):** pengguna minta edit guna **Remotion** — transkrip dulu (Whisper, word-level) untuk tentukan letak animasi/motion graphics/SFX; **SFX premium**; **jangan tutup muka** dengan grafik; patuhi **safe zone TikTok & IG**; BGM ada tapi suara mesti dominan (≈18 dB bawah suara); buang ulangan & jeda janggal; cari hook paling kuat; **tunjuk preview dulu, jangan render final**. Pengguna beri kebebasan kreatif ("ikut kreativiti kau").

- **Suara mesti sentiasa jelas — SFX tak boleh tenggelamkan perkataan** (komen pengguna selepas jam-wira: "serious cantik" pada 22–23 s tenggelam di bawah chime). SFX panjang hanya di celah senyap atau di-duck bawah suara.
- **Caption mesti tepat** — perkataan yang Whisper tak pasti (cth. "SEE" sebenarnya "SERIOUS") disemak / ditanya kepada pengguna semasa preview.
- **Jam-wira V3 (keputusan pengguna):** suka hook gabungan (kontra + b-roll produk), **buang BGM**, caption kekal besar, grafik ~15 OK.
- **Belajar dari Sample 6 vs edit Claude (jam-wira):** pengguna suka **produk kelihatan sangat awal**, **close-up produk sebagai title card**, grafik bergaya organik (bukan semua kotak seragam), **CTA kecil awal**, SFX sedikit tapi jelas. Gunakan sebagai default untuk review UGC, tapi kekalkan amalan Claude yang lebih selamat: **safe zone**, **limiter (peak ≤ −1 dBFS)**, **loudness ≈ −14 hingga −16 LUFS**, grafik tidak menutup muka/dahi.

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
| **Sample 4** | Skit lakonan komedi tajaan brand (makanan), hook makan ASMR tanpa caption, flashback masalah, title gaya brand, doodle animasi + tint merah "pedas", whip/zoom blur, segmen kempen dengan poster atas latar blur, caption kotak biru | [sample-4/](sample-4/README.md) |
| **Sample 5** | Showcase produk faceless tanpa suara (unboxing + proses), header tetap font bubbly, sticker hiasan sudut, checklist ✅ ditanda, split screen 3 panel, splash cecair putih/hitam, SFX sahaja (trending sound ditambah di TikTok) | [sample-5/](sample-5/README.md) |
| **Sample 6** | Review UGC talking-head (edit pengguna sendiri, video mentah sama dgn projek jam-wira), hook manfaat + produk di tangan, flash+impact, word-art warna, title serif atas close-up, anotasi tulisan tangan, ✓ MATERIAL, CTA cop "CHECKOUT SEKARANG!", caption kecil kuning, tiada BGM | [sample-6/](sample-6/README.md) |
