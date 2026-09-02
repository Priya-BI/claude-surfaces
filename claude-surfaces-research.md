# Claude Code vs Claude Cowork — facts basis

**Verified 2026-09-02.** Every claim in `claude-code-vs-cowork.md` and
`claude-code-vs-cowork.html` traces to a numbered source here. Sources marked
**[1P]** are first-party (Anthropic or Microsoft). Sources marked **[3P]** are
third-party and anything resting on them alone is flagged `UNVERIFIED` in the
deliverables.

Statuses on this page move fast. Several items are preview or beta. Re-verify before
relying on any status claim.

---

## A. Corrections made during research

Three things that a reasonable person would assume, which are wrong as of 2026-09-02.
They are recorded here because the deliverables are built to contradict them.

**A1. Cowork is not a research preview.** It launched as one on 2026-01-12 (macOS,
restricted plans), reached Windows parity 2026-02-10, and left preview on
**2026-04-09**, generally available across all paid plans on macOS and Windows.
Web, iOS and Android followed **2026-07-07**, with remote ("cloud") sessions in beta.
Sources: [S10] [3P] for the dates; [S1] [1P] confirms current availability on Team.
→ `UNVERIFIED` on the exact dates; the *current* GA-on-all-paid-plans state is [1P].

**A2. Cowork is not gated behind a Premium seat.** The Team plan feature list states
"Includes Claude Code and Claude Cowork" against both seat types [S1] [1P]. Usage
credits are described as available to "Standard and Premium seats" for "Claude,
Cowork, and Claude Code" [S4] [1P]. Third-party pages claiming Cowork is
Premium-only are pre-GA and stale.

**A3. Cowork *is* captured in the Compliance API.** "Cowork via Claude, Claude
Desktop, and Claude Mobile is captured in the Compliance API" [S3] [1P]. An earlier
third-party summary claiming the Compliance API and Audit Logs do not cover Cowork is
wrong. The real gaps are narrower and are recorded in section D.

---

## B. Cost — Claude plans and seats

**[S1] [1P]** Claude plans and pricing — <https://claude.com/pricing>
Team panel, verbatim: "For teams of 2 to 150". Standard seat — "All Claude features,
plus more usage than Pro" — "$20 / Per seat / month if billed annually. $25 if billed
monthly." Premium seat — "5x more usage than standard seats" — "$100 / Per seat /
month if billed annually. $125 if billed monthly." Team feature list includes:
"Includes Claude Code and Claude Cowork", "Central billing and administration",
"Single sign-on (SSO)", "Admin controls for remote and local connectors",
"No model training on your content by default", "Mix and match seat types".

**[S1a] [1P]** Same page, FAQ "Is Claude Code included in my plan?", verbatim:
"Claude Code is included in all paid plans. It shares the same usage limits as the
rest of your plan, so your work in the terminal and your chats draw from one pool.
For heavy coding sessions, you can also switch to pay-as-you-go API credits through a
Console account."

**[S1b] [1P]** Same page, FAQ on usage limits, verbatim: "Every plan has usage limits
that reset on a rolling five-hour session window, and paid plans add weekly limits on
top. Your activity across Claude on web, desktop, mobile, and Claude Code all draws
from the same pool. How much you can do depends on the length and complexity of your
conversations, the model you choose, and the features you use, so there's no fixed
message count. … On Team plans, Standard seats give more than Pro and Premium seats
give 5x more than Standard. To manage capacity and make sure all users have fair
access, we may limit your usage in other ways, such as weekly and monthly caps or
model and feature usage, at our discretion. When you reach a limit, you can wait for
it to reset, move to a higher plan, or, on paid plans, turn on usage credits to keep
working at standard API rates."

**[S2] [1P]** What is the Team plan? —
<https://support.claude.com/en/articles/9266767-what-is-the-team-plan>
Verbatim: "Team plans require a minimum of two members." Standard seats: "$25 per
member per month, billed monthly" / "$20 per member per month, billed annually".
Premium seats: "$125 per member per month, billed monthly" / "$100 per member per
month, billed annually". Caveats, verbatim: "Prices shown are for US customers and
exclude applicable taxes. Pricing, currency, and tax handling vary by region." and
"Price and plans are subject to change at Anthropic's discretion." Also: "Team plans
support up to 150 seats."

