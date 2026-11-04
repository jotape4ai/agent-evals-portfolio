from typing import Literal

from playwright.sync_api import Locator, Page, expect


def open_todo_app(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")


def add_todos(page: Page, *names: str) -> None:
    new_todo = page.get_by_role("textbox", name="What needs to be done?")
    for name in names:
        new_todo.fill(name)
        new_todo.press("Enter")


def get_todo_item(page: Page, name: str) -> Locator:
    return page.get_by_test_id("todo-item").filter(has_text=name)


def toggle_todo(page: Page, name: str) -> None:
    get_todo_item(page, name).get_by_label("Toggle Todo").check()


def edit_todo(page: Page, current_name: str, updated_name: str) -> None:
    todo_item = get_todo_item(page, current_name)
    todo_item.get_by_text(current_name, exact=True).dblclick()
    edit_input = todo_item.get_by_role("textbox")
    expect(edit_input).to_be_focused()
    edit_input.fill(updated_name)
    edit_input.press("Enter")


def clear_completed_todos(page: Page) -> None:
    page.get_by_role("button", name="Clear completed").click()


def filter_todos(page: Page, filter_name: Literal["All", "Active", "Completed"]) -> None:
    page.get_by_role("link", name=filter_name).click()
