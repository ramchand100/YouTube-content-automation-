# /angles

Generate scored angle options for a broad topic. Recommend one. Stop for approval.

## Before running

1. Read `CLAUDE.md`.
2. Read `.claude/rules/research.md`.
3. Confirm no approved angle already exists for this topic in `topics/angles/`.

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

## Check for a comprehensive-combination opportunity

Before writing the recommendation, look across the full set of scored angles.
If several of them are really different layers or facets of the same
underlying mechanism, not genuinely separate stories, say so explicitly and
ask the user whether they want the narrowest strong angle or a widened,
comprehensive version that combines the related layers into one episode.
Propose what the widened central question, thesis, and part structure would
look like so the choice is concrete, not abstract.

Settle this before the user approves an angle, not after research or
scripting has begun. Widening the scope later means retrofitting new
material onto research or a script built for a narrower angle, which is
exactly how inconsistencies creep in: figures that don't quite match because
they came from two separate research passes, terms used in a later part
that were never defined earlier, reused numbers with different rounding.
Locking the final scope before `/research` starts avoids all of it.

Do not default to recommending the comprehensive version, and do not raise
this check reflexively on every topic. Most topics are correctly scoped
narrow — CLAUDE.md's storytelling rules want one tested mechanism per
episode, not a survey, and a documentary script is "a controlled sequence of
discoveries," not a research summary. Only raise the comprehensive option
when the scored angles genuinely read as facets of one system rather than
distinct stories that happen to share a topic.

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

Once approved, save the angle details to `topics/angles/NN_slug_angle.md` (fill out
the blank form in `topics/ANGLE_TEMPLATE.md` and save the completed copy under the
episode's own number and slug) with `approval_status: approved` and today's date,
then proceed to `/research`.
