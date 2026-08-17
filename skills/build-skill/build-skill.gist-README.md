# build-skill — install in 60 seconds

**A skill is how you ship a workflow.** Not a prompt you retype — a file that names its
inputs, runs its steps, checks its own output, and knows when to stop and ask you.

`build-skill` is the skill that writes those skills. Tell it what outcome you want to
make repeatable; it interviews you, picks the closest of 94 Anthropic-published
templates, and hands back a finished `SKILL.md`.

**This gist has two files:**

| File | What it's for |
|---|---|
| `0-README.md` | You're reading it — install steps and the first prompt to run |
| `build-skill.gist.md` | **The skill.** Copy this one file and save it as `SKILL.md` |

---

## 1 · Install

Open **`build-skill.gist.md`** below, click **Raw**, select all, copy. Then save it as
`SKILL.md` inside a folder named `build-skill`:

| Surface | Where it goes |
|---|---|
| **Claude Code** | `~/.claude/skills/build-skill/SKILL.md` (all projects) or `.claude/skills/build-skill/SKILL.md` (one project) |
| **Claude.ai / Claude Desktop** | Settings → Capabilities → Skills → upload the file (or a `.zip` containing it as `SKILL.md`) |
| **Cowork** | Same as Claude Desktop — upload via the Skills settings panel |

No `git`, no GitHub account, no terminal — just a file save. Everything the skill needs
(all four reference files) is inlined in that one file.

**Have Node.js?** Skip all of the above:

```bash
npx skills add iankiku/agent-skill-factory --skill build-skill
```

That pulls the full repo version — complete 94-entry template index plus two worked
example transcripts — instead of this trimmed single-file bundle.

## 2 · Run it

Paste this into Claude, filling in the brackets:

```text
Build me a Claude skill for [MY INDUSTRY].

The workflow I want to make repeatable: [DESCRIBE IT IN ONE OR TWO SENTENCES]

My context — industry: [MY INDUSTRY] · role: [MY ROLE] · tools I use: [MY TOOLS]
Inputs a run consumes: [FILES / FOLDERS / CONNECTORS / MESSAGES]
What exists afterward that didn't before: [THE ARTIFACT]
What separates a good run from a technically-complete one: [THE BAR]
```

## What it does with that

1. **Pins the outcome** — "when *trigger*, produce *artifact* from *inputs*, meeting *bar*."
2. **Picks a template** — closest of 94, by artifact type → inputs → domain; blank one if nothing fits.
3. **Specifies the machinery** — tools, connectors, auth, permissions, workflow steps, decision points.
4. **Adds the guardrails** — validation criteria, failure modes, and a delegation plan.
5. **Dry-runs it on paper** before you trust it, then refines with you.

Two things it will never do: put a secret in a skill (connector and env-var *names*
only), or stall on a question — after three tries it picks a labeled default and keeps
going.

## The other 94

This gist is one skill. The full repo turns **all 94 use cases Anthropic publishes** into
ready templates, each with a copy-paste prompt that builds it for your industry —
marketing, sales, finance, legal, HR, education, research, nonprofits, life sciences, and more.

**→ https://github.com/iankiku/agent-skill-factory**

Not an official Anthropic project. Seed prompts are © Anthropic PBC; the scaffolding is MIT.
