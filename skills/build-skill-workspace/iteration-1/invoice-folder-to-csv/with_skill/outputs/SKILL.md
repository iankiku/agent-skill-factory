---
name: invoice-folder-to-csv
description: >-
  Turn a folder of vendor-invoice PDFs into one reconciliation-ready CSV —
  vendor name, invoice number, amount due, due date per invoice — and flag
  every invoice missing a PO number into a separate manager-approval list
  instead of paying it. Use when the user asks to process/extract/pull data
  from a folder of invoices, says things like "go through these invoices and
  build a CSV for the bookkeeper", or wants a monthly vendor-invoices folder
  turned into a spreadsheet. Do NOT use this to pay invoices, post entries to
  accounting/ERP software, assign GL codes, or reconcile bank statements
  against a ledger (that is a different outcome — see a bank-reconciliation
  skill instead).
---

# Invoice folder to CSV

## Outcome

When the user points this skill at a folder of vendor-invoice PDFs (e.g.
`vendor-invoices/`, ~30 files dropped in monthly), read every PDF and produce
**one CSV** (`invoices.csv`) with one row per invoice — vendor, invoice
number, amount due, due date, PO number, and an approval flag — plus a
second, filtered **`flagged-for-approval.csv`** listing only the invoices
that have no PO number, so those can be routed to a manager before payment.
"Good" = every file in the folder is accounted for in the output (processed,
flagged, or explicitly marked unreadable — never silently skipped), every
row's amount and due date are real recomputed/parseable values rather than
guesses, and no invoice missing a PO number can reach the bookkeeper
unflagged.

**Scope edges — this skill does NOT:**
- Pay invoices, initiate transfers, or touch banking/payment tools.
- Write, post, or sync anything into QuickBooks, accounting software, or an
  ERP — output is local files only; a human hands them to the bookkeeper.
- Assign GL/expense codes or do tax categorization.
- Reconcile these invoices against bank statements or a ledger (different
  outcome — a bank/ledger reconciliation skill, not this one).
- Approve or reject flagged invoices itself — flagging routes to a human
  manager; the skill never grants its own approval.

## Assumptions

Built non-interactively (no live user available mid-build); each item below
was a real fork in the design and got the most reversible/safe default. Flag
any of these to the user on the first real run (see Setup, step 5) so they
can correct any that don't match reality.

- `ASSUMED: trigger is manual` — the user runs this by pointing at the
  folder each month ("process this month's invoices"), not on an unattended
  schedule. Nothing in the request implies automation infrastructure, and a
  money-adjacent workflow shouldn't start running unattended by default;
  scheduling can be added later (see Setup, step 4) once the output is
  trusted.
- `ASSUMED: "flag it separately" = a column AND a second file` — the request
  says both "put it all into one CSV" and "flag it separately." Resolved as:
  every invoice still gets one row in `invoices.csv` (nothing is ever left
  out of the master file), with a `needs_approval` column; a second,
  filtered `flagged-for-approval.csv` (same columns, subset of rows) exists
  purely so the no-PO invoices can be handed to a manager without anyone
  digging through 30 rows.
- `ASSUMED: amount_due = the invoice's own "Amount Due" / "Balance Due" /
  "Total Due" figure` (tax- and fee-inclusive), falling back to "Total" only
  when the invoice prints no separate due-amount line. Never "Subtotal."
- `ASSUMED: due_date = the printed due date`; if none is printed but an
  invoice date and payment terms are (e.g. "Net 30"), compute
  `due_date = invoice_date + terms`. If neither exists, leave the field
  blank and route the row to `_needs_review/` rather than guess a date the
  bookkeeper would post against.
- `ASSUMED: uncertain PO detection counts as "no PO"` — if the skill can't
  confidently confirm a PO number exists (as opposed to confidently seeing
  none), it still sets `needs_approval = TRUE`. Fail-safe toward manager
  review, never fail-open toward "assume it's fine."
- `ASSUMED: processed PDFs are archived, not deleted` — after a clean run,
  originals move into `processed/<YYYY-MM>/` inside the same folder so next
  month's drop starts clean and a re-run doesn't double-count old invoices.

## Required context

- **Amount-due precedence:** "Amount Due"/"Balance Due"/"Total Due" line >
  "Total" line > never "Subtotal" (pre-tax).
- **Due-date precedence:** printed due date > (invoice date + stated terms)
  > blank + flagged for review. Never invent a date with no textual basis.
- **PO-number rule:** a PO number is present only if an explicit PO/purchase
  order field or reference appears on the invoice with a value. A field
  present-but-blank, or no PO field/reference anywhere, both count as "no
  PO" → `needs_approval = TRUE`.
- **Currency/date formats:** `amount_due` as a plain decimal number (no
  currency symbol, no thousands separators) so the bookkeeper's tool can
  sum the column directly; `due_date` as ISO `YYYY-MM-DD`.
