<div align="center">

<!-- ═══════════════════════════════════════════════════════════════
     HERO — CYBER-RAGE ENGINE CORE
═══════════════════════════════════════════════════════════════ -->
<svg viewBox="0 0 1100 380" xmlns="http://www.w3.org/2000/svg" width="100%" role="img" aria-label="UI UX CR — Cyber-Rage Design Intelligence Engine">
  <defs>
    <!-- Background -->
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="40%" stop-color="#0F172A"/>
      <stop offset="70%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>

    <!-- Animated title gradient -->
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF006E"/>
      <stop offset="35%" stop-color="#F97316"/>
      <stop offset="70%" stop-color="#22D3EE"/>
      <stop offset="100%" stop-color="#A78BFA"/>
      <animate attributeName="x1" values="0%;100%;0%" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="100%;200%;100%" dur="7s" repeatCount="indefinite"/>
    </linearGradient>

    <!-- Scan-line gradient -->
    <linearGradient id="scanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0"/>
      <stop offset="50%" stop-color="#22D3EE" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0"/>
    </linearGradient>

    <!-- Glow filters -->
    <filter id="softGlow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="hardGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Radial glows -->
    <radialGradient id="pinkGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF006E" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#FF006E" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="cyanGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="orangeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#F97316" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#F97316" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Base -->
  <rect width="1100" height="380" rx="28" fill="url(#heroBg)"/>

  <!-- Ambient orbs -->
  <circle cx="120" cy="90" r="160" fill="url(#pinkGlow)">
    <animate attributeName="r" values="140;180;140" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.8;1;0.8" dur="6s" repeatCount="indefinite"/>
  </circle>
  <circle cx="980" cy="290" r="170" fill="url(#cyanGlow)">
    <animate attributeName="r" values="190;150;190" dur="7s" repeatCount="indefinite"/>
  </circle>
  <circle cx="550" cy="60" r="100" fill="url(#orangeGlow)">
    <animate attributeName="r" values="90;120;90" dur="5s" repeatCount="indefinite"/>
  </circle>

  <!-- Subtle grid -->
  <g stroke="#334155" stroke-opacity="0.25" stroke-width="0.8">
    <path d="M0 50H1100 M0 100H1100 M0 150H1100 M0 200H1100 M0 250H1100 M0 300H1100 M0 350H1100"/>
    <path d="M80 0V380 M160 0V380 M240 0V380 M320 0V380 M400 0V380 M480 0V380 M560 0V380 M640 0V380 M720 0V380 M800 0V380 M880 0V380 M960 0V380 M1040 0V380"/>
  </g>

  <!-- Scanning beam -->
  <rect x="0" y="0" width="1100" height="40" fill="url(#scanGrad)">
    <animate attributeName="y" values="-40;380;-40" dur="8s" repeatCount="indefinite"/>
  </rect>

  <!-- Floating particles -->
  <g>
    <circle cx="90" cy="70" r="2.5" fill="#22D3EE">
      <animate attributeName="cy" values="70;40;70" dur="3.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0.2;1" dur="3.2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1010" cy="60" r="3" fill="#FF006E">
      <animate attributeName="cy" values="60;95;60" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.9;0.3;0.9" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="200" cy="310" r="2" fill="#F97316">
      <animate attributeName="cy" values="310;280;310" dur="3.8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="920" cy="320" r="2.5" fill="#A78BFA">
      <animate attributeName="cy" values="320;290;320" dur="4.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="480" cy="40" r="2" fill="#22D3EE">
      <animate attributeName="cx" values="480;520;480" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="750" cy="340" r="1.8" fill="#FF006E">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2.5s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Left rotating design core -->
  <g transform="translate(150 190)">
    <circle r="62" fill="none" stroke="#FF006E" stroke-opacity="0.35" stroke-width="2" stroke-dasharray="30 160">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite"/>
    </circle>
    <circle r="48" fill="none" stroke="#22D3EE" stroke-opacity="0.45" stroke-width="2.5" stroke-dasharray="40 140">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="9s" repeatCount="indefinite"/>
    </circle>
    <circle r="34" fill="none" stroke="#F97316" stroke-opacity="0.5" stroke-width="2" stroke-dasharray="25 100">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle r="16" fill="#F97316" fill-opacity="0.18" stroke="#F97316" stroke-width="1.5">
      <animate attributeName="r" values="14;18;14" dur="2.2s" repeatCount="indefinite"/>
    </circle>
    <circle r="5" fill="#F97316">
      <animate attributeName="r" values="4;7;4" dur="2.2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Right rotating core (mirrored) -->
  <g transform="translate(950 190)">
    <circle r="55" fill="none" stroke="#22D3EE" stroke-opacity="0.35" stroke-width="2" stroke-dasharray="25 150">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="11s" repeatCount="indefinite"/>
    </circle>
    <circle r="40" fill="none" stroke="#A78BFA" stroke-opacity="0.45" stroke-width="2" stroke-dasharray="35 120">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="8s" repeatCount="indefinite"/>
    </circle>
    <circle r="14" fill="#22D3EE" fill-opacity="0.15" stroke="#22D3EE" stroke-width="1.5">
      <animate attributeName="r" values="12;16;12" dur="2.5s" repeatCount="indefinite"/>
    </circle>
    <circle r="4.5" fill="#22D3EE"/>
  </g>

  <!-- Main Title -->
  <text x="550" y="145" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="92" font-weight="900" fill="url(#titleGrad)" filter="url(#softGlow)" letter-spacing="8">UI UX CR</text>

  <!-- Animated underline -->
  <rect x="340" y="175" width="420" height="4" rx="2" fill="url(#titleGrad)">
    <animate attributeName="width" values="80;420;80" dur="4.5s" repeatCount="indefinite"/>
    <animate attributeName="x" values="510;340;510" dur="4.5s" repeatCount="indefinite"/>
  </rect>

  <!-- Subtitle -->
  <text x="550" y="215" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="22" fill="#94A3B8" letter-spacing="4" font-weight="500">CYBER-RAGE DESIGN INTELLIGENCE ENGINE</text>

  <!-- Terminal command with blinking cursor -->
  <g font-family="'JetBrains Mono', 'Consolas', monospace" font-size="17">
    <text x="550" y="265" text-anchor="middle" fill="#22D3EE">
      <tspan fill="#64748B">$</tspan>
      <tspan> python3 scripts/search.py </tspan>
      <tspan fill="#FDBA74">"SaaS landing page"</tspan>
      <tspan> --design-system</tspan>
      <tspan fill="#FF006E">
        <animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/>█
      </tspan>
    </text>
  </g>

  <!-- Live badges -->
  <g font-family="'Segoe UI', system-ui, sans-serif" font-size="14" font-weight="700">
    <!-- 17 Tools -->
    <rect x="250" y="300" width="140" height="36" rx="18" fill="#FF006E" fill-opacity="0.12" stroke="#FF006E" stroke-opacity="0.55" stroke-width="1.5">
      <animate attributeName="fill-opacity" values="0.12;0.28;0.12" dur="3s" repeatCount="indefinite"/>
    </rect>
    <text x="320" y="323" text-anchor="middle" fill="#FF87B7">17 Tools</text>

    <!-- 70+ Products -->
    <rect x="410" y="300" width="150" height="36" rx="18" fill="#F97316" fill-opacity="0.12" stroke="#F97316" stroke-opacity="0.55" stroke-width="1.5">
      <animate attributeName="fill-opacity" values="0.28;0.12;0.28" dur="3.4s" repeatCount="indefinite"/>
    </rect>
    <text x="485" y="323" text-anchor="middle" fill="#FDBA74">70+ Products</text>

    <!-- 100% Python -->
    <rect x="580" y="300" width="150" height="36" rx="18" fill="#22D3EE" fill-opacity="0.12" stroke="#22D3EE" stroke-opacity="0.55" stroke-width="1.5">
      <animate attributeName="fill-opacity" values="0.12;0.28;0.12" dur="2.9s" repeatCount="indefinite"/>
    </rect>
    <text x="655" y="323" text-anchor="middle" fill="#67E8F9">100% Python</text>

    <!-- MIT -->
    <rect x="750" y="300" width="100" height="36" rx="18" fill="#10B981" fill-opacity="0.12" stroke="#10B981" stroke-opacity="0.55" stroke-width="1.5">
      <animate attributeName="fill-opacity" values="0.2;0.12;0.2" dur="3.6s" repeatCount="indefinite"/>
    </rect>
    <text x="800" y="323" text-anchor="middle" fill="#6EE7B7">MIT</text>
  </g>
