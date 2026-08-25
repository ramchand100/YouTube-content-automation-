# Storyboard & Motion-Graphic Blueprint — Episode NN
## "[EPISODE TITLE]"

<!--
Timestamp-linked to scripts/NN_<slug>.md.
FACELESS FORMAT: voiceover + motion graphics + B-roll only. No on-camera host.
Two visual layers — every cue is labelled:
  GRAPHIC = Remotion-rendered animation (built from data/epNN_data.json)
  FOOTAGE = B-roll added in CapCut at the marked cue

Every cue entry must include:
  - Timecode in and out (mm:ss - mm:ss)
  - Type: GRAPHIC or FOOTAGE
  - What appears: specific elements, text, data
  - How it builds: step-by-step animation sequence with sub-timings
  - HOLD: how many seconds it stays static after building
  - END: exact trigger and transition type (hard cut / fade / dissolve)
  - Total duration of the cue

Voiceover runs continuously. Visuals cut to match the prose, not the other way around.

STRUCTURE: check the companion script's front-matter first. Most scripts use
structure_type: flexible with `## Part N — [Name]` headings, and the number
of Parts is whatever the script's section_count says — three, four, five,
six, or more, not a fixed five. The five `## Part` blocks below are a single
worked example (based on legacy Template A's section names and a ~15-minute
runtime) showing the cue-level density and format expected in every Part —
GRAPHIC/FOOTAGE cues, Element-by-element builds, HOLD, END, pre-comp names.
Copy that density, not the count: add or remove Part blocks to match the
actual script, rename each Part after the script's own Part names, and
retime every cue against the script's actual timestamps and
estimated_duration rather than the 0:00-15:00 range used here. Only a script
with structure_type: legacy-A/B/C should keep exactly five Sections named
to match that template.
-->

**Voiceover:** ~150 wpm, documentary register. Recorded clean, no music bleed.
**Canvas:** 1920x1080. Background: off-white `#F8F9FA`. Card fill: white `#FFFFFF` with drop shadow.
**Palette:** text `#1A1A1A` · captions `#555555` · green `#1EB53A` · red `#D32F2F` · border `#E0E0E0`.
**Type:** Archivo Black for numbers and titles · Inter for body, captions, definitions.
**Source captions:** Inter 11px, `#555555`, bottom-right, visible for the full duration any number is on screen.
**Rendering:** GRAPHIC cues rendered with Remotion from data/epNN_data.json.
**Assembly:** import Remotion clips + voiceover into CapCut. Add B-roll at FOOTAGE cues.
**Music:** low ambient score under all graphics; drop entirely for key analytical lines;
silent under FOOTAGE cold opens unless specified.

---

## Part 1 — The Unsolved Reality (0:00 - 2:00)

**[0:00 - 0:10] FOOTAGE — cold open**
- Shot: [describe specific scene — a location, object, or activity that opens the question]
- Sound: ambient only — no music, no voiceover. Let the scene breathe.
- HOLD: 10 seconds static. No graphics overlay.
- END: hard cut to black at 0:10 as voiceover begins.
- Duration: 10s

**[0:10 - 0:45] GRAPHIC — opening context card (optional; use if the scene needs grounding)**
- Canvas: near-black.
- Element 1 [0:10 - 0:13]: single white line fades in — one sentence establishing time/place.
- HOLD: 5s static.
- END: fade out to black at 0:18. Voiceover continues over black.
- Duration: 8s

**[0:45 - 1:20] GRAPHIC — openingStats: the core contrast**
- Canvas: near-black.
- Element 1 [0:45 - 0:50]: left label fades in — white text, 1-2 words.
- Element 2 [0:50 - 0:56]: left number counts up — green, large.
- Element 3 [0:56 - 1:01]: right label fades in — white text.
- Element 4 [1:01 - 1:07]: right number counts up — red, large.
- Element 5 [1:07 - 1:13]: contrast line appears between them — white, smaller.
- Element 6 [1:13 - 1:18]: source caption fades in bottom-right — Inter, 12px.
- HOLD: 5s with all elements visible.
- END: hard cut at 1:23. Voiceover has delivered the contrast line.
- Duration: 35s

**[1:20 - 1:50] FOOTAGE — consequence scene**
- Shot: [describe the real-world consequence the voiceover is describing]
- Voiceover continues over footage. No graphic overlay.
- HOLD: as long as the voiceover passage runs.
- END: hard cut to title card.
- Duration: ~30s

