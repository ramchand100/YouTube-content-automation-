# Visual System

This file governs visual decisions for the channel: palette, typography,
motion graphics, and footage assembly.

---

## Colour palette

| Role | Hex | Use |
|------|-----|-----|
| Background | `#F8F9FA` | Page and card background |
| Primary text | `#1A1A1A` | Body copy, headlines |
| Secondary text | `#555555` | Captions, labels, sub-text |
| Green accent | `#1EB53A` | Growth, viable option, positive path |
| Red accent | `#D32F2F` | Cost gap, risk, decline, circular debt |
| Card background | `#FFFFFF` | Cards and callout boxes (with subtle shadow) |
| Divider / border | `#E0E0E0` | Horizontal rules, borders |

Do not use palette colours for decorative purposes. Each colour carries meaning.

---

## Typography

| Role | Typeface |
|------|----------|
| Body copy, captions, definitions | Inter |
| Numbers, titles, emphasis | Archivo Black |

---

## Graphics tool policy

**Remotion** is the primary system for all animated in-video graphics, data
visualisations, timelines, maps, diagrams, animated labels, and reusable motion
components. Episode data lives in `remotion/data/epNN_data.json`. Claude may create
and modify Remotion compositions using that JSON.

**Canva** is the primary system for thumbnails, static promotional graphics, social
assets, title cards, and designs requiring fast manual layout or collaboration.

**CapCut** is used for final footage assembly, narration, music, captions, and
placement of Remotion exports at storyboard timecodes. The editor adds B-roll at
`[FOOTAGE ...]` cues from the matching storyboard file.

Footage cues live in storyboards only. They never appear inside the script.

Do not recreate a Remotion data visualisation manually in Canva unless the graphic
is static and does not require timing, animation, or data-driven updates.

---

## Episodes 01–05 palette note

Episodes 01–05 storyboards and thumbnail prompts used the legacy dark palette
(`background: #0A0A0A`). The current standard is the light palette above.

Do not change the archived files. Use the light palette for all new episodes.
