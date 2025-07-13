from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    """
    Компонент формы регистрации пользователя.

    Атрибуты:
        email_input: Локатор поля ввода электронной почты.
        username_input: Локатор поля ввода имени пользователя.
        password_input: Локатор поля ввода пароля.

    Методы:
        check_visible: Проверяет, что поля формы отображаются и содержат ожидаемые значения.
        fill: Заполняет поля формы заданными значениями.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента формы регистрации.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.email_input = Input(page, "registration-form-email-input", "Поле Email")
        self.username_input = Input(
            page, "registration-form-username-input", "Поле Username"
        )
        self.password_input = Input(
            page, "registration-form-password-input", "Поле Password"
        )

    def check_visible(
        self, email: str = "", username: str = "", password: str = ""
    ) -> None:
        """
        Проверяет, что поля формы отображаются и содержат ожидаемые значения.

        Аргументы:
            email (str): Ожидаемое значение поля электронной почты.
            username (str): Ожидаемое значение поля имени пользователя.
            password (str): Ожидаемое значение поля пароля.
        """
        self.email_input.check_visible().check_have_value(email)
        self.username_input.check_visible().check_have_value(username)
        self.password_input.check_visible().check_have_value(password)

    def fill(self, email: str, username: str, password: str) -> None:
        """
        Заполняет поля формы значениями.

        Аргументы:
            email (str): Электронная почта пользователя.
            username (str): Имя пользователя.
            password (str): Пароль пользователя.
        """
        self.check_visible()

        self.email_input.type_text(email).check_have_value(email)
        self.username_input.type_text(username).check_have_value(username)
        self.password_input.type_text(password).check_have_value(password)
