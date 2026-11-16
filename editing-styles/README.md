# Katalog Gaya Editing

Semua editing dibuat & dirender terus oleh Claude (ffmpeg) — pengguna tak guna sebarang app editing.

## Aliran kerja WAJIB (setiap job editing)

> **SOP penuh dengan pintu kelulusan: [SOP.md](SOP.md).** Ringkasan:

1. Pengguna hantar **video mentah** (+ gambar produk jika ada).
2. **Semak audio dahulu** (`tools/audio_check.py`) — jika terlalu perlahan/senyap → berhenti & beritahu pengguna (R23).
2b. **Analisis SEMUA bahan** (raw, gambar, logo, brief; video bercakap → transkrip verbatim serentak dengan analisis visual, diguna semula di langkah 3) → cadang hanya gaya yang bahan mampu sokong, dengan bukti + apa tak sesuai + bahan tambahan (R84, SOP Fasa 2b). Pengguna pilih arah.
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

_Berdasarkan Sample 1–26 (S23–S26 satu lajur — talking head kreator/edukasi repost TikTok; S18 & S20 satu siri testimoni vendor acara — satu lajur; S7–S9 satu siri highlight acara; S10–S13 diringkaskan sebagai satu lajur kerana gaya caption & grafik sama):_

| Pattern | S1 (edukasi) | S2 (iklan UGC) | S3 (iklan feminin) | S4 (skit brand) | S5 (showcase senyap) | S6 (UGC rumah, POV) | S7–S9 (highlight acara, landscape) | S10–S13 (UGC review/haul/vlog/premis) | S14 (sewa kereta) | S15 (promo emcee) | S16 (UGC jam, kereta) | S17 (tutorial green-screen, EN) | S18/S20 (testimoni korporat, vendor acara) | S19 (UGC skincare estetik, tanpa suara) | S21 (iklan produk showroom) | S22 (highlight sekolah 9:16) | S23–S26 (talking head kreator/edukasi, repost TikTok) | Kesimpulan  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Format | 9:16 | 9:16, 60 fps | ≈9:16 | ≈9:16 | 9:16 | 9:16 | **Landscape 1920×1080** | 9:16 | 9:16 (576×1024 repost TikTok) | 9:16 HDR (HLG), 72.5 s | 9:16, 55.8 s | 9:16, 122.8 s | 9:16, 46.6 s / 44.8 s | 9:16, 48.5 s | ≈9:16 4K 60 fps, 31.2 s | 9:16 HDR (HLG), 49.3 s | 9:16 576×1024; 21.5–75 s; S26 24 fps | **9:16 untuk UGC/TikTok; landscape 1920×1080 untuk highlight acara** (tanya platform)  |
| Hook | Flash + B&W, soalan | Produk + colour bars/beep | Title soalan + sticker emoji | Makan ASMR tanpa caption | Unboxing + header + sparkle | POV skit + teks "Pov:" + sparkle | Logo intro / drone / momen VIP | Title soalan bubbly / teaser / skit / POV pintu | Kenyataan + twist harga, presenter sebelah kereta → punch-in | Emcee beraksi dengan mikrofon + header majlis ditaip | Produk terus di tangan + ciri ("water resistant tau") + whoosh reveal kotak | "❌ I NEVER DO THIS…" + kenyataan kesilapan terbesar | Petikan lucu dari tengah temubual (+ ikon "reverse" S20) → **colour bars + beep** | Close-up masalah kulit + ayat formula "makeup + sweat + oil = breakouts" | Soalan harga "Betul ke dengan RM20…?" + pill harga pop | Glitch neon → papan tanda sekolah | Kinetic title ditaip + flash (S23); kata kunci gergasi (S24); effect "orbit" + title tetap (S25); title editorial skrip + kuning gergasi (S26) | **Hook < 3.5 s: visual luar biasa/menarik + SFX; soalan atau aksi.** Colour bars + beep selepas hook kini dalam 4 rujukan (S2, Rejuran, S18, S20 — R46) |
| Potongan | Jump cut laju | Jump cut 1–3 s | Take lebih panjang masa demo | Take lakonan 2–4 s | Klip 2–12 s ikut proses | Jump cut ketat | Montaj ±0.6 s/klip ikut beat | ±1.5–1.8 s/klip (S12 lebih perlahan) | ±2.2 s/klip; B-roll ±1.2–1.5 s ikut perkataan | ±2.2 s; take panjang emcee/testimoni, montaj B-roll 1–3 s | Jump cut ±1.6 s/klip | B-roll ±3.7 s/klip; presenter atas satu take | ±2.2 s (S18, ramai orang); take tunggal + kad soalan ±10 s (S20) | Jump cut rutin ±1–1.5 s | ±1.5–3 s; gimbal push-in ganti potongan | Montaj ±0.6–1.2 s ikut beat | Take tunggal + grafik (S23–S25); cut on motion ±0.6–3 s multi-angle (S26) | **Buang jeda; laju, perlahan sedikit masa demo** |
| Framing | Punch-in 2–4 s | Punch-in ekstrem | Produk rapat ke lensa + wide | Medium + top-down + crash zoom | Close-up tangan, top-down, split 3 panel | Produk ditolak ke lensa, extreme close-up | Gimbal, drone, push-in sinematik | Muka ↔ close-up produk/makanan, POV masuk kedai | Wide presenter+kereta ↔ B-roll detail (rim, interior) | Handheld tetamu ↔ medium emcee ↔ selfie testimoni | Medium kereta ↔ extreme close-up produk ke lensa | Presenter cut-out bawah ±55% atas B-roll demo | Medium statik; 1 punch-in (S20) | Selfie dekat + produk rapat ke lensa + tekstur di tapak tangan | Wide presenter ↔ makro produk (drum, panel, lencana) | Lensa lebar 0.5×, sudut rendah dekat kanak-kanak | Medium statik; cut-out presenter atas grid/latar maya (S23, S25); multi-angle sinematik (S26) | **Variasi framing kerap** |
| Caption | ALL CAPS, teks kuning | ALL CAPS, kotak lime | ALL CAPS condensed, teks pink | ALL CAPS, kotak biru | Tiada (tiada suara) | ALL CAPS, kotak lime | Tiada (tiada suara) | ALL CAPS 2 baris, tukar warna teks **merah/hijau/kuning berselang** + emoji kecil | **1 perkataan ALL CAPS putih, ±22% dari ATAS** (langit), tiada highlight | Testimoni sahaja: **sentence case, perkataan bertambah** jadi ayat 3–4 baris, krim, ±75%, ≈36 px | ALL CAPS putih + **perkataan aktif kuning**, ≈48 px, ±78% | Tiada karaoke — **teks langkah bernombor** sentence case di atas ±22% | Karaoke ALL CAPS condensed putih + **perkataan aktif oren** (warna jenama), ≈52 px, ±78% | Tiada (tiada suara) — **teks cerita serif kecil sentence case ≈28 px** (terlalu kecil, X5) | Karaoke ALL CAPS bulat putih + **kotak gradient biru→teal**, ≈58 px, ±78% | Tiada | Karaoke ALL CAPS + kotak biru (S23); **hierarki kata kunci gergasi + kecil** (S24); lowercase + frasa kuning (S25); subtitle serif kuning kecil (S26) | **Jika ada suara:** karaoke word-by-word, ALL CAPS, putih + 1 warna highlight (teks/kotak) ikut brand/mood, 60–78% dari atas (S14: caption di atas ±22% bila produk besar penuhi bahagian bawah — R81f). **Tiada suara:** tiada caption, guna teks callout  |
| Title/grafik | Title + ❌/‼️ | Title + ❌/✅ + label pelbagai | Serif + skrip, 🎀 ✅, sticker | Title gaya brand + doodle animasi | Header tetap + checklist ✅ + sticker sudut | Search-bar pill, tulisan tangan, ✅, sparkle | Logo acara tetap (atas tengah / bawah kanan) | Screenshot harga produk, logo kedai/app + label kempen, poster promo, pill URL, teks skrip elegan | Label kegunaan **kuning + ✅** bertukar satu demi satu; tiada title/logo | **Header tetap** serif krim "Majlis Resepsi" + nama pengantin skrip putih (kanan atas) + branding "Emcee Medina" bawah | Title serif + skrip + pill "Tengok Beg Kuning!", label warna bubbly ikut warna varian, ✓ ciri, CTA tape kuning | Kad title siri serif merah atas krim-pink + papan cadangan produk | **Kad soalan atas latar blur** (menaip) + **kad akhir vendor** (logo, CTA DM, search bar URL, lencana HRDC) | Label produk skrip + anak panah, senarai manfaat bertitik, **"Day 1" → "Day 14"** | Pill harga hijau, nama produk menaip + sparkle, teks 3D, **callout berpenunjuk**, label ✅ menaip + kursor, **CTA cop condong** | **Logo program merah condong tetap** di atas (±4–8%) | Hadiah PNG pop bertimbun (S23); B-roll stok jalur atas feather (S24); katalog 17 effect (S25); **teks di belakang subjek** (S25, S26) | **Title poin utama + emoji/doodle; gaya title ikut brand/mood** |
| SFX | Pop/ding/impact | Beep/chime/click/ding | Sparkle + pop berulang + ASMR | Whoosh/ding + ASMR + foley | Sparkle/ding sahaja, selebihnya senyap | Sparkle/ding/riser setiap label | Tiada ketara (muzik dominan) | Tidak ketara | Ding pada label ✅, whoosh pada flash (kesimpulan) | Tiada ketara (BGM dominan) | Whoosh + sparkle + ding setiap label + chime CTA (±7) | Tiada | Beep colour bars sahaja | Chime ±5 pada produk/manfaat | Sparkle pada nama produk + nada penutup | Tiada | Whoosh/pop pada teks (S23, S26 — kesimpulan); tiada ketara (S24, S25) | **Setiap grafik = SFX; kekalkan bunyi ASMR/foley produk** |
| Transition | Hard cut | + 2 khas | + 3 khas (blur, mirror, splash) | + whip/zoom blur, crash zoom | Splash cecair putih/hitam, split screen | Kad foto berpusing, brush stroke, B&W reaksi | Banyak: light leak, kolaj, bingkai foto, filem, glitch, flash, tint | Hard cut; fade hitam/putih sekali-sekala | Hard cut + 1 whip blur + 1 flash putih/light leak | Flash putih ×4, light leak, tint pink, **overlay awan** (siang→malam), crossfade | Hard cut + 1 zoom blur | Hard cut sahaja (komposit 2 lapisan) | Hard cut + colour bars + blur (kad soalan) | Hard cut + 1 light leak (lompat masa) | Bingkai putih, dip gelap, panel condong (3×) | ±7: flash cyan/putih/magenta, B&W, panel condong, koyak kertas, light leak | Flash putih (S23); hard cut (S24); zoom-through, pull-back, vertigo (S25); cut on motion + blur teks (S26) | **Hard cut dominan; blur-type transition di pertukaran babak**; highlight acara & iklan produk "tech" boleh lebih banyak (S21, S22) |
| BGM | Tiada | Perlahan | Perlahan | Sangat perlahan / mungkin tiada | Tiada dalam eksport (trending sound di TikTok) | Kemungkinan tiada | Muzik penuh, tiada voiceover | Perlahan di bawah suara | Tiada/sangat perlahan (kesimpulan) | **BGM lagu ditambah pengguna** (disahkan) — penuh masa highlight, perlahan bawah testimoni | Tiada | Tiada | Perlahan bawah suara (kesimpulan); penuh di kad akhir | Lembut (piano/lo-fi) | Ada di bawah VO (kesimpulan) | Lagu rentak penuh | Berterusan bawah suara (S23, S26); tiada/sangat perlahan (S24, S25) | **Suara sentiasa dominan; BGM perlahan atau tiada. Video tanpa suara: BGM royalty-free; jika tiada yang sesuai → SFX sahaja (pengguna tambah trending sound di TikTok)** |
| Struktur | Hook → senarai → twist | Masalah → Produk → Manfaat → CTA | Masalah → Punca → Demo → CTA | Masalah (lakonan) → Produk → Kempen → CTA | Unboxing → Guna → Manfaat → Proses | POV → Keperluan → Produk → Ciri → Harga → Varian → CTA | Ikut aturcara acara | Masalah/soalan → lokasi/brand → produk + harga → CTA | Hook harga → model → luar → interior → kegunaan ✅ → tawaran → slot terhad | **Highlight majlis (bukti kerja) → testimoni pengantin/rakan (bukti sosial)** | Hook produk → masalah (anak/sekolah) → title → varian → ciri → bonus → CTA | Hook kesilapan → title siri → produk → langkah 1–4 → troubleshooting → CTA siri seterusnya | Hook → interrupt → soalan → perkenalan → soalan/jawapan ×3 → montaj 1 perkataan → kad akhir vendor | Masalah → produk → manfaat → cerita → produk 2 → Day 1 → Day 14 → packshot | Hook harga → nama → kapasiti → ciri → manfaat ✅ → CTA promo | Lokasi → aktiviti → teruja → perlawanan → hadiah | Hook → hadiah (S23); masalah → punca → rawatan (S24); senarai effect → teaser → CTA komen (S25); hook → teori → demo → hasil → CTA komen (S26) | **Masalah → Produk/solusi → Bukti/demo → CTA** |
| Ending | Cut hitam | Cut hitam + fade | Cut hitam + ding | Impact + cut hitam | Splash hitam + ding | Cut hitam + ding | Fade ke hitam | Hitam (S10, S12) / tiada (S11) / putih (S13) | Tiada (berhenti pada "berminat", mungkin terpotong) | Pudar ke krim/peach | Cut hitam 0.8 s | Kad akhir Instagram (platform) | Kad akhir vendor (pastel) — tiada hitam | Packshot + ayat ♡ → hitam | Hitam + nada penutup | Light leak → merah → hitam | CTA komen kata kunci ("STUDIO", "COLLEGE") + UI komen/profil (S25, S26); kad akhir TikTok = platform | **Cut ke hitam (+ SFX/fade)**; promo vendor/servis → **kad akhir jenama** (logo + CTA + URL, S18/S20) |

