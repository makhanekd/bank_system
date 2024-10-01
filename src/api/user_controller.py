from src.core.user import UserInputDTO, UserService
from src.data_access import UserRepository

from .response import ErrorResponse, Response, SuccessResponse


def user_service_fabric():
    return UserService(UserRepository())


class UserController:
    def __init__(self):
        self.service = user_service_fabric()

    def register(self, username: str, password: str) -> Response:
        user, error = self.service.register(UserInputDTO(username, password))

        if user:
            return SuccessResponse('Пользователь зарегистрирован', user)

        return ErrorResponse(f'Ошибка при регистрации: {error}')

    def authenticate(self, username: str, password: str) -> Response:
        user, error = self.service.authenticate(UserInputDTO(username, password))

        if user:
            return SuccessResponse('Авторизация прошла успешно', user)

        return ErrorResponse(f'Неверный логин или пароль: {error}')
