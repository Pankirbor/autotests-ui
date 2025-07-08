import pytest

from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    [
        ("  ", "password"),
        ("user.name@gmail.com", "  "),
        ("user.name@gmail.com", "password"),
    ],
)
def test_wrong_email_or_password_authorization(
    chromium_page: Page, email: str, password: str
):
    """
    Тестирует авторизацию с неправильным email или паролем.

    Цель теста: проверить, что система корректно обрабатывает попытку входа с пустыми
    или некорректными данными и отображает соответствующее сообщение об ошибке.

    Параметры:
    - `email` (str): email для ввода в поле email.
    - `password` (str): пароль для ввода в поле пароля.

    Шаги:
    1. Переходит на страницу авторизации.
    2. Вводит указанный email и пароль.
    3. Нажимает кнопку "Войти".
    4. Проверяет, что появляется уведомление о неверном email или пароле.
    5. Проверяет текст уведомления на соответствие ожидаемому значению.

    Использует: параметризацию pytest, методы playwright для работы с DOM и проверки условий.
    """

    chromium_page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )

    email_input = chromium_page.get_by_test_id("login-form-email-input").locator(
        "input"
    )
    email_input.fill(email)

    password_input = chromium_page.get_by_test_id("login-form-password-input").locator(
        "input"
    )
    password_input.fill(password)

    login_button = chromium_page.get_by_test_id("login-page-login-button")
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id(
        "login-page-wrong-email-or-password-alert"
    )
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
