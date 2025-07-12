from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class NavbarComponent(BaseComponent):
    """
    Компонент верхней навигационной панели.

    Атрибуты:
        title: Локатор текста заголовка приложения.
        greeting_text: Локатор текста приветствия пользователя.

    Методы:
        check_visible: Проверяет видимость и корректность отображения заголовка и приветствия.
    """

    def __init__(self, page: Page):
        """
        Инициализирует компонент навигационной панели.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
        """
        super().__init__(page)

        self.title = page.get_by_test_id("navigation-navbar-app-title-text")
        self.greeting_text = page.get_by_test_id("navigation-navbar-welcome-title-text")

    def check_visible(self, username: str):
        """
        Проверяет, что заголовок приложения и приветствие пользователя отображаются корректно.

        Аргументы:
            username (str): Ожидаемое имя пользователя в приветствии.
        """
        self.check_locator(self.title, "UI Course")
        self.check_locator(self.greeting_text, f"Welcome, {username}!")
