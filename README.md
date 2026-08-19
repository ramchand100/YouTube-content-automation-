# Pakistan Business & Economy — YouTube Production Pipeline

An end-to-end execution framework for a high-production, English-language YouTube
channel analyzing **Pakistan's business ecosystem, macroeconomics, corporate
strategy, and economic mechanics.** This repository is the media engine: it takes a
topic from raw idea to a research brief, to a full-length script, to an editor-ready
storyboard and thumbnail package.

The editorial constitution lives in **[`CLAUDE.md`](CLAUDE.md)** and governs
everything produced here (language, tone, length, sourcing, and the Investigative
Brief structure). Read it first.

---

## Repository structure

```
CLAUDE.md            Editorial constitution — rules every file must follow
topics/              Staging area: video ideas & deep research briefs
scripts/             Production-ready full-length English scripts + the scripting engine
storyboards/         Visual & motion-graphic blueprints for editors (timestamp-linked)
prompts/             Midjourney visual prompts & thumbnail layout specs
tools/               Automation scripts + requirements.txt
```

---

## Setup

Requires Python 3.9+.

```bash
pip install -r tools/requirements.txt
```

Dependencies: `Jinja2` (templating) and `rich` (readable CLI output; the tools
still run without it).

---

## The pipeline, end to end

The workflow moves left to right. Each stage has a tool or a template.

### 1. Pick a topic and generate a research brief  →  `topics/`

List the four content pillars:

```bash
python3 tools/topic_generator.py list
```

See research angles for a pillar (`startup`, `seth`, `macro`, `brands`):

```bash
python3 tools/topic_generator.py ideas --pillar macro
```

Promote an angle to a full research brief (written into `topics/`):

```bash
python3 tools/topic_generator.py brief --title "Raast vs The Card Networks" --pillar macro
```

The brief is pre-wired to the Investigative Brief structure and to a Pakistani-source
data checklist (SBP, PBS, FBR, SECP, PSX, and credible local reporting). **Fill it
with sourced facts before writing the script.**

### 2. Scaffold the full-length script  →  `scripts/`

Generate a production-ready script skeleton with enforced word budgets, timestamps,
visual-cue slots, and citation slots:

```bash
python3 scripts/script_engine.py --title "Raast vs The Card Networks" --pillar macro --number 02
```

This writes `scripts/02_raast_vs_the_card_networks.md`. Write each of the five
sections to its word budget, sourcing every figure. See `scripts/TEMPLATE.md` for
the bare structure. Target length: **1,800-2,500 words (~12-16 min voiceover).**

### 3. Build the storyboard  →  `storyboards/`

Create `storyboards/NN_<slug>.md` mapping each `[VISUAL mm:ss]` cue in the script to
concrete After Effects / Premiere directions (motion specs, chart overlays, map
animations, split-screens, reusable pre-comps). Use
`storyboards/01_real_estate_visuals.md` as the reference standard.

### 4. Package the thumbnails  →  `prompts/`

Create `prompts/NN_<slug>_thumbnails.md` with 2 high-CTR concepts and Midjourney
prompts. Follow the rules in `prompts/01_real_estate_thumbnails.md`: black-based
palette, green/white text, one focal point, 2-4 words that add a new idea rather
than repeat the title.

---

## Episode 01 (complete reference package)

A full, finished example of the pipeline output:

- **Script:** [`scripts/01_pakistan_real_estate_trap.md`](scripts/01_pakistan_real_estate_trap.md)
  — "The $500 Billion Trap: Why Pakistan's Wealth Is Locked in Real Estate"
  (~2,150 spoken words, fully cited).
- **Storyboard:** [`storyboards/01_real_estate_visuals.md`](storyboards/01_real_estate_visuals.md)
- **Thumbnails:** [`prompts/01_real_estate_thumbnails.md`](prompts/01_real_estate_thumbnails.md)
- **Research brief:** [`topics/the_500_billion_dollar_real_estate_trap.md`](topics/the_500_billion_dollar_real_estate_trap.md)

> Note: Episode 01 was produced under the earlier five-part narrative structure.
> The current standard is the Investigative Brief structure (CLAUDE.md section 7),
> which all new episodes use.

---

## Maintenance rules

1. **`CLAUDE.md` is law.** If a script drifts from its language, sourcing, or
   structure rules, fix the script, not the rules (unless the editorial standard has
   genuinely changed).
2. **Plain but smart.** Write at a grade 7-8 reading level, define all jargon on
   first use, and keep the analytical depth (CLAUDE.md section 2). Simple words,
   hard ideas. Applies to Episode 03 onward; Episodes 01-02 predate this rule.
3. **Number files consistently.** `NN_<slug>` across `scripts/`, `storyboards/`, and
   `prompts/` so an episode's three files sort together.
4. **Re-verify `[VERIFY]` figures before recording.** Macro numbers (SBP rate,
   inflation, FX, tax rates, sector values) move fast. Never record a stale figure.
5. **Every on-screen number needs a source caption.** Sourcing is the channel's
   whole competitive moat.
6. **Keep the speculation/analysis line clean.** State facts as facts, analysis as
   analysis, estimates as estimates. Never blur them.

---

## Conventions cheat-sheet

| Annotation | Meaning |
|---|---|
| `[VISUAL mm:ss — ...]` | On-screen visual cue for the editor |
| `[SOURCE: publication, year]` | Inline citation (also collected in the Sources block) |
| `[VERIFY]` | Figure must be re-checked against a current primary source before recording |
