from src.core.user import IUserRepository, User
from src.exceptions import BaseException


class UserRepository(IUserRepository):
    def __init__(self):
        self.users: list[User] = []
        self.last_user_id: int = -1

    def register(self, username: str, password: str) -> User:
        user = User(self.last_user_id + 1, username, password)

        if not user.check_min_length_username:
            raise BaseException('\nЛогин должен содержать не менее 3 символов!!!')

        if not user.check_min_length_password:
            raise BaseException('\nПароль должен содержать не менее 8 символов!!!')

        if user.username in [user.username for user in self.users]:
            raise BaseException('\nЛогин уже занят!!!')

        self.users.append(user)
        self.last_user_id = user.id
        return user

    def authenticate(self, username: str, password: str) -> User:
        for user in self.users:
            if user.username == username and user.password == password:
                return user

        raise BaseException('\nНеверный логин или пароль!!!')
