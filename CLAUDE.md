# Arahan untuk Claude (projek editing video)

Repo ini menyimpan rujukan gaya editing video pengguna. **Baca `editing-styles/README.md` dahulu** sebelum
sebarang tugas editing atau analisis sample — ia mengandungi aliran kerja wajib, katalog gaya
(Sample 1, Sample 2, …), pattern bersama dan citarasa pengguna.

Ringkasan:
- Video mentah → analisis & cadang gaya → storyboard imej → tunggu setuju → baru render (ffmpeg).
- Sample siap edit baharu → analisis penuh → `editing-styles/sample-N/` → kemas kini katalog & "Pattern Bersama".
- Balas dalam Bahasa Melayu santai, mesra.

Skill tersedia (taip dalam Claude Code):
- `/edit-video <link video raw>` — prosedur penuh edit video (`.claude/skills/edit-video/SKILL.md`).
- `/sample-baru <link video siap edit>` — belajar & simpan gaya baharu (`.claude/skills/sample-baru/SKILL.md`).
