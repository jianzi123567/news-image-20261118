"""Entry program for make.fun bounty news-image-20261118.

Deterministically copies the bundled image (entry.png) to /output/entry.png.
No network access, no randomness, no time dependence: the output bytes are
identical on every run. The bundled image is a true PNG (1024x1024,
904908 bytes, under the 1 MiB cap).
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(SRC, "rb") as src, open(DST, "wb") as dst:
        shutil.copyfileobj(src, dst, length=1024 * 1024)


if __name__ == "__main__":
    main()
