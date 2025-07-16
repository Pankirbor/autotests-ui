from typing import Pattern

import allure
from playwright.sync_api import expect, Locator, Page


class BaseComponent:
    """
    Базовый класс для всех компонентов пользовательского интерфейса.

    Этот класс предоставляет общие методы для проверки видимости элементов,
    их текстового содержимого, значения ввода и текущего URL страницы.

    Атрибуты:
        page (Page): Экземпляр страницы браузера.

    Методы:
        check_current_url: Проверяет, что текущий URL соответствует ожидаемому.
        check_locator: Проверяет видимость локатора и его текстовое содержимое.
        check_input_locator: Проверяет видимость поля ввода и его значение.
    """

    def __init__(self, page: Page):
        """
        Инициализирует базовый компонент.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
        """
        self.page = page

    def check_current_url(self, url: Pattern[str]):
        """
        Проверяет, что текущий URL совпадает с ожидаемым.

        Аргументы:
            url (Pattern[str]): Регулярное выражение или строка ожидаемого URL.
        """
        with allure.step(f"Checking that current url matches pattern '{url.pattern}'"):
            expect(self.page).to_have_url(url)

    def check_locator(self, locator: Locator, text: str | None = None):
        """
        Проверяет видимость элемента и его текстовое содержимое.

        Аргументы:
            locator (Locator): Локатор элемента на странице.
            text (str | None): Ожидаемый текст элемента. Если None — только проверяется видимость.
        """
        expect(locator).to_be_visible()
        if text:
            expect(locator).to_have_text(text)

    def check_input_locator(self, locator: Locator, text: str | None) -> None:
        """
        Проверяет видимость поля ввода и его значение.

        Аргументы:
            locator (Locator): Локатор поля ввода.
            value (str): Ожидаемое значение в поле ввода.
        """
        expect(locator).to_be_visible()
        if text:
            expect(locator).to_have_value(text)