- Optional: a canonical vendor-name list, if the user has one, to normalize
  spelling variants of the same vendor (e.g. "Acme Inc." vs "Acme, Inc").
  Without it, the skill uses the vendor name exactly as printed on each
  invoice, which may leave the same real-world vendor under slightly
  different strings across invoices — call this out in the run summary
  rather than silently "fixing" vendor names by guesswork.

## Inputs

- One folder path per run (default: `vendor-invoices/`), containing PDF
  invoices (expected count: ~30/month, but the skill works at any count).
- Non-PDF files (images, `.docx`, stray receipts/statements) are read on a
  best-effort basis; anything that isn't an invoice (no vendor + amount +
  invoice-number pattern) is moved to `_not_invoices/`, not forced into the
  CSV.
- Missing folder / folder doesn't exist → stop immediately and report; never
  produce an empty CSV silently.
- Empty folder (nothing to process) → report "0 invoices found" explicitly;
  do not treat this as an error, but do not fabricate rows either.

## Tools, connectors, APIs & authentication

- **Filesystem read** — list the target folder, read each PDF's text/pages.
- **Filesystem write** — create `invoices.csv` and `flagged-for-approval.csv`
  in the folder; create and move files into `processed/<YYYY-MM>/`,
  `_not_invoices/`, `_unreadable/`, `_needs_review/` subfolders.
- No external connectors (no HubSpot, Slack, QuickBooks, email, etc.) — this
  is a local file task only, and none should be added. If a future version
  needs to push the CSV somewhere, that is a new decision point requiring
  explicit approval, not an assumption this skill makes on its own.
- No authentication of any kind is required. No API keys, tokens, or
  credentials are used, stored, or referenced anywhere in this skill.

## Permissions

- **Reads:** only inside the target invoice folder (and its subfolders).
- **Writes:** only inside the target invoice folder — the two output CSVs
  at its root, plus the `processed/`, `_not_invoices/`, `_unreadable/`, and
  `_needs_review/` subfolders it manages. Originals are always **moved**,
  never deleted or overwritten.
- **Never without explicit human approval:** paying or scheduling payment
  for any invoice; writing to accounting/ERP software; emailing or
  uploading the CSV anywhere; deleting any original PDF; approving a
  flagged (no-PO) invoice — that decision belongs to the manager the flag
  routes to, not to this skill.

## Workflow

1. **Inventory** — list every file in the target folder; count them (`N`).
   Nothing moves or is deleted until step 5 passes.
2. **Fan out per-file extraction** (delegated — see Delegation) — for each
   file, extract `{vendor, invoice_number, amount_due, due_date, po_number
   or null, po_status: found|missing|unreadable, confidence}`.
3. **Aggregate & recover** — the primary agent schema-checks every result;
   any file with `confidence < 0.8` or a missing required field gets one
   re-extraction attempt (full-page text, done inline by the primary); still
   unresolved → routed to `_needs_review/` but still gets a row in
   `invoices.csv` (blank fields, `status=needs_review`) so it's never
   silently dropped.
4. **Compute flags** — set `needs_approval = TRUE` wherever `po_status` is
   `missing` or `unreadable` (see Required context: PO-number rule). Run the
   duplicate check: any two rows sharing the same `vendor` + `invoice_number`
   are both marked `duplicate = TRUE`, never silently merged.
5. **Validate** — run every check in Validation below. Any check that fails
   twice in a row halts the run before anything is written or moved (see
   Failure modes).
6. **Produce deliverables** — write `invoices.csv` (every row, all columns)
   and `flagged-for-approval.csv` (rows where `needs_approval = TRUE`).
7. **Archive** — move successfully processed PDFs into
   `processed/<YYYY-MM>/`; leave `_needs_review/`, `_unreadable/`, and
   `_not_invoices/` contents in place until a human resolves them.
8. **Report** — summarize counts (total / flagged / needs-review /
   unreadable / not-invoices) and the paths to both CSVs.

## Decision points

- **PO number confidently absent vs. extraction genuinely uncertain** →
  both set `needs_approval = TRUE`; the `po_status` column distinguishes
  them (`missing` vs `unreadable`) so a human can tell "no PO" from "couldn't
  read this one" without re-opening the PDF.
- **Which figure is "amount due"** → precedence order in Required context;
  never the pre-tax subtotal.
- **Which date is "due date"** → printed due date, else invoice date +
  terms, else blank + `_needs_review/`. Never an invented date.
- **File isn't actually an invoice** (packing slip, statement, stray
  receipt) → `_not_invoices/`, noted in the summary, not forced into the CSV
  and not silently ignored.
- **Same vendor + invoice number appears twice** (possible duplicate
  submission) → both rows kept, both flagged `duplicate = TRUE`; the
  bookkeeper decides, the skill never auto-dedupes financial data.
- **Low-confidence extraction after one retry** → `_needs_review/`, row
  still present in `invoices.csv` with blank fields and
  `status=needs_review` — the zero-files-unaccounted invariant always wins
  over a clean-looking but wrong row.

