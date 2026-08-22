#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design System Generator v2.0 - Enhanced with color theory, component code gen,
responsive patterns, RTL support, accessibility checking, theme export
Cyber-Rage Design Intelligence Engine
"""

import csv
import json
import os
from datetime import datetime
from pathlib import Path
from core import search, DATA_DIR, multi_search

REASONING_FILE = "ui-reasoning.csv"

SEARCH_CONFIG = {
    "product": {"max_results": 1},
    "style": {"max_results": 3},
    "color": {"max_results": 2},
    "landing": {"max_results": 2},
    "typography": {"max_results": 2},
    "component": {"max_results": 5},
    "animation": {"max_results": 3},
    "responsive": {"max_results": 3},
    "design_token": {"max_results": 2},
    "background": {"max_results": 3}
}


# ============ COLOR THEORY ENGINE V2 ============
class ColorTheoryEngine:
    """Advanced color theory engine v2"""

    def __init__(self):
        self.color_harmonies = {
            "complementary": "180 degrees apart on color wheel",
            "analogous": "30 degrees apart, adjacent on color wheel",
            "triadic": "120 degrees apart, forming triangle",
            "split_complementary": "Base + two colors adjacent to complement",
            "tetradic": "Four colors forming rectangle on color wheel",
            "monochromatic": "Single hue with varying saturation/lightness"
        }

    def hex_to_hsl(self, hex_color):
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16)/255, int(hex_color[2:4], 16)/255, int(hex_color[4:6], 16)/255
        max_c, min_c = max(r, g, b), min(r, g, b)
        l = (max_c + min_c) / 2
        if max_c == min_c:
            h = s = 0
        else:
            d = max_c - min_c
            s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
            if max_c == r:
                h = (g - b) / d + (6 if g < b else 0)
            elif max_c == g:
                h = (b - r) / d + 2
            else:
                h = (r - g) / d + 4
            h /= 6
        return int(h * 360), int(s * 100), int(l * 100)

    def hsl_to_hex(self, h, s, l):
        s = max(0, min(100, s)) / 100
        l = max(0, min(100, l)) / 100
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = l - c / 2
        if h < 60:
            r, g, b = c, x, 0
        elif h < 120:
            r, g, b = x, c, 0
        elif h < 180:
            r, g, b = 0, c, x
        elif h < 240:
            r, g, b = 0, x, c
        elif h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        return f"#{int((r + m) * 255):02x}{int((g + m) * 255):02x}{int((b + m) * 255):02x}"

    def relative_luminance(self, hex_color):
        r, g, b = int(hex_color.lstrip('#')[0:2], 16)/255, int(hex_color.lstrip('#')[2:4], 16)/255, int(hex_color.lstrip('#')[4:6], 16)/255
        r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
        g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
        b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def contrast_ratio(self, color1, color2):
        l1 = self.relative_luminance(color1)
        l2 = self.relative_luminance(color2)
        lighter = max(l1, l2)
        darker = min(l1, l2)
        return (lighter + 0.05) / (darker + 0.05)

    def generate_palette(self, primary_hex, harmony="complementary", count=5):
        h, s, l = self.hex_to_hsl(primary_hex)
        palette = [primary_hex]

        if harmony == "complementary":
            palette.append(self.hsl_to_hex((h + 180) % 360, s, l))
        elif harmony == "analogous":
            for offset in [-30, 30, -60, 60]:
                palette.append(self.hsl_to_hex((h + offset) % 360, s, l))
        elif harmony == "triadic":
            palette.append(self.hsl_to_hex((h + 120) % 360, s, l))
            palette.append(self.hsl_to_hex((h + 240) % 360, s, l))
        elif harmony == "split_complementary":
            palette.append(self.hsl_to_hex((h + 150) % 360, s, l))
            palette.append(self.hsl_to_hex((h + 210) % 360, s, l))
        elif harmony == "monochromatic":
            for lightness in [30, 50, 70, 90]:
                palette.append(self.hsl_to_hex(h, s, lightness))

        palette.append(self.hsl_to_hex(h, 5, 95))
        palette.append(self.hsl_to_hex(h, 5, 10))

        return palette[:count]

    def generate_extended_palette(self, primary_hex):
        try:
            h, s, l = self.hex_to_hsl(primary_hex)
            return {
                "50": self.hsl_to_hex(h, s, 95),
                "100": self.hsl_to_hex(h, s, 90),
                "200": self.hsl_to_hex(h, s, 80),
                "300": self.hsl_to_hex(h, s, 65),
                "400": self.hsl_to_hex(h, s, 55),
                "500": primary_hex,
                "600": self.hsl_to_hex(h, s, 40),
                "700": self.hsl_to_hex(h, s, 30),
                "800": self.hsl_to_hex(h, s, 20),
                "900": self.hsl_to_hex(h, s, 10),
            }
        except:
            return {}


# ============ DESIGN SYSTEM GENERATOR V2 ============
class DesignSystemGenerator:
    """Generates design system recommendations from aggregated searches."""

    def __init__(self):
        self.reasoning_data = self._load_reasoning()
        self.color_engine = ColorTheoryEngine()

    def _load_reasoning(self):
        filepath = DATA_DIR / REASONING_FILE
        if not filepath.exists():
            return []
        with open(filepath, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def _multi_domain_search(self, query, style_priority=None):
        results = {}
        for domain, config in SEARCH_CONFIG.items():
            if domain == "style" and style_priority:
                priority_query = " ".join(style_priority[:2]) if style_priority else query
                combined_query = f"{query} {priority_query}"
                results[domain] = search(combined_query, domain, config["max_results"])
            else:
                results[domain] = search(query, domain, config["max_results"])
        return results

    def _find_reasoning_rule(self, category):
        category_lower = category.lower()
        for rule in self.reasoning_data:
            if rule.get("UI_Category", "").lower() == category_lower:
                return rule
        for rule in self.reasoning_data:
            ui_cat = rule.get("UI_Category", "").lower()
            if ui_cat in category_lower or category_lower in ui_cat:
                return rule
        for rule in self.reasoning_data:
            ui_cat = rule.get("UI_Category", "").lower()
            keywords = ui_cat.replace("/", " ").replace("-", " ").split()
            if any(kw in category_lower for kw in keywords):
                return rule
        return {}

    def _apply_reasoning(self, category, search_results):
        rule = self._find_reasoning_rule(category)
        if not rule:
            return {
                "pattern": "Hero + Features + CTA",
                "style_priority": ["Minimalism", "Flat Design"],
                "color_mood": "Professional",
                "typography_mood": "Clean",
                "key_effects": "Subtle hover transitions",
                "anti_patterns": "",
                "decision_rules": {},
                "severity": "MEDIUM"
            }

        decision_rules = {}
        try:
            decision_rules = json.loads(rule.get("Decision_Rules", "{}"))
        except json.JSONDecodeError:
            pass

        return {
            "pattern": rule.get("Recommended_Pattern", ""),
            "style_priority": [s.strip() for s in rule.get("Style_Priority", "").split("+")],
            "color_mood": rule.get("Color_Mood", ""),
            "typography_mood": rule.get("Typography_Mood", ""),
            "key_effects": rule.get("Key_Effects", ""),
            "anti_patterns": rule.get("Anti_Patterns", ""),
            "decision_rules": decision_rules,
            "severity": rule.get("Severity", "MEDIUM")
        }

    def _select_best_match(self, results, priority_keywords):
        if not results:
            return {}
        if not priority_keywords:
            return results[0]

        for priority in priority_keywords:
            priority_lower = priority.lower().strip()
            for result in results:
                style_name = result.get("Style Category", "").lower()
                if priority_lower in style_name or style_name in priority_lower:
                    return result

        scored = []
        for result in results:
            result_str = str(result).lower()
            score = 0
            for kw in priority_keywords:
                kw_lower = kw.lower().strip()
                if kw_lower in result.get("Style Category", "").lower():
                    score += 10
                elif kw_lower in result.get("Keywords", "").lower():
                    score += 3
                elif kw_lower in result_str:
                    score += 1
            scored.append((score, result))

        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[0][1] if scored and scored[0][0] > 0 else results[0]

    def _extract_results(self, search_result):
        return search_result.get("results", [])

    def _generate_code_snippets(self, design_system):
        """Generate HTML/Tailwind code snippets from the design system"""
        colors = design_system.get("colors", {})
        primary = colors.get("primary", "#2563EB")
        secondary = colors.get("secondary", "#3B82F6")
        cta = colors.get("cta", "#F97316")
        bg = colors.get("background", "#F8FAFC")
        text_color = colors.get("text", "#1E293B")
        border = colors.get("border", "#E2E8F0")
        typography = design_system.get("typography", {})
        heading_font = typography.get("heading", "Inter")
        body_font = typography.get("body", "Inter")

        return {
            "button": f"""<button class="px-6 py-3 font-semibold rounded-lg transition-all duration-200 hover:translate-y-[-1px]"
        style="background: {cta}; color: white;">
  Get Started
