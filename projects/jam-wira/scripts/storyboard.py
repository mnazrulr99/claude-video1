"""Bina storyboard imej dari still Remotion (dengan overlay safe zone).
Guna: python3 -I storyboard.py <folder_still> <notes.json> <output.jpg> "<tajuk>"
notes.json = [["0.0s HOOK","Penerangan grafik/zoom","whoosh, pop"], ...] ikut susunan masa still (f_<masa>.png).
"""
import sys, json, glob
from PIL import Image, ImageDraw, ImageFont
folder, notes_p, out, title = sys.argv[1:5]
notes = json.load(open(notes_p))
files = sorted(glob.glob(folder + '/f_*.png'), key=lambda p: float(p.split('f_')[1][:-4]))
W, H, cols, pad, th = 270, 480, 7, 10, 150
rows = (len(files) + cols - 1) // cols
B = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; R_ = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font, small, big = ImageFont.truetype(B, 15), ImageFont.truetype(R_, 13), ImageFont.truetype(B, 20)
img = Image.new('RGB', (cols * (W + pad) + pad, 70 + rows * (H + th + pad)), (18, 18, 18))
d = ImageDraw.Draw(img)
d.text((pad, 15), title, font=big, fill=(124, 242, 156))
for i, (p, (t, g, s)) in enumerate(zip(files, notes)):
    x = pad + (i % cols) * (W + pad); y = 70 + (i // cols) * (H + th + pad)
    img.paste(Image.open(p).convert('RGB').resize((W, H)), (x, y))
    d.rectangle([x, y + H, x + W, y + H + th], fill=(35, 35, 35))
    d.text((x + 6, y + H + 6), t, font=font, fill=(255, 210, 63))
    d.multiline_text((x + 6, y + H + 28), g, font=small, fill=(255, 255, 255), spacing=3)  # DejaVu tiada emoji: tulis teks biasa
    d.text((x + 6, y + H + th - 22), 'SFX: ' + s, font=small, fill=(124, 242, 156))
img.save(out, quality=88)
