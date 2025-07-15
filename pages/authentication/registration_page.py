import re

from playwright.sync_api import Page

from components.authentication import RegistrationFormComponent
from elements import Button, Link, Text
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """
    Класс, представляющий страницу регистрации пользователя.

    Атрибуты:
        form (RegistrationFormComponent): Форма регистрации.
        registration_btn (Button): Кнопка "Registration".
        login_link (Link): Ссылка на страницу входа.
        title_page (Text): Заголовок страницы.

    Методы:
        click_registration_btn: Выполняет клик по кнопке "Registration" и проверяет переход на Dashboard.
        click_login_link: Выполняет клик по ссылке "Login" и проверяет переход на страницу входа.
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
        self.registration_btn = Button(
            page, "registration-page-registration-button", "Кнопка Registration"
        )
        self.login_link = Link(page, "registration-page-login-link", "Ссылка Login")
        self.title_page = Text(
            page, "authentication-ui-course-title-text", "Заголовок страницы"
        )

    def click_registration_btn(self) -> None:
        """
        Кликает по кнопке "Registration" и проверяет, что пользователь перешел на Dashboard.
        """
        self.registration_btn.check_visible().click()
        self.check_current_url(re.compile(r".*/#/dashboard"))

    def click_login_link(self) -> None:
        """
        Кликает по ссылке "Login" и проверяет, что пользователь перешел на страницу входа.
        """
        self.login_link.check_visible().click()
        self.check_current_url(re.compile(r".*/#/auth/login"))

    def check_visible_page_title(self):
        """
        Проверяет, что заголовок страницы отображается корректно.
        """
        self.title_page.check_visible().check_have_text("UI Course")
