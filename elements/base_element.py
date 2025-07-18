from typing import Self

import allure

from playwright.sync_api import Page, Locator, expect
from tools.logger import get_logger


logger = get_logger(__name__.upper())


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

    @property
    def type_of(self):
        return self.__class__.__name__

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Возвращает локатор элемента, используя переданные параметры для форматирования пути.

        Возвращает:
            Locator: Локатор элемента на странице.
        """
        locator = self.locator_path.format(**kwargs)
        step = f"Getting locator with 'data-testid={locator}' at index' {nth}'"

        with allure.step(step):
            try:
                locator = self.page.get_by_test_id(locator).nth(nth)
            except Exception as e:
                logger.error(step)
                logger.error(e)
            return locator

    def click(self, nth: int = 0, **kwargs):
        """
        Выполняет клик по элементу.
        """
        step = f"Clicking {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            self.get_locator(nth, **kwargs).click()

    def check_visible(self, nth: int = 0, **kwargs) -> Self:
        """
        Проверяет, что элемент отображается на странице.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Checking that {self.type_of} '{self.name}' is visible"
        with allure.step(step):
            logger.info(step)
            expect(self.get_locator(nth, **kwargs)).to_be_visible()
        return self

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        """
        Проверяет, что элемент содержит указанный текст.

        Аргументы:
            text (str): Ожидаемый текст в элементе.
        """
        step = f"Checking that {self.type_of} '{self.name}' has text '{text}'"
        with allure.step(step):
            logger.info(step)
            expect(self.get_locator(nth, **kwargs)).to_have_text(text)
