# /write-script

Write a complete voiceover script from an approved angle and research brief.

## Before writing

Do not write the script until all of the following are confirmed:

1. Read `CLAUDE.md` in full.
2. Read `.claude/rules/scripts.md`.
3. Read the approved angle from `topics/ANGLE_TEMPLATE.md` (`approval_status: approved`).
4. Read the research brief from `research/briefs/NN_slug_brief.md`.
5. Read the claim ledger from `research/claim-ledgers/NN_slug_claims.csv`.
6. Confirm no UNRESOLVED claims exist without `[VERIFY]` tags.
7. If any of these are missing, stop and redirect to the appropriate prior step.

## Structure selection — stop before writing

After reading the research:

1. Identify the central question.
2. Identify the thesis or proposition.
3. Classify the story logic:
   - Causal
   - Chronological
   - Financial
   - Comparative
   - Institutional
   - Operational
   - Regulatory
   - Company case study
   - Decision-focused
   - Structural or historical
4. Propose the number and names of sections.
5. For each section, state its distinct purpose.
6. Explain why this structure fits the approved angle.
7. Identify the evidence that will anchor each section.
8. Flag any sections where evidence is thin or a [VERIFY] item is load-bearing.

**Stop here. Present the proposed structure and wait for explicit approval.**

Do not write the full script until the structure is approved.

## After structure approval

Write a complete narration-only script using the approved number and section names.

Save to: `scripts/NN_slug.md`

Use the YAML front-matter from `scripts/TEMPLATE.md`. Set `status: draft`.

### Script rules

- Pure voiceover prose only — no `[VISUAL]`, `[FOOTAGE]`, or production direction.
- All visual direction belongs in the companion storyboard file.
- Cite inline: `[SOURCE: publication/institution, year]`.
- Tag unconfirmed figures: `[VERIFY]`.
- Label analysis: "this suggests" / "this implies" / "the evidence points to".
- State every concept, figure, and definition exactly once. One-clause callbacks only.
- No em dashes where a comma or period will do.
- No banned clichés (game-changer, synergy, disrupt, journey, etc.).
- No invented characters, scenes, conversations, or motives.
- The opening section must be grounded in a documented event or anomaly.
- Land the hook in the first one or two sentences — the strongest documented
  anomaly or comparison, not several paragraphs of setup. See
  `docs/editorial/storytelling.md`, "Land the hook fast."
- Immediately after the hook, include a two-to-three sentence retention bridge
  previewing what the episode investigates, before widening into the full
  documentary chain. See `docs/editorial/storytelling.md`, "Retention bridge."
- The closing section must be honest and specific — name the real obstacles.

### Do not force five sections

Use as many sections as the structure approval specifies. Three, four, five, six, or
more — the number must be justified by the story logic, not by a default.

The five-section legacy format (Template A / B / C) is available only when explicitly
requested or when the topic fits it cleanly.

## After writing

Run `/review-script` before marking the script as production-ready.
