# Claude Code vs Claude Cowork: what it costs, what it can reach, and what you can prove

**Written 2026-09-02 · statuses verified 2026-09-02 · facts basis: `claude-surfaces-research.md`**

A plain-language comparison of Anthropic's two agentic surfaces, for people who have to
decide whether to put them in front of a working data platform. Includes a costed
scenario for a twelve-person analytics team on Microsoft Fabric, a risk register for
each tool, and a section on the two ways an agent can reach Fabric from a developer's
machine.

Every price and status below traces to a dated first-party source. Several items are
preview or beta and will move. Re-check before you rely on them.

---

## 00 · The short answer

Three things are true that most comparisons of these two tools get wrong.

**They are not two purchases.** Claude Code is included in every paid plan. Cowork is
included in every paid Team seat, both Standard and Premium. Neither has a price of its
own. So "which is cheaper" has no answer — the question is what a *seat* costs, and how
fast each tool burns the allowance that comes with it.

**They share one allowance.** In Anthropic's own words, "your work in the terminal and
your chats draw from one pool." When a member runs out, usage credits let them keep
going — billed at standard API rates — and those credits cover "Claude, Cowork, and
Claude Code" alike. There is one tap and one meter per person, not two.

**The difference that should decide it is governability, not price and not even
security.** And here the result is the opposite of what most people expect: the
developer tool is the more controllable one. Claude Code starts read-only, gates
network fetches, can sandbox its own shell, and logs every operation in a cloud session
"for compliance and audit purposes." Cowork on a Team plan is all-or-nothing across the
whole organisation, runs cloud sessions on by default, keeps local session history on
the employee's own laptop outside central retention with no admin export and no
deletion endpoint yet, and sits behind network egress rules that explicitly do not
apply to web fetch, web search, or MCP servers.

**So:** buy seats, not tools. Give the platform engineers Premium seats and Claude Code.
Turn Cowork's cloud sessions off on day one and decide deliberately whether to turn them
back on. And treat the MCP path to Fabric as the one your existing controls cannot see.

---

## 01 · Same engine, two doors

Cowork was built out of Claude Code. It runs the same kind of agent loop — read
something, decide, act, check, repeat — but points it at ordinary business files instead
of a code repository, and removes the terminal.

> **In plain terms.** An *agent* here just means the model is allowed to take actions in
> a loop rather than answer one question. It reads, decides what to do, does it, looks
> at the result, and goes again. The interesting question is never "how clever is it" —
> it is "what is it allowed to touch, and who finds out."

|  | **Claude Code** | **Claude Cowork** |
|---|---|---|
| Where it runs | Terminal on your machine; also web/cloud sessions and IDE | Claude desktop app, web, iOS, Android; local or cloud sessions |
| Who it's for | Developers and engineers | Anyone — no coding required |
| What it points at | A code repository and your shell | Folders of documents you grant it |
| Status | Generally available | Generally available since 2026-04-09 (launched Jan 2026, was a preview) |
| Included in | All paid plans | All paid plans, both Team seat types |

The important consequence of the shared origin: **a control that exists for one is not
automatically present for the other.** Most of this document is about where those two
control surfaces have drifted apart.

---

## 02 · The money is one pool, not two bills

### Team seat list prices

Verified 2026-09-02. US list prices, taxes excluded. Anthropic states that "pricing,
currency, and tax handling vary by region", so treat these as the shape of the bill
rather than the invoice you will receive outside the US.

| Seat | Billed annually | Billed monthly | Usage |
|---|---|---|---|
| **Standard** | **$20** /seat/month | $25 /seat/month | 1.25× a Pro session |
| **Premium** | **$100** /seat/month | $125 /seat/month | 6.25× a Pro session — 5× a Standard seat |

Team plans require a minimum of two members and support up to 150 seats. Seat types can
be mixed. Both types include Claude Code and Cowork. Both carry a weekly limit on top of
the rolling five-hour session window, resetting at a fixed time assigned to your account.

### Where the variable cost actually is

There are only two levers, and neither is the choice between Code and Cowork:

