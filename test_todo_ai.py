from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from todo_helpers import (
    add_todos,
    clear_completed_todos,
    edit_todo,
    filter_todos,
    get_todo_item,
    open_todo_app,
    toggle_todo,
)


def test_editing_existing_todo_saves_updated_text(page: Page) -> None:
    open_todo_app(page)
    add_todos(page, "Buy groceries")

    expect(page.get_by_test_id("todo-item")).to_have_count(1)

    edit_todo(page, "Buy groceries", "Buy groceries and coffee")

    expect(page.get_by_test_id("todo-item")).to_have_count(1)
    expect(get_todo_item(page, "Buy groceries and coffee")).to_be_visible()
    expect(page.get_by_test_id("todo-item").get_by_text("Buy groceries", exact=True)).to_have_count(0)


def test_clear_completed_removes_only_completed_todos(page: Page) -> None:
    open_todo_app(page)
    add_todos(page, "Submit report", "Plan weekend")

    expect(page.get_by_test_id("todo-item")).to_have_count(2)
    expect(get_todo_item(page, "Submit report")).to_be_visible()
    expect(get_todo_item(page, "Plan weekend")).to_be_visible()
    toggle_todo(page, "Submit report")
    clear_completed_todos(page)

    expect(page.get_by_test_id("todo-item")).to_have_count(1)
    expect(get_todo_item(page, "Plan weekend")).to_be_visible()
    expect(get_todo_item(page, "Plan weekend").get_by_label("Toggle Todo")).not_to_be_checked()
    expect(get_todo_item(page, "Submit report")).to_have_count(0)
    expect(page.get_by_test_id("todo-count")).to_have_text("1 item left")


def test_active_filter_shows_only_uncompleted_todos(page: Page) -> None:
    open_todo_app(page)
    add_todos(page, "Water plants", "Reply to email")

    expect(page.get_by_test_id("todo-item")).to_have_count(2)
    expect(get_todo_item(page, "Water plants")).to_be_visible()
    expect(get_todo_item(page, "Reply to email")).to_be_visible()
    toggle_todo(page, "Water plants")
    filter_todos(page, "Active")

    expect(get_todo_item(page, "Reply to email")).to_be_visible()
    expect(get_todo_item(page, "Water plants")).not_to_be_visible()
    expect(page.get_by_test_id("todo-item").filter(visible=True)).to_have_count(1)
