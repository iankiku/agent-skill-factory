---
name: create-a-volunteer-management-system
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create a volunteer management system."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: []
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-a-volunteer-management-system
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create a volunteer management system — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Create comprehensive volunteer documentation including role descriptions, onboarding processes, communication templates, and tracking tools that professionalize volunteer management and scale your program effectively.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

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

## Inputs

- Optional: Google Drive and Gmail integrations
- No mandatory file uploads shown
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Gmail
- Google Drive
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
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Create a volunteer management system](https://claude.com/resources/use-cases/create-a-volunteer-management-system) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
