from src.exceptions import handler_exception

from .repository import IUserRepository


class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    @handler_exception
    def register(self, username: str, password: str):
        return self.user_repo.register(username, password)

    @handler_exception
    def authenticate(self, username: str, password: str):
        return self.user_repo.authenticate(username, password)
