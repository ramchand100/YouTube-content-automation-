# Delivery-notes rules — applies to delivery-notes/

## Purpose

A script (`scripts/NN_slug.md`) is clean narration text — no markup, no
performance direction, because it has to survive `/audit-sources` and
`/review-script` as plain prose. But a narrator recording that script needs
to know which words carry weight, where to pause, and where the pace should
shift. That's a different document with a different audience (the person
recording, not an auditor), so it lives in its own file and its own folder.

**Never modify the words of the narration in a delivery-notes file.** If a
sentence needs to change, that change happens in the script file first. A
delivery-notes file adds performance markup on top of already-approved
narration; it does not rewrite it.

## When to create

After a script reaches a stable draft the user is happy with (not before —
marking up prose that's still being rewritten is wasted work), create:

`delivery-notes/NN_slug_delivery-notes.md`

Regenerate it (or patch the relevant section) whenever the underlying script
changes. A delivery-notes file that doesn't match the current script wording
is worse than no delivery-notes file — flag and fix any drift immediately.

## File structure

- Header: companion script path, a pointer to this rule file, and a base
  pace (words per minute) for the episode.
- One section per script Part, in the same order, using the same Part
  names as the script.
- The full narration text of that Part, reproduced with markup — not a
  summary, not excerpts. The narrator should be able to read from this file
  alone without flipping back to the script.

## Markup convention

- `**bold**` — land weight on this word or phrase. Don't rush past it. Use
  sparingly: 2-4 per paragraph at most. Marking every other word defeats the
  purpose.
- `/` — a short breath-pause, shorter than what a full stop would naturally
  produce. Use at the seam of a comparison, right before or after a number
  that should sit with the viewer, or before a genuine (non-rhetorical)
  question.
- *Italic parenthetical notes* — pace or tone direction for the passage that
  follows, not word-by-word instruction. Examples: `(slower)`,
  `(flat, neutral delivery)`, `(pick pace back up)`, `(pause about a full
  second)`. Place these where the energy of the read should actually shift,
  not on every paragraph.
- A blank line where the script already has a paragraph break stays a
  natural breath; it does not need its own note unless something unusual
  should happen there.

## What earns emphasis or a pause

Mark weight on:
- The two sides of a stated contrast or comparison (the small number and
  the big number in the same sentence).
- A number the episode wants the viewer to actually remember.
- The word that turns an assumption (e.g. "on paper", "in theory") right
  before the script complicates it later.
- The close of a Part — the line that should be the last thing a viewer
  processes before the cut.

Do not mark emphasis on ordinary connective sentences, transitions that
exist purely for narration flow, or any word already carrying stress from
normal English sentence stress. Over-marking reads as noisy and undercuts
the words that actually need it.

## What this file is not

- Not a place for `[VISUAL...]`, `[FOOTAGE...]`, camera direction, or
  on-screen text — that's the storyboard's job
  (`.claude/rules/storyboards.md`).
- Not a second copy of the Sources block or any citation content — citations
  live only in the script.
- Not a rewrite tool. If reading the marked-up version out loud reveals a
  sentence that's awkward to say, fix the sentence in the script, then
  re-mark the corrected version here.
