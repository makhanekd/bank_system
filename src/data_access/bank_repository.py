from datetime import datetime

from src.core.bank_operation import BankOperation, IBankOperationRepository, OperationType
from src.exceptions import BaseException


class BankOperationRepository(IBankOperationRepository):
    def __init__(self):
        self.bank_operations: list[BankOperation] = []

    def topup(self, user_id: int, amount: int) -> BankOperation:
        bank_operation = BankOperation(
            user_id, amount, OperationType.TOPUP, datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        if not bank_operation.check_amount:
            raise BaseException('\nСумма должна быть больше нуля!!!')

        self.bank_operations.append(bank_operation)
        return bank_operation

    def withdraw(self, user_id: int, amount: int) -> BankOperation:
        bank_operation = BankOperation(
            user_id, amount, OperationType.WITHDRAW, datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        if not bank_operation.check_amount:
            raise BaseException('\nСумма должна быть больше нуля!!!')

        if self.balance(user_id) < amount:
            raise BaseException('\nНедостаточно средств!!!')

        self.bank_operations.append(bank_operation)
        return bank_operation

    def balance(self, user_id: int) -> int:
        balance = 0
        for bank_operation in self.bank_operations:
            if bank_operation.user_id == user_id:
                if bank_operation.operation_type == OperationType.TOPUP:
                    balance += bank_operation.amount
                elif bank_operation.operation_type == OperationType.WITHDRAW:
                    balance -= bank_operation.amount
        return balance

    def get_by_user_id(self, user_id: int) -> list[BankOperation]:
        return [bank_operation for bank_operation in self.bank_operations if bank_operation.user_id == user_id]
