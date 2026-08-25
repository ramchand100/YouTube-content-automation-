#!/usr/bin/env python3
"""
validate_script.py — Script quality and compliance checker.

Checks a production script for structural, editorial, and sourcing compliance
against CLAUDE.md rules. Reports findings without modifying any file.

IMPORTANT: This tool checks mechanical, reliably-detectable things only:
structure, front-matter completeness, banned phrases, citation presence,
word counts, and paragraph length. It does NOT and cannot reliably check
judgment-based rules — hook quality, retention-bridge quality, whether a
number's daily-life comparison actually lands, whether the script reads as
a decision chain rather than a fact list, or factual accuracy of sources.
Those require a human or an LLM-driven review; see `/review-script`.

Usage:
    python3 .claude/skills/pakistan-documentary-production/scripts/validate_script.py scripts/13_gwadar_karachi.md
    python3 .claude/skills/pakistan-documentary-production/scripts/validate_script.py scripts/13_gwadar_karachi.md --strict

Exit codes:
    0 — PASS (no blocking issues)
    1 — NEEDS REVISION (one or more blocking issues)
    2 — ERROR (file not found or unreadable)

Dependencies: standard library only (no Jinja2 or rich required).
"""

import argparse
import re
import sys
from pathlib import Path

WORDS_PER_MINUTE = 150

BANNED_CLICHES = [
    "game-changer", "game changer", "at the end of the day",
    "synergy", "synergies", "disruptive", "move the needle",
    "paradigm shift", "low-hanging fruit", "circle back",
    "take this to the next level", "leverage", "journey",
    "thought leader", "innovative solution",
]

# Formulaic opening transitions banned by docs/editorial/storytelling.md and
# .claude/rules/scripts.md. These must NOT appear — do not confuse this with
# a requirement to include one (an earlier version of this validator did,
# which was backwards).
BANNED_TRANSITIONS = [
    r"was not an accident", r"was not a coincidence",
    r"did not appear by itself", r"the numbers tell the story",
    r"but the real story is",
]

# CLAUDE.md sec4 rule 6 / docs/editorial/prose-style.md "Political neutrality".
# Flags language that frames a decision as political strategy rather than
# administrative/economic mechanics. Heuristic — a hit is worth a human look,
# not an automatic fail (e.g. "the government" as an institutional actor is
# fine; "political win" or "before the next election" is not).
POLITICAL_FRAMING_PATTERNS = [
    r"\bpolitical\s+(win|cost|incentive|strategy|efficiency)\b",
    r"\bribbon[\s-]cutting\b", r"\bribbon\s+was\s+cut\b",
    r"\bbefore\s+the\s+next\s+election\b", r"\belection[\s-]timing\b",
    r"\bcampaign\s+trail\b",
]

FICTIONAL_SCENE_PATTERNS = [
    r"\bwalked into\b", r"\bpicked up the phone\b", r"\bsat down and\b",
    r"\bremembered the day\b", r"\bfelt the weight\b", r"\bstared at\b",
    r"\bhe said\b", r"\bshe said\b", r"\bthey said\b",
    r"\bhe knew\b", r"\bshe knew\b", r"\bhe thought\b", r"\bshe thought\b",
    r"\bhe decided\b", r"\bshe decided\b",
    r"\ba small factory\b", r"\ba local shop\b",
]

VISUAL_CUE_PATTERNS = [
    r"\[VISUAL\b", r"\[FOOTAGE\b", r"\[B-ROLL\b", r"\[B-roll\b",
    r"\[GRAPHIC\b", r"\[ANIMATION\b", r"\[CUT TO\b",
    r"\[MUSIC\b", r"\[SFX\b",
]

