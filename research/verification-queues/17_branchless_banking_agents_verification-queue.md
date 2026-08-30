# Verification Queue — Episode 17: The Agent Economy That Banked Pakistan's Unbanked

- **Script:** `scripts/17_branchless_banking_agents.md` (not yet written)
- **Generated from:** `research/briefs/17_branchless_banking_agents_brief.md` and
  `research/claim-ledgers/17_branchless_banking_agents_claims.csv` (2026-08-30 research pass)
- **Format:** `.claude/rules/verification-queue.md`

## Human Verification Handoff

### Research

- 9 claim tickets opened (V-001 through V-009).
- No storyboard exists yet for this episode (research precedes structure/script) —
  the footage-queue file is skipped per `/research` instructions and should be
  generated once `/footage` runs after a storyboard exists.
- **Systemic access issue**: every `sbp.org.pk` PDF/page attempted this session
  returned HTTP 403 to both WebFetch and a direct curl through the session's
  proxy. Treat this as ACCESS BLOCKED for *any* future SBP.org.pk fetch from
  this environment, not just the specific URLs listed below — a human with an
  ordinary browser can likely reach these pages fine.
- 2 claims are UNRESOLVED at the center of the episode's riskiest section
  (Part 3, the agent workaround/overcharging claim) — see V-001 and V-002.
  These are not simple fact-checks; they may not be resolvable before scripting,
  and the brief already recommends the angle file's own fallback framing.

### Priority (before this script can move to `production-ready`)

1. **V-001 / V-002** — the Part 3 workaround and cash-in-overcharging claims.
   Highest narrative risk in the episode. If no corroboration surfaces, the
   script must use the safe fallback framing, not present either as fact.
2. **V-003** — re-derive the headline scale figures (agents, m-wallets) directly
   from a primary SBP PDF via ordinary browser access, since this session
   could not open any of them directly.
3. **V-004** — confirm current (2026) JazzCash/Easypaisa cash-in/cash-out fee
   tiers against the operators' own Schedule of Charges PDFs before recording,
   since fees revise quarterly and this brief used a secondary aggregator.
4. **V-005** — confirm the Business Recorder "make cash more expensive than
   digital" quote's exact wording and speaker attribution before using it,
   since the full article was never directly read this pass.
5. **V-006** — confirm whether SBP has *any* circular (beyond the general 2019
   BB Regulations, which this pass read in full and found no such clause)
   mandating free cash-in, before the script states this as an SBP rule.

---

## V-001 — The personal-account cash-out workaround (Part 3, core claim)

- Script location: Part 3 (not yet drafted — this is the central claim the Part
  needs to be built around or safely reframed away from).
- Current wording: n/a (script not yet written). The angle file's proposed
  framing: "an agent-side workaround: routing cash-outs through the agent's own
  personal wallet/bank account... instead of the official agent cash-out
  channel, specifically to avoid the company taking its share of the fee, then
  handing the customer cash and keeping a self-set commission entirely."
- Why verification is needed: this claim originates from the user's own
  ground knowledge, explicitly flagged in the angle file as needing independent
  corroboration before it can be scripted as fact. This research pass found
  **no independent Pakistani source** describing this specific mechanism. The
  single most relevant piece of research (CGAP, 2017, four-country fieldwork
  including Pakistan) documents the *general phenomenon* internationally but
  classifies Pakistan as a "low informal OTC market" and concludes agents in
  the studied markets do not typically use commission-driven leverage this way
  — a real complication, not a confirmation, and it is 8-9 years old (predates
  Raast and the subsequent wallet-account boom).
- Go to: SBP's Consumer Protection Department complaint data/annual report
  (if publicly summarized), Financial Monitoring Unit (FMU) suspicious-
  transaction-report summaries on BB agents, or a fresh CGAP/Karandaaz/MSC
  (MicroSave Consulting) field study more recent than 2017 if one exists.
