import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(
        self, registration_page: RegistrationPage, dashboard_page: DashboardPage
    ):
        """
        Тест проверяет успешную регистрацию пользователя через форму регистрации.

        Описание:
            Пользователь заполняет форму регистрации (электронная почта, имя пользователя и пароль),
            отправляет её и проверяет, что происходит перенаправление на страницу Dashboard.
            Проверяются видимость формы и корректность отображения элементов на странице Dashboard.

        Шаги:
            1. Переход на страницу регистрации.
            2. Проверка отображения заголовка страницы.
            3. Проверка видимости полей формы регистрации.
            4. Заполнение формы данными.
            5. Нажатие кнопки "Зарегистрироваться".
            6. Проверка отображения панели инструментов на странице Dashboard.

        Ожидаемый результат:
            Форма успешно отправлена, пользователь зарегистрирован и перенаправлен на страницу Dashboard.
        """
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )
        registration_page.check_visible_page_title()
        registration_page.form.check_visible()
        registration_page.form.fill("user.name@gmail.com", "username", "password")
        registration_page.click_registration_btn()
        dashboard_page.toolbar.check_visible()
