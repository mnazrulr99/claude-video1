# Templat job acara multi-klip (dari job Rumah Terbuka Aidilfitri, 2026-11-10)

Salin folder ini ke scratchpad, sunting untuk job baru. Klip input: `<dir_job>/v/c<N>.mp4`.

| Fail | Guna |
|---|---|
| `plan.py` | Pelan BEATS multi-klip (audio suara + shot B-roll per beat), GFX, zon caption (versi highlight bercaption) |
| `captions.py` | Caption 1–3 perkataan dari transkrip verbatim → timeline output (PHRASES = bilangan perkataan setiap paparan) |
| `base.py` | `python3 -I base.py <dir_skrip> <dir_job>` → potong setiap shot/audio berasingan + concat → `base.mp4` (laju: ±1 min) |
| `hf2.py` | Projek HyperFrames versi caption + pill + transition kilauan + BGM duck |
| `slides.py` / `slides_build.py` | **Slideshow** senyap/BGM: shot berselang crossfade + Ken Burns, title + kad akhir, BGM diselaraskan pada bar (R41, R44) |
| `../../music_raya.py` | Jana muzik raya ASAL (kompang + akordion + seruling, 120 BPM; 1 bar = 2 s) — `python3 -I tools/music_raya.py out.wav` |

Nota: jangan guna `trim` berulang pada input yang sama dalam satu filter_complex (sangat lambat) — potong shot satu-satu (cara `base.py`).
Laluan `hfinit` (output `npx hyperframes init`) dijangka bersebelahan `<dir_job>`; laluan SFX = `tools/sfx`.