</svg>

<br/>

<!-- ═══════════════════════════════════════════════════════════════
     BADGES
═══════════════════════════════════════════════════════════════ -->
<p>
  <img src="https://img.shields.io/badge/version-2.1.0-FF006E?style=for-the-badge&labelColor=0F172A" alt="Version"/>
  <img src="https://img.shields.io/badge/python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0F172A" alt="Python"/>
  <img src="https://img.shields.io/badge/tools-17_scripts-22D3EE?style=for-the-badge&labelColor=0F172A" alt="Tools"/>
  <img src="https://img.shields.io/badge/license-MIT-10B981?style=for-the-badge&labelColor=0F172A" alt="License"/>
  <img src="https://img.shields.io/badge/style-cyber--rage-A78BFA?style=for-the-badge&labelColor=0F172A" alt="Style"/>
</p>

<p>
  <a href="#-features">Features</a> ·
  <a href="#-the-toolbox">Toolbox</a> ·
  <a href="#-data-coverage">Coverage</a> ·
  <a href="#-installation">Install</a> ·
  <a href="#-usage">Usage</a> ·
  <a href="#-examples">Examples</a> ·
  <a href="#-pre-delivery-checklist">Checklist</a>
</p>

</div>

---

# 🔥 UI UX CR — Cyber-Rage Design Intelligence Engine

