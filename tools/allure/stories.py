from enum import Enum


class AllureStory(str, Enum):
    DASHBOARD_DISPLAY = "Dashboard Page Display"
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"
    INVALID_AUTH = "Invalid Credentials Handling"
    EMPTY_COURSES_LIST = "Empty Courses List"
    CREATE_COURSE = "Create Course"
    EDIT_COURSE = "Edit Course"
