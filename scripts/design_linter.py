#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design Linter - Contracts for the "no-format" half of the pipeline.

Generators emit formats (SVG parses, JS compiles) - those are easy to
validate. Recommendations (palettes, pairings) never had a contract to
violate... until now. This linter gives them one:

1. Contrast contract: every recommended text/background pair must pass
   WCAG AA; CTAs must be usable with white OR black label text.
2. Harmony contract: the hue distances in a palette must actually match
   the harmony type it claims to be (triadic = 120deg steps, etc).
3. Shade-scale contract: lightness must decrease monotonically 50->900.
4. Distinguishability contract: colors must stay distinguishable under
   protanopia / deuteranopia / tritanopia simulation.
5. Pairing contract: heading/body must not be the same font silently,
   and DB rows must import both fonts they recommend.

Cyber-Rage Design Intelligence Engine

Usage: python design_linter.py --audit-db                     # audit the whole recommendation database
       python design_linter.py --colors "#0F172A,#F8FAFC,#2563EB" --claimed-harmony complementary
       python design_linter.py --pairing "Inter,Merriweather"
"""

import argparse
import csv
import json
import sys
import io
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from color_tools import ColorTools, check_contrast

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

# Below this RGB distance, two colors are considered a collision for
# color-blind users (tunable - documented threshold, not a hard truth).
CB_COLLISION_DISTANCE = 42.0


# ============ CONTRACT 2: HARMONY MATH ============

def hue_set(colors):
    """Hues of the chromatic colors only - grays have no meaningful hue
    and would pollute the harmony geometry."""
    hues = []
    for c in colors:
        h, s, _l = ColorTools.hex_to_hsl(c)
        if s > 4:  # near-zero saturation = gray, skip
            hues.append(h)
    return hues


def circular_distance(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def classify_harmony(colors, tolerance=18):
    """Classify what harmony a set of colors ACTUALLY forms.

    Returns one of: monochromatic, analogous, complementary,
    split-complementary, triadic, tetradic, or unknown - based on the
    pairwise hue distances vs the canonical geometry of each scheme.
    """
    hues = hue_set(colors)
    if len(hues) < 2:
        return "monochromatic"
    base = hues[0]
    distances = sorted(circular_distance(base, h) for h in hues[1:])

    if max(hues) - min(hues) <= 10 or all(d <= 10 for d in distances):
        return "monochromatic"
    if all(d <= 45 for d in distances):
        return "analogous"
    if any(abs(d - 180) <= tolerance for d in distances):
        if len(distances) >= 2 and any(abs(d - 150) <= tolerance or abs(d - 210) <= tolerance for d in distances):
            return "split-complementary"
        return "complementary"
    if all(abs(d - 120) <= tolerance for d in distances):
        return "triadic"
    if all(abs(d - 90) <= tolerance for d in distances):
        return "tetradic"
    return "unknown"


HARMONY_ALIASES = {
    "complementary": "complementary", "complement": "complementary",
    "analogous": "analogous", "triadic": "triadic", "triad": "triadic",
    "split-complementary": "split-complementary", "split": "split-complementary",
    "tetradic": "tetradic", "square": "tetradic", "rectangle": "tetradic",
    "monochromatic": "monochromatic", "mono": "monochromatic",
}


def lint_harmony(colors, claimed):
    """Compare the claimed harmony with the geometry the colors form.
    Returns (errors, warnings)."""
    if not claimed:
        return [], []
    claimed_norm = HARMONY_ALIASES.get(claimed.strip().lower())
    if claimed_norm is None:
        return [], [f"unknown claimed harmony '{claimed}' (can't verify)"]
    actual = classify_harmony(colors)
    if actual == claimed_norm:
        return [], []
    if actual == "unknown":
        return [], [f"claimed '{claimed}' but hue distances match no canonical scheme cleanly"]
    return [
        f"claimed '{claimed}' but hues form '{actual}' "
        f"(hue distances don't match {claimed_norm} geometry)"
    ], []


# ============ CONTRACT 3: SHADE SCALE MONOTONICITY ============

def lint_shade_scale(shades):
    """Lightness must not increase as the shade number grows (50 -> 900)."""
    problems = []
    ordered = sorted(shades.items(), key=lambda kv: int(kv[0]))
    for (s1, c1), (s2, c2) in zip(ordered, ordered[1:]):
        l1 = ColorTools.hex_to_hsl(c1)[2]
        l2 = ColorTools.hex_to_hsl(c2)[2]
        if l2 > l1:
            problems.append(f"shade {s1} ({c1}, L={l1}) is DARKER than shade {s2} ({c2}, L={l2})")
    return problems


# ============ CONTRACT 4: COLOR-BLIND DISTINGUISHABILITY ============

SIMULATORS = {
    "protanopia": ColorTools.simulate_protanopia,
    "deuteranopia": ColorTools.simulate_deuteranopia,
    "tritanopia": ColorTools.simulate_tritanopia,
}


def rgb_distance(c1, c2):
    r1, g1, b1 = ColorTools.hex_to_rgb(c1)
    r2, g2, b2 = ColorTools.hex_to_rgb(c2)
    return ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5


def lint_colorblind_collisions(colors, threshold=CB_COLLISION_DISTANCE):
    """Pairs that collapse into near-identical colors for CVD users."""
    problems = []
    for i in range(len(colors)):
        for j in range(i + 1, len(colors)):
            c1, c2 = colors[i], colors[j]
            if rgb_distance(c1, c2) < threshold:
                continue  # already near-identical for everyone; not a CVD-specific issue
            for name, sim in SIMULATORS.items():
                d = rgb_distance(sim(c1), sim(c2))
                if d < threshold:
                    problems.append(
                        f"{c1} and {c2} become near-identical under {name} "
                        f"(distance {d:.0f} < {threshold})"
                    )
    return problems


# ============ CONTRACT 1: CONTRAST ============

def best_label_color(bg):
    """Whichever of white/black gives better contrast on bg."""
    white = check_contrast("#FFFFFF", bg)["ratio"]
    black = check_contrast("#0F172A", bg)["ratio"]
    return ("#FFFFFF", white) if white >= black else ("#0F172A", black)


def lint_contrast_set(colors):
    """Pairwise contrast contract for an arbitrary palette.

    Without knowing which color is body text, the honest floor is
    AA-large / UI-component contrast (3:1) for EVERY usable pair; pairs
    in the 3:1-4.5:1 band are fine for large text and UI but not body
    text, which is a warning, not an error. The database audit applies
    the strict 4.5:1 where the text color IS known.
    """
    errors, warnings = [], []
    for fg in colors:
        for bg in colors:
            if fg == bg:
                continue
            if ColorTools.relative_luminance(fg) <= ColorTools.relative_luminance(bg):
                continue  # only sensible direction: darker-on-lighter
            res = check_contrast(fg, bg)
            if res["ratio"] < 3:
                errors.append(f"{fg} on {bg} = {res['ratio']}:1 (below 3:1 - unusable pair)")
            elif not res["wcag_aa_normal"]:
                warnings.append(f"{fg} on {bg} = {res['ratio']}:1 (large text/UI only, not body text)")
    return errors, warnings


# ============ DATABASE AUDITS ============

def load_rows(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def audit_colors_db():
    """Audit every recommended palette in colors.csv against the contracts."""
    errors, warnings = [], []
    rows = load_rows("colors.csv")
    for row in rows:
        name = row.get("Product Type", "?")
        text = (row.get("Text (Hex)") or "").strip()
        bg = (row.get("Background (Hex)") or "").strip()
        cta = (row.get("CTA (Hex)") or "").strip()
        primary = (row.get("Primary (Hex)") or "").strip()

        def valid(c):
            return c.startswith("#") and len(c) == 7

        # Contract 1a: body text on background must pass AA
        if valid(text) and valid(bg):
            res = check_contrast(text, bg)
            if not res["wcag_aa_normal"]:
                errors.append(f"[{name}] text {text} on bg {bg} = {res['ratio']}:1 (fails AA)")

        # Contract 1b: CTA must carry a readable label (white or black)
        if valid(cta):
            label, ratio = best_label_color(cta)
            if ratio < 3:
                errors.append(f"[{name}] CTA {cta} has no readable label (best {ratio}:1 with {label})")
            elif ratio < 4.5:
                warnings.append(f"[{name}] CTA {cta} label contrast {ratio}:1 (AA large only)")

        # Contract 4: primary vs CTA must survive CVD simulation
        if valid(primary) and valid(cta):
            for prob in lint_colorblind_collisions([primary, cta]):
                warnings.append(f"[{name}] {prob}")
    return errors, warnings, len(rows)


def _norm_name(s):
    """Lowercase alphanumerics only - so 'Clash Display' matches both
    Google-style 'Clash+Display' and Fontshare-style 'clash-display'."""
    return "".join(ch for ch in s.lower() if ch.isalnum())


def audit_typography_db():
    """Audit every font-pairing recommendation in typography.csv."""
    errors, warnings = [], []
    rows = load_rows("typography.csv")
    for row in rows:
        name = row.get("Font Pairing Name", "?")
        heading = (row.get("Heading Font") or "").strip()
        body = (row.get("Body Font") or "").strip()
        css_import = (row.get("CSS Import") or "")

        # Contract 5a: silently identical fonts = no pairing at all
        if heading and body and heading.lower() == body.lower():
            warnings.append(f"[{name}] heading and body are the same font ({heading}) - intentional?")

        # Contract 5b: the import snippet must actually load both fonts.
        # Names appear differently per source (Google: 'Source+Sans+Pro',
        # Fontshare: 'source-sans-pro') - compare on normalized names.
        import_norm = _norm_name(css_import)
        has_url = "url(" in css_import or "http" in css_import
        for font in {heading, body}:
            if not font:
                continue
            if _norm_name(font) not in import_norm:
                if has_url:
                    errors.append(f"[{name}] '{font}' not loaded by its CSS Import snippet")
                else:
                    warnings.append(f"[{name}] '{font}' has no import URL (snippet says: '{css_import[:50]}')")
    return errors, warnings, len(rows)


# ============ CLI ============

def print_report(results):
    errors, warnings = results
    print("=" * 64)
    print(f"  DESIGN LINTER - {len(errors)} error(s), {len(warnings)} warning(s)")
    print("=" * 64)
    for e in errors:
        print(f"  [✗] {e}")
    for w in warnings:
        print(f"  [△] {w}")
    if not errors and not warnings:
        print("  [✓] clean - every contract holds")
    print("=" * 64)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Design Linter - Cyber-Rage")
    parser.add_argument("--colors", help="Comma-separated hex colors to lint (contrast + harmony + CVD)")
    parser.add_argument("--claimed-harmony", help="Harmony the palette claims to be (verified against hue math)")
    parser.add_argument("--shades", help="Comma-separated hex shades from light to dark (monotonicity check)")
    parser.add_argument("--pairing", help="'HeadingFont,BodyFont' to lint structurally")
    parser.add_argument("--audit-db", action="store_true", help="Audit colors.csv + typography.csv recommendations")
    parser.add_argument("--json", action="store_true", help="JSON output")

    args = parser.parse_args()

    errors, warnings = [], []

    if args.colors:
        colors = [c.strip() for c in args.colors.split(",") if c.strip()]
        try:
            for c in colors:
                ColorTools.hex_to_rgb(c)
        except ValueError:
            print(f"Invalid hex color in: {args.colors}", file=sys.stderr)
            sys.exit(2)
        c_errors, c_warnings = lint_contrast_set(colors)
        errors.extend(c_errors)
        warnings.extend(c_warnings)
        h_errors, h_warnings = lint_harmony(colors, args.claimed_harmony)
        errors.extend(h_errors)
        warnings.extend(h_warnings)
        warnings.extend(lint_colorblind_collisions(colors))

    if args.shades:
        shade_colors = [c.strip() for c in args.shades.split(",") if c.strip()]
        scale = {str(i * 100 if i else 50): c for i, c in enumerate(shade_colors)}
        problems = lint_shade_scale(scale)
        if problems:
            errors.extend(problems)
        else:
            print("[✓] shade scale is monotonically darkening")

    if args.pairing:
        parts = [p.strip() for p in args.pairing.split(",") if p.strip()]
        if len(parts) != 2:
            print("--pairing expects 'HeadingFont,BodyFont'", file=sys.stderr)
            sys.exit(2)
        heading, body = parts
        if heading.lower() == body.lower():
            warnings.append(f"heading and body are the same font ({heading}) - intentional?")

    if args.audit_db:
        c_err, c_warn, c_total = audit_colors_db()
        t_err, t_warn, t_total = audit_typography_db()
        if not args.json:
            print(f"Audited {c_total} palette rows and {t_total} font-pairing rows")
        errors.extend(c_err + t_err)
        warnings.extend(c_warn + t_warn)

    if not (args.colors or args.shades or args.pairing or args.audit_db):
        print("Specify --colors, --shades, --pairing, or --audit-db")
        sys.exit(2)

    if args.json:
        print(json.dumps({"errors": errors, "warnings": warnings}, indent=2))
    else:
        print_report((errors, warnings))

    sys.exit(1 if errors else 0)