> **Not just recommendations. Generation.**

**UI UX CR** is an ultra-premium design intelligence system built for AI assistants and power users.  
It **generates** complete design systems, **builds** full HTML/Tailwind pages, **exports** production-ready themes, and **audits** accessibility — all from your terminal.

**v2.1** ships with **17 standalone toolbox scripts**, a full-page builder, palette & typography engines, favicon/pattern generators, UI copy generator, social specs, ASCII mockups, banners, and a real WCAG accessibility auditor.

---

## ✨ Features

| Feature | What it actually does |
|---------|-----------------------|
| **Enhanced BM25 Search** | Fuzzy matching + n-grams + 120+ synonym groups |
| **Design System Generator** | 10 domains searched in parallel with reasoning engine |
| **Color Theory Engine** | 6 harmony types · WCAG contrast · color-blind simulation |
| **17 Toolbox Scripts** | Icons, CSS kits, components, animations, charts, pages… |
| **Component Generator** | 12 production-ready components (navbar, hero, pricing…) |
| **Page Builder** | Full HTML landing page in a single command |
| **Accessibility Auditor** | Real WCAG checks: contrast, alt, labels, heading order |
| **Animation Database** | 30+ patterns + full kit with `prefers-reduced-motion` |
| **Design Tokens** | 70+ categories → CSS variables & Tailwind config |

---

## 🧰 The Toolbox

<div align="center">

