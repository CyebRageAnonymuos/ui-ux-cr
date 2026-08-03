<div align="center">

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    CYBER-RAGE ANIMATED HEADER                  -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<svg width="100%" height="300" viewBox="0 0 1200 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0a0f"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1a0b2e"/>
    </linearGradient>

    <linearGradient id="neonCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5ff"/>
      <stop offset="50%" stop-color="#22d3ee"/>
      <stop offset="100%" stop-color="#00f5ff"/>
    </linearGradient>

    <linearGradient id="neonPink" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff00ff"/>
      <stop offset="50%" stop-color="#f472b6"/>
      <stop offset="100%" stop-color="#ff00ff"/>
    </linearGradient>

    <linearGradient id="neonOrange" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff6b35"/>
      <stop offset="50%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#ff6b35"/>
    </linearGradient>

    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="strongGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="coloredBlur"/>
      <feGaussianBlur stdDeviation="3" result="coloredBlur2"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="coloredBlur2"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(0,245,255,0.08)" stroke-width="0.5"/>
    </pattern>

    <mask id="textMask">
      <rect x="0" y="0" width="1200" height="300" fill="white"/>
    </mask>
  </defs>

  <!-- Background -->
  <rect width="1200" height="300" fill="url(#bgGrad)"/>
  <rect width="1200" height="300" fill="url(#grid)"/>

  <!-- Animated circuit lines -->
  <g opacity="0.3">
    <path d="M0,150 L200,150 L250,100 L400,100" fill="none" stroke="#00f5ff" stroke-width="1.5" stroke-dasharray="10,5">
      <animate attributeName="stroke-dashoffset" values="0;-30" dur="2s" repeatCount="indefinite"/>
    </path>
    <path d="M1200,200 L1000,200 L950,250 L800,250" fill="none" stroke="#ff00ff" stroke-width="1.5" stroke-dasharray="10,5">
      <animate attributeName="stroke-dashoffset" values="0;-30" dur="2.5s" repeatCount="indefinite"/>
    </path>
    <path d="M100,300 L100,250 L150,220 L150,150" fill="none" stroke="#f97316" stroke-width="1.5" stroke-dasharray="8,4">
      <animate attributeName="stroke-dashoffset" values="0;-24" dur="3s" repeatCount="indefinite"/>
    </path>
    <path d="M1100,0 L1100,50 L1050,80 L1050,150" fill="none" stroke="#22d3ee" stroke-width="1.5" stroke-dasharray="8,4">
      <animate attributeName="stroke-dashoffset" values="0;-24" dur="2.2s" repeatCount="indefinite"/>
    </path>
  </g>

  <!-- Floating particles -->
  <g>
    <circle cx="150" cy="80" r="2" fill="#00f5ff" opacity="0.8">
      <animate attributeName="cy" values="80;60;80" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0.2;0.8" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1050" cy="220" r="2" fill="#ff00ff" opacity="0.6">
      <animate attributeName="cy" values="220;200;220" dur="3.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;0.1;0.6" dur="3.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="600" cy="40" r="1.5" fill="#f97316" opacity="0.7">
      <animate attributeName="cy" values="40;30;40" dur="5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0.1;0.7" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="300" cy="260" r="2" fill="#22d3ee" opacity="0.5">
      <animate attributeName="cy" values="260;240;260" dur="4.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="900" cy="70" r="1.5" fill="#00f5ff" opacity="0.6">
      <animate attributeName="cy" values="70;55;70" dur="3.8s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Hexagon decorations -->
  <g opacity="0.15" stroke="#00f5ff" fill="none" stroke-width="1">
    <polygon points="100,150 115,141 115,123 100,114 85,123 85,141">
      <animateTransform attributeName="transform" type="rotate" values="0 100 132;360 100 132" dur="20s" repeatCount="indefinite"/>
    </polygon>
    <polygon points="1100,150 1115,141 1115,123 1100,114 1085,123 1085,141">
      <animateTransform attributeName="transform" type="rotate" values="360 1100 132;0 1100 132" dur="25s" repeatCount="indefinite"/>
    </polygon>
  </g>

  <!-- Main Title -->
  <text x="600" y="115" text-anchor="middle" font-family="monospace, Courier New, sans-serif" font-size="52" font-weight="900" fill="url(#neonCyan)" filter="url(#strongGlow)" letter-spacing="8">
    UI UX CR
    <animate attributeName="opacity" values="1;0.85;1" dur="3s" repeatCount="indefinite"/>
  </text>

  <!-- Subtitle with typing effect -->
  <text x="600" y="155" text-anchor="middle" font-family="monospace, Courier New, sans-serif" font-size="18" fill="#94a3b8" letter-spacing="6">
    CYBER-RAGE DESIGN INTELLIGENCE ENGINE
    <animate attributeName="opacity" values="0.6;1;0.6" dur="4s" repeatCount="indefinite"/>
  </text>

  <!-- Animated underline -->
  <line x1="350" y1="175" x2="850" y2="175" stroke="url(#neonPink)" stroke-width="2" filter="url(#glow)">
    <animate attributeName="x1" values="350;450;350" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="x2" values="850;750;850" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="stroke-width" values="2;4;2" dur="2s" repeatCount="indefinite"/>
  </line>

  <!-- Version Badge -->
  <rect x="555" y="195" width="90" height="28" rx="14" fill="none" stroke="url(#neonOrange)" stroke-width="1.5" filter="url(#glow)">
    <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite"/>
  </rect>
  <text x="600" y="214" text-anchor="middle" font-family="monospace, Courier New, sans-serif" font-size="13" fill="#f97316" font-weight="700" letter-spacing="2">
    v2.1
  </text>

  <!-- Stats pills -->
  <g transform="translate(0, 245)">
    <rect x="390" y="0" width="150" height="34" rx="17" fill="none" stroke="#f97316" stroke-width="1.2" stroke-opacity="0.6">
      <animate attributeName="stroke-opacity" values="0.6;1;0.6" dur="3.2s" repeatCount="indefinite"/>
    </rect>
    <text x="465" y="22" text-anchor="middle" font-family="monospace, sans-serif" font-size="12" fill="#fdba74" font-weight="600">17 TOOLS</text>

    <rect x="570" y="0" width="150" height="34" rx="17" fill="none" stroke="#22d3ee" stroke-width="1.2" stroke-opacity="0.6">
      <animate attributeName="stroke-opacity" values="1;0.6;1" dur="2.8s" repeatCount="indefinite"/>
    </rect>
    <text x="645" y="22" text-anchor="middle" font-family="monospace, sans-serif" font-size="12" fill="#67e8f9" font-weight="600">100% PYTHON</text>
  </g>

  <!-- Corner brackets -->
  <g stroke="#00f5ff" stroke-width="2" fill="none" opacity="0.6">
    <path d="M20,20 L50,20 L50,30 M20,20 L20,50 L30,50">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" repeatCount="indefinite"/>
    </path>
    <path d="M1180,20 L1150,20 L1150,30 M1180,20 L1180,50 L1170,50">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" begin="0.5s" repeatCount="indefinite"/>
    </path>
    <path d="M20,280 L50,280 L50,270 M20,280 L20,250 L30,250">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" begin="1s" repeatCount="indefinite"/>
    </path>
    <path d="M1180,280 L1150,280 L1150,270 M1180,280 L1180,250 L1170,250">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" begin="1.5s" repeatCount="indefinite"/>
    </path>
  </g>
