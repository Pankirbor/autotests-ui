import allure

from elements.base_element import BaseElement
from tools.logger import get_logger


logger = get_logger(__name__.upper())


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
        step = f"Set file '{file}' to the {self.type_of} '{self.name}'"
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.set_input_files(file)