**[1:50 - 2:00] GRAPHIC — title card**
- Canvas: near-black.
- Element 1 [1:50 - 1:54]: episode title types on — Coolvetica, large, white.
  One keyword in green or red accent.
- Element 2 [1:55 - 1:58]: sub-caption fades in — one line, white, Inter.
- Music lifts to full ambient level.
- HOLD: 4s.
- END: hard cut to Part 2 at 2:00.
- Duration: 10s

---

## Part 2 — The Paper Trail (2:00 - 6:00)

**[2:00 - 2:45] GRAPHIC — supply/demand or unit economics setup**
- Canvas: near-black.
- Element 1 [2:00 - 2:05]: section label fades in top-left — "THE PAPER TRAIL", Inter, small, dim.
- Element 2 [2:05 - 2:15]: first bar or number builds — green, animated count-up or bar fill.
  Label and source caption appear simultaneously.
- Element 3 [2:15 - 2:25]: second element builds — contrasting colour. Label and source.
- Element 4 [2:25 - 2:35]: gap or difference highlighted — red band or delta label.
- HOLD: 10s with all elements visible. Voiceover explains what is on screen.
- END: hard cut to next graphic or footage at 2:45.
- Duration: 45s

**[2:45 - 3:15] GRAPHIC — defCard: key term definition**
- Canvas: near-black.
- Element 1 [2:45 - 2:48]: term appears in white — Coolvetica, centred or left-aligned.
- Element 2 [2:48 - 2:52]: "=" separator appears.
- Element 3 [2:52 - 3:05]: definition builds word-by-word or line-by-line — Inter, white.
- HOLD: 8s with full definition visible.
- END: fade out at 3:13. Next element fades in.
- Duration: 28s

**[3:15 - 4:30] GRAPHIC — second data layer (cost stack / comparison / flow)**
- Canvas: near-black.
- [Describe the specific chart type and the data it shows.]
- Build sequence: [list each element with its sub-timecode — e.g., Element 1 [3:15-3:20]: ...]
- Source captions on every figure that appears.
- HOLD: [X]s after the build is complete.
- END: hard cut / fade at [timecode].
- Duration: ~75s

**[4:30 - 5:30] FOOTAGE — illustrative B-roll**
- Shot: [describe what footage illustrates the paper trail mechanic — e.g., a port, a terminal, a market]
- Voiceover continues. No graphic overlay except optional lower-third source caption.
- HOLD: as long as the voiceover passage runs.
- END: hard cut at 5:30.
- Duration: ~60s

**[5:30 - 6:00] GRAPHIC — section summary card**
- Canvas: near-black.
- 2-3 key figures from Part 2 held cleanly on one card.
- No animation — static summary the viewer can read before Part 3 begins.
- Source captions visible.
- HOLD: 20s.
- END: hard cut to Part 3 at 6:00.
- Duration: 30s

---

## Part 3 — The Field Reality (6:00 - 10:00)

**[6:00 - 6:45] FOOTAGE — ground-level scene**
- Shot: [specific scene — market, factory floor, distribution point, informal transaction]
- Voiceover runs over footage. No graphics overlay.
- HOLD: as long as the voiceover passage runs.
- END: hard cut to graphic at 6:45.
- Duration: ~45s

**[6:45 - 7:30] GRAPHIC — informal mechanic / flow diagram**
- Canvas: near-black.
- Pre-comp: `informalFlow`.
- Build sequence: nodes and arrows appear one step at a time, in the order the voiceover describes them.
  [List each node with its sub-timecode and label.]
- Source caption where applicable.
- HOLD: 10s after the final node appears.
- END: hard cut at 7:30.
- Duration: 45s

**[7:30 - 8:30] FOOTAGE — second ground-level scene**
- Shot: [a different location or angle that illustrates the second field mechanic]
- Duration: ~60s

**[8:30 - 9:30] GRAPHIC — defCard or data visual for second field mechanic**
- [Describe the specific card or chart.]
- Build sequence with sub-timecodes.
- HOLD: [X]s.
- END: hard cut at 9:30.
- Duration: ~60s

**[9:30 - 10:00] GRAPHIC — field reality summary**
- One clean takeaway: single line or two-item list on black.
- HOLD: 20s.
- END: hard cut to Part 4 at 10:00.
- Duration: 30s

---

