#!/usr/bin/env python3
"""Generate ascii.svg — self-typing monochrome ASCII branding for Rifqi Ariansyah (Nueeva).

Renders the NUEVA typography into a crisp ASCII character ramp,
animated with SMIL left-to-right clipPath wipe and a tracking cursor block.
Supports both dark and light modes on GitHub.
Inlines JetBrains Mono font as base64 so geometry is pinned across all devices.
"""
import base64
import os
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_FILE = os.path.join(HERE, "fonts", "jbmono-400.woff2")
RAMP = " .:-=+*#%@"

# Layout & Typography
FONT_SIZE = 12.9
CHAR_W = 7.74      # 0.600 em at FONT_SIZE
LINE_H = 15.2
ROW_DELAY = 0.08   # stagger per row in seconds
PAD_X = 16
PAD_Y = 18

MONO = ("JBMono,ui-monospace,SFMono-Regular,Menlo,Consolas,"
        "&apos;Liberation Mono&apos;,monospace")


def get_ascii_lines(image_path, cols=74, rows=22):
    im = Image.open(image_path).convert("L")
    # Crop to NUEVA letters in banner
    crop = im.crop((3600, 3450, 7620, 4330))
    resized = crop.resize((cols, rows), Image.Resampling.LANCZOS)

    lines = []
    for y in range(rows):
        row = "".join(RAMP[int(resized.getpixel((x, y)) / 255 * (len(RAMP) - 1))] for x in range(cols))
        lines.append(row.rstrip())

    # Add subtitle line
    lines.append("")
    subtitle = "--- rifqi ariansyah  ·  web security & systems developer ---"
    lines.append(subtitle.center(cols).rstrip())
    return lines


def build_svg(lines, cols=74):
    width = 620
    height = int(PAD_Y * 2 + len(lines) * LINE_H)

    with open(FONT_FILE, "rb") as f:
        font_b64 = base64.b64encode(f.read()).decode("ascii")

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" fill="none" font-family="{MONO}">',
        f"<style>",
        f"@font-face{{font-family:JBMono;font-style:normal;font-weight:400;font-display:block;"
        f"src:url(data:font/woff2;base64,{font_b64}) format('woff2')}}",
        f".a{{fill:#6e7681}}",
        f"@media(prefers-color-scheme:dark){{.a{{fill:#c9d1d9}}}}",
        f"</style>"
    ]

    for i, line in enumerate(lines):
        y = PAD_Y + i * LINE_H
        begin = f"{i * ROW_DELAY:.2f}s"
        end = f"{(i + 1) * ROW_DELAY:.2f}s"
        w_px = max(len(line), 1) * CHAR_W
        safe = (line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

        # Center line in 620px canvas
        line_pad = max(PAD_X, (width - len(line) * CHAR_W) / 2) if len(line) > 0 else PAD_X

        p.append(
            f'<clipPath id="c{i}"><rect x="{line_pad:.1f}" y="{y:.1f}" '
            f'height="{LINE_H}" width="0">'
            f'<animate attributeName="width" from="0" to="{w_px:.1f}" '
            f'begin="{begin}" dur="{ROW_DELAY}s" fill="freeze"/>'
            f'</rect></clipPath>'
        )
        p.append(
            f'<g clip-path="url(#c{i})"><text xml:space="preserve" '
            f'x="{line_pad:.1f}" y="{y + 11.4:.1f}" class="a" '
            f'font-size="{FONT_SIZE}">{safe}</text></g>'
        )
        # Cursor block riding along the wipe edge
        if line:
            p.append(
                f'<rect y="{y + 1:.1f}" width="6" height="12" class="a" opacity="0">'
                f'<animate attributeName="x" from="{line_pad:.1f}" to="{line_pad + w_px:.1f}" '
                f'begin="{begin}" dur="{ROW_DELAY}s" fill="freeze"/>'
                f'<set attributeName="opacity" to="0.8" begin="{begin}"/>'
                f'<set attributeName="opacity" to="0" begin="{end}"/>'
                f'</rect>'
            )

    p.append("</svg>")
    return "".join(p)


def main():
    root = os.path.dirname(HERE)
    banner_path = os.path.join(root, "banner.jpeg")
    out_path = os.path.join(root, "ascii.svg")

    if not os.path.exists(banner_path):
        sys.exit(f"Banner image not found at {banner_path}")

    lines = get_ascii_lines(banner_path)
    svg = build_svg(lines)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"Generated {out_path} ({len(lines)} lines, {len(svg)} bytes)")


if __name__ == "__main__":
    main()
