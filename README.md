# Pakistan Business & Economy — YouTube Production Pipeline

An end-to-end execution framework for a high-production, English-language YouTube
channel analyzing **Pakistan's business ecosystem, macroeconomics, corporate
strategy, and economic mechanics.** This repository is the media engine: it takes a
topic from raw idea through angle selection, research, scripting, storyboarding,
and footage clearance to a production-ready package.

The editorial constitution lives in **[`CLAUDE.md`](CLAUDE.md)** and governs
everything produced here. Read it first.

---

## Repository structure

```
CLAUDE.md                   Editorial constitution — governs every file
README.md                   This file
requirements.txt            Python dependencies (Jinja2, rich)
.gitignore                  Excludes /media/, *.mp4, *.mov, *.wav
.claude/
  rules/                    Path-scoped rules for scripts, research, storyboards, etc.
  skills/                   The pakistan-documentary-production skill
  commands/                 Slash commands: /angles /research /write-script etc.
  agents/                   Specialised agents: researcher, script-editor, etc.
topics/
  ANGLE_TEMPLATE.md         Angle selection form — fill before research begins
  *.md                      Research briefs and topic ideas
research/
  briefs/                   NN_slug_brief.md — full research briefs per episode
  timelines/                NN_slug_timeline.md — chronological source timelines
  claim-ledgers/            NN_slug_claims.csv — claim-by-claim classification
  source-registers/         NN_slug_sources.csv — all sources + footage rights
  audits/                   NN_slug_research-audit.md — source audit per final script
scripts/
  TEMPLATE.md               Three-template script skeleton (A / B / C)
  script_engine.py          CLI scaffolder: generates skeleton with correct section names
  NN_*.md                   Production scripts — pure voiceover prose
storyboards/
  TEMPLATE.md               Visual production plan template
  NN_*_visuals.md           Visual direction for editors — one per episode
prompts/
  NN_*_thumbnails.md        Thumbnail specs and Midjourney prompts
docs/
  footage-guidelines.md     Copyright and licence rules for B-roll footage
tools/
  topic_generator.py        Research brief generator by pillar
  validate_script.py        Script compliance checker
remotion/
  src/Root.tsx              Remotion motion-graphic compositions
  data/epNN_data.json       Per-episode animation data
```

---

## Setup

Requires Python 3.9+.

```bash
pip install -r requirements.txt
```

---

## The production workflow

Every episode follows this exact sequence. **No step may be skipped.**

### Step 1 — Broad topic → angle options (`/angles`)

A broad topic must never go directly to scripting.

Invoke `/angles` with a topic. Claude will generate 6–10 scored angle options,
recommend one, and **stop for your approval**.

```
/angles K-Electric
```

No research brief or script may begin until you have explicitly approved one angle.

### Step 2 — Approved angle → research brief (`/research`)

Once an angle is approved, invoke `/research`. This creates:

- `research/briefs/NN_slug_brief.md` — full research brief
- `research/claim-ledgers/NN_slug_claims.csv` — claim-by-claim classification
- `research/source-registers/NN_slug_sources.csv` — all sources consulted

```
/research
```

**Claude searches live sources before writing.** It does not use training-data
memory for current statistics. Every claim is classified:
VERIFIED / REPORTED / ANALYSIS / ESTIMATE / UNRESOLVED.

Alternatively, use the CLI tool to scaffold a brief:

```bash
python3 tools/topic_generator.py brief --title "K-Electric: The Karachi Power Trap" --pillar macro
```

### Step 3 — Research brief → script (`/write-script`)

Once the research brief is complete, invoke `/write-script`. Claude selects the
correct template and writes complete five-section voiceover prose.

```
/write-script
```

Or scaffold a skeleton manually:

```bash
# Template A (Macro/Institutions)
python3 scripts/script_engine.py --title "K-Electric" --template A --number 11 --pillar macro

# Template B (Company Case Study)
python3 scripts/script_engine.py --title "Interloop: Pakistan's Sock Empire" --template B --number 12

# Template C (Structural/History)
python3 scripts/script_engine.py --title "The Remittance Engine" --template C --number 13
```

