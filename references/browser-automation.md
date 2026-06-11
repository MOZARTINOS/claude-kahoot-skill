# Filling Kahoot via browser automation

This documents a browser-automation strategy for the Kahoot creator (`create.kahoot.it`). It was last reviewed on 2026-06-11. Kahoot and browser-tool interfaces change frequently: treat labels and tool names below as examples, inspect the live page, and stop safely if the required capabilities are unavailable.

## Table of contents

1. Tools and golden rules
2. Setup: connect browser, log in, start a blank kahoot
3. The per-question loop (the core)
4. Marking the correct answer
5. Title, save, and finish
6. Known pitfalls and how to handle them

## 1. Tools and golden rules

Use the available browser tools for navigation, semantic page inspection, element lookup, clicking, typing, and optional batching. In Claude-in-Chrome these may appear as tools such as `navigate`, `read_page`, `find`, `computer`, and `browser_batch`; other compatible environments may use different names.

Three rules that matter more than anything else:

- **Operate by element reference, not coordinates.** Get an element's `ref` from `read_page`/`find`, then `computer` `left_click` with that `ref` and `type`. The editor scrolls as you fill it, so fixed pixel coordinates silently land text in the wrong field or add a stray media image.
- **Verify via the accessibility tree, not screenshots.** The editor's renderer often makes `screenshot` time out for 30s. `read_page` and `find` keep working. Use them to confirm state.
- **Batch predictable steps.** `browser_batch` can chain "click title → type → click answer1 → type → … → find correct-answer switches" in a single call, which is dramatically faster than one tool call per field.

## 2. Setup

1. `navigate` to `https://create.kahoot.it/creator`.
2. Inspect the page. If you see a login page, **stop and ask the user to log in** in that browser window. Never enter credentials, one-time codes, recovery codes, or authenticate on their behalf. Resume when they confirm.
3. If a **cookie-consent banner** appears, choose the most privacy-preserving option — `find` and click "Reject all" (decline non-essential cookies) before doing anything else.
4. Confirm with the user that this is the intended account/workspace. Create a new kahoot; do not open or overwrite an existing quiz unless explicitly requested.
5. If a "Create a new kahoot" dialog appears, choose the **blank** option ("Blank" / in other locales "Blankt ark") to get an empty Quiz slide.
6. **Confirm the editor is ready before typing.** The template dialog can take a moment to fully close. After filling the first question, re-read the title and answer fields to verify that the content persisted before adding the second question.

Note: the Kahoot UI renders in the account's language. Labels below are given in English with the Norwegian equivalent in parentheses, because `find`/`read_page` match on these accessibility labels. Prefer matching by **role** (textbox, switch, button) plus a language-agnostic description in your `find` query.

## 3. The per-question loop

The first blank slide commonly already exists. Inspect the live editor before assuming this. Element references can be reassigned after any render, so re-read them as needed; do not rely on a reference remaining stable across the whole session.

Per question:

1. **Add a slide.** Click the sidebar Add button (label such as "Add"/"Legg til"), then locate the Quiz question type in the dialog.
2. **Pick Quiz type.** `browser_batch`: click the Quiz option ref from step 1 → `read_page` (`filter: interactive`) to grab the new slide's field refs.
3. **Fill the slide.** `browser_batch` chaining: click title ref → type question; then for each answer: click answer ref → type option. Field labels: title = "Question title…" ("Spørsmålstittel…"), answers = "Add answer 1..4" ("Legg til svar 1..4"). End the same batch with `find` "answer correct toggle switches" to get the switch refs.
4. **Mark correct** (see section 4): click the switch ref for the correct slot.

Keep going until all approved questions are in. Re-check progress periodically so a stale element or failed batch does not corrupt many slides.

### Why each piece is shaped this way
- Steps are split into batches because a batch stops on first error, and a `ref` found in one batch may go stale before the next batch runs — so do the click that *consumes* a freshly-found ref early in the next batch.
- Typing supports Unicode directly (æ, ø, å, accents, «»), so type the localized text as-is.

## 4. Marking the correct answer

Each answer has a toggle switch with the accessibility label **"Turn on answer N as correct"** ("Slå på svar N som riktig"). After filling the answers, `find` "answer correct toggle switches for answers 1 2 3 4" returns the four switch refs in order. Click the one matching the correct slot (1=first/red, 2=blue, 3=yellow, 4=green). `find` reports which switch is currently active/checked, so you can confirm the mark took.

Marking by switch ref is reliable; marking by clicking the colored circle by coordinate is not, because of scroll drift.

## 5. Title, save, finish

1. Click the kahoot-title button at the top ("Enter kahoot title…"). A settings dialog opens with a title textbox and a description textbox. Fill both, then click "Done" ("Ferdig").
2. Before saving, verify the title, total question count, each question's answer text, and the selected correct answer. Then click **Save** ("Lagre"). A "Your kahoot is ready" ("Kahooten er nå klar") dialog confirms that Kahoot accepted the quiz, but it does not replace content verification.
3. Click "Done" ("Ferdig") to land in the library. The kahoot is now in the user's private library.

Do **not** click "Share"/publish or anything that makes content public without explicit user permission.

## 6. Known pitfalls

- **Screenshots time out.** Expected. Don't retry endlessly — switch to `read_page`/`find`. An occasional screenshot may succeed after a `wait`; use it for a final visual check if you want one, but don't depend on it.
- **The title field sometimes isn't in `read_page`'s interactive list.** When that happens, `find` "question title input field at top" to get its ref.
- **Stray media image from a misclick.** If a coordinate click accidentally adds a media image, remove it via the "Remove media" ("Fjern mediet") button, then refill the slide by refs. This is exactly the failure that operating-by-ref prevents.
- **A freshly found `ref` is "not found" on use.** The dialog re-rendered; just `find` the element again and click the new ref.
- **Character limits.** Question ≈120, answers ≈75. If text is rejected or truncated, shorten it.
- **First slide lost.** If the very first question comes back empty after you typed it, the blank-template dialog was still resolving when you typed. Just re-fill that slide — and going forward, verify the first question persisted before continuing (see Setup step 6).
- **Plan-dependent features.** Question-type availability varies by account type, workspace, region, and subscription. Use the portable 4-option Quiz default and inspect the live editor rather than assuming a fixed free-tier feature set.
- **Tool or UI mismatch.** If semantic inspection, stable element targeting, or required controls are unavailable, stop. Deliver the companion document and report the exact remaining manual steps instead of using blind coordinate automation.
