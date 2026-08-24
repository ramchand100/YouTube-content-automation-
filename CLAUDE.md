# CLAUDE.md — Channel Production Context & Editorial Constitution

This file is the single source of truth for this channel's production system.
When a request conflicts with this file, this file wins.

For detailed guidance, see **Section 8 — Editorial References** at the bottom.

---

## 1. The Channel

A high-production, English-language YouTube channel analyzing **Pakistan's
business ecosystem, macroeconomics, corporate strategy, and economic mechanics.**

This is not a generic clone of global case-study channels. It is an insider-driven
media engine that explains the *ground truth* of doing business in Pakistan: the
informal cash economy, Seth management culture, State Bank (SBP) regulation, FBR
tax policy, logistics and energy bottlenecks, import constraints, and local tech
adoption. The edge is authenticity and local mechanics, not surface-level summary.

---

## 2. Language and Voice

**English only.** No Urdu, Roman Urdu, or hybrid language in voiceover or
on-screen script text.

Local terms with no clean English equivalent may be used as named analytical
concepts only. Define each term in plain English the first time it appears.

**Simple words. Full analytical depth.** Write for an intelligent viewer who
knows little about finance or economics. Simplify the language, never the
analysis. If an eighth-grade student or a small shop owner could not follow the
argument on first listen, simplify the language further without cutting the
analysis. Give large or technical numbers a daily-life reference point wherever
possible — see `docs/editorial/prose-style.md`, "Relatable scale."

**No undefined jargon.** When a technical term is required, define it in plain
English immediately, then use it.

**Active voice. Concrete nouns.** Prefer visible consequences over abstract
nouns. One idea per sentence.

**Read-aloud standard.** Every paragraph must sound natural when read aloud by
a professional narrator at documentary pace. If it sounds like a written report,
rewrite it.

For detailed prose rules, see `docs/editorial/prose-style.md`.

---

## 3. Target Audience

Primary:
- Pakistani entrepreneurs and startup founders.
- Corporate professionals and mid-to-senior managers.
- University students in business, economics, finance, and engineering.

Secondary:
- Foreign investors and analysts trying to understand the Pakistani market.
- The overseas Pakistani diaspora (Gulf, UK, US, Canada).

They are intelligent and time-poor. They want mechanics and consequences, not
motivational filler. Write up to their intelligence.

---

## 4. Editorial Rules

1. **Analyze through Pakistani economic reality.** Always connect a topic to the
   real local machinery: SBP policy rate, informal cash markets, the
   documented-vs-undocumented economy, FBR tax structure and withholding regime,
   DC/FBR property valuations, import LC constraints, energy tariffs and circular
   debt, and regulatory friction. A generic framing that could apply to any
   country is a failure.
2. **No repetition within a script.** Every concept, number, and definition is
   stated once — at the point where it first matters. One-clause callbacks only.
   Never re-explain.
3. **No generic corporate clichés.** Ban phrases like "game-changer," "synergy,"
   "disrupt," and "at the end of the day" unless used precisely and critically.
4. **Data discipline.** Sources first. If a number cannot be sourced, drop it or
   label it an estimate. Never invent a statistic. The sourcing rigor is the
   competitive moat; do not spend it cheaply.
5. **Fairness and safety.** Frame around documented facts and mechanics. Present
   multiple sides on contested points. Never state an unproven allegation as fact.
   This protects credibility and the creator.
6. **Neutral, non-political framing.** Describe decisions, budgets, and
   incentives in administrative and economic terms, not as political strategy.
   Avoid election-timing, ribbon-cutting, and campaign imagery. Do not attribute
   motives to a named office-holder unless a specific claim requires it and is
   directly evidenced — name the institution and describe what it did, not why
   an individual wanted credit or blame for it. See
   `docs/editorial/prose-style.md` for worked examples.
7. **Freshness.** Macro figures (SBP rate, inflation, FX, tax rates) change fast.
   Re-verify all time-sensitive figures before recording. Do not reuse a stale
   number from an older episode.

---

## 5. Formatting & Length Rules

Scripts are **complete, un-cut, full-length production scripts.** No outlines
handed off as finished, no "[continue here]" placeholders.

- **Default length:** 1,800–2,500 words (~12–16 minutes at 150 wpm).
- **Length is set by the topic, not a quota.** Deeper topics may run to
  3,500–3,800 words (~24–26 minutes). Go long only when extra length carries
  real substance: more mechanics, more PKR math, a second case, a necessary
  piece of history. Never pad. Length must be earned, every minute of it.
- **Pure voiceover prose.** No visual cues inside the script. All visual
  direction belongs in `storyboards/NN_*.md`, the single source of truth for
  editors.
- **Inline citations:** `[SOURCE: publication, year]` collected in a Sources
  block at the end.
- **[VERIFY] tags** on any figure that moves fast or could not be fully
  confirmed. Re-check before recording.

---

## 6. Production Workflow

```
Topic
→ angle options
→ approved angle
→ story design
→ research plan
→ research
→ claim ledger
→ source audit
→ structure proposal
→ structure approval
→ first narration draft
→ fact-to-story pass
→ prose pass
→ source and freshness audit
→ storyboard
```

A documentary script is not a collection of facts. It is a controlled sequence of
discoveries. Each fact must answer a question, complicate an assumption, reveal a
mechanism, show a consequence, or prepare the next question. If the viewer can
remove a paragraph without losing the logic of the investigation, the paragraph
does not belong in the script.

---

## 7. Repository Map

- `topics/` — staging area for video ideas and research briefs (pre-production).
- `scripts/` — completed, production-ready full-length English scripts, plus the
  scripting engine (`script_engine.py`) and the script template (`TEMPLATE.md`).
- `storyboards/` — visual and motion-graphic blueprints for editors, timestamp-
  linked to the matching script.
- `delivery-notes/` — optional narrator performance markup (emphasis, pauses,
  pacing) for a script that has reached a stable draft. Never changes the
  narration itself. See `.claude/rules/delivery-notes.md`.
- `prompts/` — thumbnail layout specs and Canva design briefs for static promotional
  assets. Animated in-video graphics belong in Remotion, not Canva.
- `tools/` — automation scripts (`topic_generator.py`) and shared research
  templates, with dependencies in `requirements.txt`.
- `research/` — research briefs, claim ledgers, source registers, audits, verification
  queues, and footage queues per episode. See `.claude/rules/verification-queue.md`
  for the queue format used to hand off unresolved claims and footage to a human.
- `docs/editorial/` — detailed prose, storytelling, and structure guidelines.
- `docs/templates/` — reusable document templates.

See `README.md` for how to run and maintain the pipeline.

---

## 8. Editorial References

Load the relevant file before starting any major production task:

| Task | File |
|------|------|
| Writing or reviewing scripts — prose and voice | `docs/editorial/prose-style.md` |
| Documentary storytelling and tone | `docs/editorial/storytelling.md` |
| Story structure and narrative design | `docs/editorial/narrative-structure.md` |
| Story design document | `docs/templates/story-design.md` |
| Visual identity, palette, motion graphics | `docs/editorial/visual-system.md` |
