from api.logger import get_logger
import logging

# Create a logger for exceptions
logger = get_logger("Errors", "error.log")


class BaseException(Exception):
    """
    Base class for custom exceptions with logging functionality.

    Attributes:
        message -- A readable error message.
        logger -- The logger instance used to log the error.
    """

    def __init__(self, message: str | None = "An error occurred."):
        self.message = message
        self.logger = logger
        # Log the exception message
        self.logger.exception(self.message)
        super().__init__(self.message)


class InvalidMethodType(BaseException):
    """
    Exception raised when an invalid method type is passed to the TMDBApi class methods.

    Attributes:
        message -- A readable error message that can be passed to the frontend or in the terminal.
    """

    def __init__(self, message: str | None = "Invalid method type."):
        super().__init__(message)


class NoLogExtension(BaseException):
    """
    Exception raised when there is no `.log` extension passed to a file name when calling the `get_logger` function.

    Attributes:
        message -- A readable error message that can be passed to the frontend or in the terminal.
    """

    def __init__(
        self,
        message: str | None = "The `.log` extension was not passed for the log file.",
    ):
        super().__init__(message)
