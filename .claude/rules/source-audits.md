---
paths:
  - research/audits/**
  - research/source-registers/**
---

# Source-audit rules — applies to research/audits/ and research/source-registers/

## Purpose

A source audit is created for every final script before it is marked
`status: production-ready`. It documents the exact source behind every major claim.

## Source audit file format

File: `research/audits/NN_slug_research-audit.md`

For each major claim, record:

| Field | Description |
|-------|-------------|
| Claim ID | Sequential ID: C001, C002, etc. |
| Exact script claim | The verbatim sentence or phrase from the script |
| Claim classification | VERIFIED / REPORTED / ANALYSIS / ESTIMATE / UNRESOLVED |
| Source institution | Who published it |
| Exact source title | Full title of the document, article, or report |
| Publication date | ISO date: YYYY-MM-DD |
| Data period | The time period the data covers (e.g. "FY2023–24") |
| URL | Direct URL to the source (not a search page) |
| Source tier | Primary / Tier-1 journalism / Secondary |
| Supports exact wording | Yes / Partially / No |
| Verification status | Confirmed / Needs verification / Conflicting / Removed |
| Notes | Any caveats, conflicting data, stale figures |

## Verification statuses

- **Confirmed** — the source directly supports the exact claim as written.
- **Needs verification** — source exists but data period is stale, URL is dead,
  or wording differs from what the source says.
- **Conflicting** — two or more sources give different figures; the script must note
  the conflict or use the more conservative figure with attribution.
- **Removed** — claim removed from the script because it could not be verified.

## Primary source preference

Prefer primary sources:
SBP · PBS · FBR · NEPRA · OGRA · Ministry of Finance · Ministry of Energy ·
Pakistan Economic Survey · company filings · PSX disclosures · audited accounts ·
court documents · IMF · World Bank · IEA

## What the audit does not do

The source audit is a structural and provenance check. It confirms that a source
exists and that the claim is traceable. It does not independently verify the
accuracy of the source's underlying data. That remains the scriptwriter's
responsibility when selecting sources.

## Audit gate

No script may be marked `status: production-ready` without a completed source audit
where every claim is either Confirmed or Removed.
