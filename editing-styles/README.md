# Katalog Gaya Editing

Semua editing dibuat & dirender terus oleh Claude (ffmpeg) — pengguna tak guna sebarang app editing.

## Aliran kerja WAJIB (setiap job editing)

> **SOP penuh dengan pintu kelulusan: [SOP.md](SOP.md).** Ringkasan:

1. Pengguna hantar **video mentah** (+ gambar produk jika ada).
2. **Semak audio dahulu** (`tools/audio_check.py`) — jika terlalu perlahan/senyap → berhenti & beritahu pengguna (R23).
3. **Analisis & transkrip**; tunjuk **senarai ayat tersangkut/ulang** (jangan potong dulu, R24) + **cadangan gaya**
   (Sample, hook, warna caption, BGM). Pengguna pilih.
4. **Pelan edit dalam jadual** (Saat · Layout · Visual · Kenapa; visual tukar 2–4 s, R25).
5. **Storyboard + papan layout** (satu papan semua layout) sebelum render → pengguna luluskan (R26, R29).
6. **Render PREVIEW**: video 540p dengan satu "PREVIEW" di tengah + storyboard versi klien (R22).
7. Pengguna hantar kepada **klien** → feedback → betulkan → preview baharu (ulang).
8. Klien OK semua → **render FINAL** 1080×1920 tanpa watermark.

Peraturan penuh: [LEARNINGS.md](LEARNINGS.md).

## Belajar berterusan

- Setiap sample disimpan bersama **salinan preview `preview-540p.mp4`** (540p, ~1.5–7 MB) dalam folder sample — video asal di Google Drive boleh dipadam oleh pengguna.

- Pengguna akan terus beri **video sample siap edit**. Setiap sample baharu → analisis penuh,
  simpan sebagai `sample-N/README.md`, tambah ke katalog, dan **kemas kini "Pattern Bersama" di bawah**.
- Cari pattern yang berulang merentas sample → itulah "selera" pengguna; utamakan pattern ini dalam setiap edit.
- Komen pengguna semasa semakan storyboard juga ialah data pembelajaran → catat di "Catatan citarasa pengguna".

## Pattern Bersama (dikemas kini setiap sample baharu)

_Berdasarkan Sample 1–13 (S7–S9 satu siri highlight acara; S10–S13 diringkaskan sebagai satu lajur kerana gaya caption & grafik sama):_

