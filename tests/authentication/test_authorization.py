import allure
import pytest

from allure_commons.types import Severity

from pages import LoginPage, RegistrationPage, DashboardPage
from tools.allure import AllureEpic, AllureFeature, AllureStory, AllureTag


@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:

    @allure.title("User login with wrong email or password")
    @allure.tag(AllureTag.NEGATIVE)
    @allure.story(AllureStory.INVALID_AUTH)
    @allure.sub_suite(AllureStory.INVALID_AUTH)
    @allure.severity(Severity.NORMAL)
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

    @allure.title("User login with correct credentials")
    @allure.tag(AllureTag.POSITIVE, AllureTag.END2END)
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
        self,
        login_page: LoginPage,
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
    ):
        """
        Тест проверяет успешную авторизацию пользователя с корректными данными и регистрацией нового пользователя.

        Описание:
            Пользователь регистрирует новый аккаунт, затем авторизуется, проверяет наличие элементов главной страницы
            и выходит из системы.

        Шаги:
            1. Переход на страницу авторизации.
            2. Проверка заголовка страницы.
            3. Переход на страницу регистрации.
            4. Проверка заголовка страницы регистрации.
            5. Проверка видимости формы.
            6. Заполнение формы данными.
            7. Нажатие кнопки регистрации.
            8. Проверка наличия элементов главной страницы.
            9. Выход из системы.
            10. Повторная авторизация.
            11. Проверка отображения имени пользователя в навбаре.

        Ожидаемый результат:
            Пользователь успешно регистрируется, авторизуется и видит элементы главной страницы.
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

    @allure.title("Navigation from login page to registration page")
    @allure.tag(AllureTag.NAVIGATION, AllureTag.POSITIVE)
    @allure.severity(Severity.CRITICAL)
    def test_navigate_from_authorization_to_registration(
        self, login_page: LoginPage, registration_page: RegistrationPage
    ):
        """
        Тест проверяет переход с страницы авторизации на страницу регистрации.

        Описание:
            Пользователь переходит на страницу авторизации и через ссылку "Registrtion" попадает на страницу
            регистрации. Проверяется видимость формы регистрации.

        Шаги:
            1. Переход на страницу авторизации.
            2. Нажатие на ссылку "Registrtion".
            3. Проверка видимости формы регистрации.

        Ожидаемый результат:
            После нажатия на ссылку "Registrtion" отображается форма регистрации.
        """
        login_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
        )
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(
            email="", username="", password=""
        )