1. **Seat mix.** A Premium seat costs five times a Standard seat and gives five times the
   usage. This is the whole decision. It is a straight linear trade, so the only real
   question is which people genuinely hit the Standard ceiling.
2. **Usage credits.** When a member exhausts their allowance they can keep working, at
   standard API rates. This is the only genuinely usage-based cost in the model, and the
   only place a runaway agent shows up as money.

> **Watch this one.** Because Code, Cowork and chat draw from one pool, a person who
> spends their week in Cowork has less headroom for Claude Code, and vice versa. Rolling
> Cowork out broadly does not add a line item — it quietly raises the rate at which
> existing seats hit their ceiling and start drawing credits. That is the cost of a
> Cowork rollout, and it will not appear as "Cowork" on any invoice.

---

## 03 · Worked scenario: a twelve-person Fabric platform team

An invented organisation. One platform team of twelve people running a Microsoft
Fabric-based analytics estate: ingestion pipelines, a lakehouse, semantic models, and
reporting for the rest of the business.

Nothing here is measured consumption. It is arithmetic on list prices under stated
assumptions — a model for reasoning about the shape of the bill, not a forecast.

### The team, and what each role actually needs

| Role | Count | Daily work | Needs Claude Code? | Needs Cowork? | Seat |
|---|---|---|---|---|---|
| Platform lead | 1 | Architecture, reviews, standards, vendor docs | Sometimes | Yes — documents, plans | Premium |
| Data engineer | 4 | Pipelines, notebooks, transformations, deployment | Heavily — all day | Rarely | Premium (2), Standard (2) |
| Analytics engineer | 2 | Semantic models, metric definitions, tests | Heavily | Sometimes | Premium (1), Standard (1) |
| BI developer | 3 | Reports, dashboards, DAX | Sometimes | Yes — specs, documentation | Standard |
| Data analyst | 2 | Analysis, ad-hoc questions, stakeholder decks | No | Yes — the main tool | Standard |

That is a natural mix of **4 Premium and 8 Standard**: heavy, all-day agentic coding gets
a Premium seat; everyone else starts Standard and moves up only if they actually hit the
ceiling.

### Three mixes, costed

| Mix | Composition | Per month (annual) | Per year | Per month (monthly billing) |
|---|---|---|---|---|
| A — everyone Standard | 12 × $20 | **$240** | $2,880 | $300 (+25%) |
| **B — 4 Premium, 8 Standard** | 4 × $100 + 8 × $20 | **$560** | **$6,720** | $820 (+46%) |
| C — everyone Premium | 12 × $100 | **$1,200** | $14,400 | $1,500 (+25%) |

**Recommended: Mix B, billed annually — $6,720 a year.**

Three observations a stakeholder should take from this table:

- **Start at A, not C.** Mix A is $240 a month and gives all twelve people both tools.
  If nobody hits a ceiling, you are done. Buying Premium for everyone "to be safe" costs
  five times as much for usage most of the team will never touch.
- **The monthly-billing penalty is not uniform.** It is 25% on a single-seat-type mix,
  but 46% on Mix B, because the Premium premium is proportionally larger. If you are
  going to mix seat types, annual billing matters more than you would guess.
- **Budget for credits separately, and only after you have a month of real data.** Do
  not model credit spend up front — you would be inventing a number. Turn credits on with
  a spend limit, watch one billing cycle, then decide.

### The upgrade trigger

Move someone from Standard to Premium when they hit their weekly limit repeatedly on
work that matters — not when they hit a five-hour session limit once. At $80 a month
extra per person, a single upgrade is cheap; twelve speculative upgrades are not.

---

## 04 · Blast radius: what each one can reach when it goes wrong

Both tools are agents doing real work, so "what happens on a bad day" is the right
question. The two bad days look nothing alike.

**Claude Code on a developer machine** can reach: the repository, the shell, and
whatever that shell's credentials can reach — cloud CLIs already logged in, database
connection strings, deployment pipelines, package registries. This is a large reach. But
it lands on a person who reads diffs for a living, in a directory under version control,
where the normal review gate is a pull request that someone else looks at.

