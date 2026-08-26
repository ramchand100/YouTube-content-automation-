# Verification Queue — Episode 15: The Hospital Carrying the Gap

- **Script:** `scripts/15_shaukat_khanum_funding.md`
- **Generated from:** `research/claim-ledgers/15_shaukat_khanum_funding_claims.csv` and
  `research/source-registers/15_shaukat_khanum_funding_sources.csv` (2026-08-26 pass)
- **Format:** `.claude/rules/verification-queue.md`

## Human Verification Handoff

### Research

- 8 claims require checking (V-001 through V-008).
- 1 direct figure conflict between two sources (V-005, Karachi campus cost/timeline).
- 3 items are blocked because SKMCH&RC's own official site (shaukatkhanum.org.pk)
  returns HTTP 403 to direct fetch — treat as ACCESS BLOCKED for this and any future
  episode touching this institution, not just the items already listed.
- The user has downloaded the hospital's annual report and annual audit report and
  plans to provide them directly — **these documents should resolve V-001, V-002,
  V-003, and V-004 outright**, since they are exactly the primary-source class this
  research pass could not reach. Check those four first once the documents are in hand.

### Footage

- No storyboard exists yet for this episode, so no footage-queue file has been
  generated. Run `/footage` after the storyboard is built.

### Priority (before this script can move to `production-ready`)

1. **V-001, V-002, V-003, V-004** — resolve directly against the uploaded annual
   report / annual audit report once available. This is the single highest-leverage
   action available for this episode.
2. **V-005** — reconcile the Karachi campus cost/timeline conflict (Rs 6.2bn/2021
   vs. Rs 16.4bn/2023).
3. **V-006** — confirm the UK chapter's income/spending figures and their financial
   year.
4. **V-007, V-008** — lower-priority precision items already softened or flagged
   `[VERIFY]` in the script; fine to resolve in the normal pre-recording pass.

---

## V-001 — Cumulative patients treated and Rs 88 billion free-care figure

- Script location: Part 1, opening hook.
- Current wording: "It has treated more than 127,900 patients since it opened in
  Lahore in December 1994... One of them has given away 88 billion rupees of free
  cancer treatment since 1994."
- Why verification is needed: both figures trace only to a Dawn news article
  (`C001`, `C003`), reached via WebSearch synthesis, not direct fetch. This is the
  episode's opening hook — its two most load-bearing numbers rest on secondary
  journalism, not the hospital's own audited disclosure.
- Go to: The hospital's own annual report (cumulative patients-treated and
  cumulative free-treatment-value figures are standard annual-report disclosures for
  an institution of this kind) — this is exactly what the user's uploaded document
  should cover.
- Search terms (if the uploaded document doesn't have it and a further search is
  needed):
  - Shaukat Khanum annual report cumulative patients treated free treatment value
  - SKMCH&RC "since 1994" total patients treated
