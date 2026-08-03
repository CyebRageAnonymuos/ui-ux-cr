# Skill: ui-ux-cr

# UI UX CR v2 - Cyber-Rage Design Intelligence Engine

Ultra-premium design intelligence system **v2.0** with advanced BM25 search engine, n-gram matching, Levenshtein fuzzy matching, 120+ synonym groups, color theory engine with WCAG contrast checking, component library with code generation, animation database, responsive patterns, design tokens, RTL support, CSS/Tailwind export, and color blindness simulation. Supports **70+ product types**, **46+ styles**, **80+ color palettes**, **75+ font pairings**, and **16+ tech stacks**.

## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

If Python is not installed, install it based on user's OS:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## How to Use This Skill

When user requests UI/UX work (design, build, create, implement, review, fix, improve), follow this workflow:

### Step 1: Analyze User Requirements

Extract key information from user request:
- **Product type**: SaaS, e-commerce, portfolio, dashboard, landing page, etc.
- **Style keywords**: minimal, playful, professional, elegant, dark mode, etc.
- **Industry**: healthcare, fintech, gaming, education, etc.
- **Stack**: React, Vue, Next.js, or default to `html-tailwind`

### Step 2: Generate Design System (REQUIRED)

**Always start with `--design-system`** to get comprehensive recommendations with reasoning:

```bash
python3 scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```

This command:
1. Searches 10 domains in parallel (product, style, color, landing, typography, component, animation, responsive, design_token, ux)
2. Applies reasoning rules from `ui-reasoning.csv` to select best matches
3. Generates extended color palette using color theory engine
4. Returns complete design system: pattern, style, colors, typography, effects, components, animations, responsive patterns
5. Includes anti-patterns to avoid and pre-delivery checklist

**Example:**
```bash
python3 scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

### Step 2b: Persist Design System (Master + Overrides Pattern)

To save the design system for hierarchical retrieval across sessions, add `--persist`:

```bash
python3 scripts/search.py "<query>" --design-system --persist -p "Project Name"
```

This creates:
- `design-system/MASTER.md` — Global Source of Truth with all design rules
- `design-system/pages/` — Folder for page-specific overrides

**With page-specific override:**
```bash
python3 scripts/search.py "<query>" --design-system --persist -p "Project Name" --page "dashboard"
```

### Step 2c: Comprehensive Project Analysis

For a complete analysis across all domains:

```bash
python3 scripts/search.py "<query>" --analyze
```

This returns recommendations across all 10 domains simultaneously.

### Step 2d: Advanced v2 Features

**WCAG Contrast Check:**
```bash
python3 scripts/search.py "healthcare saas" --wcag
```

**Export CSS Custom Properties:**
```bash
python3 scripts/search.py "fintech dashboard" --export-css
```

**Export Tailwind Config:**
```bash
python3 scripts/search.py "ecommerce luxury" --export-tailwind
```

**Generate Color Palette:**
```bash
python3 scripts/search.py "healthcare" --color-palette
```

### Step 3: Generate with Toolbox Scripts (v2.1)

After getting the design system, generate ready-to-use assets with the toolbox:

| Tool | Purpose | Example |
|------|---------|---------|
| `svg_generator.py` | SVG icons, patterns, logos | `python3 scripts/svg_generator.py --icon search --size 24` |
| `css_generator.py` | Shadows, gradients, glass, glow, UI kit, neumorphism | `python3 scripts/css_generator.py --ui-kit --primary #2563EB` |
| `palette_generator.py` | Harmony palettes, shade scales, WCAG report | `python3 scripts/palette_generator.py "#2563EB" --harmony triadic --check-wcag` |
| `typography_generator.py` | Modular type scales + font pairings from DB | `python3 scripts/typography_generator.py --scale golden-ratio` |
| `theme_exporter.py` | Export theme to CSS/Tailwind/SCSS/JSON | `python3 scripts/theme_exporter.py "#2563EB" --format all` |
| `layout_generator.py` | Grid systems, containers, spacing, breakpoints, layout templates | `python3 scripts/layout_generator.py --layout dashboard` |
| `component_generator.py` | Ready HTML/Tailwind components from database | `python3 scripts/component_generator.py --component navbar --product "SaaS (General)"` |
| `page_builder.py` | Compose full HTML page from components | `python3 scripts/page_builder.py --product "SaaS (General)" --sections navbar,hero,features,cta,footer --out landing.html` |
| `animation_generator.py` | CSS animations with parameters + full animation kit | `python3 scripts/animation_generator.py --type bounce --duration 0.6` |
| `chart_generator.py` | Chart.js & Recharts configs (line, bar, pie, area, radar...) | `python3 scripts/chart_generator.py --chart bar --labels "Q1,Q2" --data "25,40"` |
| `pattern_generator.py` | CSS background patterns (dots, grid, checkerboard, waves...) | `python3 scripts/pattern_generator.py checkerboard --color #2563EB` |
| `favicon_generator.py` | Favicon SVG, HTML head, PWA manifest, size cheat sheet | `python3 scripts/favicon_generator.py --text CR --bg #2563EB` |
| `copy_generator.py` | UI copy: headlines, CTAs, placeholders, errors, A/B variants | `python3 scripts/copy_generator.py --headline saas --count 3` |
| `mockup_generator.py` | ASCII wireframes (desktop, dashboard, mobile, landing, login) | `python3 scripts/mockup_generator.py --type dashboard` |
| `social_specs.py` | Social media dimension cheat sheets (10 platforms) | `python3 scripts/social_specs.py --platform instagram` |
| `banner_generator.py` | ASCII art banners for terminal | `python3 scripts/banner_generator.py --text "UI UX CR" --style block` |
| `accessibility_audit.py` | WCAG audit of HTML files (contrast, alt, labels, headings) | `python3 scripts/accessibility_audit.py index.html` |

