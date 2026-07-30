---
name: create-new-hire-onboarding-guides
description: "Turn standard company information and a new hire's specific details into a personalized welcome guide. Claude organizes logistics, schedules, and key contacts into one clear document that helps new employees feel prepared from day one. Use for tasks like “Create new hire onboarding guides” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: HR
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-new-hire-onboarding-guides
  source_title: Create new hire onboarding guides
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create new hire onboarding guides — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Turn standard company information and a new hire's specific details into a personalized welcome guide. Claude organizes logistics, schedules, and key contacts into one clear document that helps new employees feel prepared from day one.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

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

## Required context and inputs

- Google Calendar integration (required)
- Uploads: company handbook, office logistics documents, role-specific onboarding information
- Slack channel access (e.g. #design-systems)
- Optional: Extended Thinking (recommended)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Google Calendar
- Slack
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
- No inferences about protected attributes; tone reviewed for policy compliance
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

Derived from [Create new hire onboarding guides](https://claude.com/resources/use-cases/create-new-hire-onboarding-guides) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
