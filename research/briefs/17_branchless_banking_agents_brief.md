# Research Brief — Episode 17: The Agent Economy That Banked Pakistan's Unbanked

**Angle:** The Agent Economy That Banked Pakistan's Unbanked
**Script:** `scripts/17_branchless_banking_agents.md` (not yet written)
**Claim ledger:** `research/claim-ledgers/17_branchless_banking_agents_claims.csv`
**Source register:** `research/source-registers/17_branchless_banking_agents_sources.csv`
**Research date:** 2026-08-30
**Status:** Research complete, pending user review before scripting. **Read Section 8 before scripting** — it covers the two highest-risk claims in the angle (the personal-account workaround and the free-cash-in mandate) and what was and wasn't found.

---

## 1. Approved angle

*(Copied from `topics/angles/17_branchless_banking_agents_angle.md`, approved 2026-08-29.)*

### The Agent Economy That Banked Pakistan's Unbanked

| Field | Content |
|-------|---------|
| Lens | Money and unit economics · Winners and losers · Policy versus ground reality · Informal versus documented economy · Future transition |
| One-sentence framing | A network of small shopkeepers turned into cash-in/cash-out agents for Easypaisa and JazzCash actually gave tens of millions of Pakistanis their first mobile-wallet access without a bank branch — but the same unit economics that made the network spread fast in cities is why it still thins out exactly where financial inclusion was supposed to matter most, and why a chunk of that economy runs on workarounds the companies never see. |
| Central question | How does a branchless-banking agent actually make money on cash-in/cash-out transactions, how do agents' own workarounds — routing cash-outs through personal accounts to avoid the company's cut, and charging for a cash-in service that's supposed to be free — reveal a gap between the official commission structure and what actually happens at the counter, and does all of that explain both where the network reached and why an instant, free payment rail like Raast could now undercut the model that built it? |
| Tentative thesis | Agent commission structures set by the mobile wallet operators made agent density a function of transaction volume and liquidity-float cost, not policy intent — agents clustered where volume was already high and stayed thin in the low-volume rural markets financial-inclusion policy explicitly targeted. On top of that official structure, a real but undocumented layer of agent-side workarounds (routing cash-outs as personal transfers to avoid the company's cut, charging for a cash-in service mandated to be free) means the agent's actual take is often higher than the official model describes. And because Raast increasingly lets transactions skip the cash-conversion step this whole economy is built on, the agent network's core revenue moment is now under threat from the same central bank that once helped standardize it. |
| Main entities and institutions | State Bank of Pakistan (branchless banking regulatory framework, Raast, 1LINK), Easypaisa / Telenor Microfinance Bank, JazzCash / Mobilink Microfinance Bank, agent shopkeepers, Karandaaz/Financial Inclusion Insights survey data, World Bank Global Findex |
| Evidence required | SBP branchless banking quarterly/annual reports (active agent counts, transaction volumes, any geographic breakdown); SBP's branchless banking regulations on mandated free cash-in (to corroborate the overcharging practice); any reporting on agent malpractice, complaints, or SBP consumer-protection action; Karandaaz/FII survey data on rural-vs-urban and gender gaps; published agent commission rate structures; Raast transaction-volume and merchant/QR adoption data; World Bank Findex Pakistan data |
| Pakistani economic relevance | This is the physical infrastructure letting a huge share of the population move money without a bank account — its real reach, and its real informal leakage, determines who actually benefits from every other digital-payments push (Raast, BISP aid disbursement, e-commerce) |
| Audience consequence | Fintech builders need the real unit economics (official and unofficial) of the agent layer they depend on; policy-focused viewers get an honest read on how much "financial inclusion" claims match ground reality |
| Deliberate exclusions | A full investigation of Raast's own adoption mechanics and history is excluded — that's a separate episode already in the topic backlog. Here, Raast appears only as the threat to the agent commission model. SadaPay/NayaPay app-only neobanks and smartphone-based fintech lending are also excluded (no physical agent network, different model). |
| Main weakness / research risk | Agent-level profitability data likely isn't public — this leans on aggregate SBP/telco figures and industry surveys rather than agent-level primary data. The cash-out/cash-in workaround practice needs independent corroboration (SBP's free-cash-in mandate, any malpractice reporting) rather than resting on a single account — if it can't be corroborated, the script states it more cautiously as "a practice described by industry sources" rather than an established fact. Whether Raast is *already* measurably eroding agent cash-in/cash-out volumes, versus being a plausible-but-not-yet-visible risk, needs to come from actual data. |

