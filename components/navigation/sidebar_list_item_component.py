from playwright.sync_api import expect, Page

from components.base_component import BaseComponent
from elements import Button, Icon, Text


class SidebarListItemComponent(BaseComponent):
    """
    Компонент элемента списка в боковой панели (Sidebar).

    Этот класс представляет отдельный элемент боковой панели, включая иконку, заголовок и кнопку,
    с помощью которых можно перейти на соответствующую страницу.

    Атрибуты:
        icon (Icon): Иконка элемента.
        title (Text): Текст заголовка элемента.
        button (Button): Кнопка для перехода.

    Методы:
        check_visible: Проверяет видимость всех частей элемента и текст заголовка.
        navigate: Выполняет клик по кнопке и проверяет URL текущей страницы.
    """

    def __init__(self, page: Page, identifier: str):
        """
        Инициализирует компонент элемента боковой панели.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
            identifier (str): Уникальный идентификатор элемента для формирования локаторов.
        """
        super().__init__(page)

        self.icon = Icon(
            page, f"{identifier}-drawer-list-item-icon", "Иконка SidebarItem"
        )
        self.title = Text(
            page, f"{identifier}-drawer-list-item-title-text", "Заголовок SidebarItem"
        )
        self.button = Button(
            page, f"{identifier}-drawer-list-item-button", "Кнопка SidebarItem"
        )

    def check_visible(self, title: str):
        """
        Проверяет, что иконка, заголовок и кнопка элемента отображаются корректно.

        Аргументы:
            title (str): Ожидаемое значение текста заголовка.
        """
        self.icon.check_visible()
        self.button.check_visible()
        self.title.check_visible().check_have_text(title)

    def navigate(self, expected_url: str):
        """
        Кликает по кнопке элемента и проверяет, что текущий URL соответствует ожидаемому.

        Аргументы:
            expected_url (str): Регулярное выражение или строка ожидаемого URL.
        """
        self.button.check_visible().click()
        self.check_current_url(expected_url)
