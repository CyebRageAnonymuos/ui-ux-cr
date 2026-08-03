#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSS Generator - Generate CSS utilities: shadows, gradients, border-radius,
glassmorphism, glow effects, grid patterns, and complete UI kit
Cyber-Rage Design Intelligence Engine

Usage: python css_generator.py --shadow lg
       python css_generator.py --gradient "#2563EB,#F97316" --angle 135
       python css_generator.py --glass --blur 15 --opacity 0.15
       python css_generator.py --radius sm
       python css_generator.py --ui-kit --primary #2563EB --cta #F97316
"""

import argparse
import json
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


SHADOWS = {
    "xs": "0 1px 2px rgba(0,0,0,0.05)",
    "sm": "0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06)",
    "md": "0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06)",
    "lg": "0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05)",
    "xl": "0 20px 25px rgba(0,0,0,0.1), 0 10px 10px rgba(0,0,0,0.04)",
    "2xl": "0 25px 50px rgba(0,0,0,0.25)",
    "inner": "inset 0 2px 4px rgba(0,0,0,0.06)",
    "none": "none",
    "soft": "0 2px 8px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.04)",
    "elevated": "0 8px 30px rgba(0,0,0,0.12)",
    "colored-primary": "0 8px 24px rgba(37,99,235,0.25)",
    "colored-cta": "0 8px 24px rgba(249,115,22,0.25)",
    "neon": "0 0 5px rgba(0,255,136,0.5), 0 0 20px rgba(0,255,136,0.3), 0 0 50px rgba(0,255,136,0.1)",
    "glass": "0 8px 32px rgba(0,0,0,0.15)",
}

RADII = {
    "none": "0px",
    "xs": "2px",
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "xl": "16px",
    "2xl": "24px",
    "full": "9999px",
}


def generate_shadow(level):
    if level not in SHADOWS:
        return f"Unknown shadow: '{level}'. Available: {', '.join(SHADOWS.keys())}"
    value = SHADOWS[level]
    return (
        f"/* Shadow: {level} */\n"
        f".shadow-{level} {{\n"
        f"  box-shadow: {value};\n"
        f"}}\n\n"
        f"/* CSS Variable */\n"
        f":root {{\n"
        f"  --shadow-{level}: {value};\n"
        f"}}"
    )


def generate_gradient(colors, angle=135):
    stops = ", ".join(colors)
    return (
        f"/* Linear Gradient ({angle}deg) */\n"
        f".gradient {{\n"
        f"  background: linear-gradient({angle}deg, {stops});\n"
        f"}}\n\n"
        f"/* Radial Gradient */\n"
        f".gradient-radial {{\n"
        f"  background: radial-gradient(circle at 50% 50%, {stops});\n"
        f"}}"
    )


def generate_glass(blur=15, opacity=0.15, border_opacity=0.2, radius=16):
    return (
        f"/* Glassmorphism */\n"
        f".glass {{\n"
        f"  background: rgba(255, 255, 255, {opacity});\n"
        f"  backdrop-filter: blur({blur}px);\n"
        f"  -webkit-backdrop-filter: blur({blur}px);\n"
        f"  border: 1px solid rgba(255, 255, 255, {border_opacity});\n"
        f"  border-radius: {radius}px;\n"
        f"}}\n\n"
        f".glass-dark {{\n"
        f"  background: rgba(15, 23, 42, {min(opacity + 0.1, 0.6)});\n"
        f"  backdrop-filter: blur({blur}px);\n"
        f"  -webkit-backdrop-filter: blur({blur}px);\n"
        f"  border: 1px solid rgba(255, 255, 255, 0.1);\n"
        f"  border-radius: {radius}px;\n"
        f"}}"
    )


def generate_glow(color="#6366F1", intensity=20):
    return (
        f"/* Glow Effect */\n"
        f".glow {{\n"
        f"  box-shadow: 0 0 {intensity}px {color},\n"
        f"              0 0 {intensity * 2}px {color}80,\n"
        f"              0 0 {intensity * 3}px {color}40;\n"
        f"}}\n\n"
        f".glow-text {{\n"
        f"  color: {color};\n"
        f"  text-shadow: 0 0 {intensity}px {color};\n"
        f"}}"
    )


def generate_radius(level):
    if level not in RADII:
        return f"Unknown radius: '{level}'. Available: {', '.join(RADII.keys())}"
    value = RADII[level]
    return (
        f"/* Border Radius: {level} */\n"
        f".rounded-{level} {{\n"
        f"  border-radius: {value};\n"
        f"}}"
    )


def generate_ui_kit(primary="#2563EB", secondary="#3B82F6", cta="#F97316", bg="#F8FAFC", text="#1E293B"):
    return f"""/* ============================================
   UI KIT - Cyber-Rage CSS Generator
   Primary: {primary} | Secondary: {secondary} | CTA: {cta}
   ============================================ */

/* ---------- CSS Variables ---------- */
:root {{
  --color-primary: {primary};
  --color-secondary: {secondary};
  --color-cta: {cta};
  --color-bg: {bg};
  --color-text: {text};
  --radius-md: 8px;
  --radius-lg: 12px;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.1);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.07);
  --transition: all 200ms ease;
}}

/* ---------- Button Primary ---------- */
.btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  border-radius: var(--radius-md);
  font-weight: 600;
  font-size: 15px;
  cursor: pointer;
  border: none;
  transition: var(--transition);
}}
.btn-primary {{
  background: {cta};
  color: #fff;
}}
.btn-primary:hover {{
  opacity: 0.9;
  transform: translateY(-1px);
  box-shadow: 0 8px 24px {cta}40;
}}
.btn-secondary {{
  background: transparent;
  color: {primary};
  border: 2px solid {primary};
}}
.btn-secondary:hover {{
  background: {primary}10;
}}
.btn-ghost {{
  background: transparent;
  color: {text};
}}
.btn-ghost:hover {{
  background: rgba(0,0,0,0.05);
}}

