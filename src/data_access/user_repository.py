from src.core.user import (
    BaseUserException,
    IUserRepository,
    User,
    UserAuthenticationException,
    UserInputDTO,
)

from .exceptions import handler_exception


class UserRepository(IUserRepository):
    def __init__(self):
        self.users: list[User] = []
        self.last_user_id: int = -1

    @handler_exception
    def register(self, dto: UserInputDTO) -> tuple[User | None, BaseUserException | None]:
        user = User(self.last_user_id + 1, dto.username, dto.password)

        self.users.append(user)
        self.last_user_id = user.id
        return user, None

    @handler_exception
    def authenticate(self, dto: UserInputDTO) -> tuple[User | None, BaseUserException | None]:
        for user in self.users:
            if user.username == dto.username and user.password == dto.password:
                return user, None

        return None, UserAuthenticationException('\nНеверный логин или пароль!!!')

    @handler_exception
    def get_users(self) -> tuple[list[User] | None, BaseUserException | None]:
        return self.users, None
