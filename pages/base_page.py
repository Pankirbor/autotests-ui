from typing import Pattern

from playwright.sync_api import Page, Locator, expect


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
        self.page.goto(url, wait_until="networkidle")

    def reload(self) -> None:
        """
        Перезагружает текущую страницу и ждет загрузки контента DOM.
        """
        self.page.reload(wait_until="domcontentloaded")

    def check_locator(self, locator: Locator, text: str | None = None) -> None:
        """
        Проверяет видимость элемента и его текстовое содержимое.

        Аргументы:
            locator (Locator): Локатор элемента.
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
            text (str | None): Ожидаемое значение в поле ввода. Если None — только проверяется видимость.
        """
        expect(locator).to_be_visible()
        if text:
            expect(locator).to_have_value(text)

    def check_current_url(self, expected_url: Pattern[str]) -> None:
        """
        Проверяет, что текущий URL совпадает с ожидаемым.

        Аргументы:
            url (Pattern[str]): Регулярное выражение или строка ожидаемого URL.
        """
        expect(self.page).to_have_url(expected_url)
