from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.email_input = page.get_by_test_id("registration-form-email-input").locator(
            "input"
        )
        self.username_input = page.get_by_test_id(
            "registration-form-username-input"
        ).locator("input")
        self.password_input = page.get_by_test_id(
            "registration-form-password-input"
        ).locator("input")
        self.registration_btn = page.get_by_test_id(
            "registration-page-registration-button"
        )
        self.login_link = page.get_by_test_id("registration-page-login-link")
        self.title_page = page.get_by_test_id("authentication-ui-course-title-text")

    def fill_registration_form(self, email: str, username: str, password: str) -> None:
        expect(self.email_input).to_be_visible()
        self.email_input.fill(email)
        expect(self.username_input).to_be_visible()
        self.username_input.fill(username)
        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)

    def click_registration_btn(self) -> None:
        expect(self.registration_btn).to_be_visible()
        self.registration_btn.click()

    def click_login_link(self) -> None:
        expect(self.login_link).to_be_visible()
        self.login_link.click()

    def check_visible_registration_page_title(self, text_title: str):
        expect(self.title_page).to_be_visible()
        expect(self.title_page).to_have_text(text_title)
