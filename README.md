<div align="center">

# 🔥 UI UX CR — Cyber-Rage Design Intelligence Engine

**Ultra-premium design intelligence for AI assistants — 29 tools in one skill.**

<a href="https://github.com/CyebRageAnonymuos/ui-ux-cr/releases"><img src="https://img.shields.io/badge/version-3.1.0-FF006E?style=for-the-badge" alt="Version"></a>
<img src="https://img.shields.io/badge/python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/tools-29-22D3EE?style=for-the-badge" alt="Tools">
<img src="https://img.shields.io/badge/themes-65-A855F7?style=for-the-badge" alt="Themes">
<img src="https://img.shields.io/badge/icons-155-F97316?style=for-the-badge" alt="Icons">
<img src="https://img.shields.io/badge/products-70+-10B981?style=for-the-badge" alt="Products">
<img src="https://img.shields.io/badge/license-MIT-EAB308?style=for-the-badge" alt="License">

<p align="center">
  <a href="#features">Features</a> •
  <a href="#the-toolbox">The Toolbox</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#examples">Examples</a>
</p>

</div>

---

## 🧩 29 Tools at Your Fingertips

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
| 17 | `theme_pack.py` | **65 ready-made premium themes** (Dracula, Nord, Cyberpunk, Luxury Gold...) | `python3 scripts/theme_pack.py --name dracula --format css` |
| 18 | `text_deco.py` | **Fancy Unicode fonts + decorative shapes** — emoji-free | `python3 scripts/text_deco.py --text "Sale" --style gothic` |
| 19 | `accessibility_audit.py` | WCAG audit of HTML (contrast, alt, labels) | `python3 scripts/accessibility_audit.py index.html` |
| 20 | `banner_generator.py` | ASCII art banners for the terminal (2 fonts + rainbow) | `python3 scripts/banner_generator.py --text "UI UX CR" --style block` |
| 22 | `gradient_generator.py` | **NEW v3** Linear/radial/conic/mesh gradients + gradient buttons | `python3 scripts/gradient_generator.py --mesh aurora` |
| 21 | `logo_generator.py` | **NEW v3** SVG logos: monogram, badge, wordmark, shield | `python3 scripts/logo_generator.py --text "Cyber Rage" --style shield` |
| 23 | `form_generator.py` | **NEW v3** Accessible forms: login, signup, contact, search | `python3 scripts/form_generator.py --form login --primary #2563EB` |
| 24 | `email_template.py` | **NEW v3** Responsive table-based emails (welcome, reset, receipt...) | `python3 scripts/email_template.py --type reset --brand "Acme"` |
| 25 | `tokens_exporter.py` | **NEW v3** W3C + Figma Tokens + Style Dictionary export | `python3 scripts/tokens_exporter.py "#2563EB" --format figma` |
| 26 | `darkmode_generator.py` | **NEW v3** Light/dark theme pairs + persisted toggle | `python3 scripts/darkmode_generator.py "#2563EB" --toggle` |
| 27 | `seo_audit.py` | **NEW v3** SEO/head audit: title, meta, OG, headings, images | `python3 scripts/seo_audit.py index.html` |
| 28 | `icon_spriter.py` | **NEW v3** SVG symbol sprite sheets + `<use>` markup | `python3 scripts/icon_spriter.py --icons search,check --out icons.svg` |
| 29 | `design_linter.py` | **NEW v3.1** Contracts for the recommendation half: WCAG on DB palettes, harmony math, shade monotonicity, CVD collisions, font-import checks | `python3 scripts/design_linter.py --audit-db` |

**Try the fancy fonts & shapes:**

```bash
# Unicode font styles: gothic, script, bubble, aesthetic, small-caps...
python3 scripts/text_deco.py --text "Cyber Rage" --style gothic
# → ℭ𝔶𝔟𝔢𝔯 ℜ𝔞𝔤𝔢

# Decorative dividers & frames (instead of emojis)
python3 scripts/text_deco.py --divider star-line
python3 scripts/text_deco.py --frame "THEME PACK" --frame-style stars

# Progress bars & ratings
python3 scripts/text_deco.py --bar 70      # ██████████████░░░░░░ 70%
python3 scripts/text_deco.py --rating 4    # ★★★★☆
```

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

### Data coverage v3.0

