from typing import Generator
import pytest

from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope="session")
def initialize_browser_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration",
            wait_until="networkidle",
        )

        registration_btn = page.get_by_test_id("registration-page-registration-button")

        fields = ("email", "username", "password")
        values = ("user.name@gmail.com", "username", "password")
        for field, value in zip(fields, values):
            page.get_by_test_id(f"registration-form-{field}-input").locator(
                "input"
            ).type(
                value,
                delay=200,
            )

        registration_btn.click()

        context.storage_state(path="browser-state.json")


@pytest.fixture
def chromium_page_with_state(initialize_browser_state) -> Generator[Page, None, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        yield page