| Pattern | S1 (edukasi) | S2 (iklan UGC) | S3 (iklan feminin) | S4 (skit brand) | S5 (showcase senyap) | S6 (UGC rumah, POV) | S7–S9 (highlight acara, landscape) | S10–S13 (UGC review/haul/vlog/premis) | Kesimpulan |
|---|---|---|---|---|---|---|---|---|---|
| Format | 9:16 | 9:16, 60 fps | ≈9:16 | ≈9:16 | 9:16 | 9:16 | **Landscape 1920×1080** | 9:16 | **9:16 untuk UGC/TikTok; landscape 1920×1080 untuk highlight acara** (tanya platform) |
| Hook | Flash + B&W, soalan | Produk + colour bars/beep | Title soalan + sticker emoji | Makan ASMR tanpa caption | Unboxing + header + sparkle | POV skit + teks "Pov:" + sparkle | Logo intro / drone / momen VIP | Title soalan bubbly / teaser / skit / POV pintu | **Hook < 3.5 s: visual luar biasa/menarik + SFX; soalan atau aksi** |
| Potongan | Jump cut laju | Jump cut 1–3 s | Take lebih panjang masa demo | Take lakonan 2–4 s | Klip 2–12 s ikut proses | Jump cut ketat | Montaj ±0.6 s/klip ikut beat | ±1.5–1.8 s/klip (S12 lebih perlahan) | **Buang jeda; laju, perlahan sedikit masa demo** |
| Framing | Punch-in 2–4 s | Punch-in ekstrem | Produk rapat ke lensa + wide | Medium + top-down + crash zoom | Close-up tangan, top-down, split 3 panel | Produk ditolak ke lensa, extreme close-up | Gimbal, drone, push-in sinematik | Muka ↔ close-up produk/makanan, POV masuk kedai | **Variasi framing kerap** |
| Caption | ALL CAPS, teks kuning | ALL CAPS, kotak lime | ALL CAPS condensed, teks pink | ALL CAPS, kotak biru | Tiada (tiada suara) | ALL CAPS, kotak lime | Tiada (tiada suara) | ALL CAPS 2 baris, tukar warna teks **merah/hijau/kuning berselang** + emoji kecil | **Jika ada suara:** karaoke word-by-word, ALL CAPS, putih + 1 warna highlight (teks/kotak) ikut brand/mood, 60–78% dari atas. **Tiada suara:** tiada caption, guna teks callout |
| Title/grafik | Title + ❌/‼️ | Title + ❌/✅ + label pelbagai | Serif + skrip, 🎀 ✅, sticker | Title gaya brand + doodle animasi | Header tetap + checklist ✅ + sticker sudut | Search-bar pill, tulisan tangan, ✅, sparkle | Logo acara tetap (atas tengah / bawah kanan) | Screenshot harga produk, logo kedai/app + label kempen, poster promo, pill URL, teks skrip elegan | **Title poin utama + emoji/doodle; gaya title ikut brand/mood** |
| SFX | Pop/ding/impact | Beep/chime/click/ding | Sparkle + pop berulang + ASMR | Whoosh/ding + ASMR + foley | Sparkle/ding sahaja, selebihnya senyap | Sparkle/ding/riser setiap label | Tiada ketara (muzik dominan) | Tidak ketara | **Setiap grafik = SFX; kekalkan bunyi ASMR/foley produk** |
| Transition | Hard cut | + 2 khas | + 3 khas (blur, mirror, splash) | + whip/zoom blur, crash zoom | Splash cecair putih/hitam, split screen | Kad foto berpusing, brush stroke, B&W reaksi | Banyak: light leak, kolaj, bingkai foto, filem, glitch, flash, tint | Hard cut; fade hitam/putih sekali-sekala | **Hard cut dominan; blur-type transition di pertukaran babak** |
| BGM | Tiada | Perlahan | Perlahan | Sangat perlahan / mungkin tiada | Tiada dalam eksport (trending sound di TikTok) | Kemungkinan tiada | Muzik penuh, tiada voiceover | Perlahan di bawah suara | **Suara sentiasa dominan; BGM perlahan atau tiada. Video tanpa suara: BGM royalty-free; jika tiada yang sesuai → SFX sahaja (pengguna tambah trending sound di TikTok)** |
| Struktur | Hook → senarai → twist | Masalah → Produk → Manfaat → CTA | Masalah → Punca → Demo → CTA | Masalah (lakonan) → Produk → Kempen → CTA | Unboxing → Guna → Manfaat → Proses | POV → Keperluan → Produk → Ciri → Harga → Varian → CTA | Ikut aturcara acara | Masalah/soalan → lokasi/brand → produk + harga → CTA | **Masalah → Produk/solusi → Bukti/demo → CTA** |
| Ending | Cut hitam | Cut hitam + fade | Cut hitam + ding | Impact + cut hitam | Splash hitam + ding | Cut hitam + ding | Fade ke hitam | Hitam (S10, S12) / tiada (S11) / putih (S13) | **Cut ke hitam (+ SFX/fade)** |

**Pemerhatian:**
- **S10–S13 (4 genre UGC: food review, unboxing haul, skit+shopping vlog, lawatan premis)** berkongsi gaya caption yang sama: tukar warna teks berselang merah/hijau/kuning + emoji kecil. Bukti harga/brand ditunjuk sebagai **screenshot/poster/logo pop** di sebelah subjek. Presenter S11 & S12 sama (mungkin kreator tetap pengguna).
- **Kategori job baharu (S7–S9): video highlight/recap acara korporat/kerajaan, landscape.** Ciri: tiada presenter/caption, montaj laju ikut muzik, logo acara tetap, transition kreatif lebih banyak berbanding UGC. Satu acara boleh dipecah kepada beberapa video (siang, perasmian, malam).
- **5 daripada 6 sample ialah produk UGC/affiliate** dengan CTA beg kuning. Label harga, ✅, sparkle dan tulisan tangan makin kerap (S5, S6, edit pengguna). Transition kreatif sekali-dua (kad foto, brush, paper-rip, splash).
- **Edit pengguna sendiri (periuk, /compare-learnedit):** framing ketat 1.2×, label saiz atas produk, title bubbly ikut warna produk, callout + doodle sparkle, satu paper-rip transition di tengah, potongan ketat, −13 LUFS. Butiran: [LEARNINGS.md](LEARNINGS.md).
- **Edit pengguna sendiri (Rejuran, /compare-learnedit 2026-11-12):** hook = ayat punchline terus di 0 s + **colour bars & beep ±1 s** (pattern sama dengan S2), suara dipercepat 1.14×, SFX jarang (±7/50 s, hanya pada grafik + riser masa zoom), title skrip italic + bulat tebal **pink kontras** dengan produk lavender, sticker pill putih nama produk, hard cut + punch-in sahaja, tiada BGM. Butiran: R45–R55 dalam [LEARNINGS.md](LEARNINGS.md), [comparisons/2026-11-12-rejuran/](comparisons/2026-11-12-rejuran/README.md).
- **Edit pengguna sendiri (majlis raya, /compare-learnedit 2026-11-10):** highlight acara 9:16 bercerita — header nama acara tetap di atas, branding klien kecil di bawah, teks dialog ayat pendek dekat penutur (ganti caption karaoke), muzik penuh tanpa suara asal, tiada SFX, take panjang untuk momen interaksi + montaj makanan laju, light leak & dip hitam. Butiran: R36–R44 dalam [LEARNINGS.md](LEARNINGS.md), [comparisons/2026-11-10-raya/](comparisons/2026-11-10-raya/README.md).
- **4 daripada 5 sample ialah kandungan produk/brand** — jenis job utama pengguna. Ada 2 sub-jenis:
  (a) **bercakap ke kamera** (S2, S3, S4) → caption karaoke; (b) **faceless tanpa suara** (S5) → header tetap + teks callout, tiada caption.