<svg viewBox="0 0 1050 270" xmlns="http://www.w3.org/2000/svg" width="100%" aria-label="17 Toolbox Scripts">
  <defs>
    <linearGradient id="toolTitle" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF006E"/>
      <stop offset="50%" stop-color="#F97316"/>
      <stop offset="100%" stop-color="#22D3EE"/>
      <animate attributeName="x1" values="0%;100%;0%" dur="9s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>

  <text x="525" y="42" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="32" font-weight="800" fill="url(#toolTitle)">17 TOOLBOX SCRIPTS</text>

  <!-- Row 1 -->
  <g font-family="'JetBrains Mono', Consolas, monospace" font-size="12.5">
    <rect x="30" y="70" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#FF006E;#334155" dur="4s" repeatCount="indefinite"/>
    </rect>
    <text x="102" y="96" text-anchor="middle" fill="#FDBA74">search.py</text>

    <rect x="190" y="70" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#22D3EE;#334155" dur="4.4s" repeatCount="indefinite"/>
    </rect>
    <text x="262" y="96" text-anchor="middle" fill="#67E8F9">svg_generator</text>

    <rect x="350" y="70" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#10B981;#334155" dur="5s" repeatCount="indefinite"/>
    </rect>
    <text x="422" y="96" text-anchor="middle" fill="#6EE7B7">css_generator</text>

    <rect x="510" y="70" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#F97316;#334155" dur="3.7s" repeatCount="indefinite"/>
    </rect>
    <text x="582" y="96" text-anchor="middle" fill="#FDBA74">palette_gen</text>

    <rect x="670" y="70" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#A78BFA;#334155" dur="4.8s" repeatCount="indefinite"/>
    </rect>
    <text x="742" y="96" text-anchor="middle" fill="#C4B5FD">type_gen</text>

    <rect x="830" y="70" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#F472B6;#334155" dur="4.2s" repeatCount="indefinite"/>
    </rect>
    <text x="902" y="96" text-anchor="middle" fill="#F9A8D4">theme_export</text>
  </g>

  <!-- Row 2 -->
  <g font-family="'JetBrains Mono', Consolas, monospace" font-size="12.5">
    <rect x="30" y="130" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#22D3EE;#334155" dur="3.9s" repeatCount="indefinite"/>
    </rect>
    <text x="102" y="156" text-anchor="middle" fill="#67E8F9">component</text>

    <rect x="190" y="130" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#FF006E;#334155" dur="4.6s" repeatCount="indefinite"/>
    </rect>
    <text x="262" y="156" text-anchor="middle" fill="#FF87B7">page_builder</text>

    <rect x="350" y="130" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#F59E0B;#334155" dur="5.1s" repeatCount="indefinite"/>
    </rect>
    <text x="422" y="156" text-anchor="middle" fill="#FCD34D">layout_gen</text>

    <rect x="510" y="130" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#10B981;#334155" dur="4s" repeatCount="indefinite"/>
    </rect>
    <text x="582" y="156" text-anchor="middle" fill="#6EE7B7">anim_gen</text>

    <rect x="670" y="130" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#22D3EE;#334155" dur="5.3s" repeatCount="indefinite"/>
    </rect>
    <text x="742" y="156" text-anchor="middle" fill="#67E8F9">chart_gen</text>

    <rect x="830" y="130" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#A78BFA;#334155" dur="3.5s" repeatCount="indefinite"/>
    </rect>
    <text x="902" y="156" text-anchor="middle" fill="#C4B5FD">pattern_gen</text>
  </g>

  <!-- Row 3 -->
  <g font-family="'JetBrains Mono', Consolas, monospace" font-size="12.5">
    <rect x="30" y="190" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#F472B6;#334155" dur="4.7s" repeatCount="indefinite"/>
    </rect>
    <text x="102" y="216" text-anchor="middle" fill="#F9A8D4">favicon</text>

    <rect x="190" y="190" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#10B981;#334155" dur="3.8s" repeatCount="indefinite"/>
    </rect>
    <text x="262" y="216" text-anchor="middle" fill="#6EE7B7">copy_gen</text>

    <rect x="350" y="190" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#FF006E;#334155" dur="5s" repeatCount="indefinite"/>
    </rect>
    <text x="422" y="216" text-anchor="middle" fill="#FF87B7">a11y_audit</text>

    <rect x="510" y="190" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#F97316;#334155" dur="4.3s" repeatCount="indefinite"/>
    </rect>
    <text x="582" y="216" text-anchor="middle" fill="#FDBA74">mockup_gen</text>

    <rect x="670" y="190" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#22D3EE;#334155" dur="3.6s" repeatCount="indefinite"/>
    </rect>
    <text x="742" y="216" text-anchor="middle" fill="#67E8F9">social_specs</text>

    <rect x="830" y="190" width="145" height="42" rx="10" fill="#0F172A" stroke="#334155" stroke-width="1.5">
      <animate attributeName="stroke" values="#334155;#A78BFA;#334155" dur="4.9s" repeatCount="indefinite"/>
    </rect>
    <text x="902" y="216" text-anchor="middle" fill="#C4B5FD">banner_gen</text>
  </g>
