from src.core.bank_operation import BankOperation
from src.exceptions import handler_exception

from .repository import IBankOperationRepository


class BankService:
    def __init__(self, bank_repo: IBankOperationRepository):
        self.bank_repo = bank_repo

    @handler_exception
    def topup(self, user_id: int, amount: int) -> BankOperation:
        return self.bank_repo.topup(user_id, amount)

    @handler_exception
    def withdraw(self, user_id: int, amount: int) -> BankOperation:
        return self.bank_repo.withdraw(user_id, amount)

    @handler_exception
    def balance(self, user_id: int) -> int:
        return self.bank_repo.balance(user_id)

    @handler_exception
    def get_by_user_id(self, user_id: int) -> list[BankOperation]:
        return self.bank_repo.get_by_user_id(user_id)
