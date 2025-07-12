from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent


class CourseViewComponent(BaseComponent):
    """
    Компонент представления курса на странице.

    Атрибуты:
        menu_course (CourseViewMenuComponent): Меню управления курсом.
        title: Локатор заголовка курса.
        image: Локатор изображения курса.
        max_score: Локатор максимального балла.
        min_score: Локатор минимального балла.
        estimated_time: Локатор оценочного времени.

    Методы:
        check_visible: Проверяет видимость и корректность отображения элементов курса.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента представления курса.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.menu_course = CourseViewMenuComponent(page)

        self.title = page.get_by_test_id("course-widget-title-text")
        self.image = page.get_by_test_id("course-preview-image")
        self.max_score = page.get_by_test_id("course-max-score-info-row-view-text")
        self.min_score = page.get_by_test_id("course-min-score-info-row-view-text")
        self.estimated_time = page.get_by_test_id(
            "course-estimated-time-info-row-view-text"
        )
        self.course_menu_btn = page.get_by_test_id("course-view-menu-button")

    def check_visible(
        self,
        index: int,
        title: str,
        max_score: str,
        min_score: str,
        estimated_time: str,
    ):
        """
        Проверяет видимость элементов курса и их соответствие ожидаемым значениям.

        Аргументы:
            index (int): Индекс курса в списке.
            title (str): Ожидаемое название курса.
            max_score (str): Ожидаемый максимальный балл.
            min_score (str): Ожидаемый минимальный балл.
            estimated_time (str): Ожидаемое время прохождения курса.
        """
        self.check_locator(self.title.nth(index), title)
        self.check_locator(self.course_menu_btn.nth(index))
        self.check_locator(self.image.nth(index))
        self.check_locator(
            self.estimated_time.nth(index),
            f"Estimated time: {estimated_time}",
        )
        self.check_locator(self.max_score.nth(index), f"Max score: {max_score}")
        self.check_locator(self.min_score.nth(index), f"Min score: {min_score}")
