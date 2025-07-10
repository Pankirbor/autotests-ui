from typing import Pattern

from playwright.sync_api import expect, Locator, Page


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, url_path: Pattern[str]) -> None:
        expect(self.page).to_have_url(url_path)

    def check_locator(self, locator: Locator, text: str | None) -> None:
        expect(locator).to_be_visible()
        if text:
            expect(locator).to_have_text(text)

    def check_input_locator(self, locator: Locator, text: str | None) -> None:
        expect(locator).to_be_visible()
        if text:
            expect(locator).to_have_value(text)
