#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Social Specs - Social media image dimension cheat sheet for
all major platforms, with safe zone and character limits
Cyber-Rage Design Intelligence Engine

Usage: python social_specs.py --platform instagram
       python social_specs.py --all
       python social_specs.py --quick
"""

import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


PLATFORMS = {
    "instagram": {
        "name": "Instagram",
        "specs": [
            ("Profile picture", "320x320", "150x150 visible", ""),
            ("Post (square)", "1080x1080", "1:1", "safe zone 700x700"),
            ("Post (portrait)", "1080x1350", "4:5", "safe zone 700x850"),
            ("Post (landscape)", "1080x566", "1.91:1", ""),
            ("Story", "1080x1920", "9:16", "top/bottom 250px = UI"),
            ("Reels", "1080x1920", "9:16", "keep text in middle 1420px"),
            ("Highlight cover", "1080x1920", "9:16", "icon in 180x180 center"),
        ],
    },
    "twitter_x": {
        "name": "Twitter / X",
        "specs": [
            ("Profile picture", "400x400", "1:1", "shows as circle"),
            ("Header banner", "1500x500", "3:1", "safe zone 1440x320"),
            ("Post image", "1600x900", "16:9", "max 5MB"),
            ("In-stream photo", "1600x900", "16:9", ""),
            ("Card image", "1200x675", "16:9", "OG card"),
        ],
    },
    "facebook": {
        "name": "Facebook",
        "specs": [
            ("Profile picture", "170x170", "1:1", "upload 320x320"),
            ("Cover photo", "820x312", "~2.63:1", "desktop; mobile 640x360"),
            ("Page post (square)", "1200x1200", "1:1", "max 50% text rule"),
            ("Link post image", "1200x630", "1.91:1", "OG image"),
            ("Story", "1080x1920", "9:16", ""),
            ("Event cover", "1920x1080", "16:9", ""),
            ("Ad (right column)", "1080x1080", "1:1", ""),
        ],
    },
    "linkedin": {
        "name": "LinkedIn",
        "specs": [
            ("Profile picture", "400x400", "1:1", ""),
            ("Banner", "1584x396", "4:1", "safe zone 1400x300"),
            ("Company logo", "300x300", "1:1", ""),
            ("Post image", "1200x627", "1.91:1", "best for feed"),
            ("Post (square)", "1080x1080", "1:1", ""),
            ("Story", "1080x1920", "9:16", ""),
            ("Article cover", "1200x627", "1.91:1", ""),
        ],
    },
    "youtube": {
        "name": "YouTube",
        "specs": [
            ("Channel avatar", "800x800", "1:1", "shows as 98x98 circle"),
            ("Channel banner", "2560x1440", "16:9", "safe area 1546x423 center"),
            ("Video thumbnail", "1280x720", "16:9", "min 640x360, max 2MB"),
            ("Video resolution", "1920x1080", "16:9", ""),
            ("Short", "1080x1920", "9:16", ""),
            ("Community post", "1080x1920", "any", "up to 4 images"),
        ],
    },
    "whatsapp": {
        "name": "WhatsApp",
        "specs": [
            ("Profile picture", "500x500", "1:1", ""),
            ("Status", "1080x1920", "9:16", "top 250px = time/UI"),
            ("Channel image", "800x800", "1:1", ""),
            ("Sticker", "512x512", "1:1", "PNG w/ transparency"),
        ],
    },
    "tiktok": {
        "name": "TikTok",
        "specs": [
            ("Profile picture", "200x200", "1:1", ""),
            ("Video", "1080x1920", "9:16", "safe zone center 1080x1440"),
            ("Cover", "1080x1920", "9:16", ""),
            ("Ad (feed)", "1080x1920", "9:16", "top/bottom 300px = UI"),
            ("Image carousel", "1080x1920", "9:16", ""),
        ],
    },
    "pinterest": {
        "name": "Pinterest",
        "specs": [
            ("Profile picture", "165x165", "1:1", ""),
            ("Pin", "1000x1500", "2:3", "ideal ratio"),
            ("Pin (square)", "1000x1000", "1:1", ""),
            ("Board cover", "600x600", "1:1", ""),
        ],
    },
    "telegram": {
        "name": "Telegram",
        "specs": [
            ("Profile picture", "640x640", "1:1", ""),
            ("Channel photo", "640x640", "1:1", ""),
            ("Sticker", "512x512", "1:1", "WebP w/ transparency"),
        ],
    },
    "discord": {
        "name": "Discord",
        "specs": [
            ("Profile picture", "128x128", "1:1", "upload 512x512"),
            ("Server icon", "512x512", "1:1", ""),
            ("Server banner", "960x540", "16:9", "Premium servers only"),
            ("Emoji", "128x128", "1:1", "max 256KB PNG/GIF"),
        ],
    },
}


CHAR_LIMITS = {
    "twitter_x": "280 (X post), 25k (article)",
    "instagram": "2200 (caption), 30 hashtags max",
    "facebook": "63206 (post), 5000 (ad headline)",
    "linkedin": "3000 (post), 220 (headline)",
    "youtube": "100 (title), 5000 (description)",
    "tiktok": "2200 (caption)",
    "pinterest": "500 (pin description)",
    "telegram": "4096 (message)",
    "whatsapp": "65536 (status up to 1024)",
}


def print_platform(name):
    if name not in PLATFORMS:
        print(f"Unknown platform: '{name}'. Available: {', '.join(PLATFORMS.keys())}")
        return
    data = PLATFORMS[name]
    print(f"### {data['name']}")
    print(f"{'Purpose':<22} {'Size':<16} {'Ratio':<10} Notes")
    print("-" * 66)
    for purpose, size, ratio, notes in data["specs"]:
        print(f"  {purpose:<20} {size:<16} {ratio:<10} {notes}")
    if name in CHAR_LIMITS:
        print(f"\n  Character limits: {CHAR_LIMITS[name]}")
    print()


def print_all():
    for name in PLATFORMS:
        print_platform(name)


def print_quick():
    print("QUICK REFERENCE (common sizes):")
    print("=" * 60)
    print("  OG Image (social share) : 1200x630  (1.91:1)")
    print("  Twitter Card            : 1200x675  (16:9)")
    print("  Instagram Post          : 1080x1080 (1:1)")
    print("  Instagram Story         : 1080x1920 (9:16)")
    print("  YouTube Thumbnail       : 1280x720  (16:9)")
    print("  Facebook Cover          : 820x312")
    print("  LinkedIn Banner         : 1584x396")
    print("  Pinterest Pin           : 1000x1500 (2:3)")
    print("  TikTok / Reels / Short  : 1080x1920 (9:16)")
    print()
    print("  Universal safe: use 1200x630 for any link share.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Social Specs - Cyber-Rage")
    parser.add_argument("--platform", help=f"Platform ({', '.join(PLATFORMS.keys())})")
    parser.add_argument("--all", action="store_true", help="Show all platforms")
    parser.add_argument("--quick", action="store_true", help="Quick reference of common sizes")

    args = parser.parse_args()

    if args.quick:
        print_quick()
    elif args.all:
        print_all()
    elif args.platform:
        print_platform(args.platform)
    else:
        print("Specify one of: --platform, --all, --quick")
        print("Example: python social_specs.py --platform instagram")
