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

## Motion principles (CapCut)

The channel's editor works exclusively in CapCut and has no prior editing
experience. Every storyboard must describe things achievable with CapCut's
built-in tools only:

- Text layers, image layers, and simple shapes (a highlight box/rectangle).
- One-tap animation presets: fade in/out, slide in/out, zoom in/out. Applied to
  a whole layer with a single tap — never hand-keyframed.
- No multi-element animated sequences, no custom-built charts that animate
  piece by piece. If a graphic needs more than one simple in/out animation to
  read correctly, it's too complex for this pipeline — simplify it or split it
  into two separate, simpler cards.
- On-screen text and cards must match the palette tokens above.

## Thumbnail conventions

- High-contrast composition: dark text on light background or vice versa.
- One focal point (a stat, a face, a building) — no cluttered compositions.
- 2–4 words that add a new idea rather than repeat the title.
- Green (`#1EB53A`) or red (`#D32F2F`) as the single accent colour.
- Avoid stock-photo faces; prefer a clean stat card or an abstract
  representation of the topic.

## Graphics tool policy

**CapCut is the default and primary tool for all in-video graphics, text, and
animation.** Every storyboard cue should describe something buildable directly
in CapCut, or as a static image imported into CapCut — never a custom-rendered
composition.

**Source-screenshot cards are the default graphic technique.** For any
on-screen figure traceable to a real visual source document — an uploaded PDF
(annual report, audited accounts), an official webpage, a news article —
screenshot the actual source rather than building a custom chart:
1. Screenshot or crop the relevant page/section (headline, chart, or the
   sentence containing the cited figure). Crop tightly.
2. Draw a simple highlight box over the key figure (CapCut's shape tool,
   semi-transparent fill) — no redrawing or recreating the source's own chart.
3. Add a caption: "Source: [Institution/Publication], [Date]" — Inter,
   `#555555`.
4. Apply one simple CapCut zoom-in or fade-in animation. Nothing more.

This is preferred over a custom chart: no design work, faster to produce, and
more credible — the viewer sees the actual primary document.

**Plain text/number cards** (Archivo Black number + Inter label, on the
palette background, built in Canva or directly in CapCut) are the fallback,
used only when no source document exists to screenshot — typically the
channel's own ESTIMATE/ANALYSIS calculations, or a claim with no single
document to point to.

**Canva** may be used to build a static text/number card when CapCut's own
text tools aren't sufficient, or for thumbnails and social assets. Canva's
"Animate" button can add one simple preset animation before exporting as a
clip for CapCut.

Never build a custom animated chart (bar chart, donut chart, animated
timeline, multi-element sequential build) — these require design and
animation skills beyond this editor's level. If a comparison needs
visualizing, use two simple side-by-side text/number cards instead of an
animated chart.

**Remotion** (`remotion/`) is a legacy pipeline from earlier in the project.
It requires writing and rendering React code and is not part of the default
storyboard workflow. Do not reference it in new storyboards unless the user
explicitly asks for a Remotion-rendered graphic for a specific episode.
