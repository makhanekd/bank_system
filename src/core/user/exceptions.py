from src.core import CoreException


class BaseUserException(CoreException):
    def __init__(self, message: str = '/nОшибка при работе с пользователями!!!'):
        super().__init__(message)


class UserAlreadyExistsException(BaseUserException):
    def __init__(self, message: str = '/nПользователь уже существует!!!'):
        super().__init__(message)


class UserNotFoundException(BaseUserException):
    def __init__(self, message: str = '/nПользователь не найден!!!'):
        super().__init__(message)


class UserAuthenticationException(BaseUserException):
    def __init__(self, message: str = '/nНеверный логин или пароль!!!'):
        super().__init__(message)


class UserRegistrationException(BaseUserException):
    def __init__(self, message: str = '/nНеверно заданы логин или пароль!!!'):
        super().__init__(message)


class UserPasswordLengthException(BaseUserException):
    def __init__(self, message: str = '/nПароль должен содержать не менее 8 символов!!!'):
        super().__init__(message)


class UserUsernameLengthException(BaseUserException):
    def __init__(self, message: str = '/nЛогин должен содержать не менее 3 символов!!!'):
        super().__init__(message)
