import pytest

from playwright.sync_api import Page

from pages import (
    LoginPage,
    DashboardPage,
    RegistrationPage,
    CoursesListPage,
    CreateCoursePage,
)


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    """
    Фикстура для создания страницы логина.

    Аргументы:
        chromium_page (Page): Объект страницы Playwright.

    Возвращает:
        LoginPage: Объект страницы логина.
    """
    return LoginPage(chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    """
    Фикстура для создания страницы регистрации.

    Аргументы:
        chromium_page (Page): Объект страницы Playwright.

    Возвращает:
        RegistrationPage: Объект страницы регистрации.
    """
    return RegistrationPage(chromium_page)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    """
    Фикстура для создания страницы дашборда.

    Аргументы:
        chromium_page (Page): Объект страницы Playwright.

    Возвращает:
        DashboardPage: Объект страницы дашборда.
    """
    return DashboardPage(chromium_page)


@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    """
    Фикстура для создания страницы дашборда с состоянием.

    Аргументы:
        chromium_page_with_state (Page): Объект страницы Playwright с состоянием.

    Возвращает:
        DashboardPage: Объект страницы дашборда.
    """
    return DashboardPage(chromium_page_with_state)


@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    """
    Фикстура для создания страницы списка курсов.

    Аргументы:
        chromium_page_with_state (Page): Объект страницы Playwright с состоянием.

    Возвращает:
        CoursesListPage: Объект страницы списка курсов.
    """
    return CoursesListPage(chromium_page_with_state)


@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    """
    Фикстура для создания страницы создания курса.

    Аргументы:
        chromium_page_with_state (Page): Объект страницы Playwright с состоянием.

    Возвращает:
        CreateCoursePage: Объект страницы создания курса.
    """
    return CreateCoursePage(chromium_page_with_state)
