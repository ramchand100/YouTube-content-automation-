# Remotion motion graphics (proof-of-concept)

A code-driven way to build the channel's motion-graphic scenes as React components,
rendered to MP4. This folder is a **proof of concept**: one scene from Episode 02,
Section 2 ("The Paper Trail"), the Rs2,000 card-sale fee-split, driven entirely by
JSON props.

The point: charts, counters, and captions become reusable components fed by data,
so the next episode's version is the same component with different numbers. That
fits the repo's automation goal better than redrawing each chart by hand.

## What's here

```
remotion/
  package.json            deps + scripts
  remotion.config.ts      render config (image format, browser override note)
  src/
    index.ts              registerRoot entry
    Root.tsx              registers the <Composition> (id: FeeSplit)
    theme.ts              channel palette + PKR formatter (green=free, red=fee)
    scenes/FeeSplit.tsx   the data-driven scene
    data/feeSplit.json    the numbers + source caption for this render
```

## Run it

```bash
cd remotion
npm install

# Live preview in the browser (Remotion Studio):
npm run studio

# Render a single frame (fast sanity check):
npm run still      # -> out/fee-split.png

# Render the video:
npm run render     # -> out/fee-split.mp4
```

Change the numbers in `src/data/feeSplit.json` and re-render. No code edits needed
for a new set of figures.

### Browser note for this cloud environment

Remotion normally downloads its own Chrome Headless Shell on first render. In a
sandbox with a restricted network that download can be blocked (403, host not in
allowlist). A headless shell is already installed here, so pass it explicitly:

```bash
npx remotion render FeeSplit out/fee-split.mp4 \
  --props=./src/data/feeSplit.json \
  --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
```

Or set `REMOTION_BROWSER_EXECUTABLE` to that path, or uncomment the
`setBrowserExecutable` line in `remotion.config.ts`. Note: it must be the
**chrome-headless-shell** binary, not full Chrome (Remotion uses old-headless flags
that full Chrome has removed). On a normal machine none of this is needed.

Verified in this environment: a 10-second 1080p render completed in ~21 seconds.

## Fonts

The scene uses a bold system fallback stack. For the real channel look, load
Coolvetica / Archivo Black via `@remotion/fonts` (local file) or
`@remotion/google-fonts` (Archivo Black), then set it in `theme.ts`.

## Where Remotion fits, and where it doesn't

**Good fit (use it here):**
- Data-driven motion graphics: counters, bar charts, fee splits, maps, lower-thirds,
  source captions. Reusable components fed by JSON, version-controlled, reproducible.

**Not a fit (keep Premiere/After Effects):**
- Cutting real footage (drone shots, shop-counter B-roll), layering SFX and music,
  color grading, and final assembly. Remotion composites video but is not an editor.
- Voiceover: record the human VO as before and feed Remotion a finished audio file;
  it will not cut dead air, and visual-to-VO timing is managed by hand.

**Costs to know:**
- Rendering is frame-by-frame via headless Chrome. Short graphic scenes are fast; a
  full 12-16 min 4K video is heavy on one machine (parallelize on Remotion Lambda if
  needed, at AWS cost).
- Requires React/TypeScript, a different skillset from a timeline editor.
- Licensing: Remotion is free for individuals and small teams but needs a paid
  company license above a certain size. Check current terms before commercial use.

## Recommended workflow

Hybrid. Build the motion-graphic scenes and the reusable data components here in
Remotion, export them, then assemble with the footage, voiceover, SFX, and grade in
Premiere for the final cut. Bridge any bespoke After Effects animation in via Lottie
if needed.
