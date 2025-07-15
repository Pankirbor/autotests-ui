from pydantic import BaseModel


class CourseDto(BaseModel):
    title: str
    description: str
    estimated_time: str
    max_score: str
    min_score: str

    def get_data_for_check(self):
        return self.model_dump(exclude=["description"])

    def get_data_for_create(self):
        return self.model_dump()
