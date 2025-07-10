import pytest

from playwright.sync_api import expect

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    """
    Тестирует отображение страницы курсов при пустом списке курсов.

    Проверяет, что после регистрации пользователя и перехода на страницу курсов,
    отображается уведомление о том, что список курсов пустой. Проверяются текстовые
    элементы и видимость соответствующих элементов интерфейса.

    Шаги:
    1. Открывает браузер и переходит на страницу регистрации.
    2. Заполняет форму регистрации (email, имя пользователя, пароль).
    3. Выполняет регистрацию.
    4. Сохраняет состояние браузера в файл `browser-state.json`.
    5. Открывает браузер с сохранённым состоянием и переходит на страницу курсов.
    6. Проверяет наличие и текст следующих элементов:
        - Заголовок страницы "Courses".
        - Иконка отсутствия результатов.
        - Заголовок сообщения об отсутствии результатов.
        - Описание сообщения об отсутствии результатов.

    Использует: sync_playwright, методы playwright для работы с DOM и проверки условий.
    """

    page = chromium_page_with_state

    page.goto(
        " https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses",
        wait_until="networkidle",
    )
    title_courses_page = page.get_by_test_id("courses-list-toolbar-title-text")
    icon_no_results = page.get_by_test_id("courses-list-empty-view-icon")
    title_no_results = page.get_by_test_id("courses-list-empty-view-title-text")
    description_no_results = page.get_by_test_id(
        "courses-list-empty-view-description-text"
    )
    h1 = "Courses"
    h2 = "There is no results"
    icon = ""
    text = "Results from the load test pipeline will be displayed here"
    items = zip(
        (h1, icon, h2, text),
        (
            title_courses_page,
            icon_no_results,
            title_no_results,
            description_no_results,
        ),
    )
    for expexted_val, item_page in items:
        if expexted_val:
            expect(item_page).to_have_text(expexted_val)

        expect(item_page).to_be_visible()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(
    create_course_page: CreateCoursePage, courses_list_page: CoursesListPage
):
    # ? Переход на страницу создания курса и проверка наличия всех элементов страницы
    courses_list_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )
    courses_list_page.check_visable_create_course_btn()
    courses_list_page.click_create_course_btn()
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_btn()
    create_course_page.check_visable_image_view_empty_view()
    create_course_page.check_visable_image_upload_view()
    create_course_page.check_visable_create_course_form(
        title="", estimated_time="", description="", max_score="0", min_score="0"
    )
    create_course_page.check_visable_exercises_title()
    create_course_page.check_visable_exercise_create_btn()
    create_course_page.check_visable_empty_exercises_list()
    create_course_page.click_exercise_create_btn()
    create_course_page.check_visible_create_exercise_form(
        index=0, title="Exercise title", description="Exercise description"
    )

    # ? Заполнение формы и проверка наличия элементов после заполнения
    create_course_page.upload_preview_image("./testdata/files/image.jpg")
    create_course_page.check_visable_preview_image()
    create_course_page.check_visable_image_upload_view(is_image_uploaded=True)
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10",
    )
    create_course_page.fill_create_exercise_form(
        index=0, title="Playwright", description="Playwright"
    )
    create_course_page.click_delete_exercise_btn(index=0)
    create_course_page.check_visable_empty_exercises_list()
    create_course_page.click_create_course_btn()

    # ? Проверка наличия элементов после создания курса
    courses_list_page.check_visable_courses_page_title()
    courses_list_page.check_visable_create_course_btn()
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10",
    )
