---
name: build-skill
description: Build a new Claude skill (SKILL.md) for one recurring workflow. Use when the user says "build me a skill", "make this repeatable as a skill", "turn what we just did into a skill", or wants an installable skill for their industry or team. Interviews the user, starts from the closest of 94 Anthropic-published use-case templates, and delivers a complete SKILL.md. Not for one-off automations, scripts, or cron jobs that need no SKILL.md.
---

# build-skill

> **This is the single-file, standalone bundle of build-skill** — everything it
> needs (the skill itself plus its four reference files) is inlined below so you
> can install it by copying this ONE file, no `git clone` or GitHub account
> required. See "Install" at the very bottom for the two ways to use it.
>
> Wherever the instructions below say "read `references/<file>.md`", the content
> is already inlined in the "Bundled reference files" section further down this
> same document — there is nothing extra to fetch.


You are helping the user turn ONE narrow, domain-specific outcome into an executable
skill. Optimize for a skill that runs correctly unattended, not for an impressive
document. A short skill that names its inputs, checks its outputs, and knows when to
stop beats a long one that assumes.

## Ground rules (apply throughout)

- One outcome per skill. If the user describes two, split them and build the more
  valuable one first; note the second as a follow-up.
- Never put secrets in a skill. No API keys, tokens, passwords, or connection strings
  in SKILL.md, examples, or committed files — reference connectors (which authenticate
  at the platform layer) or environment variables by NAME only. If the user pastes a
  secret during the interview, do not echo it back and do not write it anywhere.
- Ask questions with the AskUserQuestion tool when available, at most 3–4 per round,
  each with concrete options. Never interrogate; every question must change what you
  build.
- Lean by default, in both directions. The skill you write should be the shortest one
  that runs correctly — cut any section that doesn't change behavior — and it should
  instruct its own runtime output to be concise: deliver the result, not a preamble, a
  restatement of the request, or a summary of the work. Verbosity is opt-in, either
  because the skill asks the user a question or because the user asked for detail.

- **"I don't know" protocol:** when the user can't answer a question, immediately
  re-ask it as 2–4 concrete options with a recommended default. If they still can't
  choose after a total of THREE attempts on the same decision (original question +
  two option-based retries), stop asking: pick the most practical default, record it
  in the draft under an `## Assumptions` section as `ASSUMED: <decision> — <why this
  default>`, tell the user you did so, and proceed. Never stall a draft on an
  unanswered question.

## Phase 1 — Pin the outcome

Get one sentence of the form: **"When <trigger>, produce <artifact> from <inputs>,
meeting <bar>."** Ask targeted questions until you can fill all four slots:

1. Trigger — what starts a run? (user request, schedule, event, incoming file/email)
2. Artifact — what exists afterward that didn't before? (file, message, record, report)
3. Inputs — what does a run consume? (files, folders, connector data, URLs, user text)
4. Bar — how would the user recognize a GOOD run vs. a technically-complete one?

Also establish scope edges: what near-miss requests should this skill REFUSE or route
elsewhere? A skill that triggers too broadly is worse than no skill.

Before moving on, write a 10-line skeleton — name, draft description, the outcome
sentence, 3–5 workflow steps, a first-guess validation check — and show it. Every
later question edits that skeleton instead of a blank page; it is much easier for a
user to correct something concrete than to answer an abstract question.

## Phase 2 — Select the closest template

Read `references/template-index.md` (compact, capability-tagged index of the 94
templates in `templates/`). Select by, in order: same artifact type → same input
sources/connectors → same domain/category. Read the top candidate's SKILL.md and
reuse its structure, validation defaults, and failure modes. Tell the user which
template you chose and why in one sentence. If nothing matches on artifact OR inputs,
say so and build from `references/blank-skill-template.md` instead — do not force a
bad template. If this skill is installed standalone and the `templates/` bodies
aren't readable in your environment, use the index entry's summary plus the blank
template — never fail the run over a missing template file.

## Phase 3 — Specify the machinery

Work through each item below. Pull answers from the interview first, the template's
defaults second, targeted questions third (the "I don't know" protocol applies):