- Prefer: The hospital's own audited annual report over any press restatement.
- Check for: Whether "88 billion rupees" is a running cumulative total as of a
  specific date (the Dawn piece's publication date) or a static figure that has
  since moved — if the annual report has a more current cumulative figure, use that
  instead and note the as-of date.
- Do not use: A source that only repeats the round Rs 88bn figure without dating it.
- Safe fallback wording (already in script, softened with `[ESTIMATE]`): keep as-is
  if the annual report does not give a more precise or more current figure.
- Status: OPEN

## V-002 — 7,300 new cancer cases in 2022 and the 75% free-treatment rate

- Script location: Part 1.
- Current wording: "in 2022 alone, more than 7,300 new patients joined that number,"
  and the network-wide claim that more than 75% of patients are treated completely
  free (`C002`, `C004`).
- Why verification is needed: both figures come from the same single Dawn article
  as V-001, via WebSearch synthesis only. The annual report should carry both figures
  directly, and likely for a more recent year than 2022.
- Go to: The hospital's annual report — patient-registry and financial-assistance
  statistics sections.
- Check for: Whether the annual report's free-treatment percentage matches 75%
  network-wide, and whether a more recent patient-count year is available than 2022
  — if so, prefer the more recent figure and update the script's year reference.
- Do not use: A source that gives a percentage without specifying whether it is
  network-wide or for a single campus (see V-008 on the Peshawar-specific figure).
- Safe fallback wording (already in script): keep the Dawn-attributed figures with
  their `REPORTED` classification if the annual report doesn't cover this precisely.
- Status: OPEN

## V-003 — Annual operating budget (Rs 34.8bn / 38bn / 43.3bn) and donation/zakat share

- Script location: Part 2 (domestic cross-subsidy) and Part 3 (diaspora funding
  comparison).
- Current wording: budget figures for 2024/2025/2026 and the claim that donations
  and zakat combined fund more than half of the annual budget in each of these years
  (`C006`, `C007`).
- Why verification is needed: sourced only from SKMCH&RC's own social-media "Fund
  Meter" updates (S12), which are institutional self-disclosure, not an audited
  report. This is the single most important claim to upgrade to audited-source
  status, since it underpins the entire "who actually pays for this" argument in
  Parts 2 and 3.
- Go to: The audited annual report/financial statements directly — this is the
  primary reason the annual audit report the user downloaded matters most for this
  episode. Look for the income statement's breakdown of revenue by source (patient
  income, donations, zakat, government grants, endowment income).
- Check for: Whether the audited figures match the Fund Meter's social-media totals,
  and whether the "more than half" donation/zakat share holds up against the actual
  income-statement breakdown, or needs a more precise percentage.
- Do not use: A source that only restates the Fund Meter figures without an
  independent audited total to check them against.
- Safe fallback wording (already in script, `REPORTED` with attribution to SKMCH&RC's
  own published figures): keep if the audited report is not year-matched to these
  specific figures.
- Status: OPEN

## V-004 — Auditor of record (A.F. Ferguson & Co.)

- Script location: Part 2, sourcing/credibility passage.
- Current wording: states the hospital's financial statements are audited annually
  by A.F. Ferguson & Co. (`C008`).
- Why verification is needed: sourced from SKMCH&RC's own site
  (shaukatkhanum.org.pk/financial-statistics/), which returned HTTP 403 to direct
  fetch this session. Never confirmed by opening the actual page or an audited
  report's cover/signature page.
- Go to: The cover page or auditor's report section of the uploaded annual audit
  report — this is normally stated on the first page of any audited financial
  statement.
- Check for: The exact current auditor of record — audit firms do occasionally
  change, so confirm this against the most recent audit rather than an older one.
- Do not use: A source repeating the auditor's name without it appearing on an
  actual audited document.
- Safe fallback wording: if unconfirmed, soften to "audited annually by an
  independent chartered accountancy firm" and drop the specific firm name.
- Status: OPEN

## V-005 — Karachi campus cost and opening-date conflict

- Script location: Part 5, Karachi campus paragraph.
- Current wording: uses the later, higher figures (Rs 16.4bn cost, 2023 opening) per
  the more recent source.
- Why verification is needed: two Tier-1 sources give materially different figures —
  a 2019 Profit by Pakistan Today article states a Rs 6.2bn cost estimate and a
  planned December 2021 opening; a later Daily Times article states Rs 16.4bn and a
  2023 opening (`C022`). This is a direct, unreconciled conflict between two
  journalism sources, not a case of one source simply being more current — the size
  of the cost increase (roughly 2.6x) deserves confirmation it isn't a reporting
  error before being used as a real construction-overrun figure in the script.
- Go to: SKMCH&RC's own annual report for the relevant years (2019 through 2023),
  which should show the Karachi project's capital expenditure line item growing
  year over year — this would let the actual overrun be shown with real interim
  figures rather than just two endpoint estimates.
- Search terms:
  - Shaukat Khanum Karachi campus construction cost annual report
  - SKMCH&RC Karachi capital expenditure 2020 2021 2022
