---
name: clean-up-promotional-emails
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Clean up promotional emails."
metadata:
  status: template — resolve every TODO before use
  category: Claude in Chrome
  recommended_model: Haiku 4.5
  features: ["Browser Use"]
  surface: "Claude in Chrome"
  source_url: https://claude.com/resources/use-cases/clean-up-promotional-emails
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Clean up promotional emails — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Claude in Chrome can scan your inbox, identify promotional and marketing emails, and flag them for your review. You decide what to delete in bulk rather than clicking through one by one.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Find emails I likely don't need so I can review and bulk delete.

Flag these:
- Promotional emails from retailers/brands
- Newsletters I haven't opened in 3+ months
- Automated notifications (delivered shipping updates, expired calendar reminders)
- Marketing emails from SaaS products

Don't flag:
- Emails from actual people (not automated)
- Anything with attachments
- Anything from [my company domain]

Output: Show me the list organized by sender so I can review before deleting.
```

## Inputs

- Logged into your Gmail account before starting the Claude in Chrome session
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Claude in Chrome extension
- Gmail
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms, and ANY click that finalizes state on a third-party site (browser-use skill: show a review step first)

## Workflow

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- Nothing is submitted/saved on a website without showing the user a review step first
- Site actions limited to the domains named in the workflow
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Page fails to load or selector drifts → retry once, then stop and report; never guess at form fields
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Clean up promotional emails](https://claude.com/resources/use-cases/clean-up-promotional-emails) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
