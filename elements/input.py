from typing import Self

from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement


class Input(BaseElement):
    """
    Класс, представляющий поле ввода на веб-странице.

    Этот класс предоставляет методы для взаимодействия с полями ввода:
    заполнение, очистка, проверка значения и ввод текста с задержкой.

    Методы:
        get_locator: Возвращает локатор поля ввода.
        fill: Заполняет поле ввода указанным значением.
        check_have_value: Проверяет, что поле содержит ожидаемое значение.
        clear: Очищает поле ввода.
        type_text: Вводит текст в поле с возможностью задания задержки между нажатиями клавиш.
    """

    def get_locator(self, **kwargs) -> Locator:
        """
        Возвращает локатор элемента ввода (input).

        Возвращает:
            Locator: Локатор поля ввода.
        """
        return super().get_locator(**kwargs).locator("input")

    def fill(self, value: str, **kwargs) -> Self:
        """
        Заполняет поле ввода указанным значением.

        Аргументы:
            value (str): Значение, которое будет введено в поле.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        self.get_locator(**kwargs).fill(value)
        return self

    def check_have_value(self, value: str, **kwargs):
        """
        Проверяет, что поле ввода содержит указанное значение.

        Аргументы:
            value (str): Ожидаемое значение в поле ввода.
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)

    def clear(self, **kwargs) -> Self:
        """
        Очищает поле ввода.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        locator = self.get_locator(**kwargs)
        locator.clear()
        return self

    def type_text(
        self,
        text: str,
        delay: int | None = None,
        timeout: float | None = None,
        no_wait_after: bool | None = None,
        **kwargs,
    ) -> Self:
        """
        Вводит текст в поле ввода с возможностью задания задержки между нажатиями.

        Аргументы:
            text (str): Текст, который будет введен.
            delay (int | None): Задержка между нажатиями в миллисекундах.
            timeout (float | None): Максимальное время ожидания завершения действия.
            no_wait_after (bool | None): Если True, не ждать завершения после ввода.

        Возвращает:
            Self: Экземпляр текущего объекта для цепочки вызовов.
        """
        locator = self.get_locator(**kwargs)
        locator.type(
            text,
            delay=delay,
            timeout=timeout,
            no_wait_after=no_wait_after,
        )
        return self
