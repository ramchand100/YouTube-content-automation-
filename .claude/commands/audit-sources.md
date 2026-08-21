# /audit-sources

Verify the exact source behind every major claim in a final script. Create the source audit file.

## Before running

1. Read `CLAUDE.md`.
2. Read `.claude/rules/source-audits.md`.
3. Identify the script file to audit (user must specify path or episode number).
4. Confirm the script has passed `/review-script` with no BLOCK items.

## What to do

### Step 1 — Extract all major claims

A "major claim" is any:
- Specific number, percentage, or financial figure
- Named statistic attributed to an organisation
- Characterisation of a company's market position, financial health, or performance
- Statement about a regulatory action, policy, or legal finding
- Historical fact presented as established

Assign each claim a sequential ID: C001, C002, etc.

### Step 2 — Locate and inspect each source

For every claim, find the source cited in the `[SOURCE: ...]` tag.
- Open and read the actual source document or article — not a search snippet.
- Confirm the source says what the script claims it says.
- Confirm the data period the source covers.
- Note if the source's wording differs from the script's wording.

### Step 3 — Create the audit file

Save to: `research/audits/NN_slug_research-audit.md`

For each claim, record:

| Field | Value |
|-------|-------|
| Claim ID | C001 |
| Exact script claim | verbatim quote from script |
| Classification | VERIFIED / REPORTED / ANALYSIS / ESTIMATE / UNRESOLVED |
| Source institution | who published it |
| Exact source title | full title |
| Publication date | YYYY-MM-DD |
| Data period | time period the data covers |
| URL | direct URL (not a search page) |
| Source tier | Primary / Tier-1 journalism / Secondary |
| Supports exact wording | Yes / Partially / No |
| Verification status | Confirmed / Needs verification / Conflicting / Removed |
| Notes | caveats, stale figures, conflicting data |

### Step 4 — Report summary

Report:
- Total claims audited
- Confirmed: N
- Needs verification: N (list them)
- Conflicting: N (list them and explain the conflict)
- Removed: N (list what was removed from the script)

### Verification status rules

- **Confirmed** — source directly supports the exact claim as written.
- **Needs verification** — source exists but URL is dead, data period is stale,
  or wording differs materially.
- **Conflicting** — two or more sources give different figures. Script must
  acknowledge the conflict or use the more conservative figure.
- **Removed** — claim removed because it could not be confirmed.

## Source preference

Primary sources first: SBP · PBS · FBR · NEPRA · OGRA · Ministry of Finance ·
Pakistan Economic Survey · company filings · PSX disclosures · IMF · World Bank

## Audit gate

The script cannot be marked `status: production-ready` until:
- Every claim is Confirmed or Removed.
- No "Needs verification" or "Conflicting" items remain unresolved.

## Important limitation

This audit verifies that a source exists and that the claim is traceable to it.
It does not independently verify the accuracy of the source's underlying data.
Factual accuracy remains the scriptwriter's responsibility in source selection.
