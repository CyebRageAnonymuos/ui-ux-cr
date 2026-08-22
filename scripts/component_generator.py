#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Component Generator - Generate ready-to-use UI components (HTML + Tailwind + CSS)
using the Cyber-Rage design database (products, colors, typography, styles)

Usage: python component_generator.py --list
       python component_generator.py --component navbar --product "SaaS (General)"
       python component_generator.py --component hero --product "Micro SaaS"
       python component_generator.py --component pricing --style Neumorphism
"""

import argparse
import csv
import os
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, os.pardir, "data")

COMPONENTS = [
    "navbar", "hero", "features", "pricing", "cta", "footer",
    "form", "card", "modal", "table", "sidebar", "dashboard",
]


def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def find_product(name):
    for row in load_csv("products.csv"):
        if name.strip().lower() in row["Product Type"].lower():
            return row
    return None


DEFAULT_COLORS_ROW = {
    "Product Type": "SaaS (General)",
    "Primary (Hex)": "#2563EB",
    "Secondary (Hex)": "#0EA5E9",
    "CTA (Hex)": "#F97316",
    "Background (Hex)": "#FFFFFF",
    "Text (Hex)": "#0F172A",
    "Border (Hex)": "#E2E8F0",
    "Notes": "default palette (no exact colors.csv match)",
}


def find_colors(product_type):
    """Look up the color row for a product, with graceful fallback.

    colors.csv does not contain a row for every product in products.csv
    (many niche products share palettes with their parent category, e.g.
    "Government/Public Service" -> "Government/Public"). Previously a
    missing row returned None and crashed every component that read
    colors["Primary (Hex)"]. Now: try the full name, then each
    "/"-separated prefix, then the general SaaS defaults.
    """
    candidates = [product_type.strip()]
    # "Government/Public Service" -> also try "Government/Public", "Government"
    parts = product_type.split("/")
    for i in range(len(parts) - 1, 0, -1):
        candidates.append("/".join(parts[:i]).strip())

    rows = load_csv("colors.csv")
    for candidate in candidates:
        for row in rows:
            if candidate.lower() in row["Product Type"].lower():
                return row
    return dict(DEFAULT_COLORS_ROW)


def available_product_names(limit=30):
    rows = load_csv("products.csv")
    names = [row["Product Type"] for row in rows]
    return names[:limit] + (["..."] if len(names) > limit else [])


def find_typography(product_type=None):
    rows = load_csv("typography.csv")
    if product_type:
        for row in rows:
            if product_type.strip().lower() in row["Best For"].lower():
                return row
    return rows[0] if rows else None


def resolve_product(args):
    product = args.product or "SaaS (General)"
    row = find_product(product)
    if row is None:
        names = ", ".join(available_product_names())
        return None, f"Unknown product. Available products: {names}"
    colors = find_colors(row["Product Type"])
    typo = find_typography(row["Product Type"]) or find_typography()
    return row, {"colors": colors, "typo": typo}


def css_vars(colors, typo):
    if not colors:
        return ""
    heading = typo["Heading Font"] if typo else "Inter"
    body = typo["Body Font"] if typo else "Inter"
    return f"""/* Design tokens: {colors['Product Type']} */
:root {{
  --primary: {colors['Primary (Hex)']};
  --secondary: {colors['Secondary (Hex)']};
  --cta: {colors['CTA (Hex)']};
  --bg: {colors['Background (Hex)']};
  --text: {colors['Text (Hex)']};
  --border: {colors['Border (Hex)']};
  --font-heading: '{heading}', sans-serif;
  --font-body: '{body}', sans-serif;
}}
body {{
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-body);
}}
h1, h2, h3, h4 {{ font-family: var(--font-heading); }}"""


def component_navbar(colors, typo):
    return """<!-- Navbar -->
