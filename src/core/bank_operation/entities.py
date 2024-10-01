from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class OperationType(Enum):
    TOPUP = 'topup'
    WITHDRAW = 'withdraw'


@dataclass
class BankOperationInputDTO:
    user_id: int
    amount: int
    operation_type: OperationType
    operation_at: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @property
    def check_amount(self):
        return self.amount > 0


@dataclass
class BankOperation:
    user_id: int
    amount: int
    operation_type: OperationType
    operation_at: str