</svg>

</div>

### The 17 Tools

| # | Script | Purpose | Quick Example |
|---|--------|---------|---------------|
| 01 | `search.py` | BM25 design search across 10 domains | `python3 scripts/search.py "saas" --design-system` |
| 02 | `svg_generator.py` | 70+ SVG icons, patterns, logos | `python3 scripts/svg_generator.py --icon search --size 24` |
| 03 | `css_generator.py` | Shadows, gradients, glass, glow, neumorphism, UI kit | `python3 scripts/css_generator.py --ui-kit --primary #2563EB` |
| 04 | `palette_generator.py` | Harmony palettes + shade scales + WCAG report | `python3 scripts/palette_generator.py "#2563EB" --harmony triadic --check-wcag` |
| 05 | `typography_generator.py` | Modular type scales + font pairings | `python3 scripts/typography_generator.py --scale golden-ratio` |
| 06 | `theme_exporter.py` | Export → CSS / Tailwind / SCSS / JSON | `python3 scripts/theme_exporter.py "#2563EB" --format all` |
| 07 | `component_generator.py` | 12 ready components from the database | `python3 scripts/component_generator.py --component navbar --product "SaaS (General)"` |
| 08 | `page_builder.py` | Compose a full HTML landing page | `python3 scripts/page_builder.py --sections navbar,hero,features,pricing,cta,footer --out landing.html` |
| 09 | `layout_generator.py` | Grids, containers, spacing, 5 templates | `python3 scripts/layout_generator.py --layout dashboard` |
| 10 | `animation_generator.py` | 12 animations + full kit | `python3 scripts/animation_generator.py --type bounce --duration 0.6` |
| 11 | `chart_generator.py` | Chart.js & Recharts configs (8 types) | `python3 scripts/chart_generator.py --chart bar --labels "Q1,Q2" --data "25,40"` |
| 12 | `pattern_generator.py` | 12 CSS background patterns | `python3 scripts/pattern_generator.py checkerboard --color #2563EB` |
| 13 | `favicon_generator.py` | Favicon SVG + HTML head + PWA manifest | `python3 scripts/favicon_generator.py --text CR --bg #2563EB` |
| 14 | `copy_generator.py` | Headlines, CTAs, placeholders, A/B variants | `python3 scripts/copy_generator.py --headline saas --count 3` |
| 15 | `mockup_generator.py` | ASCII wireframes (desktop / mobile / dashboard) | `python3 scripts/mockup_generator.py --type dashboard` |
| 16 | `social_specs.py` | Social media dimension cheat sheets | `python3 scripts/social_specs.py --platform instagram` |
| 17 | `accessibility_audit.py` | WCAG audit of HTML | `python3 scripts/accessibility_audit.py index.html` |

**60-second realistic workflow:**

```bash
# 1. Full landing page
python3 scripts/page_builder.py --product "Micro SaaS" --sections navbar,hero,features,pricing,cta,footer --out landing.html

# 2. Real SVG icons instead of emoji
python3 scripts/svg_generator.py --icon check --color "#10B981" --size 24

# 3. Complete animation kit
python3 scripts/animation_generator.py --kit

# 4. Accessibility audit
python3 scripts/accessibility_audit.py landing.html
```

---

## 📊 Data Coverage

<div align="center">

