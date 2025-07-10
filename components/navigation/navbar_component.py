from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar_title = page.get_by_test_id("navigation-navbar-app-title-text")
        self.greeting_text = page.get_by_test_id("navigation-navbar-welcome-title-text")

    def check_visible(self, username: str):
        self.check_locator(self.navbar_title, "UI Course")
        self.check_locator(self.greeting_text, f"Welcome, {username}!")
