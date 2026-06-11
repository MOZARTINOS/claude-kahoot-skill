# CLAUDE.md

Guidance for Claude Code (and other AI agents) working in this repository.

## What this is

An **unofficial Claude Agent Skill** that designs reviewable Kahoot quizzes and, only on
explicit user approval, enters them into the Kahoot web editor via browser automation.
This repo is the **distributable source** of that skill — not an application. The product
is the skill itself (`SKILL.md` + `references/`), packaged into an uploadable ZIP.

Public repo: https://github.com/MOZARTINOS/claude-kahoot-skill

## Repository layout

```text
SKILL.md                          Skill entry point + authorization rules (the contract)
references/content-design.md      Quiz quality and fact-checking guidance
references/browser-automation.md  Kahoot interaction strategy and safeguards
references/example-quiz.md        Companion-document format example
scripts/validate_skill.py         Structure/frontmatter validation (no deps)
scripts/package_skill.py          Reproducible release ZIP builder → dist/
docs/images/                      README artwork (hero .webp)
.github/workflows/                validate.yml (CI) + release.yml (tag-triggered)
```

## Core invariants — do not break

These are the reason the skill exists. Changes to `SKILL.md` must preserve them:

1. **Two-phase split.** Phase 1 (design a reviewable Markdown quiz) is the default
   deliverable. Phase 2 (browser import) runs ONLY after explicit user request + content
   approval. A request for quiz content never authorizes touching a Kahoot account.
2. **User authenticates themselves.** Never enter passwords or sign in for the user.
3. **No publish/share/assign/start** without separate explicit approval. Saving to the
   user's private library is the ceiling.
4. **Semantic automation, never blind coordinates.** Drive the editor by element
   role/label. If browser tools are incompatible, stop and preserve the quiz document.

## Skill format constraints

- `SKILL.md` frontmatter must contain **only** `name` and `description` (validator enforces).
- `name` must be `kahoot-quiz-creator` (lowercase/digits/hyphens, ≤64 chars).
- File references inside `SKILL.md` must point to existing `references/...` paths — the
  validator greps `` `references/x.md` `` / `` `assets/x.md` `` and fails on missing files.
- The four files in `REQUIRED_FILES` (see `validate_skill.py`) are what actually ship in the
  ZIP. README/CI/community files are repo-only and are NOT packaged.

## Local workflow

```powershell
python scripts/validate_skill.py    # must pass before committing skill changes
python scripts/package_skill.py     # builds dist/kahoot-quiz-creator.zip
```

CI (`validate.yml`) runs both on every push/PR to `main`. Keep it green.

## Release flow

Push a `v*` tag → `release.yml` rebuilds the ZIP and publishes a GitHub Release with
auto-generated notes and `dist/kahoot-quiz-creator.zip` attached.

```powershell
git tag -a v0.2.0 -m "v0.2.0 — <summary>"
git push origin v0.2.0
```

Bump the "last reviewed" date in `README.md` and `references/browser-automation.md` when
the Kahoot/browser-tool interaction strategy is re-verified.

## Conventions

- **Conventional commits**, no attribution line (`feat:`, `fix:`, `chore:`, `docs:`).
- Binary assets (`*.webp/.png/.jpg/.gif/.zip`) are pinned `binary` in `.gitattributes`;
  text is normalized to LF. Add new binary extensions there before committing them.
- `*.skill` and `dist/` are gitignored — build artifacts never get committed.
- GitHub Actions are SHA-pinned; let Dependabot bump them rather than editing by hand.
- Keep the disclaimer intact: not affiliated with Kahoot! ASA or Anthropic PBC.
