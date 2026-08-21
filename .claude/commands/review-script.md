# /review-script

Audit a script draft against CLAUDE.md and the script rules. Report findings only.
Do not make revisions unless the user explicitly requests them after seeing the audit.

## Before running

1. Read `CLAUDE.md`.
2. Read `.claude/rules/scripts.md`.
3. Identify the script file to review (user must specify the path or episode number).

## What to check

Run these checks in order and report each finding:

### Structure
- [ ] Exactly five section headers (`## SECTION 1` through `## SECTION 5`)
- [ ] Section names match the declared template (A, B, or C)
- [ ] `## SOURCES` block exists and is populated
- [ ] Front-matter contains all required fields: episode, approved_angle, central_question,
      thesis, template, status, word_count, estimated_duration, last_verified

### Section 1 integrity
- [ ] Opens on a documented, concrete event or institutional anomaly
- [ ] Sentences are short and punchy (flag any sentence over 25 words in Section 1)
- [ ] Contains a transitional echo sentence ("That [X] was not an accident" or equivalent)
- [ ] Closes with the single central question
- [ ] No fictional characters, invented scenes, or unverifiable anecdotes

### Nonfiction compliance
- [ ] No invented characters, employees, families, or protagonists
- [ ] No invented conversations, phone calls, or private reactions
- [ ] No invented motives, deadlines, or personal experiences
- [ ] No fictional scenes (flag patterns: "walked into", "picked up the phone",
      "looked at the numbers and realised", any named individual performing an undocumented act)

### Script purity
- [ ] No `[VISUAL ...]` annotations
- [ ] No `[FOOTAGE ...]` or `[B-ROLL ...]` cues
- [ ] No camera directions or editing instructions
- [ ] No music or sound-effect notes
- [ ] No on-screen text specifications
- [ ] No thumbnail ideas

### Language and editorial
- [ ] No banned clichés: "game-changer", "at the end of the day", "synergy",
      "disrupt" (unless used precisely and critically), "journey"
- [ ] No em dashes used where a comma or period would do (flag all em dashes)
- [ ] Every jargon term defined on first use
- [ ] No concept, figure, or definition repeated across sections (flag repetitions)
- [ ] No undefined abbreviations

### Sourcing
- [ ] Every statistical claim has an adjacent `[SOURCE: ...]` tag
- [ ] Every claim is classified (VERIFIED / REPORTED / ANALYSIS / ESTIMATE)
- [ ] Count of `[VERIFY]` tags (report the count; any above 3 warrants attention)
- [ ] No search-result snippet cited as a primary source

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

## After reviewing

Wait for the user to request revisions. Do not make changes to the script unless asked.
If the user asks for revisions, make only the changes needed to address the findings.
Do not rewrite sections that passed review.
