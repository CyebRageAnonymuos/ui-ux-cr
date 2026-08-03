<div align="center">

<!-- ==================== ANIMATED HERO BANNER ==================== -->
<svg viewBox="0 0 1000 340" xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" role="img" aria-label="UI UX CR - Cyber-Rage Design Intelligence Engine">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="50%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF006E"/>
      <stop offset="50%" stop-color="#F97316"/>
      <stop offset="100%" stop-color="#22D3EE"/>
      <animate attributeName="x1" values="0%;100%;0%" dur="6s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF006E"/>
      <stop offset="100%" stop-color="#22D3EE"/>
    </linearGradient>
    <radialGradient id="glow1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF006E" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#FF006E" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0"/>
    </radialGradient>
    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1000" height="340" rx="24" fill="url(#bgGrad)"/>

  <!-- Ambient glows -->
  <circle cx="150" cy="80" r="180" fill="url(#glow1)">
    <animate attributeName="r" values="160;200;160" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="850" cy="260" r="180" fill="url(#glow2)">
    <animate attributeName="r" values="200;160;200" dur="6s" repeatCount="indefinite"/>
  </circle>

  <!-- Grid pattern -->
  <g stroke="#334155" stroke-opacity="0.35" stroke-width="1">
    <path d="M0 60H1000 M0 120H1000 M0 180H1000 M0 240H1000 M0 300H1000" fill="none"/>
    <path d="M100 0V340 M200 0V340 M300 0V340 M400 0V340 M500 0V340 M600 0V340 M700 0V340 M800 0V340 M900 0V340" fill="none"/>
  </g>

  <!-- Floating particles -->
  <g fill="#22D3EE">
    <circle cx="120" cy="90" r="3">
      <animate attributeName="cy" values="90;60;90" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0.3;1" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="880" cy="70" r="3" fill="#FF006E">
      <animate attributeName="cy" values="70;100;70" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0.3;1" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="950" cy="200" r="2.5">
      <animate attributeName="cy" values="200;170;200" dur="3.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="60" cy="220" r="2.5" fill="#F97316">
      <animate attributeName="cy" values="220;250;220" dur="4.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="780" cy="290" r="2">
      <animate attributeName="cy" values="290;260;290" dur="3s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Rotating ring (design wheel) -->
  <g transform="translate(160 170)">
    <circle cx="0" cy="0" r="52" fill="none" stroke="#FF006E" stroke-opacity="0.5" stroke-width="3" stroke-dasharray="60 220">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="38" fill="none" stroke="#22D3EE" stroke-opacity="0.6" stroke-width="3" stroke-dasharray="40 199">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="18" fill="#F97316" fill-opacity="0.15" stroke="#F97316" stroke-width="2">
      <animate attributeName="r" values="16;20;16" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="6" fill="#F97316">
      <animate attributeName="r" values="5;8;5" dur="2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Main title -->
  <text x="500" y="140" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="86" font-weight="900" fill="url(#titleGrad)" filter="url(#softGlow)" letter-spacing="6">UI UX CR</text>

  <!-- Animated divider -->
  <rect x="330" y="170" width="340" height="4" rx="2" fill="url(#lineGrad)">
    <animate attributeName="width" values="0;340;0" dur="5s" repeatCount="indefinite"/>
  </rect>

  <!-- Subtitle -->
  <text x="500" y="205" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="24" fill="#94A3B8" letter-spacing="2">CYBER-RAGE DESIGN INTELLIGENCE ENGINE</text>

  <!-- Typing command -->
  <text x="500" y="255" text-anchor="middle" font-family="'Consolas', monospace" font-size="19" fill="#22D3EE">
    <tspan>$ python3 scripts/search.py "SaaS landing page" --design-system</tspan>
    <tspan fill="#FF006E">█</tspan>
    <animate attributeName="opacity" values="1;0.3;1" dur="1.2s" repeatCount="indefinite"/>
  </text>

  <!-- Badge chips -->
  <g font-family="'Segoe UI', Arial, sans-serif" font-size="15" font-weight="600">
    <rect x="210" y="285" width="150" height="34" rx="17" fill="#FF006E" fill-opacity="0.15" stroke="#FF006E" stroke-opacity="0.6">
      <animate attributeName="fill-opacity" values="0.15;0.3;0.15" dur="3s" repeatCount="indefinite"/>
    </rect>
    <text x="285" y="307" text-anchor="middle" fill="#FF87B7">17 Tools</text>

    <rect x="390" y="285" width="150" height="34" rx="17" fill="#F97316" fill-opacity="0.15" stroke="#F97316" stroke-opacity="0.6">
      <animate attributeName="fill-opacity" values="0.3;0.15;0.3" dur="3.2s" repeatCount="indefinite"/>
    </rect>
    <text x="465" y="307" text-anchor="middle" fill="#FDBA74">70+ Products</text>

    <rect x="570" y="285" width="150" height="34" rx="17" fill="#22D3EE" fill-opacity="0.15" stroke="#22D3EE" stroke-opacity="0.6">
      <animate attributeName="fill-opacity" values="0.15;0.3;0.15" dur="2.8s" repeatCount="indefinite"/>
    </rect>
    <text x="645" y="307" text-anchor="middle" fill="#67E8F9">100% Python</text>
  </g>
</svg>

<!-- ==================== BADGES ==================== -->
<p align="center">
  <a href="https://github.com/CyebRageAnonymuos/ui-ux-cr/releases"><img src="https://img.shields.io/badge/version-2.1.0-FF006E?style=for-the-badge" alt="Version"></a>
  <img src="https://img.shields.io/badge/python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/skill-17_tools-22D3EE?style=for-the-badge" alt="Tools">
  <img src="https://img.shields.io/badge/license-MIT-10B981?style=for-the-badge" alt="License">
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#the-toolbox">The Toolbox</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#domains">Domains</a> •
  <a href="#examples">Examples</a>
</p>

</div>

---

# 🔥 UI UX CR — Cyber-Rage Design Intelligence Engine

**UI UX CR** is an ultra-premium design intelligence system for AI assistants. It doesn't just *recommend* designs — it **generates** complete design systems, **builds** full HTML/Tailwind pages, **exports** themes, and **audits** accessibility, all from your terminal.

**v2.1 highlights:** 17 standalone toolbox scripts, full-page builder, palette & typography generators, favicon & pattern generators, UI copy generator, social media specs, ASCII mockups & banners, WCAG accessibility auditor.

---

## Features

| Feature | Description |
|---------|-------------|
| **Enhanced BM25 Search** | Fuzzy matching, n-gram detection, 120+ synonym groups |
| **Design System Generator** | 10 domains searched in parallel with reasoning engine |
| **Color Theory Engine** | Extended palettes, 6 harmony types, WCAG contrast, color-blind simulation |
| **17 Toolbox Scripts** | SVG icons, CSS kits, components, animations, charts, pages, mockups |
| **Component Generator** | 12 ready components (navbar, hero, pricing, modal, table, sidebar...) |
| **Page Builder** | Compose a full HTML landing page in one command |
| **Accessibility Auditor** | WCAG audit: contrast, alt text, labels, heading order |
| **Animation Database** | 30+ patterns + animation kit with reduced-motion fallback |
| **Design Tokens** | 70+ categories with CSS variables & Tailwind config |

---

## The Toolbox

<div align="center">

<!-- ==================== TOOLBOX SVG SHOWCASE ==================== -->
<svg viewBox="0 0 1000 240" xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" aria-label="Toolbox tools animation">
  <defs>
    <linearGradient id="tg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF006E"/>
      <stop offset="100%" stop-color="#22D3EE"/>
      <animate attributeName="x1" values="0%;100%;0%" dur="8s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>

  <text x="500" y="50" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="34" font-weight="800" fill="url(#tg)">17 TOOLBOX SCRIPTS</text>

  <!-- row 1: design tools -->
  <g font-family="'Consolas', monospace">
    <rect x="60" y="75" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#FF006E;#334155" dur="4s" repeatCount="indefinite"/></rect>
    <text x="125" y="102" text-anchor="middle" fill="#FDBA74" font-size="13">search.py</text>
    <rect x="205" y="75" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#22D3EE;#334155" dur="4.5s" repeatCount="indefinite"/></rect>
    <text x="270" y="102" text-anchor="middle" fill="#67E8F9" font-size="13">svg_gen.py</text>
    <rect x="350" y="75" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#10B981;#334155" dur="5s" repeatCount="indefinite"/></rect>
    <text x="415" y="102" text-anchor="middle" fill="#6EE7B7" font-size="13">css_gen.py</text>
    <rect x="495" y="75" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#F97316;#334155" dur="3.5s" repeatCount="indefinite"/></rect>
    <text x="560" y="102" text-anchor="middle" fill="#FDBA74" font-size="13">palette.py</text>
    <rect x="640" y="75" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#A78BFA;#334155" dur="4.2s" repeatCount="indefinite"/></rect>
    <text x="705" y="102" text-anchor="middle" fill="#C4B5FD" font-size="13">type_gen.py</text>
    <rect x="785" y="75" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#F472B6;#334155" dur="4.8s" repeatCount="indefinite"/></rect>
    <text x="850" y="102" text-anchor="middle" fill="#F9A8D4" font-size="13">theme_export</text>
  </g>

  <!-- row 2: build tools -->
  <g font-family="'Consolas', monospace">
    <rect x="60" y="135" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#22D3EE;#334155" dur="3.8s" repeatCount="indefinite"/></rect>
    <text x="125" y="162" text-anchor="middle" fill="#67E8F9" font-size="13">component.py</text>
    <rect x="205" y="135" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#FF006E;#334155" dur="4.6s" repeatCount="indefinite"/></rect>
    <text x="270" y="162" text-anchor="middle" fill="#FF87B7" font-size="13">page_builder</text>
    <rect x="350" y="135" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#F59E0B;#334155" dur="5.2s" repeatCount="indefinite"/></rect>
    <text x="415" y="162" text-anchor="middle" fill="#FCD34D" font-size="13">layout_gen</text>
    <rect x="495" y="135" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#10B981;#334155" dur="4.1s" repeatCount="indefinite"/></rect>
    <text x="560" y="162" text-anchor="middle" fill="#6EE7B7" font-size="13">anim_gen.py</text>
    <rect x="640" y="135" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#22D3EE;#334155" dur="5.5s" repeatCount="indefinite"/></rect>
    <text x="705" y="162" text-anchor="middle" fill="#67E8F9" font-size="13">chart_gen.py</text>
    <rect x="785" y="135" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#A78BFA;#334155" dur="3.6s" repeatCount="indefinite"/></rect>
    <text x="850" y="162" text-anchor="middle" fill="#C4B5FD" font-size="13">pattern_gen</text>
  </g>

  <!-- row 3: utility tools -->
  <g font-family="'Consolas', monospace">
    <rect x="60" y="195" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#F472B6;#334155" dur="4.9s" repeatCount="indefinite"/></rect>
    <text x="125" y="222" text-anchor="middle" fill="#F9A8D4" font-size="13">favicon.py</text>
    <rect x="205" y="195" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#10B981;#334155" dur="3.9s" repeatCount="indefinite"/></rect>
    <text x="270" y="222" text-anchor="middle" fill="#6EE7B7" font-size="13">copy_gen.py</text>
    <rect x="350" y="195" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#F59E0B;#334155" dur="4.4s" repeatCount="indefinite"/></rect>
    <text x="415" y="222" text-anchor="middle" fill="#FCD34D" font-size="13">a11y_audit</text>
    <rect x="495" y="195" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#FF006E;#334155" dur="5.8s" repeatCount="indefinite"/></rect>
    <text x="560" y="222" text-anchor="middle" fill="#FF87B7" font-size="13">mockup_gen</text>
    <rect x="640" y="195" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#22D3EE;#334155" dur="4.7s" repeatCount="indefinite"/></rect>
    <text x="705" y="222" text-anchor="middle" fill="#67E8F9" font-size="13">social_specs</text>
    <rect x="785" y="195" width="130" height="44" rx="10" fill="#1E293B" stroke="#334155"><animate attributeName="stroke" values="#334155;#A78BFA;#334155" dur="5.1s" repeatCount="indefinite"/></rect>
    <text x="850" y="222" text-anchor="middle" fill="#C4B5FD" font-size="13">banner_gen</text>
  </g>
</svg>

</div>

### The 17 Tools

| # | Script | What it does | Quick example |
|---|--------|--------------|---------------|
| 01 | `search.py` | BM25 design search across 10 domains | `python3 scripts/search.py "saas" --design-system` |
| 02 | `svg_generator.py` | 70+ SVG icons, 6 patterns, logos | `python3 scripts/svg_generator.py --icon search --size 24` |
| 03 | `css_generator.py` | Shadows, gradients, glass, glow, UI kit, neumorphism | `python3 scripts/css_generator.py --ui-kit --primary #2563EB` |
| 04 | `palette_generator.py` | Harmony palettes, shade scales, WCAG report | `python3 scripts/palette_generator.py "#2563EB" --harmony triadic --check-wcag` |
| 05 | `typography_generator.py` | Modular type scales + font pairings | `python3 scripts/typography_generator.py --scale golden-ratio` |
| 06 | `theme_exporter.py` | Export theme → CSS/Tailwind/SCSS/JSON | `python3 scripts/theme_exporter.py "#2563EB" --format all` |
| 07 | `component_generator.py` | 12 ready components from the database | `python3 scripts/component_generator.py --component navbar --product "SaaS (General)"` |
| 08 | `page_builder.py` | Compose a full HTML landing page | `python3 scripts/page_builder.py --sections navbar,hero,features,pricing,cta,footer --out landing.html` |
| 09 | `layout_generator.py` | Grids, containers, spacing, breakpoints, 5 templates | `python3 scripts/layout_generator.py --layout dashboard` |
| 10 | `animation_generator.py` | 12 animations with parameters + full kit | `python3 scripts/animation_generator.py --type bounce --duration 0.6` |
| 11 | `chart_generator.py` | Chart.js & Recharts configs (8 chart types) | `python3 scripts/chart_generator.py --chart bar --labels "Q1,Q2" --data "25,40"` |
| 12 | `pattern_generator.py` | 12 CSS background patterns | `python3 scripts/pattern_generator.py checkerboard --color #2563EB` |
| 13 | `favicon_generator.py` | Favicon SVG + HTML head + PWA manifest | `python3 scripts/favicon_generator.py --text CR --bg #2563EB` |
| 14 | `copy_generator.py` | Headlines, CTAs, placeholders, errors, A/B variants | `python3 scripts/copy_generator.py --headline saas --count 3` |
| 15 | `mockup_generator.py` | ASCII wireframes (desktop, mobile, dashboard, login) | `python3 scripts/mockup_generator.py --type dashboard` |
| 16 | `social_specs.py` | Social media dimension cheat sheets | `python3 scripts/social_specs.py --platform instagram` |
| 17 | `accessibility_audit.py` | WCAG audit of HTML (contrast, alt, labels) | `python3 scripts/accessibility_audit.py index.html` |

**Realistic workflow in 60 seconds:**

```bash
# 1. Build a full landing page for a Micro SaaS
python3 scripts/page_builder.py --product "Micro SaaS" --sections navbar,hero,features,pricing,cta,footer --out landing.html

# 2. Replace emoji placeholders with real SVG icons
python3 scripts/svg_generator.py --icon check --color "#10B981" --size 24

# 3. Add a complete animation kit
python3 scripts/animation_generator.py --kit

# 4. Audit the page for accessibility
python3 scripts/accessibility_audit.py landing.html
```

---

## Data Coverage v2.1

<div align="center">

<!-- ==================== ANIMATED DATA BARS ==================== -->
<svg viewBox="0 0 900 330" xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" aria-label="Data coverage chart">
  <defs>
    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF006E"/>
      <stop offset="100%" stop-color="#22D3EE"/>
    </linearGradient>
  </defs>

  <text x="450" y="40" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="30" font-weight="800" fill="#E2E8F0">DATA COVERAGE</text>

  <g font-family="'Segoe UI', Arial, sans-serif" font-size="15">
    <!-- Product Types: 70 -->
    <text x="30" y="82" fill="#94A3B8">Product Types</text>
    <rect x="220" y="70" width="560" height="20" rx="10" fill="#1E293B"/>
    <rect x="220" y="70" width="560" height="20" rx="10" fill="url(#barGrad)">
      <animate attributeName="width" values="0;560" dur="2s" fill="freeze"/>
    </rect>
    <text x="800" y="86" fill="#E2E8F0" font-weight="700">70+</text>

    <!-- Styles: 46 -->
    <text x="30" y="122" fill="#94A3B8">UI Styles</text>
    <rect x="220" y="110" width="560" height="20" rx="10" fill="#1E293B"/>
    <rect x="220" y="110" width="368" height="20" rx="10" fill="url(#barGrad)">
      <animate attributeName="width" values="0;368" dur="2s" begin="0.2s" fill="freeze"/>
    </rect>
    <text x="610" y="126" fill="#E2E8F0" font-weight="700">46+</text>

    <!-- Colors: 80 -->
    <text x="30" y="162" fill="#94A3B8">Color Palettes</text>
    <rect x="220" y="150" width="560" height="20" rx="10" fill="#1E293B"/>
    <rect x="220" y="150" width="560" height="20" rx="10" fill="url(#barGrad)">
      <animate attributeName="width" values="0;560" dur="2s" begin="0.4s" fill="freeze"/>
    </rect>
    <text x="800" y="166" fill="#E2E8F0" font-weight="700">80+</text>

    <!-- Fonts: 75 -->
    <text x="30" y="202" fill="#94A3B8">Font Pairings</text>
    <rect x="220" y="190" width="560" height="20" rx="10" fill="#1E293B"/>
    <rect x="220" y="190" width="525" height="20" rx="10" fill="url(#barGrad)">
      <animate attributeName="width" values="0;525" dur="2s" begin="0.6s" fill="freeze"/>
    </rect>
    <text x="765" y="206" fill="#E2E8F0" font-weight="700">75+</text>

    <!-- Synonyms: 120 -->
    <text x="30" y="242" fill="#94A3B8">Synonym Groups</text>
    <rect x="220" y="230" width="560" height="20" rx="10" fill="#1E293B"/>
    <rect x="220" y="230" width="560" height="20" rx="10" fill="url(#barGrad)">
      <animate attributeName="width" values="0;560" dur="2s" begin="0.8s" fill="freeze"/>
    </rect>
    <text x="800" y="246" fill="#E2E8F0" font-weight="700">120+</text>

    <!-- Tools: 17 -->
    <text x="30" y="282" fill="#94A3B8">Toolbox Scripts</text>
    <rect x="220" y="270" width="560" height="20" rx="10" fill="#1E293B"/>
    <rect x="220" y="270" width="136" height="20" rx="10" fill="#F97316">
      <animate attributeName="width" values="0;136" dur="2s" begin="1s" fill="freeze"/>
    </rect>
    <text x="375" y="286" fill="#E2E8F0" font-weight="700">17</text>
  </g>
</svg>

</div>

| Category | v1.x | v2.0 | v2.1 |
|----------|------|------|------|
| Product Types | 51 | 70+ | **70+** |
| UI Styles | 31 | 46+ | **46+** |
| Color Palettes | 61 | 80+ | **80+** |
| Font Pairings | 61 | 75+ | **75+** |
| Synonym Groups | 34 | 120+ | **120+** |
| Toolbox Scripts | ✗ | 9 | **17** |
| Components | — | — | **12 generated** |
| Layout Templates | — | — | **5** |
| Chart Types | — | — | **8 + 2 frameworks** |
| Background Patterns | — | — | **12 CSS** |
| SVG Icons | — | — | **70+** |
| WCAG Audit | ✗ | — | **Built-in tool** |

---

## Installation

### Option 1: Direct Copy

```bash
git clone https://github.com/CyebRageAnonymuos/ui-ux-cr.git
cp -r ui-ux-cr /path/to/your/project/
```

### Option 2: As an opencode / Claude skill

```bash
mkdir -p .opencode/skills/ui-ux-cr
cp -r ui-ux-cr/scripts .opencode/skills/ui-ux-cr/
cp -r ui-ux-cr/data .opencode/skills/ui-ux-cr/
cp ui-ux-cr/SKILL.md .opencode/skills/ui-ux-cr/
```

### Prerequisites

```bash
python3 --version
```

Not installed? `brew install python3` (macOS) · `sudo apt install python3` (Ubuntu) · `winget install Python.Python.3.12` (Windows)

---

## Usage

### Generate a Complete Design System (Primary Feature)

```bash
python3 scripts/search.py "SaaS landing page modern" --design-system -p "My SaaS"
```

**Output:** pattern, style, colors + extended palette, typography with Google Fonts links, effects, components with code, animations with CSS, responsive patterns, anti-patterns, pre-delivery checklist.

### Advanced Search Flags

```bash
# WCAG contrast analysis
python3 scripts/search.py "healthcare saas" --wcag

# Export CSS custom properties
python3 scripts/search.py "fintech dashboard" --export-css

# Export Tailwind config
python3 scripts/search.py "ecommerce luxury" --export-tailwind

# Extended color palette
python3 scripts/search.py "healthcare" --color-palette

# Multi-domain analysis
python3 scripts/search.py "modern dark" --multi-domains style,color,typography

# Save design system for reuse
python3 scripts/search.py "ecommerce" --design-system --persist -p "MyShop"
```

### Output Formats

```bash
python3 scripts/search.py "fintech" --design-system          # ASCII (terminal)
python3 scripts/search.py "fintech" --design-system -f markdown  # Docs
python3 scripts/search.py "glassmorphism" --domain style --json   # JSON
```

---

## Available Domains

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `style` | UI styles, colors, effects | glassmorphism, minimalism, dark mode |
| `color` | Color palettes by product | saas, ecommerce, healthcare |
| `typography` | Font pairings | elegant, playful, professional |
| `landing` | Page structure, CTA strategy | hero, testimonial, pricing |
| `chart` | Chart types & libraries | trend, comparison, funnel |
| `ux` | Best practices, anti-patterns | animation, accessibility, loading |
| `component` | Component recommendations | button, card, modal, form |
| `animation` | Animation patterns | hover, entrance, scroll |
| `responsive` | Responsive patterns | mobile-first, grid |
| `design_token` | Design tokens | color, spacing, shadow |
| `product` | Product types | SaaS, e-commerce |
| `icons` | Icon recommendations | lucide, heroicons |
| `react` | React/Next.js performance | memo, suspense, bundle |
| `web` | Web interface guidelines | aria, focus, keyboard |

## Available Stacks

`html-tailwind` (default) · `react` · `nextjs` · `vue` · `nuxtjs` · `svelte` · `swiftui` · `react-native` · `flutter` · `shadcn` · `jetpack-compose` · `angular` · `laravel` · `threejs` · `astro` · `nuxt-ui`

---

## Examples

### Example 1: SaaS Landing Page — built end to end

```bash
# Design system
python3 scripts/search.py "SaaS landing page modern" --design-system -p "My SaaS"

# Full page
python3 scripts/page_builder.py --product "SaaS (General)" --sections navbar,hero,features,pricing,cta,footer --out landing.html

# Custom CSS kit + icons
python3 scripts/css_generator.py --ui-kit --primary #2563EB --cta #F97316
python3 scripts/svg_generator.py --icon check --size 24
```

**Recommended:** Glassmorphism + Flat · Trust blue `#2563EB` + orange CTA `#F97316` · Poppins + Inter

### Example 2: Healthcare Dashboard

```bash
python3 scripts/search.py "healthcare dashboard" --design-system -p "Health App"
python3 scripts/layout_generator.py --layout dashboard
python3 scripts/chart_generator.py --chart line --labels "Mon,Tue,Wed,Thu,Fri" --data "120,180,150,220,190"
```

**Recommended:** Dark Mode (OLED) · `#0F172A` bg + health green `#22C55E` · Merriweather + Open Sans

### Example 3: E-commerce Store

```bash
python3 scripts/search.py "ecommerce luxury" --design-system -p "Luxury Shop"
python3 scripts/component_generator.py --component card --product "E-commerce"
python3 scripts/palette_generator.py "#1C1917" --harmony tetradic --check-wcag
```

**Recommended:** Liquid Glass + Glassmorphism · Premium dark + gold `#CA8A04` · Cormorant Garamond + Montserrat

---

## Pre-Delivery Checklist

- [ ] No emojis as icons — use `svg_generator.py`
- [ ] `cursor-pointer` on all clickable elements
- [ ] Hover states 150-300ms, no layout shift
- [ ] Contrast 4.5:1 minimum — verify with `accessibility_audit.py`
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] `prefers-reduced-motion` respected
- [ ] Responsive at 375 / 768 / 1024 / 1440px
- [ ] Loading, error, and empty states designed
- [ ] Dark mode tested

---

## Contributing

1. Fork the repository
2. Create your branch: `git checkout -b feature/AmazingFeature`
3. Commit: `git commit -m 'Add some AmazingFeature'`
4. Push and open a Pull Request

---

## License

MIT — see [LICENSE](LICENSE).

---

<div align="center">

<svg viewBox="0 0 600 80" xmlns="http://www.w3.org/2000/svg" width="100%" height="auto">
  <defs>
    <linearGradient id="footGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF006E"/>
      <stop offset="100%" stop-color="#22D3EE"/>
    </linearGradient>
  </defs>
  <text x="300" y="42" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="22" font-weight="800" fill="url(#footGrad)">Built with passion by Cyber-Rage</text>
  <text x="300" y="66" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-size="14" fill="#64748B">Making AI-powered design accessible to everyone</text>
  <rect x="230" y="20" width="140" height="2" rx="1" fill="url(#footGrad)">
    <animate attributeName="width" values="140;40;140" dur="3s" repeatCount="indefinite"/>
  </rect>
</svg>

**GitHub:** [CyebRageAnonymuos/ui-ux-cr](https://github.com/CyebRageAnonymuos/ui-ux-cr)

</div>