**[S2a] [1P]** Same article, usage limits. Verbatim: "For both Standard and Premium
seats, weekly limits reset at a fixed time each week that is assigned to your
account." — "**Standard seats:** Team plan Standard seats offer 1.25x more usage per
session than the Pro plan and have a weekly usage limit that applies across all
models." — "**Premium seats:** Team plan Premium seats offer 6.25x more usage per
session than the Pro plan and have a weekly usage limit that applies across all
models."

**[S4] [1P]** Manage usage credits for Team and seat-based Enterprise plans —
<https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans>
Verbatim: "Usage credits allow Team and seat-based Enterprise plan members on
Standard and Premium seats to continue working with Claude, Cowork, and Claude Code
after reaching their included usage limits. Instead of being blocked upon hitting
limits, members can keep working without interruption." And: "Usage credits don't
apply to current usage-based Enterprise plans. On those plans, there's no included
usage allowance to run out of—all usage is billed at API rates from the first token."

**[S5] [1P]** Claude API model list prices, per million tokens, cached 2026-06-24 via
the bundled `claude-api` skill reference. Relevant rows: Claude Opus 5 — $5.00 input
/ $25.00 output. Claude Sonnet 5 — $2.00 / $10.00. Claude Haiku 4.5 — $1.00 / $5.00.
These are the "standard API rates" that usage credits are billed at per [S1b].
Batch API is noted there as 50% cost. Also: Claude on Microsoft Foundry is billed
through the Microsoft Marketplace at standard API rates.
→ Prices are a cached snapshot. Re-verify against <https://claude.com/pricing> before
quoting.

### Derived: the 12-person worked scenario

All figures in the deliverables are **arithmetic on [S1]/[S2] list prices**, not
measured consumption. No usage or quota figure is asserted. Annual-billing rates
used, with the monthly-billing delta shown. US list prices, taxes excluded, and the
regional caveat from [S2] carried into the page.

| Mix | Composition | Monthly (annual billing) | Monthly (monthly billing) |
|---|---|---|---|
| A — all Standard | 12 × $20 | $240 | $300 |
| B — 4 Premium, 8 Standard | 4 × $100 + 8 × $20 | $560 | $820 |
| C — all Premium | 12 × $100 | $1,200 | $1,500 |

Annualised: A = $2,880 · B = $6,720 · C = $14,400. Monthly-billing penalty:
A +25%, B +46%, C +25%.

---

## C. What each surface is

**[S6] [1P]** Claude Code overview — <https://code.claude.com/docs/en/overview>
Claude Code is an AI coding assistant that runs in the terminal, working on the local
codebase.

**[S3] [1P]** Use Claude Cowork on Team and Enterprise plans —
<https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans>
The authoritative source for Cowork's admin, compliance and security surface. Quoted
extensively in section D.

**[S10] [3P]** Launch and GA timeline — VentureBeat, TechCrunch, eWeek, TechRadar
coverage of the 2026-01-12 launch, 2026-02-10 Windows parity, 2026-04-09 GA, and
2026-07-07 web/mobile. → `UNVERIFIED`: dates are third-party. Used only for the
timeline, never for a capability or control claim.

---

## D. Security and governance — Cowork

All quotes verbatim from **[S3] [1P]** unless noted.

**D1. Access control is all-or-nothing on Team.** "The Cowork toggle is
organization-wide—either all members have access or none do. On Enterprise plans,
admins who need per-team control can use groups and custom roles to selectively
enable Cowork or grant the 'Run Cowork in the cloud' capability to specific users or
teams. **Team plans don't have access to these controls, so Cowork remains
all-or-nothing.**"

**D2. Cloud sessions are on by default on Team.** "**Team plans:** on by default. An
owner can turn it off any time from the 'Run Cowork in the cloud' toggle." —
"**Enterprise plans:** off by default. An owner turns on 'Run Cowork in the cloud,'
then grants the Cowork in the cloud capability to a group with custom roles."

**D3. Local session history is outside central management.** "For local sessions,
Cowork stores conversation history locally on users' computers. This data is not
subject to Anthropic's standard data retention policies and **cannot be centrally
managed or exported by admins.** Claude Enterprise admins can retrieve this session
content through the Compliance API; **deletion endpoints for local sessions aren't
available yet.**" — "For sessions in the cloud, your sessions and files are saved to
your Claude account."

