from abc import ABC, abstractmethod

from .entities import User


class IUserRepository(ABC):
    @abstractmethod
    def register(self, username: str, password: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def authenticate(self, username: str, password: str) -> User:
        raise NotImplementedError
