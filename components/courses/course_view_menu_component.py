import allure

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Button


class CourseViewMenuComponent(BaseComponent):
    """
    Компонент меню управления курсом.

    Этот класс представляет меню, которое появляется при нажатии на кнопку "Menu" в интерфейсе просмотра курса.
    Содержит кнопки для редактирования и удаления курса.

    Атрибуты:
        menu_btn (Button): Кнопка для открытия меню.
        edit_menu_item (Button): Кнопка "Edit".
        delete_menu_item (Button): Кнопка "Delete".

    Методы:
        click_edit: Открывает меню и выбирает опцию редактирования.
        click_delete: Открывает меню и выбирает опцию удаления.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента меню просмотра курса.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.menu_btn = Button(page, "course-view-menu-button", "Кнопка Menu курса")
        self.edit_menu_item = Button(page, "course-view-edit-menu-item", "Кнопка Edit")
        self.delete_menu_item = Button(
            page, "course-view-delete-menu-item", "Кнопка Delete"
        )

    @allure.step('Open course menu at index "{index}" and click edit')
    def click_edit(self, index: int):
        """
        Открывает меню и выбирает опцию редактирования для элемента с указанным индексом.

        Аргументы:
            index (int): Индекс элемента в списке.
        """
        self.menu_btn.check_visible(nth=index).click(nth=index)
        self.edit_menu_item.check_visible(nth=index).click(nth=index)

    @allure.step('Open course menu at index "{index}" and click delete')
    def click_delete(self, index: int):
        """
        Открывает меню и выбирает опцию удаления для элемента с указанным индексом.

        Аргументы:
            index (int): Индекс элемента в списке.
        """
        self.menu_btn.check_visible(nth=index).click(nth=index)
        self.delete_menu_item.check_visible(nth=index).click(nth=index)
