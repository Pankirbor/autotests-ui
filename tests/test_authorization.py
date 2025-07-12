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
    Тест проверяет поведение страницы авторизации при вводе неверной электронной почты или пароля.

    Описание:
        Пользователь пытается войти с разными комбинациями невалидных данных (пустой email, пустой пароль,
        корректные данные, но несуществующий аккаунт). После отправки формы проверяется появление уведомления
        о неверных данных.

    Аргументы:
        email (str): Электронная почта для входа.
        password (str): Пароль для входа.

    Шаги:
        1. Переход на страницу авторизации.
        2. Проверка видимости формы.
        3. Заполнение формы данными.
        4. Клик по кнопке "Login".
        5. Проверка отображения сообщения об ошибке.

    Ожидаемый результат:
        При вводе неверных данных отображается соответствующее уведомление.
    """
    login_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )
    login_page.form.check_visible()
    login_page.form.fill(email, password)
    login_page.click_login_btn()
    login_page.check_visible_wrong_email_or_password_alert()
