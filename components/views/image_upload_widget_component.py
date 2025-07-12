from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, file_type: str):
        super().__init__(page)

        self.file_type = file_type

        self.empty_view = EmptyViewComponent(page, identifier)
        self.upload_icon = page.get_by_test_id(
            f"{identifier}-{file_type}-upload-widget-info-icon"
        )
        self.upload_title = page.get_by_test_id(
            f"{identifier}-{file_type}-upload-widget-info-title-text"
        )
        self.upload_description = page.get_by_test_id(
            f"{identifier}-{file_type}-upload-widget-info-description-text"
        )
        self.upload_btn = page.get_by_test_id(
            f"{identifier}-{file_type}-upload-widget-upload-button"
        )

        self.upload_remove_btn = page.get_by_test_id(
            f"{identifier}-{file_type}-upload-widget-remove-button"
        )
        self.upload_input = page.get_by_test_id(
            f"{identifier}-{file_type}-upload-widget-input"
        )

        self.file_view_uploaded = page.get_by_test_id(
            f"{identifier}-{file_type}-upload-widget-preview-{file_type}"
        )

    def check_visible(self, is_file_uploaded: bool = False):
        self.check_locator(self.upload_icon)
        self.check_locator(
            self.upload_title,
            f'Tap on "Upload {self.file_type}" button to select file',
        )
        self.check_locator(
            self.upload_description,
            "Recommended file size 540X300",
        )
        self.check_locator(self.upload_btn)

        if not is_file_uploaded:
            self.empty_view.check_visible(
                title=f"No {self.file_type} selected",
                description=f"Preview of selected {self.file_type} will be displayed here",
            )
        else:
            self.check_locator(self.upload_remove_btn)
            self.check_locator(self.file_view_uploaded)

    def upload_file(self, file_path: str):
        self.upload_input.set_input_files(file_path)

    def click_remove_button(self):
        self.upload_remove_btn.click()