- Search terms:
  - SBP Consumer Protection Department annual report branchless banking complaints
  - Karandaaz OR MicroSave Pakistan agent malpractice 2023 2024 2025
  - Pakistan branchless banking agent fraud personal account SBP FMU
  - "commission reversal" OR "off-ledger" branchless banking Pakistan agent
- Prefer: A source with actual field data (interviews, mystery shopping, complaint
  records) over a single anecdote or a general trend piece.
- Check for: Whether any finding distinguishes agent-initiated workarounds from
  customer-initiated ones (both exist internationally per CGAP's taxonomy, and
  they have different implications for who "wins" from the workaround).
- Do not use: A forum/social-media post (one was already found and discarded —
  see brief Section 8) as if it were reporting.
- Safe fallback wording (per the angle file's own pre-agreed fallback): frame
  as "a practice described by industry sources" / a firsthand ground account
  under investigation — explicitly not an established, sourced fact. The script
  should not claim this is documented, widespread, or confirmed.
- Status: OPEN

## V-002 — Agents charging for cash-in despite the free-cash-in norm (Part 3)

- Script location: Part 3, alongside V-001.
- Current wording: n/a (script not yet written).
- Why verification is needed: same origin as V-001 (user's ground knowledge,
  flagged for corroboration). This pass found no independent Pakistani source
  documenting widespread cash-in overcharging. It also could not confirm that
  SBP has a blanket regulatory mandate that cash-in be free (see V-006) — so
  even the premise that charging for cash-in would violate a specific rule is
  itself unconfirmed, separate from whether the practice occurs at all.
- Go to: Same as V-001, plus JazzCash/Easypaisa's own customer-complaint pages
  or app-store reviews (as informal signal only, not citable evidence) to see
  whether cash-in overcharging is a recurring complaint theme worth a human
  spot-check.
- Search terms:
  - "charged me to deposit" OR "cash in fee" JazzCash Easypaisa complaint
  - SBP complaint portal branchless banking agent overcharging cash-in
- Prefer: Any source with a specific, dated, attributed incident over a general
  claim that "some agents" do this.
- Do not use: App-store star ratings/reviews as citable evidence — informal
  triage signal only, to help a human decide where to look next.
- Safe fallback wording: same as V-001 — "a practice described by industry
  sources," not an established fact.
- Status: OPEN

## V-003 — Headline scale figures (agents, m-wallets) not independently confirmed

- Script location: Part 1 (the opening scale/hook figures).
- Current wording: brief cites 757,727 total agents / 239,034 active agents /
  141,560,617 accounts for Jul-Sep 2025, via a Scribd mirror of SBP data
  surfaced by Firecrawl search — a search-snippet read, not a full document read.
- Why verification is needed: this session could not open any SBP.org.pk PDF
  directly (HTTP 403 on every attempt, via both WebFetch and curl). The figures
  used are very likely accurate (SBP publishes this series every quarter and
  the mirrored numbers are internally consistent with the prior-quarter
  comparison column), but per research rules a search-result snippet is not
  final evidence.
- Go to: `sbp.org.pk/acd/branchless/Stats/` directly, via an ordinary browser
  (not this fetch environment) — download the actual quarterly PDF.
- Search terms:
  - site:sbp.org.pk branchless banking statistics [most recent quarter]
- Prefer: The primary SBP PDF over any mirror (Scribd, CollegeSidekick) or
  search snippet.
- Check for: Whether "Number of Agents" in the primary table means cumulative
  registered agents or agents onboarded that quarter, and whether the sharp
  active-agent decline noted in the brief (271,080 → 239,034) is real or a
  column-alignment misread of the mirrored snippet.
- Do not use: A secondary blog's restatement of the same figures without
  tracing it back to the SBP PDF.
- Safe fallback wording: keep the figures but attribute as "according to SBP's
  quarterly branchless banking statistics" with `[VERIFY]`, rather than stating
  them as flatly confirmed.
- Status: ACCESS BLOCKED (for this session/environment specifically — likely
  resolvable by a human with ordinary browser access)

## V-004 — Current JazzCash/Easypaisa cash-in/cash-out fee tiers

- Script location: Part 2 (official commission structure).
- Current wording: brief cites 2026 cash-out fee tiers from a Pakistan Observer
  aggregator article, not the operators' own Schedule of Charges (SOC).
- Why verification is needed: SBP's own regulation requires operators to
  publish and lock a quarterly SOC — meaning the correct, current figure is a
  moving target that must be re-checked immediately before recording, not
  assumed stable from this research date (2026-08-30).
- Go to: JazzCash's own SOC page (jazzcash.com.pk/schedule-of-charges) and
  Easypaisa's equivalent, downloading the actual current-quarter PDF (this
  session found the landing page but the linked PDF itself was not retrieved).
