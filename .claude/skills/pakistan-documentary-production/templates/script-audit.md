# Script-audit template — superseded

This file predates the channel's move to a flexible Part-N script structure
(it still checks for "exactly 5 section headers") and was left un-migrated
while `/review-script`'s real output format moved on. Rather than maintain
two parallel copies that can drift out of sync again, this file now points
to the current one instead of duplicating it:

- **Script review checklist and output format:** `.claude/commands/review-script.md`
  — the checks and the `## Script review: ...` output format every real
  review actually uses.
- **Mechanical pre-check:** `.claude/skills/pakistan-documentary-production/scripts/validate_script.py`.

Use `/review-script` for a script audit. Do not resurrect a fixed
five-section PASS/FAIL checklist here.
