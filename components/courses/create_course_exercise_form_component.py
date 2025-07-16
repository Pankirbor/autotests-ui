import allure

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Input, Button, Text


class CreateCourseExerciseFormComponent(BaseComponent):
    """
    Компонент формы создания упражнения в курсе.

    Методы:
        click_delete_exercise_btn: Кликает по кнопке удаления упражнения.
        check_visible: Проверяет видимость элементов упражнения с указанным индексом и текстами.
        fill: Заполняет поля формы упражнения заголовком и описанием.
    """

    def __init__(self, page: Page):
        super().__init__(page)

        self.delete_btn = Button(
            page,
            "create-course-exercise-{index}-box-toolbar-delete-exercise-button",
            "Кнопка удаления упражнения",
        )
        self.subtitle = Text(
            page,
            "create-course-exercise-{index}-box-toolbar-subtitle-text",
            "Подзаголовок упражнения",
        )
        self.title_input = Input(
            page,
            "create-course-exercise-form-title-{index}-input",
            "Заголовок упражнения",
        )
        self.description_input = Input(
            page,
            "create-course-exercise-form-description-{index}-input",
            "Описание упражнения",
        )

    def click_delete_exercise_btn(self, index: int):
        """
        Кликает по кнопке удаления упражнения.

        Аргументы:
            index (int): Индекс упражнения, для которого необходимо нажать на кнопку удаления.
        """
        self.delete_btn.check_visible(index=index).click(index=index)

    @allure.step('Check visible create course exercise form at index "{index}"')
    def check_visible(self, index: int, title: str, description: str):
        """
        Проверяет видимость и корректность отображения элементов упражнения.

        Аргументы:
            index (int): Индекс упражнения.
            title (str): Ожидаемый заголовок упражнения.
            description (str): Ожидаемое описание упражнения.
        """

        self.subtitle.check_visible(index=index).check_have_text(
            f"#{index + 1} Exercise", index=index
        )

        self.title_input.check_visible(index=index).check_have_value(title, index=index)

        self.description_input.check_visible(index=index).check_have_value(
            description, index=index
        )

    @allure.step('Fill create course exercise form at index "{index}"')
    def fill(self, index: int, title: str, description: str):
        """
        Заполняет поля формы упражнения заданными значениями.

        Аргументы:
            index (int): Индекс упражнения.
            title (str): Заголовок упражнения.
            description (str): Описание упражнения.
        """
        (
            self.title_input.clear(index=index)
            .type_text(title, delay=100, index=index)
            .check_have_value(title, index=index)
        )

        (
            self.description_input.clear(index=index)
            .type_text(description, delay=100, index=index)
            .check_have_value(description, index=index)
        )
