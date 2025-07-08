from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id("login-form-email-input").locator(
            "input"
        )
        self.password_input = page.get_by_test_id("login-form-password-input").locator(
            "input"
        )
        self.login_btn = page.get_by_test_id("login-page-login-button")
        self.registration_link = page.get_by_test_id("login-page-registration-link")
        self.title_page = page.get_by_test_id("authentication-ui-course-title-text")
        self.wrong_email_or_password_alert = page.get_by_test_id(
            "login-page-wrong-email-or-password-alert"
        )

    def fill_login_form(self, email: str, password: str):
        expect(self.email_input).to_be_visible()
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_btn(self):
        expect(self.login_btn).to_be_visible()
        self.login_btn.click()

    def click_registration_link(self):
        expect(self.registration_link).to_be_visible()
        self.registration_link.click()

    def check_visible_login_page_title(self, text_title: str):
        expect(self.title_page).to_be_visible()
        expect(self.title_page).to_have_text(text_title)

    def check_visible_wrong_email_or_password_alert(self, text_alert: str):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text(text_alert)
