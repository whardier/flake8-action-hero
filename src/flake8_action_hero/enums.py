from enum import IntEnum


class CommentTypeEnum(IntEnum):
    FIXME = 0
    TODO = 1
    XXX = 2
    BUG = 3
    REFACTOR = 4
    REMOVEME = 5
    LEGACY = 6
    CRITICAL = 7
    WARNING = 8