</svg>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    BADGE STRIP - ANIMATED                      -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<img src="https://img.shields.io/badge/Engine-v2.1-ff6b35?style=for-the-badge&logo=python&logoColor=white&labelColor=0a0a0f">
<img src="https://img.shields.io/badge/Python-3.8%2B-22d3ee?style=for-the-badge&logo=python&logoColor=white&labelColor=0a0a0f">
<img src="https://img.shields.io/badge/Tools-17-00f5ff?style=for-the-badge&logo=tool&logoColor=white&labelColor=0a0a0f">
<img src="https://img.shields.io/badge/License-MIT-f472b6?style=for-the-badge&logo=open-source-initiative&logoColor=white&labelColor=0a0a0f">
<img src="https://img.shields.io/badge/Status-Production%20Ready-10b981?style=for-the-badge&logo=checkmarx&logoColor=white&labelColor=0a0a0f">

<br><br>

```
$ python3 scripts/search.py "SaaS landing page" --design-system

    ╔══════════════════════════════════════════════════════════════╗
    ║  CYBER-RAGE DESIGN INTELLIGENCE ENGINE  v2.1                 ║
    ║  ─────────────────────────────────────────────────────────   ║
    ║  [⚡] 10 domains searched in parallel                       ║
    ║  [🎨] Design system generated in 0.847s                     ║
    ║  [✓]  70+ product types matched                             ║
    ╚══════════════════════════════════════════════════════════════╝
```

