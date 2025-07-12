from playwright.sync_api import Page

from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    """
    Компонент меню просмотра курса.

    Атрибуты:
        menu_btn: Локатор кнопки меню.
        edit_menu_item: Локатор пункта меню "Edit".
        delete_menu_item: Локатор пункта меню "Delete".

    Методы:
        click_edit: Кликает по кнопке меню и выбирает пункт "Edit".
        click_delete: Кликает по кнопке меню и выбирает пункт "Delete".
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента меню просмотра курса.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.menu_btn = page.get_by_test_id("course-view-menu-button")
        self.edit_menu_item = page.get_by_test_id("course-view-edit-menu-item")
        self.delete_menu_item = page.get_by_test_id("course-view-delete-menu-item")

    def click_edit(self, index: int):
        """
        Открывает меню и выбирает опцию редактирования для элемента с указанным индексом.

        Аргументы:
            index (int): Индекс элемента в списке.
        """
        self.menu_btn.nth(index).click()

        self.check_locator(self.edit_menu_item)
        self.edit_menu_item.nth(index).click()

    def click_delete(self, index: int):
        """
        Открывает меню и выбирает опцию удаления для элемента с указанным индексом.

        Аргументы:
            index (int): Индекс элемента в списке.
        """
        self.menu_btn.nth(index).click()

        self.check_locator(self.delete_menu_item)
        self.delete_menu_item.nth(index).click()
