from .entities import BankOperation, BankOperationInputDTO, OperationType
from .exceptions import BaseBankException
from .repository import IBankOperationRepository


class BankService:
    def __init__(self, bank_repo: IBankOperationRepository):
        self.bank_repo = bank_repo

    def topup(self, user_id: int, amount: int) -> tuple[BankOperation | None, BaseBankException | None]:
        operation = BankOperationInputDTO(user_id, amount, OperationType.TOPUP)

        if not operation.check_amount:
            return None, BaseBankException('Сумма должна быть больше нуля!!!')

        return self.bank_repo.topup(operation)

    def withdraw(self, user_id: int, amount: int) -> tuple[BankOperation | None, BaseBankException | None]:
        operation = BankOperationInputDTO(user_id, amount, OperationType.WITHDRAW)

        if not operation.check_amount:
            return None, BaseBankException('Сумма должна быть больше нуля!!!')

        balance, error = self.get_balance_by_user_id(user_id)

        if error or not balance:
            return None, error

        if balance < amount:
            return None, BaseBankException('Недостаточно средств!!!')

        return self.bank_repo.withdraw(operation)

    def get_balance_by_user_id(self, user_id: int) -> tuple[int | None, BaseBankException | None]:
        return self.bank_repo.get_balance(user_id)

    def get_operations_by_user_id(self, user_id: int) -> tuple[list[BankOperation] | None, BaseBankException | None]:
        return self.bank_repo.get_operations_by_user_id(user_id)
