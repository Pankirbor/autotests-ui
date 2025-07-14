from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements import Image, Text


class CourseViewComponent(BaseComponent):
    """
    Компонент представления курса.

    Этот класс представляет элементы интерфейса, отображающие информацию о конкретном курсе:
    заголовок, изображение, баллы и время прохождения. Также содержит меню управления курсом.

    Атрибуты:
        menu_course (CourseViewMenuComponent): Меню управления курсом.
        title (Text): Заголовок курса.
        image (Image): Изображение курса.
        max_score (Text): Максимальный балл за курс.
        min_score (Text): Минимальный балл для успешного завершения.
        estimated_time (Text): Продолжительность курса.

    Методы:
        check_visible: Проверяет видимость и корректность отображаемых данных.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента представления курса.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.menu_course = CourseViewMenuComponent(page)

        self.title = Text(page, "course-widget-title-text", "Заголовок курса")
        self.image = Image(page, "course-preview-image", "Картинка курса")
        self.max_score = Text(page, "course-max-score-info-row-view-text", "Макс. балл")
        self.min_score = Text(page, "course-min-score-info-row-view-text", "Мин. балл")
        self.estimated_time = Text(
            page,
            "course-estimated-time-info-row-view-text",
            "Продолжительность курса",
        )
        # self.course_menu_btn = page.get_by_test_id("course-view-menu-button")

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
        self.title.check_visible(nth=index).check_have_text(title, nth=index)
        self.menu_course.menu_btn.check_visible(nth=index)
        self.image.check_visible(nth=index)

        self.estimated_time.check_visible(nth=index).check_have_text(
            f"Estimated time: {estimated_time}", nth=index
        )

        self.max_score.check_visible(nth=index).check_have_text(
            f"Max score: {max_score}", nth=index
        )
        self.min_score.check_visible(nth=index).check_have_text(
            f"Min score: {min_score}", nth=index
        )
