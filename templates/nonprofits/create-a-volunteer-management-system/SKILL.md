---
name: create-a-volunteer-management-system
description: "Create comprehensive volunteer documentation including role descriptions, onboarding processes, communication templates, and tracking tools that professionalize volunteer management and scale your program effectively. Use for tasks like “Create a volunteer management system” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: []
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-a-volunteer-management-system
  source_title: Create a volunteer management system
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create a volunteer management system — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Create comprehensive volunteer documentation including role descriptions, onboarding processes, communication templates, and tracking tools that professionalize volunteer management and scale your program effectively.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I run a nonprofit that provides tutoring and reading programs to elementary students in underserved communities. We currently have 45 volunteers but our systems are fragmented—role descriptions are outdated, onboarding is inconsistent, and we track volunteers in scattered spreadsheets.

I need a complete volunteer program infrastructure that includes:

Role descriptions for:
- Reading Tutors (work one-on-one with students weekly)
- Reading Buddies (lead small group reading circles)
- Event Coordinators (organize book fairs and literacy events)
- Administrative Volunteers (data entry, scheduling, communications support)

Onboarding system including:
- Welcome packet with program overview
- Step-by-step onboarding process document
- Training requirements and timelines
- Background check procedures
- Volunteer handbook with policies

Communication templates for:
- Initial welcome email
- Training reminders
- Monthly volunteer newsletters
- Recognition and appreciation messages
- Check-in and feedback requests

Tracking system:
- Volunteer database with contact info, roles, hours, certifications
- Hours tracking and reporting
- Training completion tracker
- Impact metrics (students served, hours contributed)

Our volunteers range from college students to retirees. Most commit 2-4 hours per week. We require background checks for all roles and role-specific training. We serve 200 students across 3 schools.

Create professional, comprehensive documents that make our volunteer program feel organized and legitimate. Use clear formatting, maintain a warm but professional tone, and include practical guidance that both volunteers and staff can follow easily. Make these documents detailed enough to use immediately without extensive revision.
```

## Required context and inputs

- Optional: Google Drive and Gmail integrations
- No mandatory file uploads shown
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- Gmail
- Google Drive
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

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
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

Derived from [Create a volunteer management system](https://claude.com/resources/use-cases/create-a-volunteer-management-system) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
