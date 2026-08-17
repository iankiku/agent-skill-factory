---
name: build-skill
description: Build a new Claude skill (SKILL.md) for one recurring workflow. Use when the user says "build me a skill", "make this repeatable as a skill", "turn what we just did into a skill", or wants an installable skill for their industry or team. Interviews the user, starts from the closest of 94 Anthropic-published use-case templates, and delivers a complete SKILL.md. Not for one-off automations, scripts, or cron jobs that need no SKILL.md.
---

# build-skill

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

See `examples/` for two end-to-end transcripts: one connector-heavy business skill
(weekly pipeline digest) and one file-processing skill (invoice folder triage),
each showing the interview, an "I don't know" → labeled assumption, template
selection, the delegation decision, a dry-run trace, and the final SKILL.md.
