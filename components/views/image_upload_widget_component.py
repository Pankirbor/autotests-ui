from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    """
    Компонент для работы с виджетом загрузки файла.

    Атрибуты:
        file_type (str): Тип файла, связанный с виджетом.
        empty_view (EmptyViewComponent): Экземпляр компонента пустого представления.
        upload_icon: Локатор иконки загрузки.
        upload_title: Локатор заголовка виджета.
        upload_description: Локатор описания виджета.
        upload_btn: Локатор кнопки загрузки файла.
        upload_remove_btn: Локатор кнопки удаления файла.
        upload_input: Локатор поля ввода файла.
        file_view_uploaded: Локатор отображения загруженного файла.

    Методы:
        check_visible: Проверяет видимость элементов виджета.
        upload_file: Выполняет загрузку файла по указанному пути.
        click_remove_button: Кликает по кнопке удаления файла.
    """

    def __init__(self, page: Page, identifier: str, file_type: str):
        """
        Инициализирует объект FileUploadWidgetComponent.

        Аргументы:
            page (Page): Экземпляр страницы, к которой относится компонент.
            identifier (str): Уникальный идентификатор компонента для формирования локаторов.
            file_type (str): Тип файла, например 'image' или 'document'.
        """
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
        """
        Проверяет видимость элементов виджета загрузки файла.

        Аргументы:
            is_file_uploaded (bool): Флаг, указывающий, был ли файл загружен.
        """
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
        """
        Загружает файл из указанного пути.

        Аргументы:
            file_path (str): Путь к файлу на локальной машине.
        """
        self.upload_input.set_input_files(file_path)

    def click_remove_button(self):
        """
        Выполняет клик по кнопке удаления загруженного файла.
        """
        self.upload_remove_btn.click()
