#!/usr/bin/env python3
"""
script_engine.py — Full-length script scaffolder.

Generates a production-ready, full-length script skeleton that enforces the
channel's Investigative Brief structure (see CLAUDE.md section 7), word budgets,
source-citation slots, and the editorial rules in CLAUDE.md.
The writer then fills each section with sourced, 100%-English prose.

Usage:
    python3 scripts/script_engine.py --title "..." [--template A] [--pillar macro]
                                      [--number 02] [--minutes 15] [--out scripts]

Templates:
    A   Macro / Institutions  (Paper Trail → Field Reality → Systemic Domino Effect)
    B   Company Case Study    (Business Model → Operational Reality → Competitive Position)
    C   Structural / History  (The Origin → How It Plays Out → The Structural Risk)

Output: scripts/<NN>_<slug>.md  (a complete skeleton, ready to write into)

Dependencies: see requirements.txt (Jinja2).
"""

import argparse
import datetime as _dt
import re
from pathlib import Path

from jinja2 import Template

# Structure: five sections, fixed count.
# Each template varies sections 2, 3, and 4.
# Section 1 (The Anomaly) and Section 5 (The Verdict) are universal.
# Weights represent share of runtime; they are identical across templates.

WORDS_PER_MINUTE = 150

SECTION_GOALS = {
    1: ("The Anomaly",
        "An on-the-ground entry point. Open on a documented, concrete real-world "
        "event or institutional anomaly that poses the question the episode answers. "
        "Short, punchy sentences. Echo a key word. Include a transitional sentence: "
        "'That [X] was not an accident.' End with the single central question."),
    5: ("The Verdict",
        "A grounded, honest outlook. Name specifically what would need to change and "
        "what the concrete obstacles are. State clearly who this matters to: founders, "
        "investors, professionals, or students. No manufactured optimism."),
}

TEMPLATE_DEFS = {
    "A": {
        "name": "Macro / Institutions",
        "sections": {
            2: ("The Paper Trail",
                "The raw math. PKR unit economics and financial anatomy. Break down the "
                "actual numbers — costs, margins, and cash flows in rupees — so the viewer "
                "sees exactly how the money works. Government budgets, subsidy flows, "
                "cost-margin anatomy."),
            3: ("The Field Reality",
                "Ground-level mechanics. How the system actually runs day to day: the "
                "informal networks, the cash layer, and middleman dynamics the paper trail "
                "alone does not reveal."),
            4: ("The Systemic Domino Effect",
                "The macroeconomic impact. How this one system ripples into the wider "
                "economy, investors, and ordinary consumers. Tie explicitly to SBP / FBR "
                "/ FX / energy reality. SBP, FBR, and FX connections."),
        },
        "weights": {1: 0.135, 2: 0.251, 3: 0.251, 4: 0.202, 5: 0.161},
    },
    "B": {
        "name": "Company Case Study",
        "sections": {
            2: ("The Business Model",
                "Revenue model, unit economics, margin structure. How this company "
                "actually makes or loses money. State the mechanics in rupees."),
            3: ("The Operational Reality",
                "Supply chain, workforce, compliance, and the informal layer. What "
                "actually makes the operation run day to day."),
            4: ("The Competitive Position",
                "Market position vs. regional and global peers. FX, energy, and "
                "regulatory exposure. What threatens the model and how durable the "
                "competitive advantage actually is."),
        },
        "weights": {1: 0.135, 2: 0.251, 3: 0.251, 4: 0.202, 5: 0.161},
    },
    "C": {
        "name": "Structural Dependency / History",
        "sections": {
            2: ("The Origin",
                "How and when the structure was built. The decision, policy, or event "
                "that created it and why it seemed rational at the time."),
            3: ("How It Plays Out",
                "Ground-level consequences: the households, towns, industries, and "
                "institutions that the origin story produced."),
            4: ("The Structural Risk",
                "What threatens the model, what has already begun to change, and what "
                "the numbers say about whether the structure is sustainable."),
        },
        "weights": {1: 0.135, 2: 0.251, 3: 0.251, 4: 0.202, 5: 0.161},
    },
}


def _fmt_ts(minutes: float) -> str:
    total_seconds = int(round(minutes * 60))
    return f"{total_seconds // 60}:{total_seconds % 60:02d}"


