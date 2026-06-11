# kahoot-quiz-creator

A [Claude](https://claude.com) **Agent Skill** that designs a Kahoot quiz and enters it directly into the Kahoot web editor (`create.kahoot.it`) using browser automation.

It works in two phases:

1. **Content design** — clarifies the topic/audience/language, then writes a balanced set of multiple-choice questions (recognition, knowledge, famous things, traditions, funny-but-guessable, etc.) with marked correct answers and read-aloud explanations.
2. **Browser automation** — logs you (the user) into Kahoot, creates the kahoot, and types every question and answer into the editor, marking the correct option on each. It drives the editor by element role/label rather than pixel coordinates, which is what makes it reliable.

## What's inside

```
kahoot-quiz-creator/
├── SKILL.md                          # entry point: the two-phase workflow
├── references/
│   ├── content-design.md             # how to write good quiz questions
│   └── browser-automation.md         # exact Kahoot editor mechanics + per-question loop
└── assets/
    └── example-quiz.md               # an example quiz in the target format
```

## Requirements

- Claude with the **Claude-in-Chrome** browser tools available.
- A Kahoot account. **You log in yourself** — the skill never enters your password.

## Notes & limitations

- Kahoot has no field for explanations, so the skill keeps them in a companion Markdown document for the host to read aloud.
- Character limits: question text ≈120 chars, each answer ≈75 chars.
- Free Kahoot accounts support Quiz and True/False question types; the skill uses 4-option Quiz by default.
- The skill saves to your private library and will not publish or share publicly without your explicit go-ahead.

## Usage

Install the skill, then ask something like:

> "Make me a 20-question Kahoot quiz about the solar system for 6th graders, and put it into Kahoot."

## License

MIT — do whatever you like; attribution appreciated.
