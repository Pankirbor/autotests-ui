from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Input


class LoginFormComponent(BaseComponent):
    """
    Компонент формы входа в систему.

    Атрибуты:
        email_input (Input): Поле ввода электронной почты.
        password_input (Input): Поле ввода пароля.

    Методы:
        check_visible: Проверяет видимость и значение полей формы.
        fill: Заполняет поля формы значениями.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента формы входа.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.email_input = Input(page, "login-form-email-input", "Поле Email")
        self.password_input = Input(page, "login-form-password-input", "Поле Password")

    def check_visible(self, email: str = "", password: str = ""):
        """
        Проверяет, что поля формы отображаются и содержат ожидаемые значения.

        Аргументы:
            email (str): Ожидаемое значение электронной почты.
            password (str): Ожидаемое значение пароля.
        """
        self.email_input.check_visible().check_have_value(email)
        self.password_input.check_visible().check_have_value(password)

    def fill(self, email: str, password: str):
        """
        Заполняет поля формы значениями.

        Аргументы:
            email (str): Электронная почта для входа.
            password (str): Пароль для входа.
        """
        (
            self.email_input.check_visible()
            .type_text(email, delay=100)
            .check_have_value(email)
        )

        (
            self.password_input.check_visible()
            .type_text(password, delay=100)
            .check_have_value(password)
        )
