# Verification Queue — Episode 15: The Hospital Carrying the Gap

- **Script:** `scripts/15_shaukat_khanum_funding.md`
- **Generated from:** `research/claim-ledgers/15_shaukat_khanum_funding_claims.csv` and
  `research/source-registers/15_shaukat_khanum_funding_sources.csv` (2026-08-26 pass)
- **Format:** `.claude/rules/verification-queue.md`

## Human Verification Handoff

### Research

- **Update, 2026-08-26 — Firecrawl MCP pass.** Firecrawl's `firecrawl_search` tool
  crawls with its own infrastructure rather than routing through this session's
  network path, so it got past the HTTP 403 blocks on shaukatkhanum.org.pk and the
  UK Charity Commission register that stopped this episode's original research pass.
  It generally returns short search snippets, not full page reads — items it
  resolved were held at CANDIDATE, not EDITOR VERIFIED, per the no-snippets rule.
- **Update, 2026-08-26 — user-supplied primary documents.** The user uploaded the
  Trust's Annual Report 2025 and its audited financial statements for the year
  ended December 31, 2025 (audited by A.F. Ferguson & Co.), both read in full by
  Claude. This is the strongest sourcing pass this episode has had: it fully closed
  V-001, V-003, and V-004 as EDITOR VERIFIED, and substantially upgraded V-005 —
  while also catching a real, previously-unnoticed inaccuracy in the script (the
  donation/zakat share was materially understated, and the paying-patient share was
  materially overstated; both are now fixed with precise audited figures). See
  each ticket below for specifics.
- All eight tickets have now moved forward from OPEN. V-006 and the free-treatment
  half of V-002 are EDITOR VERIFIED via full document reads (Charity Commission and
  "Our Story" respectively); V-001, V-003, V-004, V-005 are EDITOR VERIFIED via the
  user-supplied annual report/audit; V-007 is EDITOR VERIFIED for the date only;
  V-008 is RESOLVED as a decision not to use a figure.

### Footage

- No storyboard exists yet for this episode, so no footage-queue file has been
  generated. Run `/footage` after the storyboard is built.

### Priority (before this script can move to `production-ready`)

1. **V-007** — the only remaining genuinely open item: the Rs 4bn Peshawar
   first-phase cost figure is still single-sourced to one 2015 news article. Low
   stakes (a historical, non-headline figure) but worth a look if time allows.
2. **V-006's flagged side-finding** — an unreconciled £49m UK zakat figure was
   found but not used; worth a note to a human researcher in case it resurfaces in
   a future pass, so it isn't accidentally used without reconciliation.
3. Everything else is now EDITOR VERIFIED or a settled RESOLVED decision — this
   episode's research is in noticeably stronger shape than the original pass, and
   no further verification work is required before `production-ready` on the
   grounds of open V-XXX tickets specifically (a normal `/review-script` and
   `/audit-sources` pass on the corrected script is still the right next step).

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
- **2026-08-26 update (Firecrawl):** Firecrawl search found the hospital's own
  "Facts and Statistics" page states "Philanthropic spending to date, Rs. 137
  billion (US$ 857 Million)" as of 2026. Snippet only, not a full page read.
- **2026-08-26 update (Annual Report 2025, full document read):** The Trust's own
  Annual Report states, precisely dated: "Rs. 125 Billion — Spent on patient
  support from 1994-2025." This is a more authoritative and more precisely dated
  figure than the live website counter (which is presumably a running total that
  has since grown past the audited 2025 figure). Script updated to use Rs 125bn,
  1994-2025, with the per-year estimate recalculated accordingly (~Rs 4bn/year
  across 31 years).
- Status: EDITOR VERIFIED (full document read of a user-supplied primary source)

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
- **2026-08-26 update:** The 7,300-new-cases-in-2022 figure was dropped from the
  script rather than resolved (no current equivalent was found). The 75% figure is
  now confirmed via a full read of the hospital's own "Our Story" page (Firecrawl
  returned the entire page, not a snippet): "the hospital has continued to treat
  more than 75% of all cancer patients seen completely free of charge." The
  cumulative cancer-case count was replaced with the official Cancer Statistics
  page's figure — see V-001's note; this is a separate claim (145,969 malignant
  cases over 31 years) from the dropped 2022-specific figure.
- Status: RESOLVED for the 75% figure (EDITOR VERIFIED, full page read); the
  2022-specific annual figure is CLOSED (removed from script, not pursued further)

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
- **2026-08-26 update (Firecrawl):** Confirmed the 2026 figure directly (Rs 43.3
  billion, "Year 2026", on the official Facts and Statistics page — snippet only).
  The 2024 figure (Rs 34.8bn) and the donation/zakat share remained unconfirmed —
  a Financial Statistics page revenue table returned only a garbled snippet.
