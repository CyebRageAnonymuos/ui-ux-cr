#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Banner Generator - ASCII art banners and typography for terminal
Cyber-Rage Design Intelligence Engine

Usage: python banner_generator.py --text "CYBER RAGE" --style block
       python banner_generator.py --text "Hello" --style small --rainbow
       python banner_generator.py --styles
"""

import argparse
import random
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


FONTS = {}

FONTS["block"] = {
    "A": [" █████ ", "██   ██", "██████ ", "██   ██", "██   ██"],
    "B": ["██████ ", "██   ██", "██████ ", "██   ██", "██████ "],
    "C": [" ██████", "██     ", "██     ", "██     ", " ██████"],
    "D": ["██████ ", "██   ██", "██   ██", "██   ██", "██████ "],
    "E": ["███████", "██     ", "█████  ", "██     ", "███████"],
    "F": ["███████", "██     ", "█████  ", "██     ", "██     "],
    "G": [" ██████", "██     ", "██  ███", "██   ██", " █████ "],
    "H": ["██   ██", "██   ██", "███████", "██   ██", "██   ██"],
    "I": ["███████", "  ███  ", "  ███  ", "  ███  ", "███████"],
    "J": ["  █████", "   ███ ", "   ███ ", "██ ███ ", " ████  "],
    "K": ["██   ██", "██  ██ ", "█████  ", "██  ██ ", "██   ██"],
    "L": ["██     ", "██     ", "██     ", "██     ", "███████"],
    "M": ["███ ███", "███████", "███████", "██ █ ██", "██   ██"],
    "N": ["███  ██", "████ ██", "██ ████", "██  ███", "██   ██"],
    "O": [" █████ ", "██   ██", "██   ██", "██   ██", " █████ "],
    "P": ["██████ ", "██   ██", "██████ ", "██     ", "██     "],
    "Q": [" █████ ", "██   ██", "██   ██", "██  ███", " ██████"],
    "R": ["██████ ", "██   ██", "██████ ", "██  ██ ", "██   ██"],
    "S": [" ██████", "██     ", " █████ ", "    ███", "██████ "],
    "T": ["███████", "  ███  ", "  ███  ", "  ███  ", "  ███  "],
    "U": ["██   ██", "██   ██", "██   ██", "██   ██", " █████ "],
    "V": ["██   ██", "██   ██", "██   ██", " ██ ██ ", "  ███  "],
    "W": ["██   ██", "██ █ ██", "███████", "███████", "██ █ ██"],
    "X": ["██   ██", " ██ ██ ", "  ███  ", " ██ ██ ", "██   ██"],
    "Y": ["██   ██", " ██ ██ ", "  ███  ", "  ███  ", "  ███  "],
    "Z": ["███████", "    ███", "   ███ ", "  ███  ", "███████"],
    "0": [" █████ ", "██   ██", "██  ███", "██   ██", " █████ "],
    "1": ["  ███  ", " ████  ", "  ███  ", "  ███  ", "███████"],
    "2": [" █████ ", "██   ██", "   ███ ", " ███   ", "███████"],
    "3": [" █████ ", "██   ██", "   ███ ", "██   ██", " █████ "],
    "4": ["██   ██", "██   ██", "███████", "    ███", "    ███"],
    "5": ["███████", "██     ", "██████ ", "    ███", "██████ "],
    "6": [" █████ ", "██     ", "██████ ", "██   ██", " █████ "],
    "7": ["███████", "    ███", "   ███ ", "  ███  ", "  ███  "],
    "8": [" █████ ", "██   ██", " █████ ", "██   ██", " █████ "],
    "9": [" █████ ", "██   ██", " ██████", "    ███", " █████ "],
    "-": ["       ", "       ", "███████", "       ", "       "],
    " ": ["       ", "       ", "       ", "       ", "       "],
    ".": ["       ", "       ", "       ", "  ███  ", "  ███  "],
    "!": ["  ███  ", "  ███  ", "  ███  ", "       ", "  ███  "],
    ":": ["       ", "  ███  ", "       ", "  ███  ", "       "],
    "+": ["       ", "  ███  ", "███████", "  ███  ", "       "],
    "*": ["       ", "██ ███ ", " █████ ", "██ ███ ", "       "],
    "#": [" █ █ █ ", "███████", " █ █ █ ", "███████", " █ █ █ "],
    "/": ["      █", "     █ ", "    █  ", "   █   ", "  █    "],
    "@": [" █████ ", "██   ██", "██ ████", "██     ", " █████ "],
}

FONTS["small"] = {
    "A": [" ▄▄ ", "██▀ ", "██  "],
    "B": ["▄▄▄ ", "██▄ ", "▀▀▀ "],
    "C": ["▄▄▄ ", "█   ", "▀▀▀ "],
    "D": ["▄▄▄ ", "█▄▄ ", "▀▀▀ "],
    "E": ["▄▄▄▄", "██▄ ", "▀▀▀ "],
    "F": ["▄▄▄▄", "██▄ ", "██  "],
    "G": ["▄▄▄ ", "█ ▀▄", "▀▄▀ "],
    "H": ["█ █ ", "███ ", "█ █ "],
    "I": ["███", " █ ", " █ "],
    "J": ["  ██", "  █ ", "▀▀  "],
    "K": ["█ ▄ ", "██  ", "█ ▀ "],
    "L": ["█   ", "█   ", "▀▀▀ "],
    "M": ["█▄▀█", "██▀█", "█  █"],
    "N": ["█▄▀█", "█ ▀█", "█  █"],
    "O": ["▄▄▄ ", "█ █ ", "▀▀▀ "],
    "P": ["▄▄▄ ", "██▄ ", "█   "],
    "Q": ["▄▄▄ ", "█ ▄▀", "▀▀▀ "],
    "R": ["▄▄▄ ", "██▄ ", "█ ▀ "],
    "S": ["▄▄▄ ", "▀▄  ", "▀▀▀ "],
    "T": ["▄██▄", " ██ ", " ██ "],
    "U": ["█ █ ", "█ █ ", "▀▀▀ "],
    "V": ["█ █ ", "█ █ ", "▀ ▀ "],
    "W": ["█ █ ", "█▄█ ", "█ █ "],
    "X": ["█ █ ", " █  ", "█ █ "],
    "Y": ["█ █ ", "▀█  ", " █  "],
    "Z": ["██▄ ", " ▄█ ", "▀▀  "],
    "0": ["▄▄▄ ", "█▄█ ", "▀▀▀ "],
    "1": ["▄█ ", " █ ", "▄█▄"],
    "2": ["▄▄▄ ", "▀▀█ ", "██▀ "],
    "3": ["▄▄▄ ", " ▀█ ", "▀▀▀ "],
    "4": ["█ █ ", "██▀ ", "  █ "],
    "5": ["██▄ ", "▀▀█ ", "▀▀▀ "],
    "6": ["▄▄▄ ", "█▄  ", "▀▀▀ "],
    "7": ["▄▄▄ ", "  █ ", " █  "],
    "8": ["▄▄▄ ", "▀█▀ ", "▀▀▀ "],
    "9": ["▄▄▄ ", " ▀█ ", "▀▀  "],
    "-": ["    ", "▀▀▀▀", "    "],
    " ": ["  ", "  ", "  "],
    ".": ["   ", "   ", "▀ "],
    "!": ["█", "█", "▀"],
    ":": ["  ", "▀▀", "  "],
    "/": ["  █", " █ ", "█  "],
    ">": [" ▄ ", "█▀ ", "▀  "],
    "<": [" ▄ ", " ▀█", "  ▀"],
}

STYLES = list(FONTS.keys())

COLORS = {
    "red": 31, "green": 32, "yellow": 33, "blue": 34, "magenta": 35,
    "cyan": 36, "white": 37, "bright-red": 91, "bright-green": 92,
    "bright-yellow": 93, "bright-blue": 94, "bright-magenta": 95,
    "bright-cyan": 96, "bright-white": 97,
}


def render(text, font, color=None, rainbow=False):
    text = text.upper()
    glyphs = []
    for ch in text:
        glyphs.append(FONTS[font].get(ch, FONTS[font][" "] if " " in FONTS[font] else ["?" * 3]))
    # Height must match the glyphs actually rendered (same fallback
    # logic as above). Deriving it from text[0] alone truncated the
    # whole banner to a single row when the first char wasn't in the font.
    height = len(glyphs[0]) if glyphs else len(FONTS[font].get("A", ["###"]))

    lines = []
    for row in range(height):
        line = "  ".join(g[row] for g in glyphs).rstrip()
        if rainbow:
            colored = []
            for i, ch in enumerate(line):
                c = COLORS[list(COLORS.keys())[i % len(COLORS)]]
                colored.append(f"\033[{c}m{ch}")
            lines.append("".join(colored) + "\033[0m")
        elif color and color in COLORS:
            lines.append(f"\033[{COLORS[color]}m{line}\033[0m")
        else:
            lines.append(line)
    return "\n".join(lines)


def print_frame(text, font):
    lines = render(text, font).splitlines()
    width = max(len(l) for l in lines)
    print("╔" + "═" * (width + 4) + "╗")
    for l in lines:
        print("║  " + l.ljust(width) + "  ║")
    print("╚" + "═" * (width + 4) + "╝")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Banner Generator - ASCII art")
    parser.add_argument("--text", help="Text to render")
    parser.add_argument("--style", default="block", help=f"Font style ({', '.join(STYLES)})")
    parser.add_argument("--color", help=f"Text color ({', '.join(COLORS.keys())})")
    parser.add_argument("--rainbow", action="store_true", help="Rainbow colors")
    parser.add_argument("--frame", action="store_true", help="Wrap in a box frame")
    parser.add_argument("--styles", action="store_true", help="List available styles")

    args = parser.parse_args()

    if args.styles:
        print("Available styles:")
        for s in STYLES:
            print(f"  - {s}")
        sys.exit(0)

    if not args.text:
        print("Specify --text (e.g. --text 'UI UX CR')")
        sys.exit(1)

    if args.style not in FONTS:
        print(f"Unknown style: '{args.style}'. Available: {', '.join(STYLES)}")
        sys.exit(1)

    if args.frame:
        print_frame(args.text, args.style)
    else:
        print(render(args.text, args.style, args.color, args.rainbow))
