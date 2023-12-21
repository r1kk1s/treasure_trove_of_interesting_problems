class RequestsAPIError(Exception):
    """Program can't get data from API"""


class RenameFileError(Exception):
    """Program can't rename file"""


class WriteFileError(Exception):
    """Program can't write file"""


def handle_exception(exception: type[Exception]):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                print(e.__doc__)
                exit(1)

        return wrapper

    return decorator