**Toolbox Workflow:**
1. `page_builder.py --product "SaaS (General)"` → get a complete HTML landing page
2. `component_generator.py --component hero` → get individual components with CSS variables
3. `svg_generator.py --icon check` → get SVG icon to replace emoji placeholders
4. `css_generator.py --ui-kit` → get complete button/card/input/badge CSS kit
5. `palette_generator.py "#2563EB" --harmony triadic` → get harmony palette with WCAG report
6. `animation_generator.py --kit` → get transitions, micro-interactions, loaders
7. `favicon_generator.py --text CR` → get favicon + HTML head + manifest
8. `accessibility_audit.py` → verify the final HTML passes WCAG checks

### Step 3: Supplement with Detailed Searches (as needed)

After getting the design system, use domain searches to get additional details:

```bash
python3 scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**Available Domains:**

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `style` | UI styles, colors, effects | glassmorphism, minimalism, dark mode |
| `color` | Color palettes by product type | saas, ecommerce, healthcare |
| `typography` | Font pairings, Google Fonts | elegant, playful, professional |
| `landing` | Page structure, CTA strategies | hero, testimonial, pricing |
| `chart` | Chart types, library recommendations | trend, comparison, funnel |
| `ux` | Best practices, anti-patterns | animation, accessibility, loading |
| `component` | Component recommendations | button, card, modal, form |
| `animation` | Animation patterns | hover, entrance, scroll, loading |
| `responsive` | Responsive design patterns | mobile-first, grid, typography |
| `design_token` | Design tokens and variables | color, spacing, typography, shadow |
| `product` | Product type recommendations | SaaS, e-commerce, healthcare |
| `icons` | Icon recommendations | lucide, heroicons, symbol |
| `react` | React/Next.js performance | memo, suspense, bundle |
| `web` | Web interface guidelines | aria, focus, keyboard |

### Step 4: Stack Guidelines (Default: html-tailwind)

Get implementation-specific best practices. If user doesn't specify a stack, **default to `html-tailwind`**.

```bash
python3 scripts/search.py "<keyword>" --stack html-tailwind
```

**Available Stacks:**

| Stack | Focus |
|-------|-------|
| `html-tailwind` | Tailwind utilities, responsive, a11y (DEFAULT) |
| `react` | State, hooks, performance, patterns |
| `nextjs` | SSR, routing, images, API routes |
| `vue` | Composition API, Pinia, Vue Router |
| `nuxtjs` | Nuxt.js specific patterns |
| `svelte` | Runes, stores, SvelteKit |
| `swiftui` | Views, State, Navigation, Animation |
| `react-native` | Components, Navigation, Lists |
| `flutter` | Widgets, State, Layout, Theming |
| `shadcn` | shadcn/ui components, theming |
| `jetpack-compose` | Composables, Modifiers, State |
| `angular` | Components, Services, RxJS |
| `laravel` | Blade, Livewire, Inertia.js |
| `threejs` | Three.js, WebGL, 3D |
| `astro` | Islands, Content Collections |
| `nuxt-ui` | Nuxt UI components |

### Step 5: Multi-Domain Search

Search across multiple domains simultaneously:

```bash
python3 scripts/search.py "<query>" --multi-domains style,color,typography
```

---

## Output Formats

The `--design-system` flag supports two output formats:

```bash
# ASCII box (default) - best for terminal display
python3 scripts/search.py "fintech crypto" --design-system