</div>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    FEATURE SHOWCASE SVG                        -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" width="28">
  <b>WHAT IS UI UX CR?</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" width="28">
</h3>

</div>

**UI UX CR** is not just another design tool — it is a **terminal-based design intelligence engine** that transforms your text prompts into complete, production-ready design systems. Built with pure Python, it runs entirely offline and generates everything from color palettes to full HTML landing pages in seconds.

Think of it as **ChatGPT for design systems**, but running locally in your terminal with zero API calls, zero subscriptions, and zero dependencies beyond Python itself.

<br>

<div align="center">

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    ANIMATED FEATURE GRID                       -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<svg width="100%" height="420" viewBox="0 0 1000 420" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5ff"/>
      <stop offset="100%" stop-color="#ff00ff"/>
    </linearGradient>
    <filter id="softGlow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Card 1: Search -->
  <rect x="10" y="10" width="310" height="120" rx="16" fill="url(#cardBg)" stroke="#00f5ff" stroke-width="1.5" stroke-opacity="0.3">
    <animate attributeName="stroke-opacity" values="0.3;0.8;0.3" dur="3s" repeatCount="indefinite"/>
  </rect>
  <text x="35" y="45" font-family="monospace, sans-serif" font-size="14" fill="#00f5ff" font-weight="700">🔍 ENHANCED BM25 SEARCH</text>
  <text x="35" y="70" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Fuzzy matching across 10 domains</text>
  <text x="35" y="88" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">120+ synonym groups</text>
  <text x="35" y="106" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">N-gram detection engine</text>

  <!-- Card 2: Design System -->
  <rect x="345" y="10" width="310" height="120" rx="16" fill="url(#cardBg)" stroke="#ff00ff" stroke-width="1.5" stroke-opacity="0.3">
    <animate attributeName="stroke-opacity" values="0.3;0.8;0.3" dur="3.5s" repeatCount="indefinite"/>
  </rect>
  <text x="370" y="45" font-family="monospace, sans-serif" font-size="14" fill="#ff00ff" font-weight="700">🎨 DESIGN SYSTEM GENERATOR</text>
  <text x="370" y="70" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Complete systems in one command</text>
  <text x="370" y="88" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Colors + typography + components</text>
  <text x="370" y="106" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Reasoning engine included</text>

  <!-- Card 3: Color Theory -->
  <rect x="680" y="10" width="310" height="120" rx="16" fill="url(#cardBg)" stroke="#f97316" stroke-width="1.5" stroke-opacity="0.3">
    <animate attributeName="stroke-opacity" values="0.3;0.8;0.3" dur="4s" repeatCount="indefinite"/>
  </rect>
  <text x="705" y="45" font-family="monospace, sans-serif" font-size="14" fill="#f97316" font-weight="700">🌈 COLOR THEORY ENGINE</text>
  <text x="705" y="70" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">6 harmony types + shade scales</text>
  <text x="705" y="88" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">WCAG contrast validation</text>
  <text x="705" y="106" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Color-blind simulation</text>

  <!-- Card 4: Toolbox -->
  <rect x="10" y="150" width="310" height="120" rx="16" fill="url(#cardBg)" stroke="#22d3ee" stroke-width="1.5" stroke-opacity="0.3">
    <animate attributeName="stroke-opacity" values="0.3;0.8;0.3" dur="3.2s" repeatCount="indefinite"/>
  </rect>
  <text x="35" y="185" font-family="monospace, sans-serif" font-size="14" fill="#22d3ee" font-weight="700">🧰 17 TOOLBOX SCRIPTS</text>
  <text x="35" y="210" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">SVG icons, CSS kits, components</text>
  <text x="35" y="228" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Animations, charts, pages, mockups</text>
  <text x="35" y="246" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Favicons, patterns, social specs</text>

  <!-- Card 5: Page Builder -->
  <rect x="345" y="150" width="310" height="120" rx="16" fill="url(#cardBg)" stroke="#10b981" stroke-width="1.5" stroke-opacity="0.3">
    <animate attributeName="stroke-opacity" values="0.3;0.8;0.3" dur="3.7s" repeatCount="indefinite"/>
  </rect>
  <text x="370" y="185" font-family="monospace, sans-serif" font-size="14" fill="#10b981" font-weight="700">🏗️ FULL PAGE BUILDER</text>
  <text x="370" y="210" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Compose landing pages in one cmd</text>
  <text x="370" y="228" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Navbar + hero + pricing + footer</text>
  <text x="370" y="246" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Tailwind CSS ready output</text>

  <!-- Card 6: Accessibility -->
  <rect x="680" y="150" width="310" height="120" rx="16" fill="url(#cardBg)" stroke="#a78bfa" stroke-width="1.5" stroke-opacity="0.3">
    <animate attributeName="stroke-opacity" values="0.3;0.8;0.3" dur="4.2s" repeatCount="indefinite"/>
  </rect>
  <text x="705" y="185" font-family="monospace, sans-serif" font-size="14" fill="#a78bfa" font-weight="700">♿ WCAG AUDITOR</text>
  <text x="705" y="210" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Contrast ratio analysis</text>
  <text x="705" y="228" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Alt text & label validation</text>
  <text x="705" y="246" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Heading order checker</text>

  <!-- Card 7: Animation -->
  <rect x="10" y="290" width="310" height="120" rx="16" fill="url(#cardBg)" stroke="#fbbf24" stroke-width="1.5" stroke-opacity="0.3">
    <animate attributeName="stroke-opacity" values="0.3;0.8;0.3" dur="3.4s" repeatCount="indefinite"/>
  </rect>
  <text x="35" y="325" font-family="monospace, sans-serif" font-size="14" fill="#fbbf24" font-weight="700">✨ ANIMATION DATABASE</text>
  <text x="35" y="350" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">30+ animation patterns</text>
  <text x="35" y="368" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Full CSS animation kit</text>
  <text x="35" y="386" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Reduced-motion fallback</text>

  <!-- Card 8: Tokens -->
  <rect x="345" y="290" width="310" height="120" rx="16" fill="url(#cardBg)" stroke="#f43f5e" stroke-width="1.5" stroke-opacity="0.3">
    <animate attributeName="stroke-opacity" values="0.3;0.8;0.3" dur="3.9s" repeatCount="indefinite"/>
  </rect>
  <text x="370" y="325" font-family="monospace, sans-serif" font-size="14" fill="#f43f5e" font-weight="700">🔖 DESIGN TOKENS</text>
  <text x="370" y="350" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">70+ token categories</text>
  <text x="370" y="368" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">CSS variables export</text>
  <text x="370" y="386" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Tailwind config generation</text>

  <!-- Card 9: Typography -->
  <rect x="680" y="290" width="310" height="120" rx="16" fill="url(#cardBg)" stroke="#06b6d4" stroke-width="1.5" stroke-opacity="0.3">
    <animate attributeName="stroke-opacity" values="0.3;0.8;0.3" dur="4.4s" repeatCount="indefinite"/>
  </rect>
  <text x="705" y="325" font-family="monospace, sans-serif" font-size="14" fill="#06b6d4" font-weight="700">🔤 TYPOGRAPHY ENGINE</text>
  <text x="705" y="350" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Modular type scales</text>
  <text x="705" y="368" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Google Fonts pairings</text>
  <text x="705" y="386" font-family="monospace, sans-serif" font-size="11" fill="#94a3b8">Golden ratio & perfect fourth</text>
