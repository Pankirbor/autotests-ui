from typing import Self

from playwright.sync_api import Page, Locator, expect


class BaseElement:
    """
    Базовый класс для элементов пользовательского интерфейса.

    Этот класс предоставляет общие методы для взаимодействия с элементами на веб-странице:
    получение локатора, клик, проверка видимости и текстового содержимого.

    Атрибуты:
        page (Page): Экземпляр страницы браузера.
        locator_path (str): Шаблон пути локатора элемента.
        name (str): Название элемента (используется для идентификации).

    Методы:
        get_locator: Получает локатор элемента.
        click: Выполняет клик по элементу.
        check_visible: Проверяет видимость элемента.
        check_have_text: Проверяет, что элемент содержит ожидаемый текст.
    """

    def __init__(self, page: Page, locator_path: str, name: str) -> None:
        """
        Инициализирует базовый элемент.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
            locator_path (str): Путь к локатору элемента.
            name (str): Название элемента.
        """
        self.page = page
        self.locator_path = locator_path
        self.name = name

    def get_locator(self, **kwargs) -> Locator:
        """
        Возвращает локатор элемента, используя переданные параметры для форматирования пути.

        Возвращает:
            Locator: Локатор элемента на странице.
        """
        return self.page.get_by_test_id(self.locator_path.format(**kwargs))

    def click(self, **kwargs):
        """
        Выполняет клик по элементу.
        """
        self.get_locator(**kwargs).click()

    def check_visible(self, **kwargs) -> Self:
        """
        Проверяет, что элемент отображается на странице.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()
        return self

    def check_have_text(self, text: str, **kwargs):
        """
        Проверяет, что элемент содержит указанный текст.

        Аргументы:
            text (str): Ожидаемый текст в элементе.
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)
