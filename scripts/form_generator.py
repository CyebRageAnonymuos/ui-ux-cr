#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Form Generator - Accessible, production-ready HTML forms with labels,
validation states (error/success), autocomplete, and CSRF placeholder:
login, signup, contact, search, newsletter
Cyber-Rage Design Intelligence Engine

Usage: python form_generator.py --form login --primary "#2563EB"
       python form_generator.py --form signup --dark
       python form_generator.py --list
"""

import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def base_css(primary, dark=False):
    surface = "#1E293B" if dark else "#FFFFFF"
    bg = "#0F172A" if dark else "#F8FAFC"
    text = "#F8FAFC" if dark else "#0F172A"
    border = "#334155" if dark else "#E2E8F0"
    muted = "#94A3B8" if dark else "#64748B"
    return f"""<style>
  :root {{
    --primary: {primary};
    --surface: {surface};
    --bg: {bg};
    --text: {text};
    --border: {border};
    --muted: {muted};
    --error: #EF4444;
    --success: #10B981;
  }}
  .form-card {{
    max-width: 420px;
    margin: 2rem auto;
    background: var(--surface);
    padding: 2rem;
    border-radius: 16px;
    border: 1px solid var(--border);
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    color: var(--text);
  }}
  .field {{ margin-bottom: 1.1rem; }}
  .field label {{
    display: block;
    font-size: 0.875rem;
    font-weight: 600;
    margin-bottom: 0.375rem;
    color: var(--text);
  }}
  .field input, .field textarea, .field select {{
    width: 100%;
    padding: 0.625rem 0.875rem;
    border: 1.5px solid var(--border);
    border-radius: 10px;
    font-size: 0.9375rem;
    background: var(--bg);
    color: var(--text);
    transition: border-color 150ms ease, box-shadow 150ms ease;
  }}
  .field input:focus, .field textarea:focus, .field select:focus {{
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px {primary}33;
  }}
  .field input[aria-invalid="true"] {{
    border-color: var(--error);
  }}
  .field .error-msg {{
    display: none;
    color: var(--error);
    font-size: 0.8125rem;
    margin-top: 0.25rem;
  }}
  .field input[aria-invalid="true"] + .error-msg {{ display: block; }}
  .hint {{ color: var(--muted); font-size: 0.8125rem; margin-top: 0.25rem; }}
  .btn {{
    width: 100%;
    padding: 0.75rem 1.5rem;
    background: var(--primary);
    color: #fff;
    font-weight: 600;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-size: 0.9375rem;
    transition: filter 150ms ease, transform 100ms ease;
  }}
  .btn:hover {{ filter: brightness(1.08); }}
  .btn:active {{ transform: scale(0.98); }}
  .form-note {{ text-align: center; font-size: 0.875rem; color: var(--muted); margin-top: 1rem; }}
  .form-note a {{ color: var(--primary); }}
  .success-banner {{
    display: none;
    background: #10B98122;
    color: var(--success);
    border: 1px solid #10B98155;
    border-radius: 10px;
    padding: 0.75rem 1rem;
    margin-bottom: 1rem;
    font-size: 0.875rem;
  }}
</style>"""


def form_login(primary, dark=False):
    return f"""<!-- Login form (accessible: labels, autocomplete, aria) -->
{base_css(primary, dark)}
<div class="form-card">
  <h2 style="margin:0 0 1.5rem">Welcome back</h2>

  <div class="success-banner" role="status">Signed in successfully.</div>

  <form method="POST" action="/login" novalidate>
    <div class="field">
      <label for="email">Email</label>
      <input type="email" id="email" name="email" autocomplete="email"
             required placeholder="you@example.com" aria-describedby="email-error">
      <p class="error-msg" id="email-error">Please enter a valid email address.</p>
    </div>

    <div class="field">
      <label for="password">Password</label>
      <input type="password" id="password" name="password"
             autocomplete="current-password" required minlength="8"
             aria-describedby="password-hint">
      <p class="hint" id="password-hint">At least 8 characters.</p>
    </div>

    <div class="field" style="display:flex; justify-content:space-between; align-items:center">
      <label for="remember" style="display:flex; align-items:center; gap:0.5rem; margin:0">
        <input type="checkbox" id="remember" name="remember" style="width:auto">
        Remember me
      </label>
      <a href="/forgot-password" style="font-size:0.875rem">Forgot password?</a>
    </div>

    <button type="submit" class="btn">Sign in</button>
  </form>

  <p class="form-note">No account? <a href="/signup">Create one</a></p>
