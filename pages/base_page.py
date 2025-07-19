from typing import Pattern

import allure

from playwright.sync_api import Page, Locator, expect
from tools.logger import get_logger


logger = get_logger(__name__.upper())


class BasePage:
    """
    Базовый класс для всех страниц веб-приложения.

    Этот класс содержит общие методы, такие как переход на страницу,
    перезагрузка страницы и проверки видимости элементов и их содержимого.

    Атрибуты:
        page (Page): Экземпляр страницы браузера.

    Методы:
        visit: Переходит на указанную URL-адрес.
        reload: Перезагружает текущую страницу.
        check_locator: Проверяет видимость элемента и его текстовое содержимое.
        check_input_locator: Проверяет видимость поля ввода и его значение.
    """

    def __init__(self, page: Page) -> None:
        """
        Инициализирует базовый класс страницы.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
        """
        self.page = page

    def visit(self, url: str) -> None:
        """
        Открывает указанную URL-страницу и ждет завершения загрузки.

        Аргументы:
            url (str): Адрес страницы, на которую нужно перейти.
        """
        step = f"Opening the url: '{url}'"
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="networkidle")

    def reload(self) -> None:
        """
        Перезагружает текущую страницу и ждет загрузки контента DOM.
        """
        step = f"Reload page with url: '{self.page.url}'"
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="domcontentloaded")

    # def check_locator(self, locator: Locator, text: str | None = None) -> None:
    #     """
    #     Проверяет видимость элемента и его текстовое содержимое.

    #     Аргументы:
    #         locator (Locator): Локатор элемента.
    #         text (str | None): Ожидаемый текст элемента. Если None — только проверяется видимость.
    #     """
    #     with allure.step(f"Checking that {locator} is visible{f'and have text{text:r}' if text else ""}"):
    #         expect(locator).to_be_visible()
    #         if text:
    #             expect(locator).to_have_text(text)

    # def check_input_locator(self, locator: Locator, text: str | None) -> None:
    #     """
    #     Проверяет видимость поля ввода и его значение.

    #     Аргументы:
    #         locator (Locator): Локатор поля ввода.
    #         text (str | None): Ожидаемое значение в поле ввода. Если None — только проверяется видимость.
    #     """
    #     with allure.step(f"Checking that  input {locator} is visible{f'and have value{text:r}' if text else ""}"):
    #         expect(locator).to_be_visible()
    #         if text:
    #             expect(locator).to_have_value(text)

    def check_current_url(self, expected_url: Pattern[str]) -> None:
        """
        Проверяет, что текущий URL совпадает с ожидаемым.

        Аргументы:
            url (Pattern[str]): Регулярное выражение или строка ожидаемого URL.
        """
        step = f"Checking that current url matches pattern '{expected_url.pattern}'"
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
