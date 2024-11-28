
from .exceptions import AppError


class Result:
    error: AppError | None = None
    exit_code: int = 0
    output: str = ""

    def __init__(
        self,
        output: str = "",
        exit_code: int = 0,
        error: AppError | None = None,
    ) -> None:
        self.error = error
        self.exit_code = exit_code
        self.output = output
