#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Theme Exporter - Export design themes to CSS, Tailwind, SCSS, and JSON formats
Cyber-Rage Design Intelligence Engine

Usage: python theme_exporter.py "#2563EB" [--format css|tailwind|scss|json|all] [--name "brand"]
"""

import json
import argparse
import sys
import io
from color_tools import ColorTools, generate_theme, generate_palette

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def export_css(theme, name="brand"):
    h, s, l = ColorTools.hex_to_hsl(theme["primary"]["base"])
    primary = theme["primary"]["base"]
    secondary = theme["secondary"]["base"]
    accent = theme["accent"]["base"]

    lines = []
    lines.append(f"/* {name.capitalize()} Theme - CSS Custom Properties */")
    lines.append(":root {")
    lines.append(f"  --{name}-primary: {primary};")
    lines.append(f"  --{name}-secondary: {secondary};")
    lines.append(f"  --{name}-accent: {accent};")
    lines.append(f"  --{name}-success: {theme['success']['base']};")
    lines.append(f"  --{name}-warning: {theme['warning']['base']};")
    lines.append(f"  --{name}-error: {theme['error']['base']};")
    lines.append(f"  --{name}-info: {theme['info']['base']};")
    lines.append("")

    # Primary scale
    lines.append(f"  /* {name} primary scale */")
    for shade, color in theme["primary"]["shades"].items():
        lines.append(f"  --{name}-primary-{shade}: {color};")
    lines.append("")

    # Neutrals
    lines.append(f"  /* {name} neutrals */")
    for shade, color in theme["primary"]["neutrals"].items():
        lines.append(f"  --{name}-neutral-{shade}: {color};")
    lines.append("")

    # Light mode
    lines.append("  /* Light mode */")
    for key, value in theme["light_mode"].items():
        lines.append(f"  --{name}-{key.replace('_', '-')}: {value};")
    lines.append("}")

    # Dark mode
    lines.append("")
    lines.append("@media (prefers-color-scheme: dark) {")
    lines.append("  :root {")
    for key, value in theme["dark_mode"].items():
        lines.append(f"    --{name}-{key.replace('_', '-')}: {value};")
    lines.append("  }")
    lines.append("}")

    # Gradient
    gradient = theme.get("gradient", {})
    if gradient:
        lines.append("")
        lines.append("/* Gradients */")
        lines.append(f"--{name}-gradient: {gradient['css_linear']};")

    return "\n".join(lines)


def export_tailwind(theme, name="brand"):
    primary_shades = theme["primary"]["shades"]
    secondary_shades = theme["secondary"]["shades"]
    accent_shades = theme["accent"]["shades"]

    config = {
        "theme": {
            "extend": {
                "colors": {
                    "primary": primary_shades,
                    "secondary": secondary_shades,
                    "accent": accent_shades,
                    "success": theme["success"]["shades"],
                    "warning": theme["warning"]["shades"],
                    "error": theme["error"]["shades"],
                    "info": theme["info"]["shades"],
                }
            }
        }
    }
    return json.dumps(config, indent=2)


def export_scss(theme, name="brand"):
    lines = []
    lines.append(f"// {name.capitalize()} Theme - SCSS Variables")
    lines.append(f"$brand-primary: {theme['primary']['base']};")
    lines.append(f"$brand-secondary: {theme['secondary']['base']};")
    lines.append(f"$brand-accent: {theme['accent']['base']};")
    lines.append(f"$brand-success: {theme['success']['base']};")
    lines.append(f"$brand-warning: {theme['warning']['base']};")
    lines.append(f"$brand-error: {theme['error']['base']};")
    lines.append(f"$brand-info: {theme['info']['base']};")
    lines.append("")

    lines.append("// Primary scale")
    for shade, color in theme["primary"]["shades"].items():
        lines.append(f"$brand-primary-{shade}: {color};")
    lines.append("")

    lines.append("// Neutrals")
    for shade, color in theme["primary"]["neutrals"].items():
        lines.append(f"$brand-neutral-{shade}: {color};")
    lines.append("")

    lines.append("// Light mode")
    for key, value in theme["light_mode"].items():
        lines.append(f"$brand-{key.replace('_', '-')}: {value};")
    lines.append("")

    lines.append("// Dark mode")
    for key, value in theme["dark_mode"].items():
        lines.append(f"$brand-dark-{key.replace('_', '-')}: {value};")

    gradient = theme.get("gradient", {})
    if gradient:
        lines.append("")
        lines.append("// Gradient")
        lines.append(f"$brand-gradient: {gradient['css_linear']};")

    return "\n".join(lines)


def export_json(theme, name="brand"):
    return json.dumps({
        "name": name,
        "colors": {
            "primary": theme["primary"]["base"],
            "primaryScale": theme["primary"]["shades"],
            "secondary": theme["secondary"]["base"],
            "secondaryScale": theme["secondary"]["shades"],
            "accent": theme["accent"]["base"],
            "accentScale": theme["accent"]["shades"],
            "semantic": {
                "success": theme["success"]["base"],
                "warning": theme["warning"]["base"],
                "error": theme["error"]["base"],
                "info": theme["info"]["base"],
            },
            "neutrals": theme["primary"]["neutrals"],
        },
        "lightMode": theme["light_mode"],
        "darkMode": theme["dark_mode"],
        "gradient": theme.get("gradient", {}).get("css_linear", ""),
    }, indent=2)


def export_all(theme, name="brand"):
    output = []
    output.append("=" * 60)
    output.append("  THEME EXPORT - ALL FORMATS")
    output.append("=" * 60)
    output.append("")
    output.append("### 1. CSS ###")
    output.append(export_css(theme, name))
    output.append("")
    output.append("### 2. TAILWIND ###")
    output.append(export_tailwind(theme, name))
    output.append("")
    output.append("### 3. SCSS ###")
    output.append(export_scss(theme, name))
    output.append("")
    output.append("### 4. JSON ###")
    output.append(export_json(theme, name))
    return "\n".join(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Theme Exporter - Cyber-Rage")
    parser.add_argument("color", help="Base color (hex)")
    parser.add_argument("--format", "-f", choices=["css", "tailwind", "scss", "json", "all"], default="all", help="Output format")
    parser.add_argument("--name", "-n", type=str, default="brand", help="Theme/color variable name")

    args = parser.parse_args()

    theme = generate_theme(args.color)

    if args.format == "css":
        print(export_css(theme, args.name))
    elif args.format == "tailwind":
        print(export_tailwind(theme, args.name))
    elif args.format == "scss":
        print(export_scss(theme, args.name))
    elif args.format == "json":
        print(export_json(theme, args.name))
    else:
        print(export_all(theme, args.name))
