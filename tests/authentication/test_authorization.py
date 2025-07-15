import pytest

from pages import LoginPage, RegistrationPage, DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("  ", "password"),
            ("user.name@gmail.com", "  "),
            ("user.name@gmail.com", "password"),
        ],
    )
    def test_wrong_email_or_password_authorization(
        self, login_page: LoginPage, email: str, password: str
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

    def test_successful_authorization(
        self,
        login_page: LoginPage,
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
    ):
        """Открываем страницу регистрации: https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration.
        Заполняем форму регистрации валидными данными и нажимаем кнопку "Registration".
        Происходит редирект на страницу "Dashboard": https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard. Нажимаем кнопку "Logout" в Sidebar, происходит редирект на страницу "Login".
        Заполняем форму авторизации валидными данными и нажимаем кнопку "Login".
        Проверяем, что происходит редирект обратно на страницу "Dashboard": https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard.
        """
        login_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
        )
        login_page.check_visible_login_page_title()
        login_page.click_registration_link()
        registration_page.check_visible_page_title()
        registration_page.form.check_visible()
        registration_page.form.fill(
            email="user.name@gmail.com", username="username", password="password"
        )
        registration_page.click_registration_btn()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.toolbar.check_visible()
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()
        login_page.check_visible_login_page_title()
        login_page.form.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_btn()
        dashboard_page.navbar.check_visible("username")

    def test_navigate_from_authorization_to_registration(
        self, login_page: LoginPage, registration_page: RegistrationPage
    ):
        login_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
        )
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(
            email="", username="", password=""
        )
