---
name: research-and-compare-travel-destinations
description: "TODO — write for triggering: when should this fire, in the user's own words, plus one near-miss it must NOT handle. Seed use case: Research and compare travel destinations."
metadata:
  status: template — resolve every TODO before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Web Search", "Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/research-and-compare-travel-destinations
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Research and compare travel destinations — skill template

Resolve every `TODO`, then delete this line. Sections that don't apply to your
version: delete them. A short skill that names its inputs and checks its output
beats a complete-looking one.

## Outcome

Create a visual comparison spreadsheet from research with images, ratings, and insights to simplify your travel planning.

TODO: one sentence for YOUR context — who runs this, on what input, producing what,
how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm planning a June vacation leaving from San Francisco, and I'm deciding between 5 destinations: Lisbon, Reykjavik, Dubrovnik, Kyoto, and Oaxaca.

Can you research these places and create a comparison spreadsheet that helps me visualize the differences across various dimensions? I want to see them side-by-side so I can compare easily.

Use color-coding or visual indicators to help me spot patterns quickly (like heat maps). Include hyperlinks to official tourism sites so I can learn more, and add cell comments explaining ratings when it's helpful and a small image of the place at the top (small, thumbnail sized photos - verify and resize if too big).

Make it look really polished and professional - something I'd feel confident sharing with my travel group. The layout should be clean and sophisticated - think premium travel magazine quality, not a basic spreadsheet. I want all five destinations visible at once so I can compare them easily.
```

## Inputs

- Web Search (toggle on before starting)
- Extended Thinking (optional, for deeper analysis)
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

1. Follow up prompts (refinement options provided)

TODO: rewrite as imperative steps for the executing agent.

## Output

Return the shortest form that carries the result. No preamble, no restating the
request, no summary of what you just did. Expand only when the user asks for detail.

## Validation

- Every factual claim traces to a provided input, connector record, or cited source
- TODO: one domain-specific check a reviewer in your org would apply

## Failure modes

- Search returns thin/conflicting results → present both readings with sources instead of picking one silently
- Ambiguous or missing input → ask one targeted question; if unattended, state the assumption inline and proceed
- Any step would take a sensitive/irreversible action → stop and hand back to the user (see Delegation)

## Delegation

Runs single-agent. TODO: if a step fans out over independent items (files, records,
vendors, channels), plan it per `docs/delegation-policy.md` and delete this line.

## Attribution

Derived from [Research and compare travel destinations](https://claude.com/resources/use-cases/research-and-compare-travel-destinations) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
