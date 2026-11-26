#!/usr/bin/env python3
"""Entry point for news-image-20261126 (v2 evening refresh).

Takes the front-page image bundled in this repository and writes it to
the grader's output directory as /output/entry.png.

The run is fully deterministic and offline: the same input bytes always
produce the same output bytes, and no network access is needed.
"""
import os
import shutil
import struct
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "entry.png"
DEST_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DEST = DEST_DIR / "entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SIZE = (1024, 1024)
BYTE_LIMIT = 1_048_576


def read_png_bytes(path):
    """Read a file and confirm it starts with the PNG signature."""
    blob = path.read_bytes()
    if blob[:8] != PNG_MAGIC:
        raise ValueError(f"{path} does not start with a PNG signature")
    return blob


def ihdr_dimensions(blob):
    """Pull the width and height out of the PNG IHDR chunk."""
    if len(blob) < 24:
        raise ValueError("file too short to hold a PNG header")
    if blob[12:16] != b"IHDR":
        raise ValueError("first PNG chunk is not IHDR")
    chunk_len = struct.unpack(">I", blob[8:12])[0]
    if chunk_len != 13:
        raise ValueError(f"IHDR chunk is {chunk_len} bytes, expected 13")
    width, height = struct.unpack(">II", blob[16:24])
    return width, height


def validate(blob):
    """Check the image is a 1024x1024 PNG under the 1 MiB cap."""
    if len(blob) > BYTE_LIMIT:
        raise ValueError(f"image is {len(blob)} bytes, over the 1 MiB cap")
    dims = ihdr_dimensions(blob)
    if dims != EXPECTED_SIZE:
        raise ValueError(f"image is {dims[0]}x{dims[1]}, expected 1024x1024")
    return dims


def deliver():
    """Validate the bundled image, then copy it to the output directory."""
    blob = read_png_bytes(SOURCE)
    dims = validate(blob)
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    # Re-read the copy so the check covers what was actually written.
    written = read_png_bytes(DEST)
    if written != blob:
        raise ValueError("output copy differs from the bundled image")
    print(f"wrote {DEST} ({len(blob)} bytes, valid "
          f"{dims[0]}x{dims[1]} PNG)")


if __name__ == "__main__":
    try:
        deliver()
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