# Markdown - best for documentation
python3 scripts/search.py "fintech crypto" --design-system -f markdown
```

---

## Example Workflow

**User request:** "Build a landing page for my SaaS product"

### Step 1: Analyze Requirements
- Product type: SaaS
- Style keywords: modern, clean, professional
- Industry: Technology/SaaS
- Stack: html-tailwind (default)

### Step 2: Generate Design System

```bash
python3 scripts/search.py "SaaS landing page modern" --design-system -p "My SaaS"
```

**Output:** Complete design system with pattern, style, colors, typography, effects, components, animations, responsive patterns.

### Step 3: Supplement with Detailed Searches

```bash
# Get UX guidelines for animation and accessibility
python3 scripts/search.py "animation accessibility" --domain ux

# Get component recommendations
python3 scripts/search.py "button card modal" --domain component

# Get responsive patterns
python3 scripts/search.py "mobile-first grid" --domain responsive
```

### Step 4: Stack Guidelines

```bash
python3 scripts/search.py "layout responsive form" --stack html-tailwind
```

### Step 5: Implement the Design

Using the design system output, implement the UI with proper colors, fonts, spacing, components, animations, and responsive patterns.

---

## Data Coverage v2.0

| Category | v1.x | v2.0 |
|----------|------|------|
| Product Types | 51 | **70+** |
| UI Styles | 31 | **46+** |
| Color Palettes | 61 | **80+** |
| Font Pairings | 61 | **75+** |
| Synonym Groups | 34 | **120+** |
| Animations | 31 | **31** |
| Components | 31 | **31** |
| Responsive Patterns | 21 | **21** |
| Backgrounds | 46 | **46** |
| Tech Stacks | 16 | **16** |
| WCAG Checks | ✗ | **Built-in** |
| Code Generation | ✗ | **Auto-generated** |
| Color Blind Simulation | ✗ | **3 types** |
| CSS/Tailwind Export | ✗ | **Supported** |
| SVG Icon/Pattern Generator | ✗ | **New tool** |
| CSS Utility Generator | ✗ | **New tool** |
| Palette Generator | ✗ | **New tool** |
| Typography Generator | ✗ | **New tool** |
| Component Code Generator | ✗ | **12 components** |
| Page Builder | ✗ | **Full HTML pages** |
| Layout/Grid Generator | ✗ | **5 templates** |
| Animation Generator | ✗ | **12 animations + kit** |
| Pattern Generator | ✗ | **12 CSS patterns** |
| Favicon Generator | ✗ | **SVG + manifest** |
| Copy Generator | ✗ | **UI microcopy** |
| ASCII Mockup Generator | ✗ | **5 layouts** |
| Chart Config Generator | ✗ | **Chart.js + Recharts** |
| Social Media Specs | ✗ | **10 platforms** |
| ASCII Banner Generator | ✗ | **2 fonts + rainbow** |
| Accessibility Auditor | ✗ | **WCAG audit tool** |

## Key Features v2.0

### Enhanced BM25 Search Engine v2
- N-gram matching (bigram/trigram) for phrase detection
- Levenshtein distance fuzzy matching for typo tolerance
- 120+ synonym groups for semantic expansion (3x more than v1)
- Category-based keyword boosting
- Weighted domain detection with exact phrase priority

### Color Theory Engine v2
- Extended palette generation (50-900 shades)
- 6 color harmony types (complementary, analogous, triadic, split-complementary, tetradic, monochromatic)
- HSL/HSV/CMYK color space conversion
- **WCAG contrast checking** (AA/AAA pass/fail)
- **Color blindness simulation** (protanopia, deuteranopia, tritanopia)
- **Gradient generation** with multi-stop CSS output
- **Temperature detection** (warm/cool/neutral)
- Automatic text color suggestion based on luminance

### Component Library v2
- 30+ pre-built component recommendations
- **Auto-generated HTML/Tailwind code snippets**
- **CSS Custom Properties export**
- **Tailwind Config export**
- Accessibility guidelines with ARIA attributes

### Animation Database v2
- 30+ animation patterns with full CSS code
- Duration, easing, GPU optimization info
- Reduced motion fallbacks
- **Category organization** (entrance, interaction, feedback, scroll, loading)

### Responsive Patterns v2
- 20+ responsive design patterns
- Mobile-first approach with container queries
- **Breakpoint specifications** (375px, 768px, 1024px, 1440px)
- Touch-friendly target sizes (44x44px)
- RTL-ready layout patterns

### Design Tokens v2
- 70+ design token categories
- CSS variables and Tailwind classes
- Light and dark mode values
- **Spacing scale** (xs to 3xl)
- **Shadow depth system** (sm to xl)

### New v2 Commands
- `--wcag` : WCAG contrast ratio analysis
- `--export-css` : Generate CSS custom properties
- `--export-tailwind` : Export Tailwind config
- `--color-palette` : Generate extended color palette

---

## Common Rules for Professional UI

### Icons & Visual Elements

| Rule | Do | Don't |
|------|----|-----|
| **No emoji icons** | Use SVG icons (Heroicons, Lucide, Simple Icons) | Use emojis as UI icons |
| **Stable hover states** | Use color/opacity transitions on hover | Use scale transforms that shift layout |
| **Correct brand logos** | Research official SVG from Simple Icons | Guess or use incorrect logo paths |
| **Consistent icon sizing** | Use fixed viewBox (24x24) with w-6 h-6 | Mix different icon sizes randomly |

### Interaction & Cursor

| Rule | Do | Don't |
|------|----|-----|
| **Cursor pointer** | Add `cursor-pointer` to all clickable elements | Leave default cursor on interactive elements |
| **Hover feedback** | Provide visual feedback (color, shadow, border) | No indication element is interactive |
| **Smooth transitions** | Use `transition-colors duration-200` | Instant state changes or too slow (>500ms) |

### Light/Dark Mode Contrast

| Rule | Do | Don't |
|------|----|-----|
| **Glass card light mode** | Use `bg-white/80` or higher opacity | Use `bg-white/10` (too transparent) |
| **Text contrast light** | Use `#0F172A` (slate-900) for text | Use `#94A3B8` (slate-400) for body text |
| **Muted text light** | Use `#475569` (slate-600) minimum | Use gray-400 or lighter |
| **Border visibility** | Use `border-gray-200` in light mode | Use `border-white/10` (invisible) |

