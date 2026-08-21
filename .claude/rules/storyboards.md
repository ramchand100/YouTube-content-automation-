---
paths:
  - storyboards/**
---

# Storyboard rules — applies to all files in storyboards/

## Purpose

Storyboard files are the single source of truth for all visual direction.
They translate script timestamps into concrete editing instructions.

**Never modify the script file from inside a storyboard session.**
The script is approved narration. The storyboard is the production plan for it.

## What storyboards contain

Every storyboard must include, for each script timestamp range:

1. **Timestamp** — matches the script section (format: `MM:SS – MM:SS`)
2. **Motion graphic / animation direction** — composition name, animation style,
   data source, duration, colour tokens from the visual system
3. **B-roll / footage direction** — what to show; where to source it (approved stock
   library or self-captured); fallback if footage is unavailable
4. **On-screen text** — exact text strings that appear, font spec, timing
5. **Chart / data overlay** — data file reference, chart type, annotation
6. **Transition** — cut, dissolve, wipe; duration
7. **Pre-comp name** — Remotion composition ID or After Effects pre-comp label

## File naming

`storyboards/NN_<slug>_visuals.md`

The `NN` and `slug` must match the companion script exactly.

## Palette

Use current palette tokens (defined in `.claude/rules/visual-system.md`):
- Episodes 01–05 used the dark palette `#0A0A0A`. Those storyboards are archived as-is.
- Episodes 06 onward use the light palette `#F8F9FA`. Apply this to all new storyboards.

## Footage notes

Every footage cue must include a rights note:
- Source library (Pexels / Pixabay / Pond5 / Shutterstock / self-captured)
- Licence type (CC0 / royalty-free / licensed)
- Fallback (Remotion motion graphic / text card) if footage is unavailable or unlicensed

Public availability does not equal reuse permission. Never assume a video is
freely usable because it appears on YouTube or a news website.