</button>""",
            "card": f"""<div class="rounded-xl p-6 shadow-md transition-all duration-200 hover:shadow-lg hover:translate-y-[-2px]"
     style="background: {bg}; border: 1px solid {border};">
  <h3 style="font-family: '{heading_font}', sans-serif; color: {text_color};">Card Title</h3>
  <p style="font-family: '{body_font}', sans-serif; color: {text_color}; opacity: 0.8;">Card content goes here</p>
</div>""",
            "hero_section": f"""<section class="min-h-screen flex flex-col justify-center items-center px-4 text-center"
     style="background: linear-gradient(135deg, {primary}11, {secondary}11);">
  <h1 class="text-4xl md:text-6xl font-bold mb-6"
      style="font-family: '{heading_font}', sans-serif; color: {text_color};">
    Headline Goes Here
  </h1>
  <p class="text-lg md:text-xl mb-8 max-w-2xl"
     style="font-family: '{body_font}', sans-serif; color: {text_color}; opacity: 0.8;">
    Subtitle or description text
  </p>
  <button class="px-8 py-4 text-lg font-semibold rounded-lg transition-all duration-200"
          style="background: {cta}; color: white;">
    Call to Action
  </button>
</section>""",
            "input": f"""<input type="text" placeholder="Enter your email"
       class="px-4 py-3 rounded-lg border transition-all duration-200 focus:outline-none focus:ring-2"
       style="border-color: {border}; focus:border-color: {primary}; --tw-ring-color: {primary}20;">""",
            "css_variables": f""":root {{
  --color-primary: {primary};
  --color-secondary: {secondary};
  --color-cta: {cta};
  --color-background: {bg};
  --color-text: {text_color};
  --color-border: {border};
  --font-heading: '{heading_font}', sans-serif;
  --font-body: '{body_font}', sans-serif;
}}"""
        }

    def _generate_component_specs(self, components):
        """Generate detailed component specifications"""
        specs = []
        for comp in components[:5]:
            name = comp.get("Component", "")
            variants = comp.get("Variants", "")
            tailwind = comp.get("Tailwind", "")
            accessibility = comp.get("Accessibility", "")
            specs.append({
                "name": name,
                "variants": variants,
                "tailwind": tailwind,
                "accessibility": accessibility,
            })
        return specs

    def generate(self, query, project_name=None):
        """Generate complete design system recommendation v2."""
        product_result = search(query, "product", 1)
        product_results = product_result.get("results", [])
        category = "General"
        if product_results:
            category = product_results[0].get("Product Type", "General")

        reasoning = self._apply_reasoning(category, {})
        style_priority = reasoning.get("style_priority", [])

        search_results = self._multi_domain_search(query, style_priority)
        search_results["product"] = product_result

        style_results = self._extract_results(search_results.get("style", {}))
        color_results = self._extract_results(search_results.get("color", {}))
        typography_results = self._extract_results(search_results.get("typography", {}))
        landing_results = self._extract_results(search_results.get("landing", {}))
        component_results = self._extract_results(search_results.get("component", {}))
        animation_results = self._extract_results(search_results.get("animation", {}))
        responsive_results = self._extract_results(search_results.get("responsive", {}))
        token_results = self._extract_results(search_results.get("design_token", {}))
        background_results = self._extract_results(search_results.get("background", {}))

        best_style = self._select_best_match(style_results, reasoning.get("style_priority", []))
        best_color = color_results[0] if color_results else {}
        best_typography = typography_results[0] if typography_results else {}
        best_landing = landing_results[0] if landing_results else {}

        style_effects = best_style.get("Effects & Animation", "")
        reasoning_effects = reasoning.get("key_effects", "")
        combined_effects = style_effects if style_effects else reasoning_effects

        primary_hex = best_color.get("Primary (Hex)", "#2563EB")
        secondary_hex = best_color.get("Secondary (Hex)", "#3B82F6")
        cta_hex = best_color.get("CTA (Hex)", "#F97316")
        bg_hex = best_color.get("Background (Hex)", "#F8FAFC")
        text_hex = best_color.get("Text (Hex)", "#1E293B")
        border_hex = best_color.get("Border (Hex)", "#E2E8F0")

        extended_palette = self.color_engine.generate_extended_palette(primary_hex)

        # Calculate contrast for accessibility
        contrast_primary_on_bg = round(self.color_engine.contrast_ratio(primary_hex, bg_hex), 2)
        contrast_text_on_bg = round(self.color_engine.contrast_ratio(text_hex, bg_hex), 2)

        design_system = {
            "project_name": project_name or query.upper(),
            "category": category,
            "query": query,
            "pattern": {
                "name": best_landing.get("Pattern Name", reasoning.get("pattern", "Hero + Features + CTA")),
                "sections": best_landing.get("Section Order", "Hero > Features > CTA"),
                "cta_placement": best_landing.get("Primary CTA Placement", "Above fold"),
                "color_strategy": best_landing.get("Color Strategy", ""),
                "conversion": best_landing.get("Conversion Optimization", "")
            },
            "style": {
                "name": best_style.get("Style Category", "Minimalism"),
                "type": best_style.get("Type", "General"),
                "effects": style_effects,
                "keywords": best_style.get("Keywords", ""),
                "best_for": best_style.get("Best For", ""),
                "performance": best_style.get("Performance", ""),
                "accessibility": best_style.get("Accessibility", ""),
                "css_keywords": best_style.get("CSS/Technical Keywords", ""),
                "checklist": best_style.get("Implementation Checklist", ""),
                "design_system_vars": best_style.get("Design System Variables", "")
            },
            "colors": {
                "primary": primary_hex,
                "secondary": secondary_hex,
                "cta": cta_hex,
                "background": bg_hex,
                "text": text_hex,
                "border": border_hex,
                "notes": best_color.get("Notes", ""),
                "extended": extended_palette,
                "contrast": {
                    "primary_on_bg": f"{contrast_primary_on_bg}:1",
                    "text_on_bg": f"{contrast_text_on_bg}:1",
                    "wcag_aa": contrast_text_on_bg >= 4.5,
                    "wcag_aaa": contrast_text_on_bg >= 7,
                }
            },
            "typography": {
                "heading": best_typography.get("Heading Font", "Inter"),
                "body": best_typography.get("Body Font", "Inter"),
                "mood": best_typography.get("Mood/Style Keywords", reasoning.get("typography_mood", "")),
                "best_for": best_typography.get("Best For", ""),
                "google_fonts_url": best_typography.get("Google Fonts URL", ""),
                "css_import": best_typography.get("CSS Import", ""),
                "tailwind_config": best_typography.get("Tailwind Config", "")
            },
            "key_effects": combined_effects,
            "anti_patterns": reasoning.get("anti_patterns", ""),
            "decision_rules": reasoning.get("decision_rules", {}),
            "severity": reasoning.get("severity", "MEDIUM"),
            "components": component_results[:5] if component_results else [],
            "component_specs": self._generate_component_specs(component_results),
            "animations": animation_results[:3] if animation_results else [],
            "responsive": responsive_results[:3] if responsive_results else [],
            "tokens": token_results[:2] if token_results else [],
            "backgrounds": background_results[:3] if background_results else [],
            "code_snippets": None,
        }

        design_system["code_snippets"] = self._generate_code_snippets(design_system)

        return design_system


# ============ OUTPUT FORMATTERS V2 ============
BOX_WIDTH = 100

def wrap_text(text, prefix, width):
    if not text:
        return []
    words = text.split()
    lines = []
    current = prefix
    for word in words:
        # Unbreakable tokens (URLs) longer than a full line get hard-split
        # into width-sized chunks, otherwise they overflow the box border.
        if len(prefix) + len(word) > width - 2:
            chunk = width - 2 - len(prefix)
            if chunk < 8:
                chunk = 8
            pieces = [word[i:i + chunk] for i in range(0, len(word), chunk)]
            for piece in pieces:
                if current != prefix:
                    lines.append(current)
                current = prefix + piece
            continue
        if len(current) + len(word) + 1 <= width - 2:
            current += (" " if current != prefix else "") + word
        else:
            if current != prefix:
                lines.append(current)
            current = prefix + word
    if current != prefix:
        lines.append(current)
    return lines


def format_ascii_box(design_system):
    """Format design system as ASCII box v2 with enhanced output."""
    project = design_system.get("project_name", "PROJECT")
    pattern = design_system.get("pattern", {})
    style = design_system.get("style", {})
    colors = design_system.get("colors", {})
    typography = design_system.get("typography", {})
    effects = design_system.get("key_effects", "")
    anti_patterns = design_system.get("anti_patterns", "")
    components = design_system.get("components", [])
    animations = design_system.get("animations", [])
    responsive = design_system.get("responsive", [])
    backgrounds = design_system.get("backgrounds", [])
    code = design_system.get("code_snippets", {})

    lines = []
    w = BOX_WIDTH + 1  # aligns borders with the 103-char content/blank rows

    lines.append("+" + "=" * w + "+")
    lines.append(f"||  UI UX CR v2 - DESIGN SYSTEM: {project}".ljust(BOX_WIDTH + 1) + "||")
    lines.append(f"||  Category: {design_system.get('category', 'General')}".ljust(BOX_WIDTH + 1) + "||")
    lines.append("+" + "=" * w + "+")
    lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    contrast_info = colors.get("contrast", {})
    contrast_line = ""
    if contrast_info:
        contrast_line = f"Contrast: Text/Bg {contrast_info.get('text_on_bg', 'N/A')} | WCAG AA: {'PASS' if contrast_info.get('wcag_aa') else 'FAIL'}"

    # Pattern
    lines.append(f"||  PATTERN: {pattern.get('name', '')}".ljust(BOX_WIDTH + 1) + "||")
    if pattern.get('conversion'):
        lines.append(f"||     Conversion: {pattern.get('conversion', '')}".ljust(BOX_WIDTH + 1) + "||")
    if pattern.get('cta_placement'):
        lines.append(f"||     CTA: {pattern.get('cta_placement', '')}".ljust(BOX_WIDTH + 1) + "||")
    lines.append("||     Sections:".ljust(BOX_WIDTH + 1) + "||")
    sections = pattern.get("sections", "").split(">")
    for i, section in enumerate([s.strip() for s in sections if s.strip()], 1):
        lines.append(f"||       {i}. {section}".ljust(BOX_WIDTH + 1) + "||")
    lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Style
    lines.append(f"||  STYLE: {style.get('name', '')}".ljust(BOX_WIDTH + 1) + "||")
    if style.get("keywords"):
        for line in wrap_text(f"Keywords: {style.get('keywords', '')}", "||     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH + 1) + "||")
    if style.get("best_for"):
        for line in wrap_text(f"Best For: {style.get('best_for', '')}", "||     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH + 1) + "||")
    if style.get("performance") or style.get("accessibility"):
        perf = f"Performance: {style.get('performance', '')} | Accessibility: {style.get('accessibility', '')}"
        lines.append(f"||     {perf}".ljust(BOX_WIDTH + 1) + "||")
    lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Colors
    lines.append("||  COLORS:".ljust(BOX_WIDTH + 1) + "||")
    lines.append(f"||     Primary:    {colors.get('primary', '')}".ljust(BOX_WIDTH + 1) + "||")
    lines.append(f"||     Secondary:  {colors.get('secondary', '')}".ljust(BOX_WIDTH + 1) + "||")
    lines.append(f"||     CTA:        {colors.get('cta', '')}".ljust(BOX_WIDTH + 1) + "||")
    lines.append(f"||     Background: {colors.get('background', '')}".ljust(BOX_WIDTH + 1) + "||")
    lines.append(f"||     Text:       {colors.get('text', '')}".ljust(BOX_WIDTH + 1) + "||")
    lines.append(f"||     Border:     {colors.get('border', '')}".ljust(BOX_WIDTH + 1) + "||")
    if contrast_line:
        lines.append(f"||     {contrast_line}".ljust(BOX_WIDTH + 1) + "||")
    if colors.get("notes"):
        for line in wrap_text(f"Notes: {colors.get('notes', '')}", "||     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH + 1) + "||")

    extended = colors.get("extended", {})
    if extended:
        lines.append("||     Extended Palette (50-900):".ljust(BOX_WIDTH + 1) + "||")
        for key, value in list(extended.items())[:6]:
            lines.append(f"||       {key}: {value}".ljust(BOX_WIDTH + 1) + "||")
    lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Typography
    heading_f = typography.get("heading", "Inter")
    body_f = typography.get("body", "Inter")
    lines.append(f"||  TYPOGRAPHY: {heading_f} (headings) / {body_f} (body)".ljust(BOX_WIDTH + 1) + "||")
    if typography.get("mood"):
        for line in wrap_text(f"Mood: {typography.get('mood', '')}", "||     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH + 1) + "||")
    if typography.get("google_fonts_url"):
        for gf_line in wrap_text(f"Google Fonts: {typography.get('google_fonts_url', '')}", "||     ", BOX_WIDTH):
            lines.append(gf_line.ljust(BOX_WIDTH + 1) + "||")
    lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Effects
    if effects:
        lines.append("||  KEY EFFECTS:".ljust(BOX_WIDTH + 1) + "||")
        for line in wrap_text(effects, "||     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH + 1) + "||")
        lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Code Snippet (Button)
    if code and code.get("button"):
        lines.append("||  CODE SNIPPET (Button):".ljust(BOX_WIDTH + 1) + "||")
        btn_code = code["button"].replace("\n", " ")[:BOX_WIDTH-10]
        lines.append(f"||     {btn_code}".ljust(BOX_WIDTH + 1) + "||")
        lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # CSS Variables
    if code and code.get("css_variables"):
        lines.append("||  CSS CUSTOM PROPERTIES:".ljust(BOX_WIDTH + 1) + "||")
        css_lines = code["css_variables"].split("\n")
        for cl in css_lines[:4]:
            cl = cl.strip()
            if cl:
                lines.append(f"||     {cl}".ljust(BOX_WIDTH + 1) + "||")
        lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Components
    if components:
        lines.append("||  RECOMMENDED COMPONENTS:".ljust(BOX_WIDTH + 1) + "||")
        for comp in components[:5]:
            comp_name = comp.get("Component", "")
            comp_variants = comp.get("Variants", "")
            comp_tailwind = comp.get("Tailwind", "")
            lines.append(f"||     - {comp_name}".ljust(BOX_WIDTH + 1) + "||")
            if comp_variants:
                lines.append(f"||       Variants: {comp_variants}".ljust(BOX_WIDTH + 1) + "||")
            if comp_tailwind:
                tw_short = comp_tailwind[:60]
                lines.append(f"||       Tailwind: {tw_short}".ljust(BOX_WIDTH + 1) + "||")
        lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Animations
    if animations:
        lines.append("||  RECOMMENDED ANIMATIONS:".ljust(BOX_WIDTH + 1) + "||")
        for anim in animations[:3]:
            anim_name = anim.get("Animation", "")
            anim_dur = anim.get("Duration", "")
            anim_ease = anim.get("Easing", "")
            lines.append(f"||     - {anim_name} ({anim_dur}, {anim_ease})".ljust(BOX_WIDTH + 1) + "||")
        lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Responsive
    if responsive:
        lines.append("||  RESPONSIVE PATTERNS:".ljust(BOX_WIDTH + 1) + "||")
        for resp in responsive[:3]:
            resp_name = resp.get("Pattern", "")
            resp_breakpoints = resp.get("Breakpoints", "")
            lines.append(f"||     - {resp_name}".ljust(BOX_WIDTH + 1) + "||")
            if resp_breakpoints:
                lines.append(f"||       Breakpoints: {resp_breakpoints}".ljust(BOX_WIDTH + 1) + "||")
        lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Backgrounds
    if backgrounds:
        lines.append("||  RECOMMENDED BACKGROUNDS:".ljust(BOX_WIDTH + 1) + "||")
        for bg in backgrounds[:3]:
            bg_name = bg.get("Background Name", "")
            bg_cat = bg.get("Category", "")
            lines.append(f"||     - {bg_name} ({bg_cat})".ljust(BOX_WIDTH + 1) + "||")
        lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Anti-patterns
    if anti_patterns:
        lines.append("||  AVOID (Anti-patterns):".ljust(BOX_WIDTH + 1) + "||")
        for line in wrap_text(anti_patterns, "||     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH + 1) + "||")
        lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    # Checklist
    lines.append("||  PRE-DELIVERY CHECKLIST:".ljust(BOX_WIDTH + 1) + "||")
    checklist = [
        "[ ] No emojis as icons (use SVG: Heroicons/Lucide)",
        "[ ] cursor-pointer on all clickable elements",
        "[ ] Hover states with smooth transitions (150-300ms)",
        "[ ] Light mode: text contrast 4.5:1 minimum",
        "[ ] Focus states visible for keyboard nav",
        "[ ] prefers-reduced-motion respected",
        "[ ] Responsive: 375px, 768px, 1024px, 1440px",
        "[ ] Dark mode tested",
        "[ ] Loading states implemented",
        "[ ] Error states handled",
        "[ ] Empty states designed",
    ]
    for item in checklist:
        lines.append(f"||     {item}".ljust(BOX_WIDTH + 1) + "||")
    lines.append("||" + " " * (BOX_WIDTH - 1) + "||")

    lines.append("+" + "=" * w + "+")

    return "\n".join(lines)


def format_markdown(design_system):
    """Format design system as enhanced markdown v2."""
    project = design_system.get("project_name", "PROJECT")
    pattern = design_system.get("pattern", {})
    style = design_system.get("style", {})
    colors = design_system.get("colors", {})
    typography = design_system.get("typography", {})
    effects = design_system.get("key_effects", "")
    anti_patterns = design_system.get("anti_patterns", "")
    components = design_system.get("components", [])
    animations = design_system.get("animations", [])
    responsive = design_system.get("responsive", [])
    code = design_system.get("code_snippets", {})

    lines = []
    lines.append(f"# Design System: {project}")
    lines.append("")
    lines.append("*Generated by UI UX CR v2 - Cyber-Rage Design Intelligence Engine*")
    lines.append("")

    # Pattern
    lines.append("## Pattern")
    lines.append(f"- **Name:** {pattern.get('name', '')}")
    if pattern.get('conversion'):
        lines.append(f"- **Conversion Focus:** {pattern.get('conversion', '')}")
    if pattern.get('cta_placement'):
        lines.append(f"- **CTA Placement:** {pattern.get('cta_placement', '')}")
    if pattern.get('color_strategy'):
        lines.append(f"- **Color Strategy:** {pattern.get('color_strategy', '')}")
    lines.append(f"- **Sections:** {pattern.get('sections', '')}")
    lines.append("")

    # Style
    lines.append("## Style")
    lines.append(f"- **Name:** {style.get('name', '')}")
    if style.get('keywords'):
        lines.append(f"- **Keywords:** {style.get('keywords', '')}")
    if style.get('best_for'):
        lines.append(f"- **Best For:** {style.get('best_for', '')}")
    if style.get('performance') or style.get('accessibility'):
        lines.append(f"- **Performance:** {style.get('performance', '')} | **Accessibility:** {style.get('accessibility', '')}")
    lines.append("")

    # Colors
    lines.append("## Colors")
    lines.append("| Role | Hex |")
    lines.append("|------|-----|")
    lines.append(f"| Primary | `{colors.get('primary', '')}` |")
    lines.append(f"| Secondary | `{colors.get('secondary', '')}` |")
    lines.append(f"| CTA | `{colors.get('cta', '')}` |")
    lines.append(f"| Background | `{colors.get('background', '')}` |")
    lines.append(f"| Text | `{colors.get('text', '')}` |")
    lines.append(f"| Border | `{colors.get('border', '')}` |")

    contrast_info = colors.get("contrast", {})
    if contrast_info:
        lines.append("")
        lines.append("### Contrast Check")
        lines.append(f"- **Text on Background:** {contrast_info.get('text_on_bg', 'N/A')}")
        lines.append(f"- **WCAG AA (4.5:1):** {'PASS' if contrast_info.get('wcag_aa') else 'FAIL'}")
        lines.append(f"- **WCAG AAA (7:1):** {'PASS' if contrast_info.get('wcag_aaa') else 'FAIL'}")

    if colors.get("notes"):
        lines.append(f"\n*Notes: {colors.get('notes', '')}*")
    lines.append("")

    extended = colors.get("extended", {})
    if extended:
        lines.append("### Extended Palette")
        lines.append("| Token | Hex |")
        lines.append("|-------|-----|")
        for key, value in extended.items():
            lines.append(f"| {key} | `{value}` |")
        lines.append("")

    # Typography
    lines.append("## Typography")
    lines.append(f"- **Heading:** {typography.get('heading', '')}")
    lines.append(f"- **Body:** {typography.get('body', '')}")
    if typography.get("mood"):
        lines.append(f"- **Mood:** {typography.get('mood', '')}")
    if typography.get("google_fonts_url"):
        lines.append(f"- **Google Fonts:** [{typography.get('heading', '')} + {typography.get('body', '')}]({typography.get('google_fonts_url', '')})")
    if typography.get("css_import"):
        lines.append(f"\n**CSS Import:**")
        lines.append(f"```css")
        lines.append(f"{typography.get('css_import', '')}")
        lines.append(f"```")
    lines.append("")

    # CSS Variables
    if code and code.get("css_variables"):
        lines.append("## CSS Custom Properties")
        lines.append("```css")
        lines.append(code["css_variables"])
        lines.append("```")
        lines.append("")

    # Code Snippets
    if code:
        lines.append("## Code Snippets")
        if code.get("button"):
            lines.append("### Button")
            lines.append("```html")
            lines.append(code["button"])
            lines.append("```")
        if code.get("card"):
            lines.append("### Card")
            lines.append("```html")
            lines.append(code["card"])
            lines.append("```")
        lines.append("")

    # Components
    if components:
        lines.append("## Recommended Components")
        for comp in components[:5]:
            lines.append(f"### {comp.get('Component', '')}")
            if comp.get('Variants'):
                lines.append(f"- **Variants:** {comp.get('Variants', '')}")
            if comp.get('Tailwind'):
                lines.append(f"- **Tailwind:** `{comp.get('Tailwind', '')}`")
            if comp.get('Accessibility'):
                lines.append(f"- **Accessibility:** {comp.get('Accessibility', '')}")
            lines.append("")

    # Animations (with code)
    if animations:
        lines.append("## Recommended Animations")
        for anim in animations[:3]:
            lines.append(f"### {anim.get('Animation', '')}")
            if anim.get('Duration'):
                lines.append(f"- **Duration:** {anim.get('Duration', '')}")
            if anim.get('Easing'):
                lines.append(f"- **Easing:** {anim.get('Easing', '')}")
            if anim.get('CSS Code'):
                lines.append(f"\n```css")
                lines.append(f"{anim.get('CSS Code', '')}")
                lines.append(f"```")
            lines.append("")

    # Responsive
    if responsive:
        lines.append("## Responsive Patterns")
        for resp in responsive[:3]:
            lines.append(f"### {resp.get('Pattern', '')}")
            if resp.get('Breakpoints'):
                lines.append(f"- **Breakpoints:** {resp.get('Breakpoints', '')}")
            if resp.get('Tailwind'):
                lines.append(f"- **Tailwind:** `{resp.get('Tailwind', '')}`")
            lines.append("")

    # Effects
    if effects:
        lines.append("## Key Effects")
        lines.append(f"{effects}")
        lines.append("")

    # Anti-patterns
    if anti_patterns:
        lines.append("## Avoid (Anti-patterns)")
        anti_list = [a.strip() for a in anti_patterns.split("+") if a.strip()]
        for anti in anti_list:
            lines.append(f"- {anti}")
        lines.append("")

    # Checklist
    lines.append("## Pre-Delivery Checklist")
    lines.append("- [ ] No emojis as icons (use SVG: Heroicons/Lucide)")
    lines.append("- [ ] cursor-pointer on all clickable elements")
    lines.append("- [ ] Hover states with smooth transitions (150-300ms)")
    lines.append("- [ ] Light mode: text contrast 4.5:1 minimum")
    lines.append("- [ ] Focus states visible for keyboard navigation")
    lines.append("- [ ] prefers-reduced-motion respected")
    lines.append("- [ ] Responsive: 375px, 768px, 1024px, 1440px")
    lines.append("- [ ] Dark mode tested")
    lines.append("- [ ] Loading states implemented")
    lines.append("- [ ] Error states handled")
    lines.append("- [ ] Empty states designed")
    lines.append("")

    return "\n".join(lines)


# ============ MAIN ENTRY POINT ============
def generate_design_system(query, project_name=None, output_format="ascii",
                           persist=False, page=None, output_dir=None):
    generator = DesignSystemGenerator()
    design_system = generator.generate(query, project_name)

    if persist:
        persist_design_system(design_system, page, output_dir, query)

    if output_format == "markdown":
        return format_markdown(design_system)
    return format_ascii_box(design_system)


# ============ PERSISTENCE FUNCTIONS ============
def persist_design_system(design_system, page=None, output_dir=None, page_query=None):
    base_dir = Path(output_dir) if output_dir else Path.cwd()

    project_name = design_system.get("project_name", "default")
    project_slug = project_name.lower().replace(' ', '-')

    design_system_dir = base_dir / "design-system" / project_slug
    pages_dir = design_system_dir / "pages"

    created_files = []

    design_system_dir.mkdir(parents=True, exist_ok=True)
    pages_dir.mkdir(parents=True, exist_ok=True)

    master_file = design_system_dir / "MASTER.md"
    master_content = format_master_md(design_system)
    with open(master_file, 'w', encoding='utf-8') as f:
        f.write(master_content)
    created_files.append(str(master_file))

    if page:
        page_file = pages_dir / f"{page.lower().replace(' ', '-')}.md"
        page_content = format_page_override_md(design_system, page, page_query)
        with open(page_file, 'w', encoding='utf-8') as f:
            f.write(page_content)
        created_files.append(str(page_file))

    return {
        "status": "success",
        "design_system_dir": str(design_system_dir),
        "created_files": created_files
    }


def format_master_md(design_system):
    """Format design system as MASTER.md v2 with enhanced content."""
    project = design_system.get("project_name", "PROJECT")
    pattern = design_system.get("pattern", {})
    style = design_system.get("style", {})
    colors = design_system.get("colors", {})
    typography = design_system.get("typography", {})
    effects = design_system.get("key_effects", "")
    anti_patterns = design_system.get("anti_patterns", "")
    code = design_system.get("code_snippets", {})

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []

    lines.append("# Design System Master File")
    lines.append("")
    lines.append("> **LOGIC:** When building a specific page, first check `design-system/<project-slug>/pages/[page-name].md`.")
    lines.append("> If that file exists, its rules **override** this Master file.")
    lines.append("> If not, strictly follow the rules below.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"**Project:** {project}")
    lines.append(f"**Generated:** {timestamp}")
    lines.append(f"**Category:** {design_system.get('category', 'General')}")
    lines.append(f"**Engine:** UI UX CR v2 - Cyber-Rage Design Intelligence Engine")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Color Palette
    lines.append("## Color Palette")
    lines.append("")
    lines.append("| Role | Hex | CSS Variable |")
    lines.append("|------|-----|--------------|")
    lines.append(f"| Primary | `{colors.get('primary', '#2563EB')}` | `--color-primary` |")
    lines.append(f"| Secondary | `{colors.get('secondary', '#3B82F6')}` | `--color-secondary` |")
    lines.append(f"| CTA/Accent | `{colors.get('cta', '#F97316')}` | `--color-cta` |")
    lines.append(f"| Background | `{colors.get('background', '#F8FAFC')}` | `--color-background` |")
    lines.append(f"| Text | `{colors.get('text', '#1E293B')}` | `--color-text` |")
    lines.append(f"| Border | `{colors.get('border', '#E2E8F0')}` | `--color-border` |")
    lines.append("")

    # Contrast info
    contrast_info = colors.get("contrast", {})
    if contrast_info:
        lines.append("**Accessibility Check:**")
        lines.append(f"- Text/Bg contrast: {contrast_info.get('text_on_bg', 'N/A')} (WCAG AA: {'PASS' if contrast_info.get('wcag_aa') else 'FAIL'})")
        lines.append("")

    # Extended Palette
    extended = colors.get("extended", {})
    if extended:
        lines.append("### Extended Palette")
        lines.append("")
        lines.append("| Token | Hex | CSS Variable |")
        lines.append("|-------|-----|--------------|")
        for key, value in extended.items():
            lines.append(f"| {key} | `{value}` | `--{key}` |")
        lines.append("")

    if colors.get("notes"):
        lines.append(f"**Color Notes:** {colors.get('notes', '')}")
        lines.append("")

    # Typography
    lines.append("## Typography")
    lines.append("")
    lines.append(f"- **Heading Font:** {typography.get('heading', 'Inter')}")
    lines.append(f"- **Body Font:** {typography.get('body', 'Inter')}")
    if typography.get("mood"):
        lines.append(f"- **Mood:** {typography.get('mood', '')}")
    if typography.get("google_fonts_url"):
        lines.append(f"- **Google Fonts:** [{typography.get('heading', '')} + {typography.get('body', '')}]({typography.get('google_fonts_url', '')})")
    lines.append("")
    if typography.get("css_import"):
        lines.append("**CSS Import:**")
        lines.append("```css")
        lines.append(typography.get("css_import", ""))
        lines.append("```")
        lines.append("")

    # CSS Custom Properties
    if code and code.get("css_variables"):
        lines.append("## CSS Custom Properties")
        lines.append("```css")
        lines.append(code["css_variables"])
        lines.append("```")
        lines.append("")

    # Spacing Variables
    lines.append("## Spacing Variables")
    lines.append("")
    lines.append("| Token | Value | Usage |")
    lines.append("|-------|-------|-------|")
    lines.append("| `--space-xs` | `4px` / `0.25rem` | Tight gaps |")
    lines.append("| `--space-sm` | `8px` / `0.5rem` | Icon gaps, inline spacing |")
    lines.append("| `--space-md` | `16px` / `1rem` | Standard padding |")
    lines.append("| `--space-lg` | `24px` / `1.5rem` | Section padding |")
    lines.append("| `--space-xl` | `32px` / `2rem` | Large gaps |")
    lines.append("| `--space-2xl` | `48px` / `3rem` | Section margins |")
    lines.append("| `--space-3xl` | `64px` / `4rem` | Hero padding |")
    lines.append("")

    # Shadow Depths
    lines.append("## Shadow Depths")
    lines.append("")
    lines.append("| Level | Value | Usage |")
    lines.append("|-------|-------|-------|")
    lines.append("| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Subtle lift |")
    lines.append("| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.1)` | Cards, buttons |")
    lines.append("| `--shadow-lg` | `0 10px 15px rgba(0,0,0,0.1)` | Modals, dropdowns |")
    lines.append("| `--shadow-xl` | `0 20px 25px rgba(0,0,0,0.15)` | Hero images |")
    lines.append("")

    # Component Specs
    lines.append("---")
    lines.append("")
    lines.append("## Component Specs")
    lines.append("")

    cta = colors.get('cta', '#F97316')
    primary = colors.get('primary', '#2563EB')
    bg = colors.get('background', '#FFFFFF')
    border = colors.get('border', '#E2E8F0')

    # Buttons
    lines.append("### Buttons")
    lines.append("")
    lines.append("```css")
    lines.append(".btn-primary {")
    lines.append(f"  background: {cta};")
    lines.append("  color: white;")
    lines.append("  padding: 12px 24px;")
    lines.append("  border-radius: 8px;")
    lines.append("  font-weight: 600;")
    lines.append("  transition: all 200ms ease;")
    lines.append("  cursor: pointer;")
    lines.append("}")
    lines.append(".btn-primary:hover {")
    lines.append("  opacity: 0.9;")
    lines.append("  transform: translateY(-1px);")
    lines.append("}")
    lines.append("")
    lines.append(".btn-secondary {")
    lines.append("  background: transparent;")
    lines.append(f"  color: {primary};")
    lines.append(f"  border: 2px solid {primary};")
    lines.append("  padding: 12px 24px;")
    lines.append("  border-radius: 8px;")
    lines.append("  font-weight: 600;")
    lines.append("  transition: all 200ms ease;")
    lines.append("  cursor: pointer;")
    lines.append("}")
    lines.append("```")
    lines.append("")

    # Cards
    lines.append("### Cards")
    lines.append("")
    lines.append("```css")
    lines.append(".card {")
    lines.append(f"  background: {bg};")
    lines.append("  border-radius: 12px;")
    lines.append("  padding: 24px;")
    lines.append("  box-shadow: var(--shadow-md);")
    lines.append("  transition: all 200ms ease;")
    lines.append("  cursor: pointer;")
    lines.append("}")
    lines.append(".card:hover {")
    lines.append("  box-shadow: var(--shadow-lg);")
    lines.append("  transform: translateY(-2px);")
    lines.append("}")
    lines.append("```")
    lines.append("")

    # Inputs
    lines.append("### Inputs")
    lines.append("")
    lines.append("```css")
    lines.append(".input {")
    lines.append("  padding: 12px 16px;")
    lines.append(f"  border: 1px solid {border};")
    lines.append("  border-radius: 8px;")
    lines.append("  font-size: 16px;")
    lines.append("  transition: border-color 200ms ease;")
    lines.append("}")
    lines.append(".input:focus {")
    lines.append(f"  border-color: {primary};")
    lines.append("  outline: none;")
    lines.append(f"  box-shadow: 0 0 0 3px {primary}20;")
    lines.append("}")
    lines.append("```")
    lines.append("")

    # Style section
    lines.append("---")
    lines.append("")
    lines.append("## Style Guidelines")
    lines.append("")
    lines.append(f"**Style:** {style.get('name', 'Minimalism')}")
    lines.append("")
    if style.get("keywords"):
        lines.append(f"**Keywords:** {style.get('keywords', '')}")
        lines.append("")
    if effects:
        lines.append(f"**Key Effects:** {effects}")
        lines.append("")

    # Layout Pattern
    lines.append("### Page Pattern")
    lines.append("")
    lines.append(f"**Pattern Name:** {pattern.get('name', '')}")
    lines.append("")
    if pattern.get('conversion'):
        lines.append(f"- **Conversion Strategy:** {pattern.get('conversion', '')}")
    if pattern.get('cta_placement'):
        lines.append(f"- **CTA Placement:** {pattern.get('cta_placement', '')}")
    lines.append(f"- **Section Order:** {pattern.get('sections', '')}")
    lines.append("")

    # Anti-Patterns
    lines.append("---")
    lines.append("")
    lines.append("## Anti-Patterns (Do NOT Use)")
    lines.append("")
    if anti_patterns:
        anti_list = [a.strip() for a in anti_patterns.split("+")]
        for anti in anti_list:
            if anti:
                lines.append(f"- {anti}")
    lines.append("")
    lines.append("### Additional Forbidden Patterns")
    lines.append("")
    lines.append("- Emojis as icons -- Use SVG icons (Heroicons, Lucide, Simple Icons)")
    lines.append("- Missing cursor:pointer -- All clickable elements must have cursor:pointer")
    lines.append("- Layout-shifting hovers -- Avoid scale transforms that shift layout")
    lines.append("- Low contrast text -- Maintain 4.5:1 minimum contrast ratio")
    lines.append("- Instant state changes -- Always use transitions (150-300ms)")
    lines.append("- Invisible focus states -- Focus states must be visible for a11y")
    lines.append("")

    # Checklist
    lines.append("---")
    lines.append("")
    lines.append("## Pre-Delivery Checklist")
    lines.append("")
    lines.append("- [ ] No emojis used as icons (use SVG instead)")
    lines.append("- [ ] All icons from consistent icon set (Heroicons/Lucide)")
    lines.append("- [ ] cursor-pointer on all clickable elements")
    lines.append("- [ ] Hover states with smooth transitions (150-300ms)")
    lines.append("- [ ] Light mode: text contrast 4.5:1 minimum")
    lines.append("- [ ] Focus states visible for keyboard navigation")
    lines.append("- [ ] prefers-reduced-motion respected")
    lines.append("- [ ] Responsive: 375px, 768px, 1024px, 1440px")
    lines.append("- [ ] No content hidden behind fixed navbars")
    lines.append("- [ ] No horizontal scroll on mobile")
    lines.append("- [ ] Dark mode tested")
    lines.append("- [ ] Loading states implemented")
    lines.append("- [ ] Error states handled")
    lines.append("- [ ] Empty states designed")
    lines.append("")

    return "\n".join(lines)


def format_page_override_md(design_system, page_name, page_query=None):
    """Format a page-specific override file with intelligent AI-generated content."""
    project = design_system.get("project_name", "PROJECT")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    page_title = page_name.replace("-", " ").replace("_", " ").title()

    page_overrides = _generate_intelligent_overrides(page_name, page_query, design_system)

    lines = []

    lines.append(f"# {page_title} Page Overrides")
    lines.append("")
    lines.append(f"> **PROJECT:** {project}")
    lines.append(f"> **Generated:** {timestamp}")
    lines.append(f"> **Page Type:** {page_overrides.get('page_type', 'General')}")
    lines.append("")
    lines.append("> IMPORTANT: Rules in this file **override** the Master file (`design-system/<project-slug>/MASTER.md`).")
    lines.append("> Only deviations from the Master are documented here. For all other rules, refer to the Master.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Page-Specific Rules")
    lines.append("")

    lines.append("### Layout Overrides")
    lines.append("")
    layout = page_overrides.get("layout", {})
    if layout:
        for key, value in layout.items():
            lines.append(f"- **{key}:** {value}")
    else:
        lines.append("- No overrides -- use Master layout")
    lines.append("")

    lines.append("### Spacing Overrides")
    lines.append("")
    spacing = page_overrides.get("spacing", {})
    if spacing:
        for key, value in spacing.items():
            lines.append(f"- **{key}:** {value}")
    else:
        lines.append("- No overrides -- use Master spacing")
    lines.append("")

    lines.append("### Typography Overrides")
    lines.append("")
    typography = page_overrides.get("typography", {})
    if typography:
        for key, value in typography.items():
            lines.append(f"- **{key}:** {value}")
    else:
        lines.append("- No overrides -- use Master typography")
    lines.append("")

    lines.append("### Color Overrides")
    lines.append("")
    colors = page_overrides.get("colors", {})
    if colors:
        for key, value in colors.items():
            lines.append(f"- **{key}:** {value}")
    else:
        lines.append("- No overrides -- use Master colors")
    lines.append("")

    lines.append("### Component Overrides")
    lines.append("")
    components = page_overrides.get("components", [])
    if components:
        for comp in components:
            lines.append(f"- {comp}")
    else:
        lines.append("- No overrides -- use Master component specs")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Page-Specific Components")
    lines.append("")
    unique_components = page_overrides.get("unique_components", [])
    if unique_components:
        for comp in unique_components:
            lines.append(f"- {comp}")
    else:
        lines.append("- No unique components for this page")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Recommendations")
    lines.append("")
    recommendations = page_overrides.get("recommendations", [])
    if recommendations:
        for rec in recommendations:
            lines.append(f"- {rec}")
    lines.append("")

    return "\n".join(lines)


def _generate_intelligent_overrides(page_name, page_query, design_system):
    from core import search

    page_lower = page_name.lower()
    query_lower = (page_query or "").lower()
    combined_context = f"{page_lower} {query_lower}"

    style_search = search(combined_context, "style", max_results=1)
    ux_search = search(combined_context, "ux", max_results=3)
    landing_search = search(combined_context, "landing", max_results=1)

    style_results = style_search.get("results", [])
    ux_results = ux_search.get("results", [])
    landing_results = landing_search.get("results", [])

    page_type = _detect_page_type(combined_context, style_results)

    layout = {}
    spacing = {}
    typography = {}
    colors = {}
    components = []
    unique_components = []
    recommendations = []

    if style_results:
        style = style_results[0]
        keywords = style.get("Keywords", "")
        effects = style.get("Effects & Animation", "")

        if any(kw in keywords.lower() for kw in ["data", "dense", "dashboard", "grid"]):
            layout["Max Width"] = "1400px or full-width"
            layout["Grid"] = "12-column grid for data flexibility"
            spacing["Content Density"] = "High -- optimize for information display"
        elif any(kw in keywords.lower() for kw in ["minimal", "simple", "clean", "single"]):
            layout["Max Width"] = "800px (narrow, focused)"
            layout["Layout"] = "Single column, centered"
            spacing["Content Density"] = "Low -- focus on clarity"
        else:
            layout["Max Width"] = "1200px (standard)"
            layout["Layout"] = "Full-width sections, centered content"

        if effects:
            recommendations.append(f"Effects: {effects}")

    for ux in ux_results:
        category = ux.get("Category", "")
        do_text = ux.get("Do", "")
        dont_text = ux.get("Don't", "")
        if do_text:
            recommendations.append(f"{category}: {do_text}")
        if dont_text:
            components.append(f"Avoid: {dont_text}")

    if landing_results:
        landing = landing_results[0]
        sections = landing.get("Section Order", "")
        cta_placement = landing.get("Primary CTA Placement", "")
        color_strategy = landing.get("Color Strategy", "")

        if sections:
            layout["Sections"] = sections
        if cta_placement:
            recommendations.append(f"CTA Placement: {cta_placement}")
        if color_strategy:
            colors["Strategy"] = color_strategy

    if not layout:
        layout["Max Width"] = "1200px"
        layout["Layout"] = "Responsive grid"

    if not recommendations:
        recommendations = [
            "Refer to MASTER.md for all design rules",
            "Add specific overrides as needed for this page"
        ]

    return {
        "page_type": page_type,
        "layout": layout,
        "spacing": spacing,
        "typography": typography,
        "colors": colors,
        "components": components,
        "unique_components": unique_components,
        "recommendations": recommendations
    }


def _detect_page_type(context, style_results):
    context_lower = context.lower()

    page_patterns = [
        (["dashboard", "admin", "analytics", "data", "metrics", "stats", "monitor", "overview"], "Dashboard / Data View"),
        (["checkout", "payment", "cart", "purchase", "order", "billing"], "Checkout / Payment"),
        (["settings", "profile", "account", "preferences", "config"], "Settings / Profile"),
        (["landing", "marketing", "homepage", "hero", "home", "promo"], "Landing / Marketing"),
        (["login", "signin", "signup", "register", "auth", "password"], "Authentication"),
        (["pricing", "plans", "subscription", "tiers", "packages"], "Pricing / Plans"),
        (["blog", "article", "post", "news", "content", "story"], "Blog / Article"),
        (["product", "item", "detail", "pdp", "shop", "store"], "Product Detail"),
        (["search", "results", "browse", "filter", "catalog", "list"], "Search Results"),
        (["empty", "404", "error", "not found", "zero"], "Empty State"),
    ]

    for keywords, page_type in page_patterns:
        if any(kw in context_lower for kw in keywords):
            return page_type

    if style_results:
        style_name = style_results[0].get("Style Category", "").lower()
        best_for = style_results[0].get("Best For", "").lower()

        if "dashboard" in best_for or "data" in best_for:
            return "Dashboard / Data View"
        elif "landing" in best_for or "marketing" in best_for:
            return "Landing / Marketing"

    return "General"


# ============ CLI SUPPORT ============
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate Design System v2 - Cyber-Rage Engine")
    parser.add_argument("query", help="Search query (e.g., 'SaaS dashboard')")
    parser.add_argument("--project-name", "-p", type=str, default=None, help="Project name")
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"], default="ascii", help="Output format")

    args = parser.parse_args()

    result = generate_design_system(args.query, args.project_name, args.format)
    print(result)
