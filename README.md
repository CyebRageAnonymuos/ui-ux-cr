<div align="center">

# 🔥 UI UX CR — Cyber-Rage Design Intelligence Engine

**Ultra-premium design intelligence for AI assistants — 17 tools in one skill.**

<a href="https://github.com/CyebRageAnonymuos/ui-ux-cr/releases"><img src="https://img.shields.io/badge/version-2.1.0-FF006E?style=for-the-badge" alt="Version"></a>
<img src="https://img.shields.io/badge/python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/tools-17-22D3EE?style=for-the-badge" alt="Tools">
<img src="https://img.shields.io/badge/products-70+-F97316?style=for-the-badge" alt="Products">
<img src="https://img.shields.io/badge/license-MIT-10B981?style=for-the-badge" alt="License">

<p align="center">
  <a href="#features">Features</a> •
  <a href="#the-toolbox">The Toolbox</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#examples">Examples</a>
</p>

</div>

---

## 🧩 17 Tools at Your Fingertips

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

**Build a full landing page in 60 seconds:**

```bash
# 1. Design system + full page
python3 scripts/page_builder.py --product "Micro SaaS" --sections navbar,hero,features,pricing,cta,footer --out landing.html

# 2. Replace emoji placeholders with real SVG icons
python3 scripts/svg_generator.py --icon check --color "#10B981" --size 24

# 3. Add a complete animation kit + palette
python3 scripts/animation_generator.py --kit
python3 scripts/palette_generator.py "#6366F1" --harmony monochromatic --check-wcag

# 4. Audit the page
python3 scripts/accessibility_audit.py landing.html
```

---

## 📊 Database coverage

### Data coverage v2.1

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

---

## 📈 Features

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

## 💾 Installation

```bash
git clone https://github.com/CyebRageAnonymuos/ui-ux-cr.git
cd ui-ux-cr
python3 --version   # needs Python 3.x
```

**As an AI skill (opencode / Claude):**

```bash
mkdir -p .opencode/skills/ui-ux-cr
cp -r ui-ux-cr/scripts .opencode/skills/ui-ux-cr/
cp -r ui-ux-cr/data .opencode/skills/ui-ux-cr/
cp ui-ux-cr/SKILL.md .opencode/skills/ui-ux-cr/
```

---

## 🎯 Usage

### Generate a Complete Design System

```bash
python3 scripts/search.py "SaaS landing page modern" --design-system -p "My SaaS"
```

**Output:** pattern, style, colors + extended palette, typography, effects, components with code, animations, responsive patterns, anti-patterns, pre-delivery checklist.

### Advanced Flags

```bash
python3 scripts/search.py "healthcare saas" --wcag              # WCAG contrast
python3 scripts/search.py "fintech dashboard" --export-css      # CSS variables
python3 scripts/search.py "ecommerce luxury" --export-tailwind  # Tailwind config
python3 scripts/search.py "healthcare" --color-palette          # Extended palette
python3 scripts/search.py "modern dark" --multi-domains style,color,typography
python3 scripts/search.py "ecommerce" --design-system --persist -p "MyShop"  # save for reuse
```

### Output Formats

```bash
python3 scripts/search.py "fintech" --design-system          # ASCII (terminal)
python3 scripts/search.py "fintech" --design-system -f markdown  # docs
python3 scripts/search.py "glassmorphism" --domain style --json   # JSON
```

---

## 🌐 Domains & Stacks

| Domain | Use For | Domain | Use For |
|--------|---------|--------|---------|
| `style` | UI styles, colors, effects | `component` | Button, card, modal, form |
| `color` | Palettes by product | `animation` | Hover, entrance, scroll |
| `typography` | Font pairings | `responsive` | Mobile-first, grid |
| `landing` | Page structure, CTA | `design_token` | Color, spacing, shadow |
| `chart` | Chart types & libraries | `product` | SaaS, e-commerce |
| `ux` | Best practices | `icons` | lucide, heroicons |
| `react` | React/Next.js perf | `web` | aria, focus, keyboard |

**Stacks:** `html-tailwind` (default) · `react` · `nextjs` · `vue` · `nuxtjs` · `svelte` · `swiftui` · `react-native` · `flutter` · `shadcn` · `jetpack-compose` · `angular` · `laravel` · `threejs` · `astro` · `nuxt-ui`

---

## 🧪 Examples

**Example 1 — SaaS Landing Page, end to end:**
```bash
python3 scripts/search.py "SaaS landing page modern" --design-system -p "My SaaS"
python3 scripts/page_builder.py --product "SaaS (General)" --sections navbar,hero,features,pricing,cta,footer --out landing.html
python3 scripts/css_generator.py --ui-kit --primary #2563EB --cta #F97316
```
→ Glassmorphism + Flat · `#2563EB` + orange CTA `#F97316` · Poppins + Inter

**Example 2 — Healthcare Dashboard:**
```bash
python3 scripts/search.py "healthcare dashboard" --design-system -p "Health App"
python3 scripts/layout_generator.py --layout dashboard
python3 scripts/chart_generator.py --chart line --labels "Mon,Tue,Wed,Thu,Fri" --data "120,180,150,220,190"
```
→ Dark Mode (OLED) · `#0F172A` + `#22C55E` · Merriweather + Open Sans

**Example 3 — E-commerce Store:**
```bash
python3 scripts/search.py "ecommerce luxury" --design-system -p "Luxury Shop"
python3 scripts/component_generator.py --component card --product "E-commerce"
python3 scripts/palette_generator.py "#1C1917" --harmony tetradic --check-wcag
```
→ Liquid Glass + Glassmorphism · premium dark + gold `#CA8A04`

---

## ✅ Pre-Delivery Checklist

- [ ] No emojis as icons
- [ ] `cursor-pointer` on clickable elements
- [ ] Hover states 150–300ms, no layout shift
- [ ] Contrast 4.5:1 minimum
- [ ] Images have alt; inputs have labels
- [ ] `prefers-reduced-motion` supported
- [ ] Responsive 375/768/1024/1440
- [ ] Loading, error, empty states
- [ ] Dark mode tested

---

## 📄 Contributing & License

1. Fork · 2. Branch · 3. Commit · 4. PR

**MIT** — see [LICENSE](LICENSE).

<div align="center">

**Built with passion by Cyber-Rage** — making AI-powered design accessible to everyone.

[CyebRageAnonymuos/ui-ux-cr](https://github.com/CyebRageAnonymuos/ui-ux-cr)

</div>