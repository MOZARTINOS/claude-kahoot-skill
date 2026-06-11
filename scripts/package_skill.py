#!/usr/bin/env python3
"""Build the uploadable Claude skill archive."""

from __future__ import annotations

import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "kahoot-quiz-creator"
DIST = ROOT / "dist"
ARCHIVE = DIST / f"{SKILL_NAME}.zip"
PACKAGE_FILES = (
    Path("SKILL.md"),
    Path("references/content-design.md"),
    Path("references/browser-automation.md"),
    Path("references/example-quiz.md"),
)


def main() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/validate_skill.py")],
        check=True,
        cwd=ROOT,
    )

    DIST.mkdir(exist_ok=True)
    if ARCHIVE.exists():
        ARCHIVE.unlink()

    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative_path in PACKAGE_FILES:
            source = ROOT / relative_path
            archive_path = (Path(SKILL_NAME) / relative_path).as_posix()
            entry = zipfile.ZipInfo(archive_path, date_time=(2026, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            normalized_text = source.read_text(encoding="utf-8").replace("\r\n", "\n")
            archive.writestr(entry, normalized_text.encode("utf-8"))

    print(f"Built {ARCHIVE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
