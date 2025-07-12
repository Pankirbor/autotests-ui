import pytest

from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.dashboard
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
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
    dashboard_page_with_state.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"
    )
    dashboard_page_with_state.navbar.check_visible("username")
    dashboard_page_with_state.sidebar.check_visible()
    dashboard_page_with_state.toolbar.check_visible()
    dashboard_page_with_state.scores_chart.check_visible()
    dashboard_page_with_state.courses_chart.check_visible()
    dashboard_page_with_state.students_chart.check_visible()
    dashboard_page_with_state.activites_chart.check_visible()