**Approval:** approved 2026-08-29, by user.

---

## 2. Central question

How does a branchless-banking agent actually make money on cash-in/cash-out transactions, how do agents' own workarounds reveal a gap between the official commission structure and ground reality, does that economics explain where the agent network reached and where it didn't, and why does SBP's Raast instant-payment rail now threaten the commission model that built this network?

---

## 3. Tentative thesis

See table above. Restated briefly: official commission economics (transaction-volume-driven, liquidity-float-constrained) explain the agent network's urban-heavy geography better than policy intent does; a separate, harder-to-document layer of agent-side workarounds may push real agent take above the official model; and Raast's free, instant rail threatens the cash-conversion step this entire commission structure depends on.

**This research pass materially qualifies two legs of that thesis — see Section 8.** The workaround claim could not be independently corroborated for Pakistan, and the best available research on it (CGAP, 2017) actually points the other way for Pakistan specifically. The Raast threat is well-supported as a *structural, anticipated* risk but not as an *already-measured* one.

---

## 4. Claims required (from the 7-part structure)

1. Scale of active mobile wallets and BB agents nationwide, most recent quarter (Part 1).
2. The rural/urban and gender gap in mobile money and financial inclusion generally (Part 1).
3. The official BB agent commission structure for cash-in and cash-out, and the liquidity/float cost agents bear (Part 2).
4. Break-even transaction volume implied by that commission structure (Part 2).
5. Whether SBP mandates free cash-in to the customer, and what the regulation actually says (Part 3).
6. Independent corroboration (or its absence) of agents routing cash-outs through personal accounts to avoid the company's commission cut (Part 3).
7. Independent corroboration (or its absence) of agents charging for cash-in despite any free-cash-in norm (Part 3).
8. Geographic/provincial distribution of BB agents, and whether it tracks the volume/liquidity economics of Parts 2-3 (Part 4).
9. Raast transaction-volume and merchant/QR (P2M) growth data (Part 5).
10. Whether Raast growth is already measurably displacing agent cash-in/cash-out volume, or is an anticipated risk (Part 5).
11. How the inclusion-narrative claims reconcile against the documented mechanism (Part 6).

---

## 5. Raw findings

### 5.1 Scale — SBP Branchless Banking statistics (Part 1)

- SBP's Branchless Banking Statistics for Jul-Sep 2025 (accessed via a Scribd-hosted mirror surfaced by Firecrawl search — **search-snippet only, primary PDF blocked, see S03**): "Number of Agents 757,727 [Jul-Sep 2025] 731,814 [Apr-Jun 2025] / Number of Active Agents 239,034 271,080 / Number of Accounts 141,560,617 135,876,186." Date accessed: 2026-08-30.
- Note the active-agent count *fell* quarter-on-quarter (271,080 → 239,034) even as total registered agents and total accounts both rose — a genuinely interesting, counter-intuitive data point worth flagging in Part 1/4, though it needs the full primary document to confirm it isn't a reporting-definition change.
- An earlier snapshot (Apr-Jun 2024, via a CollegeSidekick mirror of the same SBP series): "Number of Agents 666,682 / 651,672 ... Number of Active BB Agents 278,080 / 276,889 ... Number of Accounts 120,246,119..." — confirms continued growth in total agents and accounts across 2024-2025, though active-agent counts have fluctuated rather than climbed steadily.
- SBP Payment Systems Quarterly Review Q3 FY26 (Jan-Mar 2026), via search synthesis of press coverage (PDF itself blocked, see S02): retail payments across all formal channels reached 3.7 billion transactions worth Rs168.8 trillion (+9% QoQ by volume); 49% of accounts are linked to a mobile banking app or digital wallet; branchless banking mobile app users reached 95.8 million by March 2026 (Express Tribune); branchless banking agents facilitated ~155 million transactions worth Rs1.1 trillion in the quarter, while branchless banking players (wallet-to-wallet/digital) processed ~128 million transactions worth Rs99.5 trillion.

