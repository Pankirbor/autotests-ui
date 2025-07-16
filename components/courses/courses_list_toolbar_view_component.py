import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Button, Text


class CoursesListToolbarViewComponent(BaseComponent):
    """
    Компонент верхней панели управления списком курсов.

    Этот класс представляет элементы интерфейса, расположенные в верхней части страницы списка курсов,
    такие как заголовок и кнопка создания нового курса.

    Атрибуты:
        title (Text): Заголовок панели "Courses".
        create_course_btn (Button): Кнопка для создания нового курса.

    Методы:
        check_visible: Проверяет видимость заголовка и кнопки.
        click_create_course_btn: Выполняет клик по кнопке создания курса и проверяет URL.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.title = Text(
            page, "courses-list-toolbar-title-text", "Заголовок панели Courses"
        )
        self.create_course_btn = Button(
            page, "courses-list-toolbar-create-course-button", "Кнопка создания курса"
        )

    @allure.step("Check visible course list Toolbar")
    def check_visible(self):
        """
        Проверяет, что заголовок и кнопка создания курса отображаются корректно.
        """
        self.title.check_visible().check_have_text("Courses")
        self.create_course_btn.check_visible()

    def click_create_course_btn(self):
        """
        Выполняет клик по кнопке создания курса и проверяет URL текущей страницы.
        """
        self.create_course_btn.check_visible().click()
        self.check_current_url(re.compile(r".*/#/courses/create"))
