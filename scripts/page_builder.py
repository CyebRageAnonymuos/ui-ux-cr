#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Builder - Compose full HTML pages from the component library
navbar + hero + features + pricing + cta + footer
Cyber-Rage Design Intelligence Engine

Usage: python page_builder.py --product "SaaS (General)" --sections navbar,hero,features,cta,footer
       python page_builder.py --product "Micro SaaS" --sections hero,features,cta,footer --out landing.html
       python page_builder.py --list
"""

import argparse
import os
import re
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ALL_SECTIONS = ["navbar", "hero", "features", "pricing", "cta", "footer", "form", "card", "modal", "table", "sidebar", "dashboard"]


def load_component(name, product):
    import subprocess
    result = subprocess.run(
        [sys.executable, os.path.join(BASE_DIR, "component_generator.py"),
         "--component", name, "--product", product],
        capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode != 0:
        return "", result.stderr.strip()
    out = result.stdout

    header = []
    for line in out.splitlines():
        if line.startswith("/*"):
            header.append(line)
        else:
            break

    css_match = re.search(r'<!-- ===== Required CSS variables.*?-->.*?\n(.*)$', out, re.DOTALL)
    css_block = css_match.group(1) if css_match else ""

    html_start = out.find("<!-- Navbar") if "<!-- Navbar" in out else None
    if html_start is None:
        for marker in ["<!-- Hero Section", "<!-- Features Section", "<!-- Pricing Section",
                       "<!-- CTA Section", "<!-- Footer", "<!-- Contact Form", "<!-- Product Card",
                       "<!-- Modal", "<!-- Data Table", "<!-- Sidebar", "<!-- Dashboard"]:
            idx = out.find(marker)
            if idx != -1:
                html_start = idx
                break
    if html_start is None:
        return "", "Could not extract HTML from component output"
    html_end = out.find("<!-- ===== Required CSS")
    if html_end == -1:
        html_end = len(out)
    html = out[html_start:html_end].rstrip()

    return html, css_block


def get_css_variables(product):
    import subprocess
    result = subprocess.run(
        [sys.executable, os.path.join(BASE_DIR, "component_generator.py"),
         "--component", "hero", "--product", product],
        capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode != 0:
        return ""
    out = result.stdout
    idx = out.find("/* Design tokens")
    if idx == -1:
        return ""
    return out[idx:].rstrip()


def build_page(sections, product, title="Landing Page", with_css_vars=True):
    parts = []
    css_parts = []
    for sec in sections:
        html, css = load_component(sec, product)
        if html:
            parts.append(html)
        if css:
            css_parts.append(css)

    css_block = get_css_variables(product) if with_css_vars else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | {product}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
{css_block}
  </style>
</head>
<body class="min-h-screen">
{chr(10).join(parts)}
</body>
</html>"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Page Builder - Cyber-Rage")
    parser.add_argument("--product", default="SaaS (General)", help="Product type (e.g. 'SaaS (General)')")
    parser.add_argument("--sections", default="navbar,hero,features,cta,footer", help="Comma-separated sections")
    parser.add_argument("--title", default="Landing Page", help="Page title")
    parser.add_argument("--out", help="Write to file instead of stdout")
    parser.add_argument("--list", action="store_true", help="List available sections")
    parser.add_argument("--no-vars", action="store_true", help="Skip CSS variables block")

    args = parser.parse_args()

    if args.list:
        print("Available sections:")
        for s in ALL_SECTIONS:
            print(f"  - {s}")
        print("\nExample: python page_builder.py --product 'SaaS (General)' --sections navbar,hero,features,pricing,cta,footer")
        sys.exit(0)

    sections = [s.strip() for s in args.sections.split(",") if s.strip()]
    invalid = [s for s in sections if s not in ALL_SECTIONS]
    if invalid:
        print(f"Unknown sections: {', '.join(invalid)}. Available: {', '.join(ALL_SECTIONS)}")
        sys.exit(1)

    html = build_page(sections, args.product, args.title, with_css_vars=not args.no_vars)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Page written to {args.out} ({len(html)} bytes)")
        print(f"Open it: xdg-open {args.out}  (or open {args.out})")
    else:
        print(html)
