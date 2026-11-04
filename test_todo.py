from playwright.sync_api import Page, expect

from todo_helpers import add_todos, filter_todos, get_todo_item, open_todo_app, toggle_todo


def test_completed_filter_shows_only_completed_todos(page: Page) -> None:
    open_todo_app(page)
    add_todos(page, "take a walk", "read chapter 2 of Superintelligence book")

    toggle_todo(page, "take a walk")
    expect(page.get_by_test_id("todo-item")).to_have_count(2)
    filter_todos(page, "Completed")

    expect(get_todo_item(page, "take a walk")).to_be_visible()
    expect(get_todo_item(page, "read chapter 2 of Superintelligence book")).not_to_be_visible()
    expect(page.get_by_test_id("todo-item")).to_have_count(1)