<nav class="flex items-center justify-between px-6 py-4 bg-white shadow-sm sticky top-0 z-40">
  <div class="flex items-center gap-8">
    <span class="text-xl font-bold tracking-tight" style="color:var(--primary);font-family:var(--font-heading)">Brand</span>
    <div class="hidden md:flex gap-6 text-sm text-slate-600">
      <a href="#" class="hover:text-slate-900 transition-colors">Features</a>
      <a href="#" class="hover:text-slate-900 transition-colors">Pricing</a>
      <a href="#" class="hover:text-slate-900 transition-colors">Docs</a>
    </div>
  </div>
  <div class="flex items-center gap-3">
    <button class="px-4 py-2 text-sm text-slate-600 hover:text-slate-900">Sign in</button>
    <button class="px-4 py-2 text-sm font-semibold text-white rounded-lg hover:opacity-90 transition-opacity" style="background:var(--cta)">Get Started</button>
  </div>
</nav>
<button class="md:hidden fixed bottom-6 right-6 p-3 rounded-full text-white shadow-lg cursor-pointer" style="background:var(--primary)" aria-label="Open menu">☰</button>"""


def component_hero(colors, typo):
    return """<!-- Hero Section -->
<section class="relative overflow-hidden px-6 pt-24 pb-32 text-center" style="background:var(--bg)">
  <div class="absolute inset-0 opacity-10" style="background:radial-gradient(circle at 20% 30%, var(--primary) 0%, transparent 50%), radial-gradient(circle at 80% 70%, var(--cta) 0%, transparent 50%)"></div>
  <div class="relative max-w-3xl mx-auto">
    <span class="inline-block px-4 py-1.5 text-xs font-semibold rounded-full mb-6" style="background:var(--primary)1a;color:var(--primary)">New · v2.0 is here</span>
    <h1 class="text-4xl md:text-6xl font-bold tracking-tight mb-6" style="font-family:var(--font-heading)">
      Build something<br /><span style="color:var(--primary)">amazing</span> today
    </h1>
    <p class="text-lg text-slate-600 mb-10 max-w-xl mx-auto">
      The fastest way to ship your product. Simple, powerful, and loved by teams worldwide.
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="px-8 py-3.5 rounded-lg font-semibold text-white shadow-lg hover:opacity-90 transition-opacity" style="background:var(--cta)">Start Free Trial</button>
      <button class="px-8 py-3.5 rounded-lg font-semibold border-2 transition-colors" style="border-color:var(--primary);color:var(--primary)">Watch Demo</button>
    </div>
    <div class="mt-14 grid grid-cols-3 gap-6 text-sm text-slate-500">
      <div><strong class="block text-2xl text-slate-900" style="font-family:var(--font-heading)">10K+</strong>Active users</div>
      <div><strong class="block text-2xl text-slate-900" style="font-family:var(--font-heading)">4.9★</strong>Average rating</div>
      <div><strong class="block text-2xl text-slate-900" style="font-family:var(--font-heading)">99.9%</strong>Uptime</div>
    </div>
  </div>
</section>"""


def component_features(colors, typo):
    cards = [
        ("⚡", "Lightning Fast", "Built for performance. Pages load instantly on any device."),
        ("🔒", "Secure by Default", "Enterprise-grade security with end-to-end encryption."),
        ("📊", "Powerful Insights", "Real-time analytics that help you make smarter decisions."),
    ]
    rows = "".join(
        f"""      <div class="bg-white rounded-xl p-8 shadow-sm hover:shadow-md transition-shadow border border-slate-100">
        <div class="w-12 h-12 rounded-lg flex items-center justify-center text-2xl mb-4" style="background:var(--primary)1a">{e}</div>
        <h3 class="text-lg font-semibold mb-2" style="font-family:var(--font-heading)">{t}</h3>
        <p class="text-sm text-slate-600 leading-relaxed">{d}</p>
      </div>"""
        for e, t, d in cards
    )
    return f"""<!-- Features Section -->
