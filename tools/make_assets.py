#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asset Maker v2 - Luxury animated GIF banners for the README.
Black & champagne-gold aesthetic, elegant serif, subtle motion.

Usage: python3 tools/make_assets.py
Output:
  assets/hero-banner.gif   - luxury animated hero banner
  assets/tools-grid.gif    - gold-edged toolbox grid
  assets/stats-bars.gif    - refined data coverage bars
"""

import math
import os
import random

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
os.makedirs(ASSETS, exist_ok=True)

# --- Luxury palette: black / champagne gold / cream -------------------
BG_TOP = (12, 12, 17)
BG_MID = (20, 19, 26)
BG_BOTTOM = (8, 8, 12)
GOLD = (198, 160, 78)
GOLD_HI = (226, 197, 121)
GOLD_PALE = (243, 228, 178)
CREAM = (237, 230, 215)
MUTED = (165, 156, 128)
INK = (24, 23, 31)

_font_cache = {}


def font(size, mono=False, serif=False):
    key = (size, mono, serif)
    if key not in _font_cache:
        if serif:
            p = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
        elif mono:
            p = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
        else:
            p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        _font_cache[key] = ImageFont.truetype(p, size)
    return _font_cache[key]


def lerp_color(c1, c2, t):
    t = max(0.0, min(1.0, t))
    return tuple(int(round(c1[i] + (c2[i] - c1[i]) * t)) for i in range(3))


def save_gif(frames, path, duration=65):
    qframes = [fr.quantize(colors=192, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
               for fr in frames]
    qframes[0].save(path, save_all=True, append_images=qframes[1:],
                    duration=duration, loop=0, optimize=True)
    print(f"wrote {path} ({os.path.getsize(path) // 1024} KB, {len(frames)} frames)")


def gradient_v(w, h, stops):
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


def vignette(img, strength=0.55):
    w, h = img.size
    ov = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    cx, cy = w / 2, h / 2
    maxr = math.sqrt(cx * cx + cy * cy)
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            r = math.sqrt((x - cx) ** 2 * 1.2 + (y - cy) ** 2) / maxr
            a = int(strength * 255 * max(0.0, r - 0.5))
            if a:
                d.ellipse([x - 1, y - 1, x + 1, y + 1], fill=(0, 0, 0, a))
    ov = ov.resize((w, h))
    img.paste(ov, (0, 0), ov)
    return img


def gold_glow_asset(w, h):
    """Precomputed soft radial gold glow (RGBA)."""
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, cy = w / 2, h / 2
    maxr = min(cx, cy)
    for y in range(h):
        for x in range(w):
            r = math.sqrt((x - cx) ** 2 + (y - cy) ** 2) / maxr
            if r < 1:
                a = int(46 * (1 - r) ** 2)
                if a:
                    d.point((x, y), fill=GOLD_PALE + (a,))
    return img


def new_canvas(w, h):
    img = gradient_v(w, h, [(0.0, BG_TOP), (0.55, BG_MID), (1.0, BG_BOTTOM)])
    img = vignette(img)
    return img, ImageDraw.Draw(img, "RGBA")


def dust(d, w, h, f, seed=5, n=16):
    rnd = random.Random(seed)
    for i in range(n):
        x = rnd.uniform(0, w)
        base = rnd.uniform(0, h)
        speed = rnd.uniform(0.2, 0.55)
        amp = rnd.uniform(1.5, 5)
        r = rnd.uniform(0.6, 1.6)
        y = base + math.sin(f * 0.1 * speed + rnd.uniform(0, 6.28)) * amp
        a = int(28 + 40 * (0.5 + 0.5 * math.sin(f * 0.08 + base)))
        d.ellipse([x - r, y - r, x + r, y + r], fill=GOLD_PALE + (a,))


def frame_ticks(d, w, h, m=30, e=30):
    c = GOLD + (70,)
    for (x, y, dx, dy) in [(m, m, e, 1), (m, m, 1, e),
                           (w - m - e, m, e, 1), (w - m, m, 1, e),
                           (m, h - m - 1, e, 1), (m, h - m, 1, e),
                           (w - m - e, h - m - 1, e, 1), (w - m, h - m, 1, e)]:
        d.rectangle([x, y, x + dx, y + dy], fill=c)


def side_hairlines(d, w, h, f):
    c = GOLD + (60,)
    for x in (64, w - 64):
        d.rectangle([x, 40, x + 1, h - 40], fill=c)


def title_gold(d, text, fnt, x0, y0, t):
    """Serif title, letters gently catching the light."""
    x = x0
    for ch in text:
        b = fnt.getbbox(ch)
        cw = b[2] - b[0]
        wave = 0.5 + 0.5 * math.sin(t * 0.9 + x * 0.02)
        col = lerp_color(GOLD, GOLD_PALE, wave * 0.9)
        d.text((x, y0), ch, font=fnt, fill=col + (255,))
        x += cw + 4
    return x


def hairline_grow(d, cx, y0, max_w, t, bright_x=None):
    """Gold hairline that grows from center, with a moving bright point."""
    half = max_w * min(1.0, t * 1.4) / 2
    d.rectangle([cx - half, y0, cx + half, y0 + 1], fill=GOLD + (110,))
    if bright_x is not None:
        bx = cx - half + (2 * half) * bright_x
        d.rectangle([bx, y0 - 1, bx + 6, y0 + 2], fill=GOLD_PALE + (200,))


def make_hero():
    W, H, FR = 1100, 360, 40
    glow = gold_glow_asset(700, 130)
    frames = []
    for f in range(FR):
        t = f / (FR - 1)
        img, d = new_canvas(W, H)
        # breathing glow behind title
        breath = 0.5 + 0.5 * math.sin(t * 2 * math.pi)
        ga = int(60 + 80 * breath)
        g = glow.copy()
        g.putalpha(ga)
        img.paste(g, (W // 2 - 350, 30), g)
        d = ImageDraw.Draw(img, "RGBA")

        dust(d, W, H, f)
        frame_ticks(d, W, H)
        side_hairlines(d, W, H, f)

        # title
        fnt = font(96, serif=True)
        title = "UI UX CR"
        bb = d.textbbox((0, 0), title, font=fnt)
        tw = bb[2] - bb[0] + 3 * 4
        x0 = (W - tw) / 2
        title_gold(d, title, fnt, x0, 96, t)

        # growing hairline with moving bright point
        hairline_grow(d, W / 2, 236, 480, t, bright_x=(t * 1.7) % 1)

        # caption
        cap = "C Y B E R - R A G E   D E S I G N   I N T E L L I G E N C E"
        fnt_c = font(17, serif=True)
        cbb = d.textbbox((0, 0), cap, font=fnt_c)
        d.text(((W - (cbb[2] - cbb[0])) / 2, 258), cap, font=fnt_c, fill=CREAM + (200,))

        # sub line
        sub = "AI-POWERED UI/UX SKILL  ·  17 TOOLBOX SCRIPTS  ·  PYTHON 3"
        fnt_s = font(13, mono=True)
        sbb = d.textbbox((0, 0), sub, font=fnt_s)
        d.text(((W - (sbb[2] - sbb[0])) / 2, 300), sub, font=fnt_s, fill=MUTED + (190,))

        # version marker bottom-right
        ver = "V 2.1"
        fnt_v = font(13, serif=True)
        d.text((W - 76, H - 40), ver, font=fnt_v, fill=GOLD + (150,))
        d.rectangle([W - 76, H - 32, W - 46, H - 31], fill=GOLD + (120,))

        frames.append(img)
    save_gif(frames, os.path.join(ASSETS, "hero-banner.gif"), duration=65)


def make_tools():
    W, H, FR = 980, 290, 40
    names = ["search", "svg", "css", "palette", "type", "theme",
             "component", "page", "layout", "anim", "chart", "pattern",
             "favicon", "copy", "a11y", "mockup", "social"]
    kinds = ["SEARCH", "ICON", "CSS", "COLOR", "TYPE", "EXPORT",
             "HTML", "PAGE", "GRID", "MOTION", "DATA-VIZ", "BG",
             "BRAND", "COPY", "A11Y", "WIRE", "SIZES"]
    frames = []
    for f in range(FR):
        t = f / (FR - 1)
        img, d = new_canvas(W, H)
        dust(d, W, H, f, seed=9, n=12)
        frame_ticks(d, W, H, m=22, e=22)

        fnt = font(24, serif=True)
        txt = "T H E   T O O L B O X"
        bb = d.textbbox((0, 0), txt, font=fnt)
        d.text(((W - (bb[2] - bb[0])) / 2, 26), txt, font=fnt, fill=GOLD_PALE + (220,))
        d.rectangle([W / 2 - 70, 62, W / 2 + 70, 63], fill=GOLD + (90,))

        cw, ch = 148, 56
        gx, gy, gapx, gapy = 22, 82, 12, 14
        for i in range(len(names)):
            r, c = i // 6, i % 6
            x = gx + c * (cw + gapx)
            y = gy + r * (ch + gapy)
            wave = (t * 2.0 - i * 0.045) % 1.0
            border = lerp_color(GOLD, GOLD_PALE, wave)
            ba = int(70 + 130 * max(0.0, 1 - abs(wave - 0.5) * 2))
            d.rounded_rectangle([x, y, x + cw, y + ch], radius=8,
                                fill=INK + (235,), outline=border + (ba,), width=1)
            d.text((x + 10, y + 8), f"{i + 1:02d}", font=font(9, mono=True), fill=GOLD + (140,))
            d.text((x + cw / 2, y + 20), names[i], font=font(14, mono=True), fill=CREAM + (230,), anchor="mm")
            d.text((x + cw / 2, y + 40), kinds[i], font=font(8, mono=True), fill=MUTED + (190,), anchor="mm")

        frames.append(img)
    save_gif(frames, os.path.join(ASSETS, "tools-grid.gif"), duration=70)


def make_stats():
    W, H, FR = 980, 320, 44
    stats = [
        ("Product Types", 70, "70+"),
        ("UI Styles", 46, "46+"),
        ("Color Palettes", 80, "80+"),
        ("Font Pairings", 75, "75+"),
        ("Toolbox Scripts", 17, "17"),
    ]
    frames = []
    for f in range(FR):
        t = f / (FR - 1)
        img, d = new_canvas(W, H)
        dust(d, W, H, f, seed=13, n=12)
        frame_ticks(d, W, H, m=22, e=22)

        fnt = font(24, serif=True)
        txt = "T H E   D A T A"
        bb = d.textbbox((0, 0), txt, font=fnt)
        d.text(((W - (bb[2] - bb[0])) / 2, 24), txt, font=fnt, fill=GOLD_PALE + (220,))
        d.rectangle([W / 2 - 60, 58, W / 2 + 60, 59], fill=GOLD + (90,))

        bx0, bar_w = 250, W - 420
        y0, bh, gap = 82, 20, 38
        for i, (label, val, disp) in enumerate(stats):
            y = y0 + i * (bh + gap)
            d.text((26, y), label, font=font(15, serif=True), fill=CREAM + (215,), anchor="lm")
            d.rounded_rectangle([bx0, y - bh / 2, bx0 + bar_w, y + bh / 2], radius=10,
                                fill=(16, 16, 22, 255), outline=GOLD + (36,), width=1)
            start = 0.08 + i * 0.06
            prog = min(1.0, max(0.0, (t - start) / (1 - start)))
            ease = 1 - (1 - prog) ** 2
            wfrac = bar_w * ease
            col = lerp_color(GOLD, GOLD_PALE, 0.35)
            d.rounded_rectangle([bx0, y - bh / 2, bx0 + wfrac, y + bh / 2], radius=10,
                                fill=col + (255,))
            d.rectangle([bx0, y - bh / 2, bx0 + wfrac, y - bh / 2 + 3], fill=GOLD_PALE + (70,))
            d.text((bx0 + wfrac + 14, y), disp, font=font(16, mono=True), fill=GOLD_PALE + (235,), anchor="lm")
            if wfrac > 20:
                bx = bx0 + wfrac - 2
                d.ellipse([bx - 4, y - 4, bx + 4, y + 4], fill=GOLD_PALE + (190,))

        d.text((W / 2, H - 26), "curated from the cyber-rage design database",
               font=font(11, mono=True), fill=MUTED + (170,), anchor="mm")
        frames.append(img)
    save_gif(frames, os.path.join(ASSETS, "stats-bars.gif"), duration=65)


if __name__ == "__main__":
    make_hero()
    make_tools()
    make_stats()
