# /footage

Verify footage licences and create a footage-rights register. Never assume public
availability means reuse permission.

## Before running

1. Read `CLAUDE.md`.
2. Read `.claude/rules/footage-rights.md`.
3. Identify the episode number and slug.
4. Confirm the storyboard exists: `storyboards/NN_slug_visuals.md`.

## What to do

### Step 1 — Extract all footage cues from the storyboard

List every B-roll or footage cue by section and timestamp.

### Step 2 — Check each clip

For each footage cue:
1. Identify the source library or origin.
2. Confirm the exact licence on the specific clip (not the platform's general policy).
3. Confirm whether the licence permits:
   - Commercial use (YouTube monetisation)
   - Use without attribution, or attribution required
   - Use in modified / edited form
4. Record the licence URL (the specific page for that clip, not the library homepage).

### Step 3 — Write the footage-rights register and footage-queue tickets

Add one row per footage cue to `research/source-registers/NN_slug_sources.csv`,
using that file's existing header: `source_id,title,institution,date,url,tier,notes`
(footage rows use `F001`, `F002`... as the `source_id`, matching the storyboard's
clip IDs — do not introduce a different column schema; this file also holds every
research source for the episode and must stay one consistent shape). Record in the
`notes` field: what was directly fetched and confirmed (licence terms, content
description), what's still unconfirmed (an actual watch-through), the storyboard
cue it belongs to, and its fallback.

Then write `research/footage-queues/NN_slug_footage-queue.md` using the F-XXX
ticket format in `.claude/rules/verification-queue.md` (see
`research/footage-queues/11_pakistan_steel_mills_footage-queue.md` for a worked
example) — one ticket per cue, ending with a Handoff Summary that gives the
editor a priority-ordered watch-through list.

`cleared` status per clip: CANDIDATE (licence type and content description
confirmed via a direct page fetch, but no human watch-through yet) → EDITOR
VERIFIED (a human has watched the full clip and confirmed both content and
licence). Never mark a clip cleared on a page description or search snippet
alone — per `.claude/rules/research.md`, that is not final evidence.

### Step 4 — Flag and resolve unclear licences

Flag any clip where:
- The licence is ambiguous or the terms page is inaccessible.
- The clip is from a news broadcast, airline, or company promotional source.
- The licence is Creative Commons but requires attribution not given.
- The clip requires a paid licence that has not been purchased.

For each flagged clip, apply the fallback hierarchy in
`.claude/rules/footage-rights.md`:
1. A source-screenshot card (see `.claude/rules/visual-system.md`), if the cue
   was standing in for a citable figure or document.
2. A plain text card on the channel's colour palette.
3. Self-captured equivalent footage.

Remotion is not part of this fallback hierarchy — it's a legacy, optional
pipeline (see `.claude/rules/visual-system.md`) and should only be used if the
user explicitly asks for it on a specific episode.

Update the storyboard's B-roll cue to reflect the fallback if the original clip
cannot be cleared.

## Approved sources (no further verification needed if licence is confirmed on each clip)

- Pexels (CC0 confirmed per clip)
- Pixabay (CC0 confirmed per clip)
- Videvo CC0 section (filter to CC0 only)

## Never use without clearance

- Pakistan TV network clips (Geo, ARY, Hum, Dawn News, GNN)
- Airline promotional footage (PIA, Emirates, etc.)
- Company promotional videos
- News broadcast excerpts from any outlet
- Music without content-ID-safe licence

## After this command

No footage cue should have `cleared: pending` when the episode enters production.
Report the total count of: cleared clips / replaced with fallback / pending.
