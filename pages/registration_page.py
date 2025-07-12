import re

from playwright.sync_api import Page, expect

from components.authentication import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """
    Класс, представляющий страницу регистрации пользователя.

    Атрибуты:
        form (RegistrationFormComponent): Форма регистрации.
        registration_btn: Локатор кнопки "Registration".
        login_link: Локатор ссылки для перехода на страницу входа.
        title_page: Локатор заголовка страницы.

    Методы:
        click_registration_btn: Кликает по кнопке "Registration" и проверяет переход на Dashboard.
        click_login_link: Кликает по ссылке для перехода на страницу входа.
        check_visible_page_title: Проверяет отображение заголовка страницы.
    """

    def __init__(self, page: Page) -> None:
        """
        Инициализирует объект RegistrationPage и связанные с ним элементы.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
        """
        super().__init__(page)

        self.form = RegistrationFormComponent(page)
        self.registration_btn = page.get_by_test_id(
            "registration-page-registration-button"
        )
        self.login_link = page.get_by_test_id("registration-page-login-link")
        self.title_page = page.get_by_test_id("authentication-ui-course-title-text")

    def click_registration_btn(self) -> None:
        """
        Кликает по кнопке "Registration" и проверяет, что пользователь перешел на Dashboard.
        """
        self.check_locator(self.registration_btn)
        self.registration_btn.click()
        expect(self.page).to_have_url(re.compile(r".*/#/dashboard"))

    def click_login_link(self) -> None:
        """
        Кликает по ссылке "Login" и проверяет, что пользователь перешел на страницу входа.
        """
        self.check_locator(self.login_link)
        self.login_link.click()
        expect(self.page).to_have_url(re.compile(r".*/#/auth/login"))

    def check_visible_page_title(self):
        """
        Проверяет, что заголовок страницы отображается корректно.
        """
        self.check_locator(self.title_page, "UI Course")
