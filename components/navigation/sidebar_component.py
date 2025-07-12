import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    """
    Компонент боковой панели навигации.

    Атрибуты:
        dashboard_list_item (SidebarListItemComponent): Элемент списка для перехода на Dashboard.
        courses_list_item (SidebarListItemComponent): Элемент списка для перехода на страницу курсов.
        logout_list_item (SidebarListItemComponent): Элемент списка для выхода из аккаунта.

    Методы:
        check_visible: Проверяет видимость элементов боковой панели.
        click_logout: Кликает по кнопке "Logout" и проверяет переход на страницу входа.
        click_dashboard: Кликает по кнопке "Dashboard" и проверяет переход на главную страницу.
        click_courses: Кликает по кнопке "Courses" и проверяет переход на страницу курсов.
    """

    def __init__(self, page: Page):
        """
        Инициализирует компонент боковой панели.

        Аргументы:
            page (Page): Экземпляр страницы браузера.
        """
        super().__init__(page)

        self.dashboard_list_item = SidebarListItemComponent(
            page, identifier="dashboard"
        )
        self.courses_list_item = SidebarListItemComponent(page, identifier="courses")
        self.logout_list_item = SidebarListItemComponent(page, identifier="logout")

    def check_visible(self):
        """
        Проверяет, что все элементы боковой панели отображаются корректно.
        """
        self.dashboard_list_item.check_visible("Dashboard")
        self.courses_list_item.check_visible("Courses")
        self.logout_list_item.check_visible("Logout")

    def click_logout(self):
        """
        Выполняет клик по элементу "Logout" и проверяет переход на страницу входа.
        """
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    def click_dashboard(self):
        """
        Выполняет клик по элементу "Dashboard" и проверяет переход на главную страницу.
        """
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))

    def click_courses(self):
        """
        Выполняет клик по элементу "Courses" и проверяет переход на страницу курсов.
        """
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))
