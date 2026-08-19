#!/usr/bin/env python3
"""
script_engine.py — Full-length script scaffolder.

Generates a production-ready, full-length script skeleton that enforces the
channel's Investigative Brief structure (see CLAUDE.md section 7), word budgets,
timestamped visual cues, source-citation slots, and the editorial rules in
CLAUDE.md. The writer then fills each section with sourced, 100%-English prose.

Usage:
    python3 scripts/script_engine.py --title "..." [--pillar macro] [--number 02] [--out scripts]

Output: scripts/<NN>_<slug>.md  (a complete skeleton, ready to write into)

Dependencies: see tools/requirements.txt (Jinja2).
"""

import argparse
import datetime as _dt
import re
from pathlib import Path

from jinja2 import Template

# Structure: The Investigative Brief (see CLAUDE.md section 7).
# Each section carries a WEIGHT (share of the runtime). The actual word budget and
# timestamps are computed from the target length (--minutes), so a topic that needs
# more room simply scales every section up. Default 15 min ~= 2,250 words.
# Length is set by the topic, not a quota (see CLAUDE.md section 5): most episodes run
# 12-16 min; go longer only when the extra length carries real substance.
WORDS_PER_MINUTE = 150

PARTS = [
    {"n": 1, "title": "The Unsolved Reality", "weight": 0.135,
     "goal": "An on-the-ground entry point. Open in the field, on a concrete real-world scene or "
             "anomaly that poses the question the brief will answer. State the stakes plainly, no "
             "manufactured drama."},
    {"n": 2, "title": "The Paper Trail", "weight": 0.251,
     "goal": "The raw math. PKR unit economics and financial anatomy. Break down the actual "
             "numbers, costs, margins, and cash flows in rupees, so the viewer sees exactly how "
             "the money works."},
    {"n": 3, "title": "The Field Reality", "weight": 0.251,
     "goal": "Ground-level mechanics. How the system actually runs day to day, the informal "
             "networks, the cash layer, and distributor and middleman dynamics the paper trail "
             "alone does not reveal."},
    {"n": 4, "title": "The Systemic Domino Effect", "weight": 0.202,
     "goal": "The macroeconomic impact on Pakistan. How this one system ripples into the wider "
             "economy, investors, and ordinary consumers. Tie to SBP / FBR / FX / energy reality."},
    {"n": 5, "title": "The Verdict & Future Outlook", "weight": 0.161,
     "goal": "A realistic market forecast. A grounded, honest read on where this goes next and the "
             "concrete implications for founders, executives, investors, and students."},
]


def _fmt_ts(minutes: float) -> str:
    total_seconds = int(round(minutes * 60))
    return f"{total_seconds // 60}:{total_seconds % 60:02d}"


def build_sections(target_minutes: float):
    """Scale each section's timestamp span and word budget to the target length."""
    total_weight = sum(p["weight"] for p in PARTS)
    total_words = round(target_minutes * WORDS_PER_MINUTE)
    sections = []
    cursor = 0.0
    for i, p in enumerate(PARTS):
        span = target_minutes * p["weight"] / total_weight
        start, end = cursor, cursor + span
        cursor = end
        ts = f"{_fmt_ts(start)} - " + ("End" if i == len(PARTS) - 1 else _fmt_ts(end))
        words = round(total_words * p["weight"] / total_weight)
        sections.append({**p, "ts": ts, "words": words})
    return sections, total_words

SKELETON = Template(
    """# {{ title }}

<!--
PRODUCTION SCRIPT — conform to CLAUDE.md.
Language: 100% English, plain but smart (grade 7-8; define all jargon on first
use, keep full analytical depth). See CLAUDE.md section 2.
Length target: ~{{ total_words }} words (~{{ target_minutes }} min). Length is set
by the topic, not a quota; go longer only when the extra length carries real
substance (see CLAUDE.md section 5).
Annotate visuals inline as [VISUAL mm:ss - description].
Cite inline as [SOURCE: publication/institution, year]. Tag unconfirmed/fast-moving
numbers [VERIFY]. Collect all citations in the Sources block at the end.
-->

- **Episode:** {{ number }}
- **Pillar:** {{ pillar }}
- **Drafted:** {{ created }}
- **Word target:** ~{{ total_words }} (~{{ target_minutes }} min; five sections below carry per-section budgets)
- **Companion files:** storyboards/{{ number }}_*.md, prompts/{{ number }}_*.md

---
{% for part in parts %}
## SECTION {{ part.n }} — {{ part.title }}  ({{ part.ts }})
*Target: ~{{ part.words }} words. {{ part.goal }}*

[VISUAL {{ '%02d'|format(part.n * 2) }}:00 — open this section with a strong establishing visual]

> WRITE HERE: full voiceover prose for Section {{ part.n }}. Every claim sourced or clearly
> labelled as analysis. Connect explicitly to Pakistani economic reality.

{% endfor %}---

## SOURCES
List every citation used above, numbered, with publication and year.

1.
2.
3.

## PRODUCTION NOTES
- Voiceover pace: ~150 wpm, documentary register.
- Music: match the mood of the topic; keep under the voice.
- Re-verify all [VERIFY] figures before the final read.
"""
)


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return re.sub(r"_+", "_", text).strip("_")


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--title", required=True, help="Episode title.")
    parser.add_argument("--pillar", default="(set pillar)", help="Content pillar.")
    parser.add_argument("--number", default="NN", help="Episode number, e.g. 02.")
    parser.add_argument("--out", default="scripts", help="Output directory (default: scripts).")
    parser.add_argument("--minutes", type=float, default=15.0,
                        help="Target runtime in minutes (default 15). Use a larger value only "
                             "for a topic that genuinely needs the depth, up to ~26. Scales every "
                             "section's word budget and timestamps (see CLAUDE.md section 5).")
    args = parser.parse_args(argv)

    if not 8.0 <= args.minutes <= 30.0:
        parser.error("--minutes should be between 8 and 30. Most episodes are 12-16; "
                     "go long only when the topic earns it.")

    sections, total_words = build_sections(args.minutes)
    rendered = SKELETON.render(
        title=args.title,
        number=args.number,
        pillar=args.pillar,
        created=_dt.date.today().isoformat(),
        parts=sections,
        total_words=total_words,
        target_minutes=round(args.minutes),
    )
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.number}_{slugify(args.title)}.md"
    out_path.write_text(rendered, encoding="utf-8")
    print(f"Script skeleton written: {out_path}")
    print("Now write each PART to its word budget, sourcing every figure. See CLAUDE.md.")


if __name__ == "__main__":
    main()