<section class="px-6 py-24 bg-white">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="text-3xl md:text-4xl font-bold mb-4" style="font-family:var(--font-heading)">Everything you need</h2>
      <p class="text-slate-600 max-w-xl mx-auto">Powerful features designed to help you grow, without the complexity.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
{rows}
    </div>
  </div>
</section>"""


def component_pricing(colors, typo):
    return """<!-- Pricing Section -->
<section class="px-6 py-24" style="background:var(--bg)">
  <div class="max-w-5xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-16" style="font-family:var(--font-heading)">Simple pricing</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-white rounded-2xl p-8 border border-slate-100 shadow-sm">
        <h3 class="font-semibold mb-2">Starter</h3>
        <p class="text-3xl font-bold mb-6" style="font-family:var(--font-heading)">$0<span class="text-sm font-normal text-slate-500">/mo</span></p>
        <ul class="space-y-3 text-sm text-slate-600 mb-8">
          <li>✓ 1 project</li>
          <li>✓ Community support</li>
          <li>✓ 1 GB storage</li>
        </ul>
        <button class="w-full py-3 rounded-lg font-semibold border-2" style="border-color:var(--primary);color:var(--primary)">Get Started</button>
      </div>
      <div class="rounded-2xl p-8 text-white shadow-xl relative" style="background:var(--primary)">
        <span class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 text-xs font-bold rounded-full" style="background:var(--cta)">Popular</span>
        <h3 class="font-semibold mb-2">Pro</h3>
        <p class="text-3xl font-bold mb-6" style="font-family:var(--font-heading)">$29<span class="text-sm font-normal opacity-70">/mo</span></p>
        <ul class="space-y-3 text-sm opacity-90 mb-8">
          <li>✓ Unlimited projects</li>
          <li>✓ Priority support</li>
          <li>✓ 100 GB storage</li>
        </ul>
        <button class="w-full py-3 rounded-lg font-semibold" style="background:var(--cta)">Start Free Trial</button>
      </div>
      <div class="bg-white rounded-2xl p-8 border border-slate-100 shadow-sm">
        <h3 class="font-semibold mb-2">Team</h3>
        <p class="text-3xl font-bold mb-6" style="font-family:var(--font-heading)">$99<span class="text-sm font-normal text-slate-500">/mo</span></p>
        <ul class="space-y-3 text-sm text-slate-600 mb-8">
          <li>✓ Everything in Pro</li>
          <li>✓ 24/7 support</li>
          <li>✓ Unlimited storage</li>
        </ul>
        <button class="w-full py-3 rounded-lg font-semibold text-white hover:opacity-90" style="background:var(--cta)">Contact Sales</button>
      </div>
    </div>
  </div>
</section>"""


def component_cta(colors, typo):
    return """<!-- CTA Section -->
<section class="px-6 py-24">
  <div class="max-w-4xl mx-auto rounded-3xl px-8 py-16 text-center text-white relative overflow-hidden shadow-2xl" style="background:linear-gradient(135deg, var(--primary), var(--secondary))">
    <div class="absolute inset-0 opacity-20" style="background:radial-gradient(circle at 80% 20%, #fff 0%, transparent 40%)"></div>
    <h2 class="text-3xl md:text-4xl font-bold mb-4 relative" style="font-family:var(--font-heading)">Ready to get started?</h2>
    <p class="opacity-90 mb-8 max-w-md mx-auto relative">Join thousands of teams building better products with us.</p>
    <button class="px-10 py-4 rounded-lg font-semibold relative hover:opacity-90 transition-opacity cursor-pointer" style="background:var(--cta)">Get Started Now</button>
  </div>
</section>"""


def component_footer(colors, typo):
    return """<!-- Footer -->
