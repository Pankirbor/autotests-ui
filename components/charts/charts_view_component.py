import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Image, Text


class ChartViewComponent(BaseComponent):
    """
    Компонент отображения диаграммы.

    Этот класс представляет элементы интерфейса, связанные с визуализацией данных на диаграмме:
    заголовок и изображение самой диаграммы. Используется для проверки видимости и корректности отображения.

    Атрибуты:
        title (str): Название диаграммы.
        title_locator (Text): Локатор текста заголовка диаграммы.
        chart (Image): Локатор изображения диаграммы.

    Методы:
        check_visible: Проверяет, что заголовок и изображение диаграммы отображаются корректно.
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

        self.title_locator = Text(
            page,
            f"{self.title.lower()}-widget-title-text",
            "Название диаграммы",
        )
        self.chart = Image(page, f"{identifier_chart}-chart", "Диаграмма")

    def check_visible(self) -> None:
        """
        Проверяет видимость заголовка и самой диаграммы.
        """
        with allure.step(f"Checking that chart '{self.title}' is visible"):
            self.title_locator.check_visible().check_have_text(self.title)
            self.chart.check_visible()
