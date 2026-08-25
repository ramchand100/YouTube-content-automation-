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
- **Remotion data:** remotion/data/epNN_data.json
- **Footage rights log:** research/source-registers/NN_slug_sources.csv

---

## Part 1 — [Name from script] (00:00 – MM:SS)

### Motion graphic
[Composition name, animation type, duration, data source, palette tokens used]

### B-roll / footage
[Description of what to show; source library; licence; fallback if unavailable]

### On-screen text
[Exact text strings; font; timing; fade in / fade out]

### Chart / data overlay (if applicable)
[Chart type; data file reference; annotation text]

### Transition to Part 2
[Cut / dissolve / wipe; duration]

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

## Footage notes

Every B-roll cue must include:
- Source library (Pexels / Pixabay / Pond5 / self-captured)
- Licence type (CC0 / royalty-free / licensed)
- A fallback (Remotion graphic or text card) if footage is unavailable

Add every footage cue to `research/source-registers/NN_slug_sources.csv`.
Public availability does not equal reuse permission.

## After creating the storyboard

Confirm the footage rights log has been updated for every footage cue.
Redirect the user to `/footage` to clear outstanding rights items.
