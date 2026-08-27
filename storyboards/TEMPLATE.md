# Storyboard & Visual Production Blueprint — Episode NN
## "[EPISODE TITLE]"

<!--
Timestamp-linked to scripts/NN_<slug>.md.
FACELESS FORMAT: voiceover + simple graphics + B-roll only. No on-camera host.

EDITING TOOL: CapCut only. The editor has never edited before, so every cue must
describe something buildable directly in CapCut — a footage clip, a text layer,
an image layer, a simple shape — animated with a single one-tap preset (fade in/
out, slide in/out, zoom in/out). Never a hand-keyframed or multi-element build.
No Remotion, no After Effects, no custom-coded motion graphics.

Two cue types, always labelled:
  FOOTAGE = a B-roll clip added at this cue
  GRAPHIC = either a SOURCE-SCREENSHOT CARD (a screenshot of the real source
            document/article, cropped, with a highlight box over the key figure
            and a "Source: ..." caption — the default) or a PLAIN TEXT/NUMBER
            CARD (Archivo Black number + Inter label on the palette background,
            used only when no source document exists to screenshot)

FOOTAGE IS THE DEFAULT VISUAL LAYER. Most of an episode's runtime should be
footage the editor can drop onto the timeline. Reserve GRAPHIC cues for the
handful of moments that genuinely need a number on screen — not one graphic per
statistic. A storyboard that is mostly graphics is wrong for this editor.

Footage must be topic-specific to the scene being narrated at that moment, not
generic filler — search with terms drawn from the specific scene, not just the
episode's general subject.

Every cue entry must include:
  - Timecode in and out (mm:ss - mm:ss)
  - Type: GRAPHIC or FOOTAGE, plus GRAPHIC sub-type (source-screenshot / text card)
  - What appears: the specific shot, or the specific text/screenshot content
  - Animation: the single CapCut preset used (or "none" for footage played as-is)
  - Source caption text, where applicable
  - Duration of the cue

Voiceover runs continuously. Visuals cut to match the prose, not the other way
around.

STRUCTURE: check the companion script's front-matter first. Most scripts use
structure_type: flexible with `## Part N — [Name]` headings, and the number
of Parts is whatever the script's section_count says — three, four, five,
six, or more, not a fixed five. The five `## Part` blocks below are a single
worked example (based on legacy Template A's section names and a ~15-minute
runtime) showing the cue-level format expected in every Part. Copy the
format, not the count: add or remove Part blocks to match the actual script,
rename each Part after the script's own Part names, and retime every cue
against the script's actual timestamps and estimated_duration rather than
the 0:00-15:00 range used here. Only a script with structure_type:
legacy-A/B/C should keep exactly five Sections named to match that template.
-->

**Voiceover:** ~150 wpm, documentary register. Recorded clean, no music bleed.
**Canvas:** 1920x1080. Background: off-white `#F8F9FA`. Card fill: white `#FFFFFF` with drop shadow.
**Palette:** text `#1A1A1A` · captions `#555555` · green `#1EB53A` · red `#D32F2F` · border `#E0E0E0`.
**Type:** Archivo Black for numbers and titles · Inter for body, captions, definitions.
**Source captions:** Inter 11px, `#555555`, bottom-right, visible for the full duration any number is on screen. Format: "Source: [Institution/Publication], [Date]".
**Assembly:** import footage clips into CapCut, add source-screenshot/text-card images as image layers, apply one-tap animation presets, add voiceover, captions, and music.
**Music:** low ambient score under footage and graphics; drop entirely for key analytical lines; silent under the cold open.

---

## Part 1 — The Unsolved Reality (0:00 - 2:00)

**[0:00 - 0:12] FOOTAGE — cold open**
- Shot: [a specific, topic-related scene — a real location, object, or activity that opens the question. Search terms should name the actual subject, not "generic establishing shot."]
- Source: [Pexels/Pixabay]; licence type; fallback if unavailable
- Animation: none — footage plays as-is. Sound: ambient only, no music, no voiceover.
- Duration: 12s

**[0:12 - 0:35] GRAPHIC — source-screenshot card: the core figure**
- Type: source-screenshot card
- Visual: screenshot of [the actual source document/page], cropped to the sentence or chart containing the key figure; highlight box over the figure.
- Source caption: "Source: [Institution/Publication], [Date]"
- Animation: zoom-in (CapCut preset)
- Duration: 23s

**[0:35 - 1:20] FOOTAGE — consequence scene**
- Shot: [the real-world consequence the voiceover is describing — specific, not generic]
- Animation: none. Voiceover continues over footage.
- Duration: ~45s

**[1:20 - 1:35] GRAPHIC — title card (text card)**
- Type: plain text card
- Visual: episode title, Archivo Black, large. One keyword in green or red accent. Sub-caption below, one line, Inter.
- Animation: fade-in
- Music lifts to full ambient level.
- Duration: 15s

**Transition to Part 2:** hard cut at 2:00.

---

## Part 2 — The Paper Trail (2:00 - 6:00)