- **2026-08-26 update (audited financial statements, full document read) —
  important correction, not just a resolution.** The audited Income and
  Expenditure Account gives real total income of Rs 31.93bn (2024) and Rs 38.25bn
  (2025) — the Rs 34.8bn/2024 "budget" figure from Fund Meter does not match the
  audited actual and has been dropped from the script. More importantly: donations
  and zakat combined were **64% of income in 2024 and 67% in 2025** — not "more
  than half" as the script vaguely stated, and Net Clinical Income (paying
  patients) was only **~27% of 2025 income**, not "the other half" as Part 2
  previously implied. The script materially understated how donor-dependent this
  institution is and overstated the paying-patient contribution; both are now
  corrected with precise audited figures. The Rs 43.3bn/2026 figure is kept but
  explicitly labeled unaudited/forward-looking, since FY2026 has not closed yet.
- Status: EDITOR VERIFIED for 2024/2025 actuals and the donation/zakat/clinical
  split (full document read of a user-supplied primary source); the 2026 figure
  stays CANDIDATE/`[VERIFY]` since it cannot be audit-confirmed until the year ends

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
- **2026-08-26 update (Firecrawl):** An exact-wording snippet match from the
  Financial Statistics page named A.F. Ferguson and Co. as auditor. Snippet only.
- **2026-08-26 update (audited financial statements, full document read):** The
  Independent Auditor's Report itself was read directly — letterhead "A.F.
  Ferguson & Co., a member firm of the PwC network," signed by the firm in
  Lahore, dated May 19, 2026, engagement partner Muhammad Masood named explicitly.
  This is as primary as sourcing gets for this claim.
- Status: EDITOR VERIFIED (full document read of the primary audit report itself)

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
- **2026-08-26 update (Firecrawl) — important correction, not just a resolution.**
  Firecrawl search surfaced the hospital's own June 2026 project-status posts
  (Facebook, Instagram) and its "Karachi Project Sponsorships" page. These
  confirmed the ~Rs 16.4bn cost (also given as ~USD 109 million) but revealed that
  **the campus has not opened at all** — the script previously stated the opening
  "slipped to 2023," which is wrong. Snippets only, not full reads.
- **2026-08-26 update (annual report + audited financial statements, full
  document reads):** Both user-supplied primary documents corroborate and refine
  the Firecrawl finding. The audited Statement of Financial Position shows Rs
  16.608 billion in capital work-in-progress as of December 31, 2025 (matching the
  Firecrawl figure closely). The Annual Report's Karachi update states Rs 12.6
  billion of that was spent in 2025 alone, exterior finishing was expected Q1
  2026, equipment installation Q3 2026, and the hospital was "on track to become
  operational in December 2026" — consistent across the CEO's message, the
  Projects section, and the dedicated Karachi update page. This is now a primary,
  audited figure rather than a social-media snippet. Note: the CWIP balance may
  include minor non-Karachi capital projects too, though Karachi is almost
  certainly the overwhelming majority given Lahore and Peshawar are both
  operational; this is a reasonable, disclosed assumption, not a certainty.
- Status: EDITOR VERIFIED for the cost and opening-status correction (full
  document reads of two user-supplied primary sources); the CWIP-is-mostly-Karachi
  assumption is worth a footnote if a human ever drills into Note 10 of the
  audited accounts directly

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
- **2026-08-26 update:** Firecrawl returned the Charity Commission's full filing
  print — a structured 5-year financial-history table, not just a snippet —
  confirming financial year ending 31 December 2024, total income £17,740,632,
  total expenditure £18,097,742, and year-by-year charitable expenditure from
  FY2020 (£9.25m) through FY2024 (£16.01m). The script now states this figure with
  its confirmed year. One related figure was also found but NOT used — a UK
  fundraising page claiming "£49m of your Zakat went to 75% of patients in need in
  2024" — this doesn't reconcile with the £18m total expenditure figure above and
  needs its own check before ever being used (possibly a different scope, e.g.
  global zakat attributed to UK donors rather than this entity's own spend).
- Status: EDITOR VERIFIED for the income/expenditure/year (full document read).
  New open item: the unreconciled £49m zakat figure — not added to the queue as
  its own ticket since it isn't used anywhere, but flagged here for awareness.

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
- **2026-08-26 update:** The opening date (December 2015) is now independently
  confirmed via a full read of the hospital's own "Our Story" page. The Rs 4bn
  first-phase cost figure remains sourced only to the single 2015 Express Tribune
  article found in the original research pass — Firecrawl did not surface an
  independent confirmation of the cost specifically.
- Status: RESOLVED for the opening date (EDITOR VERIFIED); OPEN for the cost figure

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
- **2026-08-26 update:** Firecrawl search turned up additional official/social
  posts specifically about the Peshawar campus that cite 75% (e.g. a hospital
  social post: "Shaukat Khanum, Peshawar has been providing state-of-the-art free
  cancer treatment to more than 75% of deserving cancer patients"), not 90%. This
  is now three official/near-official sources agreeing on 75% for Peshawar
  specifically, against one Dawn article citing 90%. That strengthens, rather than
  resolves, the case for the script's existing choice to not use the 90% figure.
- Status: RESOLVED — keep using only the 75% network-wide figure; do not add the
  90% figure to the script
