# Arahan untuk Claude (projek editing video)

Repo ini menyimpan rujukan gaya editing video pengguna. **Baca `editing-styles/README.md` dahulu** sebelum
sebarang tugas editing atau analisis sample — ia mengandungi aliran kerja wajib, katalog gaya
(Sample 1, Sample 2, …), pattern bersama, citarasa pengguna dan pelajaran projek siap.
Untuk kerja teknikal (transkrip, potong, Remotion, audio, render), guna skill **`edit-video`**
(`.claude/skills/edit-video/SKILL.md`).

## Peraturan WAJIB pengguna (jangan langgar)

1. **Guna semua skill yang dah dipelajari** setiap kali edit video: katalog gaya (Sample 1–N), "Pattern Bersama",
   "Catatan citarasa pengguna", "Pelajaran projek siap" dan skill `edit-video`. Nyatakan dalam cadangan
   pattern/pelajaran mana yang digunakan.
2. **Selepas edit → beri PREVIEW (540p) + STORYBOARD IMEJ dulu.** **JANGAN render final** sebelum pengguna
   kata setuju/"render". Ulang preview + storyboard ikut komen sehingga setuju.
3. **Setiap kali editing habis (final dirender), simpan apa yang dipelajari** — sama macam belajar dari sample:
   - `projects/<nama>/README.md` (keputusan edit, EDL, versi, komen pengguna, kod/skrip, preview),
   - tambah baris dalam jadual **"Pelajaran projek siap"** + kemas kini **"Catatan citarasa pengguna"** /
     **"Pattern Bersama"** dalam `editing-styles/README.md`,
   - kemas kini skill `edit-video` jika ada teknik/pembetulan baharu.
   Commit & push.

Ringkasan aliran:
- Video mentah → analisis + transkrip → cadang gaya (guna skill lepas) → edit → **preview 540p + storyboard imej**
  → tunggu setuju → render final 1080×1920 → **simpan pelajaran**.
- Sample siap edit baharu (termasuk edit pengguna sendiri) → analisis penuh → `editing-styles/sample-N/`
  → kemas kini katalog & "Pattern Bersama".
- Balas dalam Bahasa Melayu santai, mesra.
