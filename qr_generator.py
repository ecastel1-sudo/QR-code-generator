#!/usr/bin/env python3
"""
Generate a QR code PNG for a website/URL.

Install once:
    pip install "qrcode[pil]"

Usage:
    python qr_generator.py https://example.com
    python qr_generator.py https://example.com -o my_qr.png --size 12 --border 4
    python qr_generator.py            # prompts for the URL
"""
import argparse
import re
import sys

import qrcode
from qrcode.constants import ERROR_CORRECT_M


def normalize_url(url: str) -> str:
    url = url.strip()
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
        url = "https://" + url  # add scheme so phones open it as a link
    return url


def default_filename(url: str) -> str:
    name = re.sub(r"^[a-zA-Z]+://", "", url)
    name = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")
    return f"qr_{name[:50] or 'code'}.png"


def make_qr(url: str, output: str, box_size: int = 10, border: int = 4,
            fill: str = "black", back: str = "white") -> str:
    qr = qrcode.QRCode(
        version=None,                 # auto-fit to the data
        error_correction=ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color=back)
    img.save(output)
    return output


def main():
    p = argparse.ArgumentParser(description="Generate a QR code for a URL.")
    p.add_argument("url", nargs="?", help="Website/URL to encode")
    p.add_argument("-o", "--output", help="Output PNG file name")
    p.add_argument("--size", type=int, default=10, help="Pixels per QR module (default 10)")
    p.add_argument("--border", type=int, default=4, help="Quiet-zone width in modules (default 4)")
    p.add_argument("--fill", default="black", help="QR colour (default black)")
    p.add_argument("--back", default="white", help="Background colour (default white)")
    args = p.parse_args()

    url = args.url or input("Enter the URL: ")
    if not url.strip():
        sys.exit("No URL given.")
    url = normalize_url(url)
    out = args.output or default_filename(url)

    make_qr(url, out, args.size, args.border, args.fill, args.back)
    print(f"Saved QR code for {url} -> {out}")


if __name__ == "__main__":
    main()
