---
paths:
  - scripts/**
---

# Script rules — applies to all files in scripts/

These rules supplement CLAUDE.md section 7. Read CLAUDE.md first.

## What scripts contain

Scripts are pure voiceover narration. No exceptions.

**Never include inside a script file:**
- `[VISUAL ...]` annotations
- `[FOOTAGE ...]` or `[B-ROLL ...]` cues
- Camera directions
- Editing instructions
- Music or sound effect notes
- On-screen text specs
- Thumbnail ideas
- Production notes (except the standard Sources block)

All visual and production direction belongs in the matching storyboard file:
`storyboards/NN_<slug>_visuals.md`.

## Required front-matter

Every script must open with this front-matter block (after the title):

```
- **Episode:** NN
- **Pillar:** [Template A: Macro · Institutions | Template B: Company · [Name] | Template C: Structural]
- **Approved angle:** [angle name from the approved ANGLE_TEMPLATE]
- **Central question:** [single question the episode answers]
- **Thesis:** [one-sentence tentative thesis]
- **Template:** A | B | C
- **Status:** draft | reviewed | production-ready
- **Drafted:** YYYY-MM-DD
- **Word target:** ~NNNN (~NN min)
- **Last verified:** YYYY-MM-DD
- **Companion files:** storyboards/NN_*.md
```

## Five-section count (fixed)

Every script has exactly five numbered sections — `## SECTION 1` through `## SECTION 5`.

Section 1 is always "The Anomaly". Section 5 is always "The Verdict".
Sections 2, 3, and 4 names depend on the declared template:

| Section | Template A | Template B | Template C |
|---------|-----------|-----------|-----------|
| 2 | The Paper Trail | The Business Model | The Origin |
| 3 | The Field Reality | The Operational Reality | How It Plays Out |
| 4 | The Systemic Domino Effect | The Competitive Position | The Structural Risk |

## Section 1 rhythm (non-negotiable)

- Short, punchy sentences (under 15 words each for the opening).
- Echo a key word or phrase across two or three consecutive sentences.
- Include a transitional sentence: "That [X] was not an accident."
- Open on a documented concrete event, decision, filing, or institutional anomaly.
- Close with the single central question in plain English.
- Never open on a fictional character, invented scene, or unverifiable anecdote.

## No-repetition rule

Every concept, figure, and definition is stated once — at the point where it first matters.
Later sections may reference it in one clause. Never re-explain.

## Citation format

Inline: `[SOURCE: publication/institution, year]`
All inline citations collected in `## SOURCES` block at the end.
Fast-moving figures tagged `[VERIFY]`.

## Claim classification (inline labelling)

Add classification before or after any claim where ambiguity exists:

- **VERIFIED** — supported by a named primary source
- **REPORTED** — credible journalism, not independently confirmed; attribute explicitly
- **ANALYSIS** — interpretation drawn from verified evidence; label it
- **ESTIMATE** — calculation with method shown
- **UNRESOLVED** — conflicting sources; tag `[VERIFY]` and note the conflict

Never present ANALYSIS as fact. Never present ESTIMATE as a VERIFIED figure.

## Nonfiction default

Never invent characters, scenes, conversations, motives, or personal experiences.
Section 1 must open on a documented event — not a dramatised version of one.
