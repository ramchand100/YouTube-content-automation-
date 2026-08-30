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

Every script must open with a YAML front-matter block between `---` delimiters:

```yaml
---
episode:
title:
topic:
approved_angle:
central_question:
thesis:
story_logic:
structure_type:
section_count:
status: draft
research_date:
data_cutoff_date:
freshness_status:
word_count:
estimated_duration:
last_verified:
---
```

`structure_type` is one of: `flexible` or `legacy-A` / `legacy-B` / `legacy-C`
(legacy types are only used when the five-section format is explicitly requested).

`section_count` must match the number of `## Part N —` sections in the script body.

## Section count and structure

The section count is determined by the approved structure, not by a template default.
Scripts may have three, four, five, six, or more sections — whatever the story logic requires.

Section headings use `## Part N — [Section Name]` format.

The structure must be approved before writing begins. See `/write-script` for the
approval gate and `.claude/skills/pakistan-documentary-production/SKILL.md` for the
story logic classification system.

### Legacy five-section format (optional)

The A/B/C five-section system from earlier episodes is available when explicitly
requested or when the topic fits one of the three templates cleanly. Legacy scripts
use `## SECTION N — [Name]` headings. Do not use the legacy format by default.

| Section | Template A | Template B | Template C |
|---------|-----------|-----------|-----------|
| 2 | The Paper Trail | The Business Model | The Origin |
| 3 | The Field Reality | The Operational Reality | How It Plays Out |
| 4 | The Systemic Domino Effect | The Competitive Position | The Structural Risk |

## Opening section rhythm (non-negotiable)

- Open on a documented concrete event, decision, filing, price, shutdown, or institutional anomaly.
- Begin with the strongest documented anomaly or consequence available.
- Use sentence-length variation naturally. Short sentences for weight; do not force a sequence of fragments.
- Do not use formulaic transitions such as "That was not an accident," "That was not a coincidence," or "The numbers tell the story." If the evidence points to a causal chain, explain it directly.
- Close the opening section with the central question in a natural sentence.
- Never open on a fictional character, invented scene, or unverifiable anecdote.

See `docs/editorial/storytelling.md` — Opening rhythm for full guidance.

## Paragraph rhythm

Keep narration paragraphs to one or two sentences — one spoken beat per
paragraph break, not dense multi-sentence blocks. This applies to the whole
script, not just the opening. See `docs/editorial/prose-style.md`,
"Paragraph rhythm," for worked examples.

## Relatable scale

Every large or technical number gets a daily-life reference point (a derived
rate, a share of another cited figure, a rupee conversion, a familiar
distance) the first time it appears. Label a derived comparison `[ESTIMATE]`
with the method shown. See `docs/editorial/prose-style.md`, "Relatable
scale."

## Section and part transitions

Every part except the last ends by creating the next analytical question, not
just stopping. See `docs/editorial/storytelling.md`, "Section and part
transitions."

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
