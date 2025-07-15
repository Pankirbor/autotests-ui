import re
from playwright.sync_api import Page

from components.authentication import LoginFormComponent
from elements import Button, Link, Text
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Класс, представляющий страницу входа в систему.

    Атрибуты:
        form (LoginFormComponent): Форма для ввода данных пользователя.
        login_btn (Button): Кнопка "Login".
        registration_link (Link): Ссылка на страницу регистрации.
        title_page (Text): Заголовок страницы.
        wrong_email_or_password_alert (Text): Сообщение об ошибке при неверной почте или пароле.

    Методы:
        click_login_btn: Выполняет клик по кнопке "Login".
        click_registration_link: Выполняет клик по ссылке "Registration".
        check_visible_login_page_title: Проверяет отображение заголовка страницы.
        check_visible_wrong_email_or_password_alert: Проверяет отображение сообщения об ошибке.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект LoginPage и связанные с ним элементы.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
        """
        super().__init__(page)

        self.form = LoginFormComponent(page)

        self.login_btn = Button(page, "login-page-login-button", "Кнопка Login")
        self.registration_link = Link(
            page, "login-page-registration-link", "Ссылка на страницу регистрации"
        )
        self.title_page = Text(
            page, "authentication-ui-course-title-text", "Заголовок страницы входа"
        )
        self.wrong_email_or_password_alert = Text(
            page,
            "login-page-wrong-email-or-password-alert",
            "Сообщение об ошибке при неверном пароле или почте",
        )

    def click_login_btn(self):
        """
        Кликает по кнопке "Login" после проверки её видимости.
        """
        self.login_btn.check_visible().click()
        self.check_current_url(re.compile(r".*/#/dashboard"))

    def click_registration_link(self):
        """
        Кликает по ссылке "Registration" после проверки её видимости.
        """
        self.registration_link.check_visible().click()
        self.check_current_url(re.compile(r".*/#/auth/registration"))

    def check_visible_login_page_title(self):
        """
        Проверяет, что заголовок страницы отображается корректно.
        """
        self.title_page.check_visible().check_have_text("UI Course")

    def check_visible_wrong_email_or_password_alert(self):
        """
        Проверяет, что отображается уведомление о неверной электронной почте или пароле.
        """
        self.wrong_email_or_password_alert.check_visible().check_have_text(
            "Wrong email or password"
        )
