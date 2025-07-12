from playwright.sync_api import Page

from components.base_component import BaseComponent


class EmptyViewComponent(BaseComponent):
    """
    Компонент, представляющий пустой вид (empty view) на странице.

    Атрибуты:
        icon: Локатор иконки компонента.
        title: Локатор заголовка компонента.
        description: Локатор описания компонента.

    Методы:
        check_visible: Проверяет видимость элементов компонента с заданным заголовком и описанием.
    """

    def __init__(self, page: Page, identifier: str):
        """
        Инициализирует объект EmptyViewComponent.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
            identifier (str): Уникальный идентификатор компонента для формирования локаторов.
        """
        super().__init__(page)

        self.icon = page.get_by_test_id(f"{identifier}-empty-view-icon")
        self.title = page.get_by_test_id(f"{identifier}-empty-view-title-text")
        self.description = page.get_by_test_id(
            f"{identifier}-empty-view-description-text"
        )

    def check_visible(self, title: str, description: str):
        """
        Проверяет, что элементы компонента (иконка, заголовок, описание) видимы и содержат правильные тексты.

        Аргументы:
            title (str): Ожидаемый текст заголовка.
            description (str): Ожидаемый текст описания.
        """
        self.check_locator(self.icon)
        self.check_locator(self.title, title)
        self.check_locator(self.description, description)
