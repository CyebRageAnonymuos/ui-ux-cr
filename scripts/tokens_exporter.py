#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tokens Exporter - Export a full design-token set from one brand color
in the W3C Design Tokens draft format AND the Figma Tokens plugin format,
plus Style Dictionary config to build CSS/Android/iOS from them.
Cyber-Rage Design Intelligence Engine

Usage: python tokens_exporter.py "#2563EB" --name brand
       python tokens_exporter.py "#A855F7" --format w3c
       python tokens_exporter.py "#10B981" --format figma
       python tokens_exporter.py "#F97316" --format style-dictionary
"""

import argparse
import json
import sys
import io
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from color_tools import generate_palette, check_contrast, ColorTools

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def w3c_tokens(hex_color, name="brand"):
    """W3C Design Tokens draft format ($value/$type per token)."""
    p = generate_palette(hex_color, "complementary")
    on_light = "#0F172A"
    on_dark = "#F8FAFC"

    def color_token(value, desc=""):
        return {"$value": value, "$type": "color", "$description": desc}

    tokens = {
        name: {
            "color": {
                "primary": {shade: color_token(c) for shade, c in p["shades"].items()},
                "neutral": {shade: color_token(c) for shade, c in p["neutrals"].items()},
                "accent": {
                    "complement": color_token(p["harmony_colors"][0], "complementary accent"),
                },
                "font": {
                    "on-light": color_token(on_light),
                    "on-dark": color_token(on_dark),
                },
            },
            "font": {
                "family": {
                    "heading": {"$value": "Inter, system-ui, sans-serif", "$type": "fontFamily"},
                    "body": {"$value": "Inter, system-ui, sans-serif", "$type": "fontFamily"},
                },
                "size": {
                    "sm": {"$value": "0.875rem", "$type": "dimension"},
                    "base": {"$value": "1rem", "$type": "dimension"},
                    "lg": {"$value": "1.125rem", "$type": "dimension"},
                    "xl": {"$value": "1.25rem", "$type": "dimension"},
                    "2xl": {"$value": "1.5rem", "$type": "dimension"},
                },
                "weight": {
                    "normal": {"$value": "400", "$type": "fontWeight"},
                    "medium": {"$value": "500", "$type": "fontWeight"},
                    "bold": {"$value": "700", "$type": "fontWeight"},
                },
            },
            "space": {
                key: {"$value": f"{v * 4}px", "$type": "dimension"}
                for key, v in {
                    "1": 1, "2": 2, "3": 3, "4": 4, "6": 6, "8": 8, "12": 12, "16": 16,
                }.items()
            },
            "radius": {
                "sm": {"$value": "6px", "$type": "dimension"},
                "md": {"$value": "10px", "$type": "dimension"},
                "lg": {"$value": "16px", "$type": "dimension"},
                "full": {"$value": "9999px", "$type": "dimension"},
            },
            "shadow": {
                "sm": {"$value": "0 1px 3px rgba(0,0,0,0.1)", "$type": "shadow"},
                "md": {"$value": "0 6px 24px rgba(0,0,0,0.12)", "$type": "shadow"},
                "lg": {"$value": "0 20px 50px rgba(0,0,0,0.16)", "$type": "shadow"},
            },
        }
    }
    return json.dumps(tokens, indent=2)


def figma_tokens(hex_color, name="brand"):
    """Figma Tokens (Tokens Studio) plugin format."""
    p = generate_palette(hex_color, "complementary")

    def set_entry(shades):
        return {
            shade: {"value": c, "type": "color"}
            for shade, c in shades.items()
        }

    data = {
        "global": {
            name: set_entry(p["shades"]),
            f"{name}-neutral": set_entry(p["neutrals"]),
            "accent": {"complement": {"value": p["harmony_colors"][0], "type": "color"}},
            "font-families": {
                "heading": {"value": "Inter", "type": "fontFamilies"},
                "body": {"value": "Inter", "type": "fontFamilies"},
            },
            "font-sizes": {
                "sm": {"value": "14", "type": "fontSizes"},
                "base": {"value": "16", "type": "fontSizes"},
                "lg": {"value": "18", "type": "fontSizes"},
                "xl": {"value": "20", "type": "fontSizes"},
            },
            "border-radius": {
                "sm": {"value": "6", "type": "borderRadius"},
                "md": {"value": "10", "type": "borderRadius"},
                "lg": {"value": "16", "type": "borderRadius"},
            },
            "spacing": {
                key: {"value": str(v * 4), "type": "spacing"}
                for key, v in {"xs": 1, "sm": 2, "md": 4, "lg": 6, "xl": 8, "2xl": 12}.items()
            },
        },
        "components": {
            "button": {
                "borderRadius": {"value": "{border-radius.md}", "type": "borderRadius"},
                "paddingX": {"value": "{spacing.md}", "type": "spacing"},
                "paddingY": {"value": "{spacing.xs}", "type": "spacing"},
            },
            "card": {
                "borderRadius": {"value": "{border-radius.lg}", "type": "borderRadius"},
                "shadow": {"value": "0 6px 24px rgba(0,0,0,0.12)", "type": "boxShadow"},
            },
        },
    }
    return json.dumps(data, indent=2)


def style_dictionary_config(hex_color, name="brand"):
    """Style Dictionary config + a ready tokens.json for build pipelines."""
    config = {
        "source": ["tokens.json"],
        "platforms": {
            "css": {
                "transformGroup": "css",
                "buildPath": "build/css/",
                "files": [{"destination": "tokens.css", "format": "css/variables"}],
            },
            "scss": {
                "transformGroup": "scss",
                "buildPath": "build/scss/",
                "files": [{"destination": "_tokens.scss", "format": "scss/variables"}],
            },
            "android": {
                "transformGroup": "android",
                "buildPath": "build/android/",
                "files": [{"destination": "colors.xml", "format": "android/colors"}],
            },
            "ios": {
                "transformGroup": "ios-swift",
                "buildPath": "build/ios/",
                "files": [{"destination": "Tokens.swift", "format": "ios-swift/class.swift"}],
            },
        },
    }
    note = f"""/* Style Dictionary pipeline
1) Save the W3C output (--format w3c) as tokens.json next to this config
2) npm install style-dictionary
3) npx style-dictionary build --config ./config.json
Generates CSS variables, SCSS variables, Android colors.xml and iOS Swift.
*/
"""
    return note + json.dumps(config, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tokens Exporter - Cyber-Rage")
    parser.add_argument("color", help="Base color (hex)")
    parser.add_argument("--name", default="brand", help="Token namespace (default 'brand')")
    parser.add_argument("--format", choices=["w3c", "figma", "style-dictionary"],
                        default="w3c", help="Token format (default w3c)")
    parser.add_argument("--out", help="Write to file instead of stdout")

    args = parser.parse_args()

    if not args.color.startswith("#") or len(args.color) != 7:
        print("Please provide a 6-digit hex color like #2563EB", file=sys.stderr)
        sys.exit(1)

    # Fail fast on invalid hex
    try:
        ColorTools.hex_to_rgb(args.color)
    except ValueError:
        print(f"Invalid hex color: {args.color}", file=sys.stderr)
        sys.exit(1)

    exporters = {
        "w3c": w3c_tokens,
        "figma": figma_tokens,
        "style-dictionary": style_dictionary_config,
    }
    output = exporters[args.format](args.color, args.name)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output + "\n")
        print(f"Tokens written to {args.out} ({len(output)} bytes)")
    else:
        print(output)
