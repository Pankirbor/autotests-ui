from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        " https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator(
        "input"
    )
    password_input = page.get_by_test_id("registration-form-password-input").locator(
        "input"
    )
    registration_btn = page.get_by_test_id("registration-page-registration-button")

    felds_to_fill = (email_input, username_input, password_input)
    values = ("user.name@gmail.com", "username", "password")
    for field, value in zip(felds_to_fill, values):
        field.fill(value)

    registration_btn.click()
    title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(title).to_have_text("Dashboard")

    page.wait_for_timeout(5000)
