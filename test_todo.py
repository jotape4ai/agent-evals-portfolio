from playwright.sync_api import Page, expect



def test_completed_filter_shows_only_completed_todos(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    new_todo = page.get_by_role("textbox", name="What needs to be done?")
    new_todo.fill("take a walk")
    new_todo.press("Enter")
    new_todo.fill("read chapter 2 of Superintelligence book")
    new_todo.press("Enter")

    page.get_by_role("listitem").filter(has_text="take a walk").get_by_label("Toggle Todo").check()
    expect(page.get_by_test_id("todo-item")).to_have_count(2)
    page.get_by_role("link", name="Completed").click()

    # your assertions here
    expect(page.get_by_role("listitem").filter(has_text="take a walk")).to_be_visible()
    expect(page.get_by_role("listitem").filter(has_text="read chapter 2 of Superintelligence book")).not_to_be_visible()
    expect(page.get_by_test_id("todo-item")).to_have_count(1)
