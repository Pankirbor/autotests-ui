import re

from playwright.sync_api import Page

from components.base_component import BaseComponent


class CoursesListToolbarViewComponent(BaseComponent):
    """
    Компонент верхней панели инструментов списка курсов.

    Атрибуты:
        title: Локатор заголовка панели.
        create_course_btn: Локатор кнопки создания нового курса.

    Методы:
        check_visible: Проверяет видимость элементов панели.
        click_create_course_btn: Кликает по кнопке создания курса и проверяет переход на соответствующую страницу.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.title = page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_course_btn = page.get_by_test_id(
            "courses-list-toolbar-create-course-button"
        )

    def check_visible(self):
        """
        Проверяет, что заголовок и кнопка создания курса отображаются корректно.
        """
        self.check_locator(self.title, "Courses")
        self.check_locator(self.create_course_btn)

    def click_create_course_btn(self):
        """
        Выполняет клик по кнопке создания курса и проверяет URL текущей страницы.
        """
        self.create_course_btn.click()
        self.check_current_url(re.compile(r".*/#/courses/create"))
