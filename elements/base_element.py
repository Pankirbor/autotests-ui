from typing import Self

import allure

from playwright.sync_api import Page, Locator, expect
from ui_coverage_tool import ActionType, SelectorType

from elements.ui_coverage import tracker
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
    def type_of(self) -> str:
        """
        Возвращает тип элемента в нижнем регистре.
        """
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

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        """
        Возвращает строковый путь локатора элемента.
        Если в локаторе есть переменные, они заменяются на значения из kwargs.

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых элементов.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Возвращает:
            str: Строковый путь локатора.
        """
        data_testid = self.locator_path.format(**kwargs)
        return f"//*[@data-testid='{data_testid}'][{nth + 1}]"

    def track_coverage(self, action_type: ActionType, nth: int = 0, **kwargs) -> None:
        """
        Отправляет информацию о выполнении действия в трекер.

        Аргументы:
            action_type (ActionType): Тип действия (клик, ввод, проверка).
            nth (int): Индекс элемента.
            **kwargs: Дополнительные аргументы для форматирования локатора.
        """
        tracker.track_coverage(
            selector=self.get_raw_locator(nth=nth, **kwargs),
            action_type=action_type,
            selector_type=SelectorType.XPATH,
        )

    def click(self, nth: int = 0, **kwargs) -> None:
        """
        Выполняет клик по элементу.

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых элементов.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        step = f"Clicking {self.type_of} '{self.name}'"
        with allure.step(step):
            logger.info(step)
            self.get_locator(nth, **kwargs).click()

        self.track_coverage(ActionType.CLICK, nth, **kwargs)

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

        self.track_coverage(ActionType.VISIBLE, nth, **kwargs)
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

        self.track_coverage(ActionType.TEXT, nth, **kwargs)
