# Review: AI-generated TodoMVC tests

## Summary

AI produced 3 working tests with sound assertions. Main issues: duplicated setup,
a CSS selector, and gaps in "what was kept" checks. All fixed; mutations confirm
each test catches its target bug.

## Findings in the AI output

- Duplicated setup in all 3 tests → shared navigation, todo creation, lookup,
  toggle, edit, clear, and filter helpers now live in `todo_helpers.py`.
- `locator("input.edit")` CSS selector → replaced with a role-based textbox
  locator inside the todo item.
- The clear-completed test did not fully check what was kept → it now verifies
  the remaining todo is unchecked and the counter says `1 item left`.

## Changes I made

- Full diff vs. the original AI output: https://github.com/jotape4ai/agent-evals-portfolio/commit/f3db066
- Extracted `todo_helpers.py` with `open_todo_app`, `add_todos`,
  `get_todo_item`, `toggle_todo`, `edit_todo`, `clear_completed_todos`, and
  `filter_todos`.
- Updated the three AI-generated tests to use the shared helpers and
  role-/test-id-based locators.
- Strengthened setup and outcomes with item counts and visibility checks.
- Added checks that the cleared todo is absent, the surviving todo is active,
  and the remaining-item counter is correct.

## Mutation results (current code)

| Test | Mutation (behavior change) | Caught by | Output |
|---|---|---|---|
| Edit | Press `Escape` instead of `Enter` to cancel the edit | Visibility check for "Buy groceries and coffee" | Fails: edited todo is not found |
| Clear completed | Comment out Clear Completed action | `to_have_count(1)` | Fails: expected to count 1, but counts 2 |
| Active filter | Remove the toggle so "Water plants" remains active | `not_to_be_visible` check for "Water plants" | Fails: expected not visible, but the todo is visible |

## Remaining risks

- All tests depend on the external demo site; a slow or unavailable site can
  cause failures unrelated to the tests.
- I ran the tests individually and in different orders; all pass.