**Script rules (non-negotiable):**
- Scripts are pure voiceover prose — no visual directions inside script files.
- All visual direction lives in the companion storyboard file.
- Every statistical claim cites `[SOURCE: publication, year]`.
- Every concept, figure, and definition is stated once — no repetition.

### Step 4 — Script review (`/review-script`)

```
/review-script scripts/11_slug.md
```

Or run the automated validator:

```bash
python3 tools/validate_script.py scripts/11_slug.md
```

The validator checks: five sections, Sources block, no visual cues inside the
script, no banned clichés, sourcing density, [VERIFY] count, and more.

### Step 5 — Source audit (`/audit-sources`)

For every final script, verify the exact source behind every major claim.

```
/audit-sources scripts/11_slug.md
```

Creates `research/audits/11_slug_research-audit.md`. No script may be marked
`production-ready` until every claim is Confirmed or Removed.

### Step 6 — Storyboard (`/storyboard`)

Create the visual production plan for the approved script.

```
/storyboard scripts/11_slug.md
```

Creates `storyboards/11_slug_visuals.md`. The storyboard translates script
timestamps into motion-graphic, B-roll, on-screen text, and chart directions.
**It never modifies the script.**

### Step 7 — Footage rights (`/footage`)

Verify licences for every B-roll cue in the storyboard.

```
/footage storyboards/11_slug_visuals.md
```

Updates `research/source-registers/11_slug_sources.csv` with cleared/pending status.
**Public availability is not copyright permission.** Every clip needs a documented licence.

### Step 8 — Final validation

```bash
python3 tools/validate_script.py scripts/11_slug.md
```

Script is production-ready when:
- Validator exits with PASS.
- Source audit is complete (all claims Confirmed or Removed).
- All footage cues are cleared (no "pending" entries).
- All `[VERIFY]` figures have been re-checked against current sources.

---

## Three content templates

| Template | Use for | Sections 2 / 3 / 4 |
|----------|---------|---------------------|
| **A** — Macro / Institutions | SOEs, energy, policy, monetary/fiscal, regulation | Paper Trail → Field Reality → Systemic Domino Effect |
| **B** — Company Case Study | Named companies, corporate strategy, sector leaders | Business Model → Operational Reality → Competitive Position |
| **C** — Structural / History | Long-cycle stories, historical investigations, debt cycles | The Origin → How It Plays Out → The Structural Risk |

Sections 1 (The Anomaly) and 5 (The Verdict) are the same for all templates.

---

## Key rules (quick reference)

| Rule | Detail |
|------|--------|
| Scripts are narration only | No `[VISUAL]`, `[FOOTAGE]`, camera, or editing directions |
| Storyboards hold all visuals | Every shot, graphic, and on-screen text goes there |
| Angle approval required | No research or scripting before the user approves an angle |
| Research must precede scripting | No script without a completed research brief |
| Public availability ≠ copyright | Every footage clip needs a documented licence |
| No fabrication | Never invent characters, scenes, conversations, or motives |
| Verify before recording | Re-check all `[VERIFY]` and macro figures before the session |

---

## Episode reference (complete packages)

| Ep | Script | Storyboard | Prompts |
|----|--------|------------|---------|
| 01 | ✓ | ✓ | ✓ |
| 02–05 | ✓ | ✓ | ✓ |
| 06 | ✓ | ✓ | ✓ |
| 07 | ✓ | ✓ | — |
| 08–10 | ✓ | — | — |

Episodes 01–05 storyboards and prompts use the old dark palette (`#0A0A0A`).
Episodes 06+ use the current light palette (`#F8F9FA`). See `.claude/rules/visual-system.md`.

---

## Available slash commands

| Command | What it does |
|---------|-------------|
| `/angles` | Generate and score angle options; recommend one; stop for approval |
| `/research` | Build research brief, claim ledger, and source register |
| `/write-script` | Write the complete five-section voiceover script |
| `/review-script` | Audit the script for structural and editorial compliance |
| `/audit-sources` | Verify source behind every major claim; create audit file |
| `/storyboard` | Create the visual production plan |
| `/footage` | Verify footage licences; create rights register |
