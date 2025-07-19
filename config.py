from enum import Enum
from typing import Any, Self

from pydantic import BaseModel, EmailStr, DirectoryPath, HttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    """
    Перечисление, представляющее поддерживаемые браузеры.

    Каждый элемент перечисления представлен в виде строки, что позволяет использовать
    значения напрямую при выборе браузера для запуска тестов или других действий.

    Members:
        WEBKIT (str): Браузер WebKit.
        CHROMIUM (str): Браузер Chromium.
        FIREFOX (str): Браузер Firefox.
    """

    WEBKIT = "webkit"
    CHROMIUM = "chromium"
    FIREFOX = "firefox"


class TestUser(BaseModel):
    """
    Модель данных, представляющая тестового пользователя.

    Используется для валидации и хранения информации о пользователе,
    необходимой для тестирования. Включает обязательные поля: имя пользователя,
    адрес электронной почты и пароль.

    Attributes:
        username (str): Имя пользователя.
        email (EmailStr): Адрес электронной почты, валидированный как корректный email.
        password (str): Пароль пользователя.
    """

    username: str
    email: EmailStr
    password: str


class Settings(BaseSettings):
    """
    Класс настроек, загружающий конфигурацию из файла `.env.test`.

    Использует `pydantic.BaseSettings` для автоматической валидации и загрузки переменных окружения.
    Конфигурация указывает путь к файлу `.env.test`, разделитель для вложенных полей и кодировку.

    Attributes:
        APP_URL (HttpUrl): URL-адрес приложения.
        HEADLESS (bool): Флаг запуска браузера в headless-режиме.
        BROWSERS (list[Browser]): Список поддерживаемых браузеров для тестирования.
        TEST_USER (TestUser): Объект с данными тестового пользователя.
        VIDEOS_PATH (DirectoryPath): Путь к директории для хранения видео записей тестов.
        TRACING_PATH (DirectoryPath): Путь к директории для хранения трассировок.
        ALLURE_RESULTS_PATH (DirectoryPath): Путь к директории результатов Allure.
        BROWSER_STATE_FILE (FilePath): Путь к файлу состояния браузера.
        SNAPSHOTS_TESTS (list[str], optional): Список тестов, для которых будут сохраняться снимки экрана.

    Methods:
        initialize: Создает экземпляр `Settings` и инициализирует структуру каталогов.
        get_base_url: Возвращает базовый URL приложения.
        get_env_properties: Возвращает словарь с основными параметрами окружения.
    """

    model_config = SettingsConfigDict(
        env_file=".env.test",
        env_nested_delimiter=".",
        env_file_encoding="utf-8",
    )
    APP_URL: HttpUrl
    HEADLESS: bool
    BROWSERS: list[Browser]
    TEST_USER: TestUser
    VIDEOS_PATH: DirectoryPath
    TRACING_PATH: DirectoryPath
    ALLURE_RESULTS_PATH: DirectoryPath
    BROWSER_STATE_FILE: FilePath

    @classmethod
    def initialize(cls) -> Self:
        """
        Создает экземпляр класса `Settings` и инициализирует структуру каталогов.

        Метод создает директории для хранения видео и трассировок, а также
        файл состояния браузера, если они не существуют.

        Returns:
            Self: Экземпляр класса `Settings` с установленными путями.
        """
        videos_path = DirectoryPath("./videos")
        tracing_path = DirectoryPath("./tracing")
        allure_results_path = DirectoryPath("./allure_results")
        browser_state_file = FilePath("browser_state.json")

        videos_path.mkdir(exist_ok=True)
        tracing_path.mkdir(exist_ok=True)
        allure_results_path.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            BROWSER_STATE_FILE=browser_state_file,
            VIDEOS_PATH=videos_path,
            TRACING_PATH=tracing_path,
            ALLURE_RESULTS_PATH=allure_results_path,
        )

    def get_base_url(self) -> str:
        """
        Возвращает базовый URL приложения.

        Добавляет завершающий слеш к значению `APP_URL`.

        Returns:
            str: Базовый URL приложения.
        """
        return f"{self.APP_URL}/"

    def get_env_properties(self) -> dict[str, Any]:
        """
        Возвращает словарь с основными параметрами окружения.

        Используется для формирования файла `environment.properties` в Allure.

        Returns:
            dict[str, Any]: Словарь с ключами `APP_URL`, `HEADLESS`, `BROWSERS`,
                            `TEST_USER`, `BROWSER_STATE_FILE`.
        """
        return self.model_dump(
            include=[
                "APP_URL",
                "HEADLESS",
                "BROWSERS",
                "TEST_USER",
                "BROWSER_STATE_FILE",
            ]
        )


settings = Settings.initialize()
