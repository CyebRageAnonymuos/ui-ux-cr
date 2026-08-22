#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI UX CR Search v2 - Enhanced BM25 search engine with fuzzy matching
Cyber-Rage Design Intelligence Engine

Usage: python search.py "<query>" [--domain <domain>] [--stack <stack>] [--max-results 3]
       python search.py "<query>" --design-system [-p "Project Name"]
       python search.py "<query>" --design-system --persist [-p "Project Name"] [--page "dashboard"]
       python search.py "<query>" --multi-domains style,color,typography
       python search.py "<query>" --analyze
       python search.py "<query>" --export-css           # Export CSS variables
       python search.py "<query>" --export-tailwind      # Export Tailwind config
       python search.py "<query>" --wcag                 # WCAG contrast check
"""

import argparse
import sys
import io
import json
from core import CSV_CONFIG, AVAILABLE_STACKS, MAX_RESULTS, search, search_stack, multi_search
from design_system import generate_design_system, persist_design_system
from color_tools import check_contrast, generate_theme, generate_palette

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def format_output(result):
    """Format results for Claude consumption (token-optimized)"""
    if "error" in result:
        return f"Error: {result['error']}"

    output = []
    if result.get("stack"):
        output.append(f"## UI UX CR Stack Guidelines")
        output.append(f"**Stack:** {result['stack']} | **Query:** {result['query']}")
    elif result.get("domains"):
        output.append(f"## UI UX CR Multi-Domain Search")
        output.append(f"**Domains:** {', '.join(result['domains'])} | **Query:** {result.get('query', 'N/A')}")
    else:
        output.append(f"## UI UX CR Search Results")
        output.append(f"**Domain:** {result['domain']} | **Query:** {result['query']}")
    output.append(f"**Source:** {result.get('file', 'multiple')} | **Found:** {result.get('count', 0)} results\n")

    if "domains" in result:
        for domain, domain_result in result.get("results", {}).items():
            output.append(f"### Domain: {domain}")
            for i, row in enumerate(domain_result.get("results", []), 1):
                output.append(f"#### Result {i}")
                for key, value in row.items():
                    value_str = str(value)
                    if len(value_str) > 300:
                        value_str = value_str[:300] + "..."
                    output.append(f"- **{key}:** {value_str}")
                output.append("")
    else:
        for i, row in enumerate(result.get('results', []), 1):
            output.append(f"### Result {i}")
            for key, value in row.items():
                value_str = str(value)
                if len(value_str) > 300:
                    value_str = value_str[:300] + "..."
                output.append(f"- **{key}:** {value_str}")
            output.append("")

    return "\n".join(output)


def analyze_project(query):
    """Comprehensive project analysis with recommendations across all domains"""
    domains = ["product", "style", "color", "typography", "landing", "ux", "component", "animation", "responsive", "background"]
    results = multi_search(query, domains, max_results=3)

    output = []
    output.append("## UI UX CR - Project Analysis")
    output.append(f"**Query:** {query}")
    output.append("")

    search_results = results.get("results", {})
    for domain, result in search_results.items():
        results_list = result.get("results", [])
        if results_list:
            output.append(f"### {domain.upper()} Recommendations")
            for i, row in enumerate(results_list, 1):
                output.append(f"**{i}.** {json.dumps(row, ensure_ascii=False)[:200]}")
            output.append("")

    return "\n".join(output)


def export_css_variables(query):
    """Export CSS custom properties based on search results"""
    color_result = search(query, "color", 1)
    colors = color_result.get("results", [])
    if not colors:
        return "/* No color data found for query */"

    c = colors[0]
    primary = c.get("Primary (Hex)", "#2563EB")
    secondary = c.get("Secondary (Hex)", "#3B82F6")
    cta = c.get("CTA (Hex)", "#F97316")
    bg = c.get("Background (Hex)", "#F8FAFC")
    text = c.get("Text (Hex)", "#1E293B")
    border = c.get("Border (Hex)", "#E2E8F0")

    # Generate extended palette
    theme = generate_theme(primary)
    css_vars = theme.get("css_variables", {})

    lines = []
    lines.append("/* CSS Custom Properties - UI UX CR v2 */")
    lines.append(":root {")
    lines.append(f"  --color-primary: {primary};")
    lines.append(f"  --color-primary-light: {css_vars.get('--primary-300', secondary)};")
    lines.append(f"  --color-primary-dark: {css_vars.get('--primary-700', '#1E40AF')};")
    lines.append(f"  --color-secondary: {secondary};")
    lines.append(f"  --color-cta: {cta};")
    lines.append(f"  --color-background: {bg};")
    lines.append(f"  --color-surface: #FFFFFF;")
    lines.append(f"  --color-text: {text};")
    lines.append(f"  --color-text-secondary: #64748B;")
    lines.append(f"  --color-border: {border};")
    lines.append(f"  --color-success: #22C55E;")
    lines.append(f"  --color-warning: #F59E0B;")
    lines.append(f"  --color-error: #EF4444;")
    lines.append(f"  --color-info: #3B82F6;")
    # Extended palette must live INSIDE the :root rule - custom
    # properties at the stylesheet top level are invalid CSS and get
    # dropped by parsers, silently losing the whole palette.
    lines.append("")
    lines.append("  /* Extended Primary Palette */")
    for key, value in theme.get("primary", {}).get("shades", {}).items():
        lines.append(f"  --primary-{key}: {value};")
    lines.append("}")
    lines.append("")
    lines.append("/* Dark Mode */")
    lines.append("@media (prefers-color-scheme: dark) {")
    lines.append("  :root {")
    lines.append("    --color-background: #0F172A;")
    lines.append("    --color-surface: #1E293B;")
    lines.append("    --color-text: #F8FAFC;")
    lines.append("    --color-text-secondary: #94A3B8;")
    lines.append("    --color-border: #334155;")
    lines.append("  }")
    lines.append("}")

    return "\n".join(lines)


def export_tailwind_config(query):
    """Export Tailwind CSS config extension"""
    color_result = search(query, "color", 1)
    typography_result = search(query, "typography", 1)

    colors = color_result.get("results", [])
    typos = typography_result.get("results", [])

    primary = colors[0].get("Primary (Hex)", "#2563EB") if colors else "#2563EB"
    secondary = colors[0].get("Secondary (Hex)", "#3B82F6") if colors else "#3B82F6"
    cta = colors[0].get("CTA (Hex)", "#F97316") if colors else "#F97316"

    heading_font = typos[0].get("Heading Font", "Inter") if typos else "Inter"
    body_font = typos[0].get("Body Font", "Inter") if typos else "Inter"

    theme = generate_theme(primary)
    primary_shades = theme.get("primary", {}).get("shades", {})

    config = {
        "theme": {
            "extend": {
                "colors": {
                    "primary": {k: v for k, v in primary_shades.items()},
                    "secondary": {"500": secondary},
                    "cta": {"500": cta},
                },
                "fontFamily": {
                    "heading": [heading_font, "sans-serif"],
                    "body": [body_font, "sans-serif"],
                }
            }
        }
    }

    return json.dumps(config, indent=2)


def wcag_check(query):
    """Run WCAG contrast check on colors from search results"""
    color_result = search(query, "color", 2)
    results_list = color_result.get("results", [])

    output = []
    output.append("# WCAG Contrast Check - UI UX CR v2")
    output.append(f"**Query:** {query}")
    output.append("")

    for row in results_list:
        product = row.get("Product Type", "Unknown")
        bg = row.get("Background (Hex)", "#FFFFFF")
        text = row.get("Text (Hex)", "#0F172A")
        primary = row.get("Primary (Hex)", "#2563EB")

        output.append(f"## {product}")
        result_text = check_contrast(text, bg)
        result_primary = check_contrast(primary, bg)

        output.append(f"- **Text ({text}) on Background ({bg}):** {result_text['ratio']}:1 - {result_text['grade']}")
        output.append(f"- **Primary ({primary}) on Background ({bg}):** {result_primary['ratio']}:1 - {result_primary['grade']}")
        output.append(f"- WCAG AA (4.5:1): {'PASS' if result_text['wcag_aa_normal'] else 'FAIL'}")
        output.append(f"- WCAG AAA (7:1): {'PASS' if result_text['wcag_aaa_normal'] else 'FAIL'}")
        output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UI UX CR Search v2 - Cyber-Rage Design Intelligence Engine")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="Search domain")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help="Stack-specific search")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="Max results (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--design-system", "-ds", action="store_true", help="Generate complete design system")
    parser.add_argument("--project-name", "-p", type=str, default=None, help="Project name")
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"], default="ascii", help="Output format")
    parser.add_argument("--persist", action="store_true", help="Save design system to design-system/")
    parser.add_argument("--page", type=str, default=None, help="Create page-specific override file")
    parser.add_argument("--output-dir", "-o", type=str, default=None, help="Output directory")
    parser.add_argument("--multi-domains", "-md", type=str, default=None, help="Comma-separated domains to search")
    parser.add_argument("--analyze", "-a", action="store_true", help="Comprehensive project analysis")
    parser.add_argument("--export-css", action="store_true", help="Export CSS custom properties")
    parser.add_argument("--export-tailwind", action="store_true", help="Export Tailwind config")
    parser.add_argument("--wcag", action="store_true", help="WCAG contrast check")
    parser.add_argument("--color-palette", action="store_true", help="Generate color palette")

    args = parser.parse_args()

    if args.export_css:
        print(export_css_variables(args.query))
    elif args.export_tailwind:
        print(export_tailwind_config(args.query))
    elif args.wcag:
        print(wcag_check(args.query))
    elif args.color_palette:
        from color_tools import generate_palette, format_palette_output
        result = search(args.query, "color", 1)
        colors = result.get("results", [])
        if colors:
            primary = colors[0].get("Primary (Hex)", "#2563EB")
            palette = generate_palette(primary)
            print(format_palette_output(palette, args.format if args.format != "ascii" else "ascii"))
        else:
            print("No color data found for query. Try a different query.")
    elif args.analyze:
        print(analyze_project(args.query))
    elif args.design_system:
        result = generate_design_system(
            args.query,
            args.project_name,
            args.format,
            persist=args.persist,
            page=args.page,
            output_dir=args.output_dir
        )
        print(result)

        if args.persist:
            # Mirror persist_design_system's actual slug logic exactly:
            # it derives the slug from project_name OR the uppercased
            # query - computing it from "default" here pointed users at
            # directories that were never created.
            effective_name = args.project_name or args.query.upper()
            project_slug = effective_name.lower().replace(' ', '-')
            base_dir = args.output_dir or "."
            print("\n" + "=" * 60)
            print(f"Design system persisted to {base_dir}/design-system/{project_slug}/")
            print(f"   {base_dir}/design-system/{project_slug}/MASTER.md")
            if args.page:
                page_filename = args.page.lower().replace(' ', '-')
                print(f"   {base_dir}/design-system/{project_slug}/pages/{page_filename}.md")
            print("=" * 60)
    elif args.multi_domains:
        domains = [d.strip() for d in args.multi_domains.split(",")]
        result = multi_search(args.query, domains, args.max_results)
        result["domains"] = domains
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
    elif args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
    else:
        result = search(args.query, args.domain, args.max_results)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
