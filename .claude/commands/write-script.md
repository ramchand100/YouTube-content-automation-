# /write-script

Write the full five-section voiceover script from approved research.

## Before running

1. Read `CLAUDE.md` in full.
2. Read `.claude/rules/scripts.md`.
3. Confirm an approved angle exists (`topics/ANGLE_TEMPLATE.md`, `approval_status: approved`).
4. Confirm a research brief exists in `research/briefs/NN_slug_brief.md`.
5. Confirm the claim ledger has no UNRESOLVED claims without `[VERIFY]` tags.
6. If any of these are missing, stop and redirect to the appropriate prior step.

## Template selection

Determine the correct template from the approved angle:
- "How does this cost or earn money?" → Template A (Macro/Institutions) or Template B (Company)
- "Why does this exist / how did we get here?" → Template C (Structural Dependency/History)

| Section | Template A | Template B | Template C |
|---------|-----------|-----------|-----------|
| 1 | The Anomaly | The Anomaly | The Anomaly |
| 2 | The Paper Trail | The Business Model | The Origin |
| 3 | The Field Reality | The Operational Reality | How It Plays Out |
| 4 | The Systemic Domino Effect | The Competitive Position | The Structural Risk |
| 5 | The Verdict | The Verdict | The Verdict |

## What to write

Write complete, production-ready voiceover prose for all five sections.

**Section 1 — The Anomaly:**
- Open on a documented, concrete anomaly (event, decision, filing, regulatory action).
- Use short, punchy sentences.
- Echo a key word or phrase across 2–3 consecutive sentences.
- Include a transitional sentence: "That [X] was not an accident."
- Close with the single central question in plain English.
- Word target: ~280–320 words.

**Sections 2–4:**
- Explain financial or structural mechanics before opinion.
- Use PKR figures where relevant.
- State every concept, figure, and definition exactly once.
- Do not repeat definitions or numbers from earlier sections.
- Label analysis explicitly: do not present it as fact.

**Section 5 — The Verdict:**
- Deliver a grounded, honest outlook.
- Name specifically what would need to change and why it has not happened.
- Name the concrete obstacles.
- State clearly who this matters to (founders, investors, professionals, students).

## Script rules

- Scripts are pure voiceover prose only.
- Do not include `[VISUAL ...]`, `[FOOTAGE ...]`, or any production direction.
- All visual direction belongs in the storyboard.
- Cite inline: `[SOURCE: publication, year]`.
- Tag unconfirmed figures: `[VERIFY]`.
- Label analysis: `[ANALYSIS]` or "this suggests" / "this implies".

## Output file

Save to: `scripts/NN_slug.md`

Use the front-matter format from `.claude/rules/scripts.md`.
Status: `draft`.

## After writing

Run `/review-script` before marking the script as production-ready.