**[2:00 - 2:40] GRAPHIC — source-screenshot card: first key figure**
- Type: source-screenshot card
- Visual: screenshot of [source document], highlight box over the figure the voiceover just stated.
- Source caption: "Source: [Institution], [Date]"
- Animation: fade-in
- Duration: 40s

**[2:40 - 3:10] GRAPHIC — text card: term definition**
- Type: plain text card
- Visual: term (Archivo Black) + one-line plain-English definition (Inter) below it.
- Animation: fade-in
- Duration: 30s

**[3:10 - 4:10] FOOTAGE — illustrative B-roll**
- Shot: [specific scene illustrating the mechanic being described — e.g. the actual type of location, activity, or object named in this part of the script]
- Animation: none. Voiceover continues.
- Duration: ~60s

**[4:10 - 4:50] GRAPHIC — source-screenshot card: second figure**
- Type: source-screenshot card
- Visual: [second cited document/page, cropped and highlighted]
- Source caption: "Source: [Institution], [Date]"
- Animation: zoom-in
- Duration: 40s

**[4:50 - 6:00] FOOTAGE — second illustrative scene**
- Shot: [a different specific scene continuing the mechanic]
- Animation: none.
- Duration: ~70s

**Transition to Part 3:** hard cut at 6:00.

---

## Part 3 — The Field Reality (6:00 - 10:00)

**[6:00 - 6:45] FOOTAGE — ground-level scene**
- Shot: [specific real-world location or activity relevant to this part]
- Duration: ~45s

**[6:45 - 7:25] GRAPHIC — text card: two-item comparison**
- Type: plain text card (used because this comparison is the channel's own
  ANALYSIS, not from a single source document)
- Visual: two figures side by side, labelled, no chart — just two stat blocks.
- Animation: fade-in on each side in sequence (two simple fades, not a build)
- Duration: 40s

**[7:25 - 8:25] FOOTAGE — second ground-level scene**
- Shot: [a different specific location/activity]
- Duration: ~60s

**[8:25 - 9:10] GRAPHIC — source-screenshot card: third figure**
- Type: source-screenshot card
- Visual: [source document, cropped and highlighted]
- Source caption: "Source: [Institution], [Date]"
- Animation: fade-in
- Duration: 45s

**[9:10 - 10:00] FOOTAGE — closing scene for this Part**
- Shot: [specific scene that closes this part's argument]
- Duration: ~50s

**Transition to Part 4:** hard cut at 10:00.

---

## Part 4 — The Systemic Domino Effect (10:00 - 13:00)

**[10:00 - 11:00] FOOTAGE — sequence of consequence scenes**
- Shot: [2-3 short specific clips, cut on the voiceover's list of consequences — each clip 15-20s]
- Duration: 60s

**[11:00 - 11:45] GRAPHIC — source-screenshot card: the macro figure**
- Type: source-screenshot card
- Visual: [the document behind the episode's central macro figure]
- Source caption: "Source: [Institution], [Date]"
- Animation: zoom-in
- Duration: 45s

**[11:45 - 13:00] FOOTAGE — macro consequence scene**
- Shot: [a specific visual representing the economy-wide/system-wide consequence]
- Duration: ~75s

**Transition to Part 5:** hard cut at 13:00.

---

## Part 5 — The Verdict & Future Outlook (13:00 - End)

**[13:00 - 13:10] GRAPHIC — text card: forward question**
- Type: plain text card
- Visual: single line, "[THE FORWARD QUESTION?]"
- Animation: fade-in. Music drops slightly.
- Duration: 10s

**[13:10 - 13:55] GRAPHIC — text card: forward paths**
- Type: plain text card
- Visual: 2-3 short labelled lines (not an animated build) — each path named
  with one status word (underway / possible / uncertain).
- Animation: fade-in
- Duration: 45s

**[13:55 - 14:30] FOOTAGE — closing scene**
- Shot: [a scene that mirrors or resolves the opening — specific, real]
- Duration: 35s

**[14:30 - 14:50] GRAPHIC — end card**
- Type: plain text card
- Visual: channel name, subscribe prompt, next-episode tease line.
- Animation: fade-in. Music fades out.
- Duration: 15-20s

---

## Global production notes

- Source captions: Inter 11px, `#555555`, bottom-right corner, visible for the
  full duration any figure is on screen. Format: "Source: Institution, Year."
- `[VERIFY]` figures must be resolved, or the on-screen card must carry a small
  "VERIFY" tag — do not present an unresolved figure as confirmed fact on screen.
- Music: ambient and low throughout. Drop entirely for key analytical
  conclusions so the voiceover lands clean. Resume quietly after the pause.
- Colour language is consistent across all episodes: green = positive,
  viable, growing, target / red = cost, gap, risk, decline. Viewers should
  read the colour without thinking after two episodes.
- Cut rhythm: cuts should land on a sentence end or a breath, not mid-phrase.
  The voiceover edit determines the visual cut, not the other way around.
- Animation: one CapCut preset per layer, applied with a single tap. Never
  stack multiple animations on one layer, never hand-keyframe.
- Export: 1080p minimum, 4K preferred. Audio: -14 LUFS integrated, -1 dBTP true peak.
