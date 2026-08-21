---
name: pakistan-documentary-production
description: >
  Use for Pakistani business, economics, macroeconomics, corporate strategy,
  energy, regulation, logistics, technology, research, documentary scripting,
  source auditing, storyboarding, and copyright-safe footage planning.
---

# Pakistan Documentary Production Skill

## Step 1 — Read the editorial constitution

Before any output, read `CLAUDE.md` in full. It governs language, tone, structure,
sourcing, and editorial rules for every file produced in this repository. It takes
precedence over any other instruction.

## Step 2 — Identify the user's intent

Determine which stage of the production workflow applies:

| User intent | Stage | Command |
|-------------|-------|---------|
| Has a broad topic, no angle yet | Angle generation | `/angles` |
| Has an approved angle, needs research | Research brief + claim ledger | `/research` |
| Has research, needs the script written | Script writing | `/write-script` |
| Has a draft script, needs review | Script review | `/review-script` |
| Has a final script, needs sources verified | Source audit | `/audit-sources` |
| Has a final script, needs visual plan | Storyboard | `/storyboard` |
| Has a storyboard, needs footage cleared | Footage rights | `/footage` |
| Wants everything from scratch | Full package | Run stages in order |

## Step 3 — Load only relevant path-scoped rules

Load the rule file that matches the current stage before writing any output:

- Writing or reviewing scripts → `.claude/rules/scripts.md`
- Research, claim ledgers, topic briefs → `.claude/rules/research.md`
- Storyboard creation → `.claude/rules/storyboards.md`
- Source auditing → `.claude/rules/source-audits.md`
- Footage rights checking → `.claude/rules/footage-rights.md`
- Visual system, palette, Remotion, thumbnails → `.claude/rules/visual-system.md`

## Step 4 — Require angle approval before research or scripting

If the user provides a broad topic and no approved angle exists:
1. Generate 6–10 angles using the angle format in `.claude/commands/angles.md`.
2. Score them using the weighted scoring table.
3. Recommend one angle.
4. Stop. Do not begin research or scripting until the user explicitly approves an angle.

## Step 5 — Require a research brief before scripting

If the user asks for a script but no research brief exists for the approved angle:
1. Redirect to `/research` first.
2. Do not write the script until the research brief exists and is complete.

## Step 6 — Select and approve a structure before writing

Do not impose a fixed number of sections on every episode. The approved angle
determines the narrative structure.

Before drafting any script:

1. Identify the central question.
2. Identify the thesis or proposition to test.
3. Classify the story logic:
   - Causal
   - Chronological
   - Financial
   - Comparative
   - Institutional
   - Operational
   - Regulatory
   - Company case study
   - Decision-focused
   - Structural or historical
4. Propose the number and names of sections.
5. Give every section a distinct purpose.
6. Explain why the structure fits the approved angle.
7. Identify evidence required for each section.
8. Identify likely repetition and causality risks.
9. Stop for structure approval before writing the full script.

A structure is approved only when:

- It serves the central question.
- No two sections repeat the same mechanism or evidence.
- Evidence precedes conclusions in every section.
- The viewer has enough context at each step.
- The opening is clear and grounded.
- The ending is honest and specific.
- It does not manufacture suspense.
- Available evidence can support every section.

The previous five-section system (Template A / B / C) is an optional legacy
format. It must not be used automatically. A script may use three, four, five,
six, or more sections when the subject requires it. The section count must be
justified by the approved angle and story logic.

Every script, regardless of section count, must contain:
- A strong grounded opening.
- A clear central question.
- A logical progression from evidence to analysis.
- Explicit uncertainty where required.
- A grounded, specific ending.

## Step 7 — Enforce nonfiction and no-fabrication

The default mode is strict nonfiction. Never invent:
- Characters, protagonists, or named individuals who are not documented
- Scenes, factory visits, office visits, or field observations
- Conversations, phone calls, or private reactions
- Motives, deadlines, or personal experiences
- Customer stories or anecdotes without documentary sources
- Quotations attributed to unnamed sources

Section 1 of every script must open on a documented event, official decision,
company filing, public statement, regulatory action, or verified market anomaly.

## Step 8 — Keep scripts narration-only

Scripts contain voiceover prose only. Never insert into a script:
- `[VISUAL ...]` or `[FOOTAGE ...]` cues
- Camera directions, editing notes, or music cues
- On-screen text specifications
- Production notes (except the Sources block)

All visual direction lives in `storyboards/NN_slug_visuals.md`.

## Step 9 — Keep visual instructions in storyboards

Storyboards contain all visual, motion-graphic, B-roll, and editing direction.
They never modify the script content. They translate approved script timestamps
into concrete production directions.

## Step 10 — Keep rights information in footage logs

Footage rights are tracked in `research/source-registers/NN_slug_sources.csv`.
Every footage cue in a storyboard must have a corresponding entry in that file.
Public availability is not copyright permission.

## Step 11 — Run the relevant audit before marking work complete

| Work | Audit required before completion |
|------|----------------------------------|
| Script | Script audit (`/review-script`) + source audit (`/audit-sources`) |
| Research brief | Claim ledger complete; no UNRESOLVED claims without `[VERIFY]` |
| Storyboard | All footage cues have rights status in the source register |
| Footage log | No "pending" entries; every clip is Cleared or replaced with fallback |

## Supporting files

Use these templates from this skill directory:
- `templates/research-brief.md` — research brief structure
- `templates/script-audit.md` — script audit checklist
- `templates/storyboard.md` — storyboard section template
- `templates/footage-rights.csv` — footage rights register headers
- `scripts/validate_script.py` — automated script validator
