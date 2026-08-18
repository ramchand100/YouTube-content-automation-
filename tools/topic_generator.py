#!/usr/bin/env python3
"""
topic_generator.py — Deep research-brief generator for the channel.

Structures video ideas and full research briefs across the four core pillars of
Pakistan's business economy. Every brief is pre-wired to the channel's 5-Part
Narrative Structure and to the real local data sources an analyst must pull from
(SBP, PBS, FBR, SECP, PSX, and credible local business reporting).

Usage:
    python3 tools/topic_generator.py list
    python3 tools/topic_generator.py ideas --pillar startup [--count 5]
    python3 tools/topic_generator.py brief --title "..." --pillar macro [--out topics]

Pillars (slug -> name):
    startup   The Startup & Tech Landscape
    seth      Seth Culture vs. Modern Management
    macro     Macroeconomics & Financial Plumbing
    brands    Consumer Brands & Export Empires

Dependencies: see requirements.txt (rich, Jinja2).
"""

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

try:
    from jinja2 import Template
except ImportError:  # pragma: no cover
    print("Missing dependency 'Jinja2'. Run: pip install -r tools/requirements.txt",
          file=sys.stderr)
    raise

try:
    from rich.console import Console
    from rich.table import Table
    _console = Console()
except ImportError:  # rich is optional at runtime; fall back to plain print
    _console = None


# --------------------------------------------------------------------------- #
# Pillar definitions
# --------------------------------------------------------------------------- #

PILLARS = {
    "startup": {
        "name": "The Startup & Tech Landscape",
        "focus": (
            "Unit economics, hypergrowth traps, burn-vs-margin reality, and "
            "Pakistani consumer behavior under low ARPU and thin cards penetration."
        ),
        "subjects": ["Airlift", "Foodpanda Pakistan", "Careem", "Bykea", "Daraz",
                     "Bazaar", "Easypaisa", "JazzCash", "SadaPay", "NayaPay"],
        "angles": [
            "How does the unit economics actually close in a low-ARPU, cash-heavy market?",
            "What killed the 2021-22 hypergrowth cohort when global capital dried up?",
            "Why does cash-on-delivery quietly break e-commerce margins here?",
            "Can a fintech make money before Raast commoditizes payments?",
            "What does 'product-market fit' mean when 80% of retail is undocumented?",
        ],
    },
    "seth": {
        "name": "Seth Culture vs. Modern Management",
        "focus": (
            "Traditional family-owned conglomerates (the 'Seth' owner-operator "
            "model) versus professional, venture-backed, process-driven management."
        ),
        "subjects": ["Nishat Group", "Packages", "Lucky Cement", "Engro",
                     "House of Habib", "Interloop", "Systems Limited"],
        "angles": [
            "Why does the Seth (owner-operator) model survive where MBAs predicted it would die?",
            "Cash-book vs. audited-book: how family firms actually track money.",
            "Succession risk: what happens to a conglomerate when the founder exits?",
            "Why professional CEOs churn fast inside family-controlled groups.",
            "When does a family firm actually need to professionalize, and when is it a trap?",
        ],
    },
    "macro": {
        "name": "Macroeconomics & Financial Plumbing",
        "focus": (
            "Payment rails (Raast, 1LINK, PayPak), real-estate capital traps, the "
            "tax structure, and import-export dynamics under FX and SBP constraints."
        ),
        "subjects": ["Raast", "1LINK", "PayPak", "SBP policy rate", "FBR withholding regime",
                     "Real-estate dead capital", "Import LC restrictions", "Circular debt"],
        "angles": [
            "How does the SBP policy rate actually transmit (or fail to) into the real economy?",
            "Why is so much national savings locked in unproductive real estate?",
            "Raast vs. the card networks: who loses when payments go free and instant?",
            "How import LC rationing silently picks industrial winners and losers.",
            "The documented-vs-undocumented economy: where the real money hides.",
        ],
    },
    "brands": {
        "name": "Consumer Brands & Export Empires",
        "focus": (
            "How Pakistani consumer and export brands built distribution moats and "
            "cracked global markets despite a weak home logistics base."
        ),
        "subjects": ["Shan Foods", "National Foods", "Khaadi", "Sapphire", "Tapal",
                     "Gul Ahmed", "Service Shoes", "K&N's"],
        "angles": [
            "How a spice/textile brand built a distribution moat competitors can't copy.",
            "The diaspora playbook: exporting to Pakistani communities abroad first.",
            "Why brand, not price, is the only defensible export edge for Pakistan.",
            "Retail expansion economics when real estate and financing are expensive.",
            "Private label vs. own brand: who really captures the export margin.",
        ],
    },
}

PILLAR_ALIASES = {
    "1": "startup", "2": "seth", "3": "macro", "4": "brands",
    "tech": "startup", "family": "seth", "economy": "macro", "consumer": "brands",
}


# --------------------------------------------------------------------------- #
# Research-brief template (Jinja2)
# --------------------------------------------------------------------------- #

