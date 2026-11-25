#!/usr/bin/env python3
"""Entry program for news-image-20261125.

Copies the front-page image (front.png, stored beside this file) to the
output location the grader reads: $MAKEFUN_OUTPUT_DIR/entry.png,
defaulting to /output/entry.png. The image sums up the world news of
Wednesday 25 November 2026: the Houthi drone strike on Riyadh's PIF
Tower, the Huawei verdict, Ukraine's strikes on Russian ships, the
Russian drone incursion into Poland, and the mine in the Strait of
Hormuz. Deterministic: the bytes written are exactly the bytes of
front.png, so repeated runs are byte-identical. Standard library only.
"""
import os
import sys

ASSET = "front.png"
OUTPUT_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ASSET)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, OUTPUT_NAME)
    with open(src, "rb") as f:
        data = f.read()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("front.png is not a PNG file")
    with open(dst, "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
