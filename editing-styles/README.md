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

_Berdasarkan Sample 1–17 (S7–S9 satu siri highlight acara; S10–S13 diringkaskan sebagai satu lajur kerana gaya caption & grafik sama):_

| Pattern | S1 (edukasi) | S2 (iklan UGC) | S3 (iklan feminin) | S4 (skit brand) | S5 (showcase senyap) | S6 (UGC rumah, POV) | S7–S9 (highlight acara, landscape) | S10–S13 (UGC review/haul/vlog/premis) | S14 (sewa kereta) | S15 (promo emcee) | S16 (UGC jam, kereta) | S17 (tutorial green-screen, EN) | Kesimpulan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Format | 9:16 | 9:16, 60 fps | ≈9:16 | ≈9:16 | 9:16 | 9:16 | **Landscape 1920×1080** | 9:16 | 9:16 (576×1024 repost TikTok) | 9:16 HDR (HLG), 72.5 s | 9:16, 55.8 s | 9:16, 122.8 s | **9:16 untuk UGC/TikTok; landscape 1920×1080 untuk highlight acara** (tanya platform) |
| Hook | Flash + B&W, soalan | Produk + colour bars/beep | Title soalan + sticker emoji | Makan ASMR tanpa caption | Unboxing + header + sparkle | POV skit + teks "Pov:" + sparkle | Logo intro / drone / momen VIP | Title soalan bubbly / teaser / skit / POV pintu | Kenyataan + twist harga, presenter sebelah kereta → punch-in | Emcee beraksi dengan mikrofon + header majlis ditaip | Produk terus di tangan + ciri ("water resistant tau") + whoosh reveal kotak | "❌ I NEVER DO THIS…" + kenyataan kesilapan terbesar | **Hook < 3.5 s: visual luar biasa/menarik + SFX; soalan atau aksi** |
| Potongan | Jump cut laju | Jump cut 1–3 s | Take lebih panjang masa demo | Take lakonan 2–4 s | Klip 2–12 s ikut proses | Jump cut ketat | Montaj ±0.6 s/klip ikut beat | ±1.5–1.8 s/klip (S12 lebih perlahan) | ±2.2 s/klip; B-roll ±1.2–1.5 s ikut perkataan | ±2.2 s; take panjang emcee/testimoni, montaj B-roll 1–3 s | Jump cut ±1.6 s/klip | B-roll ±3.7 s/klip; presenter atas satu take | **Buang jeda; laju, perlahan sedikit masa demo** |
| Framing | Punch-in 2–4 s | Punch-in ekstrem | Produk rapat ke lensa + wide | Medium + top-down + crash zoom | Close-up tangan, top-down, split 3 panel | Produk ditolak ke lensa, extreme close-up | Gimbal, drone, push-in sinematik | Muka ↔ close-up produk/makanan, POV masuk kedai | Wide presenter+kereta ↔ B-roll detail (rim, interior) | Handheld tetamu ↔ medium emcee ↔ selfie testimoni | Medium kereta ↔ extreme close-up produk ke lensa | Presenter cut-out bawah ±55% atas B-roll demo | **Variasi framing kerap** |
| Caption | ALL CAPS, teks kuning | ALL CAPS, kotak lime | ALL CAPS condensed, teks pink | ALL CAPS, kotak biru | Tiada (tiada suara) | ALL CAPS, kotak lime | Tiada (tiada suara) | ALL CAPS 2 baris, tukar warna teks **merah/hijau/kuning berselang** + emoji kecil | **1 perkataan ALL CAPS putih, ±22% dari ATAS** (langit), tiada highlight | Testimoni sahaja: **sentence case, perkataan bertambah** jadi ayat 3–4 baris, krim, ±75%, ≈36 px | ALL CAPS putih + **perkataan aktif kuning**, ≈48 px, ±78% | Tiada karaoke — **teks langkah bernombor** sentence case di atas ±22% | **Jika ada suara:** karaoke word-by-word, ALL CAPS, putih + 1 warna highlight (teks/kotak) ikut brand/mood, 60–78% dari atas (S14: caption di atas ±22% bila produk besar penuhi bahagian bawah — R81f). **Tiada suara:** tiada caption, guna teks callout |
| Title/grafik | Title + ❌/‼️ | Title + ❌/✅ + label pelbagai | Serif + skrip, 🎀 ✅, sticker | Title gaya brand + doodle animasi | Header tetap + checklist ✅ + sticker sudut | Search-bar pill, tulisan tangan, ✅, sparkle | Logo acara tetap (atas tengah / bawah kanan) | Screenshot harga produk, logo kedai/app + label kempen, poster promo, pill URL, teks skrip elegan | Label kegunaan **kuning + ✅** bertukar satu demi satu; tiada title/logo | **Header tetap** serif krim "Majlis Resepsi" + nama pengantin skrip putih (kanan atas) + branding "Emcee Medina" bawah | Title serif + skrip + pill "Tengok Beg Kuning!", label warna bubbly ikut warna varian, ✓ ciri, CTA tape kuning | Kad title siri serif merah atas krim-pink + papan cadangan produk | **Title poin utama + emoji/doodle; gaya title ikut brand/mood** |
| SFX | Pop/ding/impact | Beep/chime/click/ding | Sparkle + pop berulang + ASMR | Whoosh/ding + ASMR + foley | Sparkle/ding sahaja, selebihnya senyap | Sparkle/ding/riser setiap label | Tiada ketara (muzik dominan) | Tidak ketara | Ding pada label ✅, whoosh pada flash (kesimpulan) | Tiada ketara (BGM dominan) | Whoosh + sparkle + ding setiap label + chime CTA (±7) | Tiada | **Setiap grafik = SFX; kekalkan bunyi ASMR/foley produk** |
| Transition | Hard cut | + 2 khas | + 3 khas (blur, mirror, splash) | + whip/zoom blur, crash zoom | Splash cecair putih/hitam, split screen | Kad foto berpusing, brush stroke, B&W reaksi | Banyak: light leak, kolaj, bingkai foto, filem, glitch, flash, tint | Hard cut; fade hitam/putih sekali-sekala | Hard cut + 1 whip blur + 1 flash putih/light leak | Flash putih ×4, light leak, tint pink, **overlay awan** (siang→malam), crossfade | Hard cut + 1 zoom blur | Hard cut sahaja (komposit 2 lapisan) | **Hard cut dominan; blur-type transition di pertukaran babak** |
| BGM | Tiada | Perlahan | Perlahan | Sangat perlahan / mungkin tiada | Tiada dalam eksport (trending sound di TikTok) | Kemungkinan tiada | Muzik penuh, tiada voiceover | Perlahan di bawah suara | Tiada/sangat perlahan (kesimpulan) | **BGM lagu ditambah pengguna** (disahkan) — penuh masa highlight, perlahan bawah testimoni | Tiada | Tiada | **Suara sentiasa dominan; BGM perlahan atau tiada. Video tanpa suara: BGM royalty-free; jika tiada yang sesuai → SFX sahaja (pengguna tambah trending sound di TikTok)** |
| Struktur | Hook → senarai → twist | Masalah → Produk → Manfaat → CTA | Masalah → Punca → Demo → CTA | Masalah (lakonan) → Produk → Kempen → CTA | Unboxing → Guna → Manfaat → Proses | POV → Keperluan → Produk → Ciri → Harga → Varian → CTA | Ikut aturcara acara | Masalah/soalan → lokasi/brand → produk + harga → CTA | Hook harga → model → luar → interior → kegunaan ✅ → tawaran → slot terhad | **Highlight majlis (bukti kerja) → testimoni pengantin/rakan (bukti sosial)** | Hook produk → masalah (anak/sekolah) → title → varian → ciri → bonus → CTA | Hook kesilapan → title siri → produk → langkah 1–4 → troubleshooting → CTA siri seterusnya | **Masalah → Produk/solusi → Bukti/demo → CTA** |
| Ending | Cut hitam | Cut hitam + fade | Cut hitam + ding | Impact + cut hitam | Splash hitam + ding | Cut hitam + ding | Fade ke hitam | Hitam (S10, S12) / tiada (S11) / putih (S13) | Tiada (berhenti pada "berminat", mungkin terpotong) | Pudar ke krim/peach | Cut hitam 0.8 s | Kad akhir Instagram (platform) | **Cut ke hitam (+ SFX/fade)** |

