#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI UX CR Core v2.0 - Ultra-premium search engine with advanced BM25,
fuzzy matching, n-gram support, semantic ranking, and Persian keywords
Cyber-Rage Design Intelligence Engine
"""

import csv
import re
import json
from pathlib import Path
from math import log, sqrt
from collections import defaultdict

DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3

CSV_CONFIG = {
    "style": {
        "file": "styles.csv",
        "search_cols": ["Style Category", "Keywords", "Best For", "Type", "AI Prompt Keywords", "CSS/Technical Keywords"],
        "output_cols": ["Style Category", "Type", "Keywords", "Primary Colors", "Effects & Animation", "Best For", "Performance", "Accessibility", "Framework Compatibility", "Complexity", "AI Prompt Keywords", "CSS/Technical Keywords", "Implementation Checklist", "Design System Variables"]
    },
    "color": {
        "file": "colors.csv",
        "search_cols": ["Product Type", "Notes", "Primary (Hex)", "Secondary (Hex)"],
        "output_cols": ["Product Type", "Primary (Hex)", "Secondary (Hex)", "CTA (Hex)", "Background (Hex)", "Text (Hex)", "Border (Hex)", "Notes"]
    },
    "chart": {
        "file": "charts.csv",
        "search_cols": ["Data Type", "Keywords", "Best Chart Type", "Accessibility Notes", "Color Guidance"],
        "output_cols": ["Data Type", "Keywords", "Best Chart Type", "Secondary Options", "Color Guidance", "Accessibility Notes", "Library Recommendation", "Interactive Level"]
    },
    "landing": {
        "file": "landing.csv",
        "search_cols": ["Pattern Name", "Keywords", "Conversion Optimization", "Section Order", "Color Strategy"],
        "output_cols": ["Pattern Name", "Keywords", "Section Order", "Primary CTA Placement", "Color Strategy", "Conversion Optimization"]
    },
    "product": {
        "file": "products.csv",
        "search_cols": ["Product Type", "Keywords", "Primary Style Recommendation", "Key Considerations", "Secondary Styles"],
        "output_cols": ["Product Type", "Keywords", "Primary Style Recommendation", "Secondary Styles", "Landing Page Pattern", "Dashboard Style (if applicable)", "Color Palette Focus"]
    },
    "ux": {
        "file": "ux-guidelines.csv",
        "search_cols": ["Category", "Issue", "Description", "Platform", "Do", "Don't"],
        "output_cols": ["Category", "Issue", "Platform", "Description", "Do", "Don't", "Code Example Good", "Code Example Bad", "Severity"]
    },
    "typography": {
        "file": "typography.csv",
        "search_cols": ["Font Pairing Name", "Category", "Mood/Style Keywords", "Best For", "Heading Font", "Body Font", "Notes"],
        "output_cols": ["Font Pairing Name", "Category", "Heading Font", "Body Font", "Mood/Style Keywords", "Best For", "Google Fonts URL", "CSS Import", "Tailwind Config", "Notes"]
    },
    "icons": {
        "file": "icons.csv",
        "search_cols": ["Category", "Icon Name", "Keywords", "Best For", "Usage"],
        "output_cols": ["Category", "Icon Name", "Keywords", "Library", "Import Code", "Usage", "Best For", "Style"]
    },
    "react": {
        "file": "react-performance.csv",
        "search_cols": ["Category", "Issue", "Keywords", "Description", "Do"],
        "output_cols": ["Category", "Issue", "Platform", "Description", "Do", "Don't", "Code Example Good", "Code Example Bad", "Severity"]
    },
    "web": {
        "file": "web-interface.csv",
        "search_cols": ["Category", "Issue", "Keywords", "Description", "Do"],
        "output_cols": ["Category", "Issue", "Platform", "Description", "Do", "Don't", "Code Example Good", "Code Example Bad", "Severity"]
    },
    "component": {
        "file": "components.csv",
        "search_cols": ["Component", "Category", "Keywords", "Best For", "Variants", "Accessibility"],
        "output_cols": ["Component", "Category", "Keywords", "Variants", "CSS/Code", "Tailwind", "Accessibility", "Best For"]
    },
    "animation": {
        "file": "animations.csv",
        "search_cols": ["Animation", "Category", "Keywords", "Best For", "Duration"],
        "output_cols": ["Animation", "Category", "Keywords", "CSS Code", "Duration", "Easing", "GPU Friendly", "Reduced Motion", "Best For"]
    },
    "responsive": {
        "file": "responsive.csv",
        "search_cols": ["Pattern", "Category", "Keywords", "Best For", "Breakpoints"],
        "output_cols": ["Pattern", "Category", "Keywords", "Breakpoints", "CSS", "Tailwind", "Best For"]
    },
    "design_token": {
        "file": "design_tokens.csv",
        "search_cols": ["Token Category", "Token Name", "Keywords", "Usage", "CSS Variable"],
        "output_cols": ["Token Category", "Token Name", "Keywords", "Usage", "CSS Variable", "Tailwind", "Value Light", "Value Dark"]
    },
    "background": {
        "file": "backgrounds.csv",
        "search_cols": ["Background Name", "Category", "Keywords", "Best For", "CSS Code"],
        "output_cols": ["Background Name", "Category", "Keywords", "CSS Code", "Tailwind", "Best For", "Performance", "Accessibility"]
    }
}

STACK_CONFIG = {
    "html-tailwind": {"file": "stacks/html-tailwind.csv"},
    "react": {"file": "stacks/react.csv"},
    "nextjs": {"file": "stacks/nextjs.csv"},
    "astro": {"file": "stacks/astro.csv"},
    "vue": {"file": "stacks/vue.csv"},
    "nuxtjs": {"file": "stacks/nuxtjs.csv"},
    "nuxt-ui": {"file": "stacks/nuxt-ui.csv"},
    "svelte": {"file": "stacks/svelte.csv"},
    "swiftui": {"file": "stacks/swiftui.csv"},
    "react-native": {"file": "stacks/react-native.csv"},
    "flutter": {"file": "stacks/flutter.csv"},
    "shadcn": {"file": "stacks/shadcn.csv"},
    "jetpack-compose": {"file": "stacks/jetpack-compose.csv"},
    "angular": {"file": "stacks/angular.csv"},
    "laravel": {"file": "stacks/laravel.csv"},
    "threejs": {"file": "stacks/threejs.csv"}
}

_STACK_COLS = {
}

AVAILABLE_STACKS = list(STACK_CONFIG.keys())


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row
    return prev_row[-1]


# ============ ENHANCED BM25 V2.0 WITH ADVANCED MATCHING ============
class EnhancedBM25:
    """BM25 ranking with fuzzy matching, synonym support, n-gram analysis, and semantic boosting"""

    def __init__(self, k1=1.5, b=0.75, use_ngrams=True, use_levenshtein=True, lev_threshold=2):
        self.k1 = k1
        self.b = b
        self.use_ngrams = use_ngrams
        self.use_levenshtein = use_levenshtein
        self.lev_threshold = lev_threshold
        self.corpus = []
        self.raw_docs = []
        self.doc_lengths = []
        self.avgdl = 0
        self.idf = {}
        self.doc_freqs = defaultdict(int)
        self.N = 0
        self.vocabulary = set()
        self.synonym_map = self._build_synonym_map()
        self.category_keywords = self._build_category_keywords()

    def _build_synonym_map(self):
        """Build comprehensive synonym map 3x larger than v1"""
        return {
            "modern": ["contemporary", "current", "latest", "new", "futuristic", "cutting-edge", "modernist", "trendy", "fresh", "up-to-date", "today"],
            "minimal": ["minimalist", "clean", "simple", "basic", "essential", "stripped", "bare", "plain", "uncluttered", "streamlined", "sparse", "restrained", "reduction"],
            "dark": ["night", "midnight", "dim", "shadow", "noir", "obsidian", "black", "gloom", "shade", "twilight", "ebony", "inky", "pitch", "dark theme", "dark mode", "low light", "dark ui", "dark palette"],
            "elegant": ["sophisticated", "refined", "graceful", "classy", "premium", "luxury", "polished", "cultured", "tasteful", "distinguished", "splendid", "stylish"],
            "bold": ["strong", "powerful", "striking", "vibrant", "dynamic", "impactful", "audacious", "courageous", "daring", "forceful", "intense", "potent"],
            "soft": ["gentle", "smooth", "subtle", "muted", "calm", "peaceful", "delicate", "mild", "tender", "light", "feathery", "velvety"],
            "tech": ["technology", "digital", "cyber", "electronic", "smart", "advanced", "technical", "computing", "high-tech", "automated", "robotic", "tech-driven"],
            "creative": ["artistic", "innovative", "imaginative", "original", "unique", "experimental", "inventive", "visionary", "expressive", "ingenuity", "novel", "unconventional", "avant-garde", "progressive"],
            "professional": ["business", "corporate", "formal", "enterprise", "serious", "commercial", "official", "executive", "managerial", "organizational", "bureaucratic", "institutional"],
            "playful": ["fun", "colorful", "vibrant", "energetic", "lively", "dynamic", "whimsical", "quirky", "cheerful", "mischievous", "sportive", "frolicsome"],
            "warm": ["cozy", "comfortable", "inviting", "friendly", "approachable", "welcoming", "hospitable", "cordial", "affectionate", "tender", "homey", "snug"],
            "cool": ["fresh", "crisp", "clean", "icy", "frosty", "chill", "cooling", "refreshing", "breezy", "airy", "cold", "polar"],
            "trust": ["reliable", "secure", "safe", "credible", "dependable", "stable", "trustworthy", "honest", "faithful", "loyal", "confident", "assured"],
            "fast": ["quick", "rapid", "speedy", "instant", "immediate", "swift", "hasty", "brisk", "express", "lightning", "accelerated", "prompt"],
            "smooth": ["fluid", "seamless", "polished", "refined", "flowing", "silk", "silky", "glossy", "sleek", "velvet", "buttery", "frictionless"],
            "gradient": ["transition", "blend", "fade", "shift", "morph", "flow", "gradation", "spectrum", "continuum", "scale", "ramp", "progression", "color transition", "mesh gradient", "linear gradient", "radial gradient", "conic gradient"],
            "animation": ["motion", "movement", "transition", "effect", "dynamic", "kinetic", "animated", "moving", "active", "lively", "spirited", "vivid", "css animation", "keyframe animation", "ease", "motion design", "animation", "keyframe", "easing", "spring", "parallax", "scroll reveal", "micro interaction"],
            "responsive": ["adaptive", "flexible", "fluid", "mobile-first", "progressive", "reactive", "adjustable", "versatile", "dynamic", "elastic", "pliable", "responsive design", "mobile-friendly", "breakpoints", "responsive layout", "responsive grid", "responsive", "breakpoint", "mobile", "tablet", "grid", "flex"],
            "accessible": ["inclusive", "usable", "a11y", "universal", "barrier-free", "compliant", "approachable", "available", "open", "reachable", "obtainable"],
            "ux": ["user experience", "usability", "interaction", "interface", "user-centered", "user-friendly", "human-centered", "ergonomic", "intuitive", "user research", "design thinking", "user journey", "ux", "accessibility", "wcag", "touch", "scroll", "animation", "keyboard", "navigation", "mobile"],
            "ui": ["user interface", "visual", "design", "graphical", "front-end", "interface design", "screen design", "layout", "visual design", "frontend", "mockup", "prototype"],
            "saas": ["software as a service", "cloud", "subscription", "platform", "app", "web app", "cloud software", "online service", "hosted", "b2b software", "enterprise software", "saas", "software"],
            "ecommerce": ["e-commerce", "shop", "store", "retail", "marketplace", "commerce", "online store", "web shop", "shopping cart", "buy online", "eshop", "boutique", "buy", "cart", "product", "price", "sell"],
            "dashboard": ["admin", "panel", "control", "analytics", "overview", "monitor", "control panel", "admin panel", "reporting", "metrics", "kpi", "statistics", "data", "dashboard ui", "dashboard design", "dashboard layout"],
            "landing": ["homepage", "hero", "front page", "main page", "start page", "splash", "welcome page", "landing page", "entry page", "home", "cover", "introduction", "landing", "page", "cta", "conversion", "testimonial", "pricing", "section", "above fold"],
            "mobile": ["phone", "app", "responsive", "touch", "handheld", "portable", "smartphone", "tablet", "mobile-first", "small screen", "handheld device", "pocket"],
            "dark mode": ["night mode", "dark theme", "dark UI", "noir", "obsidian theme", "dark mode", "night theme", "low light", "dark palette", "dark scheme"],
            "glassmorphism": ["glass", "frosted", "blur", "transparent", "glassy", "glass effect", "frosted glass", "translucent", "crystalline", "see-through"],
            "neumorphism": ["soft ui", "embossed", "debossed", "soft 3d", "soft shadow", "neumorphic", "soft design", "soft interface", "soft ui"],
            "brutalism": ["raw", "stark", "bold", "industrial", "anti-design", "brutalist", "unpolished", "rough", "harsh", "unrefined"],
            "cyberpunk": ["cyber", "futuristic", "neon", "sci-fi", "tech-noir", "cyberpunk", "dystopian", "high-tech low-life", "neon noir"],
            "organic": ["natural", "biophilic", "eco", "sustainable", "green", "earthy", "biological", "living", "botanical", "nature-inspired", "eco-friendly"],
            "glass": ["transparent", "clear", "crystal", "translucent", "see-through", "frosted", "glassy", "vitreous", "crystalline", "ice"],
            "neon": ["glow", "fluorescent", "bright", "vibrant", "luminous", "radiant", "shining", "brilliant", "phosphorescent", "brightly lit"],
            "luxury": ["premium", "high-end", "exclusive", "deluxe", "opulent", "lavish", "sumptuous", "upscale", "superior", "first-class", "elite", "plush"],
            "retro": ["vintage", "classic", "nostalgic", "old-school", "throwback", "antique", "traditional", "heritage", "time-honored", "old-fashioned"],
            "futuristic": ["sci-fi", "advanced", "next-gen", "cutting-edge", "forward-thinking", "visionary", "space-age", "modernistic", "ultra-modern"],
            "healthcare": ["medical", "health", "clinical", "hospital", "patient", "wellness", "healthcare", "health-tech", "medtech", "biotech", "pharma", "therapeutic", "clinic", "doctor", "nurse", "pharmacy"],
            "fintech": ["finance", "banking", "financial", "payment", "money", "crypto", "blockchain", "trading", "investment", "wealth", "payments"],
            "gaming": ["game", "gaming", "esports", "gamer", "interactive", "entertainment", "playstation", "xbox", "console", "video game", "play"],
            "education": ["learning", "e-learning", "educational", "academic", "school", "training", "course", "university", "student", "teach", "classroom", "learn"],
            "food": ["restaurant", "culinary", "cooking", "gourmet", "dining", "cuisine", "grocery", "delivery", "kitchen", "chef", "food", "menu"],
            "travel": ["tourism", "vacation", "hotel", "flight", "destination", "adventure", "holiday", "journey", "expedition", "wanderlust", "travel", "tour", "trip"],
            "real estate": ["property", "housing", "apartment", "building", "home", "commercial", "residential", "mortgage", "realtor", "rental"],
            "fashion": ["style", "clothing", "apparel", "couture", "trendy", "garment", "wearable", "fashionable", "vogue", "wardrobe", "fashion", "boutique", "wear"],
            "startup": ["startup", "entrepreneur", "venture", "scale-up", "bootstrap", "launch", "MVP", "new business", "small business", "growth"],
            "enterprise": ["corporate", "large business", "fortune", "enterprise-grade", "scalable", "organization", "company", "firm", "conglomerate"],
            "authentication": ["login", "sign-in", "signup", "register", "auth", "password", "oauth", "sso", "login page", "authenticate"],
            "pricing": ["plans", "subscription", "tiers", "packages", "pricing table", "compare", "payments", "billing", "cost", "price"],
            "blog": ["article", "post", "content", "news", "story", "journal", "editorial", "blogging", "medium", "publication"],
            "search": ["find", "browse", "catalog", "filter", "results", "search bar", "search engine", "lookup", "query", "explore"],
            "animations": ["motion", "movement", "transition", "keyframe", "easing", "spring", "parallax", "scroll reveal", "micro-interaction"],
            "scroll": ["parallax", "scroll animation", "scroll reveal", "infinite scroll", "scroll-based", "scroll-triggered", "scroll effect"],
            "pattern": ["texture", "background pattern", "seamless", "repeat", "tile", "motif", "design pattern", "decoration"],
            "accessibility": ["a11y", "inclusive", "wcag", "screen reader", "assistive", "keyboard nav", "focus", "aria", "universal", "accessible design"],
            "forms": ["input", "field", "form", "validation", "submit", "placeholder", "label", "radio", "checkbox", "select", "textarea"],
            "navigation": ["menu", "navbar", "header", "sidebar", "nav", "breadcrumb", "tabs", "pagination", "hamburger", "drawer"],
            "interaction": ["hover", "click", "focus", "active", "gesture", "touch", "drag", "swipe", "feedback", "micro-interaction"],
            "colors": ["color palette", "scheme", "hue", "saturation", "lightness", "hex", "rgb", "hsl", "color theory", "complementary"],
            "fonts": ["typography", "typeface", "font", "serif", "sans-serif", "display", "monospace", "lettering", "text style", "font pairing"],
            "seo": ["search engine", "optimization", "meta", "ranking", "visibility", "keyword", "organic", "semantic"],
            "performance": ["speed", "optimization", "loading", "performance", "lighthouse", "core web vitals", "fast", "quick"],
            "security": ["secure", "safe", "encryption", "privacy", "protection", "cybersecurity", "data protection", "gdpr"],
            "light": ["light mode", "light theme", "bright", "white", "light ui", "light palette", "clean", "minimal", "airy"],
            "bento": ["masonry", "grid", "card grid", "dashboard", "compact", "modular", "bento grid", "bento box"],
            "hero": ["hero section", "hero image", "banner", "header", "jumbotron", "masthead", "cover", "splash"],
            "chat": ["chatbot", "conversational", "messaging", "chat ui", "message", "chat interface", "ai chat", "bot"],
            "ai": ["artificial intelligence", "machine learning", "deep learning", "neural", "intelligent", "smart", "automated", "predictive"],
            "3d": ["three.js", "webgl", "immersive", "3d model", "spatial", "depth", "threejs", "r3f", "3d graphics"],
            "wavy": ["wave", "curved", "flowing", "organic shapes", "blob", "undulating", "wavy pattern"],
            "noise": ["texture", "grain", "static", "noisy", "distressed", "rough texture", "grunge"],
            "grid": ["columns", "layout grid", "column grid", "grid system", "bootstrap grid", "css grid", "masonry grid"],
            "sidebar": ["side panel", "drawer", "side menu", "side navigation", "side bar", "aside"],
            "modal": ["dialog", "popup", "popover", "overlay", "lightbox", "modal window", "alert dialog"],
            "button": ["btn", "cta", "button", "call to action", "action button", "primary button", "button ui", "button component"],
            "card": ["card component", "card layout", "card ui", "card design", "card element", "card pattern"],
            "table": ["data table", "grid view", "list view", "tabular", "data display", "table component", "sortable table"],
            "chart": ["graph", "visualization", "chart component", "chart type", "data viz", "chart library", "chart pattern", "chart", "trend", "bar", "pie", "scatter", "heatmap", "funnel"],
            "icon": ["svg icon", "icon set", "iconography", "icon pack", "icon library", "icon component", "heroicons", "lucide"],
            "support": ["dark mode", "light mode", "theme support", "theming", "color scheme", "themeable", "theming support"],
            "rtl": ["right-to-left", "rtl support", "right-to-left languages", "persian", "arabic", "hebrew", "farsi"],
            "persian": ["farsi", "iran", "persian language", "rtl", "persian design", "persian ui", "iranian design"],
            "architecture": ["architectural", "building", "construction", "architect", "blueprint", "structural", "design system architecture"],
            "kanban": ["board", "cards", "columns", "trello-like", "project board", "task management", "agile board"],
            "timeline": ["history", "chronological", "time-based", "progress", "roadmap", "milestone", "event timeline"],
            "portfolio": ["gallery", "showcase", "work display", "project showcase", "creative portfolio", "personal website", "cv", "resume"],
            "onboarding": ["walkthrough", "guided tour", "setup wizard", "first-run", "getting started", "introduction flow"],
            "onboarding flow": ["wizard", "setup", "first time", "guided setup", "registration flow", "signup flow", "onboarding screen"],
            "loading": ["spinner", "skeleton", "progress", "loader", "loading animation", "loading state", "loading screen", "placeholder"],
            "skeleton": ["skeleton loader", "placeholder", "shimmer", "ghost element", "loading skeleton", "skeleton screen"],
            "error": ["error state", "error page", "404", "500", "error screen", "error handling", "error ui", "error message"],
            "empty": ["empty state", "no data", "empty page", "nothing to show", "placeholder", "zero state"],
            "success": ["success state", "success message", "confirmation", "done", "completed", "success animation"],
        }

    def _build_category_keywords(self):
        return {
            "realestate": ["property", "house", "apartment", "rent", "mortgage", "realtor"],
        }

    def _expand_query(self, query):
        """Expand query with synonyms for better matching"""
        tokens = self.tokenize(query)
        expanded = list(tokens)

        for token in tokens:
            for key, synonyms in self.synonym_map.items():
                key_norm = key.replace(" ", "_")
                token_norm = token.replace(" ", "_")
                if token_norm == key_norm or token_norm in [s.replace(" ", "_") for s in synonyms]:
                    expanded.extend([key] + synonyms)
                    break

        return expanded

    def tokenize(self, text):
        """Lowercase, split, remove punctuation, filter short words"""
        text = re.sub(r'[^\w\s]', ' ', str(text).lower())
        tokens = [w for w in text.split() if len(w) > 2]
        return tokens

    def _generate_ngrams(self, tokens, n=2):
        """Generate n-grams from tokens"""
        return [' '.join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]

    def fit(self, documents):
        """Build BM25 index from documents"""
        self.raw_docs = documents
        self.corpus = [self.tokenize(doc) for doc in documents]
        self.N = len(self.corpus)
        if self.N == 0:
            return
        self.doc_lengths = [len(doc) for doc in self.corpus]
        self.avgdl = sum(self.doc_lengths) / self.N

        for doc in self.corpus:
            self.vocabulary.update(doc)
            seen = set()
            for word in doc:
                if word not in seen:
                    self.doc_freqs[word] += 1
                    seen.add(word)

        for word, freq in self.doc_freqs.items():
            self.idf[word] = log((self.N - freq + 0.5) / (freq + 0.5) + 1)

    def _fuzzy_score(self, token, doc_tokens):
        """Calculate fuzzy match score between token and document tokens"""
        score = 0
        token_lower = token.lower()

        for doc_token in doc_tokens:
            doc_token_lower = doc_token.lower()

            # Exact match
            if token_lower == doc_token_lower:
                score += 3.0
            # Prefix match (e.g., "minimal" matches "minimalism")
            elif doc_token_lower.startswith(token_lower) or token_lower.startswith(doc_token_lower):
                score += 2.0
            # Contains match
            elif token_lower in doc_token_lower or doc_token_lower in token_lower:
                score += 1.5
            # Levenshtein fuzzy match
            elif self.use_levenshtein:
                dist = levenshtein_distance(token_lower[:min(len(token_lower), 6)],
                                           doc_token_lower[:min(len(doc_token_lower), 6)])
                if dist <= self.lev_threshold and dist > 0:
                    score += max(0, 1.5 - dist * 0.3)

        return score

    def score(self, query, use_synonyms=True):
        """Score all documents against query with fuzzy matching and synonym expansion"""
        query_tokens = self.tokenize(query)
        expanded_tokens = self._expand_query(query) if use_synonyms else query_tokens
        query_bigrams = self._generate_ngrams(query_tokens, 2) if self.use_ngrams else []
        query_trigrams = self._generate_ngrams(query_tokens, 3) if self.use_ngrams else []
        scores = []

        for idx, doc in enumerate(self.corpus):
            score = 0
            doc_len = self.doc_lengths[idx]
            term_freqs = defaultdict(int)
            for word in doc:
                term_freqs[word] += 1

            # Exact BM25 scoring for single tokens
            for token in query_tokens:
                if token in self.idf:
                    tf = term_freqs[token]
                    idf = self.idf[token]
                    numerator = tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                    score += idf * numerator / denominator

            # n-gram boosting
            doc_text = " ".join(doc)
            for bigram in query_bigrams:
                if bigram in doc_text:
                    score += 2.0
            for trigram in query_trigrams:
                if trigram in doc_text:
                    score += 3.0

            # Fuzzy matching for expanded tokens (synonyms)
            for token in expanded_tokens:
                if token not in query_tokens:
                    fuzzy = self._fuzzy_score(token, doc)
                    score += fuzzy * 0.7

            # Category boosting
            for cat, cat_kws in self.category_keywords.items():
                for kw in cat_kws:
                    if kw in [t.lower() for t in doc]:
                        if any(qkw in kw or kw in qkw for qkw in query_tokens):
                            score += 1.5
                        break

            scores.append((idx, score))

        return sorted(scores, key=lambda x: x[1], reverse=True)


# ============ SEARCH FUNCTIONS ============
def _load_csv(filepath):
    """Load CSV and return list of dicts"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    """Core search function using Enhanced BM25 v2"""
    if not filepath.exists():
        return []

    data = _load_csv(filepath)
    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

    bm25 = EnhancedBM25()
    bm25.fit(documents)
    ranked = bm25.score(query)

    # Threshold filtering - only return meaningful results
    if ranked and ranked[0][1] > 0:
        threshold = ranked[0][1] * 0.1
    else:
        threshold = 0

    results = []
    seen_combinations = set()
    for idx, score in ranked[:max_results]:
        if score > threshold:
            row = data[idx]
            result = {col: row.get(col, "") for col in output_cols if col in row}
            # Deduplication
            result_str = str(result)[:100]
            if result_str not in seen_combinations:
                seen_combinations.add(result_str)
                results.append(result)

    return results


def detect_domain(query):
    """Auto-detect the most relevant domain from query with weighted scoring"""
    query_lower = query.lower()

    domain_keywords = {
        "color": ["color", "palette", "hex", "#", "rgb", "hsl", "scheme", "hue", "saturation", "shade", "tint"],
        "product": ["saas", "ecommerce", "e-commerce", "fintech", "healthcare", "gaming", "portfolio", "crypto", "dashboard", "app", "platform", "product type"],
        "style": ["style", "design", "ui", "minimalism", "glassmorphism", "neumorphism", "brutalism", "dark mode", "flat", "aurora", "prompt", "css", "implementation", "variable", "checklist", "tailwind", "theme", "visual", "cyberpunk", "3d"],
        "typography": ["font", "typography", "heading", "serif", "sans", "typeface", "lettering", "text", "font pairing", "google fonts"],
        "icons": ["icon", "icons", "lucide", "heroicons", "symbol", "glyph", "pictogram", "svg icon", "icon set", "iconography"],
        "react": ["react", "next.js", "nextjs", "suspense", "memo", "usecallback", "useeffect", "rerender", "bundle", "waterfall", "barrel", "dynamic import", "rsc", "server component"],
        "web": ["aria", "focus", "outline", "semantic", "virtualize", "autocomplete", "form", "input type", "preconnect", "viewport"],
        "component": ["component", "button", "card", "modal", "dropdown", "input", "form", "widget", "element", "building block", "component library"],
        "design_token": ["token", "design system", "variable", "css variable", "spacing", "shadow", "border radius", "color token", "design token"],
        "background": ["background", "gradient", "pattern", "texture", "mesh", "aurora", "noise", "dot", "grid", "wave", "hexagon", "crt", "scanlines", "neon", "glow", "blob", "parallax", "video bg", "particles"]
    }

    scores = {}
    for domain, keywords in domain_keywords.items():
        score = 0
        for kw in keywords:
            if kw in query_lower:
                # Exact phrase matches get higher weight
                if " " in kw and kw in query_lower:
                    score += 3
                else:
                    score += 1
        scores[domain] = score

    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "style"


def search(query, domain=None, max_results=MAX_RESULTS):
    """Main search function with auto-domain detection"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["style"])
    filepath = DATA_DIR / config["file"]

    if not filepath.exists():
        return {"error": f"File not found: {filepath}", "domain": domain}

    results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)

    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results
    }


def search_stack(query, stack, max_results=MAX_RESULTS):
    """Search stack-specific guidelines"""
    if stack not in STACK_CONFIG:
        return {"error": f"Unknown stack: {stack}. Available: {', '.join(AVAILABLE_STACKS)}"}

    filepath = DATA_DIR / STACK_CONFIG[stack]["file"]

    if not filepath.exists():
        return {"error": f"Stack file not found: {filepath}", "stack": stack}

    results = _search_csv(filepath, _STACK_COLS["search_cols"], _STACK_COLS["output_cols"], query, max_results)

    return {
        "domain": "stack",
        "stack": stack,
        "query": query,
        "file": STACK_CONFIG[stack]["file"],
        "count": len(results),
        "results": results
    }


def multi_search(query, domains=None, max_results=MAX_RESULTS):
    """Search across multiple domains simultaneously"""
    if domains is None:
        domains = ["style", "color", "typography", "product", "landing"]

    results = {}
    for domain in domains:
        results[domain] = search(query, domain, max_results)
    return {"query": query, "results": results}
