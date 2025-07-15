from enum import Enum


class AllureTag(str, Enum):
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"
    NAVIGATION = "NAVIGATION"
    END2END = "END2END"
