import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    """
    Класс, представляющий поле ввода для загрузки файлов на веб-странице.

    Этот класс наследуется от BaseElement и предоставляет метод для установки файлов,
    которые будут загружены через элемент <input type="file">.

    Методы:
        set_input_files: Устанавливает файл или файлы для загрузки.
    """

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        """
        Устанавливает файл для загрузки в поле ввода.

        Аргументы:
            file (str): Путь к файлу на локальной машине.
            nth (int): Индекс элемента, если на странице несколько одинаковых полей ввода.
            **kwargs: Дополнительные параметры для форматирования локатора.
        """
        with allure.step(f"Set file '{file}' to the {self.type_of} '{self.name}'"):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
