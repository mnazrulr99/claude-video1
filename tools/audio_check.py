#!/usr/bin/env python3
"""Semak audio SEBELUM edit (R23). Jika terlalu perlahan/senyap -> BERHENTI dan beritahu pengguna.

Guna: python3 -I tools/audio_check.py <video>
Ukur: kelantangan bersepadu (LUFS), puncak, % masa senyap (< -50 dBFS), dan segmen senyap panjang (> 2 s).
Keputusan: OK / AMARAN / BERHENTI (kod keluar 0 / 1 / 2).
"""
import json, re, subprocess, sys
v = sys.argv[1]
probe = subprocess.run(["ffprobe","-v","error","-select_streams","a","-show_entries","stream=codec_name,channels,sample_rate",
                        "-of","json",v],capture_output=True,text=True).stdout
if not json.loads(probe).get("streams"):
    print("KEPUTUSAN: BERHENTI — video TIADA trek audio."); sys.exit(2)
dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",v],capture_output=True,text=True).stdout)
eb = subprocess.run(["ffmpeg","-hide_banner","-i",v,"-vn","-af","ebur128=peak=true","-f","null","-"],capture_output=True,text=True).stderr
I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", eb)[-1]); tp = re.findall(r"Peak:\s+(-?[\d.inf]+) dBFS", eb)
peak = float(tp[-1]) if tp and tp[-1] not in ("-inf",) else -120.0
sd = subprocess.run(["ffmpeg","-hide_banner","-i",v,"-vn","-af","silencedetect=noise=-50dB:d=0.3","-f","null","-"],capture_output=True,text=True).stderr
starts = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", sd)]
ends = [(float(e), float(d)) for e, d in re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", sd)]
if len(starts) > len(ends): ends.append((dur, dur - starts[-1]))
silent = sum(d for _, d in ends); long_sil = [(round(e-d,1), round(e,1)) for e, d in ends if d > 2.0]
pct = 100 * silent / dur if dur else 0
print(f"Durasi: {dur:.1f}s | Kelantangan: {I:.1f} LUFS | Puncak: {peak:.1f} dBFS | Senyap: {pct:.0f}% ({silent:.1f}s)")
if long_sil: print("Senyap panjang (>2s):", ", ".join(f"{a}-{b}s" for a, b in long_sil))
issues, warn = [], []
if I < -35 or peak < -20: issues.append(f"audio TERLALU PERLAHAN ({I:.1f} LUFS, puncak {peak:.1f} dBFS)")
elif I < -28: warn.append(f"audio agak perlahan ({I:.1f} LUFS) — boleh dikuatkan, tapi semak bunyi bising")
if pct > 60: issues.append(f"{pct:.0f}% video SENYAP")
elif pct > 30 or long_sil: warn.append(f"{pct:.0f}% senyap / ada senyap panjang — semak sama ada sengaja")
if peak > -0.1: warn.append("puncak hampir 0 dBFS — mungkin clipping/pecah")
if issues: print("KEPUTUSAN: BERHENTI —", "; ".join(issues)); sys.exit(2)
if warn: print("KEPUTUSAN: AMARAN —", "; ".join(warn)); sys.exit(1)
print("KEPUTUSAN: OK"); sys.exit(0)
