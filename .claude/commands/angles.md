# /angles

Generate scored angle options for a broad topic. Recommend one. Stop for approval.

## Before running

1. Read `CLAUDE.md`.
2. Read `.claude/rules/research.md`.
3. Confirm no approved angle already exists for this topic in `topics/`.

## What to do

The user has provided a broad topic. Generate 6 to 10 distinct angles.

**Each angle must include:**
- Angle name (short, descriptive)
- One-sentence framing
- Central question
- Tentative thesis
- Main entities and institutions involved
- Evidence required to support or refute the thesis
- Pakistani economic relevance (why this matters to Pakistani viewers specifically)
- Audience consequence (what a founder, executive, student, or investor should do differently after watching)
- What the angle deliberately excludes (scope boundary)
- Main weakness or research risk

**Use distinct lenses where relevant** (do not force irrelevant ones):
Money and unit economics · Hidden subsidy or cost transfer · Policy versus ground reality ·
Incentive conflict · Winners and losers · Supply-chain bottleneck · Regulatory friction ·
Tax and compliance burden · Informal versus documented economy · Corporate strategy ·
Market power · Consumer impact · Historical transformation · Failed promise ·
Unintended consequence · Future transition · Foreign-exchange exposure · Regional competitiveness

**No overlapping angles.** Before finalizing the list, check every pair of draft angles
against each other. If two or more angles would answer the same central question, rely on
the same core evidence, or one is really just a supporting mechanic of another (e.g. "why
the deal succeeded" and "how the debt was restructured" when the restructuring *is* the
reason it succeeded), merge them into a single angle rather than listing them as separate
rows. A merged angle keeps the strongest framing, folds the others in as supporting
mechanics or as the opening hook, and gets one row in the table and one line in scoring —
never present near-duplicates side by side and note the overlap only in prose. The 6–10
angle count applies to the post-merge, de-duplicated list.

## Scoring

Score every angle 1–5 on each dimension:

| Dimension | Weight |
|-----------|--------|
| Evidence strength | 30% |
| Distinctiveness | 20% |
| Pakistani relevance | 20% |
| Audience consequence | 15% |
| Narrative potential | 10% |
| Timeliness | 5% |

Compute the weighted score for each angle.

## Output format

Use this exact format:

```
# Angle Options: [Topic]

## Broad topic
[One sentence describing the topic.]

## Central decision
[Explain what editorial decision is being made — what angle framing will determine.]

| # | Angle | Central question | Tentative thesis | Evidence needed | Excludes | Risk |
|---|-------|-----------------|-----------------|-----------------|---------|------|
| 1 | ... | ... | ... | ... | ... | ... |

## Weighted scoring

| # | Evidence | Distinctiveness | Pakistan relevance | Audience consequence | Narrative potential | Timeliness | Weighted score |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | ... | ... | ... | ... | ... | ... | ... |

## Recommendation

- Recommended angle: [number and name]
- Why it is strongest: [one paragraph]
- Central question: [one sentence]
- Thesis to test: [one sentence]
- Story logic: [one of: Causal | Chronological | Financial | Institutional | Comparative | Operational | Regulatory | Company case study | Decision-focused | Structural/historical | combination]
- Rationale for logic: [one sentence — why does this story type fit this angle?]
- Proposed part count: [N] — [one sentence justifying the count from the story logic, not from a default]
- Proposed structure:
  - Part 1: [Name] — [Opening function: concrete anomaly or consequence that creates the central question]
  - Part 2: [Name] — [focus]
  [add or remove parts as the logic requires — do not default to five]
  - Part N: [Name] — [Closing function: defensible finding, what would need to change, who this matters to]
- Research gaps: [what must be confirmed before scripting]
- Main counterargument: [strongest objection to the thesis]
- Deliberate exclusions: [what this angle does not cover and why]
```

End every angles output with this exact line:

> Waiting for angle approval. No research or script has been started.

## After this command

Do not begin research or scripting until the user explicitly approves an angle
(either by number, name, or by saying "approved" or "go with [angle]").

Once approved, save the angle details to `topics/ANGLE_TEMPLATE.md` with
`approval_status: approved` and today's date, then proceed to `/research`.