**Cowork on a business user's machine** can reach: the folders it has been granted, the
documents in them, and — when browsing — the identity the user is already signed in as.
The reach is narrower in machine terms and wider in *business* terms: it is HR exports,
finance workbooks, contracts, board material. And it lands on a person who has no
professional reflex for spotting a malicious instruction buried in a document, and no
diff to review.

> **The asymmetry that matters.** Claude Code's risks are large but land where review
> already exists. Cowork's risks are narrower but land where no review exists. A control
> gap is only as safe as the person standing in it.

---

## 05 · Head to head

Every row below is sourced first-party. See the facts basis for the exact quotes.

| | **Claude Code** | **Claude Cowork** |
|---|---|---|
| **Cost** | Included in all paid plans | Included in all paid plans |
| **Usage** | Shared per-member pool | Same shared pool |
| **Default posture** | Manual mode starts **read-only** | Session granted access to chosen folders |
| **Per-action gate** | Asks before edits, tests, commands; approve once or always; explicit deny rules | Per-task approval for write-capable connector tools; "always allow" **off by default** |
| **Read-only exemption** | Built-in list (`ls`, `cat`, `git status`) runs without asking | Only if the connector annotates the tool read-only — most custom connectors don't, so all their tools are gated |
| **Unattended mode** | Auto mode: a separate classifier reviews actions and blocks unsafe ones; org can disable it | Cloud sessions; on by default on Team |
| **Web fetch** | `curl`/`wget` **not auto-approved**; can be denied outright | Egress rules **do not apply** to web fetch, web search, or MCP |
| **Isolation** | Sandboxed bash with filesystem + network isolation; working-directory boundary; devcontainers | Cloud sessions in an Anthropic-managed environment; local sessions on the user's machine |
| **Cloud session audit** | "All operations in cloud sessions are logged for compliance and audit purposes" | Captured in the Compliance API; OpenTelemetry stream "doesn't replace audit logging for compliance purposes" |
| **Local history** | Repo under git; session data under Anthropic retention | Local session history **not** under standard retention, **no** admin export, **no** deletion endpoint yet |
| **Scoping to some people** | Org policy and settings; auto mode disableable org-wide | **All-or-nothing on Team.** Groups and custom roles are Enterprise-only |
| **Cloud credential handling** | Secure proxy with a scoped credential; real token never in the sandbox; push restricted to the working branch | Sessions and files saved to the member's Claude account |
| **Model training** | Not on your content by default on Team/Enterprise (Commercial Terms) | Same terms — same plan |
| **Certifications** | SOC 2 Type 2, ISO 27001 (Anthropic Trust Center) | Same |

**Read the table this way:** the two tools do not differ on price, data terms, or model
quality. They differ on **defaults, scoping, and what survives as evidence.** On all
three, Claude Code is currently ahead.

---

## 06 · Risk register — Claude Code

| # | Risk | Why it's real | Mitigation available today |
|---|---|---|---|
| C1 | **Ambient credentials.** The agent's shell holds whatever the developer is logged into | A single approved command can reach production, not just the repo | Sandboxed bash with network isolation; deny rules on deployment commands; separate dev credentials from production |
| C2 | **Injection via fetched content.** Web pages, dependency READMEs, issue text can carry instructions | The agent reads untrusted text and then acts | `curl`/`wget` are not auto-approved by default; add them to `permissions.deny` to block outright; context-aware analysis of the full request |
| C3 | **Auto mode removes the human.** A classifier reviews actions instead of a person | A classifier is a model, and models are wrong sometimes | Your explicit ask and deny rules still apply in auto mode; the organisation can turn auto mode off entirely |
| C4 | **Blast radius beyond the working directory** | Shell access is not bounded by the repo | Working-directory boundary; `/sandbox` to define autonomous zones; devcontainers for hard isolation |
| C5 | **Self-hosted cloud sessions shift the burden** | For sessions routed to your own infrastructure, "isolation, network egress, and git credentials are your deployment's responsibility" | Use Anthropic-hosted environments unless you have the platform team to own the alternative |

