# Research Directory

This directory holds all pre-production research organised by episode.

**Rule: No script may begin until the research brief for the approved angle is complete.**

---

## Directory structure

```
research/
├── briefs/          # Full research briefs — one per episode
├── timelines/       # Source timelines for historical episodes
├── claim-ledgers/   # CSV claim-by-claim classification tables
├── source-registers/ # CSV source lists (also used for footage rights)
└── audits/          # Source audit files for finalised scripts
```

---

## Naming convention

Use the episode number and script slug throughout:

| File | Path |
|------|------|
| Research brief | `research/briefs/NN_slug_brief.md` |
| Timeline | `research/timelines/NN_slug_timeline.md` |
| Claim ledger | `research/claim-ledgers/NN_slug_claims.csv` |
| Source register | `research/source-registers/NN_slug_sources.csv` |
| Source audit | `research/audits/NN_slug_research-audit.md` |

Where `NN` matches the script file number and `slug` matches the script filename slug.

---

## Claim classification

Every claim in a research file, claim ledger, or script must carry one of these labels:

| Label | Meaning |
|-------|---------|
| **VERIFIED** | Directly supported by a primary or highly reliable source |
| **REPORTED** | Credible journalism, not independently confirmed; attribute the source explicitly |
| **ANALYSIS** | Interpretation drawn from verified evidence; label it clearly |
| **ESTIMATE** | Calculation or inference; show the method |
| **UNRESOLVED** | Sources conflict or evidence is insufficient; tag `[VERIFY]` |

**Rules:**
- Never present ANALYSIS as fact.
- Never present ESTIMATE as a VERIFIED figure.
- Attribute all REPORTED claims: "According to [source]..."
- Tag UNRESOLVED figures `[VERIFY]` or remove them before the brief is finalised.
- Never use a search-result snippet as final evidence. Open and read the source.

---

## Source hierarchy

Prefer sources in this order:

1. **Primary official sources:** SBP, PBS, FBR, NEPRA, OGRA, Ministry of Finance,
   Ministry of Energy, Pakistan Economic Survey, company filings, audited financials, PSX
2. **Court and regulatory documents:** National Assembly committee reports, court orders,
   SECP decisions
3. **Multilateral:** IMF, World Bank, IEA, ADB
4. **Tier-1 Pakistan business journalism:** Dawn Business, Business Recorder, Profit by
   Pakistan Today
5. **International financial journalism:** FT, Reuters, Bloomberg (Pakistan-specific)

Never rely on: social media, press releases alone, unattributed estimates, or search
snippets without reading the underlying source.

---

## Claim ledger format

File: `research/claim-ledgers/NN_slug_claims.csv`

```csv
claim_id,claim_text,classification,source_institution,url,data_period,verified,notes
C001,"[verbatim claim]",VERIFIED,"[institution]","[url]","[e.g. FY2023-24]",yes,""
```

---

## Source register format

File: `research/source-registers/NN_slug_sources.csv`

```csv
source_id,title,institution,pub_date,url,tier,notes
S001,"[full title]","[institution]","YYYY-MM-DD","[url]","Primary","[notes]"
```

The source register also doubles as the footage-rights log when extended with these columns:
`clip_id,description,timestamp,licence_type,licence_url,commercial_ok,cleared,fallback`

---

## Research approval process

Before a research brief is promoted to scripting:

1. All required claims are classified (no UNRESOLVED without `[VERIFY]`).
2. Claim ledger is complete — one row per major claim.
3. Source register lists every source consulted (not just those cited).
4. Counterarguments are documented and addressed.
5. The brief is reviewed and approved (record in `topics/ANGLE_TEMPLATE.md`).

---

## Conflicting data

When two or more sources give different figures:

1. Record both in the research brief with their sources.
2. Mark the claim UNRESOLVED.
3. Use the more conservative figure in the script, attributed explicitly.
4. Or note the conflict in the script: "Estimates range from X to Y [SOURCE / SOURCE]."
5. Flag with `[VERIFY]` for pre-recording re-check.

Never resolve a data conflict by picking the more dramatic figure.