/* ---------- Card ---------- */
.card {{
  background: #fff;
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-sm);
  border: 1px solid rgba(0,0,0,0.05);
  transition: var(--transition);
}}
.card:hover {{
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}}

/* ---------- Input ---------- */
.input {{
  width: 100%;
  padding: 12px 16px;
  border: 1px solid rgba(0,0,0,0.15);
  border-radius: var(--radius-md);
  font-size: 16px;
  transition: var(--transition);
}}
.input:focus {{
  outline: none;
  border-color: {primary};
  box-shadow: 0 0 0 3px {primary}20;
}}

/* ---------- Badge ---------- */
.badge {{
  display: inline-flex;
  padding: 4px 12px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 600;
}}
.badge-primary {{ background: {primary}15; color: {primary}; }}
.badge-success {{ background: rgba(34,197,94,0.15); color: #16A34A; }}
.badge-warning {{ background: rgba(245,158,11,0.15); color: #D97706; }}
.badge-error {{ background: rgba(239,68,68,0.15); color: #DC2626; }}

/* ---------- Skeleton ---------- */
.skeleton {{
  background: linear-gradient(90deg, #E2E8F0 25%, #F1F5F9 50%, #E2E8F0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 8px;
}}
@keyframes shimmer {{
  from {{ background-position: 200% 0; }}
  to {{ background-position: -200% 0; }}
}}

/* ---------- Focus Ring (a11y) ---------- */
:focus-visible {{
  outline: 3px solid {primary};
  outline-offset: 2px;
  border-radius: 4px;
}}

/* ---------- Reduced Motion ---------- */
@media (prefers-reduced-motion: reduce) {{
  *, *::before, *::after {{
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }}
}}"""


def generate_neumorphism(color="#E0E5EC"):
    return f"""/* Neumorphism */
.neu {{
  background: {color};
  border-radius: 16px;
  box-shadow: 9px 9px 16px rgba(163, 177, 198, 0.6),
              -9px -9px 16px rgba(255, 255, 255, 0.5);
}}
.neu-inset {{
  background: {color};
  border-radius: 16px;
  box-shadow: inset 9px 9px 16px rgba(163, 177, 198, 0.6),
              inset -9px -9px 16px rgba(255, 255, 255, 0.5);
}}
.neu-btn {{
  background: {color};
  border: none;
  border-radius: 16px;
  box-shadow: 9px 9px 16px rgba(163, 177, 198, 0.6),
              -9px -9px 16px rgba(255, 255, 255, 0.5);
  cursor: pointer;
  transition: all 200ms ease;
}}
.neu-btn:active {{
  box-shadow: inset 9px 9px 16px rgba(163, 177, 198, 0.6),
              inset -9px -9px 16px rgba(255, 255, 255, 0.5);
}}"""


def generate_glass_tailwind(blur=15):
    return (
        f"<!-- Glassmorphism Tailwind Classes -->\n"
        f"<div class=\"bg-white/15 backdrop-blur-{blur} border border-white/20 rounded-2xl p-6 shadow-lg\">\n"
        f"  Content here\n"
        f"</div>"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSS Generator - Cyber-Rage")
    parser.add_argument("--shadow", help="Shadow level (xs, sm, md, lg, xl, 2xl, inner, none, soft, elevated, colored-primary, colored-cta, neon, glass)")
    parser.add_argument("--gradient", help="Gradient colors comma-separated (e.g. '#2563EB,#F97316')")
    parser.add_argument("--angle", type=int, default=135, help="Gradient angle (default: 135)")
    parser.add_argument("--glass", action="store_true", help="Generate glassmorphism CSS")
    parser.add_argument("--blur", type=int, default=15, help="Glass blur px (default: 15)")
    parser.add_argument("--opacity", type=float, default=0.15, help="Glass opacity (default: 0.15)")
    parser.add_argument("--glow", help="Glow color (e.g. '#6366F1')")
    parser.add_argument("--radius", help="Border radius (none, xs, sm, md, lg, xl, 2xl, full)")
    parser.add_argument("--ui-kit", action="store_true", help="Generate complete UI kit")
    parser.add_argument("--neumorphism", action="store_true", help="Generate neumorphism CSS")
    parser.add_argument("--primary", default="#2563EB", help="Primary color for UI kit")
    parser.add_argument("--secondary", default="#3B82F6", help="Secondary color for UI kit")
    parser.add_argument("--cta", default="#F97316", help="CTA color for UI kit")
    parser.add_argument("--bg", default="#F8FAFC", help="Background color for UI kit")
    parser.add_argument("--text", default="#1E293B", help="Text color for UI kit")

    args = parser.parse_args()

    if args.shadow:
        print(generate_shadow(args.shadow))
    elif args.gradient:
        colors = [c.strip() for c in args.gradient.split(",")]
        print(generate_gradient(colors, args.angle))
    elif args.glass:
        print(generate_glass(args.blur, args.opacity))
    elif args.glow:
        print(generate_glow(args.glow))
    elif args.radius:
        print(generate_radius(args.radius))
    elif args.ui_kit:
        print(generate_ui_kit(args.primary, args.secondary, args.cta, args.bg, args.text))
    elif args.neumorphism:
        print(generate_neumorphism())
    else:
        print("Specify one of: --shadow, --gradient, --glass, --glow, --radius, --ui-kit, --neumorphism")
        print("Example: python css_generator.py --ui-kit --primary #2563EB --cta #F97316")
