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
2. **Visual type** — GRAPHIC or FOOTAGE
3. **For a GRAPHIC cue** — either a source-screenshot card (screenshot the real
   source document, highlight box, "Source: ..." caption) or a plain
   text/number card when no source document exists — see
   `.claude/rules/visual-system.md`, "Source-screenshot cards are the default
   graphic technique." Plus one simple CapCut animation preset (fade/slide/zoom
   in or out) — never a hand-keyframed multi-element build.
4. **For a FOOTAGE cue** — what to show, specific to the scene being narrated
   (see "Footage must be topic-specific" below); where to source it; fallback
   if unavailable
5. **On-screen text** — exact text strings that appear, font spec, timing
6. **Transition** — cut or dissolve; duration

## Balance: footage over graphics

The channel's editor works in CapCut only and has no prior editing experience.
Most of a storyboard's runtime should be FOOTAGE the editor can drop onto the
timeline, not GRAPHIC cues requiring layout or animation work. Reserve GRAPHIC
cues for the moments that genuinely need a number on screen — a headline
figure, a central comparison — not a graphic for every statistic in the
script. A storyboard that is mostly graphics is doing it wrong for this
editor; footage is the default visual layer, graphics are the exception.

## Footage must be topic-specific, not generic

A footage cue must show something specific to what the voiceover is
describing at that moment — the actual subject matter (a hospital ward, a
construction site, a specific country's cityscape, financial documents, a
court building) — not an interchangeable "any building" or "any office" clip
reused across the episode. Search stock libraries with terms drawn from the
specific scene, not just the episode's general topic.

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
- Fallback (a source-screenshot card or plain text card) if footage is
  unavailable or unlicensed

Public availability does not equal reuse permission. Never assume a video is
freely usable because it appears on YouTube or a news website.
