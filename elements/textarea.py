from typing import Self

import allure

from playwright.sync_api import expect, Locator


from elements.base_element import BaseElement
from tools.logger import get_logger


logger = get_logger(__name__.upper())


class Textarea(BaseElement):
    """
    Класс, представляющий текстовую область (textarea) на веб-странице.

    Этот класс расширяет BaseElement и предоставляет методы для взаимодействия с текстовыми областями:
    заполнение текстом, проверка значения, ввод текста с параметрами.

    Методы:
        get_locator: Получает локатор текстовой области.
        fill: Заполняет текстовую область указанным значением.
        check_have_value: Проверяет, что значение в текстовой области соответствует ожидаемому.
        type_text: Вводит текст в текстовую область с возможностью задания параметров.
    """

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Возвращает локатор текстовой области (textarea).

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых текстовых областей.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Возвращает:
            Locator: Локатор текстовой области.
        """
        try:
            locator = super().get_locator(nth, **kwargs).locator("textarea").first
        except Exception as e:
            logger.error(e)
        return locator

    def fill(self, value: str, nth: int = 0, **kwargs) -> Self:
        """
        Заполняет текстовую область указанным текстом.

        Аргументы:
            value (str): Текст, который будет введен.
            nth (int): Индекс элемента, если на странице несколько одинаковых текстовых областей.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        step = f"Fill {self.type_of} '{self.name}' to value '{value}'"
        with allure.step(step):
            logger.info(step)
            self.get_locator(nth, **kwargs).fill(value)
            return self

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        """
        Проверяет, что текстовая область содержит указанное значение.

        Аргументы:
            value (str): Ожидаемое значение в текстовой области.
            nth (int): Индекс элемента, если на странице несколько одинаковых текстовых областей.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        step = f"Checking that {self.type_of} '{self.name}' has a value '{value}'"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)

    def type_text(
        self,
        text: str,
        nth: int = 0,
        delay: int | None = None,
        timeout: float | None = None,
        no_wait_after: bool | None = None,
        **kwargs,
    ) -> Self:
        """
        Вводит текст в поле ввода с возможностью задания параметров.

        Аргументы:
            text (str): Текст, который будет введен.
            nth (int): Индекс элемента, если на странице несколько одинаковых полей.
            delay (int | None): Задержка между нажатиями клавиш в миллисекундах.
            timeout (float | None): Максимальное время ожидания завершения действия.
            no_wait_after (bool | None): Если True, не ждать завершения после ввода.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Fill {self.type_of} '{self.name}' to value {text} with delayed typing"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.type(
                text,
                delay=delay,
                timeout=timeout,
                no_wait_after=no_wait_after,
            )
            return self

    def clear(self, nth: int = 0, **kwargs) -> Self:
        """
        Очищает поле ввода.

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых полей.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        step = f"Clearing a {self.type_of} '{self.name}' of values"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.clear()
            return self
