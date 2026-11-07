#!/usr/bin/env python3
"""Transkrip audio/video dengan masa setiap perkataan (untuk caption karaoke).

Guna: python3 -I tools/transcribe.py <video_atau_audio> [output.json] [--model medium] [--lang ms]
Audio dinyahkod dengan ffmpeg (elak isu versi PyAV dengan faster-whisper).
Output JSON: [{"start","end","text","words":[{"word","start","end","prob"}]}]
"""
import argparse, json, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

p = argparse.ArgumentParser()
p.add_argument("input"); p.add_argument("output", nargs="?")
p.add_argument("--model", default="medium"); p.add_argument("--lang", default="ms")
a = p.parse_args()

raw = subprocess.run(["ffmpeg", "-v", "error", "-i", a.input, "-vn", "-ac", "1", "-ar", "16000",
                      "-f", "f32le", "-"], capture_output=True, check=True).stdout
audio = np.frombuffer(raw, np.float32)

model = WhisperModel(a.model, device="cpu", compute_type="int8")
segs, _ = model.transcribe(audio, language=a.lang, word_timestamps=True, vad_filter=True)
out = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(),
        "words": [{"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2),
                   "prob": round(w.probability, 2)} for w in (s.words or [])]} for s in segs]
for s in out:
    print(f"[{s['start']:6.2f}-{s['end']:6.2f}] {s['text']}", file=sys.stderr)
if a.output:
    json.dump(out, open(a.output, "w"), ensure_ascii=False, indent=1)
else:
    print(json.dumps(out, ensure_ascii=False))
