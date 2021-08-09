from copy import deepcopy
from typing import Any, Dict

from flake8_action_hero.enums import CommentTypeEnum

from .base import BaseAction
from .date import DateAfterAction, DateBeforeAction, DateIsAction
from .package import PackageVersionAction


ACTIONS_CLASS_MAP: Dict[str, Any] = {
    "DATE": {
        "AFTER": DateAfterAction,
        "BEFORE": DateBeforeAction,
        "IS": DateIsAction,
    },
    "PACKAGE": {
        "VERSION": PackageVersionAction,
    },
}


def get_action(
    *actions_or_strings: str,
    comment_type: CommentTypeEnum,
    comment_type_original_string: str
):

    action_class_reduction_map: Dict[str, Any] = deepcopy(ACTIONS_CLASS_MAP)

    for offset, action_or_string in enumerate(actions_or_strings, start=1):
        if action_or_string in action_class_reduction_map:
            action_class_reduction_map = action_class_reduction_map.pop(
                action_or_string
            )
            if type(action_class_reduction_map) == type(BaseAction):
                action_or_string = action_class_reduction_map(  # type: ignore
                    *actions_or_strings[offset:],
                    comment_type=comment_type,
                    comment_type_original_string=comment_type_original_string,
                )
                return action_or_string

    raise NotImplementedError()