---

## Pre-Delivery Checklist

Before delivering UI code, verify:

### Visual Quality
- [ ] No emojis used as icons (use SVG instead)
- [ ] All icons from consistent icon set (Heroicons/Lucide)
- [ ] Brand logos are correct
- [ ] Hover states don't cause layout shift

### Interaction
- [ ] All clickable elements have `cursor-pointer`
- [ ] Hover states provide clear visual feedback
- [ ] Transitions are smooth (150-300ms)
- [ ] Focus states visible for keyboard navigation

### Light/Dark Mode
- [ ] Light mode text has sufficient contrast (4.5:1 minimum)
- [ ] Glass/transparent elements visible in light mode
- [ ] Borders visible in both modes
- [ ] Test both modes before delivery

### Layout
- [ ] Floating elements have proper spacing from edges
- [ ] No content hidden behind fixed navbars
- [ ] Responsive at 375px, 768px, 1024px, 1440px
- [ ] No horizontal scroll on mobile

### Accessibility
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Color is not the only indicator
- [ ] `prefers-reduced-motion` respected

### Components
- [ ] All interactive elements keyboard accessible
- [ ] Loading states implemented
- [ ] Error states handled
- [ ] Empty states designed

---

## Tips for Better Results

1. **Be specific with keywords** - "healthcare SaaS dashboard" > "app"
2. **Use `--analyze`** - Get comprehensive analysis across all domains
3. **Search multiple times** - Different keywords reveal different insights
4. **Combine domains** - Style + Typography + Color = Complete design system
5. **Use `--multi-domains`** - Search across multiple domains simultaneously
6. **Check components** - Get component recommendations for your design
7. **Use animations** - Add polish with recommended animations
8. **Follow responsive patterns** - Ensure mobile-first design
9. **Use design tokens** - Maintain consistency with token system
10. **Iterate** - If first search doesn't match, try different keywords
