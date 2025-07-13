from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Text


class DashboardToolbarViewComponent(BaseComponent):
    """
    Компонент верхней панели инструментов главной страницы (Dashboard).

    Атрибуты:
        title (Text): Текст заголовка элемента.

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

        self.title = Text(
            page, "dashboard-toolbar-title-text", "Заголовок Dashboard Toolbar"
        )

    def check_visible(self):
        """
        Проверяет, что заголовок страницы отображается корректно.
        """
        self.title.check_visible().check_have_text("Dashboard")
