from src.core import CoreException


class BaseBankException(CoreException):
    def __init__(self, message: str = '/nОшбка при работе с банковскими операциями!!!'):
        super().__init__(message)
