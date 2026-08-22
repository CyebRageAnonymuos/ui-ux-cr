#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Email Template Generator - Responsive, table-based HTML emails that
survive Gmail/Outlook: welcome, password reset, receipt, newsletter
Cyber-Rage Design Intelligence Engine

Usage: python email_template.py --type welcome --brand "Acme" --primary "#2563EB"
       python email_template.py --type reset --brand "Acme"
       python email_template.py --list
"""

import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def email_shell(brand, primary, body_rows, preview_text):
    """Table-based shell: the only layout email clients render reliably."""
    return f"""<!-- {esc(brand)} email - table-based for Gmail/Outlook -->
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <title>{esc(brand)}</title>
  <!--[if mso]><style>body,table,td {{ font-family: Arial, sans-serif !important; }}</style><![endif]-->
</head>
<body style="margin:0; padding:0; background:#F1F5F9; -webkit-text-size-adjust:100%;">
  <!-- Preheader: shows in the inbox preview line -->
  <div style="display:none; max-height:0; overflow:hidden;">{esc(preview_text)}</div>

  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F1F5F9; padding:24px 12px;">
    <tr>
      <td align="center">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0"
               style="max-width:600px; width:100%; background:#FFFFFF; border-radius:12px; overflow:hidden;">

          <!-- Header -->
          <tr>
            <td style="background:{primary}; padding:28px 32px; text-align:center;">
              <span style="color:#FFFFFF; font-family:Arial,sans-serif; font-size:22px; font-weight:bold; letter-spacing:1px;">
                {esc(brand)}
              </span>
            </td>
          </tr>

          <!-- Body -->
{body_rows}

          <!-- Footer -->
          <tr>
            <td style="padding:24px 32px; background:#F8FAFC; border-top:1px solid #E2E8F0;
                       font-family:Arial,sans-serif; font-size:12px; color:#64748B; text-align:center;">
              You received this email because you have an account at {esc(brand)}.<br>
              <a href="#" style="color:#64748B;">Unsubscribe</a> &middot;
              <a href="#" style="color:#64748B;">Privacy policy</a><br><br>
              &copy; 2026 {esc(brand)}. All rights reserved.
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>"""


def email_welcome(brand, primary):
    body = f"""          <tr>
            <td style="padding:32px; font-family:Arial,sans-serif; color:#0F172A;">
              <h2 style="margin:0 0 12px; font-size:20px;">Welcome aboard!</h2>
              <p style="margin:0 0 16px; font-size:15px; line-height:1.6; color:#334155;">
                Thanks for joining <strong>{esc(brand)}</strong>. Your account is ready -
                here are three things to try first:
              </p>
              <ol style="margin:0 0 20px 20px; padding:0; font-size:15px; line-height:1.9; color:#334155;">
                <li>Complete your profile</li>
                <li>Explore the dashboard</li>
                <li>Invite a teammate</li>
              </ol>
              <!-- Button: rounded corners degrade safely to squares in Outlook -->
              <table role="presentation" cellpadding="0" cellspacing="0">
                <tr>
                  <td style="background:{primary}; border-radius:8px;">
                    <a href="https://example.com/dashboard"
                       style="display:inline-block; padding:12px 28px; color:#FFFFFF;
                              font-family:Arial,sans-serif; font-size:15px; font-weight:bold;
                              text-decoration:none;">
                      Go to dashboard &rarr;
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>"""
    return email_shell(brand, primary, body, "Your account is ready - 3 things to try first.")


def email_reset(brand, primary):
    body = f"""          <tr>
            <td style="padding:32px; font-family:Arial,sans-serif; color:#0F172A;">
              <h2 style="margin:0 0 12px; font-size:20px;">Reset your password</h2>
              <p style="margin:0 0 16px; font-size:15px; line-height:1.6; color:#334155;">
                We received a request to reset the password for your {esc(brand)} account.
                Click the button below - the link is valid for <strong>30 minutes</strong>.
              </p>
              <table role="presentation" cellpadding="0" cellspacing="0">
                <tr>
                  <td style="background:{primary}; border-radius:8px;">
                    <a href="https://example.com/reset?token=RESET_TOKEN"
                       style="display:inline-block; padding:12px 28px; color:#FFFFFF;
                              font-family:Arial,sans-serif; font-size:15px; font-weight:bold;
                              text-decoration:none;">
                      Reset password
                    </a>
                  </td>
                </tr>
              </table>
              <p style="margin:20px 0 0; font-size:13px; line-height:1.6; color:#64748B;">
                If the button doesn't work, paste this link into your browser:<br>
                <a href="https://example.com/reset?token=RESET_TOKEN" style="color:{primary}; word-break:break-all;">
                  https://example.com/reset?token=RESET_TOKEN
                </a><br><br>
                If you didn't request this, you can safely ignore this email -
                your password stays unchanged.
              </p>
            </td>
          </tr>"""
    return email_shell(brand, primary, body, "Reset your password (link valid for 30 minutes).")


def email_receipt(brand, primary):
    row = lambda item, qty, price: f"""                <tr>
                  <td style="padding:8px 0; font-size:14px; color:#334155;">{esc(item)} &times; {qty}</td>
                  <td style="padding:8px 0; font-size:14px; color:#0F172A; text-align:right;">{price}</td>
                </tr>"""
    body = f"""          <tr>
            <td style="padding:32px; font-family:Arial,sans-serif; color:#0F172A;">
              <h2 style="margin:0 0 4px; font-size:20px;">Receipt</h2>
              <p style="margin:0 0 20px; font-size:13px; color:#64748B;">Order #1042 &middot; Jan 12, 2026</p>

              <table role="presentation" width="100%" cellpadding="0" cellspacing="0"
                     style="border-top:1px solid #E2E8F0; border-bottom:1px solid #E2E8F0; margin-bottom:20px;">
{row("Pro plan (monthly)", 1, "$29.00")}{row("Extra seat", 2, "$12.00")}
              </table>

              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td style="font-size:16px; font-weight:bold; color:#0F172A;">Total</td>
                  <td style="font-size:16px; font-weight:bold; color:#0F172A; text-align:right;">$53.00</td>
                </tr>
              </table>

              <p style="margin:24px 0 0; font-size:13px; color:#64748B;">
                Charged to Visa ending 4242. Questions? Just reply to this email.
              </p>
            </td>
          </tr>"""
    return email_shell(brand, primary, body, "Your receipt for order #1042.")


def email_newsletter(brand, primary):
    article = lambda title, teaser: f"""                <tr>
                  <td style="padding:0 0 20px;">
                    <h3 style="margin:0 0 6px; font-size:16px;">
                      <a href="#" style="color:{primary}; text-decoration:none;">{esc(title)}</a>
                    </h3>
                    <p style="margin:0; font-size:14px; line-height:1.6; color:#334155;">{esc(teaser)}</p>
                  </td>
                </tr>"""
    body = f"""          <tr>
            <td style="padding:32px; font-family:Arial,sans-serif; color:#0F172A;">
              <h2 style="margin:0 0 20px; font-size:20px;">This week at {esc(brand)}</h2>
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
{article("Design systems that scale", "How small teams keep tokens consistent across five products.")}{article("Shipping faster with fewer bugs", "Our checklist for release week - steal it.")}
              </table>
              <table role="presentation" cellpadding="0" cellspacing="0">
                <tr>
                  <td style="background:{primary}; border-radius:8px;">
                    <a href="#" style="display:inline-block; padding:10px 22px; color:#FFFFFF;
                              font-family:Arial,sans-serif; font-size:14px; font-weight:bold; text-decoration:none;">
                      Read all posts
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>"""
    return email_shell(brand, primary, body, "Two new posts + a release checklist you can steal.")


EMAIL_TYPES = {
    "welcome": email_welcome,
    "reset": email_reset,
    "receipt": email_receipt,
    "newsletter": email_newsletter,
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Email Template Generator - Cyber-Rage")
    parser.add_argument("--type", help=f"Email type ({', '.join(EMAIL_TYPES)})")
    parser.add_argument("--brand", default="Acme", help="Brand name (default 'Acme')")
    parser.add_argument("--primary", default="#2563EB", help="Primary color (default #2563EB)")
    parser.add_argument("--out", help="Write to file instead of stdout")
    parser.add_argument("--list", action="store_true", help="List available email types")

    args = parser.parse_args()

    if args.list:
        print("Email types:")
        for t in EMAIL_TYPES:
            print(f"  - {t}")
        sys.exit(0)

    if not args.type:
        print("Specify --type (see --list)")
        sys.exit(1)

    if args.type not in EMAIL_TYPES:
        print(f"Unknown email type: '{args.type}'. Available: {', '.join(EMAIL_TYPES)}")
        sys.exit(1)

    html = EMAIL_TYPES[args.type](args.brand, args.primary)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Email written to {args.out} ({len(html)} bytes)")
    else:
        print(html)
