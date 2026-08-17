---
name: create-new-hire-onboarding-guides
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create new hire onboarding guides."
metadata:
  status: template — resolve every TODO before use
  category: HR
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-new-hire-onboarding-guides
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create new hire onboarding guides — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Turn standard company information and a new hire's specific details into a personalized welcome guide. Claude organizes logistics, schedules, and key contacts into one clear document that helps new employees feel prepared from day one.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
Create a first week guide for Sarah Chen, starting as Senior Product Designer on our Design Systems team this Monday, November 4th. Her manager is Michael Torres.

Include:
- Welcome and what to expect their first week
- Her specific onboarding schedule
- Office logistics
- Team introductions
- Tools and access she'll receive
- Common first-week questions

To find relevant information, search my Google Calendar for onboarding events, her team's slack channel #design-systems, and all the documents I've uploaded.

Make it information-dense but beautifully organized—a senior designer should look at this and think "they have great taste here." Use sophisticated typography and layout, not generic HR formatting. She should be able to scan it quickly but find everything she needs.
```

## Inputs

- Google Calendar integration (required)
- Uploads: company handbook, office logistics documents, role-specific onboarding information
- Slack channel access (e.g. #design-systems)
- Optional: Extended Thinking (recommended)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Google Calendar
- Slack
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

TODO: 3–9 imperative steps: gather inputs → process → produce artifact → validate → deliver.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- No inferences about protected attributes; tone reviewed for policy compliance
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Create new hire onboarding guides](https://claude.com/resources/use-cases/create-new-hire-onboarding-guides) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
