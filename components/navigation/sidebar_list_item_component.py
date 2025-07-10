from playwright.sync_api import expect, Page

from components.base_component import BaseComponent


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, indentifier: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f"{indentifier}-drawer-list-item-icon")
        self.title = page.get_by_test_id(f"{indentifier}-drawer-list-item-title-text")
        self.button = page.get_by_test_id(f"{indentifier}-drawer-list-item-button")

    def check_visible(self, title: str) -> None:
        self.check_locator(self.icon)
        self.check_locator(self.title, title)
        self.check_locator(self.button)

    def navigate(self, expected_url: str) -> None:
        self.button.click()
        self.check_current_url(expected_url)
