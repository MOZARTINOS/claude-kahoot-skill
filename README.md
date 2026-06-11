# Kahoot Quiz Creator

![Illustration of a quiz editor with four answer choices, content drafting, verification, approval, and browser automation](docs/images/kahoot-quiz-creator-hero.webp)

An unofficial [Claude](https://claude.ai) Agent Skill for designing a reviewable Kahoot quiz and, with explicit user approval, entering it into the Kahoot web editor through browser automation.

The skill separates two actions:

1. **Content design** creates a Markdown quiz with answers, explanations, and verification notes.
2. **Optional Kahoot import** opens `create.kahoot.it` only when the user explicitly requests it, waits for the user to sign in, and enters the approved questions.

## Safety model

- A content-only request never changes a Kahoot account.
- The user reviews the completed quiz before browser automation begins.
- The user signs in and completes authentication themselves.
- The skill does not publish, share, assign, or start a game without separate approval.
- If the live editor or browser tools are incompatible, the skill stops and preserves the quiz document instead of using blind coordinate automation.

## Requirements

- Claude with custom Skills support.
- For optional import: browser automation capable of semantic element inspection and interaction.
- A Kahoot account. Availability of question types varies by account and subscription.

The automation reference was last reviewed on **June 11, 2026**. Kahoot and browser-tool interfaces can change.

## Install

### From a release

1. Download `kahoot-quiz-creator.zip` from the latest [GitHub release](https://github.com/MOZARTINOS/claude-kahoot-skill/releases).
2. In Claude, open **Customize > Skills**.
3. Select **+ > Create skill > Upload a skill**.
4. Upload the ZIP file and enable the skill.

The release archive contains a top-level `kahoot-quiz-creator/` folder, as required by Claude's custom-skill uploader.

### From source

Run:

```powershell
python scripts/package_skill.py
```

Then upload `dist/kahoot-quiz-creator.zip` using the steps above. Do not upload GitHub's automatically generated source ZIP directly because its root folder has a different name.

## Usage

Content only:

> Create a 20-question solar-system quiz for sixth graders. Include explanations and sources, but do not open Kahoot.

Content plus import:

> Create a 20-question solar-system quiz for sixth graders. After I approve it, put it into Kahoot.

## Repository layout

```text
SKILL.md                         Skill entry point and authorization rules
references/content-design.md     Quiz quality and fact-checking guidance
references/browser-automation.md Kahoot interaction strategy and safeguards
references/example-quiz.md       Companion-document format example
scripts/validate_skill.py        Repository validation
scripts/package_skill.py         Reproducible release ZIP builder
```

## Development

Validate and package locally:

```powershell
python scripts/validate_skill.py
python scripts/package_skill.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution requirements and [SECURITY.md](SECURITY.md) for private vulnerability reporting.

## Limitations

- The portable default is a four-option Quiz with one correct answer. Kahoot supports other formats depending on the plan and live editor.
- Standard Quiz limits are currently 120 characters per question and 75 per answer.
- Explanations and source notes are kept in the companion Markdown document.
- Browser automation depends on a third-party interface and may require maintenance after UI changes.

## Disclaimer

This independent project is not affiliated with, endorsed by, or sponsored by Kahoot! ASA or Anthropic PBC. Kahoot! and Claude are trademarks of their respective owners.

## License

[MIT](LICENSE)
