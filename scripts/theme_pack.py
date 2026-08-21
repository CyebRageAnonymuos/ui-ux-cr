#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Theme Pack - 60+ ready-made premium design themes
Cyber-Rage Design Intelligence Engine

Usage:
  python3 theme_pack.py --list
  python3 theme_pack.py --name dracula --format css
  python3 theme_pack.py --name nord --format all
  python3 theme_pack.py --dark --mood cyberpunk
  python3 theme_pack.py --light --mood minimal
"""

import json
import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def T(mode, moods, bg, surface, text, muted, primary, secondary, accent,
      success, warning, error, border, heading="Inter", body="Inter",
      radius="0.75rem", shadow="soft"):
    return {
        "mode": mode, "moods": moods,
        "colors": {
            "bg": bg, "surface": surface, "text": text, "muted": muted,
            "primary": primary, "secondary": secondary, "accent": accent,
            "success": success, "warning": warning, "error": error,
            "border": border,
        },
        "fonts": {"heading": heading, "body": body},
        "radius": radius, "shadow": shadow,
    }


THEMES = {
    # ---------------- DARK ----------------
    "dracula": T("dark", ["gothic", "fun", "editor"],
        "#282A36", "#343746", "#F8F8F2", "#6272A4", "#BD93F9", "#FF79C6",
        "#50FA7B", "#50FA7B", "#F1FA8C", "#FF5555", "#44475A",
        "JetBrains Mono", "Inter"),
    "nord": T("dark", ["calm", "professional", "arctic"],
        "#2E3440", "#3B4252", "#ECEFF4", "#7B88A1", "#88C0D0", "#81A1C1",
        "#A3BE8C", "#A3BE8C", "#EBCB8B", "#BF616A", "#434C5E",
        "Source Sans 3", "Inter"),
    "tokyo-night": T("dark", ["neon", "developer", "modern"],
        "#1A1B26", "#24283B", "#C0CAF5", "#565F89", "#7AA2F7", "#BB9AF7",
        "#9ECE6A", "#9ECE6A", "#E0AF68", "#F7768E", "#292E42",
        "Space Grotesk", "Inter"),
    "tokyo-storm": T("dark", ["neon", "developer", "muted"],
        "#24283B", "#2F334D", "#C0CAF5", "#565F89", "#7AA2F7", "#BB9AF7",
        "#9ECE6A", "#9ECE6A", "#E0AF68", "#F7768E", "#343A55",
        "Space Grotesk", "Inter"),
    "catppuccin-mocha": T("dark", ["pastel", "soft", "cozy"],
        "#1E1E2E", "#313244", "#CDD6F4", "#6C7086", "#89B4FA", "#CBA6F7",
        "#A6E3A1", "#A6E3A1", "#F9E2AF", "#F38BA8", "#45475A",
        "Nunito", "Mulish"),
    "catppuccin-macchiato": T("dark", ["pastel", "soft", "cozy"],
        "#24273A", "#363A4F", "#CAD3F5", "#6E738D", "#8AADF4", "#C6A0F6",
        "#A6DA95", "#A6DA95", "#F5DBB3", "#ED8796", "#494D64",
        "Nunito", "Mulish"),
    "gruvbox-dark": T("dark", ["retro", "warm", "editor"],
        "#282828", "#3C3836", "#EBDBB2", "#928374", "#83A598", "#D3869B",
        "#8EC07C", "#B8BB26", "#FABD2F", "#FB4934", "#504945",
        "IBM Plex Mono", "IBM Plex Sans"),
    "rose-pine": T("dark", ["elegant", "muted", "artistic"],
        "#191724", "#1F1D2E", "#E0DEF4", "#908CAA", "#C4A7E7", "#EBBCBA",
        "#9CCFD8", "#9CCFD8", "#F6C177", "#EB6F92", "#26233A",
        "Cormorant Garamond", "Karla"),
    "rose-pine-moon": T("dark", ["elegant", "muted", "artistic"],
        "#232136", "#2A273F", "#E0DEF4", "#817C9C", "#C4A7E7", "#EA9A97",
        "#9CCFD8", "#9CCFD8", "#F6C177", "#EB6F92", "#393552",
        "Cormorant Garamond", "Karla"),
    "everforest-dark": T("dark", ["natural", "calm", "organic"],
        "#2D353B", "#343F44", "#D3C6AA", "#859289", "#A7C080", "#E69875",
        "#7FBBB3", "#A7C080", "#DBBC7F", "#E67E80", "#414B50",
        "Lora", "Source Sans 3"),
    "solarized-dark": T("dark", ["classic", "warm", "editor"],
        "#002B36", "#073642", "#EEE8D5", "#93A1A1", "#268BD2", "#2AA198",
        "#859900", "#859900", "#B58900", "#DC322F", "#094758",
        "IBM Plex Serif", "IBM Plex Sans"),
    "one-dark": T("dark", ["developer", "balanced", "modern"],
        "#282C34", "#21252B", "#DCDFE4", "#5C6370", "#61AFEF", "#C678DD",
        "#98C379", "#98C379", "#E5C07B", "#E06C75", "#3E4451",
        "Fira Sans", "Inter"),
    "github-dark": T("dark", ["clean", "developer", "neutral"],
        "#0D1117", "#161B22", "#E6EDF3", "#7D8590", "#2F81F7", "#A371F7",
        "#3FB950", "#3FB950", "#D29922", "#F85149", "#30363D",
        "Inter", "Inter"),
    "github-dimmed": T("dark", ["clean", "developer", "soft"],
        "#22272E", "#2D333B", "#ADBAC7", "#768390", "#539BF5", "#B083F0",
        "#57AB5A", "#57AB5A", "#C69026", "#F47067", "#444C56",
        "Inter", "Inter"),
    "material-ocean": T("dark", ["deep", "cool", "developer"],
        "#0F111A", "#131721", "#E6ECF5", "#546178", "#82AAFF", "#C792EA",
        "#00E5FF", "#C3E88D", "#FFCB6B", "#FF5370", "#1F2437",
        "Titillium Web", "Roboto"),
    "synthwave-84": T("dark", ["retro", "neon", "eighties"],
        "#251B32", "#2C2340", "#F7F7FB", "#848BB5", "#FF7EDB", "#36F9F6",
        "#FDEE5E", "#72F1B8", "#FDEE5E", "#FE4450", "#3A2F52",
        "Orbitron", "Exo 2"),
    "cyberpunk-neon": T("dark", ["cyberpunk", "neon", "futuristic"],
        "#0A0A14", "#12121F", "#EAEAEA", "#5F5F7A", "#00FFF9", "#FC00FF",
        "#FCEE0A", "#05FFA1", "#FCEE0A", "#FF003C", "#1E1E32",
        "Orbitron", "Rajdhani"),
    "luxury-gold": T("dark", ["luxury", "premium", "elegant"],
        "#0A0A0A", "#141414", "#F5F0E6", "#8A8478", "#D4AF37", "#C9A227",
        "#E8C96A", "#7BA05B", "#D4AF37", "#C0392B", "#2A2A2A",
        "Playfair Display", "Inter", "0.25rem", "luxury"),
    "oled-black": T("dark", ["minimal", "contrast", "battery"],
        "#000000", "#0A0A0A", "#FFFFFF", "#6B6B6B", "#2979FF", "#00E5FF",
        "#FFFFFF", "#00C853", "#FFD600", "#FF1744", "#1A1A1A",
        "Inter", "Inter", "0.5rem"),
    "midnight-blue": T("dark", ["calm", "corporate", "deep"],
        "#0A1128", "#101A3C", "#E2E8F0", "#64748B", "#4FC3F7", "#818CF8",
        "#34D399", "#34D399", "#FBBF24", "#F87171", "#1E293B",
        "DM Sans", "Inter"),
    "carbon": T("dark", ["industrial", "bold", "sport"],
        "#1A1A1A", "#242424", "#E0E0E0", "#737373", "#FF6B35", "#F7C59F",
        "#EFEFEF", "#7CB518", "#FFD23F", "#D64545", "#333333",
        "Oswald", "Barlow"),
    "obsidian": T("dark", ["mystic", "purple", "premium"],
        "#0C0C0F", "#16161D", "#EDEDF2", "#6E6E80", "#7C3AED", "#A78BFA",
        "#22D3EE", "#34D399", "#FBBF24", "#F43F5E", "#232330",
        "Unbounded", "Inter"),
    "matrix-green": T("dark", ["hacker", "terminal", "monochrome"],
        "#000000", "#001100", "#00FF41", "#007700", "#00FF41", "#008F11",
        "#00CC33", "#00FF41", "#AAFF00", "#FF3333", "#003300",
        "VT323", "Share Tech Mono", "0rem"),
    "terminal-amber": T("dark", ["retro", "terminal", "vintage"],
        "#100A02", "#1A1206", "#FFB000", "#996600", "#FFB000", "#FF8C00",
        "#FFCC66", "#FFB000", "#FFD700", "#FF4500", "#2E2008",
        "VT323", "Share Tech Mono", "0rem"),
    "terminal-green": T("dark", ["retro", "terminal", "hacker"],
        "#051405", "#0A1F0A", "#33FF33", "#1F991F", "#33FF33", "#00CC00",
        "#66FF66", "#33FF33", "#FFFF33", "#FF3333", "#123312",
        "VT323", "Share Tech Mono", "0rem"),
    "vaporwave": T("dark", ["retro", "aesthetic", "playful"],
        "#210B30", "#2D1B69", "#F8F4FF", "#9B94C9", "#FF71CE", "#01CDFE",
        "#B967FF", "#05FFA1", "#FFFB96", "#FF61AB", "#3D2570",
        "Monoton", "Quicksand"),
    "outrun": T("dark", ["retro", "sunset", "racing"],
        "#1A0E2E", "#2B1055", "#FDEFF9", "#9D8DA8", "#FF2E97", "#FF9E00",
        "#00D9FF", "#FFD319", "#FF2975", "#F2324B", "#3A1D63",
        "Righteous", "Exo 2"),
    "tron-legacy": T("dark", ["futuristic", "glow", "sci-fi"],
        "#04070D", "#0A1220", "#DFF3FB", "#4A6B84", "#6FC3DF", "#FF9E00",
        "#BFEFFF", "#6FC3DF", "#FF9E00", "#FF5A00", "#12283D",
        "Michroma", "Titillium Web", "0.25rem", "glow"),
    "blade-runner": T("dark", ["cinematic", "noir", "moody"],
        "#0B0F14", "#121A22", "#E8E4D8", "#6B7A80", "#FF9E1B", "#0FA3B1",
        "#F4D58D", "#7FB069", "#FF9E1B", "#D1462F", "#1E2A33",
        "Rajdhani", "Work Sans"),
    "neon-noir": T("dark", ["noir", "neon", "nightlife"],
        "#0A0A12", "#14141F", "#F2F2F7", "#61617A", "#FF2E63", "#08D9D6",
        "#FFDE59", "#08D9D6", "#FFDE59", "#FF2E63", "#1F1F30",
        "Syne", "Manrope"),
    "miami-vice": T("dark", ["retro", "tropical", "party"],
        "#160F2B", "#221743", "#FDF6FF", "#9187B8", "#FF4DA6", "#2EE6D6",
        "#FF8C42", "#2EE6D6", "#FFD166", "#EF476F", "#33235C",
        "Pacifico", "Poppins"),
    "royal-purple": T("dark", ["regal", "rich", "premium"],
        "#150E23", "#201636", "#F0EAFB", "#8B7BB5", "#8B5CF6", "#F59E0B",
        "#C4B5FD", "#34D399", "#F59E0B", "#EF4444", "#2E2150",
        "Marcellus", "Jost"),
    "emerald-night": T("dark", ["fresh", "money", "growth"],
        "#06120B", "#0C1F14", "#D1FAE5", "#5F8F75", "#10B981", "#34D399",
        "#6EE7B7", "#10B981", "#FCD34D", "#F87171", "#143524",
        "Sora", "Inter"),
    "crimson-night": T("dark", ["bold", "passion", "gaming"],
        "#140608", "#220D11", "#FBE9EC", "#96656E", "#DC2626", "#F87171",
        "#FCA5A5", "#22C55E", "#FACC15", "#DC2626", "#33151B",
        "Anton", "Archivo"),
    "ocean-deep": T("dark", ["aquatic", "calm", "flowing"],
        "#04121F", "#0A1F33", "#D6EEFF", "#5A87A8", "#0EA5E9", "#14B8A6",
        "#67E8F9", "#14B8A6", "#FDE68A", "#FB7185", "#123049",
        "Outfit", "Work Sans"),
    "forest-night": T("dark", ["natural", "earthy", "calm"],
        "#131A15", "#1C2620", "#DDE7DD", "#7C947F", "#74A57F", "#A3C585",
        "#BFD8B8", "#74A57F", "#D9B44A", "#C1554D", "#27362D",
        "Fraunces", "Karla"),
    "coffee-dark": T("dark", ["cozy", "cafe", "warm"],
        "#17110C", "#221913", "#EAD9C9", "#8A7361", "#C08552", "#A47148",
        "#DDB892", "#9CAF53", "#E3B23C", "#B0413E", "#33261C",
        "Zilla Slab", "Nunito Sans"),
    "whiskey-dark": T("dark", ["bar", "warm", "premium"],
        "#150E06", "#211710", "#F3E5D0", "#96795B", "#D97706", "#B45309",
        "#FBBF24", "#A16207", "#FBBF24", "#DC2626", "#33241A",
        "Libre Baskerville", "Open Sans"),
    "iron-man": T("dark", ["hero", "bold", "tech"],
        "#160B06", "#241109", "#FFE9D6", "#96604A", "#E23636", "#F0B429",
        "#FFD54F", "#8BC34A", "#F0B429", "#E23636", "#3A1D12",
        "Russo One", "Exo 2"),
    "batman": T("dark", ["hero", "noir", "comic"],
        "#060608", "#0E0E12", "#E8E8EC", "#5E5E6E", "#F5D000", "#3E4A6B",
        "#FFF176", "#4CAF50", "#F5D000", "#D32F2F", "#1A1A22",
        "Bebas Neue", "Inter"),
    "graphite-lime": T("dark", ["industrial", "energetic", "modern"],
        "#18181B", "#232327", "#FAFAFA", "#71717A", "#A3E635", "#FACC15",
        "#D9F99D", "#A3E635", "#FACC15", "#EF4444", "#2E2E33",
        "Archivo Black", "Archivo"),
    "slate-pro": T("dark", ["professional", "saas", "clean"],
        "#0F172A", "#1E293B", "#F1F5F9", "#64748B", "#38BDF8", "#818CF8",
        "#7DD3FC", "#4ADE80", "#FBBF24", "#F87171", "#334155",
        "Plus Jakarta Sans", "Inter"),
    "ultraviolet": T("dark", ["vibrant", "gradient", "youthful"],
        "#12081F", "#1C1030", "#F3EBFF", "#8B7BB8", "#6366F1", "#D946EF",
        "#A5B4FC", "#34D399", "#FBBF24", "#F43F5E", "#2A1A45",
        "Syne", "Urbanist"),
    "space-gray": T("dark", ["apple-like", "neutral", "product"],
        "#1C1C1E", "#2C2C2E", "#F2F2F7", "#8E8E93", "#0A84FF", "#5E5CE6",
        "#64D2FF", "#30D158", "#FFD60A", "#FF453A", "#3A3A3C",
        "Inter", "Inter", "0.875rem"),
    "blood-red": T("dark", ["intense", "dramatic", "horror"],
        "#0F0507", "#1A0A0D", "#F5E6E8", "#8F6570", "#B91C1C", "#7F1D1D",
        "#FCA5A5", "#65A30D", "#EAB308", "#B91C1C", "#2E1216",
        "Special Elite", "Courier Prime"),
    "arctic-night": T("dark", ["icy", "clean", "cool"],
        "#0B1622", "#132435", "#E3F2FD", "#6B8CAE", "#7DD3FC", "#38BDF8",
        "#BAE6FD", "#4ADE80", "#FDE68A", "#F87171", "#1D3247",
        "Sora", "Inter"),
    "deep-space": T("dark", ["cosmic", "astral", "dreamy"],
        "#070B14", "#0E1524", "#E8EDF7", "#5D6B85", "#8B5CF6", "#22D3EE",
        "#C4B5FD", "#4ADE80", "#FCD34D", "#FB7185", "#1A2438",
        "Space Grotesk", "Space Grotesk"),

    # ---------------- LIGHT ----------------
    "minimal-white": T("light", ["minimal", "mono", "clean"],
        "#FFFFFF", "#FAFAFA", "#111111", "#737373", "#111111", "#525252",
        "#2563EB", "#16A34A", "#F59E0B", "#DC2626", "#E5E5E5",
        "Inter", "Inter", "0.5rem"),
    "paper-light": T("light", ["editorial", "reading", "warm"],
        "#FAF9F6", "#F1EFE9", "#1C1917", "#78716C", "#B45309", "#44403C",
        "#0F766E", "#15803D", "#D97706", "#B91C1C", "#E7E5E4",
        "Newsreader", "Source Sans 3"),
    "solarized-light": T("light", ["classic", "warm", "editor"],
        "#FDF6E3", "#EEE8D5", "#073642", "#93A1A1", "#268BD2", "#2AA198",
        "#859900", "#859900", "#B58900", "#DC322F", "#E4DBC8",
        "IBM Plex Serif", "IBM Plex Sans"),
    "github-light": T("light", ["clean", "developer", "neutral"],
        "#FFFFFF", "#F6F8FA", "#1F2328", "#656D76", "#0969DA", "#8250DF",
        "#1A7F37", "#1A7F37", "#9A6700", "#CF222E", "#D0D7DE",
        "Inter", "Inter"),
    "notion-light": T("light", ["productivity", "docs", "neutral"],
        "#FFFFFF", "#F7F6F3", "#37352F", "#9B9A97", "#2383E2", "#EB5757",
        "#448361", "#448361", "#DFAB01", "#D44C47", "#E9E9E7",
        "Inter", "Inter"),
    "airy-blue": T("light", ["friendly", "saas", "sky"],
        "#F8FAFC", "#EFF6FF", "#1E3A5F", "#64748B", "#3B82F6", "#60A5FA",
        "#93C5FD", "#22C55E", "#F59E0B", "#EF4444", "#DBEAFE",
        "Nunito", "Open Sans"),
    "nordic-light": T("light", ["scandinavian", "calm", "cool"],
        "#F4F5F7", "#ECEEF1", "#2E3440", "#6B7280", "#5E81AC", "#81A1C1",
        "#A3BE8C", "#A3BE8C", "#EBCB8B", "#BF616A", "#D8DEE9",
        "Outfit", "Inter"),
    "sage-fresh": T("light", ["natural", "wellness", "organic"],
        "#F6F8F4", "#E8EFE4", "#2F3E33", "#6B7F6E", "#6B8F71", "#87A96B",
        "#A3C9A8", "#6B8F71", "#D4A373", "#C1554D", "#D5E0D2",
        "Fraunces", "Karla"),
    "sandstone": T("light", ["desert", "earthy", "artisan"],
        "#F5EFE6", "#EAE0D1", "#4A3728", "#8C7A64", "#B08968", "#7F5539",
        "#9C6644", "#7F9A5C", "#D4A373", "#A4453C", "#DDD2C0",
        "Marcellus", "Jost"),
    "porcelain": T("light", ["minimal", "gallery", "refined"],
        "#F9FAFB", "#F3F4F6", "#111827", "#6B7280", "#4F46E5", "#7C3AED",
        "#818CF8", "#10B981", "#F59E0B", "#EF4444", "#E5E7EB",
        "Manrope", "Inter"),
    "soft-lavender": T("light", ["gentle", "wellness", "feminine"],
        "#FAF8FF", "#F0EBFA", "#3B3355", "#8B84A8", "#8B5CF6", "#B79CED",
        "#A78BFA", "#4ADE80", "#FBBF24", "#F472B6", "#E4DCF5",
        "Quicksand", "Nunito"),
    "mint-clean": T("light", ["fresh", "health", "clean"],
        "#F7FCFA", "#E6F4EE", "#134E3A", "#5F8B76", "#10B981", "#34D399",
        "#6EE7B7", "#10B981", "#FBBF24", "#F87171", "#D1EADD",
        "Outfit", "Work Sans"),
    "peach-soft": T("light", ["warm", "food", "friendly"],
        "#FFF8F3", "#FFE8DC", "#4E342E", "#9C7B70", "#F97316", "#FB923C",
        "#FDBA74", "#84CC16", "#F59E0B", "#DC2626", "#FAD9C7",
        "Baloo 2", "Quicksand"),
    "sky-daylight": T("light", ["cheerful", "travel", "open"],
        "#F0F9FF", "#E0F2FE", "#0C4A6E", "#64748B", "#0284C7", "#38BDF8",
        "#7DD3FC", "#22C55E", "#F59E0B", "#EF4444", "#BAE6FD",
        "Sora", "Inter"),
    "ivory-luxe": T("light", ["luxury", "fashion", "elegant"],
        "#FFFFF8", "#F5F2E9", "#1A1814", "#8A8471", "#8B7355", "#B08D57",
        "#C9B37E", "#6B8E23", "#C19A3D", "#8B2500", "#E8E3D3",
        "Bodoni Moda", "Raleway", "0.125rem", "luxury"),
    "linen-calm": T("light", ["spa", "serene", "neutral"],
        "#FBF7F2", "#F2EAE0", "#44403C", "#8C827A", "#A68A64", "#C2A683",
        "#D6C3A5", "#889C6E", "#D4A373", "#B0413E", "#E5DACB",
        "Cormorant Garamond", "Mulish"),
    "studio-white": T("light", ["portfolio", "creative", "sharp"],
        "#FFFFFF", "#F5F5F5", "#0A0A0A", "#737373", "#FF3E00", "#171717",
        "#FF3E00", "#22C55E", "#FACC15", "#EF4444", "#E5E5E5",
        "Space Grotesk", "Space Grotesk", "0.25rem"),
    "cotton-candy": T("light", ["playful", "kids", "sweet"],
        "#FFF7FB", "#FFE4F1", "#4A2040", "#9C6B8E", "#EC4899", "#8B5CF6",
        "#F9A8D4", "#4ADE80", "#FBBF24", "#EF4444", "#FBD5E8",
        "Fredoka", "Baloo 2"),
}


# ============================================================
# EXPORTERS
# ============================================================

def export_css(theme, name):
    c = theme["colors"]
    lines = [
        f"/* {name} - Theme Pack (Cyber-Rage) */",
        ":root {",
        f"  --color-bg: {c['bg']};",
        f"  --color-surface: {c['surface']};",
        f"  --color-text: {c['text']};",
        f"  --color-muted: {c['muted']};",
        f"  --color-primary: {c['primary']};",
        f"  --color-secondary: {c['secondary']};",
        f"  --color-accent: {c['accent']};",
        f"  --color-success: {c['success']};",
        f"  --color-warning: {c['warning']};",
        f"  --color-error: {c['error']};",
        f"  --color-border: {c['border']};",
        f"  --radius: {theme['radius']};",
        "}",
        "",
        "/* Fonts */",
        f"body {{ font-family: '{theme['fonts']['body']}', sans-serif; background: var(--color-bg); color: var(--color-text); }}",
        f"h1, h2, h3, h4, h5, h6 {{ font-family: '{theme['fonts']['heading']}', sans-serif; }}",
    ]
    return "\n".join(lines)


def export_tailwind(theme, name):
    c = theme["colors"]
    return (
        f"// {name} - Tailwind Config (Cyber-Rage)\n"
        "module.exports = {\n"
        "  theme: {\n"
        "    extend: {\n"
        "      colors: {\n"
        f"        bg: '{c['bg']}',\n"
        f"        surface: '{c['surface']}',\n"
        f"        text: '{c['text']}',\n"
        f"        muted: '{c['muted']}',\n"
        f"        primary: '{c['primary']}',\n"
        f"        secondary: '{c['secondary']}',\n"
        f"        accent: '{c['accent']}',\n"
        f"        success: '{c['success']}',\n"
        f"        warning: '{c['warning']}',\n"
        f"        error: '{c['error']}',\n"
        f"        border: '{c['border']}',\n"
        "      },\n"
        "      fontFamily: {\n"
        f"        heading: ['{theme['fonts']['heading']}', 'sans-serif'],\n"
        f"        body: ['{theme['fonts']['body']}', 'sans-serif'],\n"
        "      },\n"
        f"      borderRadius: {{ DEFAULT: '{theme['radius']}' }},\n"
        "    },\n"
        "  },\n"
        "};"
    )


def export_json(theme, name):
    data = {"name": name}
    data.update(theme)
    return json.dumps(data, indent=2)


def print_theme_preview(name, t):
    c = t["colors"]
    icon = "[D]" if t["mode"] == "dark" else "[L]"
    moods = ", ".join(t["moods"])
    print(f"  {icon} {name:<24} P:{c['primary']}  S:{c['secondary']}  A:{c['accent']}  ({moods})")


def main():
    p = argparse.ArgumentParser(description="60+ ready-made premium themes")
    p.add_argument("--list", action="store_true", help="List all themes")
    p.add_argument("--name", help="Theme name to export")
    p.add_argument("--format", default="css", choices=["css", "tailwind", "json", "all"])
    p.add_argument("--dark", action="store_true", help="Filter: dark themes only")
    p.add_argument("--light", action="store_true", help="Filter: light themes only")
    p.add_argument("--mood", help="Filter by mood (e.g. cyberpunk, luxury, minimal)")
    args = p.parse_args()

    names = sorted(THEMES)

    if args.list or (not args.name and (args.dark or args.light or args.mood)):
        modes = []
        if args.dark:
            modes.append("dark")
        if args.light:
            modes.append("light")
        pool = [n for n in names if not modes or THEMES[n]["mode"] in modes]
        if args.mood:
            pool = [n for n in pool if args.mood.lower() in THEMES[n]["moods"]]
        print(f"Theme Pack - {len(pool)} of {len(names)} themes\n")
        for n in pool:
            print_theme_preview(n, THEMES[n])
        return

    if not args.name:
        p.print_help()
        return

    key = args.name.lower().replace(" ", "-").replace("_", "-")
    if key not in THEMES:
        close = [n for n in names if key in n or n in key]
        print(f"Theme not found: {args.name}")
        if close:
            print("Did you mean:", ", ".join(close))
        return

    t = THEMES[key]
    outputs = {
        "css": export_css(t, key),
        "tailwind": export_tailwind(t, key),
        "json": export_json(t, key),
    }
    if args.format == "all":
        for label, content in outputs.items():
            print(f"\n{'=' * 20} {label.upper()} {'=' * 20}\n")
            print(content)
    else:
        print(outputs[args.format])


if __name__ == "__main__":
    main()
