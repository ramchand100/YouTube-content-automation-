# Research Brief — Episode 16: How Pakistan's Tax System Actually Works

**Angle:** How Pakistan's Tax System Actually Works
**Script:** `scripts/16_pakistan_tax_system.md` (not yet written)
**Claim ledger:** `research/claim-ledgers/16_pakistan_tax_system_claims.csv`
**Source register:** `research/source-registers/16_pakistan_tax_system_sources.csv`
**Research date:** 2026-08-28
**Status:** Research complete, pending user review before scripting. Several fast-moving figures and one direct/indirect-tax-share discrepancy remain flagged `[VERIFY]` — see Section 7.

---

## 1. Approved angle

**How Pakistan's Tax System Actually Works**

| Field | Content |
|-------|---------|
| Lens | Institutional / structural explainer · Hidden cost transfer · Policy versus ground reality |
| One-sentence framing | Pakistan's tax system looks like an income-tax system on paper but functions like a transaction-tax system in practice — most of what the state collects is withheld or taxed at the point of a purchase, a bank transfer, or an import, split awkwardly between a federal board and provincial authorities, which is exactly why it can feel crushing to the documented minority while collecting so little overall. |
| Central question | How does money actually move from a Pakistani's pocket to the state, and why does so little of it end up as usable government revenue? |
| Tentative thesis | Pakistan's low tax-to-GDP ratio and its documented population's high felt burden are two symptoms of the same design: income tax is collected mostly through withholding rather than filed returns, indirect taxes (sales tax, customs) do more revenue work than income tax, the 18th Amendment split federal and provincial tax authority in ways that let whole categories of income (agriculture, services) fall through the cracks, and the filer/non-filer system tries to patch the resulting gap rather than close it. |
| Main entities and institutions | FBR, provincial revenue authorities (PRA, SRB, KPRA, BRA), Ministry of Finance, National Finance Commission (NFC) award, IMF program conditionality |
| Deliberate exclusions | Deep case studies of any single evasion mechanism (real estate valuation gaps, trader-lobby political history, agri-tax reform details) — each gets one clear mention as an example of the structure, not a full investigation; corporate tax policy debates (super tax) beyond a brief mention |

(Copied from `topics/ANGLE_TEMPLATE.md`, approved 2026-08-28.)

---

## 2. Central question

How does money actually move from a Pakistani's pocket to the state, and why does so little of it end up as usable government revenue?

---

## 3. Tentative thesis

Pakistan's low tax-to-GDP ratio and its documented population's high felt burden are two symptoms of one design: income tax is collected mostly through withholding, not filed returns; indirect taxes do more revenue work than income tax; the 18th Amendment split federal/provincial tax authority in ways that let whole categories of income fall through; and the filer/non-filer system patches the resulting gap rather than closing it.

---

## 4. Claims required (from the 7-part structure)

1. What is Pakistan's current tax-to-GDP ratio, and how does it compare historically and regionally?
2. What did the 18th Amendment (2010) actually change about who taxes what — federal vs. provincial?
3. What is the NFC award, what does the current (7th, 2010) formula distribute, and has it been updated since?
4. What share of FBR revenue is direct tax vs. indirect tax (sales tax, customs, FED)?
5. What share of "direct" income tax is actually collected via withholding rather than filed/assessed returns?
6. What does the withholding tax regime cover, and which categories generate the most revenue?
7. What is the filer/non-filer system, when was it introduced, and what does it currently restrict?
8. How effective is the filer/non-filer patch — does it verify real income, or just add a toll for staying undocumented?
9. Where does the system stop reaching income — cash retail, agriculture, real estate — and what is one concrete, sourced example of each?
10. What does the IMF program say about Pakistan's tax-to-GDP trajectory and tax-base-broadening commitments?
11. What provincial-level services-tax collection numbers exist (PRA/SRB/KPRA/BRA), and how do they compare to federal collection?

---

## 5. Raw findings

### 5.1 FBR Revenue Division Yearbook 2024-25 (primary — read directly)

Source: FBR, *Revenue Division Year Book 2024-25*, published FBR.gov.pk (accessed via full-text extraction, 2026-08-28).

- Total FBR net collection, FY2024-25: **Rs 11,744.3 billion**, up 26.3% YoY from Rs 9,299.1 billion in FY2023-24.
- Direct taxes: **Rs 5,791.7 billion = 49.3%** of total FBR collection (+27.8% YoY).
- Indirect taxes: **Rs 5,952.6 billion = 50.7%** of total FBR collection (+24.8% YoY), composed of:
  - Sales tax: Rs 3,901.4 billion (33.2% of total)
  - Customs duty: Rs 1,284.6 billion (10.9% of total)
  - Federal Excise Duty: Rs 766.6 billion (6.5% of total)