# Legacy five-section templates (.claude/rules/scripts.md, "Legacy five-section
# format"). Only checked when front-matter structure_type is legacy-A/B/C.
TEMPLATE_SECTIONS = {
    "A": ["The Anomaly", "The Paper Trail", "The Field Reality",
          "The Systemic Domino Effect", "The Verdict"],
    "B": ["The Anomaly", "The Business Model", "The Operational Reality",
          "The Competitive Position", "The Verdict"],
    "C": ["The Anomaly", "The Origin", "How It Plays Out",
          "The Structural Risk", "The Verdict"],
}

# The actual required YAML front-matter fields per .claude/rules/scripts.md.
REQUIRED_FRONTMATTER_FIELDS = [
    "episode", "title", "topic", "approved_angle", "central_question",
    "thesis", "story_logic", "structure_type", "section_count", "status",
    "research_date", "data_cutoff_date", "freshness_status", "word_count",
    "estimated_duration", "last_verified",
]


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def load_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        sys.exit(2)
    except Exception as exc:
        print(f"ERROR: Cannot read {path}: {exc}", file=sys.stderr)
        sys.exit(2)


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def estimate_duration(words: int) -> str:
    total_sec = round(words / WORDS_PER_MINUTE * 60)
    return f"{total_sec // 60}m {total_sec % 60:02d}s"


def extract_frontmatter(text: str) -> dict:
    """Parse the YAML-style '---' front-matter block into a flat dict.

    Deliberately simple (no PyYAML dependency): handles `key: value` and
    `key: "value"` lines. Multi-line/nested YAML values are not needed by
    any field this repo's scripts actually use.
    """
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        fm[key] = value
    return fm


def extract_sections(text: str, structure_type: str) -> list[dict]:
    """Extract '## Part N — Title' sections (the current flexible format), or
    '## SECTION N — Title' when structure_type is a legacy-A/B/C script.
    """
    heading = "SECTION" if structure_type.startswith("legacy") else "Part"
    pattern = re.compile(
        rf"^## {heading} (\d+)\s*[—–-]+\s*(.+?)(?:\s+\(.*?\))?\s*$",
        re.MULTILINE,
    )
    matches = list(pattern.finditer(text))
    sections = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections.append({
            "n": int(m.group(1)),
            "title": m.group(2).strip(),
            "body": text[start:end],
        })
    return sections


# --------------------------------------------------------------------------- #
# Check functions — each returns a list of (severity, location, message)
# --------------------------------------------------------------------------- #

Severity = str  # "BLOCK" | "WARN" | "NOTE"


def check_section_count(sections: list[dict], frontmatter: dict) -> list[tuple]:
    issues = []
    declared = frontmatter.get("section_count")
    if declared is None:
        issues.append(("WARN", "Front-matter",
                        "No section_count field found; cannot verify it matches "
                        "the number of '## Part N —' headings actually present."))
        return issues
    try:
        declared_n = int(declared)
    except ValueError:
        issues.append(("WARN", "Front-matter",
                        f"section_count value '{declared}' is not a number."))
        return issues
    if declared_n != len(sections):
        issues.append(("BLOCK", "Structure",
                        f"front-matter declares section_count: {declared_n}, but "
                        f"{len(sections)} '## Part N —' headings were found. "
                        "Scripts may use any number of sections the story logic "
                        "requires (.claude/rules/scripts.md) — this only flags a "
                        "mismatch between the declared count and the actual body."))
    return issues


def check_section_names(sections: list[dict], structure_type: str) -> list[tuple]:
    issues = []
    if not structure_type.startswith("legacy"):
        return issues  # flexible structure has no fixed names to check
    template = structure_type.split("-")[-1].upper() if "-" in structure_type else None
    expected = TEMPLATE_SECTIONS.get(template)
    if not expected:
        issues.append(("WARN", "Front-matter",
                        f"structure_type '{structure_type}' looks legacy but doesn't "
                        "map to template A, B, or C."))
        return issues
    for i, section in enumerate(sections):
        if i >= len(expected):
            break
        exp_title = expected[i]
        actual_title = section["title"]
        if exp_title.lower() not in actual_title.lower():
            issues.append(("WARN", f"Section {section['n']}",
                            f"Legacy template {template} expects '{exp_title}', "
                            f"found '{actual_title}'."))
    return issues


