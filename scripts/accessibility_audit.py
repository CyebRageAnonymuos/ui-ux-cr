#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Accessibility Audit - Audit HTML for WCAG compliance issues:
contrast, alt text, labels, heading order, aria attributes, form fields
Cyber-Rage Design Intelligence Engine

Usage: python accessibility_audit.py file.html
       python accessibility_audit.py --url https://example.com
       python accessibility_audit.py file.html --json
"""

import argparse
import io
import json
import os
import re
import sys
import urllib.request

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def hex_to_rgb(hex_color):
    hex_color = hex_color.strip().lstrip('#')
    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)
    if not re.match(r'^[0-9a-fA-F]{6}$', hex_color):
        return None
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_luminance(rgb):
    def channel(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg, bg):
    l1, l2 = rgb_to_luminance(fg), rgb_to_luminance(bg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)


def extract_styles(html):
    styles = {}
    for match in re.finditer(r'<style[^>]*>(.*?)</style>', html, re.DOTALL | re.IGNORECASE):
        for sel in re.finditer(r'([^{}]+)\{([^{}]+)\}', match.group(1)):
            selector = sel.group(1).strip()
            rules = dict(re.findall(r'([\w-]+)\s*:\s*([^;]+);', sel.group(2)))
            styles[selector] = rules
    return styles


def get_style_for(styles, selector):
    for sel, rules in styles.items():
        sel = sel.strip()
        if sel == selector or sel.endswith(" " + selector) or sel.startswith(selector):
            return rules
        if ":" in sel and sel.split(":")[0].strip() == selector:
            return rules
    return {}


def find_color(styles, html_element, props):
    for p in props:
        if p in styles:
            color = styles[p]
            match = re.search(r'#[0-9a-fA-F]{3,8}', color)
            if match:
                rgb = hex_to_rgb(match.group(0))
                if rgb:
                    return rgb, color
            match = re.search(r'rgba?\(([^)]+)\)', color)
            if match:
                nums = [int(float(n)) for n in match.group(1).replace(' ', '').split(',')[:3]]
                return tuple(nums), color
    return None, None


def audit_html(html, source_name):
    issues = []
    styles = extract_styles(html)

    img_tags = re.findall(r'<img[^>]*>', html, re.IGNORECASE)
    for img in img_tags:
        if 'alt=' not in img:
            line = img[:60]
            issues.append({
                "severity": "error",
                "wcag": "1.1.1",
                "message": "Image missing alt attribute",
                "element": line,
            })
        elif re.search(r'alt=["\']\s*["\']', img):
            issues.append({
                "severity": "warning",
                "wcag": "1.1.1",
                "message": "Empty alt attribute - use only for decorative images",
                "element": img[:60],
            })

    for tag in re.finditer(r'<(button|input|select|textarea|a)(\s[^>]*)?>', html, re.IGNORECASE):
        tag_type, attrs_str = tag.group(1).lower(), tag.group(2) or ""
        attrs_str_lower = attrs_str.lower()
        if tag_type == "input":
            input_type = re.search(r'type=["\']([^"\']+)', attrs_str_lower)
            if input_type and input_type.group(1) in ("hidden", "submit", "button", "reset"):
                continue
        if tag_type in ("button", "a"):
            content = tag.group(0)
            closing = re.search(rf'</{tag_type}>', html[tag.end():], re.IGNORECASE)
            if closing:
                inner = html[tag.end():tag.end() + closing.start()]
                if len(inner.strip()) <= 1 and "aria-label" not in attrs_str_lower and "title" not in attrs_str_lower:
                    issues.append({
                        "severity": "error",
                        "wcag": "4.1.2",
                        "message": f"<{tag_type}> has no accessible name (empty content, add aria-label or title)",
                        "element": tag.group(0)[:60],
                    })
        elif tag_type in ("input", "select", "textarea"):
            has_label = (
                "aria-label" in attrs_str_lower
                or "aria-labelledby" in attrs_str_lower
                or "title" in attrs_str_lower
            )
            if not has_label:
                form_id = re.search(r'id=["\']([^"\']+)', attrs_str_lower)
                has_for = False
                if form_id:
                    for_label = re.search(rf'<label[^>]*for=["\']{re.escape(form_id.group(1))}["\']', html, re.IGNORECASE)
                    has_for = bool(for_label)
                if not has_for:
                    issues.append({
                        "severity": "warning",
                        "wcag": "3.3.2",
                        "message": f"<{tag_type}> has no associated label (add <label for=\"id\">, aria-label, or aria-labelledby)",
                        "element": tag.group(0)[:60],
                    })

    headings = [int(m.group(1)) for m in re.finditer(r'<h([1-6])\b', html, re.IGNORECASE)]
    if headings:
        if headings[0] != 1:
            issues.append({
                "severity": "warning",
                "wcag": "1.3.1",
                "message": f"Page starts with h{headings[0]} - should start with h1",
            })
        prev = headings[0]
        for h in headings[1:]:
            if h - prev > 1:
                issues.append({
                    "severity": "warning",
                    "wcag": "1.3.1",
                    "message": f"Heading level skipped: h{prev} -> h{h}",
                })
            prev = h

    html_match = re.match(r'<html[^>]*>', html, re.IGNORECASE)
    if html_match and "lang" not in html_match.group(0).lower():
        issues.append({
            "severity": "warning",
            "wcag": "3.1.1",
            "message": "<html> tag missing lang attribute",
        })

    if "<title>" not in html.lower():
        issues.append({
            "severity": "error",
            "wcag": "2.4.2",
            "message": "Document missing <title> tag",
        })

    fg_rgb, _ = find_color(styles, html, ["color", "--color", "--text"])
    bg_rgb, _ = find_color(styles, html, ["background", "background-color", "--bg"])
    body_style = get_style_for(styles, "body") or get_style_for(styles, ":root") or get_style_for(styles, "html")
    if body_style:
        fg_rgb, _ = find_color(body_style, html, ["color", "--color", "--text"])
        bg_rgb, _ = find_color(body_style, html, ["background", "background-color", "--bg"])
    if fg_rgb and bg_rgb:
        ratio = contrast_ratio(fg_rgb, bg_rgb)
        if ratio < 4.5:
            issues.append({
                "severity": "error",
                "wcag": "1.4.3",
                "message": f"Contrast ratio {ratio:.2f}:1 below WCAG AA 4.5:1 (text on background)",
                "detail": f"fg={fg_rgb} bg={bg_rgb}",
            })
        elif ratio < 7:
            issues.append({
                "severity": "info",
                "wcag": "1.4.6",
                "message": f"Contrast ratio {ratio:.2f}:1 meets AA but below AAA 7:1",
                "detail": f"fg={fg_rgb} bg={bg_rgb}",
            })
        else:
            issues.append({
                "severity": "pass",
                "wcag": "1.4.3",
                "message": f"Contrast ratio {ratio:.2f}:1 meets WCAG AAA",
                "detail": f"fg={fg_rgb} bg={bg_rgb}",
            })

    if not issues:
        issues.append({
            "severity": "pass",
            "wcag": "all",
            "message": "No issues found in automated checks (manual review recommended)",
        })

    return issues


def print_report(issues, source_name):
    counts = {"error": 0, "warning": 0, "info": 0, "pass": 0}
    for i in issues:
        counts[i["severity"]] += 1

    print(f"Accessibility Audit: {source_name}")
    print(f"{'=' * 60}")
    print(f"Errors: {counts['error']}  |  Warnings: {counts['warning']}  |  Info: {counts['info']}  |  Passed: {counts['pass']}")
    print(f"{'=' * 60}")
    for i in issues:
        icon = {"error": "✗", "warning": "△", "info": "·", "pass": "✓"}[i["severity"]]
        print(f"[{icon}] {i['severity'].upper()} | WCAG {i['wcag']} | {i['message']}")
        if "element" in i:
            print(f"      → {i['element']}")
        if "detail" in i:
            print(f"      → {i['detail']}")
    print()
    if counts["error"] + counts["warning"] == 0:
        print("✓ No issues found. WCAG compliance looks good!")
    else:
        print("Fix the issues above to improve accessibility (WCAG 2.1 AA).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Accessibility Audit - Cyber-Rage")
    parser.add_argument("file", nargs="?", help="HTML file to audit")
    parser.add_argument("--url", help="URL to audit (fetches HTML)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if args.url:
        try:
            req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0"})
            html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="replace")
            source = args.url
        except Exception as e:
            print(f"Failed to fetch URL: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.file:
        if not os.path.exists(args.file):
            print(f"File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(args.file, encoding="utf-8", errors="replace") as f:
            html = f.read()
        source = args.file
    else:
        print("Specify a file or --url")
        sys.exit(1)

    issues = audit_html(html, source)
    if args.json:
        print(json.dumps(issues, ensure_ascii=False, indent=2))
    else:
        print_report(issues, source)
