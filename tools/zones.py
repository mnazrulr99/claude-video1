#!/usr/bin/env python3
"""Peta ruang kosong: kesan MUKA (YuNet) dan PRODUK (warna HSV, saturasi tinggi) supaya tulisan tak menutupnya.

Guna: python3 -I tools/zones.py <video> <mula>:<tamat> [...] [--hsv h1,h2,smin,vmin] [--step 0.5] [--grid 12x16]
Untuk setiap selang: cetak peta grid (F=muka, P=produk, .=kosong) dan JSON kotak muka/produk (median merentas frame).
Nota: produk dikesan ikut warna — sesuaikan --hsv (H OpenCV 0-179). Jika latar sama warna, naikkan smin.
"""
import argparse, json, os, subprocess, sys
import numpy as np, cv2
cv2.setLogLevel(0) if hasattr(cv2, "setLogLevel") else None

ap = argparse.ArgumentParser()
ap.add_argument("video"); ap.add_argument("ranges", nargs="+")
ap.add_argument("--hsv"); ap.add_argument("--step", type=float, default=0.5); ap.add_argument("--grid", default="12x16")
a = ap.parse_args()
GX, GY = map(int, a.grid.split("x"))
MODEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "face_detection_yunet_2023mar.onnx")
W, H = map(int, subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                                "-of", "csv=p=0", a.video], capture_output=True, text=True).stdout.strip().split(","))
det = cv2.FaceDetectorYN.create(MODEL, "", (W, H), 0.85)

def grab(t):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", a.video, "-frames:v", "1", "-f", "rawvideo",
                          "-pix_fmt", "bgr24", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(H, W, 3) if len(raw) == W*H*3 else None

res = []
for r in a.ranges:
    s, e = map(float, r.split(":")); fmask = np.zeros((H, W), np.float32); pmask = np.zeros((H, W), np.float32); n = 0
    fboxes, pboxes = [], []; t = s
    while t <= e + 1e-6:
        im = grab(t); t += a.step
        if im is None: continue
        n += 1
        _, faces = det.detect(im)
        if faces is not None and len(faces):
            x, y, w, h = max(faces, key=lambda f: f[2]*f[3])[:4]
            b = [int(x - w*0.45), int(y - h*0.55), int(x + w*1.45), int(y + h*1.35)]  # tudung + dagu/leher
            fboxes.append(b); fmask[max(0,b[1]):b[3], max(0,b[0]):b[2]] += 1
        if a.hsv:
            h1, h2, smin, vmin = map(int, a.hsv.split(","))
            m = cv2.inRange(cv2.cvtColor(im, cv2.COLOR_BGR2HSV), (h1, smin, vmin), (h2, 255, 255))
            m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((21, 21), np.uint8))
            pmask += (m > 0)
            ys, xs = np.nonzero(m)
            if len(xs) > 5000:
                pboxes.append([int(np.percentile(xs, 1)), int(np.percentile(ys, 1)), int(np.percentile(xs, 99)), int(np.percentile(ys, 99))])
    med = lambda bs: [int(v) for v in np.median(np.array(bs), axis=0)] if bs else None
    grid = []
    for gy in range(GY):
        row = ""
        for gx in range(GX):
            ys, xs = slice(gy*H//GY, (gy+1)*H//GY), slice(gx*W//GX, (gx+1)*W//GX)
            f = fmask[ys, xs].mean() / max(n, 1); p = pmask[ys, xs].mean() / max(n, 1)
            row += "F" if f > 0.15 else ("P" if p > 0.12 else ".")
        grid.append(row)
    res.append(dict(range=[s, e], frames=n, face=med(fboxes), product=med(pboxes), grid=grid))
    print(f"== {s:.2f}-{e:.2f}s  face={med(fboxes)} product={med(pboxes)}", file=sys.stderr)
    for gy, row in enumerate(grid): print(f"  y{gy*H//GY:5d} {row}", file=sys.stderr)
print(json.dumps(res))
