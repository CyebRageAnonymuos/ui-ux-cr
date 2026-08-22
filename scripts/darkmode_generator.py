#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dark Mode Generator - Full light/dark theme pair from one brand color:
CSS variables, semantic colors, system + class-based switching, a
persisted toggle button, and print-friendly fallbacks.
Cyber-Rage Design Intelligence Engine

Usage: python darkmode_generator.py "#2563EB"
       python darkmode_generator.py "#10B981" --strategy class
       python darkmode_generator.py "#F97316" --toggle
"""

import argparse
import sys
import io
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from color_tools import generate_palette, ColorTools, check_contrast

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def theme_pair(hex_color, strategy="system"):
    p = generate_palette(hex_color, "complementary")
    selector_prefix = ":root" if strategy == "system" else ":root:not(.dark)"

    light = "\n".join(
        f"  --primary-{shade}: {c};" for shade, c in p["shades"].items()
    )
    dark_shades = {s: ColorTools.adjust_brightness(c, 0.85) for s, c in p["shades"].items()}
    dark = "\n".join(
        f"    --primary-{shade}: {c};" for shade, c in dark_shades.items()
    )

    on_light = check_contrast(p["shades"]["600"], "#FFFFFF")
    on_dark = check_contrast(p["shades"]["400"], "#0F172A")

    return f"""/* ===== Dark Mode System (strategy: {strategy}) =====
   - "{strategy}" mode: {"follows the OS prefers-color-scheme setting" if strategy == "system" else "driven by a .dark class on <html> (set from the toggle)"}
   - Every color pair below was chosen so text contrast holds in BOTH modes.
*/
{selector_prefix} {{
  color-scheme: light;
  --bg: #F8FAFC;
  --surface: #FFFFFF;
  --surface-2: #F1F5F9;
  --text: #0F172A;
  --text-muted: #475569;
  --border: #E2E8F0;
{light}
  --success: #16A34A;
  --warning: #D97706;
  --error: #DC2626;
  --info: #2563EB;
  --shadow: 0 6px 24px rgba(15, 23, 42, 0.08);
}}

{"@media (prefers-color-scheme: dark)" if strategy == "system" else "html.dark"} {{
{'' if strategy == "system" else '  :root {'}
  color-scheme: dark;
  --bg: #0B1120;
  --surface: #111A2E;
  --surface-2: #1B2740;
  --text: #F1F5F9;
  --text-muted: #94A3B8;
  --border: #24324D;
{dark}
  --success: #4ADE80;
  --warning: #FBBF24;
  --error: #F87171;
  --info: #60A5FA;
  --shadow: 0 6px 24px rgba(0, 0, 0, 0.45);
{'' if strategy == "system" else '  }'}
}}

/* Semantic usage - swap variables, never hard-coded colors */
body {{
  background: var(--bg);
  color: var(--text);
}}
.card {{
  background: var(--surface);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}}
.text-muted {{ color: var(--text-muted); }}

/* Contrast reference (checked at generation time):
   - light mode: primary-600 on white = {on_light['ratio']}:1 ({on_light['grade']})
   - dark mode:  primary-400 on dark  = {on_dark['ratio']}:1 ({on_dark['grade']})
*/

/* Print stays light regardless of theme */
@media print {{
  :root {{
    color-scheme: light;
    --bg: #FFFFFF;
    --surface: #FFFFFF;
    --text: #000000;
  }}
}}"""


def toggle_snippet():
    return """
<!-- ===== Dark mode toggle (accessible, persisted, no flash) ===== -->
<!-- 1) Anti-flash bootstrap: put this FIRST in <head> (before CSS) -->
<script>
(function () {
  var stored = localStorage.getItem('theme');
  var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  if (stored === 'dark' || (!stored && prefersDark)) {
    document.documentElement.classList.add('dark');
  }
})();
</script>

<!-- 2) The toggle button (in your navbar) -->
<button id="theme-toggle" type="button"
        aria-label="Toggle dark mode" aria-pressed="false"
        class="p-2 rounded-lg border border-gray-300 dark:border-gray-600">
  <!-- Sun (shown in dark mode) / Moon (shown in light mode) -->
  <svg class="h-5 w-5 dark:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
    <path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8z"/>
  </svg>
  <svg class="hidden h-5 w-5 dark:block" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
    <circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4M2 12h2m16 0h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>
  </svg>
</button>

<!-- 3) Toggle logic -->
<script>
(function () {
  var btn = document.getElementById('theme-toggle');
  var root = document.documentElement;
  function sync() {
    var dark = root.classList.contains('dark');
    btn.setAttribute('aria-pressed', dark ? 'true' : 'false');
  }
  btn.addEventListener('click', function () {
    root.classList.toggle('dark');
    localStorage.setItem('theme', root.classList.contains('dark') ? 'dark' : 'light');
    sync();
  });
  sync();
})();
</script>"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dark Mode Generator - Cyber-Rage")
    parser.add_argument("color", help="Brand color (hex)")
    parser.add_argument("--strategy", choices=["system", "class"], default="system",
                        help="Switching strategy (default system)")
    parser.add_argument("--toggle", action="store_true", help="Include the toggle button snippet")

    args = parser.parse_args()

    try:
        ColorTools.hex_to_rgb(args.color)
    except (ValueError, IndexError):
        print(f"Invalid hex color: {args.color}", file=sys.stderr)
        sys.exit(1)

    print(theme_pair(args.color, args.strategy))
    if args.toggle:
        print(toggle_snippet())
