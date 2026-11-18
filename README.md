# World News — 18 November 2026 (one image)

Entry for the make.fun bounty
[news-image-20261118](https://make.fun/bounty/news-image-20261118):
"Sum up 18 November's world news in one image".

## The image

`entry.png` (1024×1024, PNG, under 1 MiB) is a five-panel news infographic
on a dark-navy front-page layout, headed **"WORLD NEWS — 18 NOVEMBER 2026"**.
Each panel pairs a large illustration with a short bold label so the day's
news is readable at a glance:

1. **APEC OPENS IN SHENZHEN** — the APEC summit opens in Shenzhen, China,
   shown as the city skyline with member flags and a summit stage.
2. **QUAD MEETS IN MANILA — XI–TRUMP–PUTIN SUMMIT SET FOR NOV 19** —
   Quad leaders unveil a new plan in Manila; Trump heads on to China; the
   first-ever Xi–Trump–Putin trilateral summit is set for 19 November in
   Shenzhen.
3. **IRAN DRONES STRIKE US RADAR IN BAHRAIN** — Iranian drones attack a US
   military radar system in Bahrain as Gulf tensions escalate.
4. **NORTH KOREA MISSILE INTO SEA OF JAPAN** — North Korea launches a
   ballistic missile into the Sea of Japan.
5. **CYCLONE AKVAN NEARS ANDHRA PRADESH** — Cyclone Akvan bears down on
   India's Andhra Pradesh coast.

## How the program works

`main.py` (Python 3.13, standard library only) deterministically copies the
bundled `entry.png` byte-for-byte to `/output/entry.png`. It makes no network
requests, uses no randomness and no time, so two runs produce identical
output bytes (verified by comparing SHA-256 hashes).

## Run it

```sh
python3 main.py   # writes /output/entry.png
```

## License

MIT — see `LICENSE`.
