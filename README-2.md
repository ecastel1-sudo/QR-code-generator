# QR Generator

A small Python command-line tool that turns any website or URL into a QR code PNG.

## Installation

Requires Python 3.8+.

```bash
pip install "qrcode[pil]"
```

Then download or clone this repo and run `qr_generator.py`.

## Usage

```bash
python qr_generator.py https://example.com
```

This saves a PNG named after the URL (e.g. `qr_example_com.png`) in the current folder.

If you run it without a URL, it prompts you for one:

```bash
python qr_generator.py
Enter the URL: example.com
```

If the URL has no scheme (`https://`, `http://`, …), `https://` is added automatically so phones open it as a link.

### Options

| Option | Default | Description |
|---|---|---|
| `-o`, `--output` | `qr_<url>.png` | Output file name |
| `--size` | `10` | Pixels per QR module (bigger = larger image) |
| `--border` | `4` | Quiet-zone width around the code, in modules |
| `--fill` | `black` | Colour of the QR code (name or hex, e.g. `#1a237e`) |
| `--back` | `white` | Background colour |

### Examples

```bash
# Custom file name and a larger image
python qr_generator.py https://example.com -o my_qr.png --size 15

# Coloured QR code
python qr_generator.py example.com --fill "#1a237e" --back white
```

## Use it from Python

```python
from qr_generator import make_qr, normalize_url

make_qr(normalize_url("example.com"), "example.png", box_size=12)
```

## Tips

- Keep strong contrast between `--fill` and `--back` (dark on light works best), or some phones won't scan it.
- Don't set `--border` below `4` if the code will sit on a busy background; the quiet zone helps scanners find it.
- The code uses medium error correction (~15% damage tolerance) and picks the smallest QR version that fits the URL.