</svg>

</div>

<br>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    ANIMATED DATA COVERAGE                      -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bar%20Chart.png" width="28">
  <b>DATA COVERAGE v2.1</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bar%20Chart.png" width="28">
</h3>

<svg width="100%" height="340" viewBox="0 0 900 340" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5ff"/>
      <stop offset="100%" stop-color="#ff00ff"/>
    </linearGradient>
    <filter id="barGlow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="900" height="340" rx="20" fill="#0a0a0f" stroke="#1e293b" stroke-width="1"/>

  <!-- Title -->
  <text x="450" y="35" text-anchor="middle" font-family="monospace, sans-serif" font-size="16" fill="#e2e8f0" font-weight="700" letter-spacing="4">DATABASE COVERAGE</text>
  <line x1="350" y1="45" x2="550" y2="45" stroke="#00f5ff" stroke-width="1" opacity="0.5"/>

  <!-- Product Types: 70+ -->
  <text x="30" y="82" font-family="monospace, sans-serif" font-size="12" fill="#94a3b8">Product Types</text>
  <rect x="220" y="70" width="600" height="18" rx="9" fill="#1e293b"/>
  <rect x="220" y="70" width="600" height="18" rx="9" fill="url(#barGrad)" filter="url(#barGlow)">
    <animate attributeName="width" values="0;600" dur="2s" begin="0.2s" fill="freeze"/>
  </rect>
  <text x="840" y="84" font-family="monospace, sans-serif" font-size="12" fill="#e2e8f0" font-weight="700">70+</text>

  <!-- UI Styles: 46+ -->
  <text x="30" y="122" font-family="monospace, sans-serif" font-size="12" fill="#94a3b8">UI Styles</text>
  <rect x="220" y="110" width="600" height="18" rx="9" fill="#1e293b"/>
  <rect x="220" y="110" width="395" height="18" rx="9" fill="url(#barGrad)" filter="url(#barGlow)">
    <animate attributeName="width" values="0;395" dur="2s" begin="0.4s" fill="freeze"/>
  </rect>
  <text x="630" y="124" font-family="monospace, sans-serif" font-size="12" fill="#e2e8f0" font-weight="700">46+</text>

  <!-- Color Palettes: 80+ -->
  <text x="30" y="162" font-family="monospace, sans-serif" font-size="12" fill="#94a3b8">Color Palettes</text>
  <rect x="220" y="150" width="600" height="18" rx="9" fill="#1e293b"/>
  <rect x="220" y="150" width="600" height="18" rx="9" fill="url(#barGrad)" filter="url(#barGlow)">
    <animate attributeName="width" values="0;600" dur="2s" begin="0.6s" fill="freeze"/>
  </rect>
  <text x="840" y="164" font-family="monospace, sans-serif" font-size="12" fill="#e2e8f0" font-weight="700">80+</text>

  <!-- Font Pairings: 75+ -->
  <text x="30" y="202" font-family="monospace, sans-serif" font-size="12" fill="#94a3b8">Font Pairings</text>
  <rect x="220" y="190" width="600" height="18" rx="9" fill="#1e293b"/>
  <rect x="220" y="190" width="562" height="18" rx="9" fill="url(#barGrad)" filter="url(#barGlow)">
    <animate attributeName="width" values="0;562" dur="2s" begin="0.8s" fill="freeze"/>
  </rect>
  <text x="802" y="204" font-family="monospace, sans-serif" font-size="12" fill="#e2e8f0" font-weight="700">75+</text>

  <!-- Synonym Groups: 120+ -->
  <text x="30" y="242" font-family="monospace, sans-serif" font-size="12" fill="#94a3b8">Synonym Groups</text>
  <rect x="220" y="230" width="600" height="18" rx="9" fill="#1e293b"/>
  <rect x="220" y="230" width="600" height="18" rx="9" fill="url(#barGrad)" filter="url(#barGlow)">
    <animate attributeName="width" values="0;600" dur="2s" begin="1s" fill="freeze"/>
  </rect>
  <text x="840" y="244" font-family="monospace, sans-serif" font-size="12" fill="#e2e8f0" font-weight="700">120+</text>

  <!-- Toolbox Scripts: 17 -->
  <text x="30" y="282" font-family="monospace, sans-serif" font-size="12" fill="#94a3b8">Toolbox Scripts</text>
  <rect x="220" y="270" width="600" height="18" rx="9" fill="#1e293b"/>
  <rect x="220" y="270" width="145" height="18" rx="9" fill="#f97316" filter="url(#barGlow)">
    <animate attributeName="width" values="0;145" dur="2s" begin="1.2s" fill="freeze"/>
  </rect>
  <text x="385" y="284" font-family="monospace, sans-serif" font-size="12" fill="#e2e8f0" font-weight="700">17</text>

  <!-- Components: 12 -->
  <text x="30" y="322" font-family="monospace, sans-serif" font-size="12" fill="#94a3b8">Components</text>
  <rect x="220" y="310" width="600" height="18" rx="9" fill="#1e293b"/>
  <rect x="220" y="310" width="102" height="18" rx="9" fill="#22d3ee" filter="url(#barGlow)">
    <animate attributeName="width" values="0;102" dur="2s" begin="1.4s" fill="freeze"/>
  </rect>
  <text x="342" y="324" font-family="monospace, sans-serif" font-size="12" fill="#e2e8f0" font-weight="700">12</text>
