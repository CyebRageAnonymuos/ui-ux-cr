#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copy Generator - Generate UI microcopy, headlines, CTAs, placeholders,
error messages, empty states, and A/B test variants
Cyber-Rage Design Intelligence Engine

Usage: python copy_generator.py --headline saas
       python copy_generator.py --cta --count 8
       python copy_generator.py --error --product "checkout"
       python copy_generator.py --empty --count 3
"""

import argparse
import random
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


HEADLINES = {
    "saas": [
        "Build faster. Ship smarter.",
        "The platform your team will actually love.",
        "Work less. Accomplish more.",
        "Your all-in-one workspace for modern teams.",
        "From idea to launch in days, not months.",
        "Simplify the complex. Automate the rest.",
        "Where great products get built.",
        "Stop juggling tools. Start shipping.",
    ],
    "ecommerce": [
        "Shop the collection everyone's talking about.",
        "Quality you can feel. Prices you'll love.",
        "Your cart called. It's ready for better.",
        "New drops, zero regrets.",
        "Elevate your everyday.",
        "Good things come to those who shop.",
    ],
    "portfolio": [
        "Designing products that people love.",
        "I turn ideas into delightful experiences.",
        "Creative, code-savvy, and deadline-proof.",
        "Let's build something people remember.",
        "Pixel-perfect. Purpose-driven.",
    ],
    "health": [
        "Feel better every day.",
        "Your health, simplified.",
        "Wellness that fits your life.",
        "Small steps. Big change.",
        "Because you deserve to feel your best.",
    ],
    "fintech": [
        "Your money, beautifully managed.",
        "Banking that keeps up with you.",
        "Grow wealth without the guesswork.",
        "Smart money moves, made simple.",
        "Control your finances, not the other way around.",
    ],
    "startup": [
        "The future is being built here.",
        "Disrupt the status quo.",
        "Move fast. Build amazing things.",
        "Where bold ideas become reality.",
        "The next big thing starts now.",
    ],
    "education": [
        "Learn anything. Master everything.",
        "Knowledge at your pace.",
        "Unlock your potential, one lesson at a time.",
        "Education without limits.",
        "Learn today. Lead tomorrow.",
    ],
    "travel": [
        "Adventure awaits.",
        "Pack light. Travel far.",
        "Your next journey starts here.",
        "Discover the world on your terms.",
        "Book now. Explore forever.",
    ],
}


CTAS = [
    "Get Started", "Start Free Trial", "Sign Up Free", "Get Started Now",
    "Start Now", "Join Today", "Create Account", "Get Access",
    "Try It Free", "Explore Now", "Learn More", "See How It Works",
    "Shop Now", "Buy Now", "Add to Cart", "Claim Your Offer",
    "Get the Deal", "Start Saving", "Get 20% Off", "Book Now",
    "Reserve Your Spot", "Join the Waitlist", "Get Early Access",
    "Upgrade Now", "Start Pro", "Unlock Premium", "Boost Your Results",
    "Watch Demo", "View Pricing", "Talk to Sales", "Request a Demo",
    "Subscribe", "Stay Updated", "Get Updates", "Download Now",
    "Start Building", "Deploy Now", "Go Live", "Launch Your Site",
]


PLACEHOLDERS = {
    "email": "you@example.com", "name": "Jane Doe", "first": "Jane", "last": "Doe",
    "password": "Enter your password", "search": "Search...", "phone": "+1 (555) 000-0000",
    "username": "jane_doe", "company": "Acme Inc.", "title": "e.g. Senior Designer",
    "bio": "Tell us a little about yourself", "message": "Type your message...",
    "location": "City, Country", "url": "https://your-site.com", "date": "MM/DD/YYYY",
    "card": "1234 5678 9012 3456", "cvv": "123", "amount": "0.00", "tag": "Add a tag...",
}


ERRORS = {
    "form": [
        "Something went wrong. Please try again.",
        "We couldn't save your changes.",
        "There was a problem. Please refresh and retry.",
        "Oops! That didn't work. Try again in a moment.",
    ],
    "auth": [
        "Incorrect email or password.",
        "This email is already registered.",
        "Your session expired. Please sign in again.",
        "Too many attempts. Try again in 60 seconds.",
    ],
    "checkout": [
        "Payment failed. Please check your card details.",
        "This card was declined. Try another payment method.",
        "Your order couldn't be processed. Please try again.",
        "Insufficient funds. Please use a different card.",
    ],
    "network": [
        "No internet connection. Check your network and retry.",
        "Connection lost. Reconnecting...",
        "We're having trouble reaching our servers. Try again soon.",
    ],
    "upload": [
        "File too large. Maximum size is 10MB.",
        "Unsupported file type. Please upload a valid file.",
        "Upload failed. Please try again.",
    ],
    "generic": [
        "Something went wrong on our end. Please try again later.",
        "We hit a snag. Your request couldn't be completed.",
    ],
}


EMPTY_STATES = [
    ("No results found", "Try adjusting your search or filters.", "search"),
    ("Nothing here yet", "Create your first item to get started.", "plus"),
    ("Your inbox is empty", "You're all caught up!", "mail"),
    ("No notifications", "We'll let you know when something happens.", "bell"),
    ("No items in cart", "Browse our best sellers and add something you love.", "cart"),
    ("You're up to date", "Check back later for new updates.", "check"),
    ("No messages yet", "Start the conversation — say hello!", "chat"),
    ("No favorites yet", "Tap the heart on anything you like.", "heart"),
]


SUCCESS_TOASTS = [
    "Saved!", "Done!", "All set!", "Changes saved.", "Upload complete.",
    "Message sent.", "Order confirmed!", "Payment successful!",
    "Account created. Welcome aboard!", "Invite sent.",
]


def pick(items, count):
    if count >= len(items):
        return items
    return random.sample(items, count)


def print_headline(category, count):
    print(f"# Headline ideas ({category})")
    for h in pick(HEADLINES[category], count):
        print(f"  • {h}")
    print()


def print_cta(count):
    print("# CTA button text")
    for c in pick(CTAS, count):
        print(f"  • {c}")
    print()


def print_placeholder(count):
    print("# Placeholder text")
    for k, v in pick(list(PLACEHOLDERS.items()), count):
        print(f"  • {v}  ({k})")
    print()


def print_errors(category, count):
    print(f"# Error messages ({category})")
    for e in pick(ERRORS[category], count):
        print(f"  • {e}")
    print()


def print_empty(count):
    print("# Empty states")
    for title, desc, icon in pick(EMPTY_STATES, count):
        print(f"  • {title} — {desc}")
    print()


def print_toasts(count):
    print("# Success toasts")
    for t in pick(SUCCESS_TOASTS, count):
        print(f"  • {t}")
    print()


def print_variants(count):
    print("# A/B test variants for 'Get Started'")
    variants = [
        "Get Started", "Start Free", "Try Free", "Start Now", "Create Account",
        "Sign Up Free", "Get Access", "Join Free", "Start Building", "Go Free",
        "Start Your Trial", "Launch Now",
    ]
    chosen = pick(variants, count)
    # Pair consecutive variants into real A/B arms - a list where every
    # row is labeled "A" isn't an A/B test.
    for i in range(0, len(chosen) - 1, 2):
        print(f"  A: {chosen[i]}   vs   B: {chosen[i + 1]}")
    if len(chosen) % 2:
        print(f"  (unpaired: {chosen[-1]})")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy Generator - Cyber-Rage")
    parser.add_argument("--headline", help=f"Headline category ({', '.join(HEADLINES.keys())})")
    parser.add_argument("--cta", action="store_true", help="Generate CTA button text")
    parser.add_argument("--placeholder", action="store_true", help="Generate placeholder text")
    parser.add_argument("--error", help=f"Error category ({', '.join(ERRORS.keys())})")
    parser.add_argument("--empty", action="store_true", help="Generate empty states")
    parser.add_argument("--toast", action="store_true", help="Generate success toasts")
    parser.add_argument("--ab", action="store_true", help="Generate A/B test variants")
    parser.add_argument("--count", type=int, default=5, help="Number of items (default: 5)")
    parser.add_argument("--seed", type=int, help="Random seed for reproducible output")

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.headline:
        if args.headline not in HEADLINES:
            print(f"Unknown category: '{args.headline}'. Available: {', '.join(HEADLINES.keys())}")
            sys.exit(1)
        print_headline(args.headline, args.count)
    elif args.cta:
        print_cta(args.count)
    elif args.placeholder:
        print_placeholder(args.count)
    elif args.error:
        if args.error not in ERRORS:
            print(f"Unknown category: '{args.error}'. Available: {', '.join(ERRORS.keys())}")
            sys.exit(1)
        print_errors(args.error, args.count)
    elif args.empty:
        print_empty(args.count)
    elif args.toast:
        print_toasts(args.count)
    elif args.ab:
        print_variants(args.count)
    else:
        print("Specify one of: --headline, --cta, --placeholder, --error, --empty, --toast, --ab")
        print("Example: python copy_generator.py --headline saas --count 3")
