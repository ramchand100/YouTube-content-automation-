# CLAUDE.md — Channel Production Context & Editorial Constitution

This file is the single source of truth for every script, storyboard, thumbnail,
and research brief produced in this repository. Any content generated here must
comply with the rules below. When a request conflicts with this file, this file
wins.

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

## 2. Language (non-negotiable)

- **STRICTLY 100% professional, direct, engaging English.**
- **No Urdu, no Roman Urdu, no Urglish hybrid** in voiceover or on-screen script
  text.
- Local terms that have no clean English equivalent (e.g. *Seth*, *patwari*,
  *plot file*, *on-money/own*) may be used **only** as named concepts, and must be
  defined in plain English the first time they appear. They are analytical
  vocabulary, not casual code-switching.
- Tone of the prose: the register of a sharp business documentary (think
  investigative business journalism), not a lecture and not a hype reel.

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

## 4. Tone & Style

- Sharp, analytical, data-backed, investigative.
- Grounded in **ground-truth local realities**, never abstract theory.
- Confident and authoritative, never hyped or exaggerated.
- Every claim is either (a) a cited fact, (b) clearly labelled analysis/opinion,
  or (c) a clearly labelled estimate. Never blur the three.
- Avoid em dashes where a comma or a period will do.

---

## 5. Formatting & Length Rules

Scripts are **complete, un-cut, full-length production scripts.** No outlines
handed off as if finished, no "[continue here]" placeholders.

- **Length:** 1,800 to 2,500 words, equal to roughly 12 to 16 minutes of
  voiceover at a documentary pace (~150 words/minute).
- **Timestamped visual cue annotations** throughout, in the form
  `[VISUAL 03:15 — description]`, so an editor can build to the script.
- **Motion-graphic instructions for editors** written in plain, buildable terms
  (what to show, what animates, what data appears). Assume a solo editor working
  in After Effects and Premiere Pro. Do not spec anything that needs a 3D team.
- **Source citations** inline as `[SOURCE: publication/institution, year]` and
  collected in a Sources block at the end of every script.
- Any figure that moves fast or could not be fully confirmed is tagged
  `[VERIFY]` so it is re-checked before recording.

---

## 6. Editorial Rules

1. **Analyze through Pakistani economic reality.** Always connect a topic to the
   real local machinery: SBP policy rate and monetary stance, informal cash
   markets, the documented-vs-undocumented economy, FBR tax structure and
   withholding regime, DC/FBR property valuations, import LC constraints, energy
   tariffs and circular debt, and regulatory friction. A generic global framing
   that could apply to any country is a failure.
2. **No generic corporate clichés.** Ban phrases like "game-changer," "at the end
   of the day," "synergy," and "disrupt" unless used precisely and critically.
3. **Data discipline.** Sources first. If a number cannot be sourced, either drop
   it or clearly label it an estimate. Never invent a statistic to sound credible.
   This rigor is the entire competitive moat; do not spend it cheaply.
4. **Fairness and safety.** Business content will touch politics, powerful groups,
   the state's economic footprint, and named companies and families. Frame around
   documented facts and mechanics, present multiple sides on contested points, and
   never state an unproven allegation as fact. This protects credibility and the
   creator.
5. **Freshness.** Macro figures (SBP rate, inflation, FX, tax rates) change fast.
   Re-verify anything time-sensitive right before recording; do not reuse a stale
   number from an older episode.

---

## 7. The 5-Part Narrative Structure (every long-form episode)

Every flagship episode is built on this spine. Timestamps are targets for a
~14-minute runtime and flex per topic.

1. **The Hook (0:00 - 2:00):** open on a central paradox, a shocking metric, or a
   hidden local anomaly. State the promise of the video and the stakes.
2. **The Ground-Truth Mechanics (2:00 - 6:00):** step-by-step, how the business or
   economic system actually operates on the ground in Pakistan.
3. **The Core Conflict / Bottleneck (6:00 - 10:00):** the structural friction:
   regulation, cash-flow traps, capital misallocation, or competitive dynamics.
4. **The Broader Macro Impact (10:00 - 13:00):** how it ripples out to the wider
   economy, investors, and ordinary consumers.
5. **Strategic Takeaways & Future Outlook (13:00 - End):** concrete, honest
   lessons for founders, executives, and students, plus a grounded forward view.

---

## 8. Repository Map

- `topics/` — staging area for video ideas and research briefs (pre-production).
- `scripts/` — completed, production-ready full-length English scripts, plus the
  scripting engine (`script_engine.py`) and the script template (`TEMPLATE.md`).
- `storyboards/` — visual and motion-graphic blueprints for editors, timestamp-
  linked to the matching script.
- `prompts/` — AI visual prompts (Midjourney) and thumbnail layout specs.
- `tools/` — automation scripts (`topic_generator.py`) and shared research
  templates, with dependencies in `requirements.txt`.

See `README.md` for how to run and maintain the pipeline.
