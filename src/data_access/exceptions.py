from termcolor import colored

from src.core.base_exceptions import CoreException


class RepositoryException(CoreException):
    def __init__(self, message: str = '/nОшибка при работе с репозиториями!!!'):
        super().__init__(message)


def handler_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(colored(e, 'red'))
            return None, RepositoryException(str(e))

    return wrapper
