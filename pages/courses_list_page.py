from playwright.sync_api import Page

from pages.base_page import BasePage
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.courses_page_title = page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_course_btn = page.get_by_test_id(
            "courses-list-toolbar-create-course-button"
        )

        self.course_card_title = page.get_by_test_id("course-widget-title-text")
        self.course_card_image = page.get_by_test_id("course-preview-image")
        self.course_card_max_score = page.get_by_test_id(
            "course-max-score-info-row-view-text"
        )
        self.course_card_min_score = page.get_by_test_id(
            "course-min-score-info-row-view-text"
        )
        self.course_card_estimated_time = page.get_by_test_id(
            "course-estimated-time-info-row-view-text"
        )

        self.course_menu_button = page.get_by_test_id("course-view-menu-button")
        self.course_edit_menu_item = page.get_by_test_id("course-view-edit-menu-item")
        self.course_delete_menu_item = page.get_by_test_id(
            "course-view-delete-menu-item"
        )

        self.empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
        self.empty_view_title = page.get_by_test_id(
            "courses-list-empty-view-title-text"
        )
        self.empty_view_description = page.get_by_test_id(
            "courses-list-empty-view-description-text"
        )

    def check_visable_courses_page_title(self):
        self.check_locator(self.courses_page_title, "Courses")

    def check_visable_create_course_btn(self):
        self.check_locator(self.create_course_btn)

    def check_visable_empty_courses_list(self):
        self.check_locator(self.empty_view_icon)
        self.check_locator(self.empty_view_title, "")
        self.check_locator(self.empty_view_description, "")

    def check_visible_course_card(
        self,
        index: int,
        title: str,
        max_score: str,
        min_score: str,
        estimated_time: str,
    ):
        self.check_locator(self.course_card_image.nth(index))
        self.check_locator(self.course_card_title.nth(index), title)
        self.check_locator(
            self.course_card_estimated_time.nth(index),
            f"Estimated time: {estimated_time}",
        )
        self.check_locator(
            self.course_card_max_score.nth(index), f"Max score: {max_score}"
        )
        self.check_locator(
            self.course_card_min_score.nth(index), f"Min score: {min_score}"
        )

    def check_visable_menu_course(self):
        self.check_locator(self.course_menu_button)

    def click_create_course_btn(self):
        self.create_course_btn.click()

    def click_edit_menu_course(self, index: int):
        self.course_menu_button.nth(index).click()
        self.check_locator(self.course_edit_menu_item.nth(index))
        self.course_edit_menu_item.nth(index).click()

    def click_delete_menu_course(self, index: int):
        self.course_menu_button.nth(index).click()
        self.check_locator(self.course_delete_menu_item.nth(index))
        self.course_edit_menu_item.nth(index).click()