</svg>

</div>

<br>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    THE 17 TOOLS TABLE                          -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Toolbox.png" width="28">
  <b>THE 17 TOOLBOX SCRIPTS</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Toolbox.png" width="28">
</h3>

</div>

| # | Script | What It Does | Quick Command |
|---|--------|-------------|---------------|
| 01 | `search.py` | BM25 design search across 10 domains | `python3 scripts/search.py "saas" --design-system` |
| 02 | `svg_generator.py` | 70+ SVG icons, 6 patterns, logos | `python3 scripts/svg_generator.py --icon search --size 24` |
| 03 | `css_generator.py` | Shadows, gradients, glass, glow, UI kit | `python3 scripts/css_generator.py --ui-kit --primary #2563EB` |
| 04 | `palette_generator.py` | Harmony palettes, shade scales, WCAG | `python3 scripts/palette_generator.py "#2563EB" --harmony triadic` |
| 05 | `typography_generator.py` | Modular type scales + font pairings | `python3 scripts/typography_generator.py --scale golden-ratio` |
| 06 | `theme_exporter.py` | Export theme → CSS/Tailwind/SCSS/JSON | `python3 scripts/theme_exporter.py "#2563EB" --format all` |
| 07 | `component_generator.py` | 12 ready components from database | `python3 scripts/component_generator.py --component navbar` |
| 08 | `page_builder.py` | Compose full HTML landing pages | `python3 scripts/page_builder.py --sections navbar,hero,features,pricing,cta,footer` |
| 09 | `layout_generator.py` | Grids, containers, spacing, breakpoints | `python3 scripts/layout_generator.py --layout dashboard` |
| 10 | `animation_generator.py` | 12 animations with parameters + kit | `python3 scripts/animation_generator.py --type bounce --duration 0.6` |
| 11 | `chart_generator.py` | Chart.js & Recharts configs (8 types) | `python3 scripts/chart_generator.py --chart bar --labels "Q1,Q2"` |
| 12 | `pattern_generator.py` | 12 CSS background patterns | `python3 scripts/pattern_generator.py checkerboard --color #2563EB` |
| 13 | `favicon_generator.py` | Favicon SVG + HTML head + PWA manifest | `python3 scripts/favicon_generator.py --text CR --bg #2563EB` |
| 14 | `copy_generator.py` | Headlines, CTAs, placeholders, A/B | `python3 scripts/copy_generator.py --headline saas --count 3` |
| 15 | `mockup_generator.py` | ASCII wireframes (desktop, mobile, etc) | `python3 scripts/mockup_generator.py --type dashboard` |
| 16 | `social_specs.py` | Social media dimension cheat sheets | `python3 scripts/social_specs.py --platform instagram` |
| 17 | `accessibility_audit.py` | WCAG audit of HTML files | `python3 scripts/accessibility_audit.py index.html` |

