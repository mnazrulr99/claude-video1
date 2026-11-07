# Projek: Jam Budak Wira (review UGC, Remotion)

**Status:** PREVIEW 540p sahaja — menunggu persetujuan pengguna sebelum render final 1080×1920.

- Video mentah: Google Drive `1us7ccW34K1LIIPguMhJArHhN4SRlxKKU` (720×1280, 87.5 s, talking-head dalam kereta, review jam analog budak warna hijau).
- Hasil potongan: **57.8 s** (buang ulangan & jeda janggal; disahkan dengan transkrip semula Whisper).
- Gaya asas: gabungan **Sample 1** (karaoke + punch-in) & **Sample 2/3** (UGC produk, title callout, CTA beg kuning).
- Fail: [`preview_540p.mp4`](preview_540p.mp4), [`storyboard.jpg`](storyboard.jpg) (zon merah = UI TikTok/IG).

## Hook
Dibuka dengan ayat paling kuat (kontra + relatable): **"Saya tak nak beli dia yang smartwatch. Saya nak cari yang dia boleh pakai pergi sekolah."**
→ crash zoom + flash, title "SMARTWATCH?" + stamp ❌ → bertukar "JAM BUDAK SEKOLAH ✅" → "Haa ni dia" (reveal + sparkle).

## Yang dibuang
"Tapi itulah, sekarang banyak jam smartwatch kan", "Korang tengok" (×2), "Dalam TikTok saya jumpa ya" (ulangan),
"Tengok…", "Haa water resistant" (ulangan), "So korang tengok", "Haa nampak tak, dia ada tulis" (ulangan),
"Haa tengok dia ada nombor", "Haa so yang ni siap ada nombor" (ulangan), "Haa sekejap lagi kita nak bagi dia pakai" (tak ditunjuk),
"Okay kalau mommies" (pembuka janggal) + semua jeda > 0.25 s.

## Susun atur & safe zone (1080×1920)
- Zon UI dielak: atas 0–220 px, bawah 1440–1920 px, kanan 140 px.
- Title/grafik atas: y≈250–380 (atas kepala). Badge/jam animasi: kiri x 54–340, y 450–760 (tepi muka, bukan atas muka).
- Caption karaoke: y≈1340 (bawah dagu), ALL CAPS Montserrat 900, putih + highlight **hijau mint #7CF29C** (ikut warna jam & "Wira suka green").
- Zoom: selang-seli 1.0/1.1 setiap potongan (sorok jump cut), punch-in pada "smartwatch" & "very good", origin pada muka.

## Audio
- Suara: highpass 85 Hz + denoise (afftdn) + compressor + loudnorm −15 LUFS.
- BGM: Kevin MacLeod – *Carefree* (CC BY 4.0 → **kredit wajib**: "Carefree" Kevin MacLeod (incompetech.com), Licensed under Creative Commons: By Attribution 4.0) pada ≈ −33 LUFS (18 dB bawah suara), fade in/out.
- SFX: Mixkit (Free License, tiada kredit) — whoosh, pop, ding, sparkle, water splash, clock tick, watch knob, reward chime.
- Master: limiter (peak −1.4 dBFS).

## Cara render semula
```bash
cd remotion && npm i && ./public-assets.sh   # + jana public/cut_video.mp4 & public/voice.wav (lihat scripts/)
npx remotion render src/index.ts JamWira out.mp4 --scale=0.5          # preview 540p
npx remotion render src/index.ts JamWira final.mp4                    # FINAL 1080×1920 (selepas setuju)
```