**Net:** manageable, with real controls, on machines whose owners understand the risk.
The residual risk is C1 — and it is a credential hygiene problem you have anyway, made
faster.

---

## 07 · Risk register — Cowork

| # | Risk | Why it's real | Mitigation available today |
|---|---|---|---|
| W1 | **No per-team scoping on Team plans.** "Team plans don't have access to these controls, so Cowork remains all-or-nothing" | You cannot give Cowork to two analysts and withhold it from ten others. It is the whole organisation or nobody | Only: leave it off, or move to Enterprise for groups and custom roles |
| W2 | **Cloud sessions are on by default on Team** | Files and session state leave the machine unless someone turns the toggle off | Organisation settings → Cowork → turn off "Run Cowork in the cloud". Do this before enabling Cowork, not after |
| W3 | **Local session history escapes central control.** "Not subject to Anthropic's standard data retention policies and cannot be centrally managed or exported by admins", and "deletion endpoints for local sessions aren't available yet" | A subject-access or deletion request cannot be satisfied for local sessions. This is a records-management gap, not a hacking risk | Prefer cloud sessions *if* central retention matters more than local processing — note this is the exact opposite of W2's advice, and the tension is real |
| W4 | **Egress controls have a stated carve-out.** "Network egress permissions don't apply to the web fetch or web search tools or MCPs" | Your domain allowlist does not constrain the paths most likely to move data | Turn off web search for Cowork and Chat in organisation capabilities; govern MCP servers separately and explicitly |
| W5 | **Egress settings bind at session start** | Changing the allowlist mid-conversation has no effect on that session | Treat policy changes as requiring new sessions; communicate that |
| W6 | **Projects cannot be restricted.** "Owners cannot restrict project creation at the organization level at this time" | Users can create workspaces with their own files, instructions and memory, outside any org-level policy | None today. Accept it or don't deploy |
| W7 | **Document-borne prompt injection.** At launch, researchers demonstrated exfiltration via a poisoned document, and a destructive command via indirect injection | The user population is least equipped to spot it | Keep "always allow" off for write tools (the default); curate the plugin catalogue; train users that documents are untrusted input |
| W8 | **Inherited browser identity** | When browsing, the agent acts as whoever the user is signed in as | Restrict or disable browser use; do not rely on "it only sees what the user sees" as a comfort |

**Net:** the controls that exist are sensible and the defaults on approvals are
conservative. But **W1, W3 and W6 have no mitigation on a Team plan** — they are
accept-or-decline. That, not prompt injection, is what makes Cowork the harder rollout.

> **On W7's evidence.** Those demonstrations were against a January 2026 build, before
> general availability and before several of the controls above shipped. They are cited
> as the *class of failure* to design against, not as a description of how Cowork behaves
> today. Anyone quoting them as current behaviour is misusing them.

---

## 08 · Reaching Microsoft Fabric: MCP server or CLI?

Your team's agent has to actually touch Fabric. There are two ways, and they differ far
more than they look.

> **In plain terms.** An **MCP server** is a small program that advertises a menu of
> tools to the model — "list workspaces", "create item", "grant role" — and the model
> picks one and calls it. A **CLI** is a command-line program: the agent writes out a
> command as text, and something has to run it. The difference is who chooses the action,
> and whether a human or a rule can stand in between.

### The two paths