- Tax-to-GDP ratio (FBR-only, federal): **10.3% in FY2024-25**, up from **8.8% in FY2023-24**. Of this, direct taxes contribute 5.1 points of GDP and indirect taxes 5.2 points.
- Domestic-stage collection (vs. import-stage) rose from 63.6% of total (FY23-24) to 64.8% (FY24-25).
- **Withholding tax (WHT): Rs 3,381.5 billion in FY2024-25** (Rs 2,739.1bn in FY23-24, +23.5% YoY) — the document states this equals **59% of total income tax collection** and **28.8% of total FBR collection**.
- Income tax composition (FY24-25, per the Yearbook's own breakdown): Withholding tax 59%, Advance tax 33%, Collection on Demand (enforcement/arrears) 5% (up from 3% the prior year). By subtraction, the remainder — tax paid voluntarily with a filed return, "with return" payments — is approximately **3%** of income tax collected. This is a load-bearing figure for Part 4 of the structure: only a small single-digit share of income tax arrives through the act of filing and paying against a self-assessed return; the rest is withheld, paid in advance, or extracted by enforcement.
- Withholding tax by category, FY2024-25 vs FY2023-24 (Rs million):

| Category | FY24-25 | FY23-24 | Growth |
|---|---:|---:|---:|
| Contracts | 737,715 | 530,724 | +39.0% |
| Salaries | 605,593 | 391,362 | +54.7% |
| Bank interest & securities | 475,127 | 482,861 | −1.6% |
| Imports | 421,766 | 380,335 | +10.9% |
| Dividends | 162,107 | 144,191 | +12.4% |
| Electricity bills | 144,371 | 129,815 | +11.2% |
| Telephone | 123,434 | 99,431 | +24.1% |
| Exports | 122,271 | 98,973 | +23.5% |

**Classification: VERIFIED** for all figures above — read directly from the primary FBR document.

### 5.2 OECD Revenue Statistics in Asia and the Pacific 2025 — Pakistan country note (primary international institution — read directly)

- Pakistan's tax-to-GDP ratio: **10.5% in 2023** (OECD's own calendar-year classification, methodologically distinct from FBR's fiscal-year, FBR-only figure above).
- Asia-Pacific regional average, 2023: **19.5%** — Pakistan sits roughly 9 percentage points below the regional average.
- Tax revenue breakdown, 2023 (% of GDP): Income/profits/capital gains taxes 4.29%; taxes on goods and services 6.05% (of which VAT/GST 3.41%, other specific goods-and-services taxes 2.60%); other taxes 0.21%.
- % of total tax revenue: Income/profits/capital gains 40.7% (the single largest category by the OECD's classification); VAT/GST 32.3%.
- Direct quote: "the highest share of tax revenues in Pakistan in 2023 was derived from taxes on income, profits and capital gains (40.7%)."

**Classification: VERIFIED.** Note for the script: the OECD's 40.7%-from-income-tax framing and the FBR Yearbook's 49.3% direct-tax share are not contradictory — they are different classification systems (OECD groups by economic base; FBR groups by its own "direct/indirect" administrative categories) and different reference years (2023 calendar vs FY24-25). Use one consistent framework in the script, sourced explicitly, rather than blending the two.

### 5.3 IMF Country Report No. 25/109 (2025) — Pakistan EFF review (primary — read directly)

- Direct quote: "To support this effort, revenue administration measures to reduce the compliance gap will continue... ensuring general government revenue reaches 12.3 percent of GDP in FY25, including FBR collections of 10.6 percent of GDP."
- General government revenue (federal + provincial combined) is projected at **15.2% of GDP in FY26** per the extraction — this is a large one-year jump from the FY25 figure and should be re-verified against the report's actual data tables before it is used in the script; flagged `[VERIFY]`.
- On agricultural income tax: "In a significant achievement, provinces have amended their AIT regimes to align with federal income tax rules, with implementation starting January 2025 and collection in September 2025." The report also notes the original AIT legislative deadline (end-October 2024) was missed, with the legislation "subsequently passed in February 2025."
- On base-broadening: "Efforts to improve compliance and expand the tax base will be monitored under a modified QPC [quantitative performance criterion] on the number of new taxpayers with a positive tax liability."

**Classification: VERIFIED** for the direct quotes above (read from the primary IMF document). The FY26 general-government-revenue figure (15.2%) is flagged `[VERIFY]` — plausibility check needed against the report's own data annex before scripting.

### 5.4 IMF Country Report No. 24/002 (2024) — Pakistan SBA review (primary — read directly)

- This document covers the 2023 Stand-By Arrangement (SBA), not the EFF that followed it.
- "The FBR has... successfully registered 1.1 million new filers, from which 170,999 new returns have been obtained through enforcement measures."
- At the time of this (2024) report, FBR revenue was projected at 8.8–8.9% of GDP for FY25–29 — a projection since superseded by the higher actual FY24-25 outturn (10.3% per the FBR Yearbook) and by the EFF's higher FY25 target (10.6%, per §5.3).

**Classification: VERIFIED** (read directly). Useful in Part 7 as an illustration of how quickly IMF program-year projections for Pakistan's tax-to-GDP trajectory have moved — worth noting the trajectory rather than treating any single projection as durable.

### 5.5 7th NFC Award, 2010 (primary — read directly)

Source: 7th National Finance Commission Award text, hosted by the KP Finance Department (finance.gkp.pk).

- Vertical split of the federal divisible pool: provinces' share rose to **56.00%** in 2010-11 and **57.50%** from 2011-12 onward; the federal government retained **42.50%**. This was a large increase from the roughly 49% provincial share under the prior (1997) award.
- Horizontal distribution formula (how the provincial share is split among the four provinces) — weighted multi-indicator formula replacing the previous population-only formula:

| Indicator | Weight |
|---|---:|
| Population | 82.00% |
| Poverty / backwardness | 10.30% |
| Revenue collection / generation | 5.00% |
| Inverse population density | 2.70% |

- Resulting province-wise shares of the provincial pool: **Punjab 51.74%, Sindh 24.55%, Khyber Pakhtunkhwa 14.62%, Balochistan 9.09%.**
- FBR's collection charge (the fee the federal government deducts before distributing the divisible pool) was cut from 5% to 1%, enlarging the pool available for distribution.
- **1% of the net divisible pool** was earmarked specifically for Khyber Pakhtunkhwa in recognition of its role as a "frontline province in the war on terror," for the full award period.
- Sindh received a compensatory grant equal to 0.66% of the divisible pool after subvention and octroi/zilla-tax grants-in-lieu were abolished.

**Classification: VERIFIED** — read directly from the primary award document.

### 5.6 NFC award status since 2010 (secondary, corroborating — search-derived, not independently opened as a single primary document)

Multiple secondary sources (Dawn, PIDE, SDPI, Wikipedia's National Finance Commission Award entry) converge on the same account: the **8th NFC was constituted on 21 July 2010 but never produced a new award** because the 7th Award (signed December 2009, effective 2010) was still in its implementation phase; the **9th NFC was constituted on 24 April 2015**. No source found in this research confirms a superseding award has been agreed since 2010. Under Article 160(6) of the Constitution, the prior award's formula continues to apply by default until a new one is agreed — meaning the 7th NFC Award's 57.5/42.5 split, described above, is understood to remain the operative formula today.

**Classification: VERIFIED (production-confirmed 2026-08-28).** The historical sequence (8th constituted without an award, 9th constituted 2015) is corroborated across multiple sources, and the production team has confirmed the 7th NFC Award's formula remains current in 2026 — no superseding award has been signed. Safe to state flatly in the script.

### 5.7 18th Amendment (2010) — federal/provincial tax devolution (secondary — search-corroborated; primary constitutional text could not be opened, see discarded sources)

Multiple sources (Business Recorder, Dawn, provincial revenue authority materials) converge on the same account:

- **Retained by FBR (federal):** income tax (on non-agricultural income), sales tax on goods, customs duty, federal excise duty.
- **Devolved to provinces:** capital gains tax, estate duty, capital value tax, wealth tax on immovable property; the provinces also gained the authority to legislate and self-collect **sales tax on services** (previously a federally-administered residual arrangement); and **agricultural income tax**, which the Constitution had already assigned to the provinces, remained a provincial subject that the 18th Amendment reaffirmed and provinces continued to administer at their own discretion.
- Following devolution, provinces created their own collecting authorities for sales tax on services: **Sindh Revenue Board (SRB, founded 2010)**, **Punjab Revenue Authority (PRA, founded 2012)**, **Khyber Pakhtunkhwa Revenue Authority (KPRA, founded 2013)**, and **Balochistan Revenue Authority (BRA)**. Founding years for SRB/PRA/KPRA confirmed by production team, 2026-08-28 (REPORTED — no primary founding-legislation document opened in this pass). BRA's Sales Tax on Services regime is confirmed to have taken effect 1 July 2015 (BRA's own stated commencement date, general rate 15%, 19.5% on telecom services).
- **Jurisdictional dispute:** Punjab and KP tax services on a destination basis (services consumed in their jurisdiction); Sindh taxes on an origin basis (services originating in its territory), which Dawn reports has led to double taxation for some taxpayers and litigation.

**Classification: REPORTED**, attributed explicitly to the outlets above. The overall shape of the devolution (which taxes went where) is corroborated across several independent sources and can be treated with reasonable confidence; specific provincial-authority founding dates are `[VERIFY]`.

### 5.8 Provincial sales-tax-on-services collection, FY2024-25 (mixed tiers — see notes)

- **Sindh (SRB):** Sindh Sales Tax (SST) collection of **Rs 284.38 billion** in FY2024-25, plus Rs 22.253 billion from the Sindh Workers' Welfare Fund / Sindh Companies Profits Workers' Participation Fund (SWWF/SWPPF), for total SRB collection of roughly **Rs 307.93 billion** — against a provincial government target of Rs 350 billion (i.e., collection fell short of target). Sourced from Profit by Pakistan Today, Business Recorder, and pkrevenue.com reporting on SRB's own released figures; a direct attempt to read SRB's FY2024-25 Annual Report PDF did not return extractable content (see discarded sources).
- **Punjab (PRA):** **Rs 270 billion** in FY2024-25, rising to Rs 368 billion in FY2025-26 (+36%). Sourced from Associated Press of Pakistan (APP, state news agency) and Profit reporting on PRA's own figures.
- **Khyber Pakhtunkhwa (KPRA):** **Rs 51.56 billion** total in FY2024-25 (against a Rs 47 billion target, +37% YoY), of which **Rs 40.3 billion** was sales tax on services and **Rs 11.26 billion** was Infrastructure Development Cess (IDC). Sourced from Profit reporting, corroborated by KPRA's own published release (kpra.gov.pk).
- **Balochistan (BRA):** No FY2024-25 collection figure was found in this research pass. **UNRESOLVED — flagged `[VERIFY]`.**

**Classification: REPORTED** for Sindh, Punjab, and KP figures (Tier-1 journalism reporting the authorities' own released numbers; not independently cross-checked against each authority's own primary annual report in every case). **UNRESOLVED** for Balochistan.

**Derived comparison (ESTIMATE, method shown):** Summing the three confirmed provincial totals — Sindh Rs 307.93bn + Punjab Rs 270bn + KP Rs 51.56bn ≈ **Rs 630 billion** in combined provincial services-tax-and-related collection for FY2024-25 (Balochistan excluded, so this understates the true provincial total) — versus the FBR's own federal sales-tax-on-goods collection of **Rs 3,901.4 billion** in the same year (§5.1). Even understated, provincial services-tax collection is roughly one-sixth the size of federal goods-sales-tax collection alone, illustrating the scale gap between the two systems referenced in Part 3. **Classification: ESTIMATE** — this comparison is my own arithmetic from the REPORTED figures above; label it as such in the script and do not present it as an official combined statistic.

### 5.9 Filer / non-filer system (REPORTED, multiple corroborating Tier-1 sources)

- The filer/non-filer distinction, with differentiated (higher) withholding tax rates for non-filers, was introduced by the **Finance Act 2014**.
- The **Tax Laws (Amendment) Act 2024** (folded into the **Finance Act 2025** / Finance Bill 2025-26) introduced **Section 114C**, defining an "**eligible person**" as someone who filed a return for the immediately preceding tax year and has declared, in their wealth statement, resources sufficient to justify the transaction; anyone else is an "**ineligible person**." Reported restrictions on ineligible persons include:
  - Closure of bank accounts with balances over Rs 1 million; restrictions on opening new current/savings accounts (except Asaan accounts); limits on cash withdrawals.
  - Blocked registration/transfer of immovable property above a Board-notified value.
  - Blocked booking, purchase, or registration of motor vehicles.
  - Blocked purchase of, or new accounts for, securities including debt securities and mutual fund units.
- **Implementation status:** The National Assembly Standing Committee on Finance and Revenue deferred Section 114C in early 2025 pending a demonstration that FBR's own online systems could support it; the FBR Chairman requested additional time to build the required technology. The provision was subsequently included in the Finance Bill for FY2025-26. Secondary reporting from 2026 describes it as "actively being used," with banks, excise/taxation departments, and property-registration authorities checking Active Taxpayer List (ATL) status — but this research pass did not find a primary FBR enforcement statistic confirming the scale of actual enforcement. **Flagged `[VERIFY]`.**
- **Stated rationale**, per government officials quoted in press coverage: broaden the tax base, increase documentation of the economy, and discourage staying outside the formal tax net by raising the cost of major transactions for the undocumented.

**Classification: REPORTED** throughout, attributed to Business Recorder, Profit by Pakistan Today, Express Tribune, PropPakistani, and 24NewsHD coverage, which converge on the same statutory description. The claim that Pakistan is unique among countries in formalizing a "non-filer" legal status (raised by one think-tank commentary, EPBDT) is an **ANALYSIS/opinion claim**, not independently verified against other countries' tax codes in this research pass — do not present it as settled fact.

### 5.10 Real estate valuation gap — one example for Part 6 (lower-tier sources, flagged)

- Multiple real-estate-industry sources (not primary/Tier-1) state that market transaction prices in Pakistan run roughly 5–10× the district-administration (DC) valuation rate and 2–4× the FBR's own notified property valuation rate, meaning declared transaction values for tax purposes are commonly a fraction of true market value.
- FBR was authorized to notify its own valuation tables (intended to sit closer to market value than DC rates) for major urban centres starting in 2016, with revisions in 2019 and 2022, and further city-by-city SRO revisions reported from October 2024 through 2026.

**Classification: ESTIMATE/REPORTED, flagged `[VERIFY]`.** The specific multiplier ranges come from real-estate industry blogs and advisory sites, not from FBR, DC, or an academic/government study directly compared side by side. Use this only as a qualitative, one-line illustration in Part 6 ("the FBR's own valuation tables still run well below open-market prices in most cities") rather than citing a specific multiplier as a hard verified figure, unless a primary FBR/PIDE source is located before scripting.

### 5.11 Agricultural income tax — one example for Parts 2 and 6 (VERIFIED via IMF report + corroborating press)

- Provinces were required, under IMF program conditionality, to harmonize their Agricultural Income Tax (AIT) regimes with federal personal/corporate income tax rates (up to 45% for high earners) by an original deadline of end-October 2024.
- All four provinces missed that deadline but subsequently passed legislation: **Punjab** (November 2024, first), **Khyber Pakhtunkhwa** (27 January 2025), **Balochistan** (3 February 2025), **Sindh** (4 February 2025).
- Implementation began January 2025, with collection starting September 2025 (per IMF Country Report 25/109, §5.3).
- Sindh's legislation, per press reporting, exempts income up to Rs 600,000 and applies a maximum 45% rate above Rs 5.6 million annually.

**Classification: VERIFIED** for the IMF-confirmed harmonization timeline and provincial passage dates (corroborated by Express Tribune, The Print, and other outlets); the specific Sindh threshold figures are **REPORTED**, attributed to press coverage rather than the Sindh AIT Act text itself, which was not directly opened in this pass.

### 5.12 Informal/undocumented economy size (ESTIMATE, wide disagreement)

Search-aggregated figures range from roughly 35% to 59% of GDP depending entirely on methodology:
- Ministry of Finance (per secondary reporting): "more than 40%" of GDP from the informal sector.
- World Bank (2022): informal economy valued at $457 billion, 35.6% of GDP-PPP.
- ILO and other national researchers: 35–40% of GDP.
- One monetary-approach academic study: 44.14% of GDP in 2022 (up from 11.17% in 1980), long-term average 28.33%.
- One figure citing Pakistan Labour Force Survey / Pakistan Economic Survey data: ~59% of GDP for FY2024-25.

**Classification: ESTIMATE, flagged `[VERIFY]`.** None of these figures were confirmed by directly opening the underlying primary report (World Bank report, PES chapter, or the academic study) in this research pass — all came through search-result synthesis. Given the width of the range (35–59%) and the total absence of methodological agreement, the script should either (a) cite one figure with its source and methodology named explicitly and not imply precision, or (b) simply state qualitatively that estimates place the informal economy at somewhere between one-third and three-fifths of GDP, which is itself the more defensible, verifiable claim.

### 5.13 Filer counts / Active Taxpayer List (ESTIMATE, high volatility, flagged)

The Active Taxpayer List (ATL) resets annually (in March, for the preceding tax year) and reported active-filer counts vary substantially by year and by source:
- 2021: ~2.5 million active filers out of ~7.1 million registered taxpayers.
- 2022: 5.73 million active taxpayers.
- 2023: 3.35 million.
- 2024: ~6 million (one source) / 4.5 million (another, cited by Arab News).
- 2025: figures ranging from 7.2 million (Arab News) to 8.3–8.47 million (TaxationPk and others) for what appears to be the same reporting period.

**Classification: ESTIMATE/REPORTED, flagged `[VERIFY]`.** The conflicting figures for the same nominal year likely reflect different snapshot dates within the ATL cycle (the list grows through the year as late filers register) rather than genuine disagreement, but this was not confirmed against FBR's own ATL statistics page directly. Before scripting any specific filer count, pull the figure directly from FBR's ATL portal on a specific date and cite that date explicitly — do not blend the secondary figures above into a single number.

### 5.14 Population context

Pakistan's population per the 2023 Digital Census (Pakistan Bureau of Statistics): **241.49 million** (241,499,431, excluding Gilgit-Baltistan and Azad Kashmir), up from 213.2 million in the 2017 census, at a 2.55% growth rate.

**Classification: REPORTED**, corroborated across Geo News, BOL News, and Islamabad Scene reporting of the PBS figure; not read directly from a PBS document in this pass. Given this is a stable, slow-moving figure (a decennial census result), it can reasonably anchor the "documented population" framing in Part 1, but cite PBS as the originating institution rather than the news outlets that reported it.

---

## 6. Verified figures (clean, citation-ready for script)

| # | Figure | Citation string |
|---|---|---|
| 1 | FBR's tax-to-GDP ratio reached 10.3% in FY2024-25, up from 8.8% in FY2023-24 | `[SOURCE: FBR Revenue Division Year Book 2024-25, 2025]` |
| 2 | FBR collected Rs 11,744.3 billion in net taxes in FY2024-25, a 26.3% increase over FY2023-24 | `[SOURCE: FBR Revenue Division Year Book 2024-25, 2025]` |
| 3 | Direct taxes made up 49.3% of FBR's total collection in FY2024-25 (Rs 5,791.7bn); indirect taxes made up 50.7% (Rs 5,952.6bn) | `[SOURCE: FBR Revenue Division Year Book 2024-25, 2025]` |
| 4 | Sales tax alone brought in Rs 3,901.4 billion (33.2% of total FBR collection) in FY2024-25 — more than all direct taxes combined minus withholding | `[SOURCE: FBR Revenue Division Year Book 2024-25, 2025]` |
| 5 | Customs duty brought in Rs 1,284.6 billion, 10.9% of total FBR collection, in FY2024-25 | `[SOURCE: FBR Revenue Division Year Book 2024-25, 2025]` |
| 6 | Withholding tax collected Rs 3,381.5 billion in FY2024-25 — 59% of all income tax collected and 28.8% of everything FBR collected | `[SOURCE: FBR Revenue Division Year Book 2024-25, 2025]` |
| 7 | Of income tax collected in FY2024-25, withholding tax accounted for 59%, advance tax for 33%, and enforcement-driven "collection on demand" for 5% — leaving roughly 3% paid voluntarily with a filed return | `[SOURCE: FBR Revenue Division Year Book 2024-25, 2025]` |
| 8 | Salary withholding tax collection rose from Rs 391.4 billion to Rs 605.6 billion between FY2023-24 and FY2024-25, a 54.7% increase | `[SOURCE: FBR Revenue Division Year Book 2024-25, 2025]` |
| 9 | Pakistan's tax-to-GDP ratio (10.5% in 2023) sat roughly 9 percentage points below the Asia-Pacific regional average of 19.5% | `[SOURCE: OECD, Revenue Statistics in Asia and the Pacific, 2025]` |
| 10 | Under the 7th NFC Award (2010), provinces receive 57.5% of the federal divisible pool and the federal government retains 42.5% | `[SOURCE: 7th National Finance Commission Award, 2010]` |
| 11 | The provincial share of the NFC divisible pool is split Punjab 51.74%, Sindh 24.55%, Khyber Pakhtunkhwa 14.62%, Balochistan 9.09% | `[SOURCE: 7th National Finance Commission Award, 2010]` |
| 12 | The IMF's EFF program targets FBR collections of 10.6% of GDP and general government revenue of 12.3% of GDP for FY2024-25 | `[SOURCE: IMF Country Report No. 25/109, 2025]` |
| 13 | Under IMF program conditionality, all four provinces passed legislation harmonizing agricultural income tax with federal rates by February 2025, with collection beginning September 2025 | `[SOURCE: IMF Country Report No. 25/109, 2025]` |
| 14 | Pakistan's population reached 241.49 million in the 2023 census | `[SOURCE: Pakistan Bureau of Statistics, 2023 Digital Census]` |

---

## 7. `[VERIFY]` flagged items

| # | Item | Why flagged | What to do before recording |
|---|---|---|---|
| ~~V1~~ | ~~Whether the 7th NFC Award's 57.5/42.5 formula remains the current operative formula~~ | **RESOLVED 2026-08-28** — confirmed by production team: the 7th NFC Award (2010) remains the current, operative formula; no superseding award has been signed. Classification upgraded to VERIFIED on production confirmation (no new primary document opened). | — |
| V2 | Direct/indirect tax share discrepancy: FBR Yearbook shows a near-even 49.3%/50.7% split for FY24-25; a separate search-derived summary attributed to the Pakistan Economic Survey claims indirect taxes are "more than 60%" of total FBR collection | The two figures conflict and may reflect different fiscal years, different classification systems (e.g., treating withholding as functionally indirect), or an imprecise secondary summary | Open the actual Pakistan Economic Survey 2025-26 fiscal chapter directly (attempted in this pass but PDF extraction failed) and reconcile against the FBR Yearbook's own numbers before the script states a specific split |
| V3 | IMF-projected general government revenue of 15.2% of GDP for FY2026 | A one-year jump from 12.3% (FY25) to 15.2% (FY26) is large and may reflect an extraction error rather than the report's actual figure | Re-open IMF Country Report 25/109's data tables directly and confirm the FY26 figure before using it |
| V4 | Balochistan Revenue Authority (BRA) FY2024-25 collection figure | Not found in this research pass | Search BRA's own site/annual report or Balochistan budget documents directly |
| ~~V5~~ | ~~Exact founding years of SRB, PRA, and KPRA~~ | **RESOLVED 2026-08-28** — confirmed by production team: SRB founded 2010, PRA founded 2012, KPRA founded 2013. Classification: REPORTED (production-confirmed; no primary founding-legislation document opened in this pass — cite a primary source before broadcast if one becomes available). | — |
| V6 | Whether Section 114C (non-filer transaction restrictions) is actually being enforced at scale in 2026, vs. still administratively deferred | Secondary reporting is inconsistent — some sources describe it as deferred pending FBR system readiness (early 2025), others describe active enforcement in 2026 | Check FBR's own current guidance/circulars and recent press for enforcement statistics before stating enforcement as a settled fact |
| V7 | Informal economy size as % of GDP | Estimates range from 35% to 59% of GDP depending on methodology, with no primary source opened directly | Either name one source and its explicit methodology, or state the range qualitatively rather than a single number |
| V8 | Active Taxpayer List / filer counts for the current tax year | Conflicting figures (7.2m–8.5m) for what appears to be the same year across different secondary sources | Pull the figure directly from FBR's ATL portal on a specific, cited date |
| V9 | Real estate market-value-to-DC/FBR-valuation-rate multiplier (5–10x DC, 2–4x FBR) | Sourced only from real-estate industry blogs, not FBR/PIDE/academic sources | Either find a primary/academic source or use only a qualitative, unquantified version of the claim |
| V10 | IMF's cited "tax capacity" estimate of 12.9% of GDP vs. actual ~10% collection | Came through search synthesis attributed to the IMF but not confirmed by directly opening the specific IMF paper making this estimate | Locate and directly read the specific IMF paper (likely an Article IV or selected-issues paper) before citing this figure |

---

## 8. Discarded sources

| Source | Reason discarded |
|---|---|
| PIDE (pide.org.pk) — "Pakistan's Tax System: Advancements, Challenges and Trillion-Dollar Future" | Returned HTTP 403 on direct fetch; content only available via search-engine summary, which the research rules treat as insufficient on its own for a load-bearing claim. Not used as a cited source; only search-summary framing referenced informally above. |
| Business Recorder opinion piece, "Beyond tax-to-GDP ratio" | Returned HTTP 403 on direct fetch; could not confirm author or direct quotes. Not used. |
| Sindh Revenue Board Annual Report 2024-25 (direct PDF) | Attempted direct extraction via full-text fetch; returned no usable content (empty/failed parse). SRB's FY24-25 figures were instead sourced from Tier-1 journalism reporting on SRB's own released numbers (see §5.8), which is a weaker evidentiary basis and is reflected in the REPORTED classification rather than VERIFIED. |
| CEIC Data — "Pakistan Tax Revenue: % of GDP" | Third-party data aggregator/paywall service; appeared in search results but was not opened. Given the FBR Yearbook and OECD country note provide the same category of figure from primary/near-primary sources, CEIC was not used. |
| Wikipedia (Economy of Pakistan; 2024-25 Pakistan federal budget; National Finance Commission Award) | Not a primary or journalistic source per the research hierarchy; used only informally to cross-check dates already corroborated elsewhere, never cited directly. |
| Various tax-advisory and property-marketing blogs (e.g. paktaxcalculator.pk, waystax.com, taxationpk.com, various FBR-valuation-rate marketing sites) | Secondary, commercially motivated content (tax-filing services, real estate agencies). Used only for corroborating widely-reported statutory facts (e.g. that a filer/non-filer distinction exists), never as the sole source for a quantitative claim. |
| Social media / forum content | None encountered as a candidate source; excluded per research rules as a standing policy. |

---

## 9. Counterarguments and how they are addressed

**Counterargument 1: The tax-to-GDP ratio is a flawed or overused headline metric — Pakistan's low ratio partly reflects a genuinely large informal/agricultural economy, not just administrative failure.**
Response: The script should not present the low tax-to-GDP ratio as evidence of pure incompetence or malice. The OECD comparison (§5.2) and the IMF's own "tax capacity" framing (§5.12/V10, pending verification) point toward Pakistan's low per-capita income, large agricultural sector, and large informal economy as structural constraints on any tax system, not just this one. The script's thesis already accounts for this by focusing on *design* (withholding-heavy collection, federal/provincial split, indirect-tax reliance) rather than claiming the low ratio is simply a failure of will.

**Counterargument 2: The filer/non-filer system, whatever its flaws, has coincided with rising withholding tax collection and a growing ATL — it may be "working" in a narrow revenue sense even if it does not verify real income.**
Response: This is a fair complication documented in the research (§5.9, §5.13): reported ATL figures and WHT collection have both grown. The script should hold two things in tension rather than dismissing the system outright — it plausibly increases toll-collection and documentation *at the margin* of specific big-ticket transactions, while critics and the research itself (via the EPBDT commentary, an ANALYSIS-level claim) note it does not require verified income or wealth beyond a self-declared wealth statement. Present this as an open question rather than a settled failure or a settled success.

**Counterargument 3: Provinces are not simply "letting income fall through the cracks" — agricultural income tax has, in fact, just been legislated in all four provinces (§5.11).**
Response: This is directly incorporated into the structure rather than avoided. Part 6 ("Where the System Stops") should note the AIT harmonization as the most recent, ongoing attempt to close this specific gap — while being honest that implementation only began in 2025 and collection in September 2025, meaning the historical gap the episode describes has been real for decades and its closure is unproven, not that reform has not been attempted at all.

**Counterargument 4: The 18th Amendment's provincial devolution was a deliberate, defensible federalism reform, not simply a design flaw that created tax gaps.**
Response: The devolution of taxing power to provinces (§5.7) was a broader constitutional and political reform with its own rationale (provincial autonomy, addressing decades of centralization grievances) that this episode's deliberate exclusions correctly keep out of scope. The script should describe the fiscal *consequence* — jurisdictional disputes over services tax (§5.7), uneven provincial capacity (§5.8's collection-figure gap between Sindh/Punjab and KP/Balochistan) — without implying the 18th Amendment itself was a mistake, which is outside this episode's remit.

---

## 10. Stakeholder map

| Stakeholder | Role | What they want | Constraint |
|---|---|---|---|
| FBR (federal) | Owner/operator of federal tax collection (income tax on non-agri income, sales tax on goods, customs, FED) | Meet IMF-linked revenue targets; expand the documented tax base | Politically costly to enforce against powerful undocumented sectors (retail, real estate); administrative/systems capacity lags legislated reforms (e.g., Section 114C delay) |
| Provincial revenue authorities (PRA, SRB, KPRA, BRA) | Operators of provincial sales-tax-on-services and (since 2025) agricultural income tax collection | Grow provincial own-source revenue independent of the NFC transfer | Much smaller collection base than FBR; inter-provincial jurisdictional disputes (origin vs. destination taxation) create litigation and taxpayer double-taxation |
| Ministry of Finance / NFC | Regulator and vertical/horizontal revenue-distribution designer | Balance federal fiscal space against provincial autonomy commitments | No NFC award has been renegotiated since 2010 despite population and needs shifting; politically difficult to reopen |
| IMF (capital provider / conditionality-setter) | External program lender setting tax-to-GDP and base-broadening benchmarks | Durable increase in Pakistan's tax-to-GDP ratio, verified by structural benchmarks | Limited direct enforcement power beyond program disbursement leverage; relies on Pakistani legislative and administrative follow-through |
| Salaried, documented filers (withholding-taxed employees) | "Customers" of the system in the sense of being its most captured payers | Want tax burden to feel proportionate to income and connected to services received | Withheld before receiving income; least able to avoid or negotiate their tax exposure (605.6bn salary WHT, §5.1) |
| Non-filers / undocumented cash economy participants | Largely outside the direct-tax net but still pay indirect taxes on every purchase | Want to avoid formal documentation costs (audits, wealth disclosure) | Face rising transaction-level restrictions (Section 114C) without necessarily facing income verification |
| Agricultural income earners | Historically lightly taxed under provincial AIT regimes | Preserve historical low-tax treatment | Now subject to harmonization with federal rates (up to 45%) as of 2025 under IMF conditionality |
| Real estate buyers/sellers | Beneficiaries of the historical DC-rate/market-rate gap | Minimize documented transaction value | FBR valuation tables have been narrowing this gap since 2016, with further revisions through 2024-2026 |
| General population / losers-by-omission | Bear the indirect-tax burden (sales tax, customs) regardless of documentation status, while public services funded by that revenue remain constrained by the low overall tax-to-GDP ratio | Want lower prices and better public services | No direct lever over the structural design described in this episode |

---

## Sources block for this brief

See `research/source-registers/16_pakistan_tax_system_sources.csv` for the complete list of sources consulted (not just cited).
