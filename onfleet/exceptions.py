class OnfleetException(Exception):
    pass


class OnfleetDuplicateKeyException(OnfleetException):
    pass


class OnfleetGeocodingError(OnfleetException):
    pass
