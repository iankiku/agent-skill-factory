---
name: create-custom-course-materials
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Create custom course materials."
metadata:
  status: template — resolve every TODO before use
  category: Education
  recommended_model: Sonnet 4.5
  features: ["Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/create-custom-course-materials
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Create custom course materials — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Transform handwritten equations and notes into formatted LaTeX documents without manual typesetting.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm a math professor converting my handwritten integration notes into a professional course materials. I have:

* Handwritten notes with equations
* A typed outline of topics

Craft a professional-looking LaTeX document, resembling a published textbook page with colored boxes and precise equations, then convert it to PDF.
```

## Inputs

- Upload handwritten notes (JPEG format) or class syllabus (PDF)
- Extended Thinking enabled for complex mathematical content and LaTeX compilation
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- No connectors detected on the source page; base Claude capabilities only
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task—specify handwritten notes and course objectives you want converted
2. Give Claude context by uploading handwritten notes, equations, or course materials
3. Claude creates a complete LaTeX document with professional formatting and compiled PDF
4. Follow up with prompts to enhance design, generate problem sets, or expand content

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Create custom course materials](https://claude.com/resources/use-cases/create-custom-course-materials) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