### 5.2 Rural/urban and gender gap — Karandaaz K-FIS 2024 (Part 1)

Verbatim/paraphrased findings, cross-corroborated across Dawn, Profit by Pakistan Today, The Express Tribune, Voicepk, and Brandsynario reporting on the same Karandaaz Financial Inclusion Survey (K-FIS) 2024 (the primary Karandaaz report itself was not independently opened — see Section 8 caveat):

- "Financial inclusion has increased fourfold, from just 8 percent in 2013 to 35 percent in 2024... driven by the rise of mobile money, now used by 30 percent of adults, up from less than 1 percent ten years ago."
- "Only 14 percent of women are financially included, compared to 56 percent of men. Mobile phone ownership among women stands at 46%... compared to 82% for men."
- "Among... mobile money wallet owners these gender gaps are much smaller, and... female mobile money wallet owners reported a higher level of comfort [with digital literacy]" — i.e. once a woman is a wallet owner, the residual gap narrows; the barrier is largely at the phone-ownership/registration stage.
- Regional financial inclusion: Punjab 40%, Islamabad 38%, Gilgit-Baltistan 33%.
- Raast awareness overall is only 15% of adults, with "24 percent of men report[ing] awareness of Raast compared to just 5 percent of women," the gap "widest in rural areas."

### 5.3 Official commission structure and float cost (Part 2)

