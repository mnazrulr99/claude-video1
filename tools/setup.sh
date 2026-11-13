#!/usr/bin/env bash
# Sediakan semua tool editing (cloud atau komputer pengguna). Selamat dijalankan berulang kali (skip yang dah ada).
# Guna: bash tools/setup.sh
set -u
ok(){ printf "  ✅ %s\n" "$1"; }; bad(){ printf "  ❌ %s\n" "$1"; MISSING=1; }
MISSING=0
echo "== Semak & pasang tool editing =="

command -v node >/dev/null && ok "Node $(node -v)" || bad "Node.js tiada (pasang Node LTS >= 22)"
command -v ffmpeg >/dev/null && ok "$(ffmpeg -version | head -1 | cut -d' ' -f1-3)" || bad "ffmpeg tiada"

PY=python3
for mod in "faster_whisper:faster-whisper" "cv2:opencv-python-headless" "PIL:pillow" "gdown:gdown" "numpy:numpy"; do
  m=${mod%%:*}; p=${mod##*:}
  if $PY -c "import $m" 2>/dev/null; then ok "$p"; else
    pip install -q "$p" 2>/dev/null || pip install -q --break-system-packages "$p" 2>/dev/null
    $PY -c "import $m" 2>/dev/null && ok "$p (baru dipasang)" || bad "$p gagal dipasang"
  fi
done
# PyAV lama boleh rosakkan faster-whisper (transcribe.py nyahkod guna ffmpeg, jadi selamat)

# Model Whisper (medium untuk Bahasa Melayu) — muat turun sekali, ±1.5 GB
$PY -c "from faster_whisper import WhisperModel; WhisperModel('medium', device='cpu', compute_type='int8')" 2>/dev/null \
  && ok "Model Whisper medium" || bad "Model Whisper medium gagal dimuat turun"

# HyperFrames (render grafik) — cache npx
npx -y hyperframes --version >/dev/null 2>&1 && ok "HyperFrames $(npx -y hyperframes --version 2>/dev/null | tail -1)" || bad "HyperFrames gagal"

# Model muka (zones.py) & SFX dalam repo
D="$(cd "$(dirname "$0")" && pwd)"
[ -f "$D/models/face_detection_yunet_2023mar.onnx" ] && ok "Model muka YuNet" || bad "tools/models/face_detection_yunet_2023mar.onnx tiada"
[ -f "$D/sfx/whoosh-soft.wav" ] && ok "SFX ($(ls "$D/sfx" | wc -l) fail)" || bad "tools/sfx tiada"

# Fon untuk caption/title
fc-list 2>/dev/null | grep -qi "Inter" && ok "Fon Inter" || echo "  ⚠️  Fon Inter tiada — guna fon tebal lain (cth. Arial Black / DejaVu Sans Bold)"

[ "$MISSING" = 0 ] && echo "== SEMUA SEDIA ✅ ==" || echo "== Ada yang belum sedia ❌ (lihat di atas) =="
