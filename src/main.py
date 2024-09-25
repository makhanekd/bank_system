from enum import Enum

from src.entities import OperationType
from src.exceptions import handler_exception
from src.repositories import BankOperationRepository, IBankOperationRepository, IUserRepository, UserRepository


class Commands(Enum):
    REGISTER = 1
    LOGIN = 2
    EXIT = 3


class CommandsAccount(Enum):
    TOPUP = 1
    WITHDRAW = 2
    BALANCE = 3
    HISTORY = 4
    EXIT = 5


class Controller:
    def __init__(self, user_repo: IUserRepository, bank_repo: IBankOperationRepository):
        self.is_session_exist: bool = True
        self.is_authenticated: bool = False
        self.auth_user_id: int = -1
        self.user_repo: IUserRepository = user_repo
        self.bank_repo: IBankOperationRepository = bank_repo

    def main(self):
        while self.is_session_exist:
            self.run_welcome_screen()
            while self.is_authenticated:
                self.run_authenticated_screen()

    def run_welcome_screen(self):
        print('\nДобро пожаловать в банковскую систему!')
        print('\n1. Регистрация\n2. Авторизация \n3. Выход')

        command = int(input('\nВыберите действие: '))

        if command == Commands.REGISTER.value:
            self._register_user()
        elif command == Commands.LOGIN.value:
            self._authenticate_user()
        elif command == Commands.EXIT.value:
            self.is_session_exist = False
        else:
            print('\nНеверная команда!!!')

    @handler_exception
    def _register_user(self):
        login = input('\nВведите логин: ')
        password = input('Введите пароль: ')

        user = self.user_repo.register(login, password)

        print(f'\nПользователь зарегистрирован, {user.username}!')

    @handler_exception
    def _authenticate_user(self):
        login = input('\nВведите логин: ')
        password = input('Введите пароль: ')

        user = self.user_repo.authenticate(login, password)
        print(f'\nАвторизация успешна, {user.username}!')

        self.is_authenticated = True
        self.auth_user_id = user.id

    def run_authenticated_screen(self):
        print('\n1. Пополнить счет\n2. Снять деньги\n3. Посмотреть баланс\n4. Посмотреть историю операций\n5. Выход')

        command = int(input('\nВыберите действие: '))

        if command == CommandsAccount.TOPUP.value:
            self.topup()
        elif command == CommandsAccount.WITHDRAW.value:
            self.withdraw()
        elif command == CommandsAccount.BALANCE.value:
            self.balance()
        elif command == CommandsAccount.HISTORY.value:
            self.history()
        elif command == CommandsAccount.EXIT.value:
            self.is_authenticated = False
        else:
            print('\nНеверная команда!!!')

    @handler_exception
    def topup(self):
        amount = int(input('\nВведите сумму: '))

        self.bank_repo.topup(self.auth_user_id, amount)

        print('\nСчет пополнен!')

    @handler_exception
    def withdraw(self):
        amount = int(input('\nВведите сумму: '))

        self.bank_repo.withdraw(self.auth_user_id, amount)

        print('\nСчет снят!')

    @handler_exception
    def balance(self):
        balance = self.bank_repo.balance(self.auth_user_id)

        print(f'\nВаш баланс: {balance}')

    def history(self):
        print('\nИстория операций:')

        operations = self.bank_repo.get_by_user_id(self.auth_user_id)
        if not operations:
            print('Нет операций')
            return

        for operation in operations:
            if operation.operation_type == OperationType.TOPUP:
                print(f'*   Пополнение счета на {operation.amount}')
            elif operation.operation_type == OperationType.WITHDRAW:
                print(f'*   Снятие со счета на: {operation.amount}')


def main():
    user_repo = UserRepository()
    bank_repo = BankOperationRepository()
    controller = Controller(user_repo, bank_repo)
    controller.main()


if __name__ == '__main__':
    main()