<svg viewBox="0 0 900 320" xmlns="http://www.w3.org/2000/svg" width="100%" aria-label="Data Coverage Bars">
  <defs>
    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF006E"/>
      <stop offset="50%" stop-color="#F97316"/>
      <stop offset="100%" stop-color="#22D3EE"/>
    </linearGradient>
  </defs>

  <text x="450" y="36" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="26" font-weight="800" fill="#E2E8F0">DATA COVERAGE v2.1</text>

  <!-- Product Types -->
  <text x="30" y="80" fill="#94A3B8" font-family="system-ui" font-size="15">Product Types</text>
  <rect x="210" y="65" width="560" height="22" rx="11" fill="#1E293B"/>
  <rect x="210" y="65" width="560" height="22" rx="11" fill="url(#barGrad)">
    <animate attributeName="width" values="0;560" dur="1.8s" fill="freeze"/>
  </rect>
  <text x="790" y="81" fill="#E2E8F0" font-weight="700" font-size="14">70+</text>

  <!-- UI Styles -->
  <text x="30" y="120" fill="#94A3B8" font-family="system-ui" font-size="15">UI Styles</text>
  <rect x="210" y="105" width="560" height="22" rx="11" fill="#1E293B"/>
  <rect x="210" y="105" width="368" height="22" rx="11" fill="url(#barGrad)">
    <animate attributeName="width" values="0;368" dur="1.8s" begin="0.2s" fill="freeze"/>
  </rect>
  <text x="600" y="121" fill="#E2E8F0" font-weight="700" font-size="14">46+</text>

  <!-- Color Palettes -->
  <text x="30" y="160" fill="#94A3B8" font-family="system-ui" font-size="15">Color Palettes</text>
  <rect x="210" y="145" width="560" height="22" rx="11" fill="#1E293B"/>
  <rect x="210" y="145" width="560" height="22" rx="11" fill="url(#barGrad)">
    <animate attributeName="width" values="0;560" dur="1.8s" begin="0.4s" fill="freeze"/>
  </rect>
  <text x="790" y="161" fill="#E2E8F0" font-weight="700" font-size="14">80+</text>

  <!-- Font Pairings -->
  <text x="30" y="200" fill="#94A3B8" font-family="system-ui" font-size="15">Font Pairings</text>
  <rect x="210" y="185" width="560" height="22" rx="11" fill="#1E293B"/>
  <rect x="210" y="185" width="525" height="22" rx="11" fill="url(#barGrad)">
    <animate attributeName="width" values="0;525" dur="1.8s" begin="0.6s" fill="freeze"/>
  </rect>
  <text x="755" y="201" fill="#E2E8F0" font-weight="700" font-size="14">75+</text>

  <!-- Synonym Groups -->
  <text x="30" y="240" fill="#94A3B8" font-family="system-ui" font-size="15">Synonym Groups</text>
  <rect x="210" y="225" width="560" height="22" rx="11" fill="#1E293B"/>
  <rect x="210" y="225" width="560" height="22" rx="11" fill="url(#barGrad)">
    <animate attributeName="width" values="0;560" dur="1.8s" begin="0.8s" fill="freeze"/>
  </rect>
  <text x="790" y="241" fill="#E2E8F0" font-weight="700" font-size="14">120+</text>

  <!-- Toolbox Scripts -->
  <text x="30" y="280" fill="#94A3B8" font-family="system-ui" font-size="15">Toolbox Scripts</text>
  <rect x="210" y="265" width="560" height="22" rx="11" fill="#1E293B"/>
  <rect x="210" y="265" width="136" height="22" rx="11" fill="#F97316">
    <animate attributeName="width" values="0;136" dur="1.8s" begin="1s" fill="freeze"/>
  </rect>
  <text x="365" y="281" fill="#E2E8F0" font-weight="700" font-size="14">17</text>
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

## 🚀 Installation

### Option 1 — Direct use

```bash
git clone https://github.com/CyebRageAnonymuos/ui-ux-cr.git
cd ui-ux-cr
```

### Option 2 — As an OpenCode / Claude skill

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