| | **Fabric MCP server** | **Fabric CLI (`fab`)** |
|---|---|---|
| What it is | Two servers: a remote **Core** server, and a local server for development workflows | `pip install ms-fabric-cli`, then `fab auth login` |
| Status | Core server is **in preview** — "features and configuration may change" | Generally available |
| Identity | Core: browser-based OAuth 2.0 with Entra ID, as you. Data-agent server: a bearer token that "can represent either a user identity or a service principal" | Four choices: interactive browser (as you), service principal + secret, service principal + certificate, or managed identity |
| Who chooses the action | **The model** picks a tool from the menu | **The agent writes a command**; a human or a permission rule can gate it before it runs |
| Permissions | "All operations respect your Fabric RBAC permissions" | Same — whatever the signed-in identity can do |
| Fabric-side audit | Core: "Fabric records them in audit logs" | Fabric API calls are recorded the same way |
| What's on the menu | Includes **delete workspaces** and **grant and revoke workspace roles** (Admin, Member, Contributor, Viewer) | Whatever command the agent writes — but each one is visible text first |
| Destructive-op guardrails | Microsoft: safeguards "are not standardized in the MCP specification and may not be supported by all clients" | Your permission rules, e.g. deny anything matching a delete |
| Compliance boundary | Microsoft: "may interact with clients and services that process data outside of Fabric's compliance boundaries… **You are responsible**" | The CLI is a local process calling Fabric's API |
| Covered by Claude's egress allowlist | **No** — "network egress permissions don't apply to … MCPs" | Yes, it's a normal command subject to normal approval |

### Why this matters more than it sounds

Three first-party statements, from two vendors who did not coordinate, all point at the
same soft spot:

1. **Anthropic:** network egress permissions do not apply to MCP servers.
2. **Microsoft:** an MCP integration may process data outside Fabric's compliance
   boundaries, and the responsibility is yours.
3. **Microsoft:** "Autonomous or misconfigured clients may perform destructive actions",
   and the safeguards that would prevent it are not part of the protocol.

Add that the Core MCP server's tool menu includes deleting workspaces and granting
workspace roles, and the conclusion is not "MCP is unsafe." It is: **MCP is the path your
existing egress controls and approval gates were not built to see, and it carries tools
that can escalate privileges and destroy things.**

### The trap on the CLI path

The CLI is not automatically safer, and here is where it goes wrong. Because
`fab auth login` offers service-principal login, and because that is the convenient
option for anything automated, teams drift towards putting a shared service principal in
the agent's environment. Do that and **you have thrown away per-user governance**: every
action arrives in Fabric's audit log as the service principal, not as the person, and
Fabric's RBAC can no longer tell your twelve engineers apart.

Microsoft says this plainly in its own MCP authentication guidance: with shared
authentication, "user context doesn't persist"; only individual authentication —
OAuth identity passthrough — preserves it. The same applies to a shared service
principal behind a CLI.

Fabric's workspace identity carries the matching warning: it is "an automatically managed
service principal", and "any individual given access to the identity is allowed to assume
it."

**So the rule is about identity, not about tooling:** interactive, per-user
authentication for interactive work; a service principal only for genuinely unattended
automation, with its own least-privilege workspace role. A shared service principal used
for a human's daily work is the single worst configuration available on either path.

---

## 09 · What a normal day looks like

**On the CLI path.** An engineer opens the terminal, and once a day runs `fab auth login`
and signs in as themselves in the browser. Their agent proposes a command —
`fab ls Analytics.Workspace`, or a notebook deployment. The first time, they approve it;
if it is routine and safe they allow it from then on. Anything destructive is in a deny
rule and never runs. Every call reaches Fabric as *them*, so the audit log names a person,
and RBAC applies their actual roles. What they gave up: the agent cannot discover Fabric's
capabilities by itself, so they occasionally have to tell it what command exists.

**On the MCP path.** The engineer connects once through a browser OAuth flow and the tool
menu appears. The agent now explores Fabric on its own — searching the catalogue,
inspecting items, chaining calls — and it is genuinely faster and requires less knowledge
of the API. What they gave up: the model is choosing from a menu that includes deleting a
workspace and granting an Admin role, the guardrails against that are not part of the
protocol, and this traffic is outside the egress allowlist. On the Core server their
identity is preserved and Fabric logs the operations, which is the good case. On a
server configured with a service principal, it is not.

**In Cowork.** An analyst grants access to a folder of monthly reports and asks for a
summary and a deck. It works, it is impressive, and nobody had to learn anything. Behind
that: if it is a local session, the conversation history is now on that laptop, outside
retention policy and beyond admin export. If it is a cloud session — the default on Team —
the files went to their Claude account. If one of those documents came from outside the
company, it was untrusted input handed to an agent.

