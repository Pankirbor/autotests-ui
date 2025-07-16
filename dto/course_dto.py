from pydantic import BaseModel


from pydantic import BaseModel


class CourseDto(BaseModel):
    """
    DTO-модель для представления данных курса.

    Attributes:
        title (str): Название курса.
        description (str): Описание курса.
        estimated_time (str): Примерное время прохождения курса.
        max_score (str): Максимальный возможный балл.
        min_score (str): Минимальный пороговый балл.
    """

    title: str
    description: str
    estimated_time: str
    max_score: str
    min_score: str

    def get_data_for_visible(self) -> dict[str, str]:
        """
        Возвращает данные модели без поля 'description'.

        Используется, например, при отображении информации о курсе,
        где описание не требуется.

        Returns:
            dict: Словарь с данными модели без поля 'description'.
        """
        return self.model_dump(exclude=["description"])

    def get_data_for_create(self) -> dict[str, str]:
        """
        Возвращает все данные модели.

        Используется, например, при создании нового курса.

        Returns:
            dict: Словарь со всеми данными модели.
        """
        return self.model_dump()
