# /research

Create the research brief, claim ledger, and source register for an approved angle.
Do not write the script.

## Before running

1. Read `CLAUDE.md`.
2. Read `.claude/rules/research.md`.
3. Confirm an approved angle exists in `topics/ANGLE_TEMPLATE.md` with
   `approval_status: approved`.
4. If no approved angle exists, redirect to `/angles` first.

## What to do

Work only from the approved angle. Do not reopen the angle decision.

**Create these files** (use the episode number NN and slug from the approved angle):

### 1. Research brief — `research/briefs/NN_slug_brief.md`

Structure:
- Approved angle (copy from ANGLE_TEMPLATE)
- Central question
- Tentative thesis
- Claims required (from the angle's sub-questions)
- Raw findings (source URL + date accessed + verbatim quote or figure)
- Verified figures (clean number + citation string ready for script)
- `[VERIFY]` flagged items
- Discarded sources (note why discarded)
- Counterarguments and how they are addressed
- Stakeholder map (owners, regulators, capital providers, customers, losers)

### 2. Claim ledger — `research/claim-ledgers/NN_slug_claims.csv`

Headers: `claim_id,claim_text,classification,source,url,verified`

Populate one row per major factual claim. Apply claim classification:
VERIFIED / REPORTED / ANALYSIS / ESTIMATE / UNRESOLVED

### 3. Source register — `research/source-registers/NN_slug_sources.csv`

Headers: `source_id,title,institution,date,url,tier,notes`

One row per source consulted (not just cited). Record tier:
Primary / Tier-1 journalism / Secondary

## Research rules

- Search for live figures before writing. Do not rely on training-data memory for
  statistics that change (inflation, interest rates, FX, company financials).
- Open and read the actual source document — not a search-result snippet.
- Use the source hierarchy from `.claude/rules/research.md`.
- Tag any figure that could not be confirmed `[VERIFY]`.
- Do not include UNRESOLVED claims without a `[VERIFY]` tag and a note.

## Nonfiction constraint

Do not invent scenes, examples, or illustrative characters to make the research
feel more concrete. Record only what is documented.

## After this command

Report:
- Research brief path
- Claim ledger path
- Source register path
- Count of VERIFIED claims
- Count of REPORTED claims
- Count of ESTIMATE claims
- Count of UNRESOLVED / `[VERIFY]` items that need resolution before scripting

Do not begin the script. Wait for the user to review the research brief and
confirm readiness to proceed.
