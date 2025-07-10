from typing import Pattern

from playwright.sync_api import Page, expect


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, url_path: Pattern[str]) -> None:
        expect(self.page).to_have_url(url_path)
