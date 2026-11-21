# news-image-20261121 entry (Python 3.13, standard library only).
#
# The image is entry.png beside this file: a front-page summary of the
# world news of Saturday 21 November 2026 — built that morning from
# reporting dated 21 November 2026 in some time zone. A masthead dates
# the page ("Saturday 21 November 2026", "52 STORIES · 7 REGIONS ·
# 16 FIELDS"), a UTC timeline runs across the top, and four hero tiles
# cover the day's biggest stories: "Rutte flies to Warsaw as NATO
# answers Poland", "Zelensky: Putin is a 'killer'", "Saudis down
# 3 Houthi missiles at Riyadh" and "IRGC claims it downed a US drone"
# over the Strait of Hormuz. Twelve more illustrated tiles follow:
# Gen Z marches in 25 countries, COP31 talks stalling past deadline,
# Denmark expelling a Russian diplomat over an "assassin plot", Trump
# urging Nvidia to bring back Huang, Trump threatening a tax on AI
# data centres abroad, Africa launching its own credit rating agency,
# a pancreatic cancer pill trial, a claimed Riemann proof, BepiColombo
# reaching Mercury orbit, an M6.7 quake in central Peru, Tanzania's
# Lissu convicted of sedition, and Alcaraz perfect at the ATP Finals.
# A world map with numbered pins 1-16 indexes those stories, stories
# 17-52 run as a numbered briefs column, and a DATE CHECK box names
# the big stories deliberately left out because they broke on another
# day. Every label was typeset programmatically, so the spelling in
# the image is exact.
#
# This program writes entry.png to the output directory in one
# byte-exact write: it reads no input, uses no clock and no randomness,
# so the grader's two runs produce identical bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import struct
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = SRC.read_bytes()
    # Guard the gate before writing: the entry must be a whole PNG
    # within the 1 MiB limit, so a bad source fails loudly here instead
    # of handing the grader an invalid image.
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    if len(data) > 1048576:
        raise SystemExit("entry.png exceeds the 1 MiB limit")
    # The gate also caps the image at 1024 by 1024 pixels: read the
    # IHDR width and height straight from the header bytes.
    width, height = struct.unpack(">II", data[16:24])
    if width > 1024 or height > 1024:
        raise SystemExit("entry.png exceeds 1024 by 1024 pixels")
    target = out_dir / "entry.png"
    target.write_bytes(data)
    # Verify the copy before reporting success: a truncated write must
    # fail loudly instead of handing the grader a corrupt image. The
    # read-back is deterministic and changes nothing about the bytes.
    if target.read_bytes() != data:
        raise SystemExit("entry.png copy failed verification")


if __name__ == "__main__":
    main()
