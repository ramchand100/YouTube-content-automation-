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

# Total target ~2,200 words across five sections (150 wpm ~= 14.5 min).
# Structure: The Investigative Brief (see CLAUDE.md section 7).
PARTS = [
    {"n": 1, "title": "The Unsolved Reality", "ts": "0:00 - 2:00", "words": 300,
     "goal": "An on-the-ground entry point. Open in the field, on a concrete real-world scene or "
             "anomaly that poses the question the brief will answer. State the stakes plainly, no "
             "manufactured drama."},
    {"n": 2, "title": "The Paper Trail", "ts": "2:00 - 6:00", "words": 560,
     "goal": "The raw math. PKR unit economics and financial anatomy. Break down the actual "
             "numbers, costs, margins, and cash flows in rupees, so the viewer sees exactly how "
             "the money works."},
    {"n": 3, "title": "The Field Reality", "ts": "6:00 - 10:00", "words": 560,
     "goal": "Ground-level mechanics. How the system actually runs day to day, the informal "
             "networks, the cash layer, and distributor and middleman dynamics the paper trail "
             "alone does not reveal."},
    {"n": 4, "title": "The Systemic Domino Effect", "ts": "10:00 - 13:00", "words": 450,
     "goal": "The macroeconomic impact on Pakistan. How this one system ripples into the wider "
             "economy, investors, and ordinary consumers. Tie to SBP / FBR / FX / energy reality."},
    {"n": 5, "title": "The Verdict & Future Outlook", "ts": "13:00 - End", "words": 360,
     "goal": "A realistic market forecast. A grounded, honest read on where this goes next and the "
             "concrete implications for founders, executives, investors, and students."},
]

SKELETON = Template(
    """# {{ title }}

<!--
PRODUCTION SCRIPT — conform to CLAUDE.md.
Language: 100% English. Length target: 1,800-2,500 words (~12-16 min).
Annotate visuals inline as [VISUAL mm:ss - description].
Cite inline as [SOURCE: publication/institution, year]. Tag unconfirmed/fast-moving
numbers [VERIFY]. Collect all citations in the Sources block at the end.
-->

- **Episode:** {{ number }}
- **Pillar:** {{ pillar }}
- **Drafted:** {{ created }}
- **Word target:** ~2,200 (five parts below carry per-section budgets)
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
    args = parser.parse_args(argv)

    rendered = SKELETON.render(
        title=args.title,
        number=args.number,
        pillar=args.pillar,
        created=_dt.date.today().isoformat(),
        parts=PARTS,
    )
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.number}_{slugify(args.title)}.md"
    out_path.write_text(rendered, encoding="utf-8")
    print(f"Script skeleton written: {out_path}")
    print("Now write each PART to its word budget, sourcing every figure. See CLAUDE.md.")


if __name__ == "__main__":
    main()
