#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Layout Generator - Generate grid systems, spacing scales, container widths,
breakpoints, and responsive layout code (CSS + Tailwind)
Cyber-Rage Design Intelligence Engine

Usage: python layout_generator.py --grid 12 --gap 16
       python layout_generator.py --container lg
       python layout_generator.py --spacing
       python layout_generator.py --breakpoints
       python layout_generator.py --layout dashboard|landing|app|auth|blog
"""

import argparse
import json
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


CONTAINERS = {
    "sm": "640px",
    "md": "768px",
    "lg": "1024px",
    "xl": "1280px",
    "2xl": "1536px",
    "full": "100%",
}

BREAKPOINTS = {
    "sm": "640px",
    "md": "768px",
    "lg": "1024px",
    "xl": "1280px",
    "2xl": "1536px",
}

SPACING_SCALE = {
    "xs": "4px  / 0.25rem",
    "sm": "8px   / 0.5rem",
    "md": "16px  / 1rem",
    "lg": "24px  / 1.5rem",
    "xl": "32px  / 2rem",
    "2xl": "48px  / 3rem",
    "3xl": "64px  / 4rem",
    "4xl": "96px  / 6rem",
    "5xl": "128px / 8rem",
}


def generate_grid(columns=12, gap=16, max_width="1280px"):
    spans = "\n".join(f".col-{i} {{ grid-column: span {i}; }}" for i in range(1, columns + 1))
    span_helpers = ", ".join(f"col-span-{i}" for i in range(1, min(columns, 6) + 1))
    return f"""/* ===== Grid System: {columns} columns, {gap}px gap ===== */

.container {{
  max-width: {max_width};
  margin: 0 auto;
  padding: 0 {gap}px;
}}

.grid {{
  display: grid;
  grid-template-columns: repeat({columns}, 1fr);
  gap: {gap}px;
}}

/* Column spans */
{spans}

/* Responsive */
@media (max-width: 768px) {{
  .grid {{
    grid-template-columns: repeat(2, 1fr);
  }}
}}

@media (max-width: 375px) {{
  .grid {{
    grid-template-columns: 1fr;
  }}
}}

/* ===== Tailwind ===== */
<div class="grid grid-cols-{columns} gap-[{gap}px]">
  <!-- span helpers: {span_helpers} -->
</div>"""


def generate_container(level="lg"):
    if level not in CONTAINERS:
        return f"Unknown container: '{level}'. Available: {', '.join(CONTAINERS.keys())}"
    width = CONTAINERS[level]
    return f"""/* Container: {level} ({width}) */
.container {{
  max-width: {width};
  margin: 0 auto;
  padding: 0 1rem;
}}
.container-fluid {{
  width: 100%;
  padding: 0 1rem;
}}
/* Tailwind: max-w-{level} mx-auto px-4 */"""


def generate_spacing():
    lines = []
    lines.append("/* ===== Spacing Scale ===== */")
    lines.append(":root {")
    for name, value in SPACING_SCALE.items():
        px = value.split("/")[0].strip().replace("px", "")
        lines.append(f"  --space-{name}: {value.split('/')[0].strip()}; /* {value.split('/')[1].strip()} */")
    lines.append("}")
    lines.append("")
    lines.append("/* Usage examples:")
    lines.append("   padding: var(--space-md);   → 16px")
    lines.append("   margin-top: var(--space-xl); → 32px")
    lines.append("   Tailwind: p-4 m-8 px-2 gap-6")
    lines.append("*/")
    return "\n".join(lines)


def generate_breakpoints():
    lines = []
    lines.append("/* ===== Breakpoints ===== */")
    lines.append("/* Mobile-first (min-width) */")
    for name, width in BREAKPOINTS.items():
        lines.append(f"@media (min-width: {width}) {{ /* {name} */ }}")
    lines.append("")
    lines.append("/* Desktop-first (max-width) */")
    for name, width in reversed(list(BREAKPOINTS.items())):
        lines.append(f"@media (max-width: {width}) {{ /* {name} */ }}")
    lines.append("")
    lines.append("/* ===== Tailwind Breakpoints ===== */")
    lines.append("sm:   # 640px   → sm:text-lg")
    lines.append("md:   # 768px   → md:grid-cols-2")
    lines.append("lg:   # 1024px  → lg:flex")
    lines.append("xl:   # 1280px  → xl:max-w-7xl")
    lines.append("2xl:  # 1536px  → 2xl:gap-8")
    lines.append("")
    lines.append("/* ===== Device Widths ===== */")
    lines.append("375px  → iPhone SE / small mobile")
    lines.append("414px  → iPhone Plus")
    lines.append("768px  → iPad portrait")
    lines.append("1024px → iPad landscape / laptop small")
    lines.append("1440px → desktop")
    lines.append("1920px → full HD desktop")
    return "\n".join(lines)


def generate_layout(template="dashboard"):
    templates = {
        "dashboard": {
            "name": "Dashboard Layout",
            "css": """/* ===== Dashboard Layout ===== */
