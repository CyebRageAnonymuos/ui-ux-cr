#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO Audit - Static SEO / HTML head audit: title, meta description,
canonical, Open Graph, Twitter cards, headings structure, images,
links, robots.txt awareness, and hreflang hints.
Cyber-Rage Design Intelligence Engine

Usage: python seo_audit.py index.html
       python seo_audit.py landing.html --json
"""

import argparse
import json
import re
import sys
import io
import os

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def read_file(path):
    if not os.path.exists(path):
        raise SystemExit(f"File not found: {path}")
    with open(path, encoding="utf-8", errors="ignore") as f:
        return f.read()


def audit(html, path=None):
    issues = []
    head = html.split("</head>", 1)[0] if "</head>" in html else html

    def add(severity, category, message, fix):
        issues.append({"severity": severity, "category": category,
                       "message": message, "fix": fix})

    # --- Title ---
    title_m = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if not title_m:
        add("error", "title", "Missing <title>", "Add a unique 50-60 char <title> per page.")
    else:
        title_text = title_m.group(1).strip()
        tlen = len(title_text)
        if tlen == 0:
            add("error", "title", "<title> is empty", "Add a descriptive 50-60 char title.")
        elif tlen > 65:
            add("warning", "title", f"Title is {tlen} chars (may truncate in SERPs)",
                "Keep titles under ~60 characters.")
        elif tlen < 20:
            add("info", "title", f"Title is short ({tlen} chars)",
                "Use 50-60 chars to include primary keyword + brand.")

    # --- Meta description ---
    desc_m = re.search(r'<meta\s+[^>]*name=["\']description["\'][^>]*>', html, re.IGNORECASE)
    if not desc_m:
        add("error", "meta", "Missing meta description",
            "Add <meta name=\"description\"> (140-160 chars, includes CTA).")
    else:
        content_m = re.search(r'content=["\'](.*?)["\']', desc_m.group(0), re.IGNORECASE)
        dlen = len(content_m.group(1)) if content_m else 0
        if dlen == 0:
            add("error", "meta", "Meta description is empty", "Write 140-160 chars.")
        elif dlen > 170:
            add("warning", "meta", f"Meta description is {dlen} chars (will truncate)",
                "Trim to under ~160 characters.")

    # --- Viewport ---
    if "name=\"viewport\"" not in html.replace("'", '"'):
        add("error", "mobile", "Missing viewport meta tag",
            'Add <meta name="viewport" content="width=device-width, initial-scale=1.0">.')

    # --- Charset ---
    if not re.search(r'<meta[^>]+charset', html, re.IGNORECASE):
        add("error", "encoding", "Missing charset declaration",
            'Add <meta charset="UTF-8"> as the first element in <head>.')

    # --- Canonical ---
    if not re.search(r'<link[^>]+rel=["\']canonical["\']', html, re.IGNORECASE):
        add("warning", "canonical", "No canonical URL",
            "Add <link rel=\"canonical\" href=\"...\"> to prevent duplicate-content issues.")

    # --- Open Graph ---
    og_tags = re.findall(r'<meta\s+[^>]*property=["\'](og:[\w:]+)["\'][^>]*>', html, re.IGNORECASE)
    og_have = set(t.lower() for t in og_tags)
    for required in ("og:title", "og:description", "og:image", "og:url"):
        if required not in og_have:
            add("warning", "social", f"Missing {required}",
                f"Add <meta property=\"{required}\" ...> for link previews.")

    # --- Twitter card ---
    if not re.search(r'<meta\s+[^>]*name=["\']twitter:card["\']', html, re.IGNORECASE):
        add("info", "social", "No twitter:card tag",
            'Add <meta name="twitter:card" content="summary_large_image">.')

    # --- Heading structure ---
    h1s = re.findall(r"<h1\b", html, re.IGNORECASE)
    if len(h1s) == 0:
        add("error", "headings", "No <h1> on the page",
            "Every page needs exactly one h1 with the primary keyword.")
    elif len(h1s) > 1:
        add("warning", "headings", f"{len(h1s)} <h1> tags (should be 1)",
            "Use one h1; demote the rest to h2/h3.")
    headings = [int(m) for m in re.findall(r"<h([1-6])\b", html, re.IGNORECASE)]
    for prev, cur in zip(headings, headings[1:]):
        if cur - prev > 1:
            add("warning", "headings", f"Heading skip: h{prev} -> h{cur}",
                "Keep heading levels sequential for screen readers and SEO.")
            break

    # --- Images ---
    imgs = re.findall(r"<img\b[^>]*>", html, re.IGNORECASE)
    missing_alt = [i for i in imgs if not re.search(r'\balt=', i)]
    if missing_alt:
        add("error", "images", f"{len(missing_alt)} <img> without alt",
            "Add descriptive alt attributes (empty alt for decorative only).")
    lazy_candidates = [i for i in imgs if "loading=" not in i]
    if len(lazy_candidates) > 3:
        add("info", "performance", f"{len(lazy_candidates)} images without loading attr",
            'Add loading="lazy" to below-the-fold images.')
    img_count = len(imgs)
    webp = sum(1 for i in imgs if ".webp" in i.lower())

    # --- Links ---
    bare_hash_links = re.findall(r'<a\s+[^>]*href=["\']#["\']', html, re.IGNORECASE)
    if len(bare_hash_links) > 2:
        add("info", "links", f"{len(bare_hash_links)} placeholder links (href=\"#\")",
            "Wire real URLs or remove until ready.")

    # --- robots / sitemap awareness (sibling files) ---
    if path:
        base_dir = os.path.dirname(os.path.abspath(path))
        if not os.path.exists(os.path.join(base_dir, "robots.txt")):
            add("info", "crawling", "No robots.txt found next to the file",
                "Add robots.txt referencing your sitemap URL.")
        if not os.path.exists(os.path.join(base_dir, "sitemap.xml")):
            add("info", "crawling", "No sitemap.xml found next to the file",
                "Add a sitemap and reference it from robots.txt.")

    score = 100
    score -= sum({"error": 15, "warning": 7, "info": 2}[i["severity"]] for i in issues)
    score = max(0, score)

    return {
        "file": path or "(html string)",
        "score": score,
        "counts": {
            "errors": sum(1 for i in issues if i["severity"] == "error"),
            "warnings": sum(1 for i in issues if i["severity"] == "warning"),
            "infos": sum(1 for i in issues if i["severity"] == "info"),
        },
        "stats": {"images": img_count, "webp_images": webp, "headings": len(headings)},
        "issues": issues,
    }


def print_report(result):
    c = result["counts"]
    score_icon = "🟢" if result["score"] >= 80 else "🟡" if result["score"] >= 50 else "🔴"
    print(f"SEO Audit: {result['file']}")
    print("=" * 60)
    print(f"{score_icon} Score: {result['score']}/100  |  "
          f"Errors: {c['errors']}  Warnings: {c['warnings']}  Info: {c['infos']}")
    print("=" * 60)
    if result["issues"]:
        icons = {"error": "✗", "warning": "△", "info": "·"}
        for i in result["issues"]:
            print(f"[{icons[i['severity']]}] {i['category'].upper()}: {i['message']}")
            print(f"      fix: {i['fix']}")
    else:
        print("✓ No issues found. On-page SEO looks solid!")
    print()
    print(f"Stats: {result['stats']['images']} images "
          f"({result['stats']['webp_images']} webp), "
          f"{result['stats']['headings']} headings")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SEO Audit - Cyber-Rage")
    parser.add_argument("file", help="HTML file to audit")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    html = read_file(args.file)
    result = audit(html, args.file)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)
        if result["counts"]["errors"] > 0:
            sys.exit(1)
