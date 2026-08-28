# /review-script

Audit a script draft against CLAUDE.md and the script rules. Report findings only.
Do not make revisions unless the user explicitly requests them after seeing the audit.

## Before running

1. Read `CLAUDE.md`.
2. Read `.claude/rules/scripts.md`.
3. Read `docs/editorial/prose-style.md` and `docs/editorial/storytelling.md`.
4. Identify the script file to review (user must specify the path or episode number).
5. Read the script's front-matter to determine `structure_type` and `section_count`.

## What to check

Run these checks in order and report each finding:

### Structure

- [ ] `structure_type: flexible` scripts use `## Part N — [Name]` headings; the
      number of Part headings matches the front-matter `section_count` field.
- [ ] `structure_type: legacy-A/B/C` scripts use `## SECTION N — [Name]` headings
      (exactly five) and section names match the declared template (A, B, or C).
      This format is only expected when explicitly requested — do not flag a
      flexible script for not having five sections.
- [ ] `## SOURCES` block exists and is populated.
- [ ] Front-matter contains all required fields: `episode, title, topic,
      approved_angle, central_question, thesis, story_logic, structure_type,
      section_count, status, research_date, data_cutoff_date, freshness_status,
      word_count, estimated_duration, last_verified`.

### Opening (Part/Section 1) integrity

- [ ] Opens on a documented, concrete event or institutional anomaly — not a
      channel greeting or preamble.
- [ ] The hook lands in the first one or two sentences — the strongest
      documented anomaly or comparison, not several paragraphs of setup. See
      `docs/editorial/storytelling.md`, "Land the hook fast."
- [ ] Immediately after the hook, a two-to-three sentence retention bridge
      previews what the episode investigates. See
      `docs/editorial/storytelling.md`, "Retention bridge."
- [ ] Sentences are short and punchy (flag any sentence over 25 words in the
      opening).
- [ ] Does NOT contain a formulaic transitional echo sentence — "That [X] was
      not an accident," "That was not a coincidence," "The numbers tell the
      story," or equivalent. These are banned; flag any instance as BLOCK. See
      `.claude/rules/scripts.md`, "Opening section rhythm."
- [ ] Closes with the single central question, in a natural sentence.
- [ ] No fictional characters, invented scenes, or unverifiable anecdotes.

### Nonfiction compliance

- [ ] No invented characters, employees, families, or protagonists.
- [ ] No invented conversations, phone calls, or private reactions.
- [ ] No invented motives, deadlines, or personal experiences.
- [ ] No fictional scenes (flag patterns: "walked into", "picked up the phone",
      "looked at the numbers and realised", any named individual performing an
      undocumented act).

### Script purity

- [ ] No `[VISUAL ...]` annotations.
- [ ] No `[FOOTAGE ...]` or `[B-ROLL ...]` cues.
- [ ] No camera directions or editing instructions.
- [ ] No music or sound-effect notes.
- [ ] No on-screen text specifications.
- [ ] No thumbnail ideas.
- [ ] No delivery-notes markup leaked into the script — no stray `**bold**`
      emphasis markers, no `/` pause markers, no `*italic parenthetical*` pace
      notes. That markup belongs only in the companion
      `delivery-notes/NN_slug_delivery-notes.md` file, never in the script
      itself. See `.claude/rules/delivery-notes.md`.

### Political neutrality

- [ ] No election-timing, ribbon-cutting, or campaign imagery.
- [ ] No motive attributed to a named office-holder unless a specific claim
      requires it and is directly evidenced.
- [ ] Decisions, budgets, and incentives are described in administrative and
      economic terms ("the authority approved," "the incentive was," "the
      policy created"), not as political strategy or a personal win. See
      CLAUDE.md §4 rule 6 and `docs/editorial/prose-style.md`, "Political
      neutrality."

### Language and editorial

- [ ] Passes the shopkeeper / eighth-grade plain-language test — an
      intelligent viewer with little finance background could follow every
      sentence on first listen. Flag any sentence that would require rereading.
      See CLAUDE.md §2 and `docs/editorial/prose-style.md`, "Language."
- [ ] Narration paragraphs run one or two sentences — one spoken beat per
      paragraph break, not dense multi-sentence blocks. Flag any paragraph
      over two sentences. See `docs/editorial/prose-style.md`, "Paragraph
      rhythm."
- [ ] Every large or technical number carries a daily-life reference point
      the first time it appears (a derived rate, a share of another cited
      figure, a rupee conversion, a familiar distance). Flag any bare large
      number with no relatable-scale anchor. See
      `docs/editorial/prose-style.md`, "Relatable scale."
- [ ] Every part (except the last) ends by creating the next analytical
      question — an open loop, not a closed summary. See
      `docs/editorial/storytelling.md`, "Section and part transitions."
- [ ] No banned clichés: "game-changer", "at the end of the day", "synergy",
      "disrupt" (unless used precisely and critically), "journey".
- [ ] No em dashes used where a comma or period would do (flag all em dashes).
- [ ] Every jargon term defined on first use.
- [ ] No concept, figure, or definition repeated across sections (flag
      repetitions).
- [ ] No undefined abbreviations.

### Sourcing

- [ ] Every statistical claim has an adjacent `[SOURCE: ...]` tag.
- [ ] Every claim is classified (VERIFIED / REPORTED / ANALYSIS / ESTIMATE /
      UNRESOLVED).
- [ ] Count of `[VERIFY]` tags (report the count; any above 3 warrants
      attention).
- [ ] No search-result snippet cited as a primary source.

### Metrics

- Total word count
- Estimated voiceover duration at 150 wpm
- Number of `[SOURCE: ...]` tags
- Number of `[VERIFY]` tags

## Output format

```
## Script review: [episode number and title]

### Summary
- Word count: N
- Estimated duration: N min N sec
- Source tags: N
- [VERIFY] tags: N

### Findings

| # | Section | Check | Finding | Severity |
|---|---------|-------|---------|---------|
| 1 | ... | ... | ... | BLOCK / WARN / NOTE |

### BLOCK items (must fix before production-ready)
[List only the blocking issues.]

### Overall status
PASS (no blocking issues) | NEEDS REVISION (N blocking issues)
```

## Important limitation

This review is a structured read against documented rules — mechanical
checks (front-matter fields, section counts, banned phrases, purity) are
reliable; judgment-based checks (hook strength, retention-bridge quality,
whether a number's relatable-scale anchor actually helps, whether framing is
genuinely neutral) are Claude's editorial read and should be treated as a
strong recommendation, not an infallible gate. `validate_script.py` covers
only the mechanical subset and can be run as a fast pre-check before a full
`/review-script` pass.

## After reviewing

Wait for the user to request revisions. Do not make changes to the script unless asked.
If the user asks for revisions, make only the changes needed to address the findings.
Do not rewrite sections that passed review.
