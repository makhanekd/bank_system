from .entities import User, UserInputDTO
from .exceptions import (
    BaseUserException,
    UserAlreadyExistsException,
    UserPasswordLengthException,
    UserUsernameLengthException,
)
from .repository import IUserRepository

ReturnUser = tuple[User | None, BaseUserException | None]


class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def register(self, dto: UserInputDTO) -> ReturnUser:
        if not dto.check_min_length_password:
            return None, UserPasswordLengthException()
        if not dto.check_min_length_username:
            return None, UserUsernameLengthException()

        users, error = self.get_users()
        if error:
            return None, error

        if users and dto.username in [user.username for user in users]:
            return None, UserAlreadyExistsException()

        return self.user_repo.register(dto)

    def authenticate(self, user: UserInputDTO) -> ReturnUser:
        return self.user_repo.authenticate(user)

    def get_users(self) -> tuple[list[User] | None, BaseUserException | None]:
        return self.user_repo.get_users()
