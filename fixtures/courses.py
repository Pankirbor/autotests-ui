import pytest

from dto.course_dto import CourseDto


@pytest.fixture
def course_create_dto():
    course = CourseDto(
        **{
            "title": "Playwright",
            "estimated_time": "2 weeks",
            "description": "Playwright",
            "max_score": "100",
            "min_score": "10",
        }
    )
    return course


@pytest.fixture
def course_edit_dto():
    course = CourseDto(
        **{
            "title": "Python",
            "estimated_time": "3 weeks",
            "description": "Python",
            "max_score": "200",
            "min_score": "20",
        }
    )
    return course
