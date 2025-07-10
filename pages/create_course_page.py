from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.create_course_page_title = page.get_by_test_id(
            "create-course-toolbar-title-text"
        )
        self.create_course_btn = page.get_by_test_id(
            "create-course-toolbar-create-course-button"
        )

        # *Виджет для изображения курса пустой
        self.course_preview_empty_view_icon = page.get_by_test_id(
            "create-course-preview-empty-view-icon"
        )
        self.course_preview_empty_view_title = page.get_by_test_id(
            "create-course-preview-empty-view-title-text"
        )
        self.course_preview_empty_view_text = page.get_by_test_id(
            "create-course-preview-empty-view-description-text"
        )

        # *Виджет для изображения курса с загруженной картинкой
        self.create_course_image_view = page.get_by_test_id(
            "create-course-preview-image-upload-widget-preview-image"
        )

        # *Виджет для добавления изображения
        self.image_upload_widget_icon = page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-icon"
        )
        self.image_upload_widget_title = page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-title-text"
        )
        self.image_upload_widget_text = page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-description-text"
        )
        self.image_upload_widget_upload_btn = page.get_by_test_id(
            "create-course-preview-image-upload-widget-upload-button"
        )
        self.image_upload_widget_remove_btn = page.get_by_test_id(
            "create-course-preview-image-upload-widget-remove-button"
        )
        self.preview_image_upload_input = page.get_by_test_id(
            "create-course-preview-image-upload-widget-input"
        )

        # *Форма
        self.course_title_input = page.get_by_test_id(
            "create-course-form-title-input"
        ).locator("input")
        self.course_time_input = page.get_by_test_id(
            "create-course-form-estimated-time-input"
        ).locator("input")
        self.course_description_input = (
            page.get_by_test_id("create-course-form-description-input")
            .locator("textarea")
            .first
        )
        self.course_max_score_input = page.get_by_test_id(
            "create-course-form-max-score-input"
        ).locator("input")
        self.course_min_score_input = page.get_by_test_id(
            "create-course-form-min-score-input"
        ).locator("input")

        # *Элементы добавления упражнений
        self.course_exercises_title = page.get_by_test_id(
            "create-course-exercises-box-toolbar-title-text"
        )
        self.course_exercises_create_btn = page.get_by_test_id(
            "create-course-exercises-box-toolbar-create-exercise-button"
        )

        # *Элементы при отсутствии упражнений
        self.exercises_empty_view_icon = page.get_by_test_id(
            "create-course-exercises-empty-view-icon"
        )
        self.exercises_empty_view_title = page.get_by_test_id(
            "create-course-exercises-empty-view-title-text"
        )
        self.exercises_empty_view_text = page.get_by_test_id(
            "create-course-exercises-empty-view-description-text"
        )

    def check_visible_create_course_title(self):
        self.check_locator(self.create_course_page_title, "Create course")

    def check_visible_create_course_btn(self):
        self.check_locator(self.create_course_btn)

    def click_create_course_btn(self):
        self.create_course_btn.click()

    def check_disabled_create_course_btn(self):
        expect(self.create_course_btn).to_be_disabled()

    def check_visable_image_view_empty_view(self):
        self.check_locator(self.course_preview_empty_view_icon)
        self.check_locator(self.course_preview_empty_view_title, "No image selected")
        self.check_locator(
            self.course_preview_empty_view_text,
            "Preview of selected image will be displayed here",
        )

    def check_visable_image_upload_view(self, is_image_uploaded: bool = False) -> None:
        self.check_locator(self.image_upload_widget_icon)
        self.check_locator(
            self.image_upload_widget_title,
            'Tap on "Upload image" button to select file',
        )
        self.check_locator(
            self.image_upload_widget_text,
            "Recommended file size 540X300",
        )
        self.check_locator(self.image_upload_widget_upload_btn)

        if is_image_uploaded:
            self.check_locator(self.image_upload_widget_remove_btn)

    def upload_preview_image(self, file_path: str):
        self.preview_image_upload_input.set_input_files(file_path)

    def check_visable_preview_image(self):
        self.check_locator(self.create_course_image_view)

    def click_remove_image_btn(self):
        self.check_locator(self.image_upload_widget_remove_btn)
        self.image_upload_widget_remove_btn.click()

    def check_visable_create_course_form(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str,
    ):
        self.check_input_locator(self.course_title_input, title)
        self.check_input_locator(self.course_description_input, description)
        self.check_input_locator(self.course_time_input, estimated_time)
        self.check_input_locator(self.course_max_score_input, max_score)
        self.check_input_locator(self.course_min_score_input, min_score)

    def fill_create_course_form(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str,
    ):
        self.course_title_input.fill(title)
        self.check_input_locator(self.course_title_input, title)

        self.course_description_input.fill(description)
        self.check_input_locator(self.course_description_input, description)

        self.course_time_input.fill(estimated_time)
        self.check_input_locator(self.course_time_input, estimated_time)

        self.course_max_score_input.fill(max_score)
        self.check_input_locator(self.course_max_score_input, max_score)

        self.course_min_score_input.fill(min_score)
        self.check_input_locator(self.course_min_score_input, min_score)

    def check_visable_exercises_title(self):
        self.check_locator(self.course_exercises_title, "Exercises")

    def check_visable_exercise_create_btn(self):
        self.check_locator(self.course_exercises_create_btn)

    def click_exercise_create_btn(self):
        self.check_locator(self.course_exercises_create_btn)
        self.course_exercises_create_btn.click()

    def check_visable_empty_exercises_list(self):
        self.check_locator(self.exercises_empty_view_icon)
        self.check_locator(self.exercises_empty_view_title, "There is no exercises")
        self.check_locator(
            self.exercises_empty_view_text,
            'Click on "Create exercise" button to create new exercise',
        )

    def click_delete_exercise_btn(self, index: int):
        delete_btn = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_btn.click()

    def check_visible_create_exercise_form(
        self, index: int, title: str, description: str
    ):
        exercise_subtitle = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-subtitle-text"
        )
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        ).locator("input")
        # print("EXERCISE TITLE INPUT", exercise_title_input.text_content())
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        ).locator("input")
        self.check_locator(exercise_subtitle, f"#{index + 1} Exercise")
        self.check_input_locator(exercise_title_input, title)
        self.check_input_locator(exercise_description_input, description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        ).locator("input")
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        ).locator("input")

        exercise_title_input.fill(title)
        self.check_input_locator(exercise_title_input, title)

        exercise_description_input.fill(description)
        self.check_input_locator(exercise_description_input, description)
