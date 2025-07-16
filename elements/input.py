from typing import Self

import allure

from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement


class Input(BaseElement):
    """
    Класс, представляющий поле ввода на веб-странице.

    Этот класс расширяет BaseElement и предоставляет методы для взаимодействия с полями ввода:
    заполнение, очистка, проверка значения и ввод текста с задержкой.

    Методы:
        get_locator: Получает локатор элемента ввода.
        fill: Заполняет поле указанным значением.
        check_have_value: Проверяет, что значение в поле соответствует ожидаемому.
        clear: Очищает поле ввода.
        type_text: Вводит текст в поле с возможностью задания параметров.
    """

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Возвращает локатор элемента ввода (input).

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых полей.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Возвращает:
            Locator: Локатор поля ввода.
        """
        return super().get_locator(nth, **kwargs).locator("input")

    def fill(self, value: str, nth: int = 0, **kwargs) -> Self:
        """
        Заполняет поле ввода указанным значением.

        Аргументы:
            value (str): Значение, которое будет введено.
            nth (int): Индекс элемента, если на странице несколько одинаковых полей.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        with allure.step(f"Fill {self.type_of} '{self.name}' to value '{value}'"):
            self.get_locator(nth, **kwargs).fill(value)
            return self

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        """
        Проверяет, что поле ввода содержит указанное значение.

        Аргументы:
            value (str): Ожидаемое значение в поле ввода.
            nth (int): Индекс элемента, если на странице несколько одинаковых полей.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        with allure.step(
            f"Checking that {self.type_of} '{self.name}' has a value '{value}'"
        ):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)

    def clear(self, nth: int = 0, **kwargs) -> Self:
        """
        Очищает поле ввода.

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых полей.
            **kwargs: Дополнительные параметры для форматирования локатора.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        with allure.step(f"Clearing a {self.type_of} '{self.name}' of values"):
            locator = self.get_locator(nth, **kwargs)
            locator.clear()
            return self

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
        with allure.step(
            f"Fill {self.type_of} '{self.name}' to value {text} with delayed typing"
        ):
            locator = self.get_locator(nth, **kwargs)
            locator.type(
                text,
                delay=delay,
                timeout=timeout,
                no_wait_after=no_wait_after,
            )
            return self
