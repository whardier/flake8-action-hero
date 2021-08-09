import re
from tokenize import COMMENT, TokenInfo
from typing import ClassVar, Iterator, List, Optional, Sequence, Tuple, Type

from .actions import get_action
from .enums import CommentTypeEnum
from .metadata import project_name, project_version


RE_BRACKETS_ROUND = re.compile(r"\([^)]*\)")
RE_BRACKETS_SQUARE = re.compile(r"\[[^)]*\]")
RE_BRACKETS_CURLY = re.compile(r"\{[^)]*\}")
RE_BRACKETS_ANGLE = re.compile(r"\<[^)]*\>")

# TODO: This is a test comment
# FIXME: This is a text comment
# perhaps a continuation as well


class ActionChecker(object):

    name: ClassVar[str] = project_name
    version: ClassVar[str] = project_version

    file_tokens: Sequence[TokenInfo]

    options = None

    filename: str

    def __init__(
        self,
        tree,
        filename: str,
        file_tokens: List[TokenInfo],
    ) -> None:

        self.filename = filename
        self.file_tokens = file_tokens

    def run(self) -> Iterator[Tuple[int, int, str, Type["ActionChecker"]]]:

        for file_comment_token in self.iterate_filter_only_comment_file_tokens():

            actions_or_strings: List[str] = []

            comment_type: Optional[CommentTypeEnum] = None
            comment_type_original_string: Optional[str] = None

            for offset, original_string in enumerate(
                file_comment_token.string.split(":")
            ):

                working_string = original_string.split("#", maxsplit=1)[-1]

                if offset == 0:
                    comment_type_original_string = working_string.strip()

                working_string = RE_BRACKETS_ROUND.sub("", working_string)
                working_string = RE_BRACKETS_SQUARE.sub("", working_string)
                working_string = RE_BRACKETS_CURLY.sub("", working_string)
                working_string = RE_BRACKETS_ANGLE.sub("", working_string)

                working_string = working_string.strip()

                if not working_string.isupper():
                    working_string = original_string
                if not working_string.isalpha():
                    working_string = original_string

                if offset == 0:
                    try:
                        comment_type = CommentTypeEnum[working_string]
                    except KeyError:
                        break
                else:
                    actions_or_strings.append(working_string)

            if (
                comment_type is not None
                and comment_type_original_string
                and actions_or_strings
            ):
                try:
                    action = get_action(
                        *actions_or_strings,
                        comment_type=comment_type,
                        comment_type_original_string=comment_type_original_string,
                    )
                except NotImplementedError:
                    continue

                error_string = action.check_and_get_error_string_or_none()

                if error_string:
                    yield (*file_comment_token.start, error_string, type(self))

        if False:
            yield 0

        # yield (1, 0, "AH001 THING", type(self))

    def iterate_filter_only_comment_file_tokens(self) -> Iterator[TokenInfo]:
        return filter(lambda file_token: file_token.type == COMMENT, self.file_tokens)
