import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    """
    Тест проверяет отображение страницы курсов при пустом списке курсов.

    Описание:
        Проверяет, что при открытии страницы курсов после регистрации нового пользователя
        отображается сообщение о том, что список курсов пустой. Проверяются элементы:
        - Навигационная панель.
        - Боковая панель.
        - Верхняя панель инструментов.
        - Сообщение о пустом списке курсов (иконка, заголовок, описание).

    Шаги:
        1. Переход на страницу курсов.
        2. Проверка видимости и корректности навигационной панели.
        3. Проверка видимости боковой панели.
        4. Проверка видимости верхней панели инструментов.
        5. Проверка отображения сообщения об отсутствии курсов.

    Ожидаемый результат:
        Все элементы страницы отображаются корректно, а пользователь видит информирующее сообщение
        о том, что список курсов пуст.
    """
    courses_list_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )
    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()
    courses_list_page.toolbar.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(
    create_course_page: CreateCoursePage, courses_list_page: CoursesListPage
):
    """
    Тест проверяет процесс создания нового курса в UI-приложении.

    Тестовые шаги:
    1. Переход на страницу списка курсов и проверка видимости кнопки создания курса.
    2. Открытие страницы создания курса и проверка отображения всех элементов формы.
    3. Загрузка изображения и заполнение формы данных курса.
    4. Проверка создания и удаления упражнения.
    5.Сохранение курса.
    6. Проверка отображения созданного курса в списке.

    Используемые страницы:
        - courses_list_page: Страница со списком курсов.
        - create_course_page: Страница с формой создания курса.

    Шаги теста:
    1. Открытие страницы курсов и проверка элементов интерфейса.
    2. Создание и заполнение формы курса.
    3. Проверка результатов после сохранения.
    """
    # ? Переход на страницу создания курса и проверка наличия всех элементов страницы
    courses_list_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )
    courses_list_page.toolbar.check_visible()
    courses_list_page.toolbar.click_create_course_btn()

    create_course_page.navbar.check_visible("username")
    create_course_page.sidebar.check_visible()
    create_course_page.toolbar.check_visible()
    create_course_page.file_upload_widget.check_visible()
    create_course_page.course_form.check_visible(
        title="", estimated_time="", description="", max_score="0", min_score="0"
    )
    create_course_page.exercises_toolbar.check_visible()
    create_course_page.check_visible_empty_exercises_list()
    create_course_page.exercises_toolbar.click_create_exercise_btn()
    create_course_page.exercise_form.check_visible(
        index=0, title="Exercise title", description="Exercise description"
    )

    # ? Заполнение формы и проверка наличия элементов после заполнения
    create_course_page.file_upload_widget.upload_file("./testdata/files/image.jpg")
    create_course_page.file_upload_widget.check_visible(is_file_uploaded=True)
    create_course_page.course_form.fill(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10",
    )
    create_course_page.exercise_form.fill(
        index=0, title="Playwright", description="Playwright"
    )
    create_course_page.exercise_form.click_delete_exercise_btn(index=0)
    create_course_page.check_visible_empty_exercises_list()
    create_course_page.toolbar.click_create_course_btn()

    # ? Проверка наличия элементов после создания курса
    courses_list_page.toolbar.check_visible()
    courses_list_page.course_card.check_visible(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10",
    )
