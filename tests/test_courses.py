from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
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
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration",
            wait_until="networkidle",
        )

        registration_btn = page.get_by_test_id("registration-page-registration-button")

        fields = ("email", "username", "password")
        values = ("user.name@gmail.com", "username", "password")
        for field, value in zip(fields, values):
            page.get_by_test_id(f"registration-form-{field}-input").locator(
                "input"
            ).type(
                value,
                delay=200,
            )

        registration_btn.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

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
