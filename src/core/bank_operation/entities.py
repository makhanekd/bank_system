from dataclasses import dataclass
from enum import Enum


class OperationType(Enum):
    TOPUP = 'topup'
    WITHDRAW = 'withdraw'


@dataclass
class BankOperation:
    user_id: int
    amount: int
    operation_type: OperationType
    operation_at: str

    @property
    def check_amount(self):
        return self.amount > 0
