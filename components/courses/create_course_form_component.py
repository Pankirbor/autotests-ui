from playwright.sync_api import Page

from components.base_component import BaseComponent


class CreateCourseFormComponent(BaseComponent):
    """
    Компонент формы создания курса.

    Атрибуты:
        title_input: Локатор поля ввода заголовка курса.
        time_input: Локатор поля ввода оценочного времени.
        description_input: Локатор поля ввода описания курса.
        max_score_input: Локатор поля ввода максимального балла.
        min_score_input: Локатор поля ввода минимального балла.

    Методы:
        check_visible: Проверяет, что поля формы отображаются и содержат ожидаемые значения.
        fill: Заполняет поля формы значениями.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента формы создания курса.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.title_input = page.get_by_test_id(
            "create-course-form-title-input"
        ).locator("input")
        self.time_input = page.get_by_test_id(
            "create-course-form-estimated-time-input"
        ).locator("input")
        self.description_input = (
            page.get_by_test_id("create-course-form-description-input")
            .locator("textarea")
            .first
        )
        self.max_score_input = page.get_by_test_id(
            "create-course-form-max-score-input"
        ).locator("input")
        self.min_score_input = page.get_by_test_id(
            "create-course-form-min-score-input"
        ).locator("input")

    def check_visible(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str,
    ):
        """
        Проверяет, что поля формы отображаются и содержат ожидаемые значения.

        Аргументы:
            title (str): Ожидаемое значение заголовка.
            estimated_time (str): Ожидаемое значение времени.
            description (str): Ожидаемое значение описания.
            max_score (str): Ожидаемое значение максимального балла.
            min_score (str): Ожидаемое значение минимального балла.
        """
        self.check_input_locator(self.title_input, title)
        self.check_input_locator(self.description_input, description)
        self.check_input_locator(self.time_input, estimated_time)
        self.check_input_locator(self.max_score_input, max_score)
        self.check_input_locator(self.min_score_input, min_score)

    def fill(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str,
    ):
        """
        Заполняет поля формы значениями.

        Аргументы:
            title (str): Заголовок курса.
            estimated_time (str): Оценочное время прохождения.
            description (str): Описание курса.
            max_score (str): Максимальный балл.
            min_score (str): Минимальный балл.
        """
        self.title_input.type(title, delay=100)
        self.check_input_locator(self.title_input, title)

        self.description_input.type(description, delay=100)
        self.check_input_locator(self.description_input, description)

        self.time_input.type(estimated_time, delay=100)
        self.check_input_locator(self.time_input, estimated_time)

        self.max_score_input.type(max_score, delay=100)
        self.check_input_locator(self.max_score_input, max_score)

        self.min_score_input.type(min_score, delay=100)
        self.check_input_locator(self.min_score_input, min_score)
