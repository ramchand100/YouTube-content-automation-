#!/usr/bin/env python3
"""
script_engine.py — Full-length script scaffolder.

Generates a production-ready, full-length script skeleton that enforces the
channel's 5-Part Narrative Structure, word budgets, timestamped visual cues,
source-citation slots, and the editorial rules in CLAUDE.md. The writer then
fills each section with sourced, 100%-English prose.

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

# Total target ~2,200 words across five parts (150 wpm ~= 14.5 min).
PARTS = [
    {"n": 1, "title": "The Hook", "ts": "0:00 - 2:00", "words": 300,
     "goal": "Open on a central paradox, a shocking sourced metric, or a hidden local anomaly. "
             "State the promise of the video and the stakes. Earn the next 12 minutes."},
    {"n": 2, "title": "The Ground-Truth Mechanics", "ts": "2:00 - 6:00", "words": 620,
     "goal": "Explain step by step how this business or economic system actually operates on the "
             "ground in Pakistan. Concrete, local, mechanical. This is where authenticity is won."},
    {"n": 3, "title": "The Core Conflict / Bottleneck", "ts": "6:00 - 10:00", "words": 620,
     "goal": "The structural friction: regulation, cash-flow trap, capital misallocation, or "
             "competitive dynamics. Who benefits from it staying broken, and who pays."},
    {"n": 4, "title": "The Broader Macro Impact", "ts": "10:00 - 13:00", "words": 450,
     "goal": "Zoom out. How this ripples into the wider Pakistani economy, investors, and ordinary "
             "consumers. Tie back to SBP / FBR / FX / energy reality."},
    {"n": 5, "title": "Strategic Takeaways & Future Outlook", "ts": "13:00 - End", "words": 360,
     "goal": "Honest, concrete lessons for founders, executives, and students. A grounded forward "
             "view. No motivational filler, no fake certainty."},
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
## PART {{ part.n }} — {{ part.title }}  ({{ part.ts }})
*Target: ~{{ part.words }} words. {{ part.goal }}*

[VISUAL {{ '%02d'|format(part.n * 2) }}:00 — open this section with a strong establishing visual]

> WRITE HERE: full voiceover prose for Part {{ part.n }}. Every claim sourced or clearly
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
