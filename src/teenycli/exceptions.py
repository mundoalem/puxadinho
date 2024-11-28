class AppError(Exception):
    """Raised when a generic application error happens."""


class NotFoundError(AppError):
    """Raised when a required information is not found."""
