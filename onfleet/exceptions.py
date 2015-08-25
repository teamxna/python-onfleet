class OnfleetError(Exception):
    """Generic error encountered with onfleet."""

    def __init__(self, message, type, code, cause, *args):
        self.message = message
        self.type = type
        self.code = code
        self.cause = cause
        super(OnfleetError, self).__init__(message, *args)
