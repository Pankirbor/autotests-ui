from playwright.sync_api import Page

from components.navigation import NavbarComponent, SidebarComponent
from components.courses import CoursesListToolbarViewComponent, CourseViewComponent
from components.views import EmptyViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    """
    Класс, представляющий страницу списка курсов.

    Атрибуты:
        navbar (NavbarComponent): Навигационная панель.
        sidebar (SidebarComponent): Боковая панель.
        toolbar (CoursesListToolbarViewComponent): Панель инструментов списка курсов.
        empty_view (EmptyViewComponent): Компонент отображения сообщения при отсутствии курсов.
        course_card (CourseViewComponent): Компонент отображения информации о курсе.

    Методы:
        check_visible_empty_view: Проверяет отображение сообщения о том, что список курсов пуст.
    """

    def __init__(self, page: Page) -> None:
        """
        Инициализирует объект CoursesListPage и связанные с ним компоненты.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
        """
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = CoursesListToolbarViewComponent(page)
        self.empty_view = EmptyViewComponent(page, identifier="courses-list")
        self.course_card = CourseViewComponent(page)

    def check_visible_empty_view(self):
        """
        Проверяет, что отображается информационное сообщение о том, что список курсов пуст.
        """
        self.empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here",
        )
