#!/usr/bin/env python3
"""Static checks for claude-code-vs-cowork.html.

    python3 check_page.py [page.html]

Adapted from leads/accuracy-cliff/semantics-vocabulary/check_page.py. Exit 0 = clean,
1 = issues, 2 = file missing.

Two of these checks exist because of real bugs that automated validation missed and
only reading a rendered PNG caught:

  * A CSS rule `svg text{fill:var(--ink)}` **overrides** every `fill="var(--teal)"`
    presentation attribute on an individual <text> — a CSS rule always beats a
    presentation attribute. Every colour-coded label silently rendered as plain ink,
    and one label became ink-on-ink and invisible. The fix is to set the default
    fill on the SVG *container* so <text> gets it by inheritance, which a
    presentation attribute then legitimately overrides.
  * Text overflowed its containing <rect>, both sideways and below the bottom edge.

This page is authored in Artifact page form: no <!doctype>, <html>, <head> or <body>
of its own, because the publisher supplies that skeleton. It still has to render
correctly straight from disk, so `*{box-sizing:border-box}` is required rather than
relying on standards mode.

Neither the fill trap nor the geometry check is visible to an HTML validator. Run this
AND look at the renders.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Average glyph advance as a fraction of font-size. Monospace is ~15% wider than
# sans; using the sans ratio for mono under-estimates and misses clipping.
ADV_SANS, ADV_MONO = 0.52, 0.60

# Superlatives this repo does not publish, plus the specific stale claims this page
# exists to correct. If a future edit reintroduces one of these, it is a factual
# regression, not a style nit.
BANNED = [
    "most secure",
    "best-in-class",
    "#1 ",
    # Cowork left research preview on 2026-04-09. Any bare present-tense claim that
    # it is still a preview is wrong.
    "Cowork is a research preview",
    "Cowork is currently a research preview",
    "Cowork is in research preview",
    "Cowork remains a research preview",
    # Cowork IS captured in the Compliance API. The widely repeated opposite is wrong.
    "Compliance API does not cover Cowork",
    "Compliance API doesn't cover Cowork",
    "audit logs do not cover Cowork",
    # Cowork ships with every paid seat, both Team seat types.
    "Cowork requires a Premium seat",
    "Cowork is only available on Premium",
    # 30 days is the API backend deletion window, NOT a cap on saved Team/Enterprise
    # sessions, which are retained in-product until someone deletes them. This
    # conflation is the most widely repeated error about Claude retention.
    "Team and Enterprise data is deleted after 30 days",
    "Team and Enterprise data is deleted within 30 days",
    "all data is deleted after 30 days",
    # ZDR requires Anthropic to enable it per organisation; it is not a self-serve toggle
    # and is not part of the standard Enterprise plan.
    "enable zero data retention in your admin settings",
    "enable ZDR from admin settings",
    "zero data retention is included in Enterprise",
]

# Acronyms a plain-language page must expand before it leans on them. Each entry is
# (acronym, expansion): the expansion must appear at or before the acronym's first use.
FIRST_MENTION = [
    ("MCP", "Model Context Protocol"),
    ("RBAC", "role-based access control"),
    ("ZDR", "zero data retention"),
]

# Variables named in the third-party guide that first-party documentation does not
# confirm. Publishing an env var that does not exist is worse than omitting it, so the
# gate keeps them out until someone verifies them and removes the entry here.
UNVERIFIED_TOKENS = [
    "DISABLE_BUG_COMMAND",
]


def text_width(s: str, size: float, mono: bool) -> float:
    return len(s) * size * (ADV_MONO if mono else ADV_SANS)


def check(path: Path) -> int:
    h = path.read_text(encoding="utf-8")
    problems: list[str] = []
    notes: list[str] = []

    # CSS-rule checks run against a comment-stripped copy: this page *documents* the
    # fill-override trap by quoting the bad rule in a comment, which would otherwise
    # trip the check against itself.
    css = re.sub(r"/\*.*?\*/", " ", h, flags=re.S)

    # ── self-contained ────────────────────────────────────────────────────────
    # Only ASSETS break offline rendering: src= on img/script/iframe, and <link href=>.
    # A plain <a href="https://…"> text link does not — this page deliberately carries
    # a curated first-party reading list. Flag assets, not hyperlinks.
    ext = re.findall(r'\bsrc\s*=\s*"(https?://[^"]+)"', h)
    ext += re.findall(r'<link\b[^>]*\bhref\s*=\s*"(https?://[^"]+)"', h, re.I)
    if ext:
        problems += [f"external asset reference: {u}" for u in ext]
    if re.search(r"<script", h, re.I):
        problems.append("<script> tag present — page should be static")
    if re.search(r"\bcdn\b|mermaid", h, re.I):
        problems.append("cdn/mermaid reference — page must render offline")

    # ── Artifact page form ────────────────────────────────────────────────────
    # Match the tag proper, not a prefix: bare "<head" also matches "<header>".
    for tag in ("<!doctype", "<html", "<head", "<body"):
        if re.search(re.escape(tag) + r"[\s>]", h, re.I):
            problems.append(
                f"{tag}> present — the Artifact publisher supplies the skeleton; "
                "authoring one nests a second document"
            )
    if not re.search(r"\*\s*\{[^}]*box-sizing", css):
        problems.append(
            "no `*{box-sizing:border-box}` — without a doctype the file opens in "
            "quirks mode from disk and the box model shifts"
        )

    # ── the fill-override trap ────────────────────────────────────────────────
    if re.search(r"svg\s+text\s*\{[^}]*\bfill\s*:", css):
        problems.append(
            "`svg text{...fill:...}` sets fill in a CSS rule; it will override every "
            'fill="var(--x)" attribute on <text>. Put the default on `.fig-box svg` instead.'
        )
    if not re.search(r"\.fig-box svg\{[^}]*\bfill\s*:", css):
        notes.append("no default fill on `.fig-box svg` — <text> without a fill may not be themed")

    # ── hardcoded colours would break dark mode ───────────────────────────────
    hard = set(re.findall(r'(?:fill|stroke)="(#[0-9A-Fa-f]{3,6})"', h))
    if hard:
        problems.append(f"hardcoded hex in markup (breaks theming): {sorted(hard)}")

    # ── theme: all three declarations required ────────────────────────────────
    if not re.search(r"\n:root\{", h):
        problems.append("no bare :root palette")
    if not ('prefers-color-scheme:dark' in h and ':root:not([data-theme="light"])' in h):
        problems.append("missing media-query dark block guarded by :root:not([data-theme=light])")
    if ':root[data-theme="dark"]' not in h:
        problems.append("missing :root[data-theme=dark] block")

    # ── SVG hygiene + geometry ────────────────────────────────────────────────
    svgs = re.findall(r'<svg\b([^>]*)>(.*?)</svg>', h, re.S)
    for n, (attrs, body) in enumerate(svgs, 1):
        vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', attrs)
        if not vb:
            problems.append(f"svg{n}: no integer viewBox")
            continue
        vw = int(vb.group(1))
        if 'role="img"' not in attrs:
            problems.append(f'svg{n}: missing role="img"')
        al = re.search(r'aria-label="([^"]*)"', attrs)
        if not al or len(al.group(1)) < 40:
            problems.append(f"svg{n}: aria-label missing or too short to describe the diagram")

        rects = [tuple(map(int, m.groups())) for m in
                 re.finditer(r'<rect x="(\d+)" y="(\d+)" width="(\d+)" height="(\d+)"', body)]
        for m in re.finditer(r'<text x="(\d+)" y="(\d+)"([^>]*)>(.*?)</text>', body, re.S):
            x, y, a, inner = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
            if 'text-anchor="middle"' in a or 'text-anchor="end"' in a:
                continue  # anchor maths differs; check these by eye
            fs = re.search(r'font-size="([\d.]+)"', a)
            if fs:
                size = float(fs.group(1))
            elif 'class="cap"' in a or 'class="hd"' in a:
                size = 9.5
            elif 'lbl-sm' in a:
                size = 10.0
            else:
                size = 13.0
            txt = re.sub(r"<[^>]+>", "", inner).strip()
            end = x + text_width(txt, size, 'mono' in a)
            if end > vw - 6:
                problems.append(f"svg{n}: text past canvas ({end:.0f}>{vw}) — {txt[:44]!r}")
            for rx, ry, rw, rh in rects:
                if rx <= x <= rx + rw and ry <= y <= ry + rh + 4:
                    if end > rx + rw - 4:
                        problems.append(
                            f"svg{n}: text overflows its rect right edge "
                            f"({end:.0f}>{rx+rw}) — {txt[:40]!r}")
                    if y > ry + rh - 3:
                        problems.append(
                            f"svg{n}: baseline y={y} at/below rect bottom {ry+rh} — {txt[:40]!r}")
                    break

    # ── content discipline ────────────────────────────────────────────────────
    for t in BANNED:
        if t in h:
            problems.append(f"banned term present: {t!r}")

    for t in UNVERIFIED_TOKENS:
        if t in h:
            problems.append(
                f"{t} appears but is not confirmed by first-party docs — verify it and "
                "remove it from UNVERIFIED_TOKENS, or take it off the page"
            )

    # A plain-language page must define its jargon before using it.
    for acro, expansion in FIRST_MENTION:
        first = re.search(rf"\b{re.escape(acro)}\b", h)
        if not first:
            continue
        exp = h.lower().find(expansion.lower())
        if exp == -1:
            problems.append(f'{acro} used but never expanded as "{expansion}"')
        elif exp > first.start():
            problems.append(
                f'{acro} first used at byte {first.start()} but expanded as '
                f'"{expansion}" only at byte {exp} — define it before leaning on it'
            )

    # Every price on this page must sit near its regional caveat, or a reader outside
    # the quoted region will quote a number that does not apply to them.
    #
    # This used to test `"$20" in h` alone. When fabric-vs-databricks.html was re-priced
    # from US dollars into Swedish kronor, every "$" disappeared and the check silently
    # stopped firing — on a page where region matters MORE, not less: the same Fabric
    # reservation is 15.8% dearer in West Europe than in Sweden Central. A currency
    # symbol is not the signal; a price is.
    if ("$20" in h or "SEK" in h) and "vary by region" not in h:
        problems.append("prices present without the 'vary by region' caveat")

    ids = set(re.findall(r'id="([^"]+)"', h))
    dangling = sorted(set(re.findall(r'href="#([^"]+)"', h)) - ids)
    if dangling:
        problems.append(f"in-page links with no target: {dangling}")

    # ── report ────────────────────────────────────────────────────────────────
    print(f"checking {path}  ({len(h):,} bytes, {len(svgs)} inline SVG)")
    if not svgs:
        print("FAILED — no inline SVGs found. Nothing was really checked.")
        return 1
    for w in notes:
        print(f"  ~ {w}")
    if problems:
        print(f"\nFAILED — {len(problems)} issue(s):")
        for p in problems:
            print(f"  x {p}")
        return 1
    print(f"  self-contained · artifact form · themed · {len(svgs)} SVGs · geometry OK")
    print("  jargon expanded before use · prices carry the regional caveat")
    print("\nPASSED — static checks clean.")
    print("  Reminder: this does NOT prove the page looks right. Render it and LOOK.")
    return 0


if __name__ == "__main__":
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "claude-code-vs-cowork.html")
    if not target.exists():
        print(f"error: {target} not found", file=sys.stderr)
        sys.exit(2)
    sys.exit(check(target))
