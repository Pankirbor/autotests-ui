from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_course = CourseViewMenuComponent(page)

        self.title = page.get_by_test_id("course-widget-title-text")
        self.image = page.get_by_test_id("course-preview-image")
        self.max_score = page.get_by_test_id("course-max-score-info-row-view-text")
        self.min_score = page.get_by_test_id("course-min-score-info-row-view-text")
        self.estimated_time = page.get_by_test_id(
            "course-estimated-time-info-row-view-text"
        )

    def check_visible(
        self,
        index: int,
        title: str,
        max_score: str,
        min_score: str,
        estimated_time: str,
    ):
        self.check_locator(self.image.nth(index))
        self.check_locator(self.title.nth(index), title)
        self.check_locator(
            self.estimated_time.nth(index),
            f"Estimated time: {estimated_time}",
        )
        self.check_locator(self.max_score.nth(index), f"Max score: {max_score}")
        self.check_locator(self.min_score.nth(index), f"Min score: {min_score}")