def check_sources_block(text: str) -> list[tuple]:
    issues = []
    if "## Sources" not in text and "## SOURCES" not in text:
        issues.append(("BLOCK", "Structure",
                        "Missing ## Sources block. Every script must end with a sources list."))
    else:
        sources_match = re.search(r"## Sources?\s*\n(.*?)(?=\n##|\Z)", text,
                                   re.DOTALL | re.IGNORECASE)
        if sources_match:
            sources_content = sources_match.group(1).strip()
            if not sources_content or sources_content in ("1.", "1.\n2.\n3."):
                issues.append(("WARN", "Sources",
                                "Sources block exists but appears to be empty or unpopulated."))
    return issues


def check_frontmatter(frontmatter: dict) -> list[tuple]:
    issues = []
    if not frontmatter:
        issues.append(("BLOCK", "Front-matter",
                        "No YAML front-matter block found between '---' delimiters."))
        return issues
    for field in REQUIRED_FRONTMATTER_FIELDS:
        if field not in frontmatter or not frontmatter[field]:
            issues.append(("WARN", "Front-matter",
                            f"Missing or empty front-matter field: '{field}'."))
    return issues


def check_opening(sections: list[dict]) -> list[tuple]:
    """Mechanical checks only. Whether the hook actually lands fast and
    whether the retention bridge actually reads well are judgment calls for
    /review-script, not something this regex-based tool can assess safely.
    """
    issues = []
    if not sections:
        return issues
    s1 = sections[0]
    body = s1["body"]

    for pattern in BANNED_TRANSITIONS:
        if re.search(pattern, body, re.IGNORECASE):
            issues.append(("BLOCK", "Part 1",
                            f"Banned formulaic transition found (pattern '{pattern}'). "
                            "docs/editorial/storytelling.md bans these outright — "
                            "do not use one, do not add one."))

    question_pattern = re.compile(r"[A-Z][^.!?]*\?", re.MULTILINE)
    if not question_pattern.findall(body):
        issues.append(("NOTE", "Part 1",
                        "No question mark found in the opening part. Confirm the "
                        "central question is stated in a natural sentence "
                        "(.claude/rules/scripts.md, Opening section rhythm)."))

    return issues


def check_nonfiction(text: str) -> list[tuple]:
    issues = []
    for pattern in FICTIONAL_SCENE_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            issues.append(("WARN", "Nonfiction",
                            f"Possible fictional scene detected: pattern '{pattern}' found "
                            f"{len(matches)} time(s). Verify these are documented facts."))
    return issues


def check_script_purity(text: str) -> list[tuple]:
    issues = []
    for pattern in VISUAL_CUE_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(("BLOCK", "Script purity",
                            f"Visual/production direction found in script: '{pattern}'. "
                            "Scripts are pure voiceover prose. Move all visual direction "
                            "to the companion storyboard file."))
    if re.search(r"\[MUSIC\b|\bsoundtrack\b|\bbackground music\b", text, re.IGNORECASE):
        issues.append(("BLOCK", "Script purity",
                        "Music direction found inside script. Remove it."))
    # Delivery-notes markup (**bold**, ' / ' pause marks) belongs only in
    # delivery-notes/NN_slug_delivery-notes.md, never in the script itself.
    if re.search(r"\*\*[^*\n]+\*\*", text):
        issues.append(("BLOCK", "Script purity",
                        "Found **bold** markup in the script body. Emphasis/pause "
                        "markup belongs only in the delivery-notes companion file "
                        "(.claude/rules/delivery-notes.md), never in scripts/*.md."))
    if re.search(r"\w\s/\s\w", text):
        issues.append(("WARN", "Script purity",
                        "Found ' / ' inside narration text, which is the delivery-notes "
                        "pause marker. Confirm this isn't stray markup left in the "
                        "script by mistake (it happened once in ep13 — see git history)."))
    return issues


