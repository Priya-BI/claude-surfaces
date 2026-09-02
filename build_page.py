#!/usr/bin/env python3
"""Generate the standalone documents served by GitHub Pages.

    python3 build_page.py

`claude-code-vs-cowork.html` is authored in **Artifact page form**: it starts at
`<title>` and carries no `<!doctype>`, `<html>`, `<head>` or `<body>` of its own,
because the claude.ai Artifact publisher supplies that skeleton at publish time.

Served directly from a static host, that same file would render in *quirks mode*. It is
built to survive that (`*{box-sizing:border-box}`, no reliance on standards-mode
defaults), but shipping a real document is better than surviving a bad one. So this
script wraps each source once and writes the document Pages actually serves.

Keeping the wrap in a script rather than maintaining a second copy by hand is the whole
point: there is exactly one source of truth for each page, and the two outputs cannot
drift apart.

Every page is listed in PAGES below. The full comparison is the site root; the excerpt
is built into its own directory so it gets a clean shareable URL ending in the
directory name rather than a `.html` suffix.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Pulled out of the source so the tab title and the page title can never disagree.
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)

# (source, output, meta description). Sources are authored in Artifact page form.
PAGES = [
    (
        Path("claude-code-vs-cowork.html"),
        Path("index.html"),
        "A costed, first-party-sourced comparison of Claude Code and Claude Cowork on "
        "seats, security and auditability, plus MCP-vs-CLI routes into Microsoft Fabric.",
    ),
    (
        Path("claudecode-vs-cowork.html"),
        Path("claudecode-vs-cowork/index.html"),
        "The costed half of the Claude Code versus Claude Cowork comparison: one shared "
        "allowance, a twelve-person seat mix, what can go wrong, and the side-by-side table.",
    ),
    (
        Path("claude-code-vs-copilot.html"),
        Path("claudecode-vs-copilot/index.html"),
        "Copilot in Fabric compared against Claude Code reaching Fabric from a developer "
        "machine: the compliance boundary, the capacity-unit meter, pros and cons, and a "
        "routing rule for deciding which tool a task belongs to.",
    ),
]


def build_one(src: Path, out: Path, description: str) -> int:
    if not src.exists():
        print(f"error: {src} not found", file=sys.stderr)
        return 2

    body = src.read_text(encoding="utf-8")

    m = TITLE_RE.search(body)
    if not m:
        print(f"error: no <title> found in {src}", file=sys.stderr)
        return 2
    title = m.group(1).strip()

    # The source's own <title> moves into the real <head>; leaving a duplicate in the
    # body is valid but untidy, so strip it from the copied content.
    content = TITLE_RE.sub("", body, count=1).lstrip("\n")

    html = (
        '<!doctype html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{title}</title>\n'
        f'<meta name="description" content="{description}">\n'
        # The palette defines both themes; tell the browser so form controls and
        # scrollbars match rather than staying stubbornly light.
        '<meta name="color-scheme" content="light dark">\n'
        '</head>\n'
        '<body>\n'
        f'{content}'
        '\n</body>\n'
        '</html>\n'
    )

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out} ({len(html):,} bytes) — title {title!r}")
    return 0


def build() -> int:
    for src, out, description in PAGES:
        rc = build_one(src, out, description)
        if rc:
            return rc
    print("  reminder: run check_page.py against the SOURCES, not these files;")
    print("  the wrapper deliberately adds the tags the source-level check forbids.")
    return 0


if __name__ == "__main__":
    sys.exit(build())