<br>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    VERSION COMPARISON TABLE                    -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Chart%20Increasing.png" width="28">
  <b>EVOLUTION: v1.x → v2.0 → v2.1</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Chart%20Increasing.png" width="28">
</h3>

</div>

| Category | v1.x | v2.0 | **v2.1** |
|----------|------|------|----------|
| Product Types | 51 | 70+ | **70+** |
| UI Styles | 31 | 46+ | **46+** |
| Color Palettes | 61 | 80+ | **80+** |
| Font Pairings | 61 | 75+ | **75+** |
| Synonym Groups | 34 | 120+ | **120+** |
| Toolbox Scripts | ❌ | 9 | **17** |
| Components | — | — | **12 generated** |
| Layout Templates | — | — | **5** |
| Chart Types | — | — | **8 + 2 frameworks** |
| Background Patterns | — | — | **12 CSS** |
| SVG Icons | — | — | **70+** |
| WCAG Audit | ❌ | — | **Built-in tool** |

<br>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    INSTALLATION SECTION                        -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" width="28">
  <b>INSTALLATION</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" width="28">
</h3>

</div>

### Option 1: Direct Clone

```bash
git clone https://github.com/CyebRageAnonymuos/ui-ux-cr.git
cd ui-ux-cr
```

### Option 2: As an OpenCode / Claude Skill

