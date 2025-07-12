from playwright.sync_api import Page

from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    """
    Компонент формы входа в систему.

    Атрибуты:
        email_input: Локатор поля ввода электронной почты.
        password_input: Локатор поля ввода пароля.

    Методы:
        check_visible: Проверяет, что поля формы отображаются и содержат ожидаемые значения.
        fill: Заполняет поля формы значениями.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента формы входа.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.email_input = page.get_by_test_id("login-form-email-input").locator(
            "input"
        )
        self.password_input = page.get_by_test_id("login-form-password-input").locator(
            "input"
        )

    def check_visible(self, email: str = "", password: str = ""):
        """
        Проверяет, что поля формы отображаются и содержат ожидаемые значения.

        Аргументы:
            email (str): Ожидаемое значение электронной почты.
            password (str): Ожидаемое значение пароля.
        """
        self.check_input_locator(self.email_input, email)
        self.check_input_locator(self.password_input, password)

    def fill(self, email: str, password: str):
        """
        Заполняет поля формы значениями.

        Аргументы:
            email (str): Электронная почта для входа.
            password (str): Пароль для входа.
        """
        self.check_visible()
        self.email_input.type(email, delay=100)
        self.check_input_locator(self.email_input, email)

        self.password_input.type(password, delay=100)
        self.check_input_locator(self.password_input, password)