- **Required context:** domain facts the model can't infer — naming conventions,
  thresholds, house style, definitions of local jargon. Capture as bullet points or
  reference files the skill will ship with.
- **Files & inputs:** exact paths/folders/formats expected at run time; what to do
  when they're missing or malformed.
- **Tools, APIs, connectors:** name each one and what it's used for. For each
  connector: is it enabled in the runtime that will execute this skill? Mark unknowns
  as setup steps, not assumptions.
- **Authentication:** how each tool authenticates (connector OAuth, env-var name,
  CLI already logged in). Names only — never values.
- **Permissions:** what the skill may read, what it may write, and the explicit list
  of actions it must NEVER take without human approval.
- **Workflow steps:** 3–9 imperative steps: gather → process → produce → validate →
  deliver. Each step names its inputs and outputs.
- **Decision points:** every fork in the workflow, with the rule that decides it.
  Default rule: prefer the reversible option; surface ambiguity rather than picking
  silently.
- **Validation criteria:** checks the skill runs on its OWN output before delivering
  — recompute totals programmatically, verify counts, check every claim traces to an
  input. At least one check must be mechanical (a script or count), not vibes.
- **Failure modes & fallbacks:** for each dependency (connector, file, site, API):
  what failure looks like, the retry policy (default: once), the degraded path, and
  when to stop and report instead of improvising.
- **Delegation:** if a step fans out over independent items, plan it per
  `references/delegation-policy.md` — every delegated task defines context, output,
  validation, and fallback; final review and sensitive actions stay with the primary
  agent. Otherwise the section is one line: "Runs single-agent." Don't delegate when
  unsure.

## Phase 4 — Draft, validate, refine

