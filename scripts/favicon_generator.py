#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Favicon Generator - Generate favicon SVG, HTML head snippet, and
sizing cheat sheet for all platforms
Cyber-Rage Design Intelligence Engine

Usage: python favicon_generator.py --text "CR"
       python favicon_generator.py --icon rocket --bg "#2563EB" --fg white
       python favicon_generator.py --html --theme-color "#2563EB"
"""

import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def generate_favicon(text="CR", bg="#2563EB", fg="#FFFFFF", shape="rounded", border_radius=12):
    if shape == "circle":
        rx, ry = 64, 64
    elif shape == "square":
        rx, ry = 0, 0
    elif shape == "squircle":
        rx, ry = 24, 24
    else:
        rx, ry = border_radius, border_radius

    letters = text[:2].upper()
    font_size = 56 if len(letters) == 2 else 72

    return f"""<!-- Favicon SVG (128x128) - save as favicon.svg -->
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg}" />
      <stop offset="100%" stop-color="{bg}88" />
    </linearGradient>
  </defs>
  <rect width="128" height="128" rx="{rx}" ry="{ry}" fill="url(#g)" />
  <text x="64" y="64" text-anchor="middle" dominant-baseline="central"
        font-family="Arial, Helvetica, sans-serif" font-weight="bold"
        font-size="{font_size}" fill="{fg}">{letters}</text>
</svg>"""


def generate_icon(icon_name, bg="#2563EB", fg="#FFFFFF"):
    icons = {
        "rocket": 'M64 8L78 40L110 54L78 68L64 100L50 68L18 54L50 40L64 8Z',
        "bolt": 'M72 8L32 72H56L48 120L96 52H70L72 8Z',
        "heart": 'M64 104C64 104 16 72 16 44C16 28 28 16 44 16C52 16 60 20 64 26C68 20 76 16 84 16C100 16 112 28 112 44C112 72 64 104 64 104Z',
        "star": 'M64 8L80 44L120 48L90 76L98 116L64 96L30 116L38 76L8 48L48 44L64 8Z',
        "shield": 'M64 8L112 28V64C112 92 92 112 64 122C36 112 16 92 16 64V28L64 8Z',
        "code": 'M48 32L16 64L48 96M80 32L112 64L80 96',
        "zap": 'M72 8L32 72H56L48 120L96 52H70L72 8Z',
        "gear": 'M64 44A20 20 0 1 0 64 84A20 20 0 1 0 64 44Z M64 24V36M64 92V104M104 64H92M36 64H24M92 36L83 45M45 83L36 92M92 92L83 83M45 45L36 36',
        "terminal": 'M24 32L56 64L24 96M64 96H104',
        "layers": 'M64 24L112 48L64 72L16 48L64 24ZM16 64L64 88L112 64M16 80L64 104L112 80',
    }
    path = icons.get(icon_name.lower(), icons["bolt"])

    return f"""<!-- Favicon SVG - {icon_name} icon (save as favicon.svg) -->
<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg}" />
      <stop offset="100%" stop-color="{bg}99" />
    </linearGradient>
  </defs>
  <rect width="128" height="128" rx="24" fill="url(#g)" />
  <g fill="none" stroke="{fg}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round">
    <path d="{path}" fill="{fg}40" stroke="{fg}"/>
  </g>
</svg>"""


def generate_html(theme_color="#2563EB"):
    return """<!-- Favicon HTML Head Snippet -->
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="icon" sizes="16x16" href="/favicon-16x16.png" type="image/png" />
<link rel="icon" sizes="32x32" href="/favicon-32x32.png" type="image/png" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
<meta name="theme-color" content="{theme}" />
<!-- PWA manifest (optional) -->
<link rel="manifest" href="/site.webmanifest" />""".replace("{theme}", theme_color)


def generate_manifest(theme_color="#2563EB", app_name="App"):
    return f"""{{
  "name": "{app_name}",
  "short_name": "{app_name[:12]}",
  "icons": [
    {{ "src": "/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png" }},
    {{ "src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png" }}
  ],
  "theme_color": "{theme_color}",
  "background_color": "#ffffff",
  "display": "standalone"
}}"""


def print_sizes():
    print("""Favicon Size Cheat Sheet:
=========================
| Size  | Purpose                           |
|-------|-----------------------------------|
| 16x16 | Browser tab, favicon (default)   |
| 32x32 | Windows taskbar, browser         |
| 48x48 | Windows site shortcut            |
| 57x57 | iOS home screen (legacy)         |
| 60x60 | iOS tab (legacy)                 |
| 72x72 | Android (legacy)                 |
| 76x76 | iOS iPad (legacy)                |
| 96x96 | Google TV                         |
| 114x114| iOS retina (legacy)              |
| 120x120| iOS retina (legacy)              |
| 128x128| Chrome Web Store                 |
| 144x144| Android (legacy), Windows tile   |
| 150x150| Windows tile (Square70x70)       |
| 152x152| iOS iPad retina (legacy)         |
| 180x180| Apple touch icon (modern)        |
| 192x192| Android Chrome (modern)          |
| 310x310| Windows tile (Square310x310)     |
| 512x512| PWA manifest (modern)            |

Recommendation:
- favicon.svg (all modern browsers, best quality)
- favicon-32x32.png + favicon-16x16.png (legacy fallback)
- apple-touch-icon.png 180x180 (iOS)
- android-chrome-192x192.png + 512x512.png (PWA)

Generate PNGs from SVG:  rsvg-convert -w 32 -h 32 favicon.svg -o favicon-32x32.png""", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Favicon Generator - Cyber-Rage")
    parser.add_argument("--text", help="Text letters for favicon (e.g. 'CR')")
    parser.add_argument("--icon", help="Icon name (rocket, bolt, heart, star, shield, code, zap, gear, terminal, layers)")
    parser.add_argument("--bg", default="#2563EB", help="Background color (default: #2563EB)")
    parser.add_argument("--fg", default="#FFFFFF", help="Text/icon color (default: white)")
    parser.add_argument("--shape", default="squircle", help="Shape (squircle, circle, square, rounded)")
    parser.add_argument("--html", action="store_true", help="Generate HTML head snippet")
    parser.add_argument("--manifest", action="store_true", help="Generate PWA manifest")
    parser.add_argument("--theme-color", default="#2563EB", help="Theme color for HTML/manifest")
    parser.add_argument("--app-name", default="App", help="App name for manifest")
    parser.add_argument("--sizes", action="store_true", help="Show favicon size cheat sheet")

    args = parser.parse_args()

    if args.sizes:
        print_sizes()
        sys.exit(0)

    if args.html:
        print(generate_html(args.theme_color))
        sys.exit(0)

    if args.manifest:
        print(generate_manifest(args.theme_color, args.app_name))
        sys.exit(0)

    if args.text:
        print(generate_favicon(args.text, args.bg, args.fg, args.shape))
    elif args.icon:
        print(generate_icon(args.icon, args.bg, args.fg))
    else:
        print("Specify one of: --text, --icon, --html, --manifest, --sizes")
        print("Example: python favicon_generator.py --text CR --bg #2563EB")
