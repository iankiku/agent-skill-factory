# Draft-skill validation checklist

Run every item against the draft before showing it to the user. Fix failures first;
note irreducible gaps as `ASSUMED:` lines or Setup steps.

## Triggering
- [ ] `description` says when to INVOKE the skill in the user's vocabulary, not what the skill is
- [ ] Negative scope present: at least one near-miss the skill should NOT handle
- [ ] `name` is kebab-case, unique in the target environment

## Outcome & inputs
- [ ] Outcome sentence fills all four slots: trigger, artifact, inputs, bar
- [ ] Every input has an expected location/format AND a missing/malformed behavior
- [ ] Required context contains no facts the model could infer on its own (bloat)

## Tools & auth
- [ ] Every workflow step's tool appears in the Tools section — and vice versa (no orphans)
- [ ] Zero credential VALUES anywhere; env vars referenced by name only
- [ ] Each connector marked enabled/needs-setup; needs-setup items appear under Setup

## Safety & permissions
- [ ] Sensitive-action list present and specific (not just the generic five)
- [ ] Nothing irreversible happens before the validation step passes
- [ ] No instruction tells the agent to bypass review, approval, or its own guidelines

## Workflow quality
- [ ] 3–9 steps, each imperative, each naming inputs and outputs
- [ ] Every decision point has a deciding rule (no "use judgment" forks)
- [ ] At least one validation check is mechanical (count, recompute, schema) — not vibes
- [ ] Every external dependency has a failure mode with retry policy and degraded path
- [ ] A "stop and report" condition exists (the skill knows when to give up)

## Output economy
- [ ] Skill instructs concise output: result first, no preamble or work-summary
- [ ] No section present that doesn't change behavior (no "n/a" filler)

## Delegation
- [ ] Delegation decided: a fan-out plan with all four contract fields, or the single line "Runs single-agent"
- [ ] Each delegated task defines all four: context, output, validation, fallback
- [ ] Only independent work is parallelized; merge/validate follows every fan-out
- [ ] Final review + all sensitive actions assigned to the primary agent

## Attribution & hygiene
- [ ] If derived from a catalog template: source URL + © Anthropic PBC attribution retained
- [ ] Assumptions section lists every default you chose for the user, labeled `ASSUMED:`
- [ ] Setup section is complete enough that a colleague could provision from it alone
- [ ] Dry-run trace produced and shown to the user before finalizing
