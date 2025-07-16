import allure

from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    """
    Класс, представляющий кнопку на веб-странице.

    Этот класс наследуется от BaseElement и добавляет специфичные методы для проверки состояния кнопки:
    включено (enabled) или выключено (disabled).

    Методы:
        check_enabled: Проверяет, что кнопка доступна для взаимодействия.
        check_disabled: Проверяет, что кнопка недоступна для взаимодействия.
    """

    def check_enabled(self, nth: int = 0, **kwargs):
        """
        Проверяет, что кнопка включена (доступна для нажатия).

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых кнопок.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        with allure.step(f"Checking that {self.type_of} '{self.name}' is enabled"):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        """
        Проверяет, что кнопка выключена (недоступна для нажатия).

        Аргументы:
            nth (int): Индекс элемента, если на странице несколько одинаковых кнопок.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        with allure.step(f"Checking that {self.type_of} '{self.name}' is disabled"):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()