- **CGAP's cross-market "typical model" (2017, Cook & Rashid)**: in the standard P2P wallet transfer, cash-in is described as free to the customer, with the agent earning a commission (paid by the provider); cash-out costs the customer a fee, and the agent again earns a commission. This is a general model description drawn across CGAP's four study markets (Pakistan, Ghana, Tanzania, Bangladesh) — useful for describing "how it's supposed to work," but it is not a Pakistan-specific regulatory citation.
- **CGAP's Pakistan-specific commission/pricing benchmark** (fieldwork ~2013-2016, published Aug 2017), on a US$20 reference transaction: customer pricing — formal OTC 5.70%, wallet "full loop" 1.85%; agent commission — formal OTC 1.95%, wallet cash-in/cash-out 1.30%. Provider gross margin: formal OTC ~3.75%, wallet ~0.5%. CGAP's own conclusion: "Formal OTC in Pakistan is much more profitable at a transaction level as compared to wallet, which appears to imply a vested interest in promoting OTC." These figures are now roughly a decade old and should be treated as historical benchmark, not current pricing.
- **Current (2026) published cash-out fee tiers**, via a secondary tariff-aggregator (Pakistan Observer, not the operators' own Schedule of Charges — see Section 8 and source register S24-S26 for the access-blocked primary): JazzCash charges Rs35 on withdrawals of Rs0-1,000, rising through a 13-tier slab to Rs400 on Rs40,001-50,000; Easypaisa charges Rs7 on Rs1-200, rising to Rs690 on Rs40,001-50,000. Neither aggregator source stated a specific cash-in fee figure — consistent with cash-in being treated as free/non-fee-bearing in the published consumer-facing tariff, though this absence is not the same as a confirmed regulatory mandate (see Section 8).
- **Structural incentive misalignment** (CGAP, "The EasyPaisa Journey from OTC to Wallets in Pakistan"): "The agent makes money every time there is an OTC transaction... On the M-wallet, fees are only paid at the activation of the wallet... While it is in our [operator's] interest to convert OTC to m-wallet, it is not in the agent's interest." This is a genuinely useful, CGAP-documented structural reason an agent's incentives diverge from the operator's — a real basis for Part 2/3 analysis, clearly CGAP's own framing, not a claim about any specific illicit workaround.
- **Liquidity/float cost**: CGAP and the multi-country Financial Inclusion Insights (FII) survey (which covers Pakistan among nine countries) both identify liquidity/float management as a leading operating cost and the top challenge cited by mobile-money agents generally. No Pakistan-specific percentage-of-cost figure was independently confirmed in this pass — treat this as a general, multi-country finding (ANALYSIS-tier), not a Pakistan-isolated statistic.
- **SBP's anti-overcharging control mechanism** (VERIFIED, direct primary-document read): Branchless Banking Regulations (rev. Dec 2019), Section 9.1(b): "AFIs must publish their schedule of charges for BB activities and services on quarterly basis for each calendar quarter and make it available at all its branches / agent locations / website. The charges cannot be increased during a quarter." This is real regulatory evidence that SBP treats fee transparency and fee-stability as a live consumer-protection concern in this market — useful context for Part 2/3, though it is *not* itself a free-cash-in mandate (see Section 8).
- **Break-even volume**: no Pakistan-specific agent break-even transaction-count figure was found in this pass (agent-level profitability data is not public, as the angle file itself anticipated). The commission percentages above (S12/S23) are the best available proxy for constructing an illustrative break-even calculation in the script, and any such calculation should be labeled ESTIMATE with the method shown.

### 5.4 The workaround/overcharging claim — SBP's free-cash-in premise and independent corroboration (Part 3, CRITICAL)

See Section 8 for the full, honest treatment. Summary of what was found:

- The 2019 SBP Branchless Banking Regulations, read in full, contain **no explicit textual clause mandating that cash-in be free of charge to the customer as a general rule**. The only "free of cost" language in the document concerns (a) viewing the last five transactions via the mobile channel, and (b) — in the separate Home Remittance Account (HRA) annexure only — account opening/closing charges and the cost of biometric verification, neither of which is a general cash-in rule.
- Profit by Pakistan Today (2021) is the strongest adjacent evidence found: an industry source told Profit that, to recoup revenue lost from SBP's IBFT fee waiver, operators "might resort to charging a fee for each cash-in at a branchless banking agent," calling this "contradictory to digital financial inclusion" since "financial inclusion could be disincentivized if they start telling people that they would have to pay to deposit their funds." This confirms the *industry norm* is that cash-in is expected/understood to be free, and that there was live commercial pressure (in 2021) to break that norm — but it is a statement about a possible future **company-level** policy shift, not evidence of an existing **agent-level** overcharging practice.
- No SBP consumer-protection circular, complaint-portal data, or Pakistani press investigation was found describing agents charging customers for cash-in in practice, or describing agents routing cash-out transactions through their own personal wallet/bank account (as an ordinary P2P transfer) specifically to avoid the operator's commission share.
- The single most relevant piece of research found — CGAP's 2017 four-country study, based on agent interviews, mystery-shopping, and Central Bank data — documents the *personal-account-routing workaround as a real, named phenomenon internationally* ("Direct deposit... a sending customer performs an unauthorized cash deposit directly onto the wallet of a registered user, typically to avoid transaction fees... popular in wallet markets"), but its own Pakistan-specific fieldwork placed **Pakistan in the "low informal OTC market" quadrant**, and its explicit conclusion was: "Do agents have a proverbial 'thumb on the scale' in promoting formal OTC... transactions? Not really... evidence from agent interviews and mystery shopping within each market suggests they do not typically have (or use) significant leverage to direct transactions." This is the closest rigorous test of the angle's specific mechanism for Pakistan, and it **cuts against, not for**, high prevalence — with the important caveat that the fieldwork is roughly a decade old (~2013-2016), predates Raast entirely, and predates the four-fold growth in wallet accounts since 2013.
- One non-citable data point was found and discarded: an unattributed Islamic-discussion-forum thread mentioning "some shopkeepers deduct Rs 10-20 extra" when sending/withdrawing small amounts. This is social-media-tier content per the source hierarchy and cannot be used as evidence, but its mere existence (people publicly asking whether such deductions are religiously permissible) is a small, non-citable signal that *some* version of ad hoc extra charging is part of ordinary Pakistani experience with these agents — it simply is not a source the brief can rely on.

### 5.5 Geographic distribution (Part 4)

Via Data Darbar Insights, an independent data-analysis blog citing SBP agent data as of December 2023 (secondary analysis of primary data, not independently re-derived from SBP's own portal — see Section 8):

- Punjab held 413,991 BB agents as of December 2023 — 63.72% of the national total, up from 62.99% in 2019 (a share larger than Punjab's population share).
- Agent density per 100,000 adults: Punjab 516 vs Balochistan 188 — a 2.74x gap.
- Fastest five-year (2019-2023) agent-count CAGR: Balochistan 27.1%, Gilgit-Baltistan 27.5% — rapid growth, but off a very low base.
- Provincial BB transaction value (2023): Punjab Rs11.06 trillion, Sindh Rs3.47 trillion, KP Rs2.7 trillion.

This pattern is directly consistent with the thesis's claim that agent density tracks pre-existing transaction volume (urban, higher-income, higher-liquidity markets) rather than financial-inclusion policy intent — Balochistan and GB's high *growth rates* off tiny bases show the network is still expanding into underserved territory, just far more slowly and from far behind.

### 5.6 The Raast threat (Part 5)

- Raast processed 742.1 million transactions worth Rs23.3 trillion in Q3 FY26 (Jan-Mar 2026) — of which P2P transactions were 664 million (+10% QoQ) worth Rs18.9 trillion, and Person-to-Merchant (P2M) transactions grew from 36.3 million to 55.9 million in a single quarter, with over 2.6 million merchants onboarded/registered by quarter-end.
- QR-based merchant payments reached 87.3 million transactions (+41% QoQ by volume, +63% by value) worth Rs0.5 trillion; 2.5 million QR-enabled merchant locations are now registered nationwide — but physical POS infrastructure lags far behind, at only 247,836 machines across 217,042 registered merchants as of March 2026 (Startup.pk), pointing to a real merchant-acceptance gap even as the rails scale.
- An easypaisa Digital Bank executive told Business Recorder / BR Research that cash needs to be made *more expensive* than digital in order to shift customer behaviour — a striking, on-record signal from inside one of the two dominant BB operators that the industry itself sees the cash-touching step (the agent's entire revenue moment) as the target of managed decline. (Access-blocked — see Section 8 caveat on this specific source.)
- **What the data does *not* show**: no dataset or analyst report found in this pass isolates a measured decline in branchless-banking agent cash-in/cash-out volume attributable specifically to Raast. In the same Q3 FY26 quarter that Raast processed 742 million transactions, BB agents themselves still facilitated ~155 million transactions worth Rs1.1 trillion, and total BB accounts/agents in the SBP quarterly series continued to grow through 2024-2025. P2M/QR volumes, while growing fast in percentage terms, remain small in absolute terms next to total Raast P2P volume and next to total agent-mediated cash volume. **The honest read: Raast is a structurally well-supported, industry-acknowledged anticipated risk to the agent commission model, not yet a measured, already-occurring erosion of agent revenue or volume.**

### 5.7 BISP as a live case study of the free-vs-paid distinction (useful for Parts 3, 5, 6)

SBP told a National Assembly Standing Committee (2026) that BISP beneficiaries withdrawing their cash-transfer payment through the new interoperable digital-wallet system will pay a PKR 280 cash-withdrawal fee — but that online transfers and Raast transactions will remain free, and that SBP will revise the schedule of charges every six months (cross-corroborated across ProPakistani, Business Recorder, PhoneWorld, and TechJuice). This is a clean, current, real-world illustration of the exact free-digital-vs-paid-cash distinction the episode's Part 5/6 argument rests on — worth considering as a concrete example in the script, separate from the harder-to-source agent-workaround claim.

---

## 6. Verified figures (clean, script-ready citations)

- SBP Branchless Banking Regulations (rev. 30 Dec 2019), §9.1(b): AFIs must publish quarterly schedules of charges; charges cannot be increased mid-quarter. `[SOURCE: State Bank of Pakistan, Branchless Banking Regulations, 2019]`
- SBP Branchless Banking Regulations (rev. 30 Dec 2019), §3.2(a)(v): cash-in and cash-out defined as a permissible activity via bank-branch counters, ATMs, and authorized agent locations — no fee/no-fee rule specified in the text. `[SOURCE: State Bank of Pakistan, Branchless Banking Regulations, 2019]`

**No other figure in this brief reaches VERIFIED status** — every scale, commission, and Raast figure was obtained via WebSearch/Firecrawl synthesis of a document this session could not directly open (SBP's own site returned HTTP 403 to every direct fetch attempt), or via secondary analysis/journalism. All are classified REPORTED, ESTIMATE, or UNRESOLVED in the claim ledger, each with its specific attribution. **This is the single biggest structural caveat on this brief** — see Section 8.

---

## 7. `[VERIFY]` flagged items

- **[VERIFY]** All SBP Branchless Banking quarterly-statistics figures (agent counts, account counts) — primary PDFs blocked (403) for this session; sourced via search-snippet mirrors only.
- **[VERIFY]** All SBP Payment Systems Quarterly Review Q3 FY26 figures (Raast volumes, retail-payment totals) — same access-blocked issue.
- **[VERIFY]** Current (2026) JazzCash/Easypaisa cash-out fee tiers — sourced from a secondary aggregator, not the operators' own Schedule of Charges PDF; fees revise quarterly per SBP regulation, so these must be re-checked immediately before recording.
- **[VERIFY]** The claim that SBP mandates free cash-in — no such explicit clause was found in the primary 2019 Regulations; treat as UNRESOLVED, not as an established regulatory fact, unless a human locates a more specific circular this pass missed.
- **[VERIFY]** The personal-account cash-out workaround and cash-in overcharging practice (the angle's own ground-knowledge claim) — no independent Pakistani corroboration found; the closest research (CGAP 2017) found low prevalence in Pakistan specifically. Per the angle file's own pre-agreed fallback, this must be scripted as "a practice described by industry sources" / a firsthand account under investigation, not as an established fact.
- **[VERIFY]** Whether Raast is already eroding agent cash-in/cash-out volume — no supporting dataset found; script as an anticipated/structural risk, not a measured one.
- **[VERIFY]** The Business Recorder "make cash more expensive than digital" interview — headline/gist confirmed via two independent searches, but the full article was never directly read (site blocked); confirm exact wording and speaker's title before quoting it in the script.
- **[VERIFY]** Karandaaz K-FIS 2024 figures — cross-corroborated across five press outlets reporting the same survey, but the primary Karandaaz report/deck itself was not independently opened.
- **[VERIFY]** Provincial agent-density figures (Punjab/Balochistan) — sourced from an independent analysis blog, not re-derived directly from SBP's EasyData portal (also fetch-blocked for this session).

---

## 8. Discarded sources

- **en.tohed.com Islamic discussion forum thread** on JazzCash/Easypaisa "extra charges" — discarded as unattributed social/forum content per the source hierarchy. Cannot be cited, even though it is suggestive.
- **web.archive.org (Wayback Machine)** — this tool environment cannot fetch web.archive.org at all ("Claude Code is unable to fetch from web.archive.org"), so it could not be used as a workaround for SBP's and Business Recorder's blocked pages. Noted so a future session doesn't waste a turn on it.
- **CGAP, "Comparing Branchless Banking in Bangladesh and Pakistan"** and the **World Bank's "Branchless Banking in Pakistan: A Laboratory for Innovation"** — both identified as strong, on-topic, primary/near-primary candidates via search, but not opened directly in this pass due to time/budget constraints. Not discarded for unreliability — flagged in the source register as follow-up candidates for a deeper pass, not used for any claim in this brief.
- **Facebook posts from SBP's official page** — used only very cautiously, as corroborating colour where consistent with other reporting, never as the sole basis for a claim, since a social-media caption is not a substitute for the underlying PDF report.

---

## 9. Counterarguments and how they are addressed

1. **"This network genuinely did expand financial access dramatically"** (the angle's own stated main counterargument). Addressed directly with the Karandaaz K-FIS trend line: financial inclusion rose from 8% (2013) to 35% (2024), and mobile money usage from under 1% to 30% of adults over the same period — a real, large, well-corroborated achievement that the script should hold in tension with the gap findings, not let the gap framing erase.
2. **"Maybe the free-cash-in premise is simply wrong, and cash-in was never guaranteed free."** Addressed head-on in Section 8: no blanket SBP regulation mandating free cash-in was found. The safest script framing is that free cash-in is an *industry-standard practice/expectation* (supported by CGAP's cross-market model description and by the 2021 Profit reporting showing operators themselves treat charging for cash-in as a violation of the inclusion mission), not a specific regulatory citation — the script should not claim SBP has "mandated" this unless a human locates a circular this pass missed.
3. **"Maybe agents don't actually have a strong incentive to run workarounds."** This is effectively what CGAP's own 2017 fieldwork concluded for Pakistan specifically (low informal-OTC market; agents don't appear to use significant commission leverage to steer transactions). The brief takes this seriously rather than burying it — the workaround claim is UNRESOLVED, not confirmed, and the CGAP finding is presented as a real complication, with the explicit caveat that it is 8-9-year-old fieldwork that predates Raast and the subsequent huge growth in wallet accounts, so it may no longer describe current conditions.
4. **"Maybe Raast isn't actually a threat yet — it's still tiny next to cash."** Addressed in Section 5.6: P2M/QR volumes are growing fast in percentage terms but remain small in absolute terms against total agent-mediated cash volume in the same quarter. The brief explicitly declines to overstate this into "already collapsing," per the research instructions, and frames it as a structurally well-supported anticipated risk instead.

---

## 10. Stakeholder map

- **Owners/operators**: Telenor Microfinance Bank (Easypaisa), Mobilink Microfinance Bank (JazzCash) — both rely on fee/commission income (documented: Telenor Bank's fee/commission income exceeded interest income in some years while the bank ran losses) and both have publicly supported SBP's digital-inclusion push while privately (per Profit's 2021 reporting) worrying about the revenue hit from fee waivers.
- **Regulator**: State Bank of Pakistan — sets the BB regulatory framework, requires quarterly published/fee-locked tariffs, waived/capped IBFT fees in 2021, operates Raast, and is simultaneously the author of both the agent-commission-protecting rules and the Raast rail that threatens that same commission model.
- **Capital providers / infrastructure**: 1LINK (interoperability), NADRA (biometric verification backbone), telecom parent companies (Telenor, VEON/Jazz) providing the underlying network and balance-sheet support for their microfinance-bank subsidiaries.
- **Agent shopkeepers**: the actual "owners" of the last-mile relationship — earn commission on cash-in/cash-out and (per CGAP) a larger, recurring commission on OTC transactions specifically, creating the incentive misalignment with operators documented in Section 5.3. Liquidity/float management is their primary operating cost and constraint.
- **Customers**: primarily first-time formal-financial-system users, disproportionately urban and male per the Karandaaz gender/rural gap findings; BISP beneficiaries are a large, policy-visible customer segment now directly experiencing the free-Raast-vs-paid-cash-withdrawal distinction.
- **Losers/externalities**: rural and female populations who remain thin in the network despite being financial-inclusion policy's explicit target; agents in low-liquidity/low-volume markets who may be structurally unable to reach break-even under the official commission model; and, if the Raast threat materializes, the agent network itself, whose core revenue moment (the cash-conversion step) is the thing an interoperable, free instant-payment rail is explicitly designed to make unnecessary.

---

## 11. Note on this session's access limitations

Every SBP.org.pk PDF and page attempted in this pass returned HTTP 403 to both the WebFetch tool and a direct curl through the session's proxy — this is a systematic access barrier, not a one-off failure, and it should be assumed to apply to future SBP.org.pk fetch attempts from this environment too. Firecrawl search (via `mcp__Firecrawl__firecrawl_search`) was used as instructed and did surface SBP data through third-party mirrors (Scribd) and search snippets, but in every case only as a snippet/summary, never as a full document read — meaning every SBP-sourced figure in this brief is REPORTED rather than VERIFIED, with the sole exception of the SBP Branchless Banking Regulations PDF (S01), which — unusually — *did* return full content to a direct WebFetch call and was read in full. If a human has direct browser/portal access to sbp.org.pk (which does not block ordinary browsers, only this fetch environment), re-deriving the headline scale and Raast figures directly from the primary PDFs before scripting would meaningfully upgrade this brief's evidentiary base.
