---
name: explore-what-claude-can-do-for-you
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Explore what Claude can do for you."
metadata:
  status: template — resolve every TODO before use
  category: Professional
  recommended_model: Opus 4.5
  features: ["Connectors"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/explore-what-claude-can-do-for-you
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Explore what Claude can do for you — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

New to Claude? Start here. Tell Claude your role and get a personalized guide to the capabilities that will matter for your work.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm a product manager at a B2B SaaS startup. I mostly work on roadmap prioritization and customer research. I'm new to Claude. How can I use you most efficiently? Can you give me 5 examples I can try right now, ideally things that would actually make a difference in my daily work. Surprise me with one of them! I've given you access to my docs (I think) to help you understand better what I do. Thanks!
```

## Inputs

- Google Drive connector (optional)
- Extended Thinking (optional)
- TODO: exact paths / folders / formats expected at run time
- TODO: domain context the model can't infer (conventions, thresholds, house style)

## Tools and auth

- Google Drive
- TODO: confirm these are enabled in the runtime that will execute this skill
- Connector OAuth or env-var NAMES only — never credential values.

## Permissions

- Reads: TODO
- Writes: TODO
- Never without a human: external comms, financial transactions, deleting or
  overwriting originals, submitting web forms

## Workflow

1. Describe the task (tell Claude your role)
2. Give Claude context (share documents for more specific suggestions)
3. See what Claude creates (receive personalized starter guide with example prompts)
4. Follow up prompts (continue conversation to refine or explore further)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Connector unavailable or unauthenticated → pause, tell the user exactly which connector to enable and why; offer a degraded run from uploaded files
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Explore what Claude can do for you](https://claude.com/resources/use-cases/explore-what-claude-can-do-for-you) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