| Category | v1.x | v2.0 | v2.2 | v3.0 |
|----------|------|------|------|------|
| Product Types | 51 | 70+ | **70+** | **70+** |
| UI Styles | 31 | 46+ | **46+** | **46+** |
| Color Palettes | 61 | 80+ | **80+** | **80+** |
| Font Pairings | 61 | 75+ | **103** | **103** |
| Premium Themes | — | — | **65** | **65** |
| Synonym Groups | 34 | 120+ | **120+** | **120+** |
| Toolbox Scripts | ✗ | 9 | 19 | **29** |
| Components | — | — | **12 generated** | **12 generated** |
| Layout Templates | — | — | **5** | **5** |
| Chart Types | — | — | **8 + 2 frameworks** | **8 + 2 frameworks** |
| Background Patterns | — | — | **12 CSS** | **12 CSS + 5 mesh presets** |
| SVG Icons | — | — | **155** | **155 + sprite sheets** |
| Unicode Font Styles | — | — | **25+** | **25+** |
| Logo Styles | — | — | — | **4** |
| Email Templates | — | — | — | **4 responsive** |
| Form Types | — | — | — | **5 accessible** |
| Token Formats | — | — | — | **W3C + Figma + Style Dictionary** |

### What's new in v3.1

- **Design Linter** (`design_linter.py`): contracts for the "no-format" half of the pipeline - the recommendation database itself is now audited. Every palette checked for WCAG AA text contrast and readable CTA labels, hue geometry verified against the claimed harmony type, shade scales checked for monotonicity, color pairs checked for color-blind collisions (protanopia/deuteranopia/tritanopia), and font-pairing rows checked to actually import both recommended fonts (Google Fonts and Fontshare URL styles). `--audit-db` audits all 81 palettes + 103 pairings; `--colors`/`--claimed-harmony`/`--shades`/`--pairing` lint arbitrary input
- First full-database audit found 2 real errors (pairings whose import snippet can't load the recommended font - Proxima Nova isn't on Google Fonts) and 27 advisory warnings

### What's new in v3.0

- **8 new tools**: gradient studio (linear/radial/conic/mesh/buttons), SVG logo generator (monogram/badge/wordmark/shield), accessible form generator, responsive email templates, W3C/Figma/Style-Dictionary token exporter, dark-mode system with no-flash toggle, SEO auditor, SVG icon sprite builder
- **28 bug fixes across the existing 19 tools**, including: SSH-style crash bugs (component_generator crashed on ~19 valid products; `--type slide` without `--param` crashed; mirrored text style crashed on X/Y/Z), invalid output (CSS variables emitted outside `:root`, chart.js `area` type, Recharts imports with empty slots, animation classes referencing non-existent keyframes), silently-ignored flags (`--style`, `--fg`, `--size`, `--mix`, `--glass`), page_builder swallowing failures and writing empty pages with exit 0, and the ASCII design-system box being misaligned on every line
- Mobile mockups render perfectly aligned at any width; Tailwind grid gap no longer emits `gap-16` for 16px

---

## 📈 Features

| Feature | Description |
|---------|-------------|
| **Enhanced BM25 Search** | Fuzzy matching, n-gram detection, 120+ synonym groups |
| **Design System Generator** | 10 domains searched in parallel with reasoning engine |
| **Color Theory Engine** | Extended palettes, 6 harmony types, WCAG contrast, color-blind simulation |
| **29 Toolbox Scripts** | SVG icons, CSS kits, components, animations, charts, pages, mockups, logos, emails, tokens |
| **65 Premium Themes** | Dracula, Nord, Tokyo Night, Cyberpunk, Luxury Gold — export to CSS/Tailwind/JSON |
| **Fancy Unicode Fonts** | 25+ text styles (gothic, script, bubble...) + decorative shapes, emoji-free |
| **Component Generator** | 12 ready components (navbar, hero, pricing, modal, table, sidebar...) |
| **Page Builder** | Compose a full HTML landing page in one command |
| **Accessibility Auditor** | WCAG audit: contrast, alt text, labels, heading order |
| **SEO Auditor** | NEW v3: title, meta, canonical, Open Graph, headings, images, lazy-loading |
| **Dark Mode System** | NEW v3: full light/dark pairs + persisted no-flash toggle |
| **Standards-based Tokens** | NEW v3: W3C Design Tokens draft + Figma Tokens + Style Dictionary pipeline |
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