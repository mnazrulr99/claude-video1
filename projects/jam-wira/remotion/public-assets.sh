#!/usr/bin/env bash
# Muat turun aset audio ke public/ (SFX: Mixkit Free License; BGM: Kevin MacLeod "Carefree", CC BY 4.0)
set -e; cd "$(dirname "$0")"; mkdir -p public/sfx public/fonts
for p in whoosh:1492 whoosh2:1490 pop:2357 poplight:3005 popclick:2364 ding:2870 confirm:2867 reward:952 sparkle:871 wand:3062 splash:1311 bubble:1317 tick:1061 knob:1064; do
  n=${p%%:*}; i=${p##*:}; curl -sSL -o public/sfx/$n.mp3 "https://assets.mixkit.co/active_storage/sfx/$i/$i-preview.mp3"; done
for p in impact:2903; do n=${p%%:*}; i=${p##*:}; curl -sSL -o public/sfx/$n.mp3 "https://assets.mixkit.co/active_storage/sfx/$i/$i-preview.mp3"; done
curl -sSL -o public/carefree.mp3 https://incompetech.com/music/royalty-free/mp3-royaltyfree/Carefree.mp3
# public/cut_video.mp4 & public/voice.wav dijana dari video mentah oleh ../scripts (cutplan.py + ffmpeg)
# V2 juga perlukan public/raw.mp4 (video mentah) untuk b-roll close-up + public/fonts/caveat700.woff2
