from playwright.sync_api import Page

from components.charts.charts_view_component import ChartViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import (
    DashboardToolbarViewComponent,
)
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """
    Класс, представляющий страницу главной панели (Dashboard).

    Атрибуты:
        navbar (NavbarComponent): Компонент верхней навигационной панели.
        sidebar (SidebarComponent): Компонент боковой панели.
        toolbar (DashboardToolbarViewComponent): Верхняя панель инструментов Dashboard.
        students_chart (ChartViewComponent): Диаграмма студентов.
        courses_chart (ChartViewComponent): Диаграмма курсов.
        activities_chart (ChartViewComponent): Диаграмма активностей.
        scores_chart (ChartViewComponent): Диаграмма оценок.

    Методы:
        __init__: Инициализирует все компоненты страницы Dashboard.
    """

    def __init__(self, page: Page) -> None:
        """
        Инициализирует объект DashboardPage и связанные с ним компоненты.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится Dashboard.
        """
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = DashboardToolbarViewComponent(page)
        self.students_chart = ChartViewComponent(
            page, "Students", identifier_chart="students-bar"
        )
        self.courses_chart = ChartViewComponent(
            page, title="Courses", identifier_chart="courses-pie"
        )
        self.activites_chart = ChartViewComponent(
            page, title="Activities", identifier_chart="activities-line"
        )
        self.scores_chart = ChartViewComponent(
            page, title="Scores", identifier_chart="scores-scatter"
        )
