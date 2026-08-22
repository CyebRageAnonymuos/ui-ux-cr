#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Color Tools v2.0 - Advanced Palette Generator, WCAG Contrast Analyzer,
Gradient Generator, Theme Generator, Color Blind Simulator, Color Mixer
Cyber-Rage Design Intelligence Engine
"""

import re
import json
from math import sqrt, pi, cos, sin, atan2, degrees

class ColorTools:
    """Advanced color manipulation tools v2.0"""

    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(r, g, b):
        r = max(0, min(255, int(r)))
        g = max(0, min(255, int(g)))
        b = max(0, min(255, int(b)))
        return f"#{r:02x}{g:02x}{b:02x}"

    @staticmethod
    def hex_to_hsl(hex_color):
        r, g, b = ColorTools.hex_to_rgb(hex_color)
        r, g, b = r / 255, g / 255, b / 255
        max_c, min_c = max(r, g, b), min(r, g, b)
        l = (max_c + min_c) / 2
        if max_c == min_c:
            h = s = 0
        else:
            d = max_c - min_c
            s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
            if max_c == r:
                h = (g - b) / d + (6 if g < b else 0)
            elif max_c == g:
                h = (b - r) / d + 2
            else:
                h = (r - g) / d + 4
            h /= 6
        return int(h * 360), int(s * 100), int(l * 100)

    @staticmethod
    def hsl_to_hex(h, s, l):
        s = max(0, min(100, s)) / 100
        l = max(0, min(100, l)) / 100
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = l - c / 2
        if h < 60:
            r, g, b = c, x, 0
        elif h < 120:
            r, g, b = x, c, 0
        elif h < 180:
            r, g, b = 0, c, x
        elif h < 240:
            r, g, b = 0, x, c
        elif h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        return ColorTools.rgb_to_hex(int((r + m) * 255), int((g + m) * 255), int((b + m) * 255))

    @staticmethod
    def hex_to_hsv(hex_color):
        r, g, b = ColorTools.hex_to_rgb(hex_color)
        r, g, b = r / 255, g / 255, b / 255
        max_c, min_c = max(r, g, b), min(r, g, b)
        v = max_c
        if max_c == 0:
            s = 0
        else:
            s = (max_c - min_c) / max_c
        if max_c == min_c:
            h = 0
        elif max_c == r:
            h = (g - b) / (max_c - min_c) + (6 if g < b else 0)
        elif max_c == g:
            h = (b - r) / (max_c - min_c) + 2
        else:
            h = (r - g) / (max_c - min_c) + 4
        h /= 6
        return int(h * 360), int(s * 100), int(v * 100)

    @staticmethod
    def hex_to_cmyk(hex_color):
        r, g, b = ColorTools.hex_to_rgb(hex_color)
        r, g, b = r / 255, g / 255, b / 255
        k = 1 - max(r, g, b)
        if k == 1:
            return 0, 0, 0, 100
        c = (1 - r - k) / (1 - k) * 100
        m = (1 - g - k) / (1 - k) * 100
        y = (1 - b - k) / (1 - k) * 100
        return int(c), int(m), int(y), int(k * 100)

    @staticmethod
    def mix_colors(color1, color2, ratio=0.5):
        """Mix two colors with given ratio (0 = all color1, 1 = all color2)"""
        r1, g1, b1 = ColorTools.hex_to_rgb(color1)
        r2, g2, b2 = ColorTools.hex_to_rgb(color2)
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        return ColorTools.rgb_to_hex(r, g, b)

    @staticmethod
    def relative_luminance(hex_color):
        """Calculate relative luminance for WCAG contrast"""
        r, g, b = ColorTools.hex_to_rgb(hex_color)
        r, g, b = r / 255, g / 255, b / 255
        r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
        g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
        b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    @staticmethod
    def contrast_ratio(color1, color2):
        """Calculate contrast ratio between two colors"""
        l1 = ColorTools.relative_luminance(color1)
        l2 = ColorTools.relative_luminance(color2)
        lighter = max(l1, l2)
        darker = min(l1, l2)
        return (lighter + 0.05) / (darker + 0.05)

    @staticmethod
    def adjust_brightness(hex_color, factor):
        """Adjust brightness of a color (factor > 1 = brighter, < 1 = darker)"""
        h, s, l = ColorTools.hex_to_hsl(hex_color)
        new_l = max(0, min(100, l * factor))
        return ColorTools.hsl_to_hex(h, s, new_l)

    @staticmethod
    def adjust_saturation(hex_color, factor):
        """Adjust saturation of a color"""
        h, s, l = ColorTools.hex_to_hsl(hex_color)
        new_s = max(0, min(100, s * factor))
        return ColorTools.hsl_to_hex(h, new_s, l)

    @staticmethod
    def simulate_protanopia(hex_color):
        """Simulate red-blind color blindness"""
        r, g, b = ColorTools.hex_to_rgb(hex_color)
        return ColorTools.rgb_to_hex(
            0.56667 * r + 0.43333 * g,
            0.55833 * r + 0.44167 * g,
            b
        )

    @staticmethod
    def simulate_deuteranopia(hex_color):
        """Simulate green-blind color blindness"""
        r, g, b = ColorTools.hex_to_rgb(hex_color)
        return ColorTools.rgb_to_hex(
            0.625 * r + 0.375 * g,
            0.7 * r + 0.3 * g,
            b
        )

    @staticmethod
    def simulate_tritanopia(hex_color):
        """Simulate blue-blind color blindness"""
        r, g, b = ColorTools.hex_to_rgb(hex_color)
        return ColorTools.rgb_to_hex(
            r,
            0.95 * g + 0.05 * b,
            0.95 * b + 0.05 * g
        )

    @staticmethod
    def is_light(hex_color):
        """Check if a color is perceived as light"""
        h, s, l = ColorTools.hex_to_hsl(hex_color)
        return l > 50

    @staticmethod
    def temperature(hex_color):
        """Estimate color temperature (warm vs cool)"""
        r, g, b = ColorTools.hex_to_rgb(hex_color)
        warmth = (r - b) / 255
        if warmth > 0.2:
            return "warm"
        elif warmth < -0.2:
            return "cool"
        return "neutral"


def generate_palette(hex_color, harmony="complementary", include_neutrals=True):
    """Generate a color palette from a single color with advanced options"""
    h, s, l = ColorTools.hex_to_hsl(hex_color)
    palette = {
        "base": hex_color,
        "harmony": harmony,
        "shades": {},
        "harmony_colors": [],
        "neutrals": {},
        "analogous_palette": [],
        "luminance": round(ColorTools.relative_luminance(hex_color), 4),
        "temperature": ColorTools.temperature(hex_color),
        "is_light": ColorTools.is_light(hex_color)
    }

    # Generate shades (50-900) with better distribution
    for shade in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]:
        if shade <= 500:
            lightness = 95 - (shade / 500) * 45
        else:
            lightness = 50 - ((shade - 500) / 400) * 40
        palette["shades"][str(shade)] = ColorTools.hsl_to_hex(h, s, int(lightness))

    # Generate harmony colors
    if harmony == "complementary":
        palette["harmony_colors"] = [
            ColorTools.hsl_to_hex((h + 180) % 360, s, l)
        ]
    elif harmony == "analogous":
        palette["harmony_colors"] = [
            ColorTools.hsl_to_hex((h - 30) % 360, s, l),
            ColorTools.hsl_to_hex((h + 30) % 360, s, l)
        ]
    elif harmony == "triadic":
        palette["harmony_colors"] = [
            ColorTools.hsl_to_hex((h + 120) % 360, s, l),
            ColorTools.hsl_to_hex((h + 240) % 360, s, l)
        ]
    elif harmony == "split_complementary":
        palette["harmony_colors"] = [
            ColorTools.hsl_to_hex((h + 150) % 360, s, l),
            ColorTools.hsl_to_hex((h + 210) % 360, s, l)
        ]
    elif harmony == "tetradic":
        palette["harmony_colors"] = [
            ColorTools.hsl_to_hex((h + 90) % 360, s, l),
            ColorTools.hsl_to_hex((h + 180) % 360, s, l),
            ColorTools.hsl_to_hex((h + 270) % 360, s, l)
        ]
    elif harmony == "monochromatic":
        palette["harmony_colors"] = [
            ColorTools.hsl_to_hex(h, s, max(10, l - 30)),
            ColorTools.hsl_to_hex(h, s, min(90, l + 30)),
            ColorTools.hsl_to_hex(h, s, max(5, l - 50)),
            ColorTools.hsl_to_hex(h, s, min(95, l + 50)),
        ]

    if include_neutrals:
        palette["neutrals"] = {
            "50": ColorTools.hsl_to_hex(h, 4, 97),
            "100": ColorTools.hsl_to_hex(h, 4, 93),
            "200": ColorTools.hsl_to_hex(h, 4, 85),
            "300": ColorTools.hsl_to_hex(h, 4, 72),
            "400": ColorTools.hsl_to_hex(h, 4, 60),
            "500": ColorTools.hsl_to_hex(h, 4, 50),
            "600": ColorTools.hsl_to_hex(h, 4, 40),
            "700": ColorTools.hsl_to_hex(h, 4, 30),
            "800": ColorTools.hsl_to_hex(h, 4, 20),
            "900": ColorTools.hsl_to_hex(h, 4, 10)
        }

    # Generate analogous palette (5 colors, 30 degrees apart)
    for i in range(-2, 3):
        palette["analogous_palette"].append(
            ColorTools.hsl_to_hex((h + i * 30) % 360, s, l)
        )

    return palette


def generate_gradient(start_color, end_color, steps=5, style="linear"):
    """Generate gradient between two colors with middle steps"""
    colors = [ColorTools.mix_colors(start_color, end_color, i/(steps-1)) for i in range(steps)]
    r1, g1, b1 = ColorTools.hex_to_rgb(start_color)
    r2, g2, b2 = ColorTools.hex_to_rgb(end_color)

    gradient = {
        "start": start_color,
        "end": end_color,
        "steps": steps,
        "colors": colors,
        "style": style,
        "css_linear": f"linear-gradient(135deg, {start_color}, {end_color})",
        "css_radial": f"radial-gradient(circle at center, {start_color}, {end_color})",
        "all_steps": colors
    }
    return gradient


def generate_multi_gradient(colors, style="linear"):
    """Generate multi-stop gradient"""
    stops = ", ".join(colors)
    return {
        "colors": colors,
        "style": style,
        "css_linear": f"linear-gradient(135deg, {stops})",
        "css_radial": f"radial-gradient(circle at center, {stops})",
        "css_conic": f"conic-gradient(from 45deg, {stops})",
    }


def check_contrast(fg_color, bg_color):
    """Check contrast ratio and WCAG compliance"""
    ratio = ColorTools.contrast_ratio(fg_color, bg_color)

    result = {
        "foreground": fg_color,
        "background": bg_color,
        "ratio": round(ratio, 2),
        "wcag_aa_normal": ratio >= 4.5,
        "wcag_aa_large": ratio >= 3,
        "wcag_aaa_normal": ratio >= 7,
        "wcag_aaa_large": ratio >= 4.5,
        "grade": ""
    }

    if ratio >= 7:
        result["grade"] = "AAA (Excellent)"
    elif ratio >= 4.5:
        result["grade"] = "AA (Good)"
    elif ratio >= 3:
        result["grade"] = "AA Large Only (Acceptable for large text)"
    else:
        result["grade"] = "FAIL (Insufficient contrast)"

    return result


def suggest_text_color(bg_color):
    """Suggest whether to use light or dark text on a background"""
    if ColorTools.is_light(bg_color):
        return "#0F172A"
    return "#F8FAFC"


def generate_theme(hex_color, include_css_vars=True):
    """Generate a complete theme from a single color v2.0"""
    h, s, l = ColorTools.hex_to_hsl(hex_color)

    # Generate primary palette
    primary = generate_palette(hex_color, "monochromatic")

    # Generate secondary (complementary)
    secondary_h = (h + 180) % 360
    secondary = generate_palette(ColorTools.hsl_to_hex(secondary_h, s, l), "monochromatic")

    # Generate accent (analogous +30)
    accent_h = (h + 30) % 360
    accent = generate_palette(ColorTools.hsl_to_hex(accent_h, s, l), "monochromatic")

    # Generate semantic colors
    success = generate_palette("#22c55e", "monochromatic")
    warning = generate_palette("#f59e0b", "monochromatic")
    error = generate_palette("#ef4444", "monochromatic")
    info = generate_palette("#3b82f6", "monochromatic")

    theme = {
        "primary": primary,
        "secondary": secondary,
        "accent": accent,
        "success": success,
        "warning": warning,
        "error": error,
        "info": info,
        "light_mode": {
            "background": "#ffffff",
            "surface": "#f8fafc",
            "text": "#0f172a",
            "text_secondary": "#64748b",
            "border": "#e2e8f0",
            "overlay": "rgba(0,0,0,0.5)",
            "shadow": "rgba(0,0,0,0.1)"
        },
        "dark_mode": {
            "background": "#0f172a",
            "surface": "#1e293b",
            "text": "#f8fafc",
            "text_secondary": "#94a3b8",
            "border": "#334155",
            "overlay": "rgba(0,0,0,0.7)",
            "shadow": "rgba(0,0,0,0.3)"
        },
        "gradient": generate_gradient(hex_color, ColorTools.hsl_to_hex((h + 180) % 360, s, l), 5),
        "contrast": check_contrast(hex_color, "#ffffff")
    }

    if include_css_vars:
        theme["css_variables"] = generate_css_variables(theme)

    return theme


def generate_css_variables(theme):
    """Generate CSS custom properties from theme"""
    vars = {}
    for mode in ["light_mode", "dark_mode"]:
        if mode in theme:
            for key, value in theme[mode].items():
                vars[f"--{key.replace('_', '-')}"] = value

    # Add color shades
    for palette_name in ["primary", "secondary", "accent"]:
        if palette_name in theme:
            for shade, color in theme[palette_name].get("shades", {}).items():
                vars[f"--{palette_name}-{shade}"] = color

    # Add semantic colors
    for semantic in ["success", "warning", "error", "info"]:
        if semantic in theme:
            for shade, color in theme[semantic].get("shades", {}).items():
                vars[f"--{semantic}-{shade}"] = color

    return vars


def generate_tailwind_config(theme):
    """Generate Tailwind config extension from theme"""
    config = {
        "theme": {
            "extend": {
                "colors": {}
            }
        }
    }

    for palette_name in ["primary", "secondary", "accent"]:
        if palette_name in theme:
            config["theme"]["extend"]["colors"][palette_name] = {}
            for shade, color in theme[palette_name].get("shades", {}).items():
                config["theme"]["extend"]["colors"][palette_name][shade] = color

    for semantic in ["success", "warning", "error", "info"]:
        if semantic in theme:
            config["theme"]["extend"]["colors"][semantic] = {}
            for shade, color in theme[semantic].get("shades", {}).items():
                config["theme"]["extend"]["colors"][semantic][shade] = color

    return config


def format_palette_output(palette, format="ascii"):
    """Format palette output"""
    if format == "json":
        return json.dumps(palette, indent=2)

    lines = []
    width = 70
    lines.append("=" * width)
    lines.append(f"  COLOR PALETTE - {palette['harmony'].upper()}")
    lines.append("  Temperature: {temp} | Light: {light} | Luminance: {lum}".format(
        temp=palette.get('temperature', 'N/A'),
        light=palette.get('is_light', True),
        lum=palette.get('luminance', 'N/A')
    ))
    lines.append("=" * width)
    lines.append("")
    lines.append(f"  Base Color: {palette['base']}")
    lines.append("")

    lines.append("  Shades (50-900):")
    for shade, color in palette['shades'].items():
        lines.append(f"    {shade}: {color}")

    lines.append("")
    lines.append(f"  Harmony Colors ({palette['harmony']}):")
    for i, color in enumerate(palette['harmony_colors'], 1):
        lines.append(f"    {i}: {color}")

    if palette.get('analogous_palette'):
        lines.append("")
        lines.append("  Analogous Palette:")
        for i, color in enumerate(palette['analogous_palette'], 1):
            lines.append(f"    {i}: {color}")

    if palette.get('neutrals'):
        lines.append("")
        lines.append("  Neutrals:")
        for shade, color in palette['neutrals'].items():
            lines.append(f"    {shade}: {color}")

    lines.append("")
    lines.append("=" * width)

    return "\n".join(lines)


def format_contrast_output(result, format="ascii"):
    """Format contrast check output"""
    if format == "json":
        return json.dumps(result, indent=2)

    lines = []
    width = 60
    lines.append("=" * width)
    lines.append("  CONTRAST CHECK")
    lines.append("=" * width)
    lines.append("")
    lines.append(f"  Foreground: {result['foreground']}")
    lines.append(f"  Background: {result['background']}")
    lines.append(f"  Ratio: {result['ratio']}:1")
    lines.append(f"  Grade: {result['grade']}")
    lines.append("")
    lines.append("  WCAG Compliance:")
    lines.append(f"    AA Normal Text (4.5:1):  {'PASS' if result['wcag_aa_normal'] else 'FAIL'}")
    lines.append(f"    AA Large Text (3:1):     {'PASS' if result['wcag_aa_large'] else 'FAIL'}")
    lines.append(f"    AAA Normal Text (7:1):   {'PASS' if result['wcag_aaa_normal'] else 'FAIL'}")
    lines.append(f"    AAA Large Text (4.5:1):  {'PASS' if result['wcag_aaa_large'] else 'FAIL'}")
    lines.append("")
    lines.append("=" * width)

    return "\n".join(lines)


def format_theme_output(theme, format="ascii"):
    """Format theme output"""
    if format == "json":
        return json.dumps(theme, indent=2, default=str)

    lines = []
    width = 70
    lines.append("=" * width)
    lines.append("  GENERATED THEME")
    lines.append("=" * width)
    lines.append("")

    for section in ["primary", "secondary", "accent"]:
        if section in theme:
            lines.append(f"  {section.upper()} COLORS:")
            lines.append(f"    Base: {theme[section]['base']}")
            for shade, color in list(theme[section].get('shades', {}).items())[::2]:
                lines.append(f"    {shade}: {color}")
            lines.append("")

    lines.append("  SEMANTIC COLORS:")
    for semantic in ["success", "warning", "error", "info"]:
        if semantic in theme:
            lines.append(f"    {semantic.title()}: {theme[semantic]['base']}")
    lines.append("")

    if theme.get("gradient"):
        g = theme["gradient"]
        lines.append("  GRADIENT:")
        lines.append(f"    CSS: {g['css_linear']}")
        for i, c in enumerate(g['all_steps']):
            lines.append(f"    Step {i+1}: {c}")
        lines.append("")

    lines.append("  LIGHT MODE:")
    for key, value in theme.get('light_mode', {}).items():
        lines.append(f"    {key}: {value}")
    lines.append("")

    lines.append("  DARK MODE:")
    for key, value in theme.get('dark_mode', {}).items():
        lines.append(f"    {key}: {value}")
    lines.append("")

    lines.append("  CONTRAST CHECK:")
    if theme.get("contrast"):
        c = theme["contrast"]
        lines.append(f"    Primary on White: {c['ratio']}:1 ({c['grade']})")
    lines.append("")

    if theme.get("css_variables"):
        lines.append("  CSS VARIABLES (sample):")
        vars_list = list(theme["css_variables"].items())[:10]
        for key, value in vars_list:
            lines.append(f"    {key}: {value}")
    lines.append("")

    lines.append("=" * width)

    return "\n".join(lines)


# ============ CLI SUPPORT ============
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Color Tools v2 - Cyber-Rage")
    parser.add_argument("color", help="Base color (hex)")
    parser.add_argument("--harmony", choices=["complementary", "analogous", "triadic", "split_complementary", "tetradic", "monochromatic"], default="complementary", help="Color harmony")
    parser.add_argument("--check-contrast", metavar="BG_COLOR", help="Check contrast against background color")
    parser.add_argument("--generate-theme", action="store_true", help="Generate complete theme")
    parser.add_argument("--gradient", metavar="END_COLOR", help="Generate gradient between two colors")
    parser.add_argument("--mix", metavar="RATIO", type=float, help="Mix two colors with ratio (0-1)")
    parser.add_argument("--simulate", choices=["protanopia", "deuteranopia", "tritanopia"], help="Simulate color blindness")
    parser.add_argument("--format", "-f", choices=["ascii", "json"], default="ascii", help="Output format")

    args = parser.parse_args()

    if args.check_contrast:
        result = check_contrast(args.color, args.check_contrast)
        print(format_contrast_output(result, args.format))
    elif args.generate_theme:
        theme = generate_theme(args.color)
        print(format_theme_output(theme, args.format))
    elif args.mix is not None:
        # Must be checked BEFORE the plain --gradient branch: "elif
        # args.gradient" used to swallow every --mix invocation first,
        # making the mix mode unreachable dead code.
        if not args.gradient:
            print("Error: --mix requires --gradient END_COLOR")
        else:
            mixed = ColorTools.mix_colors(args.color, args.gradient, args.mix)
            print(f"Mixed ({args.mix*100:.0f}%): {mixed}")
    elif args.gradient:
        g = generate_gradient(args.color, args.gradient)
        if args.format == "json":
            print(json.dumps(g, indent=2))
        else:
            print(f"Gradient: {g['start']} → {g['end']}")
            for i, c in enumerate(g['all_steps'], 1):
                print(f"  Step {i}: {c}")
            print(f"  CSS: {g['css_linear']}")
    elif args.simulate:
        simulator = {
            "protanopia": ColorTools.simulate_protanopia,
            "deuteranopia": ColorTools.simulate_deuteranopia,
            "tritanopia": ColorTools.simulate_tritanopia
        }
        result = simulator[args.simulate](args.color)
        print(f"Original: {args.color}")
        print(f"Simulated ({args.simulate}): {result}")
    else:
        palette = generate_palette(args.color, args.harmony)
        print(format_palette_output(palette, args.format))
