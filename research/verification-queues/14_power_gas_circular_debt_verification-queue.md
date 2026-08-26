# Verification Queue — Episode 14: The Machine That Never Stops Growing

- **Script:** `scripts/14_power_gas_circular_debt.md`
- **Generated from:** `research/claim-ledgers/14_power_gas_circular_debt_claims.csv` and
  `research/source-registers/14_power_gas_circular_debt_sources.csv` (2026-08-26 pass)
- **Format:** `.claude/rules/verification-queue.md`

## Human Verification Handoff

### Research

- 9 claims require checking (V-001 through V-009).
- 2 items have directly conflicting or internally inconsistent sources (V-006, V-008).
- Business Recorder and Profit by Pakistan Today returned HTTP 403 to direct fetch
  for essentially every article tried this session — treat both as ACCESS BLOCKED
  for this and any future energy-sector episode, not just the items already listed.
  This episode leans on them heavily (roughly a third of the source register), so
  this is the single biggest sourcing weakness in the brief.
- Several primary regulatory documents were identified but never opened (NEPRA
  tariff notifications, SBP/World Bank/ADB papers) — these are higher-value targets
  than re-trying the blocked press sources, since they would let claims move from
  REPORTED to VERIFIED rather than just re-confirming the same secondary reporting.

### Footage

- No storyboard exists yet for this episode, so no footage-queue file has been
  generated. Run `/footage` after the storyboard is built.

### Priority (before this script can move to `production-ready`)

1. **V-001** — resolve the combined Rs 5.286 trillion circular-debt figure against
   a primary Finance Division / Power Division document, not just The Nation's
   press summary. This is the episode's headline number.
2. **V-006** — resolve the LDPL force-majeure chronology inconsistency (`C021`).
3. **V-008** — reconcile the two conflicting IPP-renegotiation savings totals
   (Rs 3.498tn vs. Rs 4.3tn, `C034`).
4. **V-002, V-003, V-004** — upgrade the K-Electric, IMF flow-limit, and IPP-history
   claims from WebSearch-synthesis to a directly opened primary or Tier-1 source.
5. **V-005, V-007, V-009** — lower-priority precision/traceability items, already
   softened or flagged `[VERIFY]` in the script; fine to resolve in the normal
   pre-recording pass.

---

## V-001 — Combined Rs 5.286 trillion circular-debt figure

- Script location: opening hook / headline figure, referenced throughout.
- Current wording: cites the combined power-plus-gas total at Rs 5.286 trillion as
  of June 2026, up from Rs 5.206 trillion at the start of CY2026 (`C001`).
- Why verification is needed: this is the episode's single most important number,
  and it comes from a single Nation article citing an unnamed official source
  (`verified: partial`) — it does not name the specific ministry report or dataset
  it originates from.
- Go to: Ministry of Finance / Power Division circular-debt status report, or the
  IMF's own EFF/RSF review documents (which the same article says gave separate
  power/gas breakdowns) — the IMF review documents themselves would be a stronger,
  citable primary source than the newspaper's summary of them.
- Search terms:
  - IMF Pakistan third EFF review second RSF review circular debt 2026
  - Power Division Pakistan circular debt status report June 2026
  - Finance Division Pakistan energy circular debt combined total 2026
- Prefer: The IMF review document itself, or a Ministry of Finance report, over a
  single newspaper's aggregation.
- Check for: Whether the Rs 5.286tn figure is a snapshot at a stated date (June 30
  2026) consistently across sources, since circular-debt totals move fast and a
  figure quoted a few weeks apart can differ meaningfully.
- Do not use: A source that repeats the round Rs 5.286tn or Rs 5.3tn figure without
  citing its own primary origin.
- Safe fallback wording (already in script): keep `REPORTED` with explicit
  attribution to The Nation if no primary document surfaces before recording.
- Status: OPEN

## V-002 — K-Electric / NEPRA Incremental Consumption Package dispute

- Script location: power-sector section, K-Electric non-payment paragraph.
- Current wording: attributes K-Electric's Rs 194bn non-payment to a dispute over
  the Incremental Consumption Package (ICP), implemented Nov 2020–June 2021,
  extended July 2021–Oct 2023, now escalated to SIFC (`C008`).
- Why verification is needed: sourced only via WebSearch synthesis from a single
  Business Recorder article (S23), which returned HTTP 403 to direct fetch. This is
  a fairly technical regulatory dispute and deserves a primary check before being
  stated as the cause of a Rs 194bn/year gap.
- Go to: NEPRA's own decision/order on the ICP dispute, or K-Electric's own investor
  disclosures (PSX filings) referencing the SIFC escalation.
- Search terms:
  - NEPRA K-Electric Incremental Consumption Package decision
  - K-Electric SIFC circular debt dispute 2026
