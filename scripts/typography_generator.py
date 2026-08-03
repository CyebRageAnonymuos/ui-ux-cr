#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Typography Generator - Generate modular type scales, font size systems,
and font pairing suggestions from the design database
Cyber-Rage Design Intelligence Engine

Usage: python typography_generator.py --scale major-third
       python typography_generator.py --scale 1.25 --base 16
       python typography_generator.py --pairing "SaaS (General)"
       python typography_generator.py --all-scales
"""

import argparse
import csv
import os
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, os.pardir, "data")

RATIOS = {
    "minor-second": 1.067,
    "major-second": 1.125,
    "minor-third": 1.2,
    "major-third": 1.25,
    "perfect-fourth": 1.333,
    "augmented-fourth": 1.414,
    "perfect-fifth": 1.5,
    "golden-ratio": 1.618,
}

LABELS = ["h1", "h2", "h3", "h4", "h5", "h6", "body-lg", "body", "body-sm", "caption", "overline"]


def generate_scale(ratio_name="major-third", base=16, line_height=1.5):
    if ratio_name in RATIOS:
        ratio = RATIOS[ratio_name]
    else:
        try:
            ratio = float(ratio_name)
        except ValueError:
            print(f"Unknown ratio: '{ratio_name}'. Available: {', '.join(RATIOS.keys())} or a custom number")
            sys.exit(1)

    print(f"Type Scale: {ratio_name} (ratio {ratio}, base {base}px)")
    print("=" * 52)

    rows = []
    for i, label in enumerate(LABELS):
        steps_from_base = 6 - i if i < 6 else 0 - (i - 6)
        size = base * (ratio ** steps_from_base)
        px = round(size, 1)
        rem = round(size / 16, 3)
        weight = "700" if i < 4 else ("600" if i < 6 else "400")
        lh = round(line_height * (1 - (steps_from_base if steps_from_base > 0 else 0) * 0.04), 2)
        rows.append((label, px, rem, weight, lh))
        print(f"  {label:<8} {px:>6.1f}px  {rem:>5.2f}rem  weight:{weight}  lh:{lh}")

    print()
    print("CSS Variables:")
    print(":root {")
    for label, px, rem, weight, lh in rows:
        print(f'  --font-size-{label}: {rem}rem;')
    print("}")
    print()
    print("Tailwind (fontSize):")
    print("fontSize: {")
    for label, px, rem, weight, lh in rows:
        print(f"  '{label}': ['{rem}rem', {{ lineHeight: '{lh}' }}],")
    print("}")


def print_all_scales():
    for name in RATIOS:
        print(f"### {name} (ratio {RATIOS[name]})")
        generate_scale(name, 16)
        print()


def load_typography():
    path = os.path.join(DATA_DIR, "typography.csv")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def suggest_pairings(product_type=None, count=5):
    rows = load_typography()
    if not rows:
        print("typography.csv not found")
        return

    matches = []
    if product_type:
        for row in rows:
            if product_type.strip().lower() in row["Best For"].lower():
                matches.append(row)

    if not matches:
        matches = rows[:count]
        print(f"# Font Pairings {'for: ' + product_type if product_type else '(all)'}")
        print(f"# No exact match for '{product_type}' - showing top pairings\n")
    else:
        print(f"# Font Pairings for: {product_type}\n")

    for row in matches[:count]:
        print(f"## {row['Font Pairing Name']}")
        print(f"- Heading: {row['Heading Font']} | Body: {row['Body Font']}")
        print(f"- Mood: {row['Mood/Style Keywords']}")
        print(f"- Best for: {row['Best For']}")
        print(f"- CSS Import: `{row['CSS Import']}`")
        print(f"- Tailwind: `{row['Tailwind Config']}`")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Typography Generator - Cyber-Rage")
    parser.add_argument("--scale", help=f"Type scale ratio ({', '.join(RATIOS.keys())} or custom e.g. 1.35)")
    parser.add_argument("--base", type=int, default=16, help="Base font size in px (default: 16)")
    parser.add_argument("--line-height", type=float, default=1.5, help="Base line height (default: 1.5)")
    parser.add_argument("--pairing", help="Get font pairings for a product type (e.g. 'SaaS (General)')")
    parser.add_argument("--all-scales", action="store_true", help="Show all type scales")

    args = parser.parse_args()

    if args.all_scales:
        print_all_scales()
    elif args.scale:
        generate_scale(args.scale, args.base, args.line_height)
    elif args.pairing:
        suggest_pairings(args.pairing)
    else:
        print("Specify one of: --scale, --pairing, --all-scales")
        print("Example: python typography_generator.py --scale major-third --base 16")