- Transition **splash cecair** muncul dalam S3 & S5; **ding penutup yang sama** dalam S3 & S5 → kemungkinan aset CapCut kegemaran.
- Warna highlight caption sentiasa **ikut warna produk/brand/mood** (kuning, lime, pink, biru).
- Grafik maklumat (poster, infografik) diletak di atas **video yang di-blur** atau dipop masuk sebagai bukti (S3, S4).
- Bunyi semula jadi produk (buih, sedut mi, taip) **dikekalkan** sebagai ASMR.

## Catatan citarasa pengguna

> Peraturan terperinci & sejarah pembelajaran: **[LEARNINGS.md](LEARNINGS.md)** (dikemas kini oleh `/compare-learnedit`, `/edit-video`, `/sample-baru`).


- Tidak mahu buka sebarang app editing — Claude render terus.
- BGM royalty-free sahaja; pengguna pilih dari senarai.
- Hook wajib, tapi gaya hook mesti kena dengan jenis video.
- **Warna highlight caption:** Claude cadangkan pilihan (cth. padan warna produk/brand vs warna dari sample) berserta sebab dalam peringkat cadangan gaya/storyboard; **pengguna yang buat keputusan akhir**.
- Secara umum: untuk pilihan kreatif (gaya, hook, BGM, warna), Claude beri cadangan + sebab, pengguna pilih.
- **PENTING — Kedudukan tulisan:** tulisan (caption, title, badge, label, CTA) **TIDAK BOLEH tutup muka**, dan sedaya upaya **tidak tutup produk**. Letak di ruang kosong (latar/dinding). Semak dengan `tools/zones.py` + snapshot sebelum render. Jika ruang sempit, kecilkan tulisan daripada menutup muka/produk. (Maklum balas job ujian periuk: badge "HARGA TURUN!" asal menutup muka.)
- **Video tanpa suara (gaya Sample 5):** masukkan **BGM royalty-free** — Claude cadangkan beberapa pilihan (link untuk didengar) ikut mood. Jika tiada yang sesuai, render dengan **SFX sahaja tanpa BGM** supaya pengguna boleh tambah trending sound sendiri dalam TikTok.

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
| **Sample 6** | UGC produk rumah (diffuser), hook POV skit + teks "Pov:", transition kad foto berpusing + bintang/reben pink, label search-bar lokasi, label tulisan tangan (USB ✅, harga, varian), reaksi B&W lawak, brush stroke, caption kotak lime | [sample-6/](sample-6/README.md) |
| **Sample 7** | Highlight acara **landscape** (siang: gerai, agensi, lelongan, makanan, kanak-kanak) — montaj ±0.6 s ikut muzik, logo acara atas tengah, tiada caption, drone, light leak, kolaj surat khabar, bingkai foto, filem | [sample-7/](sample-7/README.md) |
| **Sample 8** | Highlight acara **landscape** (majlis perasmian VIP) — glitch RGB/B&W, penjenama sinematik + light leak, gimik pelancaran dengan tint merah, lawatan gerai | [sample-8/](sample-8/README.md) |
| **Sample 9** | Highlight acara **landscape** (konsert malam + cabutan bertuah) — logo bawah kanan, drone malam, whiteout/flare antara segmen, artis ↔ reaksi penonton | [sample-9/](sample-9/README.md) |
| **Sample 10** | Food review restoran — title soalan bubbly, muka reaksi ↔ close-up makanan, poster menu/harga, label menu kecil, pill URL CTA | [sample-10/](sample-10/README.md) |
| **Sample 11** | Unboxing haul online (Pinduoduo) — teaser hook, title bubbly, logo app, **screenshot halaman produk + harga pop**, try-on, anak dalam frame | [sample-11/](sample-11/README.md) |
| **Sample 12** | Skit keluarga + shopping vlog tajaan kedai (Eco Shop Back to School) — teks tulisan tangan, logo + label kempen, poster promo, POV masuk kedai, tag harga | [sample-12/](sample-12/README.md) |
| **Sample 13** | Lawatan premis servis (klinik laser/facial) — voiceover + B-roll, POV pintu, logo, rawatan sebenar, bukti (scan/testimoni), teks skrip elegan untuk waktu & harga promo | [sample-13/](sample-13/README.md) |
