#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gradient Generator - Full gradient studio:
linear / radial / conic, multi-stop, angle control, mesh presets,
and ready-to-use gradient buttons & backgrounds
Cyber-Rage Design Intelligence Engine

Usage: python gradient_generator.py --linear "#2563EB,#F97316" --angle 135
       python gradient_generator.py --radial "#0F172A,#6366F1"
       python gradient_generator.py --conic "#A855F7,#22D3EE,#A855F7"
       python gradient_generator.py --mesh aurora
       python gradient_generator.py --button "#2563EB" --hover
       python gradient_generator.py --presets
"""

import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def parse_colors(value):
    colors = [c.strip() for c in value.split(",") if c.strip()]
    if len(colors) < 2:
        raise SystemExit("Need at least 2 comma-separated colors (e.g. '#2563EB,#F97316')")
    return colors


def gradient_linear(colors, angle=135):
    stops = ", ".join(colors)
    return f"""/* Linear gradient {angle}deg */
.gradient {{
  background: linear-gradient({angle}deg, {stops});
}}

/* Tailwind (v3.0+ arbitrary values) */
/* class="bg-[linear-gradient({angle}deg,{stops})]" */

/* With soft hover lift */
.gradient-hover {{
  background: linear-gradient({angle}deg, {stops});
  transition: filter 200ms ease, transform 200ms ease;
}}
.gradient-hover:hover {{
  filter: brightness(1.08);
  transform: translateY(-2px);
}}"""


def gradient_radial(colors):
    first, last = colors[0], colors[-1]
    mid = ", ".join(colors)
    return f"""/* Radial gradient */
.gradient-radial {{
  background: radial-gradient(circle at center, {mid});
}}

/* Soft glow orb (great for hero backgrounds) */
.glow-orb {{
  position: absolute;
  width: 500px;
  height: 500px;
  border-radius: 50%;
  background: radial-gradient(circle, {first}55 0%, transparent 70%);
  filter: blur(60px);
  pointer-events: none;
}}

/* Button with subtle radial depth */
.btn-radial {{
  background: radial-gradient(circle at 30% 30%, {first}, {last});
  color: #fff;
  border-radius: 12px;
  padding: 12px 24px;
}}"""


def gradient_conic(colors):
    stops = ", ".join(colors)
    return f"""/* Conic gradient */
.gradient-conic {{
  background: conic-gradient(from 180deg, {stops});
}}

/* Animated conic border (premium card look) */
.card-conic-border {{
  position: relative;
  border-radius: 16px;
  padding: 1px; /* border thickness */
  background: conic-gradient(from 180deg, {stops});
}}
.card-conic-border > .inner {{
  background: #fff;
  border-radius: 15px;
  padding: 24px;
}}

/* Spinner */
.conic-spinner {{
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: conic-gradient(from 0deg, transparent 10%, {colors[0]}, transparent 90%);
  animation: conic-spin 1s linear infinite;
}}
@keyframes conic-spin {{
  to {{ transform: rotate(360deg); }}
}}"""


MESH_PRESETS = {
    "aurora": ("#0F172A", ["#6366F155", "#22D3EE44", "#A855F755"]),
    "sunset": ("#1E1B4B", ["#F9731644", "#EC489944", "#8B5CF644"]),
    "ocean": ("#0C4A6E", ["#22D3EE44", "#3B82F655", "#06B6D455"]),
    "candy": ("#FDF2F8", ["#F9A8D466", "#A5F3FC66", "#FDE68A66"]),
    "forest": ("#052E16", ["#22C55E44", "#84CC1644", "#10B98144"]),
}


def gradient_mesh(name):
    if name not in MESH_PRESETS:
        return f"Unknown mesh preset: '{name}'. Available: {', '.join(MESH_PRESETS)}"
    base, blobs = MESH_PRESETS[name]
    blob_css = "\n".join(
        f""".blob-{i + 1} {{
  position: absolute;
  width: 60%;
  height: 60%;
  border-radius: 50%;
  filter: blur(80px);
  background: radial-gradient(circle, {color} 0%, transparent 70%);
}}
.blob-{i + 1}:nth-of-type({i + 1}) {{ top: {top}%; left: {left}%; }}"""
        for i, (color, top, left) in enumerate(zip(blobs, (5, 35, 15), (5, 25, 55)))
    )
    return f"""/* Mesh gradient: {name} */
.mesh-{name} {{
  position: relative;
  background: {base};
  overflow: hidden;
  isolation: isolate;
}}
.mesh-{name} > .blob {{
  position: absolute;
  z-index: -1;
}}
{blob_css}

/* Content stays above the blobs */
.mesh-{name} > *:not(.blob) {{
  position: relative;
  z-index: 1;
}}"""


def gradient_button(color, hover=False, second="#F97316"):
    hover_css = f"""
.btn-gradient:hover {{
  background-size: 150% 150%;
  background-position: 100% 50%;
}}""" if hover else ""
    return f"""/* Gradient button */
.btn-gradient {{
  background: linear-gradient(135deg, {color}, {second});
  background-size: 200% 200%;
  background-position: 0% 50%;
  color: #fff;
  font-weight: 600;
  padding: 12px 28px;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  transition: background-position 300ms ease, transform 200ms ease, box-shadow 200ms ease;
  box-shadow: 0 4px 14px {color}55;
}}
.btn-gradient:active {{
  transform: scale(0.97);
}}
@media (prefers-reduced-motion: reduce) {{
  .btn-gradient {{ transition: none; }}
}}{hover_css}"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gradient Generator - Cyber-Rage")
    parser.add_argument("--linear", metavar="COLORS", help="Linear gradient colors (e.g. '#2563EB,#F97316')")
    parser.add_argument("--radial", metavar="COLORS", help="Radial gradient colors")
    parser.add_argument("--conic", metavar="COLORS", help="Conic gradient colors")
    parser.add_argument("--mesh", help=f"Mesh gradient preset ({', '.join(MESH_PRESETS)})")
    parser.add_argument("--button", metavar="COLOR", help="Gradient button from a base color")
    parser.add_argument("--hover", action="store_true", help="Add animated hover to --button")
    parser.add_argument("--second", default="#F97316", help="Second color for --button (default #F97316)")
    parser.add_argument("--angle", type=int, default=135, help="Linear angle in degrees (default 135)")
    parser.add_argument("--presets", action="store_true", help="List mesh presets")

    args = parser.parse_args()

    if args.presets:
        print("Mesh presets:")
        for name, (base, blobs) in MESH_PRESETS.items():
            print(f"  - {name} (base {base}, {len(blobs)} blobs)")
        sys.exit(0)

    if args.linear:
        print(gradient_linear(parse_colors(args.linear), args.angle))
    elif args.radial:
        print(gradient_radial(parse_colors(args.radial)))
    elif args.conic:
        print(gradient_conic(parse_colors(args.conic)))
    elif args.mesh:
        print(gradient_mesh(args.mesh))
    elif args.button:
        print(gradient_button(args.button, args.hover, args.second))
    else:
        print("Specify one of: --linear, --radial, --conic, --mesh, --button, --presets")
        print("Example: python gradient_generator.py --linear '#2563EB,#F97316' --angle 135")
        sys.exit(1)