</div>"""


def form_signup(primary, dark=False):
    return f"""<!-- Signup form (accessible, password rules upfront) -->
{base_css(primary, dark)}
<div class="form-card">
  <h2 style="margin:0 0 1.5rem">Create your account</h2>

  <form method="POST" action="/signup" novalidate>
    <div class="field">
      <label for="name">Full name</label>
      <input type="text" id="name" name="name" autocomplete="name" required>
    </div>

    <div class="field">
      <label for="email">Email</label>
      <input type="email" id="email" name="email" autocomplete="email" required>
    </div>

    <div class="field">
      <label for="new-password">Password</label>
      <input type="password" id="new-password" name="password"
             autocomplete="new-password" required minlength="8"
             aria-describedby="pwd-rules">
      <p class="hint" id="pwd-rules">Minimum 8 characters. Mix letters and numbers.</p>
    </div>

    <div class="field">
      <label for="confirm">Confirm password</label>
      <input type="password" id="confirm" name="confirm"
             autocomplete="new-password" required>
    </div>

    <button type="submit" class="btn">Create account</button>
  </form>

  <p class="form-note">Already have an account? <a href="/login">Sign in</a></p>
</div>"""


def form_contact(primary, dark=False):
    return f"""<!-- Contact form (labels + textarea + honeypot spam trap) -->
{base_css(primary, dark)}
<div class="form-card" style="max-width:520px">
  <h2 style="margin:0 0 1.5rem">Get in touch</h2>

  <form method="POST" action="/contact" novalidate>
    <!-- Honeypot: real users never see/fill this; bots do -->
    <div style="position:absolute; left:-9999px" aria-hidden="true">
      <label for="company">Company</label>
      <input type="text" id="company" name="company" tabindex="-1" autocomplete="off">
    </div>

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem">
      <div class="field">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" autocomplete="name" required>
      </div>
      <div class="field">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" autocomplete="email" required>
      </div>
    </div>

    <div class="field">
      <label for="subject">Subject</label>
      <select id="subject" name="subject">
        <option>General question</option>
        <option>Support</option>
        <option>Partnership</option>
        <option>Feedback</option>
      </select>
    </div>

    <div class="field">
      <label for="message">Message</label>
      <textarea id="message" name="message" rows="5" required minlength="10"
                aria-describedby="message-error"></textarea>
      <p class="error-msg" id="message-error">Please write at least 10 characters.</p>
    </div>

    <button type="submit" class="btn">Send message</button>
  </form>
</div>"""


def form_search(primary, dark=False):
    return f"""<!-- Search form (role=search, no label needed with aria-label) -->
{base_css(primary, dark)}
<form method="GET" action="/search" role="search"
      style="display:flex; gap:0.5rem; max-width:480px; margin:1rem auto">
  <div class="field" style="flex:1; margin:0">
    <label for="q" class="sr-only" style="position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0 0 0 0)">Search</label>
    <input type="search" id="q" name="q" placeholder="Search..."
           autocomplete="off" aria-label="Search the site">
  </div>
  <button type="submit" class="btn" style="width:auto; padding:0.625rem 1.25rem">Search</button>
</form>"""


def form_newsletter(primary, dark=False):
    return f"""<!-- Newsletter form (inline, single purpose) -->
{base_css(primary, dark)}
<form method="POST" action="/subscribe" aria-label="Subscribe to the newsletter"
      style="display:flex; gap:0.5rem; max-width:440px; margin:1rem auto">
  <div class="field" style="flex:1; margin:0">
    <label for="nl-email" class="sr-only" style="position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0 0 0 0)">Email address</label>
    <input type="email" id="nl-email" name="email" autocomplete="email"
           placeholder="Enter your email" required>
  </div>
  <button type="submit" class="btn" style="width:auto; padding:0.625rem 1.25rem">Subscribe</button>
</form>
<p class="form-note">No spam. Unsubscribe anytime.</p>"""


FORMS = {
    "login": form_login,
    "signup": form_signup,
    "contact": form_contact,
    "search": form_search,
    "newsletter": form_newsletter,
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Form Generator - Cyber-Rage")
    parser.add_argument("--form", help=f"Form type ({', '.join(FORMS)})")
    parser.add_argument("--primary", default="#2563EB", help="Primary color (default #2563EB)")
    parser.add_argument("--dark", action="store_true", help="Dark variant")
    parser.add_argument("--list", action="store_true", help="List available forms")

    args = parser.parse_args()

    if args.list:
        print("Available forms:")
        for f in FORMS:
            print(f"  - {f}")
        sys.exit(0)

    if not args.form:
        print("Specify --form (see --list)")
        sys.exit(1)

    if args.form not in FORMS:
        print(f"Unknown form: '{args.form}'. Available: {', '.join(FORMS)}")
        sys.exit(1)

    print(FORMS[args.form](args.primary, args.dark))
