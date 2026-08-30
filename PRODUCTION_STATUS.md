# Production Status

This file is the current state of the pipeline — what's active, what stage
it's at, and what's been deliberately deferred. It's injected into context
automatically at the start of every session in this repo (see the
SessionStart hook in `.claude/settings.json`), so a fresh session should
orient from this file before asking the user what to do.

**Read this, then CLAUDE.md, then act.** Don't re-derive state that's
already written down here — update it instead when it goes stale.

**Last updated:** 2026-08-29
**Branch:** `claude/episode-16-branch-bp7k9n`
**Local commits not yet pushed:** GitHub push is currently blocked — org
admin needs to install/reconnect the Claude GitHub App
(https://github.com/apps/claude/installations/select_target). Push as soon
as access is restored; do not treat local-only commits as lost work.

---

## Active episode

**Episode 16 — How Pakistan's Tax System Actually Works** (`16_pakistan_tax_system`)

| Step | Status |
|---|---|
| Angle | approved — `topics/angles/16_pakistan_tax_system_angle.md` |
| Research | complete, reconciled — `research/briefs/16_pakistan_tax_system_brief.md` |
| Script | drafted, rewritten to current craft standards — `scripts/16_pakistan_tax_system.md`, `status: draft` |
| Review | **not yet run** — `/review-script` is the next step |
| Source audit | not started |
| Storyboard | not started |
| Footage | not started |

**Known issues on this script, not yet fixed** (from a full-repo audit,
2026-08-29 — deliberately deferred per user request to fix system-level
issues first):
- Paragraph rhythm violated in 6 of 7 parts (dense 3-4 sentence paragraphs
  instead of the 1-2 sentence spoken-beat rule).
- Part 4 has a fact-density violation (4 consecutive fact-only sentences in
  one paragraph, no interpretation between them).
- ~12 REPORTED-classified citations are stated as flat fact where the claim
  ledger marks them `verified: partial` — missing `[VERIFY]` tags (about 40%
  of REPORTED citations overstate their certainty).
- Minor: "under a sixth" (Part 3) is technically the wrong direction —
  16.73% is just above one-sixth, not under it.
- Retention-bridge paragraph is still present in the script text (the rule
  requiring one has since been removed repo-wide, but existing scripts were
  left untouched — this is cosmetic, not a defect, and doesn't need fixing
  unless the user asks).

**Next step:** run `/review-script` on `scripts/16_pakistan_tax_system.md`
and fix what it finds (it should catch all of the above, plus anything new).

---

## System-level fixes already applied (2026-08-29)

A full-repo audit found this branch's merge (of two divergent episode
histories) left real contradictions and a tooling bug. All of the following
are fixed — see commit `5ae4978` for the full list:

- Fixed `validate_script.py`'s word-count bug (it counted the whole raw
  file instead of narration prose, inflating `word_count`/`estimated_duration`
  by 25-40% on multiple episodes) and a related bug where the last Part's
  body bled into the trailing Sources block.
- Removed the retention-bridge rule entirely (user request) — from
  `docs/editorial/storytelling.md`, `.claude/commands/write-script.md`,
  `.claude/commands/review-script.md`, and the validator.
- Fixed the Remotion-vs-CapCut contradiction across `CLAUDE.md`,
  `docs/footage-guidelines.md`, and the copyright-reviewer agent.
- Rewrote `.claude/agents/script-editor.md` (was still describing a fixed
  five-section process, predating the flexible Part-N structure).
- Reconciled the footage-rights register schema across 5 files that each
  described a different, unused CSV column layout.
- Redirected 3 stale skill templates to the canonical files instead of
  maintaining parallel copies.
- Added the missing paragraph-rhythm / relatable-scale / part-transition
  rules to `.claude/rules/scripts.md`.
- Removed the never-implemented `research/timelines/` convention; updated
  README's stale episode-reference table; consolidated `tools/requirements.txt`.

## Known issues NOT yet fixed — per-episode content backlog

Deliberately deferred (user said "leave episodes for now" on 2026-08-29).
Fix these when the user asks to work on that specific episode — do not fix
them opportunistically as a side effect of other work, since the user set
that scope boundary on purpose.

- **Episode 01 (`01_pakistan_railways_freight`)** — the script file is
  effectively empty (1 byte). A complete draft existed in git history
  (`git show 81715c2^:scripts/01_pakistan_railways_freight.md`) and was
  deleted in a later commit. Research (brief, 59-row claim ledger, 48-source
  register) is intact and reasonably strong. This episode needs a script
  written or restored before it can proceed at all.
- **Episode 11 (`11_pakistan_steel_mills`)** — a stated "Rs 6 million per
  hour" figure doesn't reconcile with the Rs 25.5bn/year loss it's tagged as
  derived from (implies roughly double). The storyboard is stale and
  Remotion-based: it hardcodes "Rs 19 billion" and "Rs 20B+ annual interest"
  as settled facts while the script and this episode's own verification
  queue mark both as disputed/`[VERIFY]`. It also has an unsourced invented
  1981 workforce data point, and needs a full storyboard rebuild against the
  current CapCut/source-screenshot rules.
- **Episode 12 (`12_metro_bus_subsidy`)** — no storyboard, source audit, or
  verification queue exist despite ~9 open `[VERIFY]` items in the script.
- **Episode 13 (`13_gwadar_karachi`)** — two no-repetition violations: the
  Strait of Hormuz is defined twice (Parts 2 and 4), and a "what a port
  needs" four-item list is restated almost verbatim between Parts 3 and 4.
  No verification queue exists despite nearly every claim being
  `verified: partial`.
- **Episode 14 (`14_power_gas_circular_debt`)** — **two real arithmetic
  errors in its own headline statistics**: the capacity-charge split is
  stated as 63%/37% but the cited figures actually compute to ~68%/32%; the
  SNGPL receivables share is stated as 9-14% but computes to ~9-18%. Also,
  the script states only the Rs 3.498tn IPP-savings figure even though its
  own verification queue (V-008) explicitly says to present both that and
  the conflicting Rs 4.3tn figure rather than pick one silently.
- **Episode 15 (`15_shaukat_khanum_funding`, the "reference standard"
  episode)** — front-matter word count was inflated ~26% by the same
  validator bug (now fixed going forward; this episode's own front matter
  hasn't been recomputed). Correcting it reveals the real script (1,586
  words) falls below CLAUDE.md's 1,800-word default minimum. Missing a
  delivery-notes file despite being past the trigger point for one. One
  near-miss banned cliché ("only half the story"). Audit gate not fully
  closed (5/30 claims still "Needs verification").

---

## How a new session should resume

1. Read this file (you probably just did, via the SessionStart hook).
2. Read `CLAUDE.md` for the editorial constitution.
3. If the user doesn't specify an episode, assume Episode 16 is current and
   its next step is `/review-script`.
4. If the user asks about repo health, system issues, or "what's broken,"
   the per-episode backlog above is the answer — don't re-audit from
   scratch unless something has clearly changed since 2026-08-29.
5. Update this file whenever an episode moves stage, a backlog item gets
   fixed, or a new one is found. A stale status file is worse than none —
   keep it in sync with reality the way `.claude/rules/delivery-notes.md`
   asks of delivery notes.