- Prefer: A NEPRA order or K-Electric PSX filing over a single press paraphrase.
- Check for: Whether the ICP dispute is the sole driver of the Rs 194bn figure, or
  one of several contributing factors bundled into that number.
- Do not use: A source repeating the ICP/SIFC framing without a primary regulatory
  document behind it.
- Safe fallback wording (already in script): keep `REPORTED` with attribution if
  unconfirmed.
- Status: OPEN

## V-003 — IMF's requested circular-debt flow limit (Rs 300–325bn)

- Script location: reform/IMF-conditionality section.
- Current wording: states the IMF requested the circular-debt flow be restricted to
  Rs 300–325bn, lower than the prior year's level (`C010`).
- Why verification is needed: sourced only via WebSearch synthesis from a single
  Express Tribune article (S06), which returned HTTP 403 to direct fetch. IMF
  program conditions are exactly the kind of figure that should trace to the IMF's
  own published program documents, not a press paraphrase.
- Go to: The IMF's Pakistan EFF/RSF staff report or program documents (published on
  imf.org), which typically state quantitative performance criteria explicitly.
- Search terms:
  - IMF Pakistan EFF review circular debt flow ceiling structural benchmark
  - IMF Pakistan staff report power sector circular debt target
- Prefer: The IMF staff report's own wording over a news summary of it.
- Check for: Whether this is a formal performance criterion/structural benchmark
  (with real consequences for non-compliance) or an informal expectation — these
  carry different weight in the script's framing.
- Do not use: A source that states the figure without specifying whether it's a
  binding program condition.
- Safe fallback wording (already in script): keep `REPORTED` if unconfirmed.
- Status: OPEN

## V-004 — 1994 Power Policy capacity-payment mechanism history

- Script location: structural/historical section on why capacity payments exist.
- Current wording: attributes the take-or-pay, USD-indexed 18% rate-of-return
  structure to the 1994 Power Policy, built in on IMF/ADB advice (`C026`).
- Why verification is needed: sourced from an SDPI policy paper found via
  WebSearch, not yet directly fetched and read (source register lists it as
  "identified via search, not yet fetched").
