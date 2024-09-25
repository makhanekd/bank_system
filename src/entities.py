from dataclasses import dataclass
from enum import Enum


class OperationType(Enum):
    TOPUP = 'topup'
    WITHDRAW = 'withdraw'


@dataclass(frozen=True)
class User:
    id: int
    username: str
    password: str

    @property
    def check_min_length_password(self):
        return len(self.password) >= 8

    @property
    def check_min_length_username(self):
        return len(self.username) >= 3


@dataclass
class BankOperation:
    user_id: int
    amount: float
    operation_type: OperationType
    operation_at: str

    @property
    def check_amount(self):
        return self.amount > 0
