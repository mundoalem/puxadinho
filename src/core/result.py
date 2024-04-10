from typing import Optional

from .exceptions import AppError


class Result:
    error: Optional[AppError] = None
    exit_code: int = 0
    output: str = ""

    def __init__(
        self,
        output: str = "",
        exit_code: int = 0,
        error: Optional[AppError] = None,
    ) -> None:
        self.error = error
        self.exit_code = exit_code
        self.output = output
