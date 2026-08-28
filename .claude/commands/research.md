# /research

Create the research brief, claim ledger, and source register for an approved angle.
Do not write the script.

## Before running

1. Read `CLAUDE.md`.
2. Read `.claude/rules/research.md`.
3. Confirm an approved angle exists in `topics/angles/NN_slug_angle.md` with
   `approval_status: approved`.
4. If no approved angle exists, redirect to `/angles` first.

## What to do

Work only from the approved angle. Do not reopen the angle decision.

**Create these files** (use the episode number NN and slug from the approved angle):

### 1. Research brief — `research/briefs/NN_slug_brief.md`

Structure:
- Approved angle (copy from `topics/angles/NN_slug_angle.md`)
- Central question
- Tentative thesis
- Claims required (from the angle's sub-questions)
- Raw findings (source URL + date accessed + verbatim quote or figure)
- Verified figures (clean number + citation string ready for script)
- `[VERIFY]` flagged items
- Discarded sources (note why discarded)
- Counterarguments and how they are addressed
- Stakeholder map (owners, regulators, capital providers, customers, losers)

### 2. Claim ledger — `research/claim-ledgers/NN_slug_claims.csv`

Headers: `claim_id,claim_text,classification,source,url,verified`

Populate one row per major factual claim. Apply claim classification:
VERIFIED / REPORTED / ANALYSIS / ESTIMATE / UNRESOLVED

### 3. Source register — `research/source-registers/NN_slug_sources.csv`

Headers: `source_id,title,institution,date,url,tier,notes`

One row per source consulted (not just cited). Record tier:
Primary / Tier-1 journalism / Secondary

## Research rules

- Search for live figures before writing. Do not rely on training-data memory for
  statistics that change (inflation, interest rates, FX, company financials).
- Open and read the actual source document — not a search-result snippet.
- Use the source hierarchy from `.claude/rules/research.md`.
- Tag any figure that could not be confirmed `[VERIFY]`.
- Do not include UNRESOLVED claims without a `[VERIFY]` tag and a note.

## Firecrawl — use for every research pass

If an `mcp__Firecrawl__firecrawl_search` tool is available this session, use it
as the default first attempt for any source that returns a fetch error (HTTP
403 or similar) to a direct WebFetch — this has repeatedly gotten past blocks
on sites like shaukatkhanum.org.pk, the UK Charity Commission register,
Business Recorder, and Profit by Pakistan Today that direct fetch could not
reach, because Firecrawl crawls with its own infrastructure rather than
routing through this session's network path. Try it before giving up on a
blocked primary or official source and falling back to WebSearch-synthesis-only
sourcing.

If the Firecrawl tool is not available in a given session (its MCP connector
can disconnect between sessions), say so plainly and fall back to the normal
WebFetch/WebSearch approach — do not silently skip this step or claim a source
was checked via Firecrawl when it wasn't.

**Firecrawl results still count as a "search-result snippet" unless the tool
returns full page content** — some results come back as a short
title/description snippet, others as the full page markdown (this varies by
page, not predictably). Check which you got:
- Full page content returned → this satisfies "open and read the actual
  source document." Classify normally and cite it as a direct read.
- Short snippet only → this is still not final evidence per the rule above.
  Use it to identify the correct figure and cite it as `REPORTED` with a note
  that it was Firecrawl-search-confirmed but not a full document read, and add
  a verification-queue ticket (status `CANDIDATE`) for a human — or a follow-up
  full read — to close it out. Do not mark a snippet-sourced claim `VERIFIED`
  or a verification-queue ticket `EDITOR VERIFIED`.

If Firecrawl's own crawl surfaces information that contradicts something
already believed true (a claimed completion date, a cost figure, a status),
treat that as a real finding to investigate, not noise — it may be catching a
stale assumption the way it did for episode 15's Karachi campus opening date.

## Nonfiction constraint

Do not invent scenes, examples, or illustrative characters to make the research
feel more concrete. Record only what is documented.

## Verification queue — required for every episode

Once the claim ledger and source register are complete, generate:

`research/verification-queues/NN_slug_verification-queue.md`

using the ticket format and status vocabulary in
`.claude/rules/verification-queue.md`. This is not optional and does not wait for a
`/review-script` or `/audit-sources` pass — generate it as part of `/research`
itself, from the claim ledger and source register directly, so the human handoff
list exists from the first draft rather than being reconstructed later.

Do not open a V-XXX ticket for every REPORTED or ESTIMATE claim mechanically.
Prioritize, the same way a source audit does: claims that are load-bearing (opening
hooks, headline figures, the thesis's central number), claims with directly
conflicting sources, claims sourced only through a site that returned a fetch
error (ACCESS BLOCKED) rather than a directly read document, and claims marked
UNRESOLVED. A claim that is REPORTED, attributed, and consistent across two or more
independently corroborating sources does not need its own ticket just because it
wasn't independently fetched.

End the file with the same Human Verification Handoff structure used in
`research/verification-queues/11_pakistan_steel_mills_verification-queue.md`:
research and footage status counts, and a priority-ordered list of the 3-5 items
that matter most before the script can move to `production-ready`. If no storyboard
exists yet for this episode, state that explicitly and skip the footage-queue file
until `/footage` runs.

## After this command

Report:
- Research brief path
- Claim ledger path
- Source register path
- Verification queue path
- Count of VERIFIED claims
- Count of REPORTED claims
- Count of ESTIMATE claims
- Count of UNRESOLVED / `[VERIFY]` items that need resolution before scripting
- Count of open verification-queue tickets and the top priority items among them

Do not begin the script. Wait for the user to review the research brief and
confirm readiness to proceed.
