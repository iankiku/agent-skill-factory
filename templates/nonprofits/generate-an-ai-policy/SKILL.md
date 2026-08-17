---
name: generate-an-ai-policy
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Generate an AI policy."
metadata:
  status: template — resolve every TODO before use
  category: Nonprofits
  recommended_model: Sonnet 4.5
  features: ["Web Search"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/generate-an-ai-policy
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Generate an AI policy — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Create organization-specific AI usage policies covering data privacy, appropriate use cases, staff guidelines, and ethical considerations tailored to your nonprofit's mission and beneficiary protection needs.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

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

## Inputs

- Files to upload: existing data privacy policy, organizational code of ethics, donor privacy policies, employee handbook sections, vendor management policies
- Web Search enabled (noted as optional but recommended)
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

1. Describe the task: provide organizational context and policy requirements
2. Give Claude context: upload existing policies (data privacy, code of ethics, etc.)
3. What Claude creates: produces Word document and Excel workbook
4. Follow up prompts: three suggested refinement prompts listed
5. Tricks, tips, and troubleshooting: five practical implementation suggestions

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- Donor/beneficiary PII is excluded from outputs unless explicitly requested
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Generate an AI policy](https://claude.com/resources/use-cases/generate-an-ai-policy) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
