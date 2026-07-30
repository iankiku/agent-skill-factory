# Setup

## Install the build-skill skill

**Claude.ai / Cowork (recommended):** zip the `skills/build-skill/` folder and upload
it as a skill (Settings → Capabilities → Skills, or ask Claude in a Cowork session to
install it). The folder is self-contained — `SKILL.md` plus `references/` and
`examples/` travel with it.

**Claude Code:** copy `skills/build-skill/` into your project's `.claude/skills/`
directory (or `~/.claude/skills/` for all projects). Invoke with `/build-skill` or by
asking to "build a skill for …".

Note: `build-skill` reads `references/template-index.md` and template files by
relative path. In claude.ai the bundled `references/` are always available; template
bodies under `templates/` are only readable when the repo itself is present (Claude
Code checkout, or a Cowork session with this repo cloned/connected). Without them,
build-skill still works — it falls back to `references/blank-skill-template.md`.

## Use a catalog template directly

1. Find your workflow in [`../INDEX.md`](../INDEX.md).
2. Copy `templates/<category>/<name>/` somewhere you can edit it.
3. Resolve every `TODO` marker — the template tells you what each one needs.
4. Rename the skill (frontmatter `name`) so it won't collide, sharpen the
   `description` for triggering, and delete the `status:` line under `metadata:`.
5. Install as above. Run it once on a low-stakes input before trusting it.

## Prerequisites by feature

Templates inherit prerequisites from their source use case (listed per template):

- **Connectors** — enable the named connector(s) in Claude's settings; they
  authenticate via their own OAuth flows. Skills never handle credentials.
- **Browser Use** — requires the Claude in Chrome extension with site permissions
  granted for the domains the skill touches.
- **Cowork** — requires a Cowork session with the relevant folder connected.
- **Claude for Excel / Word** — requires the respective add-in installed.
- **Custom visuals / Extended Thinking / Web Search / Research** — toggle the
  feature in the conversation where the skill runs.

## Secrets policy

No skill in this repo asks for, stores, or echoes credentials. If a skill you
generate needs an API that has no connector, reference an environment variable by
NAME in the skill and set the value only in the runtime's env — never in the skill
file, never in this repo. `.gitignore` blocks `.env` files as a backstop.

## Regenerating the catalog

```bash
# refresh data/raw/*.json first (re-extract from claude.com), then:
python3 scripts/generate.py   # rebuilds catalog/, templates/, INDEX.md
```

Regeneration overwrites `catalog/` and `templates/` entirely — customize copies,
not the generated trees.

## Validating your first generated skill

Follow either end-to-end example as a reference run
([1](../skills/build-skill/examples/example-1-weekly-pipeline-digest.md),
[2](../skills/build-skill/examples/example-2-invoice-folder-triage.md)): the
dry-run trace pattern in Phase 5 — one realistic input walked through every step on
paper, validations shown firing — is the acceptance test for any skill before its
first unattended run.
