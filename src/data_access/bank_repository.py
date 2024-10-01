from datetime import datetime

from src.core.bank_operation import (
    BankOperation,
    BankOperationInputDTO,
    BaseBankException,
    IBankOperationRepository,
    OperationType,
)
from src.core.user import (
    BaseUserException,
)

from .exceptions import handler_exception


class BankOperationRepository(IBankOperationRepository):
    def __init__(self):
        self.bank_operations: list[BankOperation] = []

    @handler_exception
    def topup(self, dto: BankOperationInputDTO) -> tuple[BankOperation | None, BaseBankException | None]:
        bank_operation = BankOperation(dto.user_id, dto.amount, dto.operation_type, dto.operation_at)
        self.bank_operations.append(bank_operation)
        return bank_operation, None

    @handler_exception
    def withdraw(self, user_id: int, amount: int) -> tuple[BankOperation | None, BaseBankException | None]:
        bank_operation = BankOperation(
            user_id, amount, OperationType.WITHDRAW, datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        self.bank_operations.append(bank_operation)
        return bank_operation, None

    @handler_exception
    def get_balance(self, user_id: int) -> tuple[int | None, BaseUserException | None]:
        balance = 0
        for bank_operation in self.bank_operations:
            if bank_operation.user_id == user_id:
                if bank_operation.operation_type == OperationType.TOPUP:
                    balance += bank_operation.amount
                elif bank_operation.operation_type == OperationType.WITHDRAW:
                    balance -= bank_operation.amount
        return balance, None

    @handler_exception
    def get_operations_by_user_id(self, user_id: int) -> tuple[list[BankOperation] | None, BaseBankException | None]:
        return [bank_operation for bank_operation in self.bank_operations if bank_operation.user_id == user_id], None
