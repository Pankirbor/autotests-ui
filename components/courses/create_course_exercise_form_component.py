from playwright.sync_api import Page

from components.base_component import BaseComponent


class CreateCourseExerciseFormComponent(BaseComponent):
    """
    Компонент формы создания упражнения в курсе.

    Методы:
        click_delete_exercise_btn: Кликает по кнопке удаления упражнения.
        check_visible: Проверяет видимость элементов упражнения с указанным индексом и текстами.
        fill: Заполняет поля формы упражнения заголовком и описанием.
    """

    def click_delete_exercise_btn(self, index: int):
        """
        Кликает по кнопке удаления упражнения.

        Аргументы:
            index (int): Индекс упражнения, для которого необходимо нажать на кнопку удаления.
        """
        delete_btn = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_btn.click()

    def check_visible(self, index: int, title: str, description: str):
        """
        Проверяет видимость и корректность отображения элементов упражнения.

        Аргументы:
            index (int): Индекс упражнения.
            title (str): Ожидаемый заголовок упражнения.
            description (str): Ожидаемое описание упражнения.
        """
        exercise_subtitle = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-subtitle-text"
        )
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        ).locator("input")

        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        ).locator("input")
        self.check_locator(exercise_subtitle, f"#{index + 1} Exercise")
        self.check_input_locator(exercise_title_input, title)
        self.check_input_locator(exercise_description_input, description)

    def fill(self, index: int, title: str, description: str):
        """
        Заполняет поля формы упражнения заданными значениями.

        Аргументы:
            index (int): Индекс упражнения.
            title (str): Заголовок упражнения.
            description (str): Описание упражнения.
        """
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        ).locator("input")
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        ).locator("input")

        exercise_title_input.fill(title)
        self.check_input_locator(exercise_title_input, title)

        exercise_description_input.fill(description)
        self.check_input_locator(exercise_description_input, description)