- Search terms:
  - JazzCash schedule of charges PDF [current quarter] 2026
  - Easypaisa schedule of charges PDF [current quarter] 2026
- Prefer: The operator's own published SOC PDF over any third-party aggregator.
- Check for: Whether a cash-in fee has been introduced (per the 2021 Profit
  reporting's warning that this was a live possibility) — this is a load-bearing
  check given the Part 3 discussion of the free-cash-in norm.
- Do not use: An aggregator blog with no visible publish/update date.
- Safe fallback wording: describe the fee structure qualitatively ("a rising
  tiered fee on cash withdrawal") without a specific current-quarter number if
  the SOC cannot be confirmed before recording.
- Status: OPEN

## V-005 — "Make cash more expensive than digital" (easypaisa executive quote)

- Script location: Part 5 (the Raast threat).
- Current wording: brief attributes to a Business Recorder / BR Research
  interview with an "easypaisa Digital Bank chief" (one search result named
  Jahanzeb Khan, CEO), headlined "Make cash more expensive than digital."
- Why verification is needed: the full article could not be fetched this
  session (HTTP 403 on both WebFetch and curl with two different user agents;
  web.archive.org is also unreachable from this tool). Only the headline and a
  one-sentence gist were confirmed, via two independent WebSearch queries.
- Go to: brecorder.com/news/amp/40422255 (or the non-AMP version) via an
  ordinary browser.
- Search terms:
  - site:brecorder.com "make cash more expensive than digital"
- Prefer: The full interview text over the headline alone, to get the exact
  quote, the speaker's correct title, and the surrounding context (was this
  said specifically about the agent commission model, or about digital
  adoption generally?).
- Do not use: The headline alone as if it were a verbatim quote in the script
  — confirm exact wording before using quotation marks.
- Safe fallback wording: paraphrase without quotation marks — "an executive at
  one of the two dominant mobile-wallet operators has said publicly that cash
  needs to become more expensive than digital payments to shift behaviour" —
  if the exact quote can't be re-confirmed.
- Status: ACCESS BLOCKED

## V-006 — Does SBP mandate free cash-in anywhere beyond the 2019 BB Regulations?

- Script location: Part 3 (the regulatory anchor for the workaround discussion).
- Current wording: brief states, based on a full direct read of the 2019 BB
  Regulations, that no such blanket clause exists in that document.
- Why verification is needed: this pass read the *current, consolidated* 2019
  regulation in full, but did not exhaustively search every individual BPRD/
  BC&CPD circular issued since (SBP issues many narrower circulars that amend
  or sit alongside the consolidated regulations). It is possible a narrower
  circular on BB consumer protection specifically addresses cash-in fees and
  was missed.
- Go to: SBP's Consumer Protection Department circular index
  (sbp.org.pk/cpd/cpd-shelf.asp) and the BPRD circular index, scanning circular
  titles/summaries for "cash-in" or "agent fee" specifically.
- Search terms:
  - SBP BC&CPD circular cash-in fee branchless banking
  - SBP BPRD circular agent commission consumer protection
- Prefer: An actual circular text over a secondary summary.
- Check for: A circular date — if one exists, note whether it predates or
  postdates the 2021 Profit reporting on the industry's cash-in-fee concern,
  since that would clarify whether SBP acted preemptively or reactively.
- Do not use: A source that merely asserts "cash-in is free" without citing a
  specific regulation or circular number.
- Safe fallback wording: keep the current brief's framing — "an industry norm
  supported by adjacent SBP fee interventions, not a confirmed blanket
  regulatory mandate" — unless a specific circular is found.
- Status: OPEN

## V-007 — Provincial agent-density figures (Punjab vs Balochistan)

- Script location: Part 4 (geographic distribution).
- Current wording: brief cites Data Darbar Insights' analysis of SBP data
  (Punjab 413,991 agents / 63.72% of national total / 516 per 100k adults;
  Balochistan 188 per 100k adults) as of December 2023.
- Why verification is needed: this is a secondary analysis of primary SBP
  EasyData series data, not independently re-derived — the underlying SBP
  EasyData portal also returned HTTP 403 to this session's fetch attempt.
- Go to: `easydata.sbp.org.pk` directly via ordinary browser, provincial
  branchless-banking-agent series.
- Search terms:
  - SBP EasyData branchless banking agents by province
- Prefer: The primary SBP EasyData series over the secondary blog's numbers.
- Check for: Whether more recent (2024/2025) provincial data is available,
  since the cited figures are from December 2023 and the episode's headline
  scale figures are from Q3 2025 — a roughly two-year gap that should be
  narrowed if possible.
- Do not use: A source that doesn't specify its as-of date.
- Safe fallback wording: keep the December 2023 figures but explicitly date
  them in the script ("as of the most recent published provincial breakdown,
  December 2023") rather than implying they're current to the episode's
  headline quarter.
- Status: ACCESS BLOCKED

## V-008 — Karandaaz K-FIS 2024 primary report not independently opened

- Script location: Part 1 and Part 6 (inclusion-narrative reconciliation).
- Current wording: brief cites financial-inclusion/gender/mobile-money figures
  cross-corroborated across five press outlets covering the same Karandaaz
  survey, but the primary Karandaaz report/narrative deck itself was not
  opened.
- Why verification is needed: five independent outlets reporting the same
  numbers is a reasonably strong REPORTED-tier basis, but the source hierarchy
  prefers a direct primary read, and Karandaaz's own report may contain
  additional detail (methodology, confidence intervals, provincial breakdowns
  beyond the three cited) useful for the script.
- Go to: karandaaz.com.pk/research/publications/karandaaz-financial-inclusion-survey
  — download the Narrative Report and Presentation Deck directly.
- Search terms:
  - Karandaaz K-FIS 2024 narrative report PDF download
- Prefer: The primary Karandaaz PDF over any press paraphrase.
- Check for: Sample size and methodology notes, and whether Karandaaz's own
  report gives a mobile-money-specific (not just overall financial inclusion)
  rural/urban split, which would sharpen Part 1's hook.
- Do not use: A source that restates the headline percentages without the
  underlying survey wave/date.
- Safe fallback wording: current REPORTED framing, attributing to "Karandaaz's
  2024 Financial Inclusion Survey, as reported by [outlet]" is acceptable if
  the primary document isn't opened before recording.
- Status: CANDIDATE

## V-009 — Active-agent count decline (271,080 → 239,034) between Apr-Jun and Jul-Sep 2025

- Script location: Part 1 or Part 4, if this counter-intuitive data point is
  used (active agents falling even as total registered agents and accounts
  both rose).
- Why verification is needed: this is exactly the kind of surprising figure
  that could either be a genuinely interesting finding (worth a sentence in
  the script) or a snippet-parsing error (columns misread from the Scribd
  mirror's rendering). It should not be used in the script until confirmed
  against the primary PDF.
- Go to: same as V-003.
- Search terms: same as V-003.
- Check for: SBP's own definition of "active" (e.g., agents with at least one
  transaction in the quarter) — a definitional change between quarters could
  also explain an apparent decline without reflecting real agent attrition.
- Do not use: The Scribd-mirrored snippet alone as confirmation this is real.
- Safe fallback wording: omit this specific data point from the script unless
  confirmed against the primary document.
- Status: CANDIDATE
