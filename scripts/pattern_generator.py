#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pattern Generator - Generate CSS background patterns:
dots, grid, stripes, checkerboard, zigzag, triangles, waves, polka
Cyber-Rage Design Intelligence Engine

Usage: python pattern_generator.py dots
       python pattern_generator.py grid --color "#2563EB" --bg "#F8FAFC"
       python pattern_generator.py --all --sizes 12 20
"""

import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


PATTERNS = [
    "dots", "grid", "stripes", "diagonal-stripes", "checkerboard",
    "zigzag", "triangles", "waves", "polka", "crosshatch", "dots-large", "columns",
]


def hex_rgba(hex_color, alpha):
    hex_color = hex_color.lstrip("#")
    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return f"rgba({r}, {g}, {b}, {alpha})"


def p_dots(color, bg, size):
    c = hex_rgba(color, 1)
    return f"""/* Dots pattern */
.dots {{
  background-color: {bg};
  background-image: radial-gradient({c} {max(1, size // 8)}px, transparent {max(1, size // 8)}px);
  background-size: {size}px {size}px;
}}"""


def p_dots_large(color, bg, size):
    c = hex_rgba(color, 0.4)
    return f"""/* Large dots / polka pattern */
.dots-large {{
  background-color: {bg};
  background-image: radial-gradient({c} {max(2, size // 6)}px, transparent {max(2, size // 6)}px);
  background-size: {size * 2}px {size * 2}px;
}}"""


def p_grid(color, bg, size):
    c = hex_rgba(color, 0.4)
    return f"""/* Grid pattern */
.grid {{
  background-color: {bg};
  background-image: linear-gradient({c} 1px, transparent 1px),
                    linear-gradient(90deg, {c} 1px, transparent 1px);
  background-size: {size}px {size}px;
}}"""


def p_stripes(color, bg, size):
    c = hex_rgba(color, 0.8)
    return f"""/* Horizontal stripes */
.stripes {{
  background-color: {bg};
  background-image: repeating-linear-gradient(0deg, {c} 0, {c} {size // 3}px, transparent {size // 3}px, transparent {size}px);
}}"""


def p_diagonal(color, bg, size):
    c = hex_rgba(color, 0.5)
    return f"""/* Diagonal stripes */
.diagonal-stripes {{
  background-color: {bg};
  background-image: repeating-linear-gradient(45deg, {c} 0, {c} {size // 4}px, transparent {size // 4}px, transparent {size}px);
}}"""


def p_checker(color, bg, size):
    c = hex_rgba(color, 0.6)
    return f"""/* Checkerboard */
.checkerboard {{
  background-color: {bg};
  background-image: conic-gradient({c} 25%, transparent 25% 50%, {c} 50% 75%, transparent 75%);
  background-size: {size * 2}px {size * 2}px;
}}"""


def p_zigzag(color, bg, size):
    c = hex_rgba(color, 0.5)
    return f"""/* Zigzag */
.zigzag {{
  background-color: {bg};
  background-image: linear-gradient(135deg, {c} 25%, transparent 25%),
                    linear-gradient(225deg, {c} 25%, transparent 25%);
  background-position: 0 0, {size}px 0, 0 {size}px, {size}px {size}px;
  background-size: {size * 2}px {size * 2}px;
}}"""


def p_triangles(color, bg, size):
    c = hex_rgba(color, 0.3)
    return f"""/* Triangles */
.triangles {{
  background-color: {bg};
  background-image: linear-gradient(45deg, {c} 25%, transparent 25%),
                    linear-gradient(-45deg, {c} 25%, transparent 25%);
  background-size: {size}px {size}px;
}}"""


def p_waves(color, bg, size):
    c = hex_rgba(color, 0.5)
    return f"""/* Waves (radial pairs) */
.waves {{
  background-color: {bg};
  background-image: radial-gradient(circle at 100% 150%, {c} 24%, transparent 24%, transparent 28%, {c} 28%, {c} 36%, transparent 36%, transparent 40%, transparent),
                    radial-gradient(circle at 0 150%, {c} 24%, transparent 24%, transparent 28%, {c} 28%, {c} 36%, transparent 36%, transparent 40%, transparent);
  background-size: {size * 2}px {size}px;
}}"""


def p_polka(color, bg, size):
    c1 = hex_rgba(color, 1)
    c2 = hex_rgba(color, 0.35)
    r = max(2, size // 5)
    return f"""/* Polka (two-tone dots) */
.polka {{
  background-color: {bg};
  background-image: radial-gradient({c1} {r}px, transparent {r}px),
                    radial-gradient({c2} {r}px, transparent {r}px);
  background-position: 0 0, {size // 2}px {size // 2}px;
  background-size: {size}px {size}px;
}}"""


def p_crosshatch(color, bg, size):
    c = hex_rgba(color, 0.4)
    return f"""/* Crosshatch */
.crosshatch {{
  background-color: {bg};
  background-image: repeating-linear-gradient(45deg, {c} 0, {c} 1px, transparent 0, transparent {size // 2}px),
                    repeating-linear-gradient(-45deg, {c} 0, {c} 1px, transparent 0, transparent {size // 2}px);
}}"""


def p_columns(color, bg, size):
    c = hex_rgba(color, 0.6)
    return f"""/* Vertical columns */
.columns {{
  background-color: {bg};
  background-image: repeating-linear-gradient(90deg, {c} 0, {c} {max(2, size // 6)}px, transparent {max(2, size // 6)}px, transparent {size}px);
}}"""


GENERATORS = {
    "dots": p_dots, "grid": p_grid, "stripes": p_stripes,
    "diagonal-stripes": p_diagonal, "checkerboard": p_checker,
    "zigzag": p_zigzag, "triangles": p_triangles, "waves": p_waves,
    "polka": p_polka, "crosshatch": p_crosshatch,
    "dots-large": p_dots_large, "columns": p_columns,
}


def print_all(color, bg, size):
    for name in PATTERNS:
        print(GENERATORS[name](color, bg, size))
        print()
    print("""Usage: add class to any element, e.g.
  <div class="dots h-96 w-full"></div>
  <section class="grid bg-white" style="min-height:300px"></section>""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pattern Generator - Cyber-Rage")
    parser.add_argument("pattern", nargs="?", help=f"Pattern name ({', '.join(PATTERNS)}) or 'all'")
    parser.add_argument("--color", default="#2563EB", help="Pattern color (default: #2563EB)")
    parser.add_argument("--bg", default="#F8FAFC", help="Background color (default: #F8FAFC)")
    parser.add_argument("--size", type=int, default=16, help="Pattern size in px (default: 16)")
    parser.add_argument("--list", action="store_true", help="List available patterns")

    args = parser.parse_args()

    if args.list:
        print("Available patterns:")
        for p in PATTERNS:
            print(f"  - {p}")
        sys.exit(0)

    if not args.pattern:
        print("Specify a pattern name (see --list) or 'all'")
        sys.exit(1)

    if args.pattern == "all":
        print_all(args.color, args.bg, args.size)
    elif args.pattern in GENERATORS:
        print(GENERATORS[args.pattern](args.color, args.bg, args.size))
    else:
        print(f"Unknown pattern: '{args.pattern}'. Available: {', '.join(PATTERNS)}")
        sys.exit(1)
