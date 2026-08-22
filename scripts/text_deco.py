#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text Decorator - Fancy Unicode fonts + decorative shapes (emoji-free)
Cyber-Rage Design Intelligence Engine

Usage:
  python3 text_deco.py --text "Hello" --style gothic
  python3 text_deco.py --text "SALE" --style bubble
  python3 text_deco.py --divider wave
  python3 text_deco.py --frame "TITLE" --frame-style double
  python3 scripts/text_deco.py --symbols stars
  python3 text_deco.py --bar 70
  python3 text_deco.py --rating 4
  python3 text_deco.py --styles
"""

import argparse
import sys
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ============================================================
# UNICODE FONT STYLES
# ============================================================

_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_LOWER = "abcdefghijklmnopqrstuvwxyz"
_DIGITS = "0123456789"


def _map_style(upper, lower="", digits=""):
    return {"upper": upper, "lower": lower or upper, "digits": digits}


# Mathematical alphanumeric symbols + letterlike maps
STYLES = {
    "gothic": _map_style(
        "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ",
        "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"),
    "gothic-bold": _map_style(
        "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅",
        "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"),
    "script": _map_style(
        "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵",
        "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"),
    "script-bold": _map_style(
        "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩",
        "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"),
    "double-struck": _map_style(
        "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
        "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
        "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"),
    "monospace": _map_style(
        "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉",
        "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
        "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"),
    "serif-bold": _map_style(
        "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙",
        "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
        "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"),
    "serif-italic": _map_style(
        "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍",
        "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧"),
    "serif-bold-italic": _map_style(
        "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁",
        "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛"),
    "sans-bold": _map_style(
        "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭",
        "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇",
        "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"),
    "sans-italic": _map_style(
        "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡",
        "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"),
    "sans-bold-italic": _map_style(
        "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕",
        "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯"),
    "bubble": _map_style(
        "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ",
        "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ",
        "⓿❶❷❸❹❺❻❼❽❾"),
    "bubble-dark": _map_style(
        "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩",
        "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"),
    "square": _map_style(
        "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉",
        "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"),
    "square-dark": _map_style(
        "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉",
        "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉"),
    "aesthetic": _map_style(
        "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ",
        "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",
        "０１２３４５６７８９"),
    "small-caps": _map_style(
        "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀsᴛᴜᴠᴡxʏᴢ",
        "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀsᴛᴜᴠᴡxʏᴢ"),
    "inverted": _map_style(
        "∀qƆpƎℲ⅁HIſʞ˥WNOԀQɹS⊥∩ΛMX⅄Z",
        "ɐqɔpǝɟƃɥıɾʞlɯuodbɹsʇnʌʍxʎz",
        "0ƖᄅƐㄣϛ9ㄥ86"),
    "mirrored": _map_style(
        "ABↃDƎꟻGHІJK⅃MNOꟼQЯSTUVWXYZ",
        "ɒdɔbɘʇϱʜiꞁʞlmnoqpɿƨƚuvwxyz"),
    "currency": _map_style(
        "₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩XɎⱫ",
        "₳ƀȼđɇfǥħɨɉꝅłmnøᵽqɍȿŧʉvwxɏƶ"),
}

# Combining-mark styles (applied per character)
COMBINING = {
    "strike": "\u0336",
    "underline": "\u0332",
    "double-underline": "\u0333",
    "overline": "\u0305",
    "dotted": "\u0307",
    "slash": "\u0338",
    "wave": "\u0330",
}


def style_text(text, style):
    """Convert text to a fancy Unicode style."""
    if style in COMBINING:
        mark = COMBINING[style]
        return "".join(ch + mark for ch in text)
    if style == "spaced":
        return " ".join(list(text))
    if style not in STYLES:
        raise SystemExit(f"Unknown style: {style}. Use --styles to list all.")
    m = STYLES[style]
    out = []
    for ch in text:
        if ch in _UPPER:
            i = _UPPER.index(ch)
            out.append(m["upper"][i])
        elif ch in _LOWER:
            i = _LOWER.index(ch)
            out.append(m["lower"][i])
        elif ch in _DIGITS and m["digits"]:
            i = _DIGITS.index(ch)
            out.append(m["digits"][i])
        else:
            out.append(ch)
    return "".join(out)


def list_styles():
    print("Available font styles:\n")
    demo = "Abc 123"
    for name in STYLES:
        print(f"  {name:<18} {style_text(demo, name)}")
    for name in COMBINING:
        print(f"  {name:<18} {style_text(demo, name)}")
    print(f"  {'spaced':<18} {style_text(demo, 'spaced')}")
    print(f"\nTotal: {len(STYLES) + len(COMBINING) + 1} styles")


# ============================================================
# DECORATIVE SHAPES (emoji-free)
# ============================================================

DIVIDERS = {
    "line":     "─" * 40,
    "double":   "═" * 40,
    "heavy":    "━" * 40,
    "dash":     "┄" * 40,
    "dot":      "·" * 40,
    "bullet":   "•" * 40,
    "wave":     "﹏" * 20,
    "tilde":    "~" * 40,
    "star":     "─✦─".center(60, "─").replace("──", "──"),
    "star-line": "─────────✦─────────",
    "diamond":  "─────────◆─────────",
    "diamond-o": "────────◇───────",
    "sparkle":  "·˚ ༘────✧──── ༘˚·",
    "flower":   "─────────❋─────────",
    "clover":   "───────❖───────",
    "arrow":    "═══════➤",
    "chevron":  "»»»»»»»»»»»»»»»»»»»»",
    "blocks":   "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁",
    "checker":  "▚▚▚▚▚▚▚▚▚▚▚▚▚▚▚▚▚▚▚▚",
    "diag":     "▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞",
    "shade-l":  "░" * 40,
    "shade-m":  "▒" * 40,
    "shade-h":  "▓" * 40,
    "solid":    "█" * 40,
    "bracket":  "╞══════════════════════╡",
    "ornate":   "╔════════════◆════════════╗",
    "circuit":  "─┤├──┤├──┤├──┤├──┤├─",
    "rune":     "ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛏᛒᛖᛗᛚᛜᛞᛟ",
    "greek":    "αβγδεζηθικλμνξοπρστυφχψω",
    "dots-hi":  "⣿" * 20,
    "braille":  "⠋⠛⠹⠸⠼⠴⠦⠧⠇⠏" * 2,
    "triangles":"◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤",
    "zigzag":   "∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧",
    "mountain": "/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\",
    "knot":     "═══╦═══╦═══╦═══╦═══",
    "chain":    "─○───●───○───●───○───",
    "moons":    "☾────☽────☾────☽",
    "cards":    "♠────♣────♥────♦",
    "arrows-dn":"↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓",
}

SYMBOLS = {
    "stars": ["★", "☆", "✦", "✧", "✩", "✪", "✫", "✬", "✭", "✮", "✯", "✰", "⋆", "✵", "✶", "✷", "✸", "✹", "✺", "⁂"],
    "arrows": ["→", "←", "↑", "↓", "⇒", "⇐", "➜", "➤", "▶", "◀", "▲", "▼", "»", "«", "↠", "⇢", "⇝", "⟶", "⟹", "↳", "↰", "⇀", "↼", "↔", "⇄", "⤴", "⤵", "➔", "➟", "➡", "➢", "➣", "➥", "➦", "➨"],
    "geometric": ["■", "□", "▪", "▫", "▬", "▲", "►", "▼", "◄", "◆", "◇", "○", "●", "◐", "◑", "◒", "◓", "◢", "◣", "◤", "◥", "◈", "◉", "⊙", "⊚", "⊛", "⬟", "⬢", "⬡"],
    "status": ["✓", "✔", "✗", "✘", "☑", "☒", "√", "×", "✕", "✖", "⍻", "⚠", "⌛", "⏳", "⚑", "⚐", "⚑", "⚓", "⚔", "⚙", "⚗", "⚛", "⚜"],
    "boxes": ["「」", "『』", "【】", "〖〗", "《》", "〈〉", "⟦⟧", "⟪⟫", "⌈⌉", "⌊⌋", "︵︶", "﹁﹂", "﹃﹄"],
    "music": ["♪", "♫", "♬", "♩", "♭", "♮", "♯", "𝄞", "𝄢"],
    "misc": ["°", "†", "‡", "§", "¶", "©", "®", "™", "№", "℗", "⅍", "Ω", "∞", "µ", "π", "Δ", "Σ", "Φ", "Ψ", "Θ", "Λ", "Ξ", "Γ"],
    "cards": ["♠", "♣", "♥", "♦", "♤", "♧", "♡", "♢", "⚀", "⚁", "⚂", "⚃", "⚄", "⚅"],
    "technical": ["⌘", "⌥", "⌫", "⎋", "⇧", "␣", "⏎", "⇥", "⌦", "⌧", "⎘", "⎚", "⌨", "⌚", "⌇", "⌁", "⌌", "⌍", "⌎", "⌏"],
    "math": ["∀", "∂", "∃", "∅", "∇", "∈", "∉", "∋", "∏", "∑", "−", "∓", "∗", "∘", "∝", "∞", "∠", "∧", "∨", "∩", "∪", "∫", "∴", "∼", "≅", "≈", "≠", "≡", "≤", "≥", "⊂", "⊃", "⊆", "⊇", "⊕", "⊗", "⊥"],
    "currency": ["$", "€", "£", "¥", "₹", "₽", "₿", "¢", "₴", "₺", "₩", "₪", "₫", "₭", "₱", "₡", "₥", "ƒ", "₠", "₢", "₣", "₤", "₦", "₧", "₨", "₩", "₪", "₫", "€", "₭", "₮", "₯", "₰", "₲", "₳", "₴", "₵", "₶", "₷", "₸", "₹", "₺", "₻", "₼", "₽", "₾", "₿"],
    "weather": ["☀", "☁", "☂", "☃", "☄", "☾", "☽", "❄", "❅", "❆", "⚡", "☍", "☏", "✇"],
    "zodiac": ["♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓"],
    "chess": ["♔", "♕", "♖", "♗", "♘", "♙", "♚", "♛", "♜", "♝", "♞", "♟"],
    "notes-dots": ["⋅", "∙", "•", "◦", "‣", "⁃", "∙", "○", "◌", "◍", "◎", "☉", "⦿", "⧂", "⧃", "⧉"],
    "superscript": ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", "⁺", "⁻", "⁼", "⁽", "⁾", "ⁿ", "ⁱ"],
    "subscript": ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₊", "₋", "₌", "₍", "₎"],
    "spinners": [["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"], ["◐", "◓", "◑", "◒"], ["▖", "▘", "▝", "▗"], ["┤", "┘", "┴", "└", "├", "┌", "┬", "┐"], ["◢", "◣", "◤", "◥"], ["◰", "◳", "◲", "◱"], ["◴", "◷", "◶", "◵"], ["◐", "◓", "◑", "◒"]],
}

FRAME_STYLES = {
    "single":   ("┌", "─", "┐", "│", "└", "┘"),
    "double":   ("╔", "═", "╗", "║", "╚", "╝"),
    "rounded":  ("╭", "─", "╮", "│", "╰", "╯"),
    "heavy":    ("┏", "━", "┓", "┃", "┗", "┛"),
    "dashed":   ("┌", "┄", "┐", "┆", "└", "┘"),
    "stars":    ("✦", "─", "✦", "│", "✦", "✦"),
    "diamond":  ("◆", "─", "◆", "│", "◆", "◆"),
    "block":    ("█", "█", "█", "█", "█", "█"),
    "shade":    ("▓", "░", "▓", "░", "▓", "▓"),
    "arrow":    ("➤", "─", "◄", "│", "➤", "◄"),
    "sparkle":  ("✧", "⋆", "✧", "·", "✧", "✧"),
    "tech":     ("◤", "─", "◥", "│", "◣", "◢"),
}


def make_frame(text, style="single", pad=2):
    tl, h, tr, v, bl, br = FRAME_STYLES.get(style, FRAME_STYLES["single"])
    inner = f"{' ' * pad}{text}{' ' * pad}"
    width = len(inner) + 2
    lines = [tl + h * width + tr]
    lines.append(v + " " + inner + " " + v)
    lines.append(bl + h * width + br)
    return "\n".join(lines)


def make_bar(percent, width=20, fill="█", empty="░"):
    percent = max(0, min(100, percent))
    filled = int(round(width * percent / 100))
    return fill * filled + empty * (width - filled)


def make_rating(score, max_score=5, full="★", empty="☆"):
    score = max(0, min(max_score, score))
    return full * score + empty * (max_score - score)


def list_dividers():
    print("Available dividers:\n")
    for name, art in DIVIDERS.items():
        print(f"  {name:<12} {art}")


def list_symbols(category=None):
    cats = [category] if category else list(SYMBOLS)
    for cat in cats:
        if cat not in SYMBOLS:
            print(f"Unknown category: {cat}. Categories: {', '.join(SYMBOLS)}")
            continue
        val = SYMBOLS[cat]
        print(f"{cat}:")
        if isinstance(val[0], list):
            for i, seq in enumerate(val):
                print(f"  [{i}] {' '.join(seq)}")
        else:
            print("  " + " ".join(val))
        print()


def main():
    p = argparse.ArgumentParser(description="Fancy Unicode fonts + decorative shapes (emoji-free)")
    p.add_argument("--text", help="Text to transform")
    p.add_argument("--style", default=None, help="Font style (see --styles)")
    p.add_argument("--styles", action="store_true", help="List all font styles")
    p.add_argument("--divider", help="Print a divider (see --dividers)")
    p.add_argument("--dividers", action="store_true", help="List dividers")
    p.add_argument("--frame", help="Wrap text in a decorative frame")
    p.add_argument("--frame-style", default="single", help="Frame style (see --frames)")
    p.add_argument("--frames", action="store_true", help="List frame styles")
    p.add_argument("--symbols", nargs="?", const="__all__", metavar="CATEGORY", help="List symbol categories")
    p.add_argument("--bar", type=int, metavar="PERCENT", help="Progress bar 0-100")
    p.add_argument("--bar-width", type=int, default=20)
    p.add_argument("--rating", type=int, metavar="SCORE", help="Star rating")
    p.add_argument("--max-rating", type=int, default=5)
    args = p.parse_args()

    if args.styles:
        list_styles()
    elif args.dividers:
        list_dividers()
    elif args.divider:
        art = DIVIDERS.get(args.divider)
        if art is None:
            print(f"Unknown divider: {args.divider}. Use --dividers to list all.")
        else:
            print(art)
    elif args.frames:
        print("Frame styles:", ", ".join(FRAME_STYLES))
    elif args.symbols:
        cat = None if args.symbols == "__all__" else args.symbols
        list_symbols(cat)
    elif args.bar is not None:
        label = f" {args.bar}%"
        print(make_bar(args.bar, args.bar_width) + label)
    elif args.rating is not None:
        print(make_rating(args.rating, args.max_rating))
    elif args.frame is not None:
        print(make_frame(args.frame, args.frame_style))
    elif args.text and args.style:
        print(style_text(args.text, args.style))
    elif args.text:
        # Show the text in every style
        for name in list(STYLES):
            try:
                print(f"{name:<18} {style_text(args.text, name)}")
            except Exception:
                pass
        for name in COMBINING:
            print(f"{name:<18} {style_text(args.text, name)}")
    else:
        p.print_help()


if __name__ == "__main__":
    main()