**Pemerhatian:**
- **Sample 23–26 (folder Drive 2026-11-16, kumpulan ke-2, 4 video — semua repost TikTok 576×1024):** tema bersama = **talking head yang "dihidupkan" dengan grafik/tipografi, bukan potongan**.
  - **S23 + S24 (editor "by.miyun", BM):** **editor lain (bukan pengguna — disahkan)**, portfolio (video dalam kad bucu bulat atas latar kabur — lapisan pameran, bukan gaya). S23: kinetic title hook, flash putih, **presenter cut-out atas grid + PNG hadiah pop bertimbun**, caption kotak biru. S24: **caption hierarki kata kunci gergasi + perkataan kecil**, **B-roll stok di ⅓ atas dengan feather** (pakar sentiasa di skrin). → R83 (a)–(e).
  - **S25 (@tenfoldmarc, EN):** **katalog 17 effect yang dibina Claude** (orbit, ui world, frame break, checklist, headline wall, chart grow, pull-back reveal, paper cut, doodle boil, vertigo, cover story, glass type…) — rujukan idea effect untuk R60. → R83 (f), kod E1–E17.
  - **S26 (@omgadrian, EN):** tipografi editorial **skrip putih + condensed kuning gergasi**, **teks di belakang subjek**, blur-in/out, cut on motion multi-angle. → R83 (g)–(i).
  - **Pattern berulang baharu:** (1) **teks/title di belakang subjek** (S25 cover story, S26) — perlukan cut-out; (2) **CTA "komen kata kunci"** (S25 "STUDIO", S26 "COLLEGE") untuk kreator/servis; (3) **penekanan melalui SAIZ perkataan** (S24, S25, S26) sebagai alternatif kepada warna highlight.
