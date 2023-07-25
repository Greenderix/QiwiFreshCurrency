class IncorrectDateError(Exception):
    def __init__(self, message):
        super().__init__(message)


class IncorrectCodeError(Exception):
    def __init__(self, message):
        super().__init__(message)
