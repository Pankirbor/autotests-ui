from playwright.sync_api import expect, Page

from components.base_component import BaseComponent


class SidebarListItemComponent(BaseComponent):
    """
    Компонент элемента списка в боковой панели навигации.

    Атрибуты:
        icon: Локатор иконки элемента.
        title: Локатор текста заголовка элемента.
        button: Локатор кнопки, с помощью которой происходит переход.

    Методы:
        check_visible: Проверяет видимость иконки, заголовка и кнопки.
        navigate: Кликает по кнопке и проверяет переход на ожидаемый URL.
    """

    def __init__(self, page: Page, identifier: str):
        """
        Инициализирует компонент элемента боковой панели.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
            identifier (str): Уникальный идентификатор элемента для формирования локаторов.
        """
        super().__init__(page)

        self.icon = page.get_by_test_id(f"{identifier}-drawer-list-item-icon")
        self.title = page.get_by_test_id(f"{identifier}-drawer-list-item-title-text")
        self.button = page.get_by_test_id(f"{identifier}-drawer-list-item-button")

    def check_visible(self, title: str):
        """
        Проверяет, что иконка, заголовок и кнопка элемента отображаются корректно.

        Аргументы:
            title (str): Ожидаемое значение текста заголовка.
        """
        self.check_locator(self.icon)
        self.check_locator(self.title, title)
        self.check_locator(self.button)

    def navigate(self, expected_url: str):
        """
        Кликает по кнопке элемента и проверяет, что текущий URL соответствует ожидаемому.

        Аргументы:
            expected_url (str): Регулярное выражение или строка ожидаемого URL.
        """
        self.button.click()
        self.check_current_url(expected_url)
