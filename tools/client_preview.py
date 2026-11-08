#!/usr/bin/env python3
"""Hasilkan PREVIEW untuk klien: resolusi rendah + watermark "PREVIEW" (tidak boleh guna sebagai video akhir).

Guna: python3 -I tools/client_preview.py <video_input> <video_output> [--width 540] [--label "PREVIEW"]
      python3 -I tools/client_preview.py --image <storyboard.jpg> <output.jpg>   (watermark pada imej storyboard)
Watermark: SATU perkataan "PREVIEW" di tengah (condong, lutsinar ±43%). Tiada jalur/teks lain.
"""
import argparse, os, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument("input"); ap.add_argument("output")
ap.add_argument("--width", type=int, default=540); ap.add_argument("--label", default="PREVIEW")
ap.add_argument("--image", action="store_true", help="input ialah imej (storyboard)")
a = ap.parse_args()
FONT = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
if not os.path.exists(FONT):
    FONT = next((p for p in ["/Library/Fonts/Arial Bold.ttf", "C:/Windows/Fonts/arialbd.ttf",
                             "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"] if os.path.exists(p)), None)
def font(sz): return ImageFont.truetype(FONT, sz) if FONT else ImageFont.load_default()

def watermark(w, h):
    """Satu perkataan "PREVIEW" sahaja di tengah, condong sedikit, lutsinar."""
    wm = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    fs = max(24, w // 5); f = font(fs)
    txt = Image.new("RGBA", (w*2, fs*2), (0, 0, 0, 0)); d = ImageDraw.Draw(txt)
    d.text((w, fs), a.label, font=f, fill=(255, 255, 255, 110), stroke_width=max(2, fs//14), stroke_fill=(0, 0, 0, 70), anchor="mm")
    txt = txt.rotate(25, resample=Image.BICUBIC, expand=True)
    wm.alpha_composite(txt, ((w - txt.width)//2, (h - txt.height)//2))
    return wm

if a.image:
    im = Image.open(a.input).convert("RGBA")
    if im.width > 1600: im = im.resize((1600, round(im.height*1600/im.width)), Image.LANCZOS)
    out = Image.alpha_composite(im, watermark(im.width, im.height)).convert("RGB")
    out.save(a.output, quality=80); print("ok", a.output)
else:
    w = a.width
    h = int(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
        "-of", "csv=p=0", a.input], capture_output=True, text=True).stdout.strip().split(",")[1]) * w
    w0 = int(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width",
        "-of", "csv=p=0", a.input], capture_output=True, text=True).stdout.strip())
    h = (h // w0) // 2 * 2
    with tempfile.TemporaryDirectory() as td:
        png = os.path.join(td, "wm.png"); watermark(w, h).save(png)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.input, "-i", png, "-filter_complex",
            f"[0:v]scale={w}:{h}:flags=bicubic,format=yuv420p[v];[v][1:v]overlay=0:0",
            "-c:v", "libx264", "-crf", "30", "-preset", "medium", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", a.output], check=True)
    print("ok", a.output)
