import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements import Button, Text


class CreateCourseToolbarViewComponent(BaseComponent):
    """
    Компонент верхней панели управления при создании курса.

    Этот класс представляет элементы интерфейса, связанные с процессом создания нового курса,
    такие как заголовок и кнопка "Создать курс".

    Атрибуты:
        title (Text): Заголовок панели "Create course".
        create_course_btn (Button): Кнопка для завершения создания курса.

    Методы:
        check_visible: Проверяет видимость заголовка и состояние кнопки.
        click_create_course_btn: Выполняет клик по кнопке "Создать курс" и проверяет переход на страницу курсов.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.title = Text(
            page, "create-course-toolbar-title-text", "Заголовок панели Create course"
        )
        self.create_course_btn = Button(
            page,
            "create-course-toolbar-create-course-button",
            "Кнопка создать курс",
        )

    def check_visible(self):
        """
        Проверяет, что заголовок отображается корректно и кнопка "Создать курс" отключена.
        """
        self.title.check_visible().check_have_text("Create course")
        self.create_course_btn.check_disabled()

    def click_create_course_btn(self):
        """
        Кликает по кнопке "Создать курс" и проверяет переход на страницу курсов.
        """
        self.create_course_btn.check_visible().click()
        self.check_current_url(re.compile(r".*/#/courses"))
