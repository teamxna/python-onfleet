import re

options_re = re.compile(r'"(.*?)"')


def parse_options(self):
    """Parse the onfleet string for the proposed options."""
    return options_re.findall(self.cause)


class OnfleetError(Exception):
    """Generic error encountered with onfleet."""

    def __init__(self, message, type, code, cause, *args):
        self.message = message
        self.type = type
        self.code = code
        self.cause = cause
        super(OnfleetError, self).__init__(message, *args)


class MultipleDestinationsError(OnfleetError):
    """Error for when the API returns multiple destination options."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        super(MultipleDestinationsError, self).__init__(*args, **kwargs)
