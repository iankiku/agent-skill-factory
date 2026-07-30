# Run notes — invoice-folder-to-csv

Process followed: `build-skill/SKILL.md` (agent-skill-factory), phases 1–5.
This was a **non-interactive** build: no live human was available to answer
the interview questions the skill normally asks via `AskUserQuestion`, so I
answered them myself, in character as the user in the prompt (a small-business
owner/engineer who currently opens ~30 vendor-invoice PDFs by hand every
month). Every place I did this is called out below and mirrored as an
`ASSUMED:` line in the delivered `SKILL.md` so a real user can correct it on
first use, per the skill's own "I don't know" protocol.

## Template selection (Phase 2)

Read `references/template-index.md`, then the full bodies of the two closest
candidates in `templates/`:

- `templates/personal/organize-files-by-whats-in-them/SKILL.md` — closest on
  **inputs** (a local folder of mixed files, no connector, Cowork-style
  folder grant) but wrong on **artifact** (it reorganizes files into folders;
  this task wants one CSV, files stay in place except for archiving).
- `templates/finance/reconcile-transactions-across-your-accounts/SKILL.md` —
  closest on **domain** (accounts-payable style reconciliation feeding a
  bookkeeper) and its validation language ("figures reconcile to source...
  flag, never silently correct discrepancies") but wrong on **inputs**
  (expects bank export + ledger file uploads, not a folder of invoice PDFs)
  and **artifact** (an annotated reconciliation report, not a row-per-invoice
  CSV).

Neither matches on artifact type (a CSV of extracted per-invoice fields), so
per Phase 2's rule ("if nothing matches on artifact OR inputs... build from
`blank-skill-template.md`"), I built from **`references/blank-skill-template.md`**
and pulled two things in from the catalog rather than forcing either template
wholesale:
- the *input-handling shape* (local folder, no connectors, reversible moves)
  from `organize-files-by-whats-in-them`;
- the *validation rigor* ("recompute, don't assume; flag, don't silently
  fix") from `reconcile-transactions-across-your-accounts`.

I also leaned on `build-skill/examples/example-2-invoice-folder-triage.md` —
a worked example bundled with `build-skill` itself for a near-identical task
(a folder of supplier invoices, per-file extraction, a 20%-review-rate
circuit breaker, a "zero files unaccounted for" mechanical invariant). It
isn't a catalog template and I didn't copy its final skill verbatim (its
artifact is a renamed/foldered file tree + `index.xlsx`; this task's artifact
is one `invoices.csv` — no renaming, no supplier foldering), but its
structure, the file-fan-out delegation call, and the "zero unaccounted"
validation pattern carried over directly.

## Phase 1 — pinning the outcome (self-answered)

The interview questions below were answered by me, in character, because no
human was present. Each maps to an `ASSUMED:` line in the shipped `SKILL.md`.

1. **Trigger** — manual, user points the skill at the folder each month
   ("process this month's invoices"), not an unattended schedule. Nothing in
   the request implies scheduling infrastructure, and I didn't want to
   default a money-adjacent workflow into running unattended.
2. **"Flag it separately" vs. "put it all into one CSV"** — these two asks
   look like they conflict. Resolved as: one CSV always gets every row (the
   literal "put it all into one CSV"), with a `needs_approval` column, PLUS
   a second filtered file (`flagged-for-approval.csv`) so the no-PO subset
   is routable to a manager without hunting through every row. This is the
   single biggest interpretive call in the build; it's called out first in
   Assumptions and flagged for correction at Setup step 5.
3. **What "amount due" means precisely** — the invoice's own "Amount
   Due"/"Balance Due"/"Total Due" line (tax-inclusive), never the pre-tax
   subtotal, falling back to "Total" only if no separate due-figure exists.
4. **What "due date" means precisely** — the printed due date; if absent,
   invoice date + stated payment terms; if neither exists, blank + flagged
   for review rather than an invented date.
5. **Folder lifecycle across months** — assumed the folder is a rolling drop
   (new invoices added monthly) rather than replaced wholesale, so processed
   PDFs get archived into `processed/<YYYY-MM>/` after a clean run — this
   prevents a re-run (or next month's run, if old files are still sitting
   there) from double-counting the same invoice.
6. **Uncertain PO detection** — treated the same as "confirmed no PO" for
   the approval flag (fail-safe toward manager review), but recorded
   separately in a `po_status` column (`missing` vs. `unreadable`) so a human
   can tell the two apart without reopening the PDF.

Scope edge established: this skill produces files for a human to hand to the
bookkeeper — it never pays invoices, writes to accounting/ERP software,
assigns GL codes, or reconciles against bank statements (that's a different
outcome, explicitly out of scope in the frontmatter's negative scope).

## Phase 3 — machinery

- **Tools/auth:** filesystem read + write only, entirely local to the target
  folder. No connectors, no API keys, no credentials anywhere — deliberately
  resisted the temptation to wire in anything (e.g. email-to-bookkeeper,
  QuickBooks push) that wasn't asked for; those would each be new sensitive
  actions requiring explicit approval, not defaults a skill should assume.
- **Validation:** five checks, all mechanical/recomputed rather than
  vibes-based — row-count-vs-file-count ("zero unaccounted"), CSV-to-CSV
  flag-count cross-check, amount/date parse checks, a flag-consistency rule
  (`needs_approval` recomputed from `po_status`, never asserted
  independently), and a duplicate-surfacing rule. Two failures on the same
  check halts the run before any file is written or moved.
- **Failure modes:** unreadable/scanned PDFs, unfindable required fields,
  missing target folder, a 20%-review-rate circuit breaker (borrowed from
  the bundled example-2 pattern — a high review rate usually means
  extraction itself is broken, not that many invoices are individually
  bad), and an idempotency guard against re-processing already-archived
  files.

## Phase 4 — delegation plan

Applied `references/delegation-policy.md`. Per-file extraction across ~30
independent PDFs is exactly the canonical per-item fan-out case (no shared
state, closed context per file, closed output schema) — delegated to a
smaller/faster model. Everything else stays with the primary: duplicate
detection needs the whole aggregated table (cross-item, not independent);
computing the `needs_approval` flag and running validation exist specifically
to catch a delegated sub-agent's mistakes, so delegating them would defeat
the point; writing the CSVs and moving/archiving files are the only mutating
actions in the skill and are batched strictly after validation passes.

## Phase 5 — dry-run trace (paper walkthrough, ~30 files)

Input: 30 files (27 PDFs, 2 JPG scans, 1 stray packing slip).

1. Inventory: N = 30.
2. Fan out 30 extraction tasks → 26 clean, 2 low-confidence (re-extracted
   inline: 1 recovers, 1 stays low-confidence → `_needs_review/`), 1 PO field
   genuinely blank → `po_status=missing`, 1 file is the packing slip (no
   invoice-number/amount pattern) → routed to `_not_invoices/` at
   classification, not counted as an invoice.
3. Aggregate: 28 invoices extracted cleanly or recovered on retry (26 clean
   + 1 recovered + 1 low-confidence → `_needs_review/` but still counted),
   plus 1 unreadable-after-retry scan (blank-field placeholder row, per the
   "never silently drop" rule) = 29 rows destined for `invoices.csv`. The
   packing slip is the only file with no CSV row (it goes to
   `_not_invoices/` instead). 29 + 1 = 30 files accounted for.
4. Compute flags: 4 rows have `po_status` in {missing, unreadable} →
   `needs_approval=TRUE` (the 1 confirmed-missing PO, plus the 1
   unreadable-scan placeholder and 1 needs_review row, fail-safe; a 4th
   ordinary invoice also happens to have no PO printed). Duplicate check:
   one vendor appears twice with different invoice numbers → correctly NOT
   flagged as duplicate (different invoice numbers = different invoices).
5. Validate: rows-in-CSV (29) == files (30) − not_invoices (1) ✓.
   Flagged-file count (4) == `flagged-for-approval.csv` row count (4) ✓.
   All amounts numeric > 0 ✓ (except placeholder rows, which are excluded
   from the numeric check and routed for review instead). All due dates
   parse ✓ (same placeholder exclusion).
6. Deliverables written: `invoices.csv` (29 rows), `flagged-for-approval.csv`
   (4 rows).
7. Archive: 28 clean/recovered PDFs → `processed/2026-07/`; the 1 unreadable
   scan stays in `_unreadable/`; the 1 packing slip stays in
   `_not_invoices/` — neither is archived as "done" until a human resolves
   it.
8. Report: "30 files in → 29 invoices logged (4 flagged for manager
   approval, 1 needs manual review), 1 non-invoice set aside. Nothing
   unaccounted for."

This trace is why the shipped `SKILL.md` treats "unreadable" the same as any
other invoice for the zero-unaccounted invariant (a blank flagged row, not an
omission) while still keeping it out of the auto-archive step.

## Checklist self-check

Ran `references/validation-checklist.md` against the final draft: triggering
(description + negative scope + kebab-case name), outcome/inputs (all four
slots, every input has a missing/malformed path), tools/auth (no connectors,
no credential values), safety (specific sensitive-action list, nothing
irreversible before validation, no bypass instructions), workflow (8 steps,
every decision point has a rule, mechanical validation present, stop-and-report
conditions present), delegation (present, all four contract fields on the one
delegated task, only independent work parallelized, primary keeps final review
and every sensitive action), and hygiene (Assumptions section complete, Setup
section provisionable standalone, dry-run trace produced above). No verbatim
template content was reused, so no attribution block was added — only the
*shape* of two catalog templates and the bundled invoice-triage example
informed the structure, per the notes above.

## What I did not build

Per the "one outcome per skill" ground rule, I did not fold in: renaming or
foldering the PDFs by supplier (that's the bundled example-2's outcome, a
different artifact), automatic scheduling (flagged as a Setup follow-up, not
a default), or vendor-name normalization beyond an optional canonical list
(flagged as optional Required-context input, not built as automatic fuzzy
matching, since guessing at vendor identity is exactly the kind of silent
"fix" the validation rules are designed to avoid).
