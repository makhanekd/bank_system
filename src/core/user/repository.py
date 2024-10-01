from abc import ABC, abstractmethod

from .entities import User, UserInputDTO
from .exceptions import (
    BaseUserException,
)


class IUserRepository(ABC):
    @abstractmethod
    def register(self, user: UserInputDTO) -> tuple[User | None, BaseUserException | None]:
        raise NotImplementedError

    @abstractmethod
    def authenticate(self, user: UserInputDTO) -> tuple[User | None, BaseUserException | None]:
        raise NotImplementedError

    @abstractmethod
    def get_users(self) -> tuple[list[User] | None, BaseUserException | None]:
        raise NotImplementedError
