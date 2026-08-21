#!/usr/bin/env python3
"""
validate_script.py — Script quality and compliance checker.

Checks a production script for structural, editorial, and sourcing compliance
against CLAUDE.md rules. Reports findings without modifying any file.

The validator checks against the script's declared structure, not a fixed
five-section default. Scripts may have any number of sections; the declared
section_count in front-matter is the authority.

IMPORTANT: This tool checks metadata, structure, and possible problems.
It does NOT independently verify the factual accuracy of cited sources.
Source verification requires human inspection of the actual source documents.

Usage:
    python3 tools/validate_script.py scripts/01_slug.md
    python3 tools/validate_script.py scripts/01_slug.md --strict

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

# Legacy five-section templates — used only when template: A/B/C is declared.
LEGACY_TEMPLATE_SECTIONS = {
    "A": ["The Anomaly", "The Paper Trail", "The Field Reality",
          "The Systemic Domino Effect", "The Verdict"],
    "B": ["The Anomaly", "The Business Model", "The Operational Reality",
          "The Competitive Position", "The Verdict"],
    "C": ["The Anomaly", "The Origin", "How It Plays Out",
          "The Structural Risk", "The Verdict"],
}

# Fields required in either YAML or markdown front-matter.
# Each entry: (yaml_key, markdown_field_name)
REQUIRED_FRONTMATTER_FIELDS = [
    ("approved_angle", "Approved angle"),
    ("central_question", "Central question"),
    ("thesis", "Thesis"),
    ("status", "Status"),
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


def extract_sections(text: str) -> list[dict]:
    """Extract ## Part N — or ## SECTION N — headings."""
    pattern = re.compile(
        r"^## (?:Part|SECTION)\s+(\d+)\s*[—–-]+\s*(.+?)(?:\s+\(.*?\))?\s*$",
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


def detect_template(text: str) -> str | None:
    """Detect legacy A/B/C template from old markdown front-matter."""
    m = re.search(r"\*\*Template\*\*\s*:\s*([ABC])", text, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    m = re.search(r"- \*\*Template:\*\*\s*([ABC])", text, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    return None


def detect_structure_type(text: str) -> str | None:
    """Detect structure_type from YAML front-matter."""
    m = re.search(r"^structure_type:\s*(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return None


def extract_declared_section_count(text: str) -> int | None:
    """Read section_count from YAML or markdown front-matter."""
    # YAML style: section_count: 4
    m = re.search(r"^section_count:\s*(\d+)", text, re.MULTILINE)
    if m:
        return int(m.group(1))
    # Markdown style: **Section count:** 4
    m = re.search(
        r"\*\*Section count[:\*]\*?\s*:?\s*(\d+)",
        text, re.IGNORECASE,
    )
    if m:
        return int(m.group(1))
    return None


# --------------------------------------------------------------------------- #
# Check functions — each returns a list of (severity, location, message)
# --------------------------------------------------------------------------- #

Severity = str  # "BLOCK" | "WARN" | "NOTE"


def check_section_count(sections: list[dict], declared_count: int | None) -> list[tuple]:
    """Check actual section count against declared count."""
    issues = []
    actual = len(sections)

    if actual == 0:
        issues.append(("BLOCK", "Structure",
                        "No sections found. Script must contain at least one "
                        "## Part N or ## SECTION N heading."))
        return issues

    if declared_count is None:
        issues.append(("WARN", "Structure metadata",
                        "section_count not declared in front-matter. "
                        "Add it so the validator can confirm the approved structure."))
    elif actual != declared_count:
        issues.append(("WARN", "Structure",
                        f"Section count does not match approved structure: "
                        f"declared {declared_count}, found {actual}."))

    return issues


def check_opening_and_ending(sections: list[dict]) -> list[tuple]:
    """Check that an opening and a grounded ending exist."""
    issues = []
    if not sections:
        return issues

    opening = sections[0]
    if len(opening["body"].split()) < 50:
        issues.append(("WARN", f"Part {opening['n']} (opening)",
                        "Opening section is very short (under 50 words). "
                        "Missing strong opening."))

    ending = sections[-1]
    if len(ending["body"].split()) < 50:
        issues.append(("WARN", f"Part {ending['n']} (ending)",
                        "Closing section is very short (under 50 words). "
                        "Missing grounded ending."))

    return issues


def check_section_names(sections: list[dict], template: str | None) -> list[tuple]:
    """For legacy A/B/C templates, verify section names match the template."""
    issues = []
    if template is None:
        return issues  # Flexible structure — names are user-defined, not checked here

    expected = LEGACY_TEMPLATE_SECTIONS.get(template)
    if not expected:
        issues.append(("WARN", "Front-matter",
                        f"Unknown legacy template value '{template}'. Expected A, B, or C."))
        return issues

    if len(sections) != 5:
        issues.append(("WARN", "Structure",
                        f"Legacy template {template} expects 5 sections, found {len(sections)}."))

    for i, section in enumerate(sections):
        if i >= len(expected):
            break
        exp_title = expected[i]
        actual_title = section["title"]
        if exp_title.lower() not in actual_title.lower():
            issues.append(("WARN", f"Section {section['n']}",
                            f"Template {template} expects '{exp_title}', found '{actual_title}'."))
    return issues


def check_sources_block(text: str) -> list[tuple]:
    issues = []
    if "## SOURCES" not in text and "## Sources" not in text:
        issues.append(("BLOCK", "Structure",
                        "Missing ## SOURCES block. Every script must end with a sources list."))
    else:
        sources_match = re.search(r"## SOURCES?\s*\n(.*?)(?=\n##|\Z)", text,
                                  re.DOTALL | re.IGNORECASE)
        if sources_match:
            sources_content = sources_match.group(1).strip()
            if not sources_content or sources_content in ("1.", "1.\n2.\n3."):
                issues.append(("WARN", "Sources",
                                "SOURCES block exists but appears to be empty or unpopulated."))
    return issues


def check_frontmatter(text: str) -> list[tuple]:
    issues = []
    for yaml_key, md_field in REQUIRED_FRONTMATTER_FIELDS:
        # YAML style: key: value (at start of line)
        yaml_pattern = re.compile(
            rf"^{re.escape(yaml_key)}\s*:", re.MULTILINE | re.IGNORECASE,
        )
        # Markdown style: **Field**: or **Field:**
        md_pattern = re.compile(
            rf"\*\*{re.escape(md_field)}\*\*\s*:|\*\*{re.escape(md_field)}:\*\*",
            re.IGNORECASE,
        )
        if not yaml_pattern.search(text) and not md_pattern.search(text):
            issues.append(("WARN", "Front-matter",
                            f"Missing field: '{md_field}' (YAML key: {yaml_key})."))
    return issues


def check_opening_section(sections: list[dict]) -> list[tuple]:
    """Check opening section rhythm — applicable to any story logic."""
    issues = []
    if not sections:
        return issues
    s1 = sections[0]
    body = s1["body"]

    sentences = re.split(r"(?<=[.!?])\s+", body.strip())
    long_sentences = [s for s in sentences[:10] if len(s.split()) > 25]
    if long_sentences:
        for s in long_sentences:
            issues.append(("WARN", f"Part {s1['n']} (opening)",
                            f"Long sentence in opening ({len(s.split())} words): "
                            f"'{s[:80]}...'"))

    transition_patterns = [
        r"was not an accident", r"was not a coincidence", r"did not appear by itself",
        r"this was not", r"that was not",
    ]
    has_transition = any(re.search(p, body, re.IGNORECASE) for p in transition_patterns)
    if not has_transition:
        issues.append(("WARN", f"Part {s1['n']} (opening)",
                        "No transitional echo sentence found "
                        "('That [X] was not an accident' or equivalent)."))

    question_pattern = re.compile(r"[A-Z][^.!?]*\?", re.MULTILINE)
    questions = question_pattern.findall(body)
    if not questions:
        issues.append(("WARN", f"Part {s1['n']} (opening)",
                        "Opening section does not appear to close with a question. "
                        "The central question should appear at the end of the opening."))

    return issues


def check_nonfiction(text: str, sections: list[dict]) -> list[tuple]:
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
                issues.append(("WARN", f"Part {section['n']}",
                                f"Possible repeated definition near: '...{m.group(1)[:50]}...'. "
                                "Every concept is stated once (CLAUDE.md rule 2)."))
            else:
                defined_terms[term_snippet] = section["n"]
    return issues


def check_sourcing(text: str, sections: list[dict]) -> list[tuple]:
    issues = []
    source_tag_count = len(re.findall(r"\[SOURCE:", text, re.IGNORECASE))
    verify_count = len(re.findall(r"\[VERIFY\]", text, re.IGNORECASE))

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
                        "figures detected. Every statistical claim requires a source tag."))
    elif source_tag_count < len(stat_claims) // 3:
        issues.append(("WARN", "Sourcing",
                        f"Low source-tag ratio: {source_tag_count} tags for approximately "
                        f"{len(stat_claims)} statistical figures. Check for unsourced claims."))

    if verify_count > 5:
        issues.append(("WARN", "Sourcing",
                        f"High [VERIFY] count: {verify_count}. "
                        "Resolve these before recording (re-verify all current figures)."))

    return issues, source_tag_count, verify_count


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def run(path: Path, strict: bool = False) -> int:
    text = load_file(path)
    sections = extract_sections(text)
    template = detect_template(text)
    structure_type = detect_structure_type(text)
    declared_count = extract_declared_section_count(text)
    narration_words = word_count(text)
    duration = estimate_duration(narration_words)

    all_issues: list[tuple] = []

    all_issues += check_section_count(sections, declared_count)
    all_issues += check_opening_and_ending(sections)
    all_issues += check_section_names(sections, template)
    all_issues += check_sources_block(text)
    all_issues += check_frontmatter(text)
    all_issues += check_opening_section(sections)
    all_issues += check_nonfiction(text, sections)
    all_issues += check_script_purity(text)
    all_issues += check_cliches(text)
    all_issues += check_em_dashes(text)
    all_issues += check_repetition(sections)

    sourcing_result = check_sourcing(text, sections)
    sourcing_issues, source_tag_count, verify_count = sourcing_result
    all_issues += sourcing_issues

    block_issues = [i for i in all_issues if i[0] == "BLOCK"]
    warn_issues = [i for i in all_issues if i[0] == "WARN"]

    structure_label = template or structure_type or "flexible (undeclared)"

    print(f"\n{'='*60}")
    print(f"  Script validator: {path.name}")
    print(f"{'='*60}\n")

    print(f"  Words:           {narration_words:,}")
    print(f"  Est. duration:   {duration} (at {WORDS_PER_MINUTE} wpm)")
    print(f"  Structure:       {structure_label}")
    print(f"  Declared parts:  {declared_count if declared_count is not None else 'not set'}")
    print(f"  Parts found:     {len(sections)}")
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
    print("  NOTE: This tool checks structure and metadata only.")
    print("  Factual accuracy requires human inspection of the actual sources.")
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
