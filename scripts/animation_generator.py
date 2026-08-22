#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Animation Generator - Generate CSS animations with customizable parameters:
fade, slide, scale, rotate, bounce, pulse, shimmer, flip, shake, glow, spin
Cyber-Rage Design Intelligence Engine

Usage: python animation_generator.py --list
       python animation_generator.py --type fade --duration 0.5 --easing ease-out
       python animation_generator.py --type bounce --distance 20
       python animation_generator.py --kit --primary #2563EB
"""

import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


EASINGS = {
    "linear": "linear",
    "ease": "ease",
    "ease-in": "ease-in",
    "ease-out": "ease-out",
    "ease-in-out": "ease-in-out",
    "spring": "cubic-bezier(0.68, -0.55, 0.265, 1.55)",
    "bounce": "cubic-bezier(0.68, -0.55, 0.265, 1.55)",
    "smooth": "cubic-bezier(0.4, 0, 0.2, 1)",
    "snappy": "cubic-bezier(0.2, 0.8, 0.2, 1)",
    "back": "cubic-bezier(0.175, 0.885, 0.32, 1.275)",
    "expo": "cubic-bezier(0.19, 1, 0.22, 1)",
}


def keyframes_fade(opacity_start=0):
    return f"""@keyframes fade-in {{
  from {{ opacity: {opacity_start}; }}
  to   {{ opacity: 1; }}
}}"""


def keyframes_slide(direction="up", distance=40):
    if direction == "up":
        transform = f"translateY({distance}px)"
    elif direction == "down":
        transform = f"translateY(-{distance}px)"
    elif direction == "left":
        transform = f"translateX({distance}px)"
    elif direction == "right":
        transform = f"translateX(-{distance}px)"
    return f"""@keyframes slide-{direction} {{
  from {{ opacity: 0; transform: {transform}; }}
  to   {{ opacity: 1; transform: translate(0, 0); }}
}}"""


def keyframes_scale(scale_from=0.8, scale_to=1.0):
    return f"""@keyframes scale-in {{
  from {{ opacity: 0; transform: scale({scale_from}); }}
  to   {{ opacity: 1; transform: scale({scale_to}); }}
}}"""


def keyframes_rotate(deg_from=0, deg_to=360):
    return f"""@keyframes rotate {{
  from {{ transform: rotate({deg_from}deg); }}
  to   {{ transform: rotate({deg_to}deg); }}
}}"""


def keyframes_bounce(distance=20):
    return f"""@keyframes bounce {{
  0%, 100% {{ transform: translateY(0); }}
  50%      {{ transform: translateY(-{distance}px); }}
}}"""


def keyframes_pulse(max_scale=1.05):
    return f"""@keyframes pulse {{
  0%, 100% {{ transform: scale(1); }}
  50%      {{ transform: scale({max_scale}); }}
}}"""


def keyframes_shimmer(base="#E2E8F0", light="#F8FAFC"):
    return f"""@keyframes shimmer {{
  from {{ background-position: 200% 0; }}
  to   {{ background-position: -200% 0; }}
}}
.shimmer {{
  background: linear-gradient(90deg, {base} 25%, {light} 50%, {base} 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}}"""


def keyframes_flip():
    return """@keyframes flip {
  from { transform: perspective(600px) rotateY(0deg); }
  to   { transform: perspective(600px) rotateY(360deg); }
}"""


def keyframes_shake(distance=8):
    return f"""@keyframes shake {{
  0%, 100% {{ transform: translateX(0); }}
  10%, 50%, 90% {{ transform: translateX(-{distance}px); }}
  30%, 70% {{ transform: translateX({distance}px); }}
}}"""


def keyframes_glow(color="#6366F1"):
    return f"""@keyframes glow {{
  0%, 100% {{ box-shadow: 0 0 5px {color}, 0 0 10px {color}66; }}
  50%      {{ box-shadow: 0 0 20px {color}, 0 0 40px {color}88; }}
}}"""


def keyframes_spin(duration="1s"):
    return f"""@keyframes spin {{
  from {{ transform: rotate(0deg); }}
  to   {{ transform: rotate(360deg); }}
}}
.spin {{
  display: inline-block;
  animation: spin {duration} linear infinite;
}}"""


def keyframes_wave(rotate=15):
    return f"""@keyframes wave {{
  0%, 100% {{ transform: rotate(0deg); }}
  50%      {{ transform: rotate({rotate}deg); }}
}}"""


def build_animation(anim_type, duration, easing, delay, distance, color, other):
    # Slide direction must be one of the four supported values; an empty
    # or bogus --param previously fell through keyframes_slide() with no
    # branch matching, crashing on an unassigned variable.
    slide_direction = other if other in ("up", "down", "left", "right") else "up"

    # The animation shorthand must reference the EXACT keyframes name the
    # builders emit (fade-in, scale-in, slide-<dir>...), otherwise the
    # browser silently runs nothing.
    KEYFRAME_NAMES = {
        "fade": "fade-in",
        "slide": f"slide-{slide_direction}",
        "scale": "scale-in",
    }

    keyframes = {
        "fade": keyframes_fade,
        "slide": lambda: keyframes_slide(slide_direction, distance),
        "scale": lambda: keyframes_scale(other if other else 0.8, 1.0),
        "rotate": lambda: keyframes_rotate(0, 360),
        "bounce": lambda: keyframes_bounce(distance),
        "pulse": lambda: keyframes_pulse(other if other else 1.05),
        "shimmer": lambda: keyframes_shimmer(),
        "flip": lambda: keyframes_flip(),
        "shake": lambda: keyframes_shake(distance),
        "glow": lambda: keyframes_glow(color),
        "spin": lambda: keyframes_spin(),
        "wave": lambda: keyframes_wave(other if other else 15),
    }
    easing_value = EASINGS.get(easing, easing)
    css_keyframes = keyframes[anim_type]()
    class_name = anim_type
    if anim_type == "slide":
        class_name = f"slide-{slide_direction}"
    animation_name = KEYFRAME_NAMES.get(anim_type, anim_type)

    css_class = f""".{class_name} {{
  animation: {animation_name} {duration}s {easing_value} {delay}s both;
}}"""

    return css_keyframes + "\n\n" + css_class


def generate_kit(primary="#2563EB"):
    return f"""/* ===== Animation Kit ===== */
:root {{
  --anim-fast: 150ms;
  --anim-base: 300ms;
  --anim-slow: 600ms;
  --anim-spring: cubic-bezier(0.68, -0.55, 0.265, 1.55);
  --anim-smooth: cubic-bezier(0.4, 0, 0.2, 1);
}}

/* Transitions */
.t-hover {{
  transition: all var(--anim-base) var(--anim-smooth);
}}
.t-hover:hover {{
  transform: translateY(-2px);
}}

.t-press {{
  transition: transform var(--anim-fast) var(--anim-spring);
}}
.t-press:active {{
  transform: scale(0.95);
}}

/* Micro-interactions */
.btn {{
  transition: all var(--anim-base) var(--anim-smooth);
}}
.btn:hover {{
  box-shadow: 0 8px 24px {primary}40;
  transform: translateY(-1px);
}}
.btn:active {{
  transform: scale(0.97);
}}

/* Scroll reveal (paste near your JS to add .reveal on scroll) */
.reveal {{
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 600ms cubic-bezier(0.4, 0, 0.2, 1), transform 600ms cubic-bezier(0.4, 0, 0.2, 1);
}}
.reveal.visible {{
  opacity: 1;
  transform: translateY(0);
}}

/* Stagger helper: .stagger > * */
.stagger > * {{
  opacity: 0;
  animation: fade-slide-up 500ms var(--anim-smooth) forwards;
}}
.stagger > *:nth-child(1) {{ animation-delay: 0ms; }}
.stagger > *:nth-child(2) {{ animation-delay: 80ms; }}
.stagger > *:nth-child(3) {{ animation-delay: 160ms; }}
.stagger > *:nth-child(4) {{ animation-delay: 240ms; }}
.stagger > *:nth-child(5) {{ animation-delay: 320ms; }}
.stagger > *:nth-child(6) {{ animation-delay: 400ms; }}
.stagger > *:nth-child(7) {{ animation-delay: 480ms; }}
.stagger > *:nth-child(8) {{ animation-delay: 560ms; }}

@keyframes fade-slide-up {{
  from {{ opacity: 0; transform: translateY(24px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}

/* Keyframes used by .loader and .skeleton below (previously referenced
   but never defined in this kit, leaving both inert) */
@keyframes spin {{
  from {{ transform: rotate(0deg); }}
  to   {{ transform: rotate(360deg); }}
}}
@keyframes shimmer {{
  from {{ background-position: 200% 0; }}
  to   {{ background-position: -200% 0; }}
}}

/* Loader */
.loader {{
  width: 40px;
  height: 40px;
  border: 4px solid {primary}22;
  border-top-color: {primary};
  border-radius: 50%;
  animation: spin 800ms linear infinite;
}}

/* Skeleton */
.skeleton {{
  background: linear-gradient(90deg, #E2E8F0 25%, #F1F5F9 50%, #E2E8F0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 8px;
}}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {{
  *, *::before, *::after {{
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }}
}}"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Animation Generator - Cyber-Rage")
    parser.add_argument("--list", action="store_true", help="List animation types")
    parser.add_argument("--type", help="Animation type (fade, slide, scale, rotate, bounce, pulse, shimmer, flip, shake, glow, spin, wave)")
    parser.add_argument("--duration", type=float, default=0.5, help="Duration in seconds (default: 0.5)")
    parser.add_argument("--easing", default="ease-out", help=f"Easing function ({', '.join(EASINGS.keys())})")
    parser.add_argument("--delay", type=float, default=0, help="Delay in seconds (default: 0)")
    parser.add_argument("--distance", type=int, default=20, help="Distance in px for slide/bounce/shake (default: 20)")
    parser.add_argument("--color", default="#6366F1", help="Color for glow (default: #6366F1)")
    parser.add_argument("--param", default="", help="Extra param: slide direction (up/down/left/right), scale from, pulse max scale, wave rotate deg")
    parser.add_argument("--kit", action="store_true", help="Generate full animation kit")
    parser.add_argument("--primary", default="#2563EB", help="Primary color for kit")

    args = parser.parse_args()

    if args.list:
        print("Available animations:")
        for a in ["fade", "slide (--param up/down/left/right)", "scale (--param from-scale)", "rotate", "bounce (--distance)", "pulse (--param max-scale)", "shimmer", "flip", "shake (--distance)", "glow (--color)", "spin", "wave (--param deg)"]:
            print(f"  - {a}")
        sys.exit(0)

    if args.kit:
        print(generate_kit(args.primary))
        sys.exit(0)

    if not args.type:
        print("Specify --type (see --list) or --kit")
        sys.exit(1)

    valid = ["fade", "slide", "scale", "rotate", "bounce", "pulse", "shimmer", "flip", "shake", "glow", "spin", "wave"]
    if args.type not in valid:
        print(f"Unknown animation: '{args.type}'. Available: {', '.join(valid)}")
        sys.exit(1)

    print(build_animation(args.type, args.duration, args.easing, args.delay, args.distance, args.color, args.param))
