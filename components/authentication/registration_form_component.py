from playwright.sync_api import Page

from components.base_component import BaseComponent


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

        self.email_input = page.get_by_test_id("registration-form-email-input").locator(
            "input"
        )
        self.username_input = page.get_by_test_id(
            "registration-form-username-input"
        ).locator("input")
        self.password_input = page.get_by_test_id(
            "registration-form-password-input"
        ).locator("input")

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
        self.check_input_locator(self.email_input, email)
        self.check_input_locator(self.username_input, username)
        self.check_input_locator(self.password_input, password)

    def fill(self, email: str, username: str, password: str) -> None:
        """
        Заполняет поля формы значениями.

        Аргументы:
            email (str): Электронная почта пользователя.
            username (str): Имя пользователя.
            password (str): Пароль пользователя.
        """
        self.check_visible()
        self.email_input.fill(email)
        self.check_input_locator(self.email_input, email)

        self.username_input.fill(username)
        self.check_input_locator(self.username_input, username)

        self.password_input.fill(password)
        self.check_input_locator(self.password_input, password)
