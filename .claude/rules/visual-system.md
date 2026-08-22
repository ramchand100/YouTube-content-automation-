---
paths:
  - storyboards/**
  - prompts/**
  - remotion/**
---

# Visual system rules — applies to storyboards/, prompts/, and remotion/

## Current palette (episodes 06 onward)

Apply these tokens to all new storyboards, thumbnail specs, and Remotion compositions.

| Token | Hex | Use |
|-------|-----|-----|
| Background | `#F8F9FA` | Page / slide background |
| Primary text | `#1A1A1A` | Titles, body text |
| Secondary text | `#555555` | Captions, definitions, supporting labels |
| Green accent | `#1EB53A` | Growth, positive path, viable option |
| Red accent | `#D32F2F` | Cost gap, risk, decline, circular debt |
| Card background | `#FFFFFF` | Data cards, callout boxes |
| Border / divider | `#E0E0E0` | Separators, card outlines |

## Archive palette (episodes 01–05)

Storyboards and prompt files for episodes 01–05 use the dark palette:
- Background: `#0A0A0A`
- Text: `#F5F5F5`

These are archived as-is. Do not migrate them to the light palette.
When referencing episodes 01–05 visuals, note the palette divergence.

## Typography

- **Inter** — body text, captions, definitions, supporting labels
- **Archivo Black** — numbers, titles, key stats, callout figures

## Motion principles (Remotion)

- Compositions are defined in `remotion/src/Root.tsx`.
- Data per episode lives in `remotion/data/epNN_data.json`.
- Animations: simple entrances (fade, slide-up); no complex motion unless the data
  requires it.
- On-screen text and chart overlays must match the palette tokens above.

## Thumbnail conventions

- High-contrast composition: dark text on light background or vice versa.
- One focal point (a stat, a face, a building) — no cluttered compositions.
- 2–4 words that add a new idea rather than repeat the title.
- Green (`#1EB53A`) or red (`#D32F2F`) as the single accent colour.
- Avoid stock-photo faces; prefer motion-graphic data visuals or abstract
  representations of the topic.

## Graphics tool policy

**Remotion** is the primary system for all animated in-video graphics, data
visualisations, timelines, maps, diagrams, animated labels, and reusable motion
components.

Claude may create and modify Remotion compositions using episode-specific JSON data.

**Canva** is the primary system for thumbnails, static promotional graphics, social
assets, title cards, and designs requiring fast manual layout or collaboration.

**CapCut** is used for final footage assembly, narration, music, captions, and
placement of Remotion exports at storyboard timecodes.

Do not recreate a Remotion data visualisation manually in Canva unless the graphic
is static and does not require timing, animation, or data-driven updates.
