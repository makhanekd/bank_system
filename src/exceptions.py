class BaseException(ValueError):
    pass


def handler_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException as e:
            print(e)

    return wrapper
