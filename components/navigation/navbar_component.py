import allure

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements import Text


class NavbarComponent(BaseComponent):
    """
    Компонент навигационной панели (Navbar).

    Этот класс представляет элементы верхней панели приложения, такие как заголовок и приветственное сообщение.

    Атрибуты:
        title (Text): Заголовок приложения в Navbar.
        greeting_text (Text): Приветственное сообщение для пользователя.

    Методы:
        check_visible: Проверяет видимость и текстовое содержимое элементов Navbar.
    """

    def __init__(self, page: Page):
        """
        Инициализирует компонент навигационной панели.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
        """
        super().__init__(page)

        self.title = Text(page, "navigation-navbar-app-title-text", "Заголовок Navbar")
        self.greeting_text = Text(
            page, "navigation-navbar-welcome-title-text", "Приветственный текст Navbar"
        )

    @allure.step("Check visible Navbar")
    def check_visible(self, username: str):
        """
        Проверяет, что заголовок приложения и приветствие пользователя отображаются корректно.

        Аргументы:
            username (str): Ожидаемое имя пользователя в приветствии.
        """
        self.title.check_visible().check_have_text("UI Course")
        self.greeting_text.check_visible().check_have_text(f"Welcome, {username}!")
