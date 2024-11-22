class BaseException(Exception):
    def __init__(self, *args, message: str | None = None):
        self.message = message
        super().__init__(*args)


class InvalidMethodType(BaseException):
    """
    Exception raised when and invalid method type is passed to the  TMDBApi class methods

    Attributes:
        `message` -- A readable error message that can be passed to the frontend or in the terminal
    """

    def __init__(self, message: str | None = "Invalid method type."):
        self.message = message
        super().__init__(self.message)
