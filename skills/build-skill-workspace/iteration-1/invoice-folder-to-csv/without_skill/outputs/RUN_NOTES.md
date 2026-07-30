# Run notes — vendor-invoices → CSV

## What this is
A single script, `extract_invoices.py`, that replaces the "open each PDF by
hand" workflow. Point it at a folder of vendor-invoice PDFs and it writes:

- `invoices.csv` — one row per invoice: vendor name, invoice number, amount
  due, due date, PO number, plus a `needs_manager_approval` flag and a
  `confidence`/`notes` column.
- `invoices_needs_approval.csv` — just the subset with no PO number found,
  ready to hand straight to a manager (this directly answers the "flag
  separately" part of the ask, without forcing the bookkeeper to filter the
  main sheet themselves).

Usage:
```
python3 extract_invoices.py /path/to/vendor-invoices -o invoices_2026-07.csv
```
If no folder argument is given it defaults to `./vendor-invoices` (matching
the name in the request), and if no `-o` is given it writes `invoices.csv`.

## Why a script instead of manually reading 30 PDFs each time
This is a monthly, ~30-file, mechanical task with a fixed shape (same five
fields, every time). That's a script problem, not a one-off Q&A problem —
running it takes seconds and it's fully repeatable next month. I did not
build this as an installable Claude "skill" (no `SKILL.md`/frontmatter) since
that wasn't asked for here; it's a standalone Python file the user can run
directly, or later wrap into a skill if they want Claude to run it for them
automatically each month.

## How extraction works
1. **PDF → text**: tries `PyMuPDF` (fitz), then `pypdf`, then `pdfplumber`,
   whichever is already installed; falls back to the `pdftotext` CLI
   (poppler) if none of those Python libraries are present. If literally
   none of the above exist on the machine, it prints exactly what to
   `pip install` rather than failing silently.
2. **Field parsing** is regex/heuristic, not a trained model:
   - *Invoice number / amount due / due date / PO number*: looks for the
     common label variants ("Invoice #", "Invoice No.", "Amount Due",
     "Balance Due", "Total Due", "Due Date", "PO Number", "P.O. #", etc.)
     and captures the value that follows.
   - *Vendor name*: first tries explicit labels ("Vendor:", "Remit To:",
     "Bill From:", "From:", "Sold By:"); if none exist, falls back to the
     first non-trivial line of the PDF (usually the letterhead), and as a
     last resort derives a guess from the filename. Anything but the
     labeled match is marked "low confidence."
   - *Due date* is normalized to `YYYY-MM-DD` regardless of whether the
     source used `7/31/2026`, `2026-07-31`, or `July 31, 2026`.
3. **PO-number flag**: if no PO number is found on the invoice, that row's
   `needs_manager_approval` is set to `TRUE` and it's duplicated into
   `invoices_needs_approval.csv`.
4. Every row also carries `confidence` (`high` / `low` / `none`) and
   `notes` explaining exactly what wasn't found, so nothing is silently
   wrong — the bookkeeper (or the user) can sort by `confidence` and only
   eyeball the handful of rows that need it, rather than re-checking all 30.

## Testing performed
There was no real `vendor-invoices` folder available in this environment
(non-interactive eval, no such folder on disk), so I could not run this
against the user's actual invoices. To validate the script actually works
rather than just reads plausibly, I generated four synthetic test PDFs
covering different real-world layout variations and ran the script against
them end-to-end:

| Test case | What it covers | Result |
|---|---|---|
| `acme_supplies_001.pdf` | Standard labeled layout, PO present, MM/DD/YYYY date | All 5 fields extracted correctly |
| `bluewave_hosting_0099.pdf` | Different label wording ("Invoice #", "Total Due", "Payment Due Date"), **no PO number** | Extracted correctly; correctly flagged `needs_manager_approval = TRUE` |
| `crestline_logistics_77.pdf` | "Remit To:"-style vendor line with trailing address, "Balance Due" wording, spelled-out month date ("5 August 2026") | All 5 fields correct; vendor name correctly trimmed to just the company (not the trailing address) |
| `weird_layout_vendor.pdf` | Sparse invoice missing invoice #, due date, and PO number | Correctly extracted what exists (vendor via fallback, amount), correctly flagged missing fields in `notes` and `needs_manager_approval = TRUE` |
| `blank_scanned.pdf` (added after initial pass) | Image-only/no-text-layer PDF (simulates a scanned invoice) | Did not crash; row flagged `NO TEXT EXTRACTED... enter manually`, confidence `low` |

All five ran cleanly through the actual `extract_invoices.py` (not a
simulation of it) using the system's installed PyMuPDF as the text backend.
Test PDFs and outputs were generated/run in a scratch directory, not
committed here — only the script itself is a deliverable.

## Assumptions made (no user available to ask)
- **Field definitions**: "amount due" = the final payable amount (prefers
  "Amount Due"/"Balance Due"/"Total Due" over a plain "Total", which is
  often subtotal-before-tax). If a vendor's invoice only ever says "Total,"
  that's what gets captured — worth a first-month spot check.
- **One currency**: no currency conversion or multi-currency handling. If
  vendors bill in different currencies, the raw amount is captured as-is
  with no currency column — flag this back to me if that's the case and
  I'll add a `currency` column.
- **No OCR**: scanned/image-only PDFs (no embedded text layer) are flagged
  for manual entry rather than silently guessed at. Adding OCR
  (`pytesseract` + `pdf2image`) is straightforward if this turns out to be
  common — I didn't add it preemptively since it's an extra system
  dependency (needs the Tesseract binary installed) that may not be wanted.
- **"Flag separately"** was interpreted as: keep everything in one CSV (as
  asked) but add a boolean column *and* emit a second, filtered CSV of just
  the flagged rows — covers both "sortable in the master sheet" and
  "something I can immediately hand to a manager" without picking one only.
- **Dependencies**: the script has no hard-required third-party dependency;
  it looks for whatever PDF library is already on the machine and tells the
  user exactly what to `pip install` if none is found, per this repo's
  preference for matching existing tooling rather than introducing new
  requirements files for a single script.
- Not built as a formal Claude Code "skill" package — this task didn't ask
  for one, and a plain script is simpler for a user who just wants to run
  it monthly. If recurring/automated use (e.g., "do this every time I say
  '/invoices'") is wanted, wrapping it as a skill would be a small follow-up.

## What the user should do
1. Make sure a PDF-reading library is available: `pip3 install pymupdf`
   (fastest, recommended) — or nothing at all if `pdftotext` (poppler) is
   already installed (`brew install poppler` on macOS if not).
2. Run: `python3 extract_invoices.py /path/to/vendor-invoices -o invoices.csv`
3. Open `invoices.csv`, sort/filter by the `confidence` column, and
   spot-check any `low`/`none` rows before sending to the bookkeeper.
4. Send `invoices_needs_approval.csv` to whoever needs to approve invoices
   lacking a PO number.
