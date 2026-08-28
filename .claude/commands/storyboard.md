# /storyboard

Create a visual production plan for a finalised script. Never modify the script.

## Before running

1. Read `CLAUDE.md`.
2. Read `.claude/rules/storyboards.md`.
3. Read `.claude/rules/visual-system.md`.
4. Confirm the companion script exists and has been reviewed.
5. Identify the episode number and slug.

## What to create

Output file: `storyboards/NN_slug_visuals.md`

The storyboard translates each script section's timestamp range into concrete
production directions. It never changes the narration or the section structure.

## Structure

Read the script's front-matter first. `structure_type: flexible` scripts use
`## Part N — [Name]` headings, and the number of Parts is whatever the
script's `section_count` field says — three, four, five, six, or more. Do
not assume five. Only `structure_type: legacy-A/B/C` scripts use the fixed
five-`SECTION` format.

Build one storyboard block per script Part (or Section, for legacy scripts),
using the script's own Part names and in the script's own order:

```markdown
# [Episode Title] — Visual Production Plan

- **Episode:** NN
- **Script file:** scripts/NN_slug.md
- **Structure:** flexible, N parts (matches script `section_count`) | legacy-A/B/C
- **Palette:** light (#F8F9FA background) — current standard for ep 06+
- **Editing tool:** CapCut only — beginner-friendly, one-tap animation presets
- **Footage rights log:** research/source-registers/NN_slug_sources.csv

---

## Part 1 — [Name from script] (00:00 – MM:SS)

### [00:00 – 00:XX] FOOTAGE — [short label]
- Shot: [specific, topic-related scene — not generic filler; see "Footage
  balance and specificity" below]
- Source: [library]; licence; fallback if unavailable
- Animation: none (footage plays as-is) or a simple CapCut zoom/pan
- Duration: [X]s

### [00:XX – 00:YY] GRAPHIC — [short label]
- Type: source-screenshot card | plain text/number card (see
  `.claude/rules/visual-system.md`, "Source-screenshot cards")
- Visual: [what's on screen — the screenshotted source + highlight, or the
  text/number and label]
- Animation: one CapCut preset only (fade in / slide in / zoom in) — never a
  multi-element build
- Source caption: "Source: [Institution/Publication], [Date]" (omit only for
  the channel's own ESTIMATE/ANALYSIS cards, which are unsourced by nature)
- Duration: [X]s

### Transition to Part 2
[Cut / dissolve; duration]

---

[Repeat for each remaining Part in the script, using its actual name and
heading number. The last Part has no "Transition to next Part" — end with a
closing treatment instead.]
```

## Visual system

Apply the current palette (episodes 06+):
- Background: `#F8F9FA`
- Primary text: `#1A1A1A`
- Secondary text: `#555555`
- Green accent: `#1EB53A`
- Red accent: `#D32F2F`

## Footage balance and specificity

The channel's editor works in CapCut only and has never edited before.
Default to footage over graphics: most of the runtime should be B-roll the
editor can drop straight onto the timeline. Reserve GRAPHIC cues for the
handful of moments that genuinely need a number on screen (a headline figure,
a central comparison) — not one graphic per statistic.

Every footage cue must show something specific to the scene being narrated —
search terms drawn from that specific moment, not the episode's general
topic. Avoid interchangeable "any building" filler.

## Graphics: source-screenshot cards first

Default graphic technique: screenshot the actual source document (an
uploaded PDF page, an official webpage, a news article) behind an on-screen
figure, crop tight, add a highlight box over the key figure, caption
"Source: [Institution], [Date]," apply one simple CapCut zoom/fade. This
needs no design work and is more credible than a recreated chart. Use a
plain text/number card only when no source document exists to screenshot.
Never build a custom animated chart (bar/donut/timeline) — beyond this
editor's skill level; use two simple side-by-side cards instead if a
comparison needs visualizing.

## Footage notes

Every B-roll cue must include:
- Source library (Pexels / Pixabay / Pond5 / self-captured)
- Licence type (CC0 / royalty-free / licensed)
- A fallback (a source-screenshot card or plain text card) if footage is
  unavailable

Add every footage cue to `research/source-registers/NN_slug_sources.csv`.
Public availability does not equal reuse permission.

## After creating the storyboard

Confirm the footage rights log has been updated for every footage cue.
Redirect the user to `/footage` to clear outstanding rights items.
