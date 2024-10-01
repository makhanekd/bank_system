from termcolor import colored


class ApplicationException(Exception):
    pass


def handler_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApplicationException as e:
            print(colored(e, 'red'))

    return wrapper
