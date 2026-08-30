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
  ANGLE_TEMPLATE.md         Blank angle selection form — fill before research begins
  angles/                   NN_slug_angle.md — one completed, approved angle per episode
research/
  briefs/                   NN_slug_brief.md — full research briefs per episode
  claim-ledgers/            NN_slug_claims.csv — claim-by-claim classification
  source-registers/         NN_slug_sources.csv — all sources + footage rights
  audits/                   NN_slug_research-audit.md — source audit per final script
  verification-queues/      NN_slug_verification-queue.md — actionable to-do list from an audit's open claims
  footage-queues/           NN_slug_footage-queue.md — actionable to-do list from unresolved footage cues
scripts/
  TEMPLATE.md               Script skeleton — flexible Part-N structure (default)
  script_engine.py          CLI scaffolder for the optional legacy Template A/B/C skeleton only
  NN_*.md                   Production scripts — pure voiceover prose
storyboards/
  TEMPLATE.md               Visual production plan template (flexible Part-N, cue-level detail)
  NN_*_visuals.md           Visual direction for editors — one per episode
delivery-notes/
  NN_*_delivery-notes.md    Optional narrator performance markup (emphasis/pause/pace), never the script itself
prompts/
  NN_*_thumbnails.md        Thumbnail specs and Canva design briefs (not yet populated)
docs/
  editorial/                Prose, storytelling, structure, and visual-system guidance
  footage-guidelines.md     Copyright and licence rules for B-roll footage
tools/
  topic_generator.py        Idea and starting-research-scaffold generator by pillar
  validate_script.py        Thin wrapper — delegates to the canonical validator in
                             .claude/skills/pakistan-documentary-production/scripts/
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

Alternatively, use the CLI tool to generate a starting research scaffold
(not a finished brief — still needs claim classification, a claim ledger,
and a source register before it can support scripting):

```bash
python3 tools/topic_generator.py brief --title "K-Electric: The Karachi Power Trap" --pillar macro
```

### Step 3 — Research brief → script (`/write-script`)

Once the research brief is complete, invoke `/write-script`. Claude classifies
the story logic (causal, financial, institutional, comparative, and so on),
proposes a number and names of `## Part N —` sections sized to what the story
actually needs — three, four, five, six, or more, never a default — and
**stops for your approval** before writing the full script.

```
/write-script
```

The five-section `## SECTION N —` format (legacy Template A / B / C) is
available only when explicitly requested or when a topic fits it cleanly. To
scaffold that legacy skeleton manually instead of using `/write-script`'s
flexible structure:

```bash
# Template A (Macro/Institutions)
python3 scripts/script_engine.py --title "K-Electric" --template A --number 11 --pillar macro

# Template B (Company Case Study)
python3 scripts/script_engine.py --title "Interloop: Pakistan's Sock Empire" --template B --number 12

# Template C (Structural/History)
python3 scripts/script_engine.py --title "The Remittance Engine" --template C --number 13
```

There is no CLI scaffolder for the flexible structure — `/write-script`
writes it directly once you approve the proposed Part structure.

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

The validator checks mechanical/structural things only: the declared
`section_count` matches the actual `## Part N —` headings, front-matter
completeness, a populated Sources block, no visual cues or delivery-notes
markup inside the script, no banned clichés or banned formulaic transitions,
political-framing patterns, paragraph rhythm, sourcing density, `[VERIFY]`
count, and more. It does not judge hook quality or factual accuracy — that's
`/review-script`.

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

## Script structure

The default is a **flexible structure**: `/write-script` classifies the
story logic (causal, chronological, financial, institutional, comparative,
operational, regulatory, company case study, decision-focused, or
structural/historical) and proposes as many `## Part N —` sections as that
logic actually needs, then stops for approval before writing. Do not default
to five sections — the count must be justified by the story, not a template.

### Legacy five-section templates (optional)

Available only when explicitly requested or when a topic fits one of these
three cleanly. Legacy scripts use `## SECTION N —` headings instead of
`## Part N —`.

| Template | Use for | Sections 2 / 3 / 4 |
|----------|---------|---------------------|
| **A** — Macro / Institutions | SOEs, energy, policy, monetary/fiscal, regulation | Paper Trail → Field Reality → Systemic Domino Effect |
| **B** — Company Case Study | Named companies, corporate strategy, sector leaders | Business Model → Operational Reality → Competitive Position |
| **C** — Structural / History | Long-cycle stories, historical investigations, debt cycles | The Origin → How It Plays Out → The Structural Risk |

Sections 1 (The Anomaly) and 5 (The Verdict) are the same for all three legacy templates.

---

## Key rules (quick reference)

| Rule | Detail |
|------|--------|
| Scripts are narration only | No `[VISUAL]`, `[FOOTAGE]`, camera, or editing directions |
| Storyboards hold all visuals | Every shot, graphic, and on-screen text goes there |
| Delivery notes are separate too | Narrator emphasis/pause/pace markup lives only in `delivery-notes/`, never in the script |
| Angle approval required | No research or scripting before the user approves an angle |
| Research must precede scripting | No script without a completed research brief |
| Structure is flexible, not fixed | `/write-script` proposes the Part count the story logic needs — never a default five |
| Neutral, non-political framing | Decisions described in administrative/economic terms, not political strategy |
| Plain, everyday language | Every sentence should be followable by an eighth-grade student or small shop owner |
| Public availability ≠ copyright | Every footage clip needs a documented licence |
| No fabrication | Never invent characters, scenes, conversations, or motives |
| Verify before recording | Re-check all `[VERIFY]` and macro figures before the session |

---

## Episode reference

Reflects what actually exists in this repo, not an aspirational target.

| Ep | Topic | Script | Storyboard | Audit | Delivery notes |
|----|-------|--------|------------|-------|-----------------|
| 01 | Pakistan Railways freight | draft only, incomplete | — | — | — |
| 11 | Pakistan Steel Mills | ✓ | ✓ | ✓ | — |
| 12 | Metro Bus subsidy | ✓ | — | — | — |
| 13 | Gwadar vs. Karachi port | ✓ | — | — | ✓ |
| 14 | Power/gas circular debt | ✓ | — | — | — |
| 15 | Shaukat Khanum funding | ✓ | ✓ | ✓ | — |
| 16 | Pakistan tax system | ✓ | — | — | — |

Episodes 12, 13, 14, and 16 still need `/storyboard` and `/audit-sources`.
Episode 01's script file is not a usable draft — a research brief and claim
ledger exist, but the script needs to be (re)written before this episode can
proceed. See `.claude/rules/visual-system.md` for the palette (episodes
01–05 archived dark `#0A0A0A`; episode 06+ light `#F8F9FA` — episode 01
predates any storyboard in this repo, so it has not been assigned a palette).

---

## Available slash commands

| Command | What it does |
|---------|-------------|
| `/angles` | Generate and score angle options; recommend one; stop for approval |
| `/research` | Build research brief, claim ledger, and source register |
| `/write-script` | Propose a flexible Part structure, then write the complete voiceover script |
| `/review-script` | Audit the script for structural and editorial compliance |
| `/audit-sources` | Verify source behind every major claim; create audit file |
| `/storyboard` | Create the visual production plan |
| `/footage` | Verify footage licences; create rights register |