- Go to: The SDPI paper itself (S29), or the World Bank policy working paper already
  identified in the register (S30, "Learning from Power Sector Reform: The Case of
  Pakistan") — both are primary-adjacent sources on this exact history and should
  simply be opened and read, not re-searched.
- Check for: The precise attribution — whether it was specifically IMF and ADB
  advice, or a broader set of advisors/donors, and whether "18% USD-indexed" applied
  uniformly or varied by project.
- Do not use: A source that repeats "1994 Power Policy" as a label without detailing
  the mechanism.
- Safe fallback wording (already in script): keep `REPORTED` if the two identified
  documents don't resolve this cleanly.
- Status: OPEN

## V-005 — NEPRA CY2026 capacity-charge figures (Rs 17.19/unit, Rs 3,185.97bn total)

- Script location: capacity-payment section.
- Current wording: cites NEPRA-approved CY2026 capacity charges and total projected
  power purchase price (`C028`).
- Why verification is needed: a primary NEPRA determination document (S32) was
  identified in the source register but never fetched or read — this is a case
  where the primary source is sitting right there and just needs to be opened.
- Go to: S32 directly — `nepra.org.pk/tariff/Tariff/Ex-WAPDA%20DISCOS/2026/Decision%20of%20the%20Authority%20Motion%20of%20Federal%20Govt.%201004-23%20dated%2012.01.2026.PDF`
- Check for: Whether the figures in the script match the determination's own
  numbers exactly, since The Nation's article (S31) is a secondary paraphrase of
  this same document.
- Do not use: The Nation's figure alone when the primary determination is directly
  linked and accessible.
- Safe fallback wording: none needed if the primary document confirms the figures —
  this should be a quick upgrade from REPORTED to VERIFIED.
- Status: OPEN

## V-006 — LDPL force-majeure chronology inconsistency

- Script location: IPP/gas-linkage case-study section (Liberty Daharki Power).
- Current wording: currently marked UNRESOLVED in the claim ledger and not stated
  as a clean timeline in the script (`C021`).
- Why verification is needed: the research found a March 2023 force-majeure notice
  reportedly served by LDPL after a gas-supply suspension, but also a prior October
  2021 PPA Amendment Agreement that had already established non-supply of gas by
  SNGPL as an "Other Force Majeure Event" — these two facts as currently stated
  don't obviously fit together in sequence, and the underlying Business Recorder
  article (S09) returned HTTP 403 to direct fetch, so this was never resolved by
  actually reading the source.
- Go to: The Business Recorder article directly (S09), or LDPL/SNGPL's own PPA
  amendment filings if publicly available, to establish the actual sequence of
  events.
- Search terms:
  - Liberty Daharki Power SNGPL force majeure notice 2023
  - LDPL PPA Amendment Agreement October 2021 force majeure gas
- Check for: Whether these are two separate incidents (an earlier contractual
  amendment, then a later actual invocation) rather than a contradiction — that
  would resolve the apparent inconsistency without needing new information.
- Do not use: Either fact alone in the script until the sequence is confirmed,
  since an incorrect causal chain here would misstate how the dispute unfolded.
- Safe fallback wording: omit this sub-detail from the script and use only the
  confirmed Rs 20.029bn dues figure (`C019`) if the chronology can't be resolved.
- Status: OPEN

## V-007 — SNGPL power-sector receivables and PBS/CPPA-G root cause attribution

- Script location: gas-linkage section, SNGPL receivables paragraph.
- Current wording: attributes SNGPL's power-sector receivables to inadequate fund
  releases by CPPA-G to the power sector (`C017`).
- Why verification is needed: sourced only via WebSearch synthesis from a single
  Business Recorder article (S10), which returned HTTP 403 to direct fetch.
- Go to: CPPA-G's own disclosures, or a direct read of S10, or the EnergyUpdate.com.pk
  corroborating coverage (S05, S12), which was directly fetched and could be
  re-checked for this specific attribution.
- Check for: Whether this is CPPA-G's own stated reason or an inference reporters
  drew from the broader circular-debt chain.
- Do not use: The attribution as settled fact if it turns out to be a reporter's
  inference rather than an official statement.
- Safe fallback wording (already in script): keep `REPORTED` if unconfirmed.
- Status: OPEN

## V-008 — Conflicting IPP-renegotiation savings totals (Rs 3.498tn vs. Rs 4.3tn)

- Script location: reform-history section, IPP renegotiation outcomes.
- Current wording: currently marked UNRESOLVED, not reconciled in the script
  (`C034`).
- Why verification is needed: EnergyUpdate.com.pk (S37) reports Power Division
  savings projections totaling Rs 3.498 trillion with a stated component breakdown;
  a separate, later PhotoNews Pakistan article (S38) states the government claims
  Rs 4.3 trillion in total savings, with no reconciliation between the two figures
  found in this research pass. A roughly 23% gap between two "official" savings
  claims is a real discrepancy, not noise — it directly affects how credible the
  script's reform-outcome claim reads.
- Go to: The Power Division's own public statements or a Ministry of Energy press
  release covering the more recent, higher figure, to see whether it explicitly
  supersedes the Rs 3.498tn figure (e.g., because more IPPs were added to the
  renegotiation program between the two reports) or whether it's a different way of
  counting the same deals.
- Search terms:
  - Power Division Pakistan IPP renegotiation total savings Rs4.3 trillion
  - Ministry of Energy Pakistan IPP contract savings updated figure
- Check for: The date range and IPP count each figure covers — if the two reports
  are simply counting a different, expanding set of renegotiated contracts at
  different points in time, that resolves the apparent conflict without needing to
  pick one as "correct."
- Do not use: Either figure as the sole savings total in the script until this is
  resolved; if unresolved, present both explicitly as differing official claims
  rather than picking one silently.
- Safe fallback wording: "government officials have cited renegotiation savings
  estimates ranging from roughly Rs 3.5 trillion to Rs 4.3 trillion depending on the
  source and date" — states the conflict honestly rather than picking a number.
- Status: OPEN

## V-009 — Rs 2.4 trillion earlier circular-debt figure vs. later Aug 2026 figures

- Script location: not currently used as a stated figure — flagged in the claim
  ledger as needing date reconciliation before use (`C035`).
- Current wording: n/a.
- Why verification is needed: an earlier report put circular debt at Rs 2.4
  trillion, projected to fall to Rs 400–450bn after a Rs 1.23 trillion loan
  restructuring; this is far below the Rs 5.286tn combined / Rs 1.675tn power-only
  figures used elsewhere in the brief, and the two snapshots were never dated
  precisely enough to confirm whether this represents the power sector only, an
  earlier year, or a figure that simply didn't hold.
- Go to: Whatever source produced the Rs 2.4tn / Rs 400–450bn projection — retrace
  it and confirm its date and scope (power-only vs. combined) before using it
  anywhere, including in any before/after historical framing.
- Check for: Confirmation that the projected fall to Rs 400–450bn is the same
  restructuring effort documented elsewhere, and an honest accounting of why it
  didn't hold if it's being used to illustrate a failed reform attempt.
- Do not use: This figure in any voiceover claim until its date and scope are
  pinned down — right now it risks either double-counting or an apples-to-oranges
  comparison against the Aug 2026 figures.
- Safe fallback wording: omit this figure from the script entirely unless a firm
  date/scope is established; the existing Aug 2026 figures carry the narrative
  without it.
- Status: OPEN
