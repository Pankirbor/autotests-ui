import pytest

from pages.login_page import LoginPage


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
    login_page: LoginPage, email: str, password: str
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
    login_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )
    login_page.fill_login_form(email, password)
    login_page.click_login_btn()
    login_page.check_visible_wrong_email_or_password_alert(
        text_alert="Wrong email or password"
    )