<footer class="px-6 py-16 bg-slate-900 text-slate-400">
  <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8">
    <div>
      <span class="text-lg font-bold text-white mb-4 block" style="font-family:var(--font-heading)">Brand</span>
      <p class="text-sm">Building the future of design, one pixel at a time.</p>
    </div>
    <div>
      <h3 class="text-white font-semibold text-sm mb-4">Product</h3>
      <ul class="space-y-2 text-sm">
        <li><a href="#" class="hover:text-white transition-colors">Features</a></li>
        <li><a href="#" class="hover:text-white transition-colors">Pricing</a></li>
        <li><a href="#" class="hover:text-white transition-colors">Changelog</a></li>
      </ul>
    </div>
    <div>
      <h3 class="text-white font-semibold text-sm mb-4">Company</h3>
      <ul class="space-y-2 text-sm">
        <li><a href="#" class="hover:text-white transition-colors">About</a></li>
        <li><a href="#" class="hover:text-white transition-colors">Blog</a></li>
        <li><a href="#" class="hover:text-white transition-colors">Careers</a></li>
      </ul>
    </div>
    <div>
      <h3 class="text-white font-semibold text-sm mb-4">Legal</h3>
      <ul class="space-y-2 text-sm">
        <li><a href="#" class="hover:text-white transition-colors">Privacy</a></li>
        <li><a href="#" class="hover:text-white transition-colors">Terms</a></li>
      </ul>
    </div>
  </div>
  <div class="max-w-6xl mx-auto mt-12 pt-8 border-t border-slate-800 flex flex-col md:flex-row justify-between gap-4 text-xs">
    <span>© 2026 Brand. All rights reserved.</span>
    <span>Made with ❤ for the web</span>
  </div>
</footer>"""


def component_form(colors, typo):
    return """<!-- Contact Form -->
<section class="px-6 py-24 bg-white">
  <div class="max-w-lg mx-auto">
    <h2 class="text-3xl font-bold text-center mb-8" style="font-family:var(--font-heading)">Get in touch</h2>
    <form class="space-y-5">
      <div class="grid grid-cols-2 gap-4">
        <label class="block">
          <span class="text-sm font-medium text-slate-700 mb-1.5 block">First name</span>
          <input type="text" placeholder="Jane" class="w-full px-4 py-3 rounded-lg border transition-shadow focus:outline-none focus:ring-4" style="border-color:var(--border)" onfocus="this.style.boxShadow='0 0 0 3px var(--primary)33'" onblur="this.style.boxShadow='none'" />
        </label>
        <label class="block">
          <span class="text-sm font-medium text-slate-700 mb-1.5 block">Last name</span>
          <input type="text" placeholder="Doe" class="w-full px-4 py-3 rounded-lg border transition-shadow focus:outline-none focus:ring-4" style="border-color:var(--border)" onfocus="this.style.boxShadow='0 0 0 3px var(--primary)33'" onblur="this.style.boxShadow='none'" />
        </label>
      </div>
      <label class="block">
        <span class="text-sm font-medium text-slate-700 mb-1.5 block">Email</span>
        <input type="email" placeholder="jane@example.com" class="w-full px-4 py-3 rounded-lg border transition-shadow focus:outline-none focus:ring-4" style="border-color:var(--border)" onfocus="this.style.boxShadow='0 0 0 3px var(--primary)33'" onblur="this.style.boxShadow='none'" />
      </label>
      <label class="block">
        <span class="text-sm font-medium text-slate-700 mb-1.5 block">Message</span>
        <textarea rows="5" placeholder="Tell us what you need..." class="w-full px-4 py-3 rounded-lg border transition-shadow focus:outline-none focus:ring-4" style="border-color:var(--border)" onfocus="this.style.boxShadow='0 0 0 3px var(--primary)33'" onblur="this.style.boxShadow='none'"></textarea>
      </label>
      <button type="submit" class="w-full py-3.5 rounded-lg font-semibold text-white hover:opacity-90 transition-opacity cursor-pointer" style="background:var(--cta)">Send Message</button>
    </form>
  </div>
</section>"""


def component_card(colors, typo):
    return """<!-- Product Card -->