- **Sample 18–22 (folder Drive 2026-11-16, 6 video):** video ke-5 (Manhattan Fish Market) ialah **duplikat tepat Sample 10** (frame identik) — tidak disimpan semula.
  - **S18 + S20 (engagelife × Mars, testimoni team-building):** genre baharu **testimoni peserta untuk vendor acara korporat** — **kad soalan temubual atas latar blur** sebagai pemisah bab, hook petikan lucu + **colour bars + beep** (R46 kini 4 rujukan → pattern kuat selera pengguna), caption putih + **warna jenama** (oren), **kad akhir vendor** (logo, CTA DM, search bar URL menaip, lencana HRDC). Selari struktur "bukti sosial" S15/R73. → R82 (tanya ikut job).
  - **S19 (Eucerin, UGC skincare tanpa suara):** sub-jenis "aesthetic diary" — teks serif kecil sentence case (saiz terlalu kecil — X5), label produk skrip + anak panah, senarai manfaat bertitik, **Day 1 → Day 14** dengan satu light leak untuk lompat masa, BGM lembut + chime hanya pada produk (selari R48/R65). → R82 (tanya ikut job).
  - **S21 (Coway, iklan showroom):** grafik "tech" padat — pill harga pop (R63), nama produk menaip + sparkle, **callout berpenunjuk spec**, label ✅ menaip dengan kursor (keluarga R18/R19), **CTA cop condong + gema teks**, caption kotak gradient biru-teal (keluarga P15). −7.8 LUFS & 4K 60 fps tidak dipelajari (X4, X11). → R82 (tanya ikut job).
  - **S22 (SKeSAS, highlight sekolah 9:16):** mengesahkan kategori highlight acara (R30–R42) dalam **9:16**: logo program condong tetap di atas, montaj ±0.6–1 s ikut beat, muzik penuh, tiada caption/SFX, transition pelbagai jenis. Logo ±4–8% terlalu tinggi (zon UI atas). → R82 (tanya ikut job).
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
| **Sample 18** | Testimoni peserta team-building (engagelife × Mars, 5 orang) — hook petikan lucu + **colour bars/beep**, **kad soalan atas latar blur**, caption karaoke putih + **oren jenama**, montaj jawapan 1 perkataan, **kad akhir vendor** (logo, CTA DM, search bar URL, HRDC) | [sample-18/](sample-18/README.md) |
| **Sample 19** | UGC skincare **tanpa suara** "aesthetic diary" (Eucerin) — teks serif kecil sentence case, label produk skrip + anak panah, senarai manfaat bertitik, **Day 1 → Day 14** + light leak, BGM lembut + chime pada produk | [sample-19/](sample-19/README.md) |
| **Sample 20** | Siri S18 — testimoni **seorang** peserta, take tunggal + 4 kad soalan blur, hook + **ikon "reverse" oren**, colour bars SMPTE + beep, 1 punch-in, kad akhir vendor | [sample-20/](sample-20/README.md) |
| **Sample 21** | Iklan produk showroom (Coway washer dryer, 31 s) — caption karaoke + **kotak gradient biru-teal**, pill harga RM20, nama produk menaip + sparkle, teks 3D, **callout berpenunjuk**, label ✅ menaip + kursor, transition bingkai/panel, **CTA cop condong** | [sample-21/](sample-21/README.md) |
| **Sample 22** | Highlight program sukan sekolah **9:16** (SKeSAS) — **logo condong tetap di atas**, montaj ±0.6–1 s ikut beat, muzik penuh, tiada caption, flash warna/B&W/panel condong/koyak kertas/light leak | [sample-22/](sample-22/README.md) |
| **Sample 23** | Pengumuman kontes talking head BM (by.miyun) — **kinetic title hook** + flash putih, **presenter cut-out tepi kertas atas grid biru**, **PNG hadiah pop bertimbun** (motosikal → iPhone → laptop), caption ALL CAPS + kotak biru | [sample-23/](sample-23/README.md) |
| **Sample 24** | Doktor talking head BM (by.miyun) — **caption hierarki: kata kunci ALL CAPS gergasi + perkataan kecil**, **B-roll stok di ⅓ atas dengan feather**, satu take | [sample-24/](sample-24/README.md) |
| **Sample 25** | "17 video effects Claude can create" (EN) — **katalog effect bernombor** (orbit, ui world, frame break, checklist, headline wall, chart grow, pull-back reveal, paper cut, doodle boil, vertigo, cover story, glass type…), CTA komen "STUDIO" | [sample-25/](sample-25/README.md) |
| **Sample 26** | Tutorial kreator sinematik (EN) — **title editorial skrip putih + condensed kuning gergasi**, **teks di belakang subjek**, blur-in/out, cut on motion multi-angle, subtitle serif kuning, CTA komen "COLLEGE" | [sample-26/](sample-26/README.md) |

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

