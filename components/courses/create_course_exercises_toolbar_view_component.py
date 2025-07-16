import allure

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Button, Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    """
    Компонент верхней панели управления упражнениями при создании курса.

    Этот класс представляет элементы интерфейса, связанные с добавлением упражнений в процессе создания курса,
    такие как заголовок и кнопка для создания нового упражнения.

    Атрибуты:
        title (Text): Заголовок панели "Exercises".
        create_exercise_btn (Button): Кнопка для создания нового упражнения.

    Методы:
        check_visible: Проверяет видимость заголовка и кнопки.
        click_create_exercise_btn: Выполняет клик по кнопке создания упражнения.
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.title = Text(
            page,
            "create-course-exercises-box-toolbar-title-text",
            "Заголовок панели Exercises",
        )
        self.create_exercise_btn = Button(
            page,
            "create-course-exercises-box-toolbar-create-exercise-button",
            "Кнопка создания упражнения",
        )

    @allure.step("Check visible Exercise Toolbar")
    def check_visible(self):
        """
        Проверяет, что заголовок и кнопка создания упражнения отображаются корректно.
        """
        self.title.check_visible().check_have_text("Exercises")
        self.create_exercise_btn.check_visible()

    def click_create_exercise_btn(self):
        """
        Выполняет клик по кнопке создания упражнения.
        """
        self.create_exercise_btn.check_visible().click()
