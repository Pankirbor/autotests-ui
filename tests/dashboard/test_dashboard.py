import allure
import pytest

from allure_commons.types import Severity

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure import AllureEpic, AllureFeature, AllureStory, AllureTag
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.dashboard
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD_UI)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD_UI)
class TestDashboard:

    @allure.title("Check displaying of dashboard page")
    @allure.tag(AllureTag.POSITIVE)
    @allure.story(AllureStory.DASHBOARD_DISPLAY)
    @allure.sub_suite(AllureStory.DASHBOARD_DISPLAY)
    @allure.severity(Severity.CRITICAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        """
        Тест проверяет отображение всех элементов на странице Dashboard.

        Шаги:
            1. Переход на страницу Dashboard.
            2. Проверка видимости и корректности отображения навигационной панели.
            3. Проверка видимости боковой панели.
            4. Проверка видимости верхней панели инструментов.
            5. Проверка видимости диаграмм: Scores, Courses, Students, Activities.

        Ожидаемый результат:
            Все элементы страницы Dashboard отображаются корректно.
        """
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.navbar.check_visible(settings.TEST_USER.username)
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.toolbar.check_visible()
        dashboard_page_with_state.scores_chart.check_visible()
        dashboard_page_with_state.courses_chart.check_visible()
        dashboard_page_with_state.students_chart.check_visible()
        dashboard_page_with_state.activites_chart.check_visible()
