import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(
    registration_page: RegistrationPage, dashboard_page: DashboardPage
):
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
    registration_page.visit(
        " https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )
    registration_page.fill_registration_form(
        "user.name@gmail.com", "username", "password"
    )
    registration_page.click_registration_btn()
    dashboard_page.visit(registration_page.page.url)
    dashboard_page.check_visible_dashboard_page_title(text_title="Dashboard")