BRIEF_TEMPLATE = Template(
    """# Research Brief: {{ title }}

- **Pillar:** {{ pillar_name }}
- **Status:** DRAFT / research in progress
- **Created:** {{ created }}
- **Target length:** 1,800-2,500 words (12-16 min voiceover)

> Fill every section with sourced facts before this brief is promoted to a script.
> Tag unconfirmed or fast-moving numbers with [VERIFY]. Language of the final
> script is 100% English (see CLAUDE.md).

---

## 1. Central Paradox / Hook Hypothesis  (maps to Narrative Part 1)
State the single counter-intuitive tension this episode resolves. One or two
shocking, sourced metrics that make a viewer stop scrolling.

- Paradox:
- Hook metric #1 [SOURCE: , year]:
- Hook metric #2 [SOURCE: , year]:

## 2. Ground-Truth Mechanics  (maps to Narrative Part 2)
Exactly how the system works on the ground in Pakistan. Answer plainly:

{% for q in mechanics_questions %}- {{ q }}
{% endfor %}
## 3. Core Conflict / Bottleneck  (maps to Narrative Part 3)
The structural friction. Regulation, cash-flow trap, capital misallocation, or
competitive dynamics.

- The bottleneck in one sentence:
- Who benefits from it staying broken:
- Who pays for it:

## 4. Broader Macro Impact  (maps to Narrative Part 4)
Ripple effects to the wider economy, investors, and ordinary consumers.

- Impact on GDP / investment / jobs:
- Impact on the ordinary consumer:
- Link to SBP / FBR / FX / energy reality:

## 5. Strategic Takeaways & Outlook  (maps to Narrative Part 5)
Honest, concrete lessons. No motivational filler.

- Lesson for founders:
- Lesson for executives:
- Lesson for students / investors:
- Grounded forward view:

---

## DATA TO GATHER (Pakistani sources first)
Pull real numbers from primary local sources before writing a single line.

- [ ] State Bank of Pakistan (SBP): policy rate, monetary stance, sector data
- [ ] Pakistan Bureau of Statistics (PBS): inflation, trade, national accounts
- [ ] Federal Board of Revenue (FBR): tax structure, withholding, property values
- [ ] SECP: company filings, incorporation and sector data
- [ ] Pakistan Stock Exchange (PSX): listed-company financials and disclosures
- [ ] Sector-specific: {{ sector_sources }}
- [ ] Credible reporting: Profit by Pakistan Today, Dawn Business, Business Recorder
- [ ] International cross-check: World Bank, IMF, relevant industry bodies

## STAKEHOLDER MAP
- Owners / operators:
- Regulators:
- Capital providers:
- Customers:
- Losers / externalities:

## RISK & SENSITIVITY FLAGS
- Political / defamation exposure:
- Contested claims needing both sides:
- Figures that must be re-verified before recording [VERIFY]:

## SOURCES (running list)
1.
2.
3.
"""
)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return re.sub(r"_+", "_", text).strip("_")


def resolve_pillar(key: str) -> str:
    key = key.lower().strip()
    key = PILLAR_ALIASES.get(key, key)
    if key not in PILLARS:
        valid = ", ".join(PILLARS.keys())
        raise SystemExit(f"Unknown pillar '{key}'. Valid: {valid}")
    return key


def sector_sources_for(pillar_key: str) -> str:
    return {
        "startup": "startup coverage (Data Darbar, Deep Dive by Profit), app-store ranks, Raast/SBP fintech data",
        "seth": "SECP filings, PSX annual reports, family-group disclosures",
        "macro": "SBP payment-systems reviews, FBR valuation tables, real-estate portals (Zameen), IMF program docs",
        "brands": "export data (TDAP, PBS trade), retail footprints, company export disclosures",
    }[pillar_key]


# --------------------------------------------------------------------------- #
# Commands
# --------------------------------------------------------------------------- #

def cmd_list(_args) -> None:
    if _console:
        table = Table(title="Content Pillars", show_lines=True)
        table.add_column("Slug", style="bold cyan")
        table.add_column("Pillar")
        table.add_column("Focus")
        for slug, p in PILLARS.items():
            table.add_row(slug, p["name"], p["focus"])
        _console.print(table)
    else:
        for slug, p in PILLARS.items():
            print(f"\n[{slug}] {p['name']}\n  {p['focus']}")


def cmd_ideas(args) -> None:
    key = resolve_pillar(args.pillar)
    p = PILLARS[key]
    count = max(1, min(args.count, len(p["angles"])))
    print(f"\n{p['name']}  ({key})\n{'=' * len(p['name'])}")
    print(f"Focus: {p['focus']}\n")
    print("Subjects in play: " + ", ".join(p["subjects"]) + "\n")
    print("Research angles (each is a potential episode):")
    for i, angle in enumerate(p["angles"][:count], 1):
        print(f"  {i}. {angle}")
    print("\nPromote one to a full brief:")
    print(f'  python3 tools/topic_generator.py brief --title "<episode title>" --pillar {key}')


def cmd_brief(args) -> None:
    key = resolve_pillar(args.pillar)
    p = PILLARS[key]
    rendered = BRIEF_TEMPLATE.render(
        title=args.title,
        pillar_name=p["name"],
        created=_dt.date.today().isoformat(),
        mechanics_questions=p["angles"],
        sector_sources=sector_sources_for(key),
    )
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slugify(args.title)}.md"
    out_path.write_text(rendered, encoding="utf-8")
    print(f"Research brief written: {out_path}")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="List the content pillars.").set_defaults(func=cmd_list)

    p_ideas = sub.add_parser("ideas", help="Print research angles for a pillar.")
    p_ideas.add_argument("--pillar", required=True, help="Pillar slug or 1-4.")
    p_ideas.add_argument("--count", type=int, default=5, help="How many angles to show.")
    p_ideas.set_defaults(func=cmd_ideas)

    p_brief = sub.add_parser("brief", help="Generate a full research brief in /topics.")
    p_brief.add_argument("--title", required=True, help="Working episode title.")
    p_brief.add_argument("--pillar", required=True, help="Pillar slug or 1-4.")
    p_brief.add_argument("--out", default="topics", help="Output directory (default: topics).")
    p_brief.set_defaults(func=cmd_brief)

    return parser


def main(argv=None) -> None:
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
