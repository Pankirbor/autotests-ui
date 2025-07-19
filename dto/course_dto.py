from pydantic import BaseModel, FilePath


class CourseDto(BaseModel):
    """
    Модель данных курса.

    Attributes:
        title (str): Название курса.
        description (str): Описание курса.
        estimated_time (str): Оценочное время прохождения.
        max_score (str): Максимальный балл за курс.
        min_score (str): Минимальный балл для успешного завершения.
        source_image (FilePath): Путь к изображению курса.
    """

    title: str
    description: str
    estimated_time: str
    max_score: str
    min_score: str
    source_image: FilePath

    def get_data_for_check(self):
        """
        Возвращает данные модели без поля 'description'.

        Используется, например, при отображении информации о курсе,
        где описание не требуется.

        Returns:
            dict: Словарь с данными модели без полей 'description', 'source_image'.
        """
        return self.model_dump(exclude=["description", "source_image"])

    def get_data_for_create(self):
        """
        Возвращает все данные модели.

        Используется, например, при создании нового курса.

        Returns:
            dict: Словарь с данными модели без поля 'source_image'.
        """
        return self.model_dump(exclude=["source_image"])
