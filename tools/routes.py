from enum import Enum


class AppRoute(str, Enum):
    """
    Перечисление маршрутов приложения.

    Представляет собой пути к различным страницам веб-приложения в виде строк.
    Используется для удобного обращения к URL внутри тестов или логики приложения.

    Members:
        LOGIN (str): Путь к странице входа в систему.
        REGISTRATION (str): Путь к странице регистрации.
        DASHBOARD (str): Путь к главной странице пользователя.
        COURSES (str): Путь к странице курсов.
        COURSES_CREATE (str): Путь к странице создания курса.
        AUTORIZATION (str): Путь к странице авторизации.
    """

    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"
    DASHBOARD = "./#/dashboard"
    COURSES = "./#/courses"
    COURSES_CREATE = "./#/courses/create"
    AUTORIZATION = "./#/auth/login"
