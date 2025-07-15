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
    return LoginPage(chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(chromium_page)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(chromium_page)


@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(chromium_page_with_state)


@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(chromium_page_with_state)


@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(chromium_page_with_state)
