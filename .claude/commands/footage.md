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

### Step 3 — Write the footage-rights register

File: `research/source-registers/NN_slug_sources.csv`

Headers:
```
clip_id,description,timestamp,source,licence_type,licence_url,commercial_ok,cleared,fallback,notes
```

One row per footage cue. `cleared` values: yes / no / pending.

### Step 4 — Flag and resolve unclear licences

Flag any clip where:
- The licence is ambiguous or the terms page is inaccessible.
- The clip is from a news broadcast, airline, or company promotional source.
- The licence is Creative Commons but requires attribution not given.
- The clip requires a paid licence that has not been purchased.

For each flagged clip, apply the fallback hierarchy:
1. Remotion motion graphic
2. Text card on channel palette
3. Self-captured equivalent footage

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