Not installed?  
`brew install python3` (macOS) · `sudo apt install python3` (Ubuntu) · `winget install Python.Python.3.12` (Windows)

---

## 💻 Usage

### Generate a Complete Design System (core feature)

```bash
python3 scripts/search.py "SaaS landing page modern" --design-system -p "My SaaS"
```

**You get:** pattern · style · colors + extended palette · typography (with Google Fonts) · effects · components with code · animations with CSS · responsive patterns · anti-patterns · pre-delivery checklist.

### Advanced Flags

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

# Persist design system for reuse
python3 scripts/search.py "ecommerce" --design-system --persist -p "MyShop"
```

### Output Formats

```bash
python3 scripts/search.py "fintech" --design-system              # ASCII (terminal)
python3 scripts/search.py "fintech" --design-system -f markdown  # Markdown docs
python3 scripts/search.py "glassmorphism" --domain style --json  # JSON
```

---

## 🗂 Available Domains

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

## 🎯 Examples

### Example 1 — SaaS Landing Page (end-to-end)

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

### Example 2 — Healthcare Dashboard

```bash
python3 scripts/search.py "healthcare dashboard" --design-system -p "Health App"
python3 scripts/layout_generator.py --layout dashboard
python3 scripts/chart_generator.py --chart line --labels "Mon,Tue,Wed,Thu,Fri" --data "120,180,150,220,190"
```

**Recommended:** Dark Mode (OLED) · `#0F172A` bg + health green `#22C55E` · Merriweather + Open Sans

### Example 3 — Luxury E-commerce

```bash
python3 scripts/search.py "ecommerce luxury" --design-system -p "Luxury Shop"
python3 scripts/component_generator.py --component card --product "E-commerce"
python3 scripts/palette_generator.py "#1C1917" --harmony tetradic --check-wcag
```

**Recommended:** Liquid Glass + Glassmorphism · Premium dark + gold `#CA8A04` · Cormorant Garamond + Montserrat

---

## ✅ Pre-Delivery Checklist

- [ ] No emojis as icons — use `svg_generator.py`
- [ ] `cursor-pointer` on every clickable element
- [ ] Hover states 150–300 ms, zero layout shift
- [ ] Contrast ≥ 4.5:1 — verify with `accessibility_audit.py`
- [ ] All images have meaningful `alt` text
- [ ] Form inputs have associated labels
- [ ] `prefers-reduced-motion` is respected
- [ ] Tested at 375 / 768 / 1024 / 1440 px
- [ ] Loading, error, and empty states designed
- [ ] Dark mode tested

---

## 🤝 Contributing

1. Fork the repository  
2. Create your branch: `git checkout -b feature/AmazingFeature`  
3. Commit: `git commit -m 'Add some AmazingFeature'`  
4. Push and open a Pull Request  

---

## 📄 License

MIT — see [LICENSE](LICENSE).

---

<div align="center">

<svg viewBox="0 0 700 100" xmlns="http://www.w3.org/2000/svg" width="100%">
  <defs>
    <linearGradient id="footGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF006E"/>
      <stop offset="50%" stop-color="#F97316"/>
      <stop offset="100%" stop-color="#22D3EE"/>
      <animate attributeName="x1" values="0%;100%;0%" dur="6s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>

  <text x="350" y="40" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="22" font-weight="800" fill="url(#footGrad)">Built with passion by Cyber-Rage</text>
  <text x="350" y="68" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="14" fill="#64748B">Making AI-powered design accessible to everyone</text>

  <rect x="260" y="82" width="180" height="3" rx="1.5" fill="url(#footGrad)">
    <animate attributeName="width" values="180;60;180" dur="3.5s" repeatCount="indefinite"/>
    <animate attributeName="x" values="260;320;260" dur="3.5s" repeatCount="indefinite"/>
  </rect>
</svg>

<br/>

**GitHub:** [CyebRageAnonymuos/ui-ux-cr](https://github.com/CyebRageAnonymuos/ui-ux-cr)

</div>
