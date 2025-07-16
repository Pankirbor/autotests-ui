import allure

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Input, Textarea


class CreateCourseFormComponent(BaseComponent):
    """
    Компонент формы создания курса.

    Этот класс представляет элементы интерфейса, связанные с заполнением данных при создании нового курса.
    Содержит поля для ввода заголовка, времени прохождения, описания, максимального и минимального баллов.

    Атрибуты:
        title_input (Input): Поле ввода заголовка курса.
        time_input (Input): Поле ввода времени прохождения курса.
        description_input (Textarea): Поле ввода описания курса.
        max_score_input (Input): Поле ввода максимального балла.
        min_score_input (Input): Поле ввода минимального балла.

    Методы:
        check_visible: Проверяет видимость полей и их значения.
        fill: Заполняет поля данными.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента формы создания курса.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.title_input = Input(
            page, "create-course-form-title-input", "Поле ввода заголовка"
        )
        self.time_input = Input(
            page,
            "create-course-form-estimated-time-input",
            "Поле ввода оценочного времени",
        )
        self.description_input = Textarea(
            page, "create-course-form-description-input", "Поле ввода описания"
        )
        self.max_score_input = Input(
            page, "create-course-form-max-score-input", "Поле ввода макс. балла"
        )
        self.min_score_input = Input(
            page, "create-course-form-min-score-input", "Поле ввода мин. балла"
        )

    @allure.step("Check visible course form")
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
        self.title_input.check_visible().check_have_value(title)
        self.description_input.check_visible().check_have_value(description)
        self.time_input.check_visible().check_have_value(estimated_time)
        self.max_score_input.check_visible().check_have_value(max_score)
        self.min_score_input.check_visible().check_have_value(min_score)

    @allure.step("Fill course form")
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
        (
            self.title_input.check_visible()
            .clear()
            .type_text(title, delay=100)
            .check_have_value(title)
        )

        (
            self.description_input.check_visible()
            .clear()
            .type_text(description, delay=100)
            .check_have_value(description)
        )

        (
            self.time_input.check_visible()
            .clear()
            .type_text(estimated_time, delay=100)
            .check_have_value(estimated_time)
        )

        (
            self.max_score_input.check_visible()
            .clear()
            .type_text(max_score, delay=100)
            .check_have_value(max_score)
        )

        (
            self.min_score_input.check_visible()
            .clear()
            .type_text(min_score, delay=100)
            .check_have_value(min_score)
        )
