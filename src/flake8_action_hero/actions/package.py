from importlib.metadata import PackageNotFoundError
from typing import Optional

from .base import BaseAction


try:
    import packaging.requirements

    PACKAGING_REQUIREMENTS = True
except ImportError:
    PACKAGING_REQUIREMENTS = False

try:
    import importlib.metadata as importlib_metadata

    IMPORTLIB_METADATA = True
except ImportError:
    import importlib_metadata  # type: ignore

    IMPORTLIB_METADATA = True
except ImportError:
    IMPORTLIB_METADATA = False


class PackageVersionAction(BaseAction):

    requirement_string: str

    def __init__(self, requirement_string: str, *args, **kwargs):

        self.requirement_string = requirement_string
        super().__init__(*args, **kwargs)

    def check_and_get_error_string_or_none(self) -> Optional[str]:
        if PACKAGING_REQUIREMENTS and IMPORTLIB_METADATA:
            requirement = packaging.requirements.Requirement(self.requirement_string)
            try:
                package_version: str = importlib_metadata.version(requirement.name)
            except PackageNotFoundError:
                return self.generate_error_string(
                    error_code_prefix="AH41",
                    error_message=f"Package version condition issue ({requirement.name} via {requirement} not installed)",  # noqa
                )
            if requirement.specifier.contains(package_version):
                return self.generate_error_string(
                    error_code_prefix="AH40",
                    error_message=f"Package version condition met ({requirement} contains {requirement.name}=={package_version})",  # noqa
                )
        else:
            if not PACKAGING_REQUIREMENTS:
                return self.generate_error_string(
                    error_code_prefix="AH49",
                    error_message=f"Package version condition issue (packaging not installed)",  # noqa
                )
            if not IMPORTLIB_METADATA:
                return self.generate_error_string(
                    error_code_prefix="AH49",
                    error_message=f"Package version condition issue (importlib_metadata not installed)",  # noqa
                )

        return None
