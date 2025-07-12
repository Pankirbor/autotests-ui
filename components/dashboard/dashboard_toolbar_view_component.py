from playwright.sync_api import Page

from components.base_component import BaseComponent


class DashboardToolbarViewComponent(BaseComponent):
    """
    Компонент верхней панели инструментов главной страницы (Dashboard).

    Атрибуты:
        title: Локатор заголовка страницы.

    Методы:
        check_visible: Проверяет, что заголовок страницы отображается корректно.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.title = page.get_by_test_id("dashboard-toolbar-title-text")

    def check_visible(self):
        """
        Проверяет, что заголовок страницы отображается корректно.
        """
        self.check_locator(self.title, "Dashboard")
