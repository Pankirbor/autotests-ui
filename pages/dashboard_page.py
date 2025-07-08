from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.dashboard_page_title = page.get_by_test_id("dashboard-toolbar-title-text")

    def check_visible_dashboard_page_title(self, text_title: str) -> None:
        expect(self.dashboard_page_title).to_be_visible()
        expect(self.dashboard_page_title).to_have_text(text_title)