---

## 10 · What I'd do

**Buy Mix B, annually.** Four Premium seats for the people who live in an agent all day,
eight Standard for everyone else, $6,720 a year for twelve people. Start everyone on
Standard if you want to be careful; upgrade on evidence of repeated weekly-limit hits,
not on anticipation.

**Give Claude Code to the engineers, in Manual mode, sandboxed.** Deny `curl` and `wget`.
Put deployment commands in deny rules. Keep production credentials out of the shell the
agent can see. This is the surface with the best defaults and the best evidence trail, and
it lands on people who review changes for a living.

**Turn off "Run Cowork in the cloud" before you enable Cowork.** It is on by default on
Team. Make turning it back on a deliberate decision with a reason attached.

**Then make an honest call on Cowork itself.** On a Team plan it is all-or-nothing, you
cannot restrict project creation, and local session history is outside your retention and
deletion controls. If your organisation has real records-management obligations, those
three facts are the decision, and the answer is either "wait" or "move to Enterprise for
groups and custom roles." If it does not, enable it, keep write-tool approvals per-task
(the default), curate the plugin catalogue, and tell people that a document from outside
the company is untrusted input.

**For Fabric, use the CLI with interactive per-user login for daily work.** Not because
the CLI is inherently safer, but because it keeps three things you otherwise lose: a named
human in the audit log, a text command a rule can gate, and traffic your egress policy can
actually see. Use the Core MCP server where its discovery is worth it — read-heavy
exploration by people who understand what the tool menu contains — and keep it off the
path that touches sensitive workspaces while it is still in preview. Reserve service
principals for genuinely unattended automation, each with its own least-privilege role.

### The case against all of that

The strongest argument against this position, stated as well as I can make it:

**I am optimising for auditability at the expense of the people who need the help most.**
The engineers I am handing Claude Code to are the ones who least need an AI assistant to
be productive — they already have tooling, scripting and command-line fluency. The
analysts I am telling to wait are the ones for whom Cowork is transformative, because it
removes the exact barrier that has always excluded them. A twelve-person team is not a
bank. Weighing a records-management gap in local session history against months of
compounding productivity for half the team may simply be the wrong trade, and "wait for
Enterprise" can be an expensive way to feel careful.

The counter-argument to my Fabric recommendation is similar and sharper: I am
recommending the older, slower path largely because the newer one is in preview, and
preview status is a statement about change velocity, not about risk. Microsoft's warnings
are generic MCP caveats that apply to every MCP client including the CLI-driven agent I
recommended. And "the model picks from a menu" versus "the agent writes a command" is a
thinner distinction than I made it sound — a command can be destructive too, and a
permission rule can gate an MCP tool call just as well as a shell command in clients that
support it.

**Where I still land, and why.** Two of the three Cowork gaps — no per-team scoping, no
project restriction — are not risk judgements, they are missing features, and no amount of
appetite makes them go away on a Team plan. That is what tips it. But if your organisation
has no formal retention obligations, enable Cowork, and I would not argue hard.

---

## Notes

**Facts basis.** Every price, quote and status traces to a numbered, dated source in
`claude-surfaces-research.md`. Prices are US list, taxes excluded; Anthropic states that
pricing, currency and tax handling vary by region, and that prices are subject to change.

**Shelf life.** Verified 2026-09-02. The Fabric Core MCP server is in preview. Cowork's
cloud sessions, Compliance API coverage of local sessions, and its admin control surface
are all actively changing. Claude Code's permission modes vary by plan and surface. Any
status claim here should be re-checked before it is relied on.

**Corrections made while researching this.** Cowork is not a research preview and is not
gated behind a Premium seat — both were true earlier in 2026 and are not now. Cowork *is*
captured in the Compliance API; a widely repeated claim that it is not is wrong. The real
gaps are narrower and are listed in section 07.

**The organisation is invented.** No real organisation, person, workspace or object name
appears anywhere in this document.