```bash
mkdir -p .opencode/skills/ui-ux-cr
cp -r ui-ux-cr/scripts .opencode/skills/ui-ux-cr/
cp -r ui-ux-cr/data .opencode/skills/ui-ux-cr/
cp ui-ux-cr/SKILL.md .opencode/skills/ui-ux-cr/
```

### Prerequisites

```bash
python3 --version   # Requires Python 3.8+
```

> **No pip install. No dependencies. No API keys.** Just pure Python.

<br>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    USAGE SECTION                               -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Keyboard.png" width="28">
  <b>USAGE</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Keyboard.png" width="28">
</h3>

</div>

### Primary Feature: Generate a Complete Design System

```bash
python3 scripts/search.py "SaaS landing page modern" --design-system -p "My SaaS"
```

**Output includes:**
- Pattern & style recommendations
- Color palette + extended palette
- Typography with Google Fonts links
- Effects & components with code
- Animations with CSS
- Responsive patterns & anti-patterns
- Pre-delivery checklist

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
python3 scripts/search.py "fintech" --design-system              # ASCII (terminal)
python3 scripts/search.py "fintech" --design-system -f markdown  # Markdown docs
python3 scripts/search.py "glassmorphism" --domain style --json   # JSON API
```

<br>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    REALISTIC WORKFLOW                          -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Stopwatch.png" width="28">
  <b>REALISTIC WORKFLOW: 60 SECONDS</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Stopwatch.png" width="28">
</h3>

</div>

```bash
# 1. Build a full landing page for a Micro SaaS
python3 scripts/page_builder.py --product "Micro SaaS"   --sections navbar,hero,features,pricing,cta,footer   --out landing.html

# 2. Replace emoji placeholders with real SVG icons
python3 scripts/svg_generator.py --icon check --color "#10B981" --size 24

# 3. Add a complete animation kit
python3 scripts/animation_generator.py --kit

# 4. Audit the page for accessibility
python3 scripts/accessibility_audit.py landing.html
```

<br>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    DOMAINS & STACKS                            -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Books.png" width="28">
  <b>AVAILABLE DOMAINS & STACKS</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Books.png" width="28">
</h3>

</div>

### Domains

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

### Supported Stacks

```
html-tailwind (default) · react · nextjs · vue · nuxtjs · svelte
swiftui · react-native · flutter · shadcn · jetpack-compose · angular
laravel · threejs · astro · nuxt-ui
```

<br>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    EXAMPLES SECTION                            -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Light%20Bulb.png" width="28">
  <b>EXAMPLES</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Light%20Bulb.png" width="28">
</h3>

</div>

### Example 1: SaaS Landing Page — Built End to End

```bash
# Design system
python3 scripts/search.py "SaaS landing page modern" --design-system -p "My SaaS"

