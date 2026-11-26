#!/usr/bin/env python3
"""Entry program for news-image-20261126.

Copies the front-page image held in this repository to /output/entry.png.
No network, no randomness: both runs write the same bytes.
"""
import os
import shutil
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DST = OUT_DIR / "entry.png"
MAX_BYTES = 1_048_576


def check_png(path):
    """Confirm path is a whole PNG of 1024x1024 at most and under the cap."""
    data = path.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
    assert len(data) <= MAX_BYTES, "over the 1 MiB cap"
    width, height = struct.unpack(">II", data[16:24])
    assert (width, height) == (1024, 1024), "not 1024x1024"
    return len(data)


def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    size = check_png(DST)
    print(f"wrote {DST} ({size} bytes, valid 1024x1024 PNG)")


if __name__ == "__main__":
    main()
