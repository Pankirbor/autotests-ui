from playwright.sync_api import Page

from components.base_component import BaseComponent


class ChartViewComponent(BaseComponent):
    """
    Компонент представления диаграммы.

    Атрибуты:
        title (str): Название диаграммы.
        title_locator: Локатор заголовка диаграммы.
        chart: Локатор самой диаграммы.

    Методы:
        check_visible: Проверяет, что заголовок и диаграмма отображаются корректно.
    """

    def __init__(self, page: Page, title: str, identifier_chart: str):
        """
        Инициализирует объект компонента диаграммы.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
            title (str): Название диаграммы.
            identifier_chart (str): Уникальный идентификатор диаграммы для формирования локатора.
        """
        super().__init__(page)

        self.title = title

        self.title_locator = page.get_by_test_id(
            f"{self.title.lower()}-widget-title-text"
        )
        self.chart = page.get_by_test_id(f"{identifier_chart}-chart")

    def check_visible(self) -> None:
        """
        Проверяет видимость заголовка и самой диаграммы.
        """
        self.check_locator(self.title_locator, self.title)
        self.check_locator(self.chart)
