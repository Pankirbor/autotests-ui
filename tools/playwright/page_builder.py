import typing

import allure
from playwright.sync_api import Playwright, Page


def playwright_page_builder(
    playwright: Playwright, test_name: str, state: str | None = None
) -> typing.Iterator[Page]:
    """
    Генератор, создающий и настраивающий страницу Playwright для запуска теста.

    Эта функция используется в качестве фикстуры в тестах. Она запускает браузер,
    создает контекст с возможностью записи видео и трассировки, а после выполнения
    теста завершает работу браузера и прикрепляет результаты (видео и трассировку)
    к отчету Allure.

    Args:
        playwright (Playwright): Объект Playwright для управления браузером.
        test_name (str): Название теста, используется для именования файлов
                         трассировки и видео.
        state (str | None): Необязательный параметр — путь к файлу состояния
                            браузера для восстановления авторизации и т.п.

    Yields:
        Page: Объект страницы Playwright, готовый к использованию в тесте.

    Returns:
        Generator[Page, None, None]: Генератор, возвращающий страницу Playwright.

    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=state, record_video_dir="./videos")
    context.tracing.start(
        name=test_name, screenshots=True, snapshots=True, sources=True
    )
    page = context.new_page()

    yield page

    context.tracing.stop(path=f"./tracing/{test_name}.zip")
    browser.close()

    allure.attach.file(
        source=f"./tracing/{test_name}.zip",
        name="trace",
        extension="zip",
    )
    allure.attach.file(
        source=page.video.path,
        name="video",
        attachment_type=allure.attachment_type.WEBM,
    )
