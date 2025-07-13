from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Icon, Text


class EmptyViewComponent(BaseComponent):
    """
    Компонент отображения сообщения об отсутствии данных.

    Этот класс используется для проверки элементов, которые отображаются, когда данные не найдены,
    например, при пустом списке курсов или результатов. Включает иконку, заголовок и описание.

    Атрибуты:
        icon (Icon): Иконка, отображающая состояние "пусто".
        title (Text): Заголовок сообщения.
        description (Text): Описание сообщения.

    Методы:
        check_visible: Проверяет видимость всех частей компонента и корректность текста.
    """

    def __init__(self, page: Page, identifier: str):
        """
        Инициализирует объект EmptyViewComponent.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
            identifier (str): Уникальный идентификатор компонента для формирования локаторов.
        """
        super().__init__(page)

        self.icon = Icon(page, f"{identifier}-empty-view-icon", "Иконка EmptyView")
        self.title = Text(
            page, f"{identifier}-empty-view-title-text", "Заголовок EmptyView"
        )
        self.description = Text(
            page, f"{identifier}-empty-view-description-text", "Описание EmptyView"
        )

    def check_visible(self, title: str, description: str):
        """
        Проверяет, что элементы компонента (иконка, заголовок, описание) видимы и содержат правильные тексты.

        Аргументы:
            title (str): Ожидаемый текст заголовка.
            description (str): Ожидаемый текст описания.
        """
        self.icon.check_visible()
        self.title.check_visible().check_have_text(title)
        self.description.check_visible().check_have_text(description)
