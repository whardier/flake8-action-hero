from abc import ABC
from datetime import date, datetime
from typing import Optional

from .base import BaseAction


class DateAction(BaseAction, ABC):

    datetime_now: datetime
    datetime_check: datetime

    date_now: date
    date_check: date

    datetime_now_str: str
    datetime_check_str: str

    date_now_str: str
    date_check_str: str

    def __init__(self, date_string: str, *args, **kwargs):

        self.datetime_now = datetime.now()
        self.datetime_check = datetime.strptime(date_string.strip(), "%Y-%m-%d")

        self.date_now = self.datetime_now.date()
        self.date_check = self.datetime_check.date()

        self.datetime_now_str = self.datetime_now.isoformat()
        self.datetime_check_str = self.datetime_check.isoformat()

        self.date_now_str = self.date_now.isoformat()
        self.date_check_str = self.date_check.isoformat()

        super().__init__(*args, **kwargs)


class DateAfterAction(DateAction):
    def check_and_get_error_string_or_none(self) -> Optional[str]:
        if self.datetime_now > self.datetime_check:
            return self.generate_error_string(
                error_code_prefix="AH00",
                error_message=f"Date after condition met ({self.datetime_now_str} > {self.datetime_check_str})",  # noqa
            )
        return None


class DateBeforeAction(DateAction):
    def check_and_get_error_string_or_none(self) -> Optional[str]:
        if self.datetime_now < self.datetime_check:
            return self.generate_error_string(
                error_code_prefix="AH01",
                error_message=f"Date before condition met ({self.datetime_now_str} < {self.datetime_check_str})",  # noqa
            )
        return None


class DateIsAction(DateAction):
    def check_and_get_error_string_or_none(self) -> Optional[str]:
        if self.datetime_now.date() == self.datetime_check.date():
            return self.generate_error_string(
                error_code_prefix="AH02",
                error_message=f"Date is condition met ({self.date_check_str} is the current date)",  # noqa
            )
        return None
