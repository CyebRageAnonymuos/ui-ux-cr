#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mockup Generator - Generate ASCII wireframes and mockups for
desktop, mobile, tablet, and dashboard layouts
Cyber-Rage Design Intelligence Engine

Usage: python mockup_generator.py --type desktop
       python mockup_generator.py --type landing
       python mockup_generator.py --type dashboard --width 90
"""

import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def line(width, char="─"):
    return "┌" + char * width + "┐"


def row(content, width, char="│"):
    return char + content.ljust(width) + char


def label(text, width):
    text = f" {text} "
    return text[:width].ljust(width)


def generate_desktop(width=80):
    lines = []
    lines.append(line(width))
    lines.append(row("  LOGO                    NAV: Home  About  Contact  [Login]  [Sign Up]", width))
    lines.append(line(width))
    lines.append(row("", width))
    lines.append(row("  ┌────────────────────────────────────────────┐", width))
    lines.append(row("  │                                            │", width))
    lines.append(row("  │           HERO HEADLINE                     │", width))
    lines.append(row("  │      Sub-headline text goes here            │", width))
    lines.append(row("  │                                            │", width))
    lines.append(row("  │      [Primary CTA]   [Secondary CTA]        │", width))
    lines.append(row("  └────────────────────────────────────────────┘", width))
    lines.append(row("", width))
    lines.append(row("  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐", width))
    lines.append(row("  │  Feature 1  │ │  Feature 2  │ │  Feature 3  │", width))
    lines.append(row("  │   icon +    │ │   icon +    │ │   icon +    │", width))
    lines.append(row("  │   text      │ │   text      │ │   text      │", width))
    lines.append(row("  └─────────────┘ └─────────────┘ └─────────────┘", width))
    lines.append(row("", width))
    lines.append(row("  ┌────────────────────────────────────────────┐", width))
    lines.append(row("  │            CTA / NEWSLETTER SECTION         │", width))
    lines.append(row("  │            [email input] [Subscribe]        │", width))
    lines.append(row("  └────────────────────────────────────────────┘", width))
    lines.append(row("", width))
    lines.append(row("  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐", width))
    lines.append(row("  │  Footer Col 1 │ │  Footer Col 2 │ │  Footer Col 3 │", width))
    lines.append(row("  └───────────────┘ └───────────────┘ └───────────────┘", width))
    lines.append(line(width))
    return "\n".join(lines)


def generate_dashboard(width=80):
    lines = []
    lines.append(line(width))
    lines.append(row("  ┌──────┐ ┌──────────────────────────────────────────────┐", width))
    lines.append(row("  │ LOGO │ │  SEARCH BAR                     [bell] [JD]  │", width))
    lines.append(row("  ├──────┤ ├──────────────────────────────────────────────┤", width))
    lines.append(row("  │      │ │  ┌──────────┐ ┌──────────┐ ┌──────────┐      │", width))
    lines.append(row("  │ Nav  │ │  │ Revenue  │ │  Users   │ │  Orders  │      │", width))
    lines.append(row("  │      │ │  │  $48,290 │ │  2,847   │ │  1,204   │      │", width))
    lines.append(row("  │      │ │  │  ↑ 12.5% │ │  ↑ 8.2%  │ │  ↓ 2.1%  │      │", width))
    lines.append(row("  │      │ ├──────────┴──────────┴──────────┘      │", width))
    lines.append(row("  │      │ │  ┌──────────────────────┐ ┌──────────┐ │", width))
    lines.append(row("  │      │ │  │    CHART (line/bar)  │ │  Recent  │ │", width))
    lines.append(row("  │      │ │  │     ▁▂▃▅▇▅▃▂         │ │  Activity│ │", width))
    lines.append(row("  │      │ │  └──────────────────────┘ └──────────┘ │", width))
    lines.append(row("  │      │ │  ┌──────────────────────────────────┐  │", width))
    lines.append(row("  │      │ │  │  TABLE: Name | Email | Status    │  │", width))
    lines.append(row("  │      │ │  └──────────────────────────────────┘  │", width))
    lines.append(row("  └──────┘ └──────────────────────────────────────┘", width))
    lines.append(line(width))
    return "\n".join(lines)


def generate_mobile(width=36):
    # All content rows go through row()/inner boxes so the right border
    # stays aligned at any width (previously most rows were hardcoded
    # for one width and ragged everywhere else).
    def inner_box(title, inner_width):
        top = "┌" + "─" * inner_width + "┐"
        mid = "│" + title.center(inner_width) + "│"
        bot = "└" + "─" * inner_width + "┘"
        return top, mid, bot

    def sep():
        return "├" + "─" * width + "┤"

    lines = []
    lines.append(line(width))
    lines.append(row(label(" 9:41 AM", width - 2), width))
    lines.append(sep())
    lines.append(row("  [menu]  Brand" + " " * max(0, width - 30) + "[cart] ", width))
    lines.append(sep())
    lines.append(row("", width))
    box_w = max(10, width - 10)
    top, mid, bot = inner_box("HERO IMAGE", box_w)
    lines.append(row("  " + top, width))
    lines.append(row("  " + mid, width))
    lines.append(row("  " + bot, width))
    lines.append(row("", width))
    lines.append(row("  Big headline", width))
    lines.append(row("  supporting text...", width))
    lines.append(row("", width))
    cta = "[ " + "─" * max(4, width - 18) + " CTA " + "─" * max(4, width - 18) + " ]"
    lines.append(row("  " + cta[:max(4, width - 4)], width))
    lines.append(row("", width))
    top, mid, bot = inner_box("Product 1", max(8, width - 12))
    lines.append(row("  " + top, width))
    lines.append(row("  " + mid, width))
    lines.append(row("  " + bot, width))
    lines.append(row("", width))
    lines.append(sep())
    lines.append(row("  [home]  [search]  [add]  [chat]  [me]", width))
    lines.append("└" + "─" * width + "┘")
    return "\n".join(lines)


def generate_landing(width=90):
    lines = []
    lines.append(line(width))
    lines.append(row("  NAVBAR: [logo]  Features  Pricing  Docs  About      [Sign in] [Get started]", width))
    lines.append(line(width))
    lines.append(row("  ┌───────────────────────────────────────────────────────────┐", width))
    lines.append(row("  │  H1: Build faster with Cyber-Rage                         │", width))
    lines.append(row("  │  Sub: The all-in-one design toolkit for modern teams.     │", width))
    lines.append(row("  │                                                           │", width))
    lines.append(row("  │        [ Start Free ]            [ Watch Demo ▶ ]         │", width))
    lines.append(row("  └───────────────────────────────────────────────────────────┘", width))
    lines.append(row("  Trusted by: [company logos row ▄▄▄▄▄ ▄▄▄ ▄▄▄▄▄▄ ▄▄▄]", width))
    lines.append(row("", width))
    lines.append(row("  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐", width))
    lines.append(row("  │ Feature1 │ │ Feature2 │ │ Feature3 │ │ Feature4 │", width))
    lines.append(row("  └──────────┘ └──────────┘ └──────────┘ └──────────┘", width))
    lines.append(row("", width))
    lines.append(row("  ┌───────────────────────────┐   ┌───────────────────────────┐", width))
    lines.append(row("  │  Social Proof / Testimonial│   │  Product Screenshot      │", width))
    lines.append(row("  │  \"This changed our lives\" │   │  ┌───────────────┐       │", width))
    lines.append(row("  └───────────────────────────┘   │  │   UI mockup   │       │", width))
    lines.append(row("                                   │  └───────────────┘       │", width))
    lines.append(row("                                   └───────────────────────────┘", width))
    lines.append(row("", width))
    lines.append(row("  ┌───────────────────────────────────────────────────────────┐", width))
    lines.append(row("  │  CTA SECTION — [ Join 10,000+ teams ]                     │", width))
    lines.append(row("  └───────────────────────────────────────────────────────────┘", width))
    lines.append(row("", width))
    lines.append(row("  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐", width))
    lines.append(row("  │ Footer Col │ │ Footer Col │ │ Footer Col │ │ Social     │", width))
    lines.append(row("  └────────────┘ └────────────┘ └────────────┘ └────────────┘", width))
    lines.append(line(width))
    return "\n".join(lines)


def generate_login(width=60):
    lines = []
    lines.append(line(width))
    lines.append(row("", width))
    lines.append(row("                          ┌─────────────────────────┐", width))
    lines.append(row("                          │        [ LOGO ]         │", width))
    lines.append(row("                          │   Welcome back!         │", width))
    lines.append(row("                          │                         │", width))
    lines.append(row("                          │   Email                 │", width))
    lines.append(row("                          │   ┌───────────────┐     │", width))
    lines.append(row("                          │   │               │     │", width))
    lines.append(row("                          │   └───────────────┘     │", width))
    lines.append(row("                          │   Password              │", width))
    lines.append(row("                          │   ┌───────────────┐     │", width))
    lines.append(row("                          │   │ •••••••••      │     │", width))
    lines.append(row("                          │   └───────────────┘     │", width))
    lines.append(row("                          │                         │", width))
    lines.append(row("                          │   [ Sign In ]           │", width))
    lines.append(row("                          │   ──── or ────          │", width))
    lines.append(row("                          │   [ Continue with G ]   │", width))
    lines.append(row("                          │   Forgot password?      │", width))
    lines.append(row("                          └─────────────────────────┘", width))
    lines.append(row("", width))
    lines.append(line(width))
    return "\n".join(lines)


def generate_homepage(width=90):
    return generate_landing(width)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mockup Generator - ASCII Wireframes")
    parser.add_argument("--type", default="desktop", help="Mockup type: desktop, dashboard, mobile, landing, login, homepage")
    parser.add_argument("--width", type=int, default=80, help="Total width in chars (default: 80)")

    args = parser.parse_args()

    generators = {
        "desktop": generate_desktop,
        "dashboard": generate_dashboard,
        "mobile": generate_mobile,
        "landing": generate_landing,
        "login": generate_login,
        "homepage": generate_homepage,
    }

    if args.type not in generators:
        print(f"Unknown type: '{args.type}'. Available: {', '.join(generators.keys())}")
        sys.exit(1)

    print(generators[args.type](args.width))
