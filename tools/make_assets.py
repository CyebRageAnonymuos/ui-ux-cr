#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asset Maker - Generate animated GIF banners for the README.
Guaranteed animation on every platform (GitHub, mobile, all browsers).

Usage: python3 tools/make_assets.py
Output:
  assets/hero-banner.gif   - main animated hero banner
  assets/tools-grid.gif    - 17 pulsing tool chips
  assets/stats-bars.gif    - animated data coverage bars
"""

import math
import os
import random

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
os.makedirs(ASSETS, exist_ok=True)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

CYAN = (34, 211, 238)
PINK = (255, 0, 110)
ORANGE = (249, 115, 22)
LIME = (163, 230, 53)
VIOLET = (167, 139, 250)
SLATE = (148, 163, 184)
WHITE = (240, 247, 255)

_font_cache = {}


def font(size, mono=False, bold=True):
    key = (size, mono, bold)
    if key not in _font_cache:
        path = FONT_MONO if mono else (FONT_BOLD if bold else FONT)
        _font_cache[key] = ImageFont.truetype(path, size)
    return _font_cache[key]


def lerp_color(c1, c2, t):
    t = max(0.0, min(1.0, t))
    return tuple(int(round(c1[i] + (c2[i] - c1[i]) * t)) for i in range(3))


def gradient_v(w, h, stops):
    """Vertical gradient. stops: [(pos, (r,g,b)), ...]"""
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        t = y / (h - 1)
        color = stops[-1][1]
        for i in range(len(stops) - 1):
            p0, c0 = stops[i]
            p1, c1 = stops[i + 1]
            if p0 <= t <= p1:
                color = lerp_color(c0, c1, (t - p0) / (p1 - p0))
                break
        for x in range(w):
            px[x, y] = color
    return img


def new_canvas(w, h, seed=0, n_particles=26):
    stops = [(0.0, (8, 10, 22)), (0.45, (15, 23, 42)), (0.85, (36, 10, 48)), (1.0, (8, 10, 22))]
    img = gradient_v(w, h, stops)
    d = ImageDraw.Draw(img, "RGBA")
    return img, d


def particles(d, w, h, f, seed=11, n=26, colors=None):
    rnd = random.Random(seed)
    colors = colors or [CYAN, PINK, ORANGE, WHITE]
    for i in range(n):
        x = rnd.uniform(0, w)
        base = rnd.uniform(0, h)
        amp = rnd.uniform(3, 14)
        r = rnd.uniform(0.8, 2.6)
        speed = rnd.uniform(0.5, 1.5)
        phase = rnd.uniform(0, 6.28)
        y = base + math.sin(f * 0.15 * speed + phase) * amp
        c = colors[i % len(colors)]
        alpha = int(80 + 140 * (0.5 + 0.5 * math.sin(f * 0.2 + phase)))
        d.ellipse([x - r, y - r, x + r, y + r], fill=c + (alpha,))


def draw_rings(d, cx, cy, f):
    for i, (radius, color, dr) in enumerate([(52, CYAN, 1), (40, PINK, -1), (28, ORANGE, 2)]):
        ang = (f * dr * 90) % 360
        d.arc([cx - radius, cy - radius, cx + radius, cy + radius],
              start=ang, end=ang + 90, fill=color, width=3)
    r = 8 + 2 * math.sin(f * 0.35)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE)


def glow_text(d, xy, text, fnt, fill, glow, rad=3, passes=4):
    x, y = xy
    for i in range(passes, 0, -1):
        col = (glow[0], glow[1], glow[2], int(90 / i))
        for dx in (-i, 0, i):
            for dy in (-i, 0, i):
                if dx or dy:
                    d.text((x + dx, y + dy), text, font=fnt, fill=col)
    d.text((x, y), text, font=fnt, fill=fill)


def save_gif(frames, path, duration=52):
    qframes = [fr.quantize(colors=128, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
               for fr in frames]
    qframes[0].save(path, save_all=True, append_images=qframes[1:],
                    duration=duration, loop=0, optimize=True)
    size_kb = os.path.getsize(path) // 1024
    print(f"wrote {path} ({size_kb} KB, {len(frames)} frames)")


def make_hero():
    W, H, FR = 900, 320, 36
    frames = []
    for f in range(FR):
        t = f / FR
        img, d = new_canvas(W, H)
        particles(d, W, H, f)
        draw_rings(d, 128, 148, f)

        # animated gradient title
        sweep = 0.5 + 0.5 * math.sin(f * 0.08)
        c1 = lerp_color(CYAN, PINK, sweep)
        c2 = lerp_color(PINK, CYAN, sweep)
        fnt = font(92)
        title = "UI UX CR"
        bb = d.textbbox((0, 0), title, font=fnt)
        tw = bb[2] - bb[0]
        x0 = (W - tw) / 2
        y0 = 62
        glow_text(d, (x0, y0), title, fnt, c1 + (255,), c1)

        # moving shine on title
        shine_x = (f * 1.1) % (tw + 300) - 150
        for i in range(int(tw)):
            if abs(i - shine_x) < 46:
                a = int(70 * (1 - abs(i - shine_x) / 46))
                xp = x0 + i
                d.line([(xp, y0 + 6), (xp, y0 + fnt.size - 8)], fill=(255, 255, 255, a))

        # sweep divider
        track_y = 168
        d.rectangle([W * 0.2, track_y, W * 0.8, track_y + 3], fill=(40, 52, 74, 255))
        sx = W * 0.2 + t * W * 0.6
        d.rectangle([sx, track_y, min(W * 0.8, sx + 130), track_y + 3],
                    fill=lerp_color(CYAN, PINK, t) + (255,))

        # subtitle
        sub = "CYBER-RAGE DESIGN INTELLIGENCE ENGINE"
        fnt_s = font(19)
        sbb = d.textbbox((0, 0), sub, font=fnt_s)
        d.text(((W - (sbb[2] - sbb[0])) / 2, 178), sub, font=fnt_s,
               fill=SLATE + (255,))

        # typing terminal
        lines = [
            '$ python3 scripts/search.py "saas" --design-system',
            '$ python3 scripts/page_builder.py --out landing.html',
            '$ python3 scripts/accessibility_audit.py landing.html',
        ]
        line = lines[int(t * 3) % 3]
        n = int(((f * 2.4) % 1.0) * len(line))
        shown = line[:n]
        fnt_m = font(15, mono=True)
        mbb = d.textbbox((0, 0), shown, font=fnt_m)
        xm = (W - (mbb[2] - mbb[0])) / 2
        ym = 228
        d.text((xm, ym), shown, font=fnt_m, fill=CYAN + (255,))
        if int(f * 2) % 2 == 0:
            d.rectangle([xm + mbb[2], ym, xm + mbb[2] + 9, ym + 17], fill=PINK)

        # version chip
        chip = "v2.1"
        fnt_c = font(14, bold=True)
        pulse = 0.5 + 0.5 * math.sin(f * 0.3)
        ccol = lerp_color((255, 0, 110), (80, 20, 60), pulse)
        cbb = d.textbbox((0, 0), chip, font=fnt_c)
        cw = cbb[2] - cbb[0] + 24
        d.rounded_rectangle([W - cw - 18, 14, W - 14, 46], radius=16, fill=ccol + (255,))
        d.text((W - cw - 18 + 12, 14), chip, font=fnt_c, fill=WHITE + (255,))
        frames.append(img)
    save_gif(frames, os.path.join(ASSETS, "hero-banner.gif"))
    


def make_tools():
    W, H, FR = 960, 268, 32
    names = ["search.py", "svg_gen", "css_gen", "palette", "type_gen", "theme_xport",
             "component", "page_build", "layout_gen", "anim_gen", "chart_gen", "pattern_gen",
             "favicon", "copy_gen", "a11y_audit", "mockup_gen", "social_specs"]
    cols = [CYAN, PINK, ORANGE, LIME, VIOLET, CYAN,
            PINK, ORANGE, LIME, VIOLET, CYAN, PINK,
            ORANGE, LIME, VIOLET, CYAN, PINK]
    frames = []
    for f in range(FR):
        img, d = new_canvas(W, H)
        particles(d, W, H, f)
        # title
        fnt = font(26)
        ttxt = "17 TOOLBOX SCRIPTS"
        bb = d.textbbox((0, 0), ttxt, font=fnt)
        d.text(((W - (bb[2] - bb[0])) / 2, 18), ttxt, font=fnt,
               fill=lerp_color(CYAN, PINK, (f / FR)) + (255,))
        # chips 6x3
        chipw, chiph, gx0, gy0 = 150, 40, 20, 62
        for i, (nm, col) in enumerate(zip(names, cols)):
            r, c = i // 6, i % 6
            x = gx0 + c * (chipw + 12)
            y = gy0 + r * (chiph + 16)
            pulse = 0.5 + 0.5 * math.sin(f * 0.3 - i * 0.5)
            border = tuple(int(col[j] * (0.35 + 0.65 * pulse)) for j in range(3))
            d.rounded_rectangle([x, y, x + chipw, y + chiph], radius=12,
                                fill=(15, 23, 42, 235), outline=border, width=2)
            fnt_ch = font(14, mono=True)
            d.text((x + chipw / 2, y + chiph / 2), nm, font=fnt_ch,
                   fill=WHITE + (255,), anchor="mm")
        # footer note
        d.text((W / 2, H - 18), "generators, builders, auditors - one skill",
               font=font(13), fill=SLATE + (255,), anchor="mm")
        frames.append(img)
    save_gif(frames, os.path.join(ASSETS, "tools-grid.gif"), duration=60)
    


def make_stats():
    W, H, FR = 960, 300, 36
    stats = [
        ("Product Types", 70, "70+", PINK),
        ("UI Styles", 46, "46+", CYAN),
        ("Color Palettes", 80, "80+", ORANGE),
        ("Font Pairings", 75, "75+", VIOLET),
        ("Toolbox Scripts", 17, "17", LIME),
    ]
    bar_x0, bar_w = 250, W - 340
    frames = []
    for f in range(FR):
        t = f / (FR - 1)
        img, d = new_canvas(W, H)
        particles(d, W, H, f)
        fnt = font(30)
        ttxt = "DATA COVERAGE"
        bb = d.textbbox((0, 0), ttxt, font=fnt)
        d.text(((W - (bb[2] - bb[0])) / 2, 26), ttxt, font=fnt, fill=WHITE + (255,))
        y0 = 84
        bar_h = 22
        for i, (label, val, disp, col) in enumerate(stats):
            y = y0 + i * (bar_h + 34)
            d.text((24, y), label, font=font(15), fill=SLATE + (255,), anchor="lm")
            d.rounded_rectangle([bar_x0, y - bar_h / 2, bar_x0 + bar_w, y + bar_h / 2],
                                radius=11, fill=(30, 41, 59, 255))
            start = 0.15 + i * 0.04
            prog = min(1.0, max(0.0, (t - start) / (1 - start)))
            frac = val / 100.0 * prog
            wfrac = bar_w * frac
            d.rounded_rectangle([bar_x0, y - bar_h / 2, bar_x0 + wfrac, y + bar_h / 2],
                                radius=11, fill=col + (255,))
            d.text((bar_x0 + wfrac + 12, y), disp, font=font(18), fill=WHITE + (255,), anchor="lm")
        d.text((W / 2, H - 20), "curated from the cyber-rage design database",
               font=font(13), fill=SLATE + (255,), anchor="mm")
        frames.append(img)
    save_gif(frames, os.path.join(ASSETS, "stats-bars.gif"), duration=56)
    


if __name__ == "__main__":
    make_hero()
    make_tools()
    make_stats()