def build_sections(template_key: str, target_minutes: float) -> tuple[list[dict], int]:
    tdef = TEMPLATE_DEFS[template_key]
    weights = tdef["weights"]
    total_words = round(target_minutes * WORDS_PER_MINUTE)
    sections = []
    cursor = 0.0
    for n in range(1, 6):
        w = weights[n]
        span = target_minutes * w
        start, end = cursor, cursor + span
        cursor = end
        ts = f"{_fmt_ts(start)} - " + ("End" if n == 5 else _fmt_ts(end))
        words = round(total_words * w)
        if n in (1, 5):
            title, goal = SECTION_GOALS[n]
        else:
            title, goal = tdef["sections"][n]
        sections.append({"n": n, "title": title, "goal": goal, "ts": ts, "words": words})
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

SCRIPTS ARE PURE VOICEOVER PROSE. No visual cues inside this file.
All visual direction lives in the companion storyboard file.

Cite inline as [SOURCE: publication/institution, year]. Tag unconfirmed/fast-moving
numbers [VERIFY]. Collect all citations in the Sources block at the end.
Label analysis explicitly — never present it as fact.
-->

- **Episode:** {{ number }}
- **Pillar:** {{ pillar }}
- **Approved angle:** [fill from topics/angles/NN_slug_angle.md before writing]
- **Central question:** [fill from approved angle]
- **Thesis:** [fill from approved angle]
- **Template:** {{ template }}
- **Status:** draft
- **Drafted:** {{ created }}
- **Word target:** ~{{ total_words }} (~{{ target_minutes }} min)
- **Last verified:** {{ created }}
- **Companion files:** storyboards/{{ number }}_*_visuals.md

---
{% for part in parts %}
## SECTION {{ part.n }} — {{ part.title }}  ({{ part.ts }})
*Target: ~{{ part.words }} words. {{ part.goal }}*

> WRITE HERE: full voiceover prose for Section {{ part.n }}. Every statistical claim
> must have an adjacent [SOURCE: publication, year] tag. Label all analysis.
> Connect explicitly to Pakistani economic reality.

{% endfor %}---

## SOURCES
List every citation used above, numbered, with publication and year.

1.
2.
3.

## PRODUCTION NOTES
- Voiceover pace: ~150 wpm, documentary register.
- Re-verify all [VERIFY] figures before the final read.
- Run: python3 tools/validate_script.py {{ out }}/{{ number }}_{{ slug }}.md
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
    parser.add_argument("--template", default="A", choices=["A", "B", "C"],
                        help="Content template: A (Macro/Institutions), B (Company), "
                             "C (Structural/History). Default: A.")
    parser.add_argument("--pillar", default="(set pillar)", help="Content pillar label.")
    parser.add_argument("--number", default="NN", help="Episode number, e.g. 02.")
    parser.add_argument("--out", default="scripts", help="Output directory (default: scripts).")
    parser.add_argument("--minutes", type=float, default=15.0,
                        help="Target runtime in minutes (default 15). Most episodes run 12-16; "
                             "use up to ~26 only when the topic genuinely needs the depth "
                             "(see CLAUDE.md section 5).")
    args = parser.parse_args(argv)

    if not 8.0 <= args.minutes <= 30.0:
        parser.error("--minutes should be between 8 and 30. Most episodes are 12-16; "
                     "go long only when the topic earns it.")

    slug = slugify(args.title)
    sections, total_words = build_sections(args.template, args.minutes)
    rendered = SKELETON.render(
        title=args.title,
        number=args.number,
        pillar=args.pillar,
        template=args.template,
        created=_dt.date.today().isoformat(),
        parts=sections,
        total_words=total_words,
        target_minutes=round(args.minutes),
        out=args.out,
        slug=slug,
    )
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.number}_{slug}.md"
    out_path.write_text(rendered, encoding="utf-8")
    tdef_name = TEMPLATE_DEFS[args.template]["name"]
    print(f"Script skeleton written: {out_path}")
    print(f"Template: {args.template} ({tdef_name})")
    print("Fill each section to its word budget, sourcing every figure. See CLAUDE.md.")
    print(f"Validate when done: python3 tools/validate_script.py {out_path}")


if __name__ == "__main__":
    main()