<div class="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-shadow border border-slate-100 max-w-sm">
  <div class="h-48 flex items-center justify-center" style="background:linear-gradient(135deg, var(--primary)22, var(--secondary)22)">
    <div class="w-16 h-16 rounded-2xl flex items-center justify-center text-white text-2xl" style="background:var(--primary)">🛒</div>
  </div>
  <div class="p-6">
    <div class="flex items-center justify-between mb-2">
      <span class="px-2.5 py-1 text-xs font-semibold rounded-full" style="background:var(--primary)1a;color:var(--primary)">New</span>
      <span class="text-sm text-slate-400">★ 4.9</span>
    </div>
    <h3 class="text-lg font-semibold mb-1" style="font-family:var(--font-heading)">Product Name</h3>
    <p class="text-sm text-slate-600 mb-4">Short description of the product goes here.</p>
    <div class="flex items-center justify-between">
      <span class="text-xl font-bold" style="font-family:var(--font-heading)">$49<span class="text-sm font-normal text-slate-400 line-through ml-1">$79</span></span>
      <button class="px-5 py-2.5 rounded-lg text-sm font-semibold text-white hover:opacity-90 transition-opacity cursor-pointer" style="background:var(--cta)">Add to Cart</button>
    </div>
  </div>
</div>"""


def component_modal(colors, typo):
    return """<!-- Modal -->
<div id="modal" class="fixed inset-0 z-50 hidden items-center justify-center p-4">
  <div class="absolute inset-0 bg-black/50 backdrop-blur-sm" onclick="document.getElementById('modal').classList.add('hidden');document.getElementById('modal').classList.remove('flex')"></div>
  <div class="relative bg-white rounded-2xl max-w-md w-full p-8 shadow-2xl">
    <button class="absolute top-4 right-4 w-8 h-8 rounded-full text-slate-400 hover:bg-slate-100 hover:text-slate-600 transition-colors cursor-pointer" onclick="document.getElementById('modal').classList.add('hidden');document.getElementById('modal').classList.remove('flex')">✕</button>
    <div class="w-14 h-14 rounded-xl flex items-center justify-center text-2xl mb-4" style="background:var(--primary)1a">🎉</div>
    <h3 class="text-xl font-bold mb-2" style="font-family:var(--font-heading)">Congratulations!</h3>
    <p class="text-sm text-slate-600 mb-6">Your account has been created successfully. Start exploring right away.</p>
    <div class="flex gap-3">
      <button class="flex-1 py-3 rounded-lg font-semibold text-white hover:opacity-90 transition-opacity cursor-pointer" style="background:var(--primary)">Continue</button>
      <button class="px-6 py-3 rounded-lg font-semibold text-slate-600 hover:bg-slate-100 transition-colors cursor-pointer">Cancel</button>
    </div>
  </div>
</div>
<button class="px-6 py-3 rounded-lg font-semibold text-white cursor-pointer" style="background:var(--primary)" onclick="document.getElementById('modal').classList.remove('hidden');document.getElementById('modal').classList.add('flex')">Open Modal</button>"""


def component_table(colors, typo):
    rows = "".join(
        f"""        <tr class="border-b border-slate-100 hover:bg-slate-50 transition-colors">
          <td class="px-6 py-4 text-sm font-medium">User {i}</td>
          <td class="px-6 py-4 text-sm text-slate-600">user{i}@example.com</td>
          <td class="px-6 py-4"><span class="px-2.5 py-1 text-xs font-semibold rounded-full" style="background:{s}1a;color:{s}">{st}</span></td>
          <td class="px-6 py-4 text-sm text-slate-500">Feb {i}, 2026</td>
          <td class="px-6 py-4 text-right">
            <button class="px-3 py-1.5 text-xs font-semibold rounded-md border transition-colors cursor-pointer" style="border-color:var(--border)" onmouseover="this.style.color='var(--primary)'" onmouseout="this.style.color=''">Edit</button>
          </td>
        </tr>"""
        for i, (s, st) in enumerate(
            [(colors["Primary (Hex)"], "Active"), ("#10B981", "Active"), ("#F59E0B", "Pending"), ("#EF4444", "Blocked"), ("#10B981", "Active")],
            start=1,
        )
    )
    return f"""<!-- Data Table -->