1. Write the draft using `references/blank-skill-template.md` for structure (or the
   chosen template's). The `description` is written for TRIGGERING — what requests
   should invoke it, in the user's vocabulary, including negative scope. Include only
   the sections that change behavior; omit the rest rather than filling them with
   "n/a".
2. Self-check the draft against `references/validation-checklist.md`. Fix what fails.
3. **Dry-run:** walk one realistic input through the workflow ON PAPER, step by step,
   and show the user the trace — where each decision point fires, what validation
   catches, what the output looks like. This is the fastest way to expose gaps.
4. Present the draft plus the dry-run trace. Ask for corrections on: trigger wording,
   the validation bar, and any `ASSUMED:` line. Refine in place — at most one
   clarifying round per revision, then re-run the checklist.
5. When the user accepts (or after two refinement rounds with no blocking feedback),
   deliver the skill folder: `SKILL.md` plus any reference files, with a one-paragraph
   install note for their environment (claude.ai skill upload, Cowork, or Claude Code
   `.claude/skills/`).

## What good looks like

The full repo ships two end-to-end example transcripts (a connector-heavy business
skill and a file-processing skill) under `examples/` — not inlined here to keep this
bundle short; see the "Install" section below for where to find them if you want the
complete repo.

---

## Bundled reference files

These are inlined verbatim so this single file is fully self-contained. In the full
repo they live at `skills/build-skill/references/<name>.md`.

### `references/template-index.md`

One line per template: `path | category | artifact/outcome | inputs & connectors | features`.
Select by artifact type first, then input sources, then category. Paths are relative to the repo root.

**Categories covered:** Claude in Chrome, Cowork, Education, Finance, HR, Legal, Life
Sciences, Marketing, Nonprofits, Personal, Professional, Research, Sales — 94
templates total. The full capability-tagged index (all 94 one-line entries) lives at
`skills/build-skill/references/template-index.md` in the
[full repo](https://github.com/iankiku/agent-skill-factory) — it's ~140 lines and
was left out of this bundle to keep the copy-paste file short. If you're using this
standalone bundle without the full index, treat Phase 2 as: ask the user for the
closest match to one of the 13 categories above, or fall back to the blank template
below — never stall the draft over a missing index.

### `references/blank-skill-template.md`

## Blank skill template

Use when no catalog template matches the outcome on artifact type OR input sources.
Required: Outcome, Inputs, Workflow, Validation, Permissions (what it must never do
without a human), Setup. Everything else is included only when it changes behavior —
delete it otherwise. A section reading "n/a" is worse than no section: it costs the
runtime tokens and teaches the model that empty structure is acceptable.

```markdown
---
name: <kebab-case-name>
description: <What it produces and WHEN to invoke it, in the user's vocabulary.
  Include negative scope: "Do NOT use for <near-miss>.">
---

## <Skill title>

### Outcome
When <trigger>, produce <artifact> from <inputs>, meeting <bar>.

### Assumptions
<Only if the interview left decisions open. Each line: "ASSUMED: <decision> — <why>".
Delete the section when empty.>

### Required context
<Domain facts the model can't infer: conventions, thresholds, house style, jargon.>

### Inputs
<Exact paths/folders/formats expected at run time; behavior when missing/malformed.>

### Tools, connectors, APIs & authentication
<Each tool + what it's for + how it authenticates (connector OAuth / env-var NAME /
pre-authenticated CLI). Never credential values. Missing auth = stop and instruct.>

### Permissions
Reads: <...>  Writes: <...>
Never without human approval: <external sends, system-of-record writes, deletions,
payments, form submissions — plus skill-specific items>.

### Workflow
1. <gather> → 2. <process> → ... → n-1. <validate> → n. <deliver>
<Each step names its inputs and outputs.>

### Decision points
<Each fork + the rule that decides it. Default: prefer reversible; surface ambiguity.>

### Output

Shortest form that carries the result. No preamble, no restating the request, no
summary of the work performed. Expand only on request.

### Validation
<Checks run on the skill's OWN output before delivery. At least one mechanical check.>

### Failure modes & fallbacks
<Per dependency: failure signature → retry policy → degraded path → when to stop
and report.>

### Delegation
<Per the delegation policy (bundled with build-skill as
references/delegation-policy.md; restate the relevant rules inline so the generated
skill is self-contained). Either the per-step plan with the four contract
fields (context, output, validation, fallback) for each delegated task, or:
"Runs single-agent; no step meets the delegation bar." Parallelize only independent
work. Final review and sensitive actions stay with the primary agent.>

### Setup
<Everything the user must provision before first run: connectors to enable, files
to place, folder access to grant, env vars to set (names only).>
```

### `references/delegation-policy.md`

## Delegation policy

Every skill generated in this repository embeds a delegation decision: when does the
primary agent do the work itself, and when does it hand a task to a capability-matched
model or sub-agent? This document is the single source of truth; generated skills
reference it and specialize its defaults.

### The decision, in order

1. **Does the step require trust the sub-agent can't carry?** Sensitive actions —
   sending external communications, writing to systems of record, financial
   transactions, deleting/overwriting originals, submitting web forms, anything
   irreversible — are NEVER delegated. The primary agent performs them, after final
   review, with human approval where the skill demands it.
2. **Is the step the synthesis?** Final review, cross-checking sub-results against
   each other, and assembling the deliverable stay with the primary agent. A sub-agent
   never grades its own work into the final artifact.
3. **Is the step self-contained?** Delegate only when the task can be specified with a
   closed context slice (the sub-agent needs nothing it wasn't handed) and a closed
   output contract (the primary can validate the result without re-doing the work).
   If specifying the task takes longer than doing it, don't delegate.
4. **Does capability match cost?** Route mechanical, high-volume steps (per-file
   extraction, per-record formatting, bulk classification) to a smaller/faster model;
   route judgment-heavy steps (ambiguous classification, adversarial verification,
   domain reasoning) to the strongest available model. Default: inherit the primary's
   model when unsure.

### The contract every delegated task must define

A skill that delegates MUST specify, per delegated task — no exceptions:

| Field | Meaning |
|---|---|
| **Context** | The minimal input slice the sub-agent receives (files, records, instructions). Nothing implicit. |
| **Output** | The exact deliverable and format (schema, file path, or structured summary). |
| **Validation** | The check the PRIMARY agent runs on the returned result before using it (schema-valid? count matches? spot-check passes?). |
| **Fallback** | What happens when the task fails or returns empty: retry once, degrade to primary doing it inline, or surface to the user. |

### Parallelization

- Parallelize **only independent work**: tasks that share no mutable state and whose
  outputs don't feed each other. Per-item fan-out (one task per file/vendor/channel)
  is the canonical safe case.
- Anything sequential by nature — a step consuming the previous step's output —
  runs in order, no barrier games.
- After a parallel fan-out, the primary agent merges, dedupes, and validates the
  results before anything downstream uses them.

### What stays with the primary agent — always

- Final review of the assembled deliverable against the skill's validation criteria
- All sensitive actions (list above), each behind explicit user approval when the
  skill touches external systems
- Secrets and credentials: sub-agents never receive tokens, keys, or passwords;
  connectors authenticate at the platform layer, and skills never proxy credentials
- The decision to stop: when validation fails twice, the primary halts and reports
  rather than delegating a third attempt

### `references/validation-checklist.md`

## Draft-skill validation checklist

Run every item against the draft before showing it to the user. Fix failures first;
note irreducible gaps as `ASSUMED:` lines or Setup steps.

### Triggering
- [ ] `description` says when to INVOKE the skill in the user's vocabulary, not what the skill is
- [ ] Negative scope present: at least one near-miss the skill should NOT handle
- [ ] `name` is kebab-case, unique in the target environment

### Outcome & inputs
- [ ] Outcome sentence fills all four slots: trigger, artifact, inputs, bar
- [ ] Every input has an expected location/format AND a missing/malformed behavior
- [ ] Required context contains no facts the model could infer on its own (bloat)

### Tools & auth
- [ ] Every workflow step's tool appears in the Tools section — and vice versa (no orphans)
- [ ] Zero credential VALUES anywhere; env vars referenced by name only
- [ ] Each connector marked enabled/needs-setup; needs-setup items appear under Setup

### Safety & permissions
- [ ] Sensitive-action list present and specific (not just the generic five)
- [ ] Nothing irreversible happens before the validation step passes
- [ ] No instruction tells the agent to bypass review, approval, or its own guidelines

### Workflow quality
- [ ] 3–9 steps, each imperative, each naming inputs and outputs
- [ ] Every decision point has a deciding rule (no "use judgment" forks)
- [ ] At least one validation check is mechanical (count, recompute, schema) — not vibes
- [ ] Every external dependency has a failure mode with retry policy and degraded path
- [ ] A "stop and report" condition exists (the skill knows when to give up)

### Output economy
- [ ] Skill instructs concise output: result first, no preamble or work-summary
- [ ] No section present that doesn't change behavior (no "n/a" filler)

### Delegation
- [ ] Delegation decided: a fan-out plan with all four contract fields, or the single line "Runs single-agent"
- [ ] Each delegated task defines all four: context, output, validation, fallback
- [ ] Only independent work is parallelized; merge/validate follows every fan-out
- [ ] Final review + all sensitive actions assigned to the primary agent

### Attribution & hygiene
- [ ] If derived from a catalog template: source URL + © Anthropic PBC attribution retained
- [ ] Assumptions section lists every default you chose for the user, labeled `ASSUMED:`
- [ ] Setup section is complete enough that a colleague could provision from it alone
- [ ] Dry-run trace produced and shown to the user before finalizing

---

## Install

Copy this whole file and save it as `SKILL.md` inside a folder named `build-skill`:

- **Claude Code / Claude CLI:** `~/.claude/skills/build-skill/SKILL.md` (all projects),
  or `.claude/skills/build-skill/SKILL.md` inside one project.
- **Claude.ai / Claude Desktop:** Settings → Capabilities → Skills → upload this file
  (or a `.zip` containing it as `SKILL.md`).
- **Cowork:** same as Claude Desktop — upload via the Skills settings panel.

With Node.js, `npx skills add iankiku/agent-skill-factory --skill build-skill` installs
the full repo version instead (complete 94-entry template index, two worked examples).

Step-by-step install and the first prompt to run: **`0-README.md`** in the
[public gist](https://gist.github.com/iankiku/0366d5701cf8268ee05c24cd30fa366b).
The other 93 use cases, their templates, and a copy-paste prompt for each:
**https://github.com/iankiku/agent-skill-factory**
