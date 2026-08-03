#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Palette Generator - Generate full color palettes with harmony types,
shade scales, WCAG contrast checks, and export as CSS/Tailwind/JSON
Cyber-Rage Design Intelligence Engine

Usage: python palette_generator.py "#2563EB"
       python palette_generator.py "#2563EB" --harmony complementary --format tailwind
       python palette_generator.py "#F97316" --harmony triadic --check-wcag
"""

import argparse
import colorsys
import json
import re
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def hex_to_rgb(hex_color):
    hex_color = hex_color.strip().lstrip('#')
    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)
    if not re.match(r'^[0-9a-fA-F]{6}$', hex_color):
        return None
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*[max(0, min(255, int(round(c)))) for c in rgb])


def rgb_to_hsl(rgb):
    r, g, b = (c / 255 for c in rgb)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return (h * 360, s * 100, l * 100)


def hsl_to_rgb(h, s, l):
    h = (h % 360) / 360
    r, g, b = colorsys.hls_to_rgb(h, l / 100, s / 100)
    return (r * 255, g * 255, b * 255)


def adjust_lightness(rgb, amount):
    h, s, l = rgb_to_hsl(rgb)
    l = max(0, min(100, l + amount))
    return rgb_to_hex(hsl_to_rgb(h, s, l))


def rgb_to_luminance(rgb):
    def channel(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg, bg):
    l1, l2 = rgb_to_luminance(fg), rgb_to_luminance(bg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)


def harmony_colors(hex_color, harmony):
    rgb = hex_to_rgb(hex_color)
    if not rgb:
        return []
    h, s, l = rgb_to_hsl(rgb)
    angles = {
        "complementary": [0, 180],
        "analogous": [0, 30, 330],
        "triadic": [0, 120, 240],
        "split-complementary": [0, 150, 210],
        "tetradic": [0, 90, 180, 270],
        "square": [0, 90, 180, 270],
        "monochromatic": [0, 0, 0, 0, 0],
    }
    angles = angles.get(harmony, angles["complementary"])
    if harmony == "monochromatic":
        lights = [10, 25, 0, -15, -30]
        return [adjust_lightness(rgb, amt) for amt in lights]
    return [rgb_to_hex(hsl_to_rgb(h + a, s, l)) for a in angles]


def shade_scale(hex_color, steps=10):
    rgb = hex_to_rgb(hex_color)
    shades = []
    for i in range(steps):
        ratio = i / (steps - 1)
        shade = tuple(rgb[j] * ratio for j in range(3))
        shades.append(rgb_to_hex(shade))
    return shades


def tint_shade_scale(hex_color, steps=5):
    rgb = hex_to_rgb(hex_color)
    tints = [rgb_to_hex(tuple(rgb[j] + (255 - rgb[j]) * (i / steps) for j in range(3))) for i in range(steps, 0, -1)]
    shades = [rgb_to_hex(tuple(rgb[j] * (1 - i / (steps + 4)) for j in range(3))) for i in range(1, steps + 2)]
    return tints + [hex_color] + shades


def wcag_report(hex_color, palette):
    rgb = hex_to_rgb(hex_color)
    lines = ["WCAG Contrast Report (on white / on black):"]
    for c in palette:
        cr = hex_to_rgb(c)
        if not cr:
            continue
        on_white = contrast_ratio(cr, (255, 255, 255))
        on_black = contrast_ratio(cr, (0, 0, 0))
        badge = lambda r: "AAA" if r >= 7 else ("AA" if r >= 4.5 else ("AA-lg" if r >= 3 else "FAIL"))
        lines.append(f"  {c}  white:{on_white:.2f} [{badge(on_white)}]  black:{on_black:.2f} [{badge(on_black)}]")
    return "\n".join(lines)


def export_css(palette, name="palette"):
    lines = [f":root {{"]
    for i, c in enumerate(palette):
        lines.append(f"  --{name}-{i + 1}: {c};")
    lines.append("}")
    return "\n".join(lines)


def export_tailwind(palette, name="brand"):
    colors = ", ".join(f"'{i + 1}': '{c}'" for i, c in enumerate(palette))
    return f"""module.exports = {{
  theme: {{
    extend: {{
      colors: {{
        {name}: {{ {colors} }}
      }}
    }}
  }}
}}"""


def export_json(palette, harmony, base):
    return json.dumps({
        "base": base,
        "harmony": harmony,
        "palette": palette,
    }, indent=2)


def print_swatches(palette):
    print("Swatch preview:")
    for c in palette:
        rgb = hex_to_rgb(c)
        block = "█" * 12
        print(f"  {block}  {c}  rgb{rgb}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Palette Generator - Cyber-Rage")
    parser.add_argument("color", help="Base hex color (e.g. #2563EB)")
    parser.add_argument("--harmony", default="complementary", help="Harmony type (complementary, analogous, triadic, split-complementary, tetradic, square, monochromatic)")
    parser.add_argument("--scale", action="store_true", help="Show 50-900 shade scale")
    parser.add_argument("--check-wcag", action="store_true", help="Show WCAG contrast report")
    parser.add_argument("--format", choices=["css", "tailwind", "json", "text"], default="text", help="Output format")

    args = parser.parse_args()

    rgb = hex_to_rgb(args.color)
    if not rgb:
        print(f"Invalid hex color: '{args.color}'. Use format like #2563EB")
        sys.exit(1)

    palette = harmony_colors(args.color, args.harmony)

    print(f"Base color: {args.color} ({rgb})")
    print(f"Harmony: {args.harmony}")

    if args.format == "css":
        print(export_css(palette))
    elif args.format == "tailwind":
        print(export_tailwind(palette))
    elif args.format == "json":
        print(export_json(palette, args.harmony, args.color))
    else:
        print_swatches(palette)
        print("Palette:", " → ".join(palette))
        if args.scale:
            print("\nShade scale (50-900):")
            tints_shades = tint_shade_scale(args.color)
            labels = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]
            for label, c in zip(labels, tints_shades):
                print(f"  {label}: {c}")
        if args.check_wcag:
            print()
            print(wcag_report(args.color, palette))
