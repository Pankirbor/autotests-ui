from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def visit(self, url: str) -> None:
        self.page.goto(url, wait_until="networkidle")

    def reload(self) -> None:
        self.page.reload(wait_until="domcontentloaded")

    def check_locator(self, locator: Locator, text: str | None) -> None:
        expect(locator).to_be_visible()
        if text:
            expect(locator).to_have_text(text)

    def check_input_locator(self, locator: Locator, text: str | None) -> None:
        expect(locator).to_be_visible()
        if text:
            expect(locator).to_have_value(text)