### Folder Drive 2026-11-16 (`1OfFviyqvOR45oq_iOwwc4XFs5seswRij`) — kumpulan 1 bernama "Document from ~n"; kumpulan 2 bernama hash md5 (`562ca19d….mp4` dll.)

| ID fail Drive | Dalam repo |
|---|---|
| `14GeVuAzYXKv8nhu5KlzA6u5LLopwwbz4` | **Sample 18** |
| `1HhvY3vqnHMi9jy0snigrO1baRXF8gOcY` | **Sample 19** |
| `1UjAyNQcTqmdkaIcw--a70z6nGnIX8x0e` | **Sample 20** |
| `1aL6oepCgtS01Oz_ipzhhHu7y7ECyz-I9` | **Sample 21** |
| `1nolVYUoKcZScIX1slNhIeIaKMYTmxLcN` | Duplikat **Sample 10** (tidak disimpan semula) |
| `1tzcXuw7YVZrMAYxUnaq-TnYyZUjhTSz8` | **Sample 22** |
| `1XCkwK0XHUu-lYXiDkiyggYGLcBUsDMlS` | **Sample 23** (kumpulan ke-2) |
| `1gEfDd0uMEBdYhRm1HHIG4uubbxnopBDH` | **Sample 24** |
| `1ufFLSMST_ByWGWR3vgX_3IBqw1KA0vbQ` | **Sample 25** |
| `1UQpzsQK3Jv_Qjt6jnK2P6mSrYnq5oSb1` | **Sample 26** |
