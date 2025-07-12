import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    """
    Компонент верхней панели инструментов страницы создания курса.

    Атрибуты:
        title: Локатор заголовка панели.
        create_course_btn: Локатор кнопки "Создать курс".

    Методы:
        check_visible: Проверяет видимость элементов и состояние кнопки.
        click_create_course_btn: Кликает по кнопке "Создать курс" и проверяет переход на страницу курсов.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.title = page.get_by_test_id("create-course-toolbar-title-text")
        self.create_course_btn = page.get_by_test_id(
            "create-course-toolbar-create-course-button"
        )

    def check_visible(self):
        """
        Проверяет, что заголовок отображается корректно и кнопка "Создать курс" отключена.
        """
        self.check_locator(self.title, "Create course")
        expect(self.create_course_btn).to_be_disabled()

    def click_create_course_btn(self):
        """
        Кликает по кнопке "Создать курс" и проверяет переход на страницу курсов.
        """
        self.check_locator(self.create_course_btn)
        self.create_course_btn.click()
        self.check_current_url(re.compile(r".*/#/courses"))
