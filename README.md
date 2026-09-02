# Code, Cowork, and Fabric

**Read it here → https://data-blueprint-lab.github.io/claude-surfaces/**

A comparison of Anthropic's two agentic surfaces — **Claude Code** and **Claude
Cowork** — on cost, security and governance, plus the two ways an agent reaches
**Microsoft Fabric** from a developer machine (an MCP server, or the `fab` CLI).

Written for people who have to make a deployment decision and want the numbers and the
sources, not a feature grid. Verified **2026-09-02**.

## The short version

**They are not two purchases.** Claude Code is included in every paid plan; Cowork is
included in every paid Team seat, Standard and Premium alike. Neither has a price of its
own, so "which is cheaper" has no answer.

**They share one allowance.** Anthropic's own words: "your work in the terminal and your
chats draw from one pool." Usage credits cover "Claude, Cowork, and Claude Code" from one
included allowance. So a Cowork rollout adds no line item — it raises the rate at which
existing seats hit their ceiling and start drawing credits at API rates.

**The deciding difference is governability, and the result is counterintuitive:** the
developer tool is the more controllable one. Claude Code starts read-only, does not
auto-approve web fetches, can sandbox its own shell, and logs cloud-session operations
"for compliance and audit purposes." Cowork on a Team plan is all-or-nothing across the
whole organisation, runs cloud sessions on by default, keeps local session history on the
user's own machine outside central retention with no admin export and no deletion
endpoint yet, and sits behind network egress rules that explicitly do not apply to web
fetch, web search, or MCP servers.

**A second axis most comparisons skip — including the first version of this page:** what
actually travels to the vendor, and how long it is kept. Neither tool differs, but the
numbers are not the ones usually quoted. Thirty days is the *API backend* deletion window,
not a cap on saved Team or Enterprise coding sessions, which are retained in-product until
someone deletes them. Anything submitted as feedback — a thumbs-down, a bug report — carries
**five years**, on a commercial plan too. And zero data retention is not a switch you can
flip: it is not part of the standard Enterprise plan, cannot be enabled from admin settings,
and is mutually exclusive with Anthropic's covered models, which on Azure Foundry means a
separate Azure subscription.

**On Fabric,** three first-party statements from two uncoordinated vendors point at the
same soft spot: Anthropic says egress permissions don't apply to MCP servers; Microsoft
says an MCP integration may "process data outside of Fabric's compliance boundaries" and
that destructive-operation safeguards "are not standardized in the MCP specification."
The Fabric Core MCP server's tool menu includes deleting workspaces and granting
workspace roles. Meanwhile a shared service principal — the convenient option on either
route — erases the named human from Fabric's audit log.

## Three corrections this repo exists to record

Things a reasonable person would assume, which were wrong as of 2026-09-02:

1. **Cowork is not a research preview.** It left preview on 2026-04-09 and is generally
   available on all paid plans across macOS, Windows, web and mobile.
2. **Cowork is not gated behind a Premium seat.** Both Team seat types include it.
3. **Cowork *is* captured in the Compliance API.** The widely repeated claim that the
   Compliance API and audit logs do not cover it is wrong. The real gaps are narrower —
   and are listed in section 07 of the page.

`check_page.py` bans all three stale claims as literal string matches, so an edit that
reintroduces one fails the check rather than shipping.

## What's in here

| File | What it's for |
|---|---|
| `claude-code-vs-cowork.html` | **Source of the page.** Authored in claude.ai Artifact page form, so it deliberately has no `<!doctype>`/`<html>`/`<head>`/`<body>` — the publisher supplies those. |
| `index.html` | **Generated.** What GitHub Pages serves: the source wrapped in a real HTML document. Produced by `build_page.py`; don't hand-edit. |
| `claude-code-vs-cowork.md` | The same argument in prose, readable on GitHub. |
| `claude-surfaces-research.md` | **The facts basis.** Numbered, dated sources — `[1P]` first-party, `[3P]` third-party, `UNVERIFIED` where a claim rests on third-party sources only. Start here if you want to check a number. |
| `check_page.py` | Static checks for the source page. |
| `build_page.py` | Generates `index.html` from the source. |

## Editing it

```sh
# 1. edit the source (never index.html)
$EDITOR claude-code-vs-cowork.html

# 2. gate it — must exit 0
python3 check_page.py claude-code-vs-cowork.html

# 3. regenerate what Pages serves
python3 build_page.py

# 4. then LOOK at it. Static checks do not prove a page renders correctly.
```

The checker enforces: self-containment (no scripts, external assets, CDN or Mermaid),
Artifact page form, the `svg text{fill:…}` override trap, hardcoded hex, all three theme
declarations, per-SVG integer `viewBox` + `role="img"` + a substantive `aria-label`, SVG
text geometry against its containing rect, banned stale claims, first-mention expansion
of `MCP` and `RBAC`, the regional price caveat, and dangling `#` anchors.

To inspect one diagram at a time, extract the `<style>` block plus a single `<figure>`
into a standalone file and screenshot that — cropping a full-page screenshot with
`sips --cropOffset` silently ignores the offset.

## Scope and caveats

- **Prices are US list, excluding tax.** Anthropic states that "pricing, currency, and
  tax handling vary by region" and that prices are subject to change. Outside the US,
  treat the figures as the shape of the bill, not the invoice.
- **No usage or quota figure is asserted.** The costed scenario is arithmetic on list
  prices under stated assumptions — a model, not a forecast.
- **The organisation is invented.** The twelve-person Fabric platform team is a composite
  built to make the arithmetic concrete. No real organisation, person, workspace or
  object name appears anywhere.
- **No Claude–Fabric product integration is claimed.** Fabric is the work context of the
  scenario team.
- **Shelf life is short.** The Fabric Core MCP server is in preview; Cowork's
  cloud-session defaults, Compliance API coverage of local sessions and admin control
  surface are all moving, as are Claude Code's permission modes across plans and
  surfaces. Roughly a quarter of the described surface is preview or beta. Re-check any
  status claim before relying on it.

Not affiliated with, endorsed by, or reviewed by Anthropic or Microsoft. Every quoted
claim is attributed to its published source in the facts basis; go read those rather than
trusting this summary.
