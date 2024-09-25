from abc import ABC, abstractmethod
from datetime import datetime

from src.entities import BankOperation, OperationType, User
from src.exceptions import BaseException


class IUserRepository(ABC):
    @abstractmethod
    def register(self, username: str, password: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def authenticate(self, username: str, password: str) -> User:
        raise NotImplementedError


class UserRepository(IUserRepository):
    def __init__(self):
        self.users: list[User] = []
        self.last_user_id: int = -1

    def register(self, username: str, password: str) -> User:
        user = User(self.last_user_id + 1, username, password)

        if not user.check_min_length_username:
            raise BaseException('\nЛогин должен содержать не менее 3 символов')

        if not user.check_min_length_password:
            raise BaseException('\nПароль должен содержать не менее 8 символов')

        if user.username in [user.username for user in self.users]:
            raise BaseException('\nЛогин уже занят')

        self.users.append(user)
        self.last_user_id = user.id
        return user

    def authenticate(self, username: str, password: str) -> User:
        for user in self.users:
            if user.username == username and user.password == password:
                return user

        raise BaseException('\nНеверный логин или пароль')


class IBankOperationRepository(ABC):
    @abstractmethod
    def topup(self, user_id: int, amount: float) -> BankOperation:
        raise NotImplementedError

    @abstractmethod
    def withdraw(self, user_id: int, amount: float) -> BankOperation:
        raise NotImplementedError

    @abstractmethod
    def balance(self, user_id: int) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> list[BankOperation]:
        raise NotImplementedError


class BankOperationRepository(IBankOperationRepository):
    def __init__(self):
        self.bank_operations: list[BankOperation] = []

    def topup(self, user_id: int, amount: float) -> BankOperation:
        bank_operation = BankOperation(
            user_id, amount, OperationType.TOPUP, datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        if not bank_operation.check_amount:
            raise BaseException('\nСумма должна быть больше нуля')

        self.bank_operations.append(bank_operation)
        return bank_operation

    def withdraw(self, user_id: int, amount: float) -> BankOperation:
        bank_operation = BankOperation(
            user_id, amount, OperationType.WITHDRAW, datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        if not bank_operation.check_amount:
            raise BaseException('\nСумма должна быть больше нуля')

        if self.balance(user_id) < amount:
            raise BaseException('\nНедостаточно средств')

        self.bank_operations.append(bank_operation)
        return bank_operation

    def balance(self, user_id: int) -> float:
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
