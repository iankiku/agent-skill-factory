---
name: organize-your-legal-workflows-using-projects
description: "Stop explaining your review standards for every contract. Claude Projects let you upload your playbooks once and reference them automatically across hundreds of reviews. Use for tasks like “Organize your legal workflows using Projects” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Legal
  recommended_model: Opus 4.5
  features: ["Projects"]
  surface: "Claude.ai chat (Claude Projects)"
  source_url: https://claude.com/resources/use-cases/organize-your-legal-workflows-using-projects
  source_title: Organize your legal workflows using Projects
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Organize your legal workflows using Projects — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Stop explaining your review standards for every contract. Claude Projects let you upload your playbooks once and reference them automatically across hundreds of reviews.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm setting up a Project for NDA reviews at our firm. We handle about 30 NDAs a week and I want Claude to reference our standard terms, flag deviations, and maintain consistency in our review comments.

I've uploaded our NDA playbook, our standard mutual NDA template, and our list of unacceptable terms. Analyze these documents and create an NDA Review Standards Guide that captures our voice, tone, and structure we use throughout our writing. Make this a professional reference document I can upload to the Project knowledge, so Claude can reference it during every review.

Then help me craft optimized project instructions I can paste into the custom instructions field—instructions that tell Claude to reference the standards guide and apply our approach.
```

## Required context and inputs

- Upload core reference materials (review playbook, standard template, prohibited terms list)
- Google Drive, Microsoft 365, Notion, or Box connectors (optional)
- Extended Thinking for complex analysis (optional)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Box
- Google Drive
- Microsoft 365
- Notion
- TODO: confirm which connectors are enabled in the runtime that will execute this skill
- Authentication: connectors authenticate via their own OAuth flows — this skill must
  NEVER ask for, store, or echo credentials, tokens, or API keys. If auth is missing,
  stop and tell the user which connector to enable.

## Permissions and sensitive actions

- Reads: TODO (folders, channels, records this skill may read)
- Writes: TODO (what it may create/modify, and where)
- Held back for the primary agent / human: sending external communications, financial
  transactions, deleting or overwriting originals, submitting web forms

## Workflow

1. Describe the task
2. Give Claude context
3. What Claude creates
4. Follow up prompts
5. Tricks, tips, and troubleshooting

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- No changed defined terms or citations without an explicit redline entry
- Reviewed-by-human gate before anything leaves the building
- TODO: add one domain-specific check a reviewer in your org would apply

## Failure modes and fallbacks

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Apply the repo's delegation policy (`docs/delegation-policy.md` — bundle or restate
it if you install this skill outside the repo). Defaults for this template:

- Run single-agent unless a step fans out over independent items (files, records,
  vendors, channels). Only independent work parallelizes.
- Each delegated task must ship with: the minimal context slice it needs, an explicit
  output contract, a validation check the primary agent runs on the result, and a
  fallback if it returns empty or fails.
- Final review, synthesis, and every sensitive action listed above stay with the
  primary agent.
- TODO: name the concrete subtasks (if any) that qualify for delegation here.

## Attribution

Derived from [Organize your legal workflows using Projects](https://claude.com/resources/use-cases/organize-your-legal-workflows-using-projects) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
