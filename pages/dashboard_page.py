from playwright.sync_api import Page

from components.navigation.navbar_component import NavbarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.title_dashboard_page = page.get_by_test_id("dashboard-toolbar-title-text")
        self.title_chart_view_sudents = page.get_by_test_id(
            "students-widget-title-text"
        )
        self.chart_view_students = page.get_by_test_id("students-bar-chart")

        self.title_chart_view_courses = page.get_by_test_id("courses-widget-title-text")
        self.chart_view_courses = page.get_by_test_id("courses-pie-chart")

        self.title_chart_view_scores = page.get_by_test_id("scores-widget-title-text")
        self.chart_view_scores = page.get_by_test_id("scores-scatter-chart")

        self.title_chart_view_activities = page.get_by_test_id(
            "activities-widget-title-text"
        )
        self.chart_view_activites = page.get_by_test_id("activities-line-chart")

    def check_visible_dashboard_page_title(self) -> None:
        self.check_locator(self.title_dashboard_page, "Dashboard")

    def check_visible_students_chart(self) -> None:
        self.check_locator(self.title_chart_view_sudents, "Students")
        self.check_locator(self.chart_view_students)

    def check_visible_courses_chart(self) -> None:
        self.check_locator(self.title_chart_view_courses, "Courses")
        self.check_locator(self.chart_view_courses)

    def check_visible_activities_chart(self) -> None:
        self.check_locator(self.title_chart_view_activities, "Activities")
        self.check_locator(self.chart_view_activites)

    def check_visible_scores_chart(self) -> None:
        self.check_locator(self.title_chart_view_scores, "Scores")
        self.check_locator(self.chart_view_scores)