<div class="bg-white rounded-xl shadow-sm border border-slate-100 overflow-hidden">
  <div class="px-6 py-4 flex items-center justify-between border-b border-slate-100">
    <h3 class="font-semibold" style="font-family:var(--font-heading)">Users</h3>
    <button class="px-4 py-2 text-sm font-semibold text-white rounded-lg hover:opacity-90 cursor-pointer" style="background:var(--primary)">+ Add User</button>
  </div>
  <div class="overflow-x-auto">
    <table class="w-full text-left">
      <thead>
        <tr class="text-xs text-slate-500 uppercase tracking-wider">
          <th class="px-6 py-3">Name</th>
          <th class="px-6 py-3">Email</th>
          <th class="px-6 py-3">Status</th>
          <th class="px-6 py-3">Joined</th>
          <th class="px-6 py-3 text-right">Actions</th>
        </tr>
      </thead>
      <tbody>
{rows}
      </tbody>
    </table>
  </div>
</div>"""


def component_sidebar(colors, typo):
    items = [
        ("📊", "Dashboard", True),
        ("👥", "Users", False),
        ("🛍️", "Products", False),
        ("📦", "Orders", False),
        ("💬", "Messages", False),
        ("⚙️", "Settings", False),
    ]
    rows = "".join(
        f"""      <a href="#" class="flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm transition-colors {'text-white' if a else 'text-slate-400 hover:text-white hover:bg-slate-700/50'}" style="background:{'var(--primary)' if a else 'transparent'}">
        <span>{e}</span>{t}{'<span class="ml-auto text-xs px-2 py-0.5 rounded-full" style="background:var(--cta)">3</span>' if e == '💬' else ''}
      </a>"""
        for e, t, a in items
    )
    return f"""<!-- Sidebar -->
<div class="flex min-h-screen">
  <aside class="w-60 flex-shrink-0 bg-slate-900 p-4 flex flex-col gap-6">
    <div class="flex items-center gap-3 px-4 pt-2">
      <div class="w-8 h-8 rounded-lg flex items-center justify-center text-white text-sm font-bold" style="background:var(--primary)">C</div>
      <span class="text-white font-bold" style="font-family:var(--font-heading)">CyberUI</span>
    </div>
    <nav class="flex flex-col gap-1.5">
{rows}
    </nav>
    <div class="mt-auto p-3 rounded-xl bg-slate-800 flex items-center gap-3">
      <div class="w-9 h-9 rounded-full bg-slate-600 flex items-center justify-center text-sm text-white">JD</div>
      <div class="flex-1 min-w-0">
        <p class="text-sm text-white truncate">John Doe</p>
        <p class="text-xs text-slate-500">Admin</p>
      </div>
      <button class="text-slate-500 hover:text-white cursor-pointer">⚙</button>
    </div>
  </aside>
  <main class="flex-1 bg-slate-50 p-8">
    <h1 class="text-2xl font-bold mb-6" style="font-family:var(--font-heading)">Dashboard</h1>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="bg-white rounded-xl p-6 shadow-sm border border-slate-100">
        <p class="text-sm text-slate-500">Revenue</p>
        <p class="text-2xl font-bold mt-1" style="font-family:var(--font-heading)">$48,290</p>
        <span class="text-xs font-semibold text-emerald-500">↑ 12.5%</span>
      </div>
      <div class="bg-white rounded-xl p-6 shadow-sm border border-slate-100">
        <p class="text-sm text-slate-500">Users</p>
        <p class="text-2xl font-bold mt-1" style="font-family:var(--font-heading)">2,847</p>
        <span class="text-xs font-semibold text-emerald-500">↑ 8.2%</span>
      </div>
      <div class="bg-white rounded-xl p-6 shadow-sm border border-slate-100">
        <p class="text-sm text-slate-500">Orders</p>
        <p class="text-2xl font-bold mt-1" style="font-family:var(--font-heading)">1,204</p>
        <span class="text-xs font-semibold text-amber-500">↓ 2.1%</span>
      </div>
    </div>
  </main>
