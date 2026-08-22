#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Icon Spriter - Build an SVG symbol sprite sheet from svg_generator's
icon set (or a directory of your own SVGs) + ready-to-use <use> markup
and an on-demand loader snippet.
Cyber-Rage Design Intelligence Engine

Usage: python icon_spriter.py --icons search,check,plus,x
       python icon_spriter.py --all
       python icon_spriter.py --dir ./my-icons
       python icon_spriter.py --list
"""

import argparse
import os
import re
import sys
import io

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def get_available_icons():
    import svg_generator
    return sorted(getattr(svg_generator, "ICONS", {}).keys())


def icon_body(icon_name):
    """Pull a single icon's inner markup from svg_generator's ICONS.

    ICONS values come in two shapes: raw SVG element markup (contains
    '<circle .../>' etc.) or bare SVG path data ('M12 12L...'). Only the
    latter gets wrapped in a <path>; wrapping markup produces invalid
    nested-attribute output.
    """
    import svg_generator
    icons = getattr(svg_generator, "ICONS", None)
    if icons is None:
        return None
    entry = icons.get(icon_name)
    if entry is None:
        return None
    if isinstance(entry, str):
        if "<svg" in entry:
            inner = re.sub(r"^.*?<svg[^>]*>", "", entry, flags=re.DOTALL)
            inner = re.sub(r"</svg>\s*$", "", inner)
            return inner.strip()
        if "<" in entry:  # element markup (circle/line/path/...) without wrapper
            return entry.strip()
        return f'<path d="{entry}"/>'
    return None


def sprite_from_svg_dir(directory):
    """Wrap each .svg file in the directory as a <symbol>."""
    symbols = []
    names = []
    for fname in sorted(os.listdir(directory)):
        if not fname.endswith(".svg"):
            continue
        with open(os.path.join(directory, fname), encoding="utf-8") as f:
            content = f.read()
        inner = re.sub(r"^.*?<svg[^>]*>", "", content, flags=re.DOTALL | re.IGNORECASE)
        inner = re.sub(r"</svg>\s*$", "", inner, flags=re.DOTALL | re.IGNORECASE).strip()
        symbol_id = re.sub(r"[^a-z0-9-]", "-", fname[:-4].lower())
        symbols.append(f'  <symbol id="i-{symbol_id}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n    {inner}\n  </symbol>')
        names.append(symbol_id)
    return symbols, names


def build_sprite(symbols):
    return f"""<!-- SVG sprite sheet (save as icons.svg, include once per page) -->
<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">
{chr(10).join(symbols)}
</svg>"""


def usage_snippet(names):
    examples = names[:4] if names else ["search"]
    uses = "\n".join(
        f'<svg class="icon" aria-hidden="true"><use href="icons.svg#i-{n}"/></svg>'
        for n in examples
    )
    all_ids = ", ".join(f"i-{n}" for n in names) if names else "(none)"
    return f"""
<!-- ===== Usage ===== -->
<!-- 1) Include the sprite once, right after <body> opens -->
<!-- 2) Reference icons anywhere: -->
{uses}

<!-- Available symbol IDs: {all_ids} -->

<!-- Icon sizing (icons inherit currentColor): -->
<style>
  .icon {{
    width: 24px;
    height: 24px;
    fill: none;
    stroke: currentColor;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex-shrink: 0;
  }}
</style>

<!-- Accessible labeled icon: -->
<button type="button" aria-label="Search">
  <svg class="icon" aria-hidden="true"><use href="icons.svg#i-search"/></svg>
</button>"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Icon Spriter - Cyber-Rage")
    parser.add_argument("--icons", help="Comma-separated icon names from svg_generator (e.g. search,check,plus)")
    parser.add_argument("--all", action="store_true", help="Sprite ALL built-in icons")
    parser.add_argument("--dir", help="Sprite every .svg file in a directory instead")
    parser.add_argument("--out", help="Write sprite to file (icons.svg)")
    parser.add_argument("--list", action="store_true", help="List available built-in icons")

    args = parser.parse_args()

    if args.list:
        icons = get_available_icons()
        print(f"Built-in icons ({len(icons)}):")
        print("  " + ", ".join(icons))
        sys.exit(0)

    symbols, names = [], []

    if args.dir:
        if not os.path.isdir(args.dir):
            print(f"Not a directory: {args.dir}", file=sys.stderr)
            sys.exit(1)
        symbols, names = sprite_from_svg_dir(args.dir)
    elif args.all:
        for name in get_available_icons():
            body = icon_body(name)
            if body:
                symbols.append(
                    f'  <symbol id="i-{name}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n    {body}\n  </symbol>'
                )
                names.append(name)
    elif args.icons:
        wanted = [i.strip() for i in args.icons.split(",") if i.strip()]
        missing = []
        for name in wanted:
            body = icon_body(name)
            if body is None:
                missing.append(name)
                continue
            symbols.append(
                f'  <symbol id="i-{name}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n    {body}\n  </symbol>'
            )
            names.append(name)
        if missing:
            available = get_available_icons()
            print(f"Unknown icons: {', '.join(missing)}", file=sys.stderr)
            print(f"Available ({len(available)}): {', '.join(available[:40])}...", file=sys.stderr)
            if not names:
                sys.exit(1)
    else:
        print("Specify --icons, --all, --dir, or --list")
        sys.exit(1)

    if not symbols:
        print("No icons found to sprite.", file=sys.stderr)
        sys.exit(1)

    sprite = build_sprite(symbols)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(sprite + "\n")
        print(f"Sprite written to {args.out} ({len(symbols)} icons)")
    else:
        print(sprite)
        print(usage_snippet(names))
