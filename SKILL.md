---
name: kahoot-quiz-creator
description: Design high-quality Kahoot quizzes and, when the user explicitly asks for it, enter them into the Kahoot web editor with browser automation. Use when the user asks to create Kahoot content, classroom or training trivia, an interactive multiple-choice quiz, or to put existing questions into Kahoot. Default to producing a reviewable quiz document; only modify the user's Kahoot account after explicit confirmation.
---

# Kahoot Quiz Creator

Create a Kahoot quiz in two independently useful phases: first design and review the content, then optionally enter it into the Kahoot web editor.

Do not assume that a request for quiz content authorizes browser automation. Phase 1 is the default deliverable. Run Phase 2 only when the user explicitly requests import into Kahoot and confirms the final content.

## Phase 1 — Design the content (do this first, away from the browser)

The browser editor is slow to fill, so every question should be final before you start typing it in. Rushing into the editor with half-formed questions means painful re-editing.

1. **Clarify scope.** Confirm or reasonably infer the topic, audience age/level, number of questions, language, tone, and whether tie-breakers are wanted. Ask only for details that materially affect the result.
2. **Write the questions.** Follow `references/content-design.md` for the question mix, difficulty balance, the 4-option format, correct-answer marking, and read-aloud explanations. Localize references to the audience (e.g., use songs/traditions the players actually know).
3. **Verify factual claims.** Check dates, statistics, quotations, current events, and other unstable facts against reliable sources. Flag ambiguity instead of inventing certainty. For educational quizzes, prefer primary or authoritative sources and record source links in a short notes section when verification matters.
4. **Save a companion document.** Write the full quiz — questions, options, marked answers, and a one-line explanation per question — to a Markdown file the user keeps. Kahoot's standard quiz editor has no dedicated explanation field, so the host can read these aloud. Put any tie-breaker questions and verification notes here too. Use `references/example-quiz.md` as the format reference when useful.
5. **Request review.** Present the completed document and ask the user to confirm it before opening or changing Kahoot. If the user only requested content, stop here.

Only move to Phase 2 after the user has explicitly requested account changes and approved the quiz content.

## Phase 2 — Enter it into Kahoot (browser automation)

Read `references/browser-automation.md` before starting. It documents a robust interaction strategy and known failure modes. Browser tool names and Kahoot labels can change, so inspect the available tools and live page rather than assuming the examples are exact.

- **The user must log in themselves.** Never enter the user's password or authenticate for them. Navigate to the Kahoot creator, and if a login screen appears, ask the user to sign in (Google/Microsoft/Apple/email) in that browser window, then continue once they confirm.
- **Require explicit authorization.** Before creating or editing anything, confirm which Kahoot account/workspace and quiz should be changed. Do not overwrite an existing quiz unless the user explicitly asks.
- **Drive the editor by element role/label, not pixel coordinates.** Fill the question title and answer fields by clicking their element references and typing; mark the correct answer using the "mark answer N as correct" switch found by its accessibility label. Coordinates drift as the page scrolls and will silently put text in the wrong place.
- **Verify semantically.** Prefer accessibility-tree or DOM inspection over screenshots when the browser tools support it. After entry, verify the question count, text, answer choices, correct-answer state, and title. A successful save alone is not proof that every field is correct.
- **Respect current limits.** Standard Quiz questions currently allow up to 120 characters and answers up to 75 characters. Re-check the live editor if it rejects content or if another question/import type is used.
- **Don't publish or share without explicit permission.** Saving to the user's private library is fine; clicking "Share"/publish, or anything public, requires the user's go-ahead.
- **Stop safely on incompatibility.** If the required browser tools are unavailable or the editor no longer matches this workflow, preserve the companion document and explain what remains instead of improvising risky account actions.

## Definition of done

For content-only requests, the reviewed companion document is delivered with answers, explanations, and any verification notes.

For import requests, the document is delivered and the quiz is saved in the explicitly selected Kahoot account with its title, question count, answer choices, and correct-answer selections verified. Publishing, sharing, assigning, or starting a live game remains unperformed unless separately authorized.