</div>"""


def component_dashboard(colors, typo):
    return component_sidebar(colors, typo) + "\n\n<!-- Dashboard main content above -->"


def build_full_html(component_html, css_block, title="Component Preview"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
{css_block}
  </style>
</head>
<body class="min-h-screen">
{component_html}
</body>
</html>"""


def find_style(name):
    for row in load_csv("styles.csv"):
        if name.strip().lower() in row.get("Style Category", "").lower():
            return row
    return None


def style_css_overrides(style_row):
    """Style-specific CSS tokens derived from the styles.csv row.

    Applies what the database actually knows about the style (primary
    colors, effects) on top of the product palette, so --style has a
    real, visible effect on the generated component's stylesheet.
    """
    if not style_row:
        return ""
    lines = [f"/* Style override: {style_row['Style Category']} ({style_row.get('Type', '')}) */"]
    if style_row.get("Primary Colors"):
        lines.append(f"/* Style palette hint: {style_row['Primary Colors']} */")
    if style_row.get("Effects & Animation"):
        effect = style_row["Effects & Animation"].split(";")[0].strip()
        if effect:
            lines.append(f"/* Signature effect: {effect} */")
            name_slug = style_row["Style Category"].lower().replace(" ", "-")
            lines.append(f".style-{name_slug} {{ /* {effect} */ }}")
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Component Generator - Cyber-Rage")
    parser.add_argument("--list", action="store_true", help="List available components")
    parser.add_argument("--component", help=f"Component type ({', '.join(COMPONENTS)})")
    parser.add_argument("--product", help="Product type from database (e.g. 'SaaS (General)')")
    parser.add_argument("--style", help="Style override from styles.csv (e.g. Neumorphism, Glassmorphism)")
    parser.add_argument("--full", action="store_true", help="Output full HTML page")

    args = parser.parse_args()

    if args.list:
        print("Available components:")
        for c in COMPONENTS:
            print(f"  - {c}")
        print("\nExample: python component_generator.py --component hero --product 'SaaS (General)'")
        sys.exit(0)

    if not args.component:
        print("Specify --component (see --list) and optionally --product")
        sys.exit(1)

    if args.component not in COMPONENTS:
        print(f"Unknown component: '{args.component}'. Available: {', '.join(COMPONENTS)}")
        sys.exit(1)

    product_row, assets = resolve_product(args)
    if product_row is None:
        print(assets)
        sys.exit(1)

    style_row = None
    if args.style:
        style_row = find_style(args.style)
        if style_row is None:
            style_names = ", ".join(
                row["Style Category"] for row in load_csv("styles.csv")
            )
            print(f"Unknown style: '{args.style}'. Available styles: {style_names}", file=sys.stderr)
            sys.exit(1)

    colors = assets["colors"]
    typo = assets["typo"]

    generator = globals()[f"component_{args.component}"]
    component_html = generator(colors, typo)
    css_block = css_vars(colors, typo)
    if style_row:
        css_block = css_block + "\n" + style_css_overrides(style_row)

    print(f"/* Product: {product_row['Product Type']} | Colors: {colors['Notes']} */")
    print(f"/* Typography: {typo['Font Pairing Name']} ({typo['Heading Font']} + {typo['Body Font']}) */")
    print(f"/* Primary: {colors['Primary (Hex)']} | CTA: {colors['CTA (Hex)']} | BG: {colors['Background (Hex)']} */")
    print()
    print(component_html)
    print()
    print("<!-- ===== Required CSS variables (paste into your stylesheet) ===== -->")
    print(css_block)

    if args.full:
        print()
        print("<!-- ===== Full HTML Preview ===== -->")
        print(build_full_html(component_html, css_block, f"{args.component} - {product_row['Product Type']}"))
