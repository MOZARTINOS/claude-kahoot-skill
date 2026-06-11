# Contributing

Contributions that improve quiz quality, safety, compatibility, or documentation are welcome.

## Before opening a pull request

1. Keep account-changing actions behind explicit user approval.
2. Do not add credentials, cookies, session data, personal quiz content, or screenshots containing private account information.
3. Treat browser labels and workflows as version-sensitive. Include the date and environment used when updating automation instructions.
4. Prefer authoritative sources for Kahoot limits and current product behavior.
5. Run:

```powershell
python scripts/validate_skill.py
python scripts/package_skill.py
```

The packaged ZIP must contain `kahoot-quiz-creator/SKILL.md` at its root and must not contain repository-only files such as `.git`, `.github`, or `README.md`.

## Pull requests

Describe the behavior changed, how it was verified, and whether it affects browser automation or account actions. Keep unrelated changes out of the same pull request.