**Pemerhatian:**
- **S16 (BettyRahmad, jam tangan budak dalam kereta):** kreator **BettyRahmad kini 3 sample (S5, S6, S16)** — kemungkinan kreator tetap pengguna. Mengesahkan gaya lalai: **caption karaoke putih + perkataan aktif kuning ±48 px** (R16/R62), hook produk terus di tangan (R45), jump cut ketat + extreme close-up ke lensa (R6/R7), satu zoom blur (R53), tiada BGM (R55), cut hitam (R12). Baharu: **label warna varian diwarnakan ikut warna sendiri** dan **CTA "CHECKOUT SEKARANG!" + tape kuning** (pilihan R80 — tanya ikut job, Claude cadang dulu). −19.5 LUFS/+0.5 dBFS & ±7 SFX tidak dipelajari (R14, R65).
- **S17 (@abbeyyung, tutorial serum, English):** format baharu **tutorial green-screen** — presenter cut-out di bawah bercakap sepanjang video atas B-roll demo sepadan ayat, **teks langkah bernombor di atas** (ganti caption karaoke), kad title siri berjenama + papan produk, tiada SFX/BGM. **Format green-screen diterima untuk klien (R78)**; gaya teks (karaoke vs langkah bernombor) **tanya setiap job (R79)**; kad title siri = pilihan R80 (Claude cadang dulu). Kad akhir Instagram = platform, bukan gaya.
- **S15 (promo servis Emcee Medina, majlis resepsi):** genre **promosi servis emcee** kini ada 2 rujukan (edit pengguna raya "Emcee Hafiz" + S15) — pattern berulang: **header tetap nama majlis (serif) + branding emcee kecil + flash/light leak + suasana majlis** (mengesahkan R38–R42). Baharu: **segmen testimoni klien** selepas highlight (pengantin → pasangan → rakan, soalan "So far emcee macam mana?") dengan caption ayat bertambah, dan nama pengantin skrip di bawah header. Branding ±93% & −8.2 LUFS tidak dipelajari (X6, R14).
- **S14 (sewa kereta mewah, sampel potential client):** genre servis baharu — presenter sebelah produk besar + B-roll ciri yang sepadan dengan setiap perkataan (menguatkan R37). Caption **satu perkataan di ATAS** kerana separuh bawah frame dipenuhi kereta (alternatif kepada caption bawah R16/R62 — pilihan R81f, Claude cadang dulu). Grafik minimum; label kegunaan kuning ✅ satu demi satu. Hook "Nampak macam X, tapi…" = kenyataan + twist harga (selari R45/R56).
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
- **UGC bercakap (job herba-headspa, 2026-11-13):** suara **asal** (tiada denoise/percepat, R61); caption ±48 px digeser kiri supaya tak bertindih butang TikTok (R62); callout ikut masa subtitle (R63); filter ringan sahaja (R64); Claude hantar video **bersih tanpa SFX/BGM** + jadual masa SFX — pengguna tambah sendiri (R65, R66). Tiada BGM lalai kekal (R55).
- **Video kenangan / pemandangan (job kenangan-airterjun, 2026-11-14):** tanya foto klien awal (R67); foto sebagai bookend dengan light leak masuk/keluar sahaja (R68–R70); bunyi alam diperlahankan untuk BGM pengguna (R71).
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
| **Sample 14** | Iklan sewa kereta mewah (Mercedes CLA) — presenter sebelah kereta, hook twist harga, B-roll ciri ikut perkataan, **caption 1 perkataan putih di atas**, label kuning ✅ (Content/Date/Business Meeting), whip blur + flash putih, CTA slot terhad | [sample-14/](sample-14/README.md) |
| **Sample 15** | Promo servis emcee (Emcee Medina, majlis resepsi) — **highlight majlis → testimoni pengantin/rakan**, header tetap serif krim "Majlis Resepsi" + nama pengantin skrip, branding emcee kecil, flash putih/light leak/overlay awan, caption ayat bertambah (testimoni sahaja), BGM lagu (pengguna) di-duck bawah testimoni | [sample-15/](sample-15/README.md) |
| **Sample 16** | UGC review jam tangan budak dalam kereta (BettyRahmad) — hook produk di tangan, **caption karaoke putih + kuning**, title serif + skrip + pill "Tengok Beg Kuning!", **label warna varian bubbly ikut warna** (PINK/PUTIH/GREEN), ✓ MATERIAL SILICONE, CTA "CHECKOUT SEKARANG!" + tape kuning, 1 zoom blur, cut hitam | [sample-16/](sample-16/README.md) |
| **Sample 17** | Tutorial edukasi **green-screen** (English, @abbeyyung) — presenter cut-out di bawah atas B-roll demo, hook "❌ I NEVER DO THIS…", **teks langkah bernombor di atas**, kad title siri + papan produk krim-pink, tiada SFX/BGM | [sample-17/](sample-17/README.md) |

### Nama fail dalam Google Drive ≠ nombor Sample dalam repo

Folder Drive sample: https://drive.google.com/drive/folders/1lFhA17JXB5XjRyRc5Aezp6wnJvucvkFa — padankan ikut **ID fail**, bukan nama.

| Nama dalam Drive | Dalam repo |
|---|---|
| Sample 1–5 | Sample 1–5 |
| Sample 6 | **Sample 16** |
| Sample 7 | Edit pengguna periuk → `comparisons/2026-11-07-periuk/` |
| Sample 8 | Sample 6 |
| Sample 9–15 | Sample 7–13 |
| Sample 16 | **Sample 17** |
| Sample 17 | Edit pengguna kenangan-airterjun → `comparisons/2026-11-14-kenangan-airterjun/` |
| Sample 18 | Sample 14 |
| Sample 19 | Sample 15 |
