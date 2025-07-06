from playwright.sync_api import sync_playwright, expect


def test_successful_registration():
    """
    Тестирует успешную регистрацию пользователя на сайте.

    Шаги:
    1. Запускает браузер и переходит на страницу регистрации.
    2. Находит поля ввода для email, имя пользователя и пароль.
    3. Заполняет поля тестовыми данными.
    4. Нажимает на кнопку регистрации.
    5. Проверяет, что после успешной регистрации пользователь перенаправляется
       на страницу Dashboard и заголовок страницы равен "Dashboard".

    Использует: sync_playwright, методы playwright для работы с DOM и проверки условий.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(
            " https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )

        email_input = page.get_by_test_id("registration-form-email-input").locator(
            "input"
        )
        username_input = page.get_by_test_id(
            "registration-form-username-input"
        ).locator("input")
        password_input = page.get_by_test_id(
            "registration-form-password-input"
        ).locator("input")
        registration_btn = page.get_by_test_id("registration-page-registration-button")

        felds_to_fill = (email_input, username_input, password_input)
        values = ("user.name@gmail.com", "username", "password")
        for field, value in zip(felds_to_fill, values):
            field.fill(value)

        registration_btn.click()
        title = page.get_by_test_id("dashboard-toolbar-title-text")
        expect(title).to_have_text("Dashboard")
