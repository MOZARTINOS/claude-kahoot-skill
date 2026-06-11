---
name: kahoot-quiz-creator
description: Design a Kahoot quiz and enter it directly into the Kahoot web editor via browser automation. Use this whenever the user wants to create a Kahoot, build a quiz/trivia game, prepare a classroom or training quiz, make an interactive multiple-choice game, or "put my questions into Kahoot" — even if they don't say the word "Kahoot" explicitly but describe an interactive multiple-choice quiz game with points and a leaderboard. Covers both writing high-quality questions AND filling them into create.kahoot.it through the Claude-in-Chrome browser tools.
---

# Kahoot Quiz Creator

This skill helps you create a Kahoot quiz end to end: first design strong question content, then type that content directly into the Kahoot web editor using browser automation.

Work in two distinct phases. Don't blur them — getting the content right before touching the browser is what makes the automation go smoothly.

## Phase 1 — Design the content (do this first, away from the browser)

The browser editor is slow to fill, so every question should be final before you start typing it in. Rushing into the editor with half-formed questions means painful re-editing.

1. **Clarify scope.** Before writing, confirm the essentials with the user: topic, audience age/level, number of questions, language, tone (serious vs. playful), and whether they want tie-breaker questions. Underspecified quizzes waste effort — a "quiz about animals" for 7-year-olds is a very different artifact than one for a university class.
2. **Write the questions.** Follow `references/content-design.md` for the question mix, difficulty balance, the 4-option format, correct-answer marking, and read-aloud explanations. Localize references to the audience (e.g., use songs/traditions the players actually know).
3. **Save a companion document.** Kahoot has **no field for explanations**, so write the full quiz — questions, options, marked answers, and a one-line explanation per question — to a Markdown file the user keeps. The teacher/host reads the explanations aloud; they live in the doc, not in Kahoot. Put any tie-breaker questions here too.

Only once the content is locked do you move to Phase 2.

## Phase 2 — Enter it into Kahoot (browser automation)

Read `references/browser-automation.md` before you start — it documents the exact editor mechanics (element labels, the per-question loop, pitfalls) that make this reliable. Key points up front:

- **The user must log in themselves.** Never enter the user's password or authenticate for them. Navigate to the Kahoot creator, and if a login screen appears, ask the user to sign in (Google/Microsoft/Apple/email) in that browser window, then continue once they confirm.
- **Drive the editor by element role/label, not pixel coordinates.** Fill the question title and answer fields by clicking their element references and typing; mark the correct answer using the "mark answer N as correct" switch found by its accessibility label. Coordinates drift as the page scrolls and will silently put text in the wrong place.
- **Verify with `read_page`/`find`, not screenshots.** The Kahoot editor's renderer frequently makes `screenshot` time out. The accessibility tree is the reliable source of truth, and Kahoot won't let you save unless every question has a correct answer marked — so a successful save is itself a strong correctness check.
- **Respect character limits:** question text ≈ 120 characters, each answer ≈ 75 characters. Trim before typing.
- **Don't publish or share without explicit permission.** Saving to the user's private library is fine; clicking "Share"/publish, or anything public, requires the user's go-ahead.

## Definition of done

The quiz is saved in the user's Kahoot library with every question entered and a correct answer marked on each, the companion explanation document is delivered to the user, and you've offered (not performed) next steps like previewing or changing the cover image.