.layout {
  display: flex;
  min-height: 100vh;
}
.sidebar {
  width: 240px;
  flex-shrink: 0;
  background: #1E293B;
  color: #F8FAFC;
  padding: 24px 16px;
}
.main {
  flex: 1;
  padding: 24px;
  overflow-x: auto;
}
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 24px;
  background: #fff;
  border-bottom: 1px solid #E2E8F0;
  position: sticky;
  top: 0;
  z-index: 40;
}
.content-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 16px;
  padding: 24px;
}
.kpi-card { grid-column: span 3; }
.chart-card { grid-column: span 6; }
.table-card { grid-column: span 12; }

/* Responsive */
@media (max-width: 1024px) {
  .kpi-card { grid-column: span 6; }
  .chart-card { grid-column: span 12; }
}
@media (max-width: 768px) {
  .sidebar { display: none; }
  .kpi-card { grid-column: span 12; }
}""",
            "tailwind": """<!-- Dashboard Layout - Tailwind -->
<div class="flex min-h-screen">
  <aside class="hidden lg:block w-60 flex-shrink-0 bg-slate-800 text-slate-50 p-6">
    <!-- Sidebar content -->
  </aside>
  <main class="flex-1">
    <header class="sticky top-0 z-40 bg-white border-b border-slate-200 px-6 py-4 flex items-center justify-between">
      <!-- Topbar -->
    </header>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 p-6">
      <!-- KPI cards -->
    </div>
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 px-6">
      <!-- Charts -->
    </div>
  </main>
</div>"""
        },
        "landing": {
            "name": "Landing Page Layout",
            "css": """/* ===== Landing Page Layout ===== */
