from playwright.sync_api import Page, expect


def test_editing_existing_todo_saves_updated_text(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    new_todo = page.get_by_role("textbox", name="What needs to be done?")
    new_todo.fill("Buy groceries")
    new_todo.press("Enter")

    todo_item = page.get_by_test_id("todo-item").filter(has_text="Buy groceries")
    todo_item.get_by_text("Buy groceries").dblclick()
    edit_input = todo_item.locator("input.edit")
    expect(edit_input).to_be_focused()
    edit_input.fill("Buy groceries and coffee")
    edit_input.press("Enter")

    expect(page.get_by_test_id("todo-item")).to_have_count(1)
    expect(page.get_by_test_id("todo-item").get_by_text("Buy groceries and coffee")).to_be_visible()
    expect(page.get_by_text("Buy groceries", exact=True)).not_to_be_visible()


def test_clear_completed_removes_only_completed_todos(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    new_todo = page.get_by_role("textbox", name="What needs to be done?")
    new_todo.fill("Submit report")
    new_todo.press("Enter")
    new_todo.fill("Plan weekend")
    new_todo.press("Enter")

    page.get_by_test_id("todo-item").filter(has_text="Submit report").get_by_label("Toggle Todo").check()
    page.get_by_role("button", name="Clear completed").click()

    expect(page.get_by_test_id("todo-item")).to_have_count(1)
    expect(page.get_by_test_id("todo-item").get_by_text("Plan weekend")).to_be_visible()
    expect(page.get_by_text("Submit report", exact=True)).not_to_be_visible()


def test_active_filter_shows_only_uncompleted_todos(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    new_todo = page.get_by_role("textbox", name="What needs to be done?")
    new_todo.fill("Water plants")
    new_todo.press("Enter")
    new_todo.fill("Reply to email")
    new_todo.press("Enter")

    page.get_by_test_id("todo-item").filter(has_text="Water plants").get_by_label("Toggle Todo").check()
    page.get_by_role("link", name="Active").click()

    expect(page.get_by_test_id("todo-item").filter(has_text="Reply to email")).to_be_visible()
    expect(page.get_by_test_id("todo-item").filter(has_text="Water plants")).not_to_be_visible()
    expect(page.get_by_test_id("todo-item").filter(visible=True)).to_have_count(1)