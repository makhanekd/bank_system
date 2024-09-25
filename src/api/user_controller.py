from src.core.user import UserService
from src.data_access import UserRepository

from .response import ErrorResponse, Response, SuccessResponse


def user_service_fabric():
    return UserService(UserRepository())


class UserController:
    def __init__(self):
        self.service = user_service_fabric()

    def register(self, username: str, password: str) -> Response:
        user = self.service.register(username, password)
        if user:
            return SuccessResponse('Пользователь зарегистрирован', user)
        else:
            return ErrorResponse('Ошибка при регистрации')

    def authenticate(self, username: str, password: str) -> Response:
        user = self.service.authenticate(username, password)
        if user:
            return SuccessResponse('Авторизация прошла успешно', user)
        else:
            return ErrorResponse('Неверный логин или пароль')
