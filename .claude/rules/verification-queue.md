# Verification-queue rules — applies to research/verification-queues/ and research/footage-queues/

## Purpose

A source audit (`.claude/rules/source-audits.md`) records what was checked and what
was found. It does not, by itself, produce a practical to-do list a human can work
from on their phone. The verification queue and footage queue turn every "Needs
verification" / "Conflicting" audit row, and every un-cleared footage cue, into an
actionable ticket: what to check, where to go, what search terms to use, what
would count as confirmation, and what to write if verification fails.

Never resolve uncertainty by guessing. Never call a source verified because its
title or a search snippet looked relevant — verified means its actual contents
were inspected, either by Claude through a successful fetch or by a human.

## When to create or update

After any research pass, `/audit-sources` run, or `/footage` run that leaves
claims or footage cues unresolved, create or update:

- `research/verification-queues/NN_slug_verification-queue.md`
- `research/footage-queues/NN_slug_footage-queue.md`

Regenerate the verification queue from the current source audit rather than
maintaining the two independently — the audit is the source of truth for
claim-to-source traceability; the queue is a derived, actionable view of its
open rows.

## Claim ticket format (V-XXX)

```markdown
### V-001 — <short label>

- Script location: <Part / paragraph>
- Current wording: "<exact script text>"
- Why verification is needed: <conflict, staleness, untraceable citation, etc.>
- Go to: <named institutions / document types — primary sources preferred>
- Search terms:
  - <term 1>
  - <term 2>
- Prefer: <primary government/company/court record over press>
- Check for: <the specific ambiguity — date precision, accounting definition,
  whether a figure is cumulative vs. annual, etc.>
- Do not use: <a source class that would look sufficient but isn't — e.g. a
  source that only repeats the commonly cited figure without its own reporting>
- Safe fallback wording: "<what to write in the script if verification fails
  or time runs out>"
- Status: OPEN
```

## Footage ticket format (F-XXX)

```markdown
### F-001 — <short label>

- Narration line: "<the line this footage plays under>"
- Required visual: <what the shot needs to show and why>
- Search locations: <platforms — CC0 libraries first per footage-rights.md>
- Search terms:
  - <term 1>
- Check:
  - Does the visual match the required content (not just the title)?
  - Any identifiable branding, logos, signage, or real people in frame?
  - Licence terms for this specific platform/clip class?
- Needed from editor: exact URL, timecode, downloaded file, licence/permission
  record, attribution text (if any).
- Status: CANDIDATE
```

## Status vocabulary

For claims (`verification-queue.md`), layered on top of the
Confirmed/Needs verification/Conflicting/Removed classification already used
in the source audit:

- **OPEN** — needs research or verification.
- **ACCESS BLOCKED** — Claude could not reach the source (network, login,
  platform restriction). Say so explicitly; do not substitute a weaker source
  and call the item resolved.
- **CANDIDATE** — a possible source has been identified but not yet inspected
  for accuracy.
- **EDITOR VERIFIED** — a human (or Claude, where fetch succeeded) has opened
  the source and confirmed its contents against the claim.

For footage (`footage-queue.md`), layered on top of the cleared yes/no/pending
column in the source register (`footage-rights.md`):

- **OPEN** — no candidate identified yet.
- **ACCESS BLOCKED** — the clip platform could not be reached.
- **CANDIDATE** — a clip has been found; its stated licence terms may be
  confirmed, but its actual visual content has not been inspected frame-by-frame
  by a human or by Claude.
- **RIGHTS UNCONFIRMED** — the visual content is acceptable but licence/permission
  is not yet established.
- **EDITOR VERIFIED** — a human has opened the clip, watched it, and confirmed
  both content and rights.

Do not mark a footage item EDITOR VERIFIED, or "cleared" in the source register,
merely because a page's title or text description looked relevant, and do not
treat a platform's general/site-wide licence terms as sufficient on their own —
confirming the licence type is necessary but not sufficient; the specific clip's
visual content still needs a real watch-through before it is usable.

## Session handoff

End the verification queue file with a short handoff summary: counts of open
claims, conflicts, blocked sources, and footage still needing visual or rights
confirmation, followed by a priority-ordered list of the 3-5 items that matter
most before the script can move to `production-ready`.