**D4. Compliance coverage exists, with a stated limit.** "Team and Enterprise owners
can stream Cowork events to your SIEM and observability tools through OpenTelemetry.
This gives security teams visibility into tool calls, file access, human approval
decisions, and more—**though it doesn't replace audit logging for compliance
purposes.**" — "Cowork via Claude, Claude Desktop, and Claude Mobile is captured in
the Compliance API."

**D5. Network egress does not cover MCP or web fetch.** "Cowork respects your
organization's current network egress permissions. Review your network access
settings in Organization settings > Capabilities under Code execution before enabling
Cowork." — "Network settings are applied when a new Cowork session is created. If you
change the network access mode or add domains to the allowlist while a conversation
is already active, those changes will not take effect in that session." —
"**Important:** Network egress permissions don't apply to the web fetch or web search
tools or MCPs, including Claude in Chrome. Web fetch runs server-side and is limited
to search results and URLs you've shared."

**D6. Write-tool approvals default to per-task.** "The organization setting Allow
'Always allow' for connector tools … controls whether members can skip per-task
approval for write-capable connector tools in Cowork. **This setting is off by
default.**" — "Read-only tools are exempt only when the connector annotates them as
read-only. **Most custom connectors don't annotate their tools, so every tool on
those connectors is gated.**" — On Enterprise "the most restrictive layer wins. Role
grants can't override it."

**D7. Projects have no org-level control.** "Projects are available to all Cowork
users. **There are no separate admin controls for projects, so owners cannot restrict
project creation at the organization level at this time.**"

**D8. Plugin distribution is controllable.** Per-plugin preferences: "Installed by
default", "Available", "Required" (members cannot uninstall), "Not available"
(hidden). Enterprise can override per group.

**[S11] [3P]** Documented attack research at and shortly after launch: PromptArmor
demonstrated a prompt-injection chain via a Word document leading to exfiltration of
local financial documents; HiddenLayer demonstrated an indirect prompt injection
producing a destructive shell command; reporting notes Anthropic self-reported an
approximate 1% residual attack success rate for Claude in Chrome after mitigations,
and that browsing reuses the user's authenticated session.
→ `UNVERIFIED`. These are researcher and press claims about a January 2026 build,
before GA and before the controls in D1–D8 shipped. In the deliverables they are
presented as *the class of failure to design against*, dated, and never as a
description of current behaviour.

---

## E. Security and governance — Claude Code

**[S7] [1P]** Claude Code security — <https://code.claude.com/docs/en/security>

**[S8] [1P]** Claude Code data usage — <https://code.claude.com/docs/en/data-usage>
Data training policy is stated per audience, with commercial (Team/Enterprise/API)
distinguished from consumer plans.

**[S9] [1P]** Is my data used for model training? —
<https://privacy.anthropic.com/en/articles/7996868-is-my-data-used-for-model-training>
Scoped to "our commercial products such as Claude for Work and the Anthropic API".
Corroborated by [S1]'s Team feature line "No model training on your content by
default".

---

## F. Reaching Microsoft Fabric — MCP server vs CLI

**[S20] [1P]** What are Fabric MCP Servers? —
<https://learn.microsoft.com/rest/api/fabric/articles/mcp-servers/what-is-fabric-mcp-server>
Verbatim: "Microsoft Fabric provides two complementary Model Context Protocol (MCP)
servers … Choose the remote **Core** server for quick access to Fabric workspaces and
items, or the local **Fabric MCP Server** for development workflows with API
documentation, OneLake data, and extensibility."

**[S21] [1P]** Fabric Core MCP Server overview —
<https://learn.microsoft.com/rest/api/fabric/articles/mcp-servers/core-remote/overview-core-mcp-server>
Status, verbatim: "Fabric Core MCP Server is currently in **preview**. Features and
configuration may change before general availability." Flow: endpoint
`https://api.fabric.microsoft.com/v1/mcp/core`; "You authenticate through a
browser-based OAuth 2.0 flow with Microsoft Entra ID"; "**All operations respect your
Fabric RBAC permissions, and Fabric records them in audit logs.**" Supported
operations include catalog search; "**Workspace operations** — List, create, update,
and delete workspaces"; item CRUD; "**Permission management** — Grant and revoke
workspace roles (Admin, Member, Contributor, Viewer)"; folders; capacities.

