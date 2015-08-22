class OnfleetException(Exception):
    pass


class OnfleetDuplicateKeyException(OnfleetException):
    pass


class OnfleetGeocodingException(OnfleetException):
    pass
