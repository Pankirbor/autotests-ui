from playwright.sync_api import Page

from components.base_component import BaseComponent


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    """
    Компонент верхней панели инструментов раздела упражнений при создании курса.

    Атрибуты:
        title: Локатор заголовка панели.
        create_exercise_btn: Локатор кнопки "Создать упражнение".

    Методы:
        check_visible: Проверяет видимость заголовка и кнопки создания упражнения.
        click_create_exercise_btn: Кликает по кнопке "Создать упражнение".
    """

    def __init__(self, page: Page):
        """
        Инициализирует объект компонента.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
        """
        super().__init__(page)

        self.title = page.get_by_test_id(
            "create-course-exercises-box-toolbar-title-text"
        )
        self.create_exercise_btn = page.get_by_test_id(
            "create-course-exercises-box-toolbar-create-exercise-button"
        )

    def check_visible(self):
        """
        Проверяет, что заголовок и кнопка создания упражнения отображаются корректно.
        """
        self.check_locator(self.title, "Exercises")
        self.check_locator(self.create_exercise_btn)

    def click_create_exercise_btn(self):
        """
        Выполняет клик по кнопке создания упражнения.
        """
        self.check_locator(self.create_exercise_btn)
        self.create_exercise_btn.click()
