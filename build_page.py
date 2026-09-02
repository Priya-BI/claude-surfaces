#!/usr/bin/env python3
"""Generate the standalone index.html served by GitHub Pages.

    python3 build_page.py

`claude-code-vs-cowork.html` is authored in **Artifact page form**: it starts at
`<title>` and carries no `<!doctype>`, `<html>`, `<head>` or `<body>` of its own,
because the claude.ai Artifact publisher supplies that skeleton at publish time.

Served directly from a static host, that same file would render in *quirks mode*. It is
built to survive that (`*{box-sizing:border-box}`, no reliance on standards-mode
defaults), but shipping a real document is better than surviving a bad one. So this
script wraps the source once and writes `index.html`.

Keeping the wrap in a script rather than maintaining a second copy by hand is the whole
point: there is exactly one source of truth for the content, and the two outputs cannot
drift apart.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SRC = Path("claude-code-vs-cowork.html")
OUT = Path("index.html")

# Pulled out of the source so the tab title and the page title can never disagree.
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)

DESCRIPTION = (
    "A costed, first-party-sourced comparison of Claude Code and Claude Cowork on "
    "seats, security and auditability, plus MCP-vs-CLI routes into Microsoft Fabric."
)


def build() -> int:
    if not SRC.exists():
        print(f"error: {SRC} not found", file=sys.stderr)
        return 2

    body = SRC.read_text(encoding="utf-8")

    m = TITLE_RE.search(body)
    if not m:
        print(f"error: no <title> found in {SRC}", file=sys.stderr)
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
        f'<meta name="description" content="{DESCRIPTION}">\n'
        # The palette defines both themes; tell the browser so form controls and
        # scrollbars match rather than staying stubbornly light.
        '<meta name="color-scheme" content="light dark">\n'
        '</head>\n'
        '<body>\n'
        f'{content}'
        '\n</body>\n'
        '</html>\n'
    )

    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({len(html):,} bytes) — title {title!r}")
    print("  reminder: run check_page.py against the SOURCE, not this file;")
    print("  the wrapper deliberately adds the tags the source-level check forbids.")
    return 0


if __name__ == "__main__":
    sys.exit(build())
