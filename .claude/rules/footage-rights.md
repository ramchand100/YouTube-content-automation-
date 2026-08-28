---
paths:
  - docs/**
  - research/**
  - storyboards/**
---

# Footage-rights rules — applies to docs/, research/, and storyboards/

## Default position

Public availability is not copyright permission.

Never assume a video, image, or audio file may be reused because:
- It appears on YouTube.
- It appears on a news website.
- It appears in search results.
- It is "just B-roll" or "just background".
- The creator appears to be a government body or public institution.

## Approved sources

### Free / CC0
- Pexels (pexels.com) — confirm licence on each clip
- Pixabay (pixabay.com) — confirm licence on each clip
- Videvo CC0 section (videvo.net, filter by CC0 only)

### Licensed stock (requires account and purchase)
- Pond5
- Shutterstock (with active licence)
- Artgrid
- Envato Elements (with active subscription)

### Self-captured
- Any footage the channel shoots itself.

### Official government / regulatory footage
- Pakistan government press conferences, National Assembly sessions, SECP/SBP official
  releases marked for reuse. Confirm the specific clip's licence before use.

## Never use without clearance

- Pakistan TV network clips (Geo, ARY, Hum, Dawn News)
- Airline promotional footage (PIA, Emirates, etc.) without rights
- Company promotional videos without rights
- News broadcast clips from any outlet
- Music without a content-ID-safe licence

## Rights register

Every footage cue in a storyboard must appear in the episode's footage-rights log:
`research/source-registers/NN_slug_sources.csv`

Columns: clip_id | description | source | licence | url | cleared (yes/no/pending) | fallback

## Fallback hierarchy

If footage cannot be cleared:
1. Replace with a source-screenshot card (see `.claude/rules/visual-system.md`)
   if the cue was standing in for a citable figure or document.
2. Replace with a plain text card on the channel's colour palette.
3. Replace with self-captured equivalent footage.

Never ship a clip with an unclear or assumed licence.
