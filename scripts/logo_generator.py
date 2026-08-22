#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logo Generator - Simple, clean SVG logos from a name or initials:
monogram, badge, wordmark, and shield styles + favicon-sized variants
Cyber-Rage Design Intelligence Engine

Usage: python logo_generator.py --text "CR" --style monogram --color "#2563EB"
       python logo_generator.py --text "Cyber Rage" --style wordmark --dark
       python logo_generator.py --text "S" --style badge --color "#F97316"
       python logo_generator.py --styles
"""

import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def initials(text):
    parts = [p for p in text.strip().split() if p]
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    return text.strip()[:2].upper() or "CR"


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def logo_monogram(text, color, dark=False):
    bg = "#0F172A" if dark else color
    fg = "#FFFFFF"
    return f"""<!-- Monogram logo (save as logo.svg) -->
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128" role="img" aria-label="{esc(text)} logo">
  <rect width="128" height="128" rx="28" fill="{bg}"/>
  <text x="64" y="66" text-anchor="middle" dominant-baseline="central"
        font-family="Arial, Helvetica, sans-serif" font-size="52" font-weight="800"
        fill="{fg}">{esc(initials(text))}</text>
</svg>"""


def logo_badge(text, color, dark=False):
    fg = "#F8FAFC" if dark else "#FFFFFF"
    bg = "#0F172A" if dark else color
    return f"""<!-- Badge logo (save as logo.svg) -->
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128" role="img" aria-label="{esc(text)} logo">
  <circle cx="64" cy="64" r="58" fill="{bg}"/>
  <circle cx="64" cy="64" r="58" fill="none" stroke="#FFFFFF" stroke-opacity="0.25" stroke-width="3"/>
  <circle cx="64" cy="64" r="46" fill="none" stroke="#FFFFFF" stroke-opacity="0.15" stroke-width="1.5"/>
  <text x="64" y="66" text-anchor="middle" dominant-baseline="central"
        font-family="Arial, Helvetica, sans-serif" font-size="44" font-weight="800"
        fill="{fg}">{esc(initials(text))}</text>
</svg>"""


def logo_wordmark(text, color, dark=False):
    word_color = "#F8FAFC" if dark else "#0F172A"
    return f"""<!-- Wordmark logo with accent dot (save as logo.svg) -->
<svg xmlns="http://www.w3.org/2000/svg" width="300" height="64" viewBox="0 0 300 64" role="img" aria-label="{esc(text)} logo">
  <rect x="4" y="8" width="48" height="48" rx="12" fill="{color}"/>
  <text x="28" y="33" text-anchor="middle" dominant-baseline="central"
        font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="800"
        fill="#FFFFFF">{esc(initials(text))}</text>
  <text x="66" y="33" dominant-baseline="central"
        font-family="Arial, Helvetica, sans-serif" font-size="26" font-weight="700"
        fill="{word_color}">{esc(text.strip())}</text>
  <circle cx="{66 + 9.5 * len(text.strip()) + 8}" cy="38" r="4" fill="{color}"/>
</svg>"""


def logo_shield(text, color, dark=False):
    fg = "#FFFFFF"
    return f"""<!-- Shield logo (save as logo.svg) -->
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128" role="img" aria-label="{esc(text)} logo">
  <defs>
    <linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{color}"/>
      <stop offset="100%" stop-color="{color}99"/>
    </linearGradient>
  </defs>
  <path d="M64 8L112 26V64C112 92 92 112 64 122C36 112 16 92 16 64V26L64 8Z"
        fill="url(#lg)"/>
  <path d="M64 8L112 26V64C112 92 92 112 64 122C36 112 16 92 16 64V26L64 8Z"
        fill="none" stroke="#FFFFFF" stroke-opacity="0.2" stroke-width="2"/>
  <text x="64" y="66" text-anchor="middle" dominant-baseline="central"
        font-family="Arial, Helvetica, sans-serif" font-size="38" font-weight="800"
        fill="{fg}">{esc(initials(text))}</text>
</svg>"""


LOGO_STYLES = {
    "monogram": logo_monogram,
    "badge": logo_badge,
    "wordmark": logo_wordmark,
    "shield": logo_shield,
}


def html_usage_snippet(style):
    return f"""
<!-- Usage -->
<img src="logo.svg" alt="Company logo" width="48" height="48">
<!-- Or inline for theme-aware coloring ({style} style): -->
<!-- paste the SVG markup directly into your HTML and set fill="currentColor" -->"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Logo Generator - Cyber-Rage")
    parser.add_argument("--text", help="Brand name or initials (e.g. 'Cyber Rage' or 'CR')")
    parser.add_argument("--style", help=f"Logo style ({', '.join(LOGO_STYLES)})")
    parser.add_argument("--color", default="#2563EB", help="Brand color (default #2563EB)")
    parser.add_argument("--dark", action="store_true", help="Dark-mode variant")
    parser.add_argument("--styles", action="store_true", help="List available styles")

    args = parser.parse_args()

    if args.styles:
        print("Logo styles:")
        for s in LOGO_STYLES:
            print(f"  - {s}")
        sys.exit(0)

    if not args.text or not args.style:
        print("Specify --text and --style (see --styles)")
        sys.exit(1)

    if args.style not in LOGO_STYLES:
        print(f"Unknown style: '{args.style}'. Available: {', '.join(LOGO_STYLES)}")
        sys.exit(1)

    print(LOGO_STYLES[args.style](args.text, args.color, args.dark))
    print(html_usage_snippet(args.style))
