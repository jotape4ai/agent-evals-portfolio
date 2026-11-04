# Agent Evals Portfolio

I'm a QA engineer (10+ years, web apps) building evaluations for AI agents.
This repo tracks that work, from E2E automation to agent evals.

## Contents
- `test_todo.py` — Playwright E2E test: Verifying the Completed filter hides active todos, so a broken filter can’t pass silently.
- `test_todo_ai.py` — Playwright E2E tests for editing todos, clearing completed todos, and filtering active todos.
- `todo_helpers.py` — Shared helpers for setting up and interacting with the TodoMVC demo app in the tests.
- `REVIEW.md` — Review of the AI-generated TodoMVC tests, including findings, changes, mutation results, and remaining risks.

## Run it
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install --with-deps
pytest

## Coming next
- Approval-gate evals for a tool-using agent (pass^k reliability)