# Full page
python3 scripts/page_builder.py --product "SaaS (General)"   --sections navbar,hero,features,pricing,cta,footer   --out landing.html

# Custom CSS kit + icons
python3 scripts/css_generator.py --ui-kit --primary #2563EB --cta #F97316
python3 scripts/svg_generator.py --icon check --size 24
```

> **Recommended:** Glassmorphism + Flat · Trust blue `#2563EB` + orange CTA `#F97316` · Poppins + Inter

### Example 2: Healthcare Dashboard

```bash
python3 scripts/search.py "healthcare dashboard" --design-system -p "Health App"
python3 scripts/layout_generator.py --layout dashboard
python3 scripts/chart_generator.py --chart line   --labels "Mon,Tue,Wed,Thu,Fri"   --data "120,180,150,220,190"
```

> **Recommended:** Dark Mode (OLED) · `#0F172A` bg + health green `#22C55E` · Merriweather + Open Sans

### Example 3: E-commerce Luxury Store

```bash
python3 scripts/search.py "ecommerce luxury" --design-system -p "Luxury Shop"
python3 scripts/component_generator.py --component card --product "E-commerce"
python3 scripts/palette_generator.py "#1C1917" --harmony tetradic --check-wcag
```

> **Recommended:** Liquid Glass + Glassmorphism · Premium dark + gold `#CA8A04` · Cormorant Garamond + Montserrat

<br>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    PRE-DELIVERY CHECKLIST                      -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Clipboard.png" width="28">
  <b>PRE-DELIVERY CHECKLIST</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Clipboard.png" width="28">
</h3>

</div>

```
☐ No emojis as icons — use svg_generator.py
☐ cursor-pointer on all clickable elements
☐ Hover states 150-300ms, no layout shift
☐ Contrast 4.5:1 minimum — verify with accessibility_audit.py
☐ All images have alt text
☐ Form inputs have labels
☐ prefers-reduced-motion respected
☐ Responsive at 375 / 768 / 1024 / 1440px
☐ Loading, error, and empty states designed
☐ Dark mode tested
```

<br>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    CONTRIBUTING & LICENSE                      -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<h3>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Handshake.png" width="28">
  <b>CONTRIBUTING</b>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Handshake.png" width="28">
</h3>

</div>

1. **Fork** the repository
2. Create your branch: `git checkout -b feature/AmazingFeature`
3. Commit: `git commit -m 'Add some AmazingFeature'`
4. Push and open a **Pull Request**

<div align="center">

---

## License

**MIT** — see [LICENSE](LICENSE) for details.

<br>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    FOOTER ANIMATION                            -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<svg width="100%" height="100" viewBox="0 0 1200 100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="footerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5ff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00f5ff" stop-opacity="1"/>
      <stop offset="100%" stop-color="#ff00ff" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <line x1="100" y1="50" x2="1100" y2="50" stroke="url(#footerGrad)" stroke-width="1.5">
    <animate attributeName="stroke-width" values="1.5;3;1.5" dur="3s" repeatCount="indefinite"/>
  </line>
  <text x="600" y="75" text-anchor="middle" font-family="monospace, sans-serif" font-size="12" fill="#475569" letter-spacing="8">
    CYBER-RAGE DESIGN INTELLIGENCE ENGINE
    <animate attributeName="opacity" values="0.4;0.8;0.4" dur="4s" repeatCount="indefinite"/>
  </text>
  <text x="600" y="92" text-anchor="middle" font-family="monospace, sans-serif" font-size="10" fill="#334155" letter-spacing="4">
    BUILT WITH PURE PYTHON · ZERO DEPENDENCIES · OFFLINE FIRST
  </text>
</svg>

</div>
