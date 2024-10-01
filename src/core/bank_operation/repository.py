from abc import ABC, abstractmethod

from .entities import BankOperation, BankOperationInputDTO
from .exceptions import BaseBankException


class IBankOperationRepository(ABC):
    @abstractmethod
    def topup(self, operation: BankOperationInputDTO) -> tuple[BankOperation | None, BaseBankException | None]:
        raise NotImplementedError

    @abstractmethod
    def withdraw(self, operation: BankOperationInputDTO) -> tuple[BankOperation | None, BaseBankException | None]:
        raise NotImplementedError

    @abstractmethod
    def get_balance(self, user_id: int) -> tuple[int | None, BaseBankException | None]:
        raise NotImplementedError

    @abstractmethod
    def get_operations_by_user_id(self, user_id: int) -> tuple[list[BankOperation] | None, BaseBankException | None]:
        raise NotImplementedError
