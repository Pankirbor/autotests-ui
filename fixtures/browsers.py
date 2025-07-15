from typing import Generator

import pytest

from playwright.sync_api import Playwright, Page

from pages import RegistrationPage


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, None, None]:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    """
    Фикстура для инициализации браузера и сохранения состояния после регистрации.

    Эта фикстура запускается один раз за сессию тестирования. Она открывает браузер,
    регистрирует нового пользователя на странице регистрации и сохраняет состояние контекста
    в файл `browser-state.json`, чтобы использовать его в последующих тестах.

    Аргументы:
        playwright (Playwright): Объект Playwright для управления браузером.

    Возвращает:
        None
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )
    registration_page.form.fill("user.name@gmail.com", "username", "password")
    registration_page.click_registration_btn()
    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(
    initialize_browser_state, playwright: Playwright
) -> Generator[Page, None, None]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    yield page
    browser.close()
