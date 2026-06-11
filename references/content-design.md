# Content design for a Kahoot quiz

Good Kahoot content is the part that makes the game fun. The editor only stores text — the craft is in the questions. Use these principles, adapting freely to the audience.

## Format for every question

Write each question in this exact shape so it transfers cleanly into the editor and into the companion document:

```
Question N: [question text, ≈120 chars max]
A. [option]   B. [option]   C. [option]   D. [option]   (each ≈75 chars max)
Correct answer: [A/B/C/D]
Explanation: [one short sentence the host reads aloud]
```

Use a 4-option Quiz with one correct answer as this skill's portable default. Kahoot can support fewer or more options and multiple correct answers depending on the question type and subscription, but only use those variants when the user requests them and the live editor supports them. The explanation lives in the companion document for the host to read after the timer ends.

## The question mix

A quiz that's all the same kind of question gets boring fast. Aim for a deliberate spread. A useful default mix for ~20–25 questions:

- **Recognition / identification** — "Which of these is X?" Concrete and easy to start with.
- **Core knowledge** — the actual facts you want to reinforce.
- **Recognition of famous things** — melodies, logos, quotes, landmarks; players love these.
- **Traditions / culture** — context the audience shares.
- **Funny / guessable** — at least a few questions where even someone who doesn't know can laugh and guess from the options. These keep energy high and let weaker players score. Make the wrong options playful but clearly wrong (e.g., a fictional "unicorn horn" among real instruments).
- **A couple of "applied" or comparison questions** — "What's the difference between X and Y?"

State the categories you're targeting up front and make sure each is represented.

## Difficulty and audience

- Keep difficulty in an **easy-to-moderate** band for mixed/young audiences; avoid niche expert trivia unless the user asks. A spread of mostly-easy with a few moderate questions keeps everyone engaged.
- **Age-appropriateness:** for children/teens, keep language, examples, and humor friendly and clean. If the group spans several age bands (e.g., a school with younger and older kids), bias toward the younger end so everyone can play.
- **Localize.** Swap generic references for ones the players actually know — local holidays, regional names, school or workplace traditions, things specific to the group. A question anchored in something the audience has actually experienced lands far better than a generic one.

## Wrong-answer (distractor) craft

The three wrong options ("distractors") decide how good a question is. Make them plausible-but-wrong for serious questions, and amusing-but-clearly-wrong for the funny ones. Avoid two options that could both be argued correct. Vary which letter is correct across the quiz so there's no guessable pattern.

## Fact checking and ambiguity

- Verify unstable facts such as current officeholders, records, prices, rankings, populations, and recent events at the time the quiz is created.
- Prefer primary or authoritative sources. For disputed topics, either avoid the question or state the intended convention precisely.
- Check that the explanation supports the marked answer and does not introduce a conflicting claim.
- Add a short `Sources / verification notes` section to the companion document when the quiz relies on current or specialized facts.
- Never fabricate a citation. If reliable verification is unavailable, flag the question for review or replace it.

## Tie-breakers

Offer 5 bonus tie-breaker questions for when teams finish level. These work best as numeric-estimate or single-fact questions ("How many keys on a piano?") where "closest" or "first correct" decides it. Keep them in the companion document; they're usually asked verbally rather than added as Kahoot slides.

## The companion document

Always deliver a Markdown file containing the full quiz in the format above, plus any requested tie-breakers and verification notes. This is what the host uses to review the quiz and read explanations aloud.
