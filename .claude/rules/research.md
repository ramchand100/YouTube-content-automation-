---
paths:
  - research/**
  - topics/**
---

# Research rules — applies to all files in research/ and topics/

## Workflow gate

A research brief or script may not begin until one angle has been explicitly approved
by the user. The approved angle must be recorded in `topics/angles/NN_slug_angle.md`
(one file per episode, using the blank form in `topics/ANGLE_TEMPLATE.md`) with
`approval_status: approved` and a date.

## Claim classification

Every claim in a research file must carry one of these labels:

| Label | Meaning |
|-------|---------|
| VERIFIED | Directly supported by a primary or highly reliable source |
| REPORTED | Credible journalism, not independently confirmed; attribute explicitly |
| ANALYSIS | Interpretation based on verified evidence |
| ESTIMATE | Calculation or inference; show the method |
| UNRESOLVED | Sources conflict or evidence is insufficient |

**Rules:**
- Never present ANALYSIS as fact.
- Never present ESTIMATE as a VERIFIED figure.
- Attribute all REPORTED claims explicitly: "According to [source]..."
- Tag all UNRESOLVED figures `[VERIFY]` or remove them before the brief is finalised.
- Never use a search-result snippet as final evidence. Open and read the source document.

## Source hierarchy (prefer in this order)

1. SBP, PBS, FBR, NEPRA, OGRA, Ministry of Finance, Ministry of Energy
2. Pakistan Economic Survey, company filings, audited financial statements, PSX disclosures
3. Court documents, regulatory orders, National Assembly / Senate committee reports
4. IMF, World Bank, IEA, ADB
5. Credible English-language Pakistan business journalism (Dawn Business, Business Recorder, Profit by Pakistan Today)
6. International financial journalism (FT, Reuters, Bloomberg) with Pakistan coverage

Never rely on social media, press releases alone, or unattributed estimates.

## Research file structure

Use this naming convention:

```
research/briefs/NN_slug_brief.md
research/timelines/NN_slug_timeline.md
research/claim-ledgers/NN_slug_claims.csv
research/source-registers/NN_slug_sources.csv
research/audits/NN_slug_research-audit.md
```

Where `NN` is the episode number and `slug` matches the script filename slug.

## Research brief must include

1. Approved angle (copy from `topics/angles/NN_slug_angle.md`)
2. Central question
3. Tentative thesis
4. Claims required (from angle sub-questions)
5. Raw findings (source URL, date accessed, verbatim quote or figure)
6. Verified figures (clean number + citation string ready for script)
7. `[VERIFY]` flagged items
8. Discarded sources (note why)
9. Counterarguments and how they are addressed
10. Stakeholder map

## Before the research brief is complete

- All required claims must be either VERIFIED, REPORTED (attributed), ANALYSIS (labelled),
  or ESTIMATE (method shown).
- No UNRESOLVED claim may remain in the brief without a `[VERIFY]` tag.
- The source register must list every source consulted (not just those cited).