## Part 4 — The Systemic Domino Effect (10:00 - 13:00)

**[10:00 - 11:00] GRAPHIC — macroRipple: first domino chain**
- Pre-comp: `macroRipple`.
- Canvas: near-black.
- Build sequence: each block appears and falls into the next, timed to the voiceover.
  Block 1 [10:00 - 10:08]: [label] — white block, fades in.
  Block 2 [10:08 - 10:16]: [label] — white block, falls from Block 1.
  Block 3 [10:16 - 10:24]: [label] falls.
  [Continue for all blocks in the chain.]
- Source captions appear below each block as it lands.
- HOLD: 10s after final block lands.
- END: hard cut at 11:00.
- Duration: 60s

**[11:00 - 11:45] GRAPHIC — FX / fiscal impact**
- [Describe specific bars, maps, or data visuals for macro Part 4 second beat.]
- Build sequence with sub-timecodes.
- Source captions.
- HOLD: [X]s.
- END: hard cut at 11:45.
- Duration: 45s

**[11:45 - 13:00] FOOTAGE — macro consequence scene**
- Shot: [a visual that represents the economy-wide consequence — e.g., factory, construction site, market]
- Voiceover delivers the systemic summary over footage.
- END: hard cut to Part 5 at 13:00.
- Duration: ~75s

---

## Part 5 — The Verdict & Future Outlook (13:00 - End)

**[13:00 - 13:10] GRAPHIC — forward question**
- Canvas: near-black.
- Single line, white: "[THE FORWARD QUESTION?]"
- Fade in slowly over 3s.
- HOLD: 7s static. Music drops slightly.
- END: hard cut at 13:10.
- Duration: 10s

**[13:10 - 13:55] GRAPHIC — outlook: forward paths**
- Pre-comp: `outlook`.
- Canvas: near-black.
- Row 1 [13:10 - 13:20]: [Path 1] — icon + label + timeline appears. Green if underway.
- Row 2 [13:20 - 13:30]: [Path 2] — icon + label + timeline. Amber if possible.
- Row 3 [13:30 - 13:40]: [Path 3] — icon + label + timeline. Grey if uncertain.
- Source captions where applicable.
- HOLD: 12s with all three rows visible.
- END: hard cut at 13:52.
- Duration: 42s

**[13:55 - 14:30] FOOTAGE — closing scene**
- Shot: [a scene that mirrors or resolves the opening — same location, different outcome, or forward-looking]
- Voiceover delivers verdict and implications over footage.
- END: fade to black at 14:30.
- Duration: 35s

**[14:30 - 14:50] GRAPHIC — end card**
- Canvas: near-black.
- Channel logo fades in centred.
- Subscribe button or prompt appears below.
- "[NEXT EPISODE TEASE]" line appears — one sentence.
- Music fades out.
- HOLD: 15s.
- END: video ends at 14:45-15:00.
- Duration: 15-20s

---

## Reusable pre-comps (build once, parameterise, reuse every episode)

| Pre-comp | Inputs | Typical duration |
|---|---|---|
| `defCard` | term, definition | 20-30s |
| `sourceCaption` | source text string | overlay, no fixed duration |
| `openingStats` | two labels, two numbers, contrast line | 30-40s |
| `unitEcon` | cost/revenue row data | 45-75s |
| `paperTrailSummary` | 2-3 key figures | 25-30s static |
| `informalFlow` | node labels, arrow sequence | 40-60s |
| `macroRipple` | block labels, sequence order | 50-70s |
| `outlook` | path label, icon, timeline string × 3 | 40-50s |

---

## Global production notes
- Every on-screen number has a `sourceCaption`. Any `[VERIFY]` figure confirmed
  from primary source before the graphic is rendered.
- Source caption format: publication/institution, year — Inter font, 11px,
  bottom-right corner, white at 60% opacity. Present for as long as the
  number is on screen.
- Music: ambient and low throughout. Drop entirely for key analytical conclusions
  so the voiceover lands clean. Resume quietly after the pause.
- Colour language is consistent across all episodes:
  green = positive, viable, growing, target / red = cost, gap, risk, decline.
  Viewers should read the colour without thinking after two episodes.
- Cut rhythm: graphics should cut on a sentence end or a breath, not mid-phrase.
  The voiceover edit determines the visual cut, not the other way around.
- Export: 1080p minimum, 4K preferred. Audio: -14 LUFS integrated, -1 dBTP true peak.
