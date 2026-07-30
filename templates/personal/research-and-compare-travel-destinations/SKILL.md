---
name: research-and-compare-travel-destinations
description: "Create a visual comparison spreadsheet from research with images, ratings, and insights to simplify your travel planning. Use for tasks like “Research and compare travel destinations” and close variants. TEMPLATE — customize before installing."
metadata:
  status: template — customize all TODO markers before use
  category: Personal
  recommended_model: Sonnet 4.5
  features: ["Web Search", "Extended Thinking"]
  surface: "Claude.ai chat"
  source_url: https://claude.com/resources/use-cases/research-and-compare-travel-destinations
  source_title: Research and compare travel destinations
  retrieved_at: 2026-07-26
  attribution: "Seed prompt and workflow © Anthropic PBC (claude.com/resources/use-cases); scaffold original to agent-skill-factory"
---

# Research and compare travel destinations — skill template

Turn this template into a working skill by resolving every `TODO`. The seed prompt
below is the published Anthropic example this template was derived from; your skill
should generalize it for repeated, hands-off use.

## Outcome

Create a visual comparison spreadsheet from research with images, ratings, and insights to simplify your travel planning.

TODO: Restate the outcome for YOUR context in one sentence: who runs this, on what
input, producing what artifact, how often.

## Seed prompt (verbatim from source, © Anthropic PBC)

```text
I'm planning a June vacation leaving from San Francisco, and I'm deciding between 5 destinations: Lisbon, Reykjavik, Dubrovnik, Kyoto, and Oaxaca.

Can you research these places and create a comparison spreadsheet that helps me visualize the differences across various dimensions? I want to see them side-by-side so I can compare easily.

Use color-coding or visual indicators to help me spot patterns quickly (like heat maps). Include hyperlinks to official tourism sites so I can learn more, and add cell comments explaining ratings when it's helpful and a small image of the place at the top (small, thumbnail sized photos - verify and resize if too big).

Make it look really polished and professional - something I'd feel confident sharing with my travel group. The layout should be clean and sophisticated - think premium travel magazine quality, not a basic spreadsheet. I want all five destinations visible at once so I can compare them easily.
```

## Required context and inputs

- Web Search (toggle on before starting)
- Extended Thinking (optional, for deeper analysis)
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

1. Describe the task
2. Give Claude context
3. What Claude creates
4. Follow up prompts (refinement options provided)
5. Tricks, tips, and troubleshooting

TODO: adapt the steps above (from the source page) into imperative instructions for the executing agent, including what to do between steps.

## Decision points

- TODO: list each point where the skill must choose between paths, with the rule to apply
- Default rule: prefer the reversible option; when two readings of the input are
  plausible, surface both rather than picking silently.

## Validation criteria

- Output matches the outcome statement above (spot-check against the seed prompt's asks)
- Every factual claim is traceable to a provided input, connector record, or cited source
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

Derived from [Research and compare travel destinations](https://claude.com/resources/use-cases/research-and-compare-travel-destinations) (retrieved 2026-07-26). Seed prompt and
workflow content © Anthropic PBC. Scaffold structure original to this repository.
