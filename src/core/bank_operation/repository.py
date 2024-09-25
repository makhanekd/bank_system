from abc import ABC, abstractmethod

from .entities import BankOperation


class IBankOperationRepository(ABC):
    @abstractmethod
    def topup(self, user_id: int, amount: int) -> BankOperation:
        raise NotImplementedError

    @abstractmethod
    def withdraw(self, user_id: int, amount: int) -> BankOperation:
        raise NotImplementedError

    @abstractmethod
    def balance(self, user_id: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> list[BankOperation]:
        raise NotImplementedError