def check_political_framing(text: str) -> list[tuple]:
    issues = []
    for pattern in POLITICAL_FRAMING_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(("WARN", "Neutral framing",
                            f"Possible political-strategy framing (pattern '{pattern}'). "
                            "CLAUDE.md sec4 rule 6 wants administrative/economic framing "
                            "instead — see docs/editorial/prose-style.md, "
                            "'Political neutrality'."))
    return issues


def check_cliches(text: str) -> list[tuple]:
    issues = []
    for cliche in BANNED_CLICHES:
        if cliche.lower() in text.lower():
            issues.append(("WARN", "Language",
                            f"Banned cliché found: '{cliche}'. "
                            "Remove or rewrite (see CLAUDE.md section 4)."))
    return issues


def check_em_dashes(text: str) -> list[tuple]:
    issues = []
    count = text.count("—")
    if count > 0:
        issues.append(("WARN", "Language",
                        f"Found {count} em dash(es). Replace with comma or period "
                        "where possible (CLAUDE.md section 4)."))
    return issues


def check_paragraph_rhythm(sections: list[dict]) -> list[tuple]:
    """docs/editorial/prose-style.md, 'Paragraph rhythm': narration paragraphs
    should be one or two sentences, one spoken beat each.
    """
    issues = []
    for section in sections:
        paragraphs = [p.strip() for p in section["body"].split("\n\n") if p.strip()]
        for p in paragraphs:
            clean = re.sub(r"\[.*?\]", "", p)  # strip citation/VERIFY tags
            sentence_count = len(re.findall(r"[.!?](?:\s|$)", clean))
            if sentence_count > 2:
                issues.append(("NOTE", f"Section {section['n']}",
                                f"Paragraph has {sentence_count} sentences — "
                                f"consider breaking into shorter spoken beats: "
                                f"'{p[:70]}...'"))
    return issues


def check_repetition(sections: list[dict]) -> list[tuple]:
    issues = []
    defined_terms: dict[str, int] = {}
    definition_pattern = re.compile(
        r"(?:—|,\s*(?:meaning|which means|that is|defined as|known as))\s*([a-z][^.]{5,60})\.",
        re.IGNORECASE
    )
    for section in sections:
        for m in definition_pattern.finditer(section["body"]):
            term_snippet = m.group(1)[:30].lower().strip()
            if term_snippet in defined_terms:
                issues.append(("WARN", f"Section {section['n']}",
                                f"Possible repeated definition near: '...{m.group(1)[:50]}...'. "
                                "Every concept is stated once (CLAUDE.md rule 2)."))
            else:
                defined_terms[term_snippet] = section["n"]
    return issues


