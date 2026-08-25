#!/usr/bin/env python3
"""
validate_script.py — thin wrapper around the canonical script validator.

The real implementation lives at
`.claude/skills/pakistan-documentary-production/scripts/validate_script.py`,
the file the pakistan-documentary-production skill and `/review-script`
both point to. This wrapper exists only so the
`python3 tools/validate_script.py scripts/NN_slug.md` command documented in
README.md keeps working from the repo root, without a second,
independently-maintained copy of the checks that can silently drift out of
sync with the first — which is exactly what had happened here before this
file became a wrapper (the two copies had diverged by hundreds of lines,
disagreeing on required front-matter fields and even on which direction the
banned-transition check should run). See git history for the fix.

Do not add or edit checks in this file. Add them to the canonical file above.

Usage:
    python3 tools/validate_script.py scripts/01_slug.md
    python3 tools/validate_script.py scripts/01_slug.md --strict
"""

import importlib.util
import sys
from pathlib import Path

_CANONICAL = (
    Path(__file__).resolve().parent.parent
    / ".claude" / "skills" / "pakistan-documentary-production"
    / "scripts" / "validate_script.py"
)


def _load_canonical():
    spec = importlib.util.spec_from_file_location(
        "_validate_script_canonical", _CANONICAL
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    if not _CANONICAL.exists():
        print(f"ERROR: canonical validator not found at {_CANONICAL}", file=sys.stderr)
        sys.exit(2)
    _load_canonical().main()
