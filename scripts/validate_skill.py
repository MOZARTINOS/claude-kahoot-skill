#!/usr/bin/env python3
"""Validate the distributable Kahoot skill without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILE = ROOT / "SKILL.md"
EXPECTED_NAME = "kahoot-quiz-creator"
REQUIRED_FILES = (
    "SKILL.md",
    "references/content-design.md",
    "references/browser-automation.md",
    "references/example-quiz.md",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            fail(f"missing required file: {relative_path}")

    text = SKILL_FILE.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()

    if set(fields) != {"name", "description"}:
        fail("frontmatter must contain only name and description")
    if fields["name"] != EXPECTED_NAME:
        fail(f"name must be {EXPECTED_NAME!r}")
    if not fields["description"]:
        fail("description must not be empty")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", fields["name"]):
        fail("name must use lowercase letters, digits, and hyphens")

    markdown_paths = set(
        re.findall(r"`((?:assets|references)/[^`\s]+\.md)`", text)
    )
    for relative_path in markdown_paths:
        if not (ROOT / relative_path).is_file():
            fail(f"SKILL.md references a missing file: {relative_path}")

    print("Skill validation passed.")


if __name__ == "__main__":
    main()
