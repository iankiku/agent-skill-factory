# Skill Benchmark: build-skill

**Model**: claude-sonnet-5
**Date**: 2026-07-30T13:40:00Z
**Evals**: 0, 1, 2 (3 runs each per configuration)

## Summary

| Metric | With Skill | Without Skill | Delta |
|--------|------------|---------------|-------|
| Pass Rate | 100% ± 0% | 62% ± 27% | +0.38 |
| Time | 258.9s ± 45.5s | 211.2s ± 76.5s | +47.7s |
| Tokens | 99575 ± 9690 | 79366 ± 9572 | +20209 |

## Notes

- build-skill's win is concentrated on artifact type and rigor, not raw task competence: on the pure file-processing eval (invoice-folder-to-csv) the baseline scored 86% even without the skill, because Claude can solve that class of task well unassisted. The delta is much bigger on the connector-heavy eval (hubspot-slack-weekly-digest, 100% vs 33%) and the no-catalog-match eval (commit-message-drafter, 100% vs 67%), where the missing delegation plan, mechanical validation section, and transparent template provenance are exactly what a generic response skips.
- The 'Validation bar matches the team's exact format' assertion (eval 2) is the cleanest with/without split: with-skill produced 4 concrete mechanical checks (regex, char-count, mood-list, diff-echo heuristic); without-skill described the same format in prose with nothing to mechanically check it against. This is build-skill's Phase 3 'at least one check must be mechanical, not vibes' rule working as intended.
- without_skill is faster and cheaper on average (211s/79k tokens vs 259s/100k tokens) — expected, since it skips the interview/template-selection/dry-run/checklist phases entirely. The cost delta (+21%) buys a completely different, reusable artifact type, not just a better version of the same one-off answer.
- Both with_skill and without_skill passed every 'no credential values leaked' check across all 6 runs — the secrets ground rule holds regardless of whether build-skill is used, likely because none of the three tasks required a genuinely novel unsupported credential type.
- Only 1 run per configuration per eval (not the usual 3) — stddev of 0 on with_skill's pass_rate reflects perfect-3-for-3 agreement across evals, not per-eval repeat-run variance. Treat these as directional results from a first pass, not a statistically tight benchmark.