- Prefer: The hospital's own capital-expenditure disclosure over press estimates
  made mid-construction.
- Check for: Whether the cost increase reflects scope changes (the completed
  facility description in `C023` — 1 million sq ft, more beds/ICU capacity than
  originally planned — suggests the project itself may have grown, not just its
  price), which would be a more defensible framing than an unexplained overrun.
- Do not use: Either endpoint figure alone without noting the other exists.
- Safe fallback wording (already in script): keep both figures with explicit
  attribution to their respective years/sources if no more granular data surfaces.
- Status: OPEN

## V-006 — UK chapter (Shaukat Khanum Memorial Trust) income/spending and financial year

- Script location: Part 3, diaspora funding section.
- Current wording: not currently used as a stated figure in the script pending
  resolution (marked UNRESOLVED in the claim ledger, `C014`).
- Why verification is needed: a GBP 17.74 million income / GBP 18.1 million spending
  figure was found via WebSearch, but the UK Charity Commission register itself
  returned HTTP 403 to direct fetch, and the specific financial year the figures
  apply to was never confirmed.
- Go to: UK Charity Commission full filing print for charity #1000580
  (register-of-charities.charitycommission.gov.uk), or the beta platform duplicate
  listing (S22) — try both since one platform may be reachable when the other isn't.
- Check for: The exact financial year end date the income/spending figures cover,
  and whether more recent filings are available than whatever year this figure
  traces to.
- Do not use: A secondary aggregator site restating Charity Commission figures
  without a dated filing year.
- Safe fallback wording: if this cannot be resolved, the script's current choice —
  omitting a specific UK-chapter figure rather than stating an unconfirmed one — is
  the correct default and should stay.
- Status: OPEN

## V-007 — Peshawar campus first-phase cost (Rs 4bn) and opening date

- Script location: Part 5.
- Current wording: "The Peshawar campus opened in December 2015, after a first
  phase that cost about 4 billion rupees" (`C021`).
- Why verification is needed: sourced only via WebSearch synthesis from a single
  Express Tribune article, not directly fetched or cross-corroborated by a second
  source the way most other figures in this brief are.
- Go to: The annual report's historical/expansion section, which typically recaps
  each campus's build cost as part of the institution's own narrative.
- Check for: Whether "Rs 4 billion" refers to the first phase specifically (as
  currently written) or the eventual total cost of the Peshawar campus — these are
  likely different figures.
- Do not use: A source that gives a Peshawar cost figure without specifying phase.
- Safe fallback wording (already in script): keep as `REPORTED` with attribution if
  unconfirmed.
- Status: OPEN

## V-008 — Peshawar-specific 90%+ free-treatment rate vs. 75% network-wide figure

- Script location: not currently reconciled in the script; the network-wide 75%
  figure is used and the Peshawar-specific 90%+ figure is not, pending this check.
- Current wording: n/a — deliberately not stated as a Peshawar-specific claim yet.
- Why verification is needed: Dawn's Peshawar-specific coverage (`C005`, S08) states
  more than 90% of visitors to that campus receive free treatment, notably higher
  than the 75% network-wide figure (`C002`). These could both be true (Peshawar may
  serve a poorer catchment population than Lahore or Karachi), but the difference is
  large enough to need an explicit check before either using the Peshawar figure or
  ignoring it.
- Go to: The annual report's per-campus statistics, if broken out by location, or a
  direct read of the Dawn Peshawar article (S08) to confirm what population the 90%
  figure describes (all visitors, or a subset).
- Check for: Whether "90% of visitors" and "75% of patients" are even measuring the
  same thing (visitors vs. treated patients are not necessarily identical
  populations).
- Do not use: The 90% figure as a headline claim without resolving whether it's
  comparable to the 75% figure or describing something narrower.
- Safe fallback wording: keep the current script's approach of using only the
  reconciled, network-wide 75% figure until this is resolved.
- Status: OPEN
