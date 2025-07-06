from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        " https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration",
        wait_until="networkidle",
    )
    registration_button = page.get_by_test_id("registration-page-registration-button")

    expect(registration_button).to_be_disabled()

    fields = ("email", "username", "password")
    values = ("user.name@gmail.com", "username", "password")

    for field, value in zip(fields, values):
        page.get_by_test_id(f"registration-form-{field}-input").locator("input").fill(
            value
        )

    expect(registration_button).not_to_be_disabled()

    page.wait_for_timeout(3000)
