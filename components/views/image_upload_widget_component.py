from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements import Button, Icon, FileInput, Image, Text


class ImageUploadWidgetComponent(BaseComponent):
    """
    Компонент виджета загрузки файла.

    Этот класс представляет элементы интерфейса, связанные с загрузкой и удалением файлов,
    таких как кнопка загрузки, описание, иконка и изображение загруженного файла.

    Атрибуты:
        file_type (str): Тип файла (например, 'image', 'document').
        empty_view (EmptyViewComponent): Сообщение о том, что файл не выбран.
        upload_icon (Icon): Иконка загрузки.
        upload_title (Text): Заголовок окна загрузки.
        upload_description (Text): Описание окна загрузки.
        upload_btn (Button): Кнопка "Загрузить".
        upload_remove_btn (Button): Кнопка "Удалить".
        upload_input (FileInput): Поле для выбора файла.
        file_view_uploaded (Image): Изображение или превью загруженного файла.

    Методы:
        check_visible: Проверяет отображение элементов в зависимости от наличия загруженного файла.
        upload_file: Загружает файл по указанному пути.
        click_remove_button: Выполняет клик по кнопке удаления файла.
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
        self.upload_icon = Icon(
            page, f"{identifier}-{file_type}-upload-widget-info-icon", "Иконка загрузки"
        )
        self.upload_title = Text(
            page,
            f"{identifier}-{file_type}-upload-widget-info-title-text",
            "Заголовок окна загрузки",
        )
        self.upload_description = Text(
            page,
            f"{identifier}-{file_type}-upload-widget-info-description-text",
            "Описание окна загрузки",
        )
        self.upload_btn = Button(
            page,
            f"{identifier}-{file_type}-upload-widget-upload-button",
            "Кнопка загрузки",
        )

        self.upload_remove_btn = Button(
            page,
            f"{identifier}-{file_type}-upload-widget-remove-button",
            "Кнопка удаления изображения",
        )
        self.upload_input = FileInput(
            page, f"{identifier}-{file_type}-upload-widget-input", "Поле выбора файла"
        )

        self.file_view_uploaded = Image(
            page,
            f"{identifier}-{file_type}-upload-widget-preview-{file_type}",
            "Изображение курса",
        )

    def check_visible(self, is_file_uploaded: bool = False):
        """
        Проверяет видимость элементов виджета загрузки файла.

        Аргументы:
            is_file_uploaded (bool): Флаг, указывающий, был ли файл загружен.
        """
        self.upload_icon.check_visible()

        self.upload_title.check_visible().check_have_text(
            f'Tap on "Upload {self.file_type}" button to select file',
        )

        self.upload_description.check_visible().check_have_text(
            "Recommended file size 540X300"
        )
        self.upload_btn.check_visible()

        if not is_file_uploaded:
            self.empty_view.check_visible(
                title=f"No {self.file_type} selected",
                description=f"Preview of selected {self.file_type} will be displayed here",
            )
        else:
            self.upload_remove_btn.check_visible()
            self.file_view_uploaded.check_visible()

    def upload_file(self, file_path: str):
        """
        Загружает файл из указанного пути.

        Аргументы:
            file_path (str): Путь к файлу на локальной машине.
        """
        self.upload_input.check_visible().set_input_files(file_path)

    def click_remove_button(self):
        """
        Выполняет клик по кнопке удаления загруженного файла.
        """
        self.upload_remove_btn.check_visible().click()
