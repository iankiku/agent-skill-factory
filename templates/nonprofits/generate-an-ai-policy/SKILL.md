---
name: generate-an-ai-policy
description: "Create organization-specific AI usage policies covering data privacy, appropriate use cases, staff guidelines, and ethical considerations tailored to your nonprofit's mission and beneficiary protection needs. Use for tasks like “Generate an AI policy” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Web Search"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/generate-an-ai-policy
  source_title: Generate an AI policy
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Generate an AI policy — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Create organization-specific AI usage policies covering data privacy, appropriate use cases, staff guidelines, and ethical considerations tailored to your nonprofit's mission and beneficiary protection needs.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I need to develop an AI usage policy for our nonprofit that serves vulnerable populations. We're a mid-sized organization (75 staff, 200 volunteers) focused on youth mental health services. We're starting to use AI tools for administrative tasks, donor communications, and some program operations, and we need clear governance.

First, use Research to find examples of AI policies from other nonprofits, particularly those serving vulnerable populations or working with youth. I want to understand what governance frameworks are emerging in the sector and what specific protections other organizations are implementing.

Key context about our organization:

We work with minors (ages 12-18) receiving mental health support

- We handle sensitive health information, family data, and personal stories
- Our donors expect transparency about how we use technology
- Staff skill levels with AI vary widely
- We're concerned about bias in AI systems affecting vulnerable populations

I'm uploading our existing data privacy policy and code of ethics so the AI policy aligns with our current standards.

Create a comprehensive AI usage policy that includes:

Governance structure:

- Who approves AI tool adoption
- Risk assessment framework
- Oversight responsibilities

Data privacy and protection:

- What data can/cannot be used with AI tools
- Beneficiary information safeguards
- Donor data protections
- Data retention and deletion protocols

Appropriate use cases:

- Approved applications (administrative, communications, analysis)
- Prohibited uses (clinical decisions, automated beneficiary assessments)
- Gray areas requiring case-by-case review

Staff guidelines:

- Training requirements
- Verification responsibilities
- When to escalate decisions to humans
- Documentation requirements

Ethical considerations:

- Bias detection and mitigation
- Transparency with beneficiaries and donors
- Mission alignment assessment
- Community impact evaluation

I need a comprehensive policy document (Word) and a simpler version for our website (md). Make these professional and board-ready with sophisticated formatting.
```

## Required context and inputs

- Files to upload: existing data privacy policy, organizational code of ethics, donor privacy policies, employee handbook sections, vendor management policies
- Web Search enabled (noted as optional but recommended)
- TODO: exact file paths / folders / message formats this skill should expect
- TODO: domain context the model cannot infer (naming conventions, thresholds, house style)

## Tools, connectors, APIs, and authentication

- No connectors detected on the source page; base Claude capabilities only
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

1. Describe the task: provide organizational context and policy requirements
2. Give Claude context: upload existing policies (data privacy, code of ethics, etc.)
3. What Claude creates: produces Word document and Excel workbook
4. Follow up prompts: three suggested refinement prompts listed
5. Tricks, tips, and troubleshooting: five practical implementation suggestions

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

- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
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

Derived from [Generate an AI policy](https://claude.com/resources/use-cases/generate-an-ai-policy) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
