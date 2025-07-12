from playwright.sync_api import Page, expect

from components.courses import (
    CreateCourseExerciseFormComponent,
    CreateCourseExercisesToolbarViewComponent,
    CreateCourseFormComponent,
    CreateCourseToolbarViewComponent,
)
from components.navigation import NavbarComponent, SidebarComponent
from components.views import ImageUploadWidgetComponent, EmptyViewComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    """
    Класс, представляющий страницу создания нового курса.

    Атрибуты:
        navbar (NavbarComponent): Навигационная панель.
        sidebar (SidebarComponent): Боковая панель.
        toolbar (CreateCourseToolbarViewComponent): Верхняя панель инструментов страницы создания курса.
        file_upload_widget (FileUploadWidgetComponent): Виджет загрузки изображения для превью курса.
        course_form (CreateCourseFormComponent): Форма ввода данных курса.
        empty_exercise_view (EmptyViewComponent): Компонент, отображающий сообщение при отсутствии упражнений.
        exercises_toolbar (CreateCourseExercisesToolbarViewComponent): Панель инструментов раздела упражнений.
        exercise_form (CreateCourseExerciseFormComponent): Форма добавления упражнений к курсу.

    Методы:
        check_visible_empty_exercises_list: Проверяет отображение сообщения об отсутствии упражнений.
    """

    def __init__(self, page: Page) -> None:
        """
        Инициализирует объект страницы и все её компоненты.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится класс.
        """
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = CreateCourseToolbarViewComponent(page)
        self.file_upload_widget = ImageUploadWidgetComponent(
            page, identifier="create-course-preview", file_type="image"
        )
        self.course_form = CreateCourseFormComponent(page)
        self.empty_exercise_view = EmptyViewComponent(
            page, identifier="create-course-exercises"
        )
        self.exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.exercise_form = CreateCourseExerciseFormComponent(page)

    def check_visible_empty_exercises_list(self):
        """
        Проверяет, что отображается информационное сообщение о том,
        что список упражнений пуст и как его заполнить.
        """
        self.empty_exercise_view.check_visible(
            title="There is no exercises",
            description='Click on "Create exercise" button to create new exercise',
        )