def check_sourcing(text: str) -> tuple:
    issues = []
    source_tag_count = len(re.findall(r"\[SOURCE:", text, re.IGNORECASE))
    verify_count = len(re.findall(r"\[VERIFY", text, re.IGNORECASE))

    number_pattern = re.compile(
        r"(?:Rs\.?\s*[\d,.]+\s*(?:billion|million|crore|trillion)?|"
        r"\d+[\d,.]*\s*(?:percent|%)|"
        r"\$\s*[\d,.]+\s*(?:billion|million)?|"
        r"\d{1,3}(?:,\d{3})+)",
        re.IGNORECASE
    )
    stat_claims = number_pattern.findall(text)

    if source_tag_count == 0 and stat_claims:
        issues.append(("BLOCK", "Sourcing",
                        f"No [SOURCE: ...] tags found, but {len(stat_claims)} statistical "
                        "figures detected. Every statistical claim requires a source tag "
                        "(a REPORTED/ESTIMATE/VERIFY classification tag also satisfies this)."))
    elif source_tag_count < len(stat_claims) // 3:
        issues.append(("NOTE", "Sourcing",
                        f"Low [SOURCE:] tag ratio: {source_tag_count} tags for approximately "
                        f"{len(stat_claims)} statistical figures. Many may instead carry "
                        "[REPORTED]/[ESTIMATE]/[VERIFY] tags, which is fine — spot-check."))

    if verify_count > 5:
        issues.append(("NOTE", "Sourcing",
                        f"{verify_count} [VERIFY] tags found. Resolve these before "
                        "recording (re-verify all current figures)."))

    return issues, source_tag_count, verify_count


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def run(path: Path, strict: bool = False) -> int:
    text = load_file(path)
    frontmatter = extract_frontmatter(text)
    structure_type = frontmatter.get("structure_type", "flexible")
    sections = extract_sections(text, structure_type)
    narration_words = word_count(text)
    duration = estimate_duration(narration_words)

    all_issues: list[tuple] = []

    all_issues += check_section_count(sections, frontmatter)
    all_issues += check_section_names(sections, structure_type)
    all_issues += check_sources_block(text)
    all_issues += check_frontmatter(frontmatter)
    all_issues += check_opening(sections)
    all_issues += check_nonfiction(text)
    all_issues += check_script_purity(text)
    all_issues += check_political_framing(text)
    all_issues += check_cliches(text)
    all_issues += check_em_dashes(text)
    all_issues += check_paragraph_rhythm(sections)
    all_issues += check_repetition(sections)

    sourcing_issues, source_tag_count, verify_count = check_sourcing(text)
    all_issues += sourcing_issues

    block_issues = [i for i in all_issues if i[0] == "BLOCK"]
    warn_issues = [i for i in all_issues if i[0] == "WARN"]

    print(f"\n{'='*60}")
    print(f"  Script validator: {path.name}")
    print(f"{'='*60}\n")

    print(f"  Words:           {narration_words:,}")
    print(f"  Est. duration:   {duration} (at {WORDS_PER_MINUTE} wpm)")
    print(f"  structure_type:  {structure_type}")
    print(f"  Sections found:  {len(sections)}"
          + (f" (declared: {frontmatter.get('section_count')})" if frontmatter.get("section_count") else ""))
    print(f"  [SOURCE:] tags:  {source_tag_count}")
    print(f"  [VERIFY] tags:   {verify_count}")
    print()

    if all_issues:
        print("  Findings:")
        print(f"  {'#':<4} {'Sev':<6} {'Location':<25} Message")
        print(f"  {'-'*4} {'-'*6} {'-'*25} {'-'*40}")
        for i, (sev, loc, msg) in enumerate(all_issues, 1):
            print(f"  {i:<4} {sev:<6} {loc:<25} {msg[:80]}")
            if len(msg) > 80:
                print(f"  {'':4} {'':6} {'':25}   ...{msg[80:]}")
        print()

    if block_issues:
        print(f"  BLOCK items ({len(block_issues)}) — must fix before production-ready:")
        for sev, loc, msg in block_issues:
            print(f"    - [{loc}] {msg[:100]}")
        print()

    overall = "PASS" if not block_issues else "NEEDS REVISION"
    if strict and warn_issues:
        overall = "NEEDS REVISION"

    print(f"  Overall: {overall}")
    print()

    print("  NOTE: This tool checks mechanical structure, metadata, and banned")
    print("  language only. Hook quality, retention-bridge quality, whether a")
    print("  number's daily-life comparison lands, decision-chain vs. fact-list")
    print("  storytelling, neutral-framing nuance, and factual accuracy all")
    print("  require /review-script or a human read.")
    print(f"{'='*60}\n")

    return 0 if overall == "PASS" else 1


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("script", type=Path, help="Path to the script .md file.")
    parser.add_argument("--strict", action="store_true",
                        help="Treat WARN items as blocking (stricter gate).")
    args = parser.parse_args(argv)
    sys.exit(run(args.script, args.strict))


if __name__ == "__main__":
    main()