**[S22] [1P]** Overview of the Power BI MCP servers (Preview) —
<https://learn.microsoft.com/power-bi/developer/mcp/mcp-servers-overview>
Security, verbatim: "MCP as a phenomenon is very novel and cutting-edge. As with all
new technology standards, consider doing a security review…" Permissions and risk,
verbatim: "MCP clients can invoke operations based on the user's Fabric Role-Based
Access Control (RBAC) permissions. **Autonomous or misconfigured clients may perform
destructive actions.** You should review and apply least-privilege RBAC roles and
implement safeguards before deployment. **Certain safeguards, such as flags to
prevent destructive operations, are not standardized in the MCP specification and may
not be supported by all clients.**" Compliance responsibility, verbatim: "This MCP
server may interact with clients and services that **process data outside of Fabric's
compliance boundaries**, and are processed in accordance with your chosen client or
service(s) applicable terms and data handling policies. **You are responsible** for
ensuring that any integration complies with applicable organizational, regulatory,
and contractual requirements."

**[S23] [1P]** Data agent as MCP server (preview) —
<https://learn.microsoft.com/fabric/data-science/data-agent-mcp-server>
Verbatim: "Every request to the MCP endpoint must be authenticated against Fabric.
Your client attaches a bearer token in the `Authorization` header, and the token must
have permission to access the target workspace and data agent. **The token can
represent either a user identity or a service principal.**" Scope:
`https://api.fabric.microsoft.com/.default`. Also: "The data agent MCP server doesn't
support dynamic client registration."

**[S24] [1P]** Fabric command line interface —
<https://learn.microsoft.com/rest/api/fabric/articles/fabric-command-line-interface>
Install `pip install ms-fabric-cli`, Python 3.10+, `fab auth login`. Four login
methods, verbatim: "Interactive with web browser", "Service principal
authentication with secret", "Service principal authentication with certificate",
"Managed identity authentication". Also: "Any Fabric user can use the CLI. … You can
also use the CLI as a service principal for automation tasks."

**[S25] [1P]** Set up authentication for MCP tools —
<https://learn.microsoft.com/azure/foundry/agents/how-to/mcp-authentication>
The identity-preservation table. Two scenarios, verbatim: "**Shared
authentication**: Every user of the agent uses the same identity to authenticate to
the MCP server. **User context doesn't persist.**" / "**Individual
authentication**: Each user authenticates with their own account so their user
context persists." Method table marks Key-based, Entra agent identity and Entra
project managed identity as "User context persists: **No**", and OAuth identity
passthrough as "**Yes**".

**[S26] [1P]** Workspace identity —
<https://learn.microsoft.com/fabric/security/workspace-identity>
Verbatim warning: "Workspace identity is an automatically managed service principal
created by Fabric users. Access to this identity should be carefully managed and
monitored, as **any individual given access to the identity is allowed to assume
it.**" Audit events for creation/deletion appear in the Purview Audit Log.

**[S27] [1P]** Authenticate with workspace identity —
<https://learn.microsoft.com/fabric/security/workspace-identity-authenticate>
Run-time identity requirement, verbatim: "The identity that *runs* the pipeline must
also have an admin, member, or contributor role in the workspace. Fabric checks this
permission at run time… **Because of this requirement, a pipeline that succeeds when
you run it manually might fail when the same pipeline runs on a schedule under a
different identity.**"

### The cross-vendor convergence

The page's spine rests on three independent first-party statements that all point at
the same weakness in the agentic path:

1. Anthropic [S3/D5]: network egress permissions "don't apply to … MCPs".
2. Microsoft [S22]: MCP integrations "may interact with clients and services that
   process data outside of Fabric's compliance boundaries", responsibility yours.
3. Microsoft [S22]: destructive-operation safeguards "are not standardized in the MCP
   specification and may not be supported by all clients".

Combined with [S21] — the Core MCP surface can delete workspaces and grant workspace
roles — and [S25] — shared-identity MCP auth loses per-user context — the conclusion
is not "MCP is unsafe" but "MCP is the path your existing egress and approval controls
were not designed to see, holding tools that can escalate and destroy."

---

## G. Deliberately excluded

- **No Claude–Fabric product integration is claimed.** Fabric is the work context of
  the scenario team. The only Claude-on-Microsoft fact used is [S5]: Claude is
  available on Microsoft Foundry at standard API rates.
- **No measured usage, quota percentage, or consumption figure.** The scenario is
  arithmetic on list prices under stated assumptions.
- **No Enterprise-plan pricing.** Quote-based; the page notes only that Team stops at
  150 seats [S2].
- **The scenario organisation is invented.** No real organisation, person, workspace,
  or object name appears in any deliverable.
