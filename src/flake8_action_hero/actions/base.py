from abc import ABC, abstractmethod
from typing import Optional

from flake8_action_hero.enums import CommentTypeEnum


class BaseAction(ABC):

    message: str

    comment_type: CommentTypeEnum
    comment_value: int
    comment_type_original_string: str

    def __init__(
        self,
        *messages: str,
        comment_type=CommentTypeEnum,
        comment_type_original_string: str,
        **kwargs,
    ):

        self.message = ":".join(messages).strip()

        self.comment_type = comment_type
        self.comment_value = comment_type.value
        self.comment_type_original_string = comment_type_original_string.strip()

    @abstractmethod
    def check_and_get_error_string_or_none(self) -> Optional[str]:
        raise NotImplementedError()

    def generate_error_string(self, error_code_prefix: str, error_message: str) -> str:
        return f"{error_code_prefix}{self.comment_value} {error_message}: {self.comment_type_original_string}: {self.message}"  # noqa
