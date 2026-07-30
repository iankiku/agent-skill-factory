# agent-skill-factory

A catalog of the 94 use cases Anthropic publishes at
[claude.com/resources/use-cases](https://claude.com/resources/use-cases) — reproduced
with attribution and consistent metadata — plus a skill template derived from each
one, and a primary **`build-skill`** skill that turns any narrow, domain-specific
outcome into an executable Claude skill.

Not an official Anthropic project. See [ATTRIBUTION.md](ATTRIBUTION.md) for the
licensing posture of the reproduced content.

## What's here

| Path | Contents |
|---|---|
| [`INDEX.md`](INDEX.md) | Every use case by category, linking source page, catalog doc, and template |
| [`catalog/`](catalog/) | 94 use-case docs: YAML frontmatter metadata + verbatim seed prompt + attribution |
| [`templates/`](templates/) | 94 skill templates (one `SKILL.md` scaffold per use case, organized by category) |
| [`skills/build-skill/`](skills/build-skill/) | The primary skill: interview → template selection → draft → dry-run → refine |
| [`docs/`](docs/) | [Setup](docs/SETUP.md) and the [delegation policy](docs/delegation-policy.md) all skills inherit |
| [`data/`](data/) | Machine-readable layer: `manifest.json` + one raw JSON per use case |
| [`scripts/generate.py`](scripts/generate.py) | Regenerates `catalog/`, `templates/`, and `INDEX.md` from `data/raw/` |

## The 60-second tour

**Want a ready-made starting point?** Find your workflow in [`INDEX.md`](INDEX.md),
open its template under `templates/<category>/<name>/SKILL.md`, resolve the `TODO`
markers, and install it (see [docs/SETUP.md](docs/SETUP.md)).

**Want a skill for something the catalog doesn't cover?** Install
[`skills/build-skill/`](skills/build-skill/SKILL.md) and tell Claude what outcome you
want to make repeatable. It interviews you, picks the closest of the 94 templates
(or a blank one), specifies inputs, tools, auth, permissions, validation, failure
modes, and a delegation plan, then drafts and refines the skill with you — including
a paper dry-run before you trust it. If you keep answering "I don't know", it offers
concrete options, and after three attempts it makes clearly labeled assumptions and
proceeds rather than stalling.

## Design decisions worth knowing

- **Verbatim prompts, labeled provenance.** Seed prompts are reproduced word-for-word
  and marked © Anthropic PBC; everything scaffolded around them is original to this
  repo (MIT — the license file is unmodified MIT; the split is defined in
  [ATTRIBUTION.md](ATTRIBUTION.md)). Metadata is uniform across all 94 entries:
  category, recommended model, features, surface, source URL, retrieval date, and
  extraction status (`ok`, or `partial` when a page showed no boxed example prompt
  and the task text from its steps was used instead).
- **Delegation is a first-class section.** Every template and every generated skill
  must decide primary-agent vs. sub-agent execution per step, define
  context/output/validation/fallback for each delegated task, parallelize only
  independent work, and keep final review and sensitive actions with the primary
  agent. The canonical rules are [docs/delegation-policy.md](docs/delegation-policy.md)
  (bundled verbatim into `build-skill`'s references so the skill travels standalone).
- **No secrets, ever.** Skills reference connectors and env-var *names*; credential
  values never appear in a skill, an example, or this repo. See the checklist in
  [`skills/build-skill/references/validation-checklist.md`](skills/build-skill/references/validation-checklist.md).
- **Regenerable.** The markdown layer is a build artifact of `data/raw/`. To refresh
  after Anthropic updates their pages: re-extract the JSONs, then
  `python3 scripts/generate.py`.

## End-to-end examples

Two complete `build-skill` transcripts — interview, "I don't know" handling,
template selection, delegation decisions, dry-run trace, and final skill:

- [Weekly pipeline digest](skills/build-skill/examples/example-1-weekly-pipeline-digest.md) — connector-heavy (HubSpot, Fireflies, Slack)
- [Invoice folder triage](skills/build-skill/examples/example-2-invoice-folder-triage.md) — pure file processing in Cowork