## Validation

Run before anything is delivered or moved:

- **Mechanical — zero unaccounted:** `(rows in invoices.csv) == (files in
  folder) - (files in _not_invoices/)`. Recomputed by counting, not assumed.
- **Mechanical — flag consistency:** `(rows in flagged-for-approval.csv) ==
  (rows in invoices.csv where needs_approval == TRUE)`. Cross-file count
  check, not a re-derivation from memory.
- **Mechanical — field sanity:** every `amount_due` parses as a positive
  number; every `due_date` parses as a real calendar date in `YYYY-MM-DD`;
  any row that fails either check is routed to `_needs_review/` instead of
  shipped with a bad value.
- **No silent approvals:** every row where `po_status` is `missing` or
  `unreadable` has `needs_approval == TRUE` — recomputed as a rule, never
  asserted independently, so a code path can't accidentally let one through.
- **Duplicate surfacing:** no two rows share `vendor` + `invoice_number`
  without both being marked `duplicate = TRUE`.
- Any check failing twice on the same run → **stop, do not write or move
  anything, report exactly which check failed and on which files** (see
  Failure modes).

## Failure modes & fallbacks

- **PDF unreadable / corrupt / scanned image with no extractable text** →
  retry the read once; still fails → move to `_unreadable/`, row in
  `invoices.csv` with blank fields, `status=unreadable`,
  `needs_approval=TRUE` (fail-safe — never assume an unreadable invoice is
  fine to pay).
- **Vendor or invoice number can't be found at all** → same fallback as
  above (`_needs_review/`, blank fields, flagged) — never fabricate a
  plausible-looking value to fill the row.
- **Target folder missing or unreadable** → stop immediately, report the
  path, do not create an empty CSV.
- **More than ~20% of files land in `_needs_review/` + `_unreadable/`
  combined** → stop before producing final CSVs and report — this usually
  means extraction itself is broken (wrong folder, all-scanned-image
  batch, wrong file types), not that 1-in-5 invoices are individually bad.
- **A file was already processed in a prior run** (found already sitting in
  `processed/<YYYY-MM>/`) → skip re-processing it, note the skip in the
  summary — prevents double-counting when a folder still has old archived
  files alongside new drops.
- **Validation fails twice** on the same mechanical check → stop; write
  nothing; report the exact check and the specific file(s) involved.

## Delegation

Per the delegation policy this skill was built under (restated here so it
is self-contained):

| Step | Decision | Contract |
|---|---|---|
| Per-file field extraction (~30 independent PDFs) | **Delegate** (smaller/faster model, parallel fan-out) | **Context:** one file's text/pages + the fixed field list + the three precedence rules (amount-due, due-date, PO-number) from Required context. **Output:** fixed JSON `{file, vendor, invoice_number, amount_due, due_date, po_number\|null, po_status: found\|missing\|unreadable, confidence}`. **Validation:** primary schema-checks every returned object and re-extracts (once, inline) anything with `confidence < 0.8` or a missing required field. **Fallback:** on repeat failure, route to `_needs_review/` or `_unreadable/` per Failure modes — never guess a value to fill the schema. |
| Duplicate detection (vendor + invoice_number across the whole table) | **Primary** | Needs the full aggregated table — a cross-item comparison, not an independent per-file task. |
| Compute `needs_approval` flag | **Primary** | A one-line rule, but it's the crux of "don't silently pay an unapproved invoice" — kept with the primary rather than trusted to a sub-agent's summary. |
| Validation checks | **Primary** | The checks exist specifically so the primary catches its own sub-agents' mistakes; delegating validation would defeat the point. |
| Writing CSVs + moving/archiving files | **Primary, always** | The only mutating/sensitive actions in this skill — batched strictly after validation passes, so a failed run costs nothing. |

Parallelization is limited to the per-file extraction fan-out (independent
files, no shared state). The primary merges, validates, and only then acts
on the results — nothing downstream of the fan-out runs until validation
passes.

## Setup

1. Point the skill at the invoice folder (default `vendor-invoices/`);
   grant the executing environment read/write access to it (Claude Code
   project access, or a Cowork folder connection — no external connector
   needed).
2. Nothing to authenticate — no API keys, tokens, or connectors to enable.
3. Optional: hand the skill a canonical vendor-name list if you want vendor
   names normalized across invoices; otherwise it uses each invoice's
   printed name as-is.
4. Optional, once trusted: schedule a monthly run (e.g. via a scheduling
   skill) instead of triggering it by hand each month — not enabled by
   default (see Assumptions).
5. First real run: review the `Assumptions` section above with the user —
   especially the amount-due/due-date precedence rules and the "uncertain
   PO = flagged" default — and correct any `ASSUMED:` line that doesn't
   match how this business actually wants it done. Also review
   `flagged-for-approval.csv` and anything in `_needs_review/` before
   calling a month's run "done."