.nav {
  position: sticky;
  top: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 32px;
  background: rgba(255,255,255,0.9);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid #E2E8F0;
}
.hero {
  min-height: calc(100vh - 64px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 64px 24px;
}
.features {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  padding: 64px 32px;
  max-width: 1200px;
  margin: 0 auto;
}
.cta-section {
  text-align: center;
  padding: 96px 32px;
}
.footer {
  padding: 48px 32px;
  background: #F8FAFC;
  border-top: 1px solid #E2E8F0;
}
@media (max-width: 768px) {
  .features { grid-template-columns: 1fr; }
  .hero { padding: 48px 16px; }
}""",
            "tailwind": """<!-- Landing Page Layout - Tailwind -->
<nav class="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b border-slate-200 px-4 md:px-8 py-4 flex items-center justify-between">
  <!-- Nav -->
</nav>
<section class="min-h-screen flex flex-col items-center justify-center text-center px-4 md:px-8 py-16">
  <!-- Hero -->
</section>
<section class="grid grid-cols-1 md:grid-cols-3 gap-8 px-4 md:px-8 py-16 max-w-6xl mx-auto">
  <!-- Features -->
</section>
<section class="text-center px-4 py-24">
  <!-- CTA -->
</section>
<footer class="px-4 md:px-8 py-12 bg-slate-50 border-t border-slate-200">
  <!-- Footer -->
</footer>"""
        },
        "auth": {
            "name": "Auth / Login Layout",
            "css": """/* ===== Auth Layout ===== */
.auth-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: linear-gradient(135deg, #F8FAFC, #E2E8F0);
}
.auth-card {
  width: 100%;
  max-width: 420px;
  background: #fff;
  border-radius: 16px;
  padding: 40px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}
.auth-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.auth-field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
@media (max-width: 480px) {
  .auth-card { padding: 24px; }
}""",
            "tailwind": """<!-- Auth Layout - Tailwind -->
<div class="min-h-screen flex items-center justify-center px-4 bg-gradient-to-br from-slate-50 to-slate-200">
  <div class="w-full max-w-md bg-white rounded-2xl p-8 md:p-10 shadow-2xl">
    <form class="flex flex-col gap-4">
      <label class="flex flex-col gap-2">
        <span class="text-sm font-medium text-slate-700">Email</span>
        <input type="email" class="px-4 py-3 rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500" />
      </label>
      <button type="submit" class="px-6 py-3 rounded-lg bg-blue-600 text-white font-semibold hover:bg-blue-700 transition-colors cursor-pointer">
        Sign In
      </button>
    </form>
  </div>
</div>"""
        },
        "blog": {
            "name": "Blog / Article Layout",
            "css": """/* ===== Blog Layout ===== */
.blog-header {
  max-width: 800px;
  margin: 0 auto;
  padding: 48px 24px 24px;
}
.blog-content {
  max-width: 720px;
  margin: 0 auto;
  padding: 24px;
  line-height: 1.8;
  font-size: 17px;
}
.blog-sidebar {
  position: sticky;
  top: 24px;
  align-self: start;
}
.blog-grid {
  display: grid;
  grid-template-columns: 1fr 280px;
  gap: 48px;
  max-width: 1100px;
  margin: 0 auto;
  padding: 24px;
}
@media (max-width: 1024px) {
  .blog-grid { grid-template-columns: 1fr; }
}""",
            "tailwind": """<!-- Blog Layout - Tailwind -->
<div class="max-w-4xl mx-auto px-4 py-12">
  <article class="prose prose-slate max-w-none">
    <h1 class="text-4xl font-bold mb-6">Article Title</h1>
    <p class="text-slate-600 leading-relaxed text-lg">
      Article content...
    </p>
  </article>
</div>"""
        },
        "app": {
            "name": "Mobile App Layout",
            "css": """/* ===== Mobile App Layout ===== */
.app-shell {
  max-width: 480px;
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: #F8FAFC;
}
.app-header {
  position: sticky;
  top: 0;
  z-index: 40;
  background: #fff;
  padding: 16px;
  border-bottom: 1px solid #E2E8F0;
}
.app-content {
  flex: 1;
  padding: 16px;
  overflow-y: auto;
}
.app-tabbar {
  position: sticky;
  bottom: 0;
  display: flex;
  background: #fff;
  border-top: 1px solid #E2E8F0;
  padding: 8px 0;
}
.app-tab {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 8px;
  cursor: pointer;
  font-size: 11px;
  color: #64748B;
}
.app-tab.active { color: #2563EB; }""",
            "tailwind": """<!-- Mobile App Layout - Tailwind -->
<div class="max-w-[480px] mx-auto min-h-screen flex flex-col bg-slate-50">
  <header class="sticky top-0 z-40 bg-white p-4 border-b border-slate-200">
    <!-- Header -->
  </header>
  <main class="flex-1 p-4 overflow-y-auto">
    <!-- Content -->
  </main>
  <nav class="sticky bottom-0 bg-white border-t border-slate-200 py-2 flex">
    <button class="flex-1 flex flex-col items-center gap-1 py-2 text-xs text-slate-500 cursor-pointer">
      <!-- Tab 1 -->
    </button>
  </nav>
</div>"""
        }
    }

    if template not in templates:
        return f"Unknown layout: '{template}'. Available: {', '.join(templates.keys())}"

    data = templates[template]
    return f"/* ===== {data['name']} ===== */\n\n### CSS ###\n{data['css']}\n\n### Tailwind ###\n{data['tailwind']}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Layout Generator - Cyber-Rage")
    parser.add_argument("--grid", type=int, help="Grid columns count")
    parser.add_argument("--gap", type=int, default=16, help="Grid gap in px")
    parser.add_argument("--container", help="Container width (sm, md, lg, xl, 2xl, full)")
    parser.add_argument("--spacing", action="store_true", help="Show spacing scale")
    parser.add_argument("--breakpoints", action="store_true", help="Show breakpoints")
    parser.add_argument("--layout", help="Layout template (dashboard, landing, auth, blog, app)")

    args = parser.parse_args()

    if args.grid:
        print(generate_grid(args.grid, args.gap))
    elif args.container:
        print(generate_container(args.container))
    elif args.spacing:
        print(generate_spacing())
    elif args.breakpoints:
        print(generate_breakpoints())
    elif args.layout:
        print(generate_layout(args.layout))
    else:
        print("Specify one of: --grid, --container, --spacing, --breakpoints, --layout")
        print("Example: python layout_generator.py --layout dashboard")
