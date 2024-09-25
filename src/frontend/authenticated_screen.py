from src.api import BankController
from src.core.bank_operation import OperationType
from src.entities import Session

from ._screen import BaseScreen
from .enums import CommandsAccount


class AuthenticatedScreen(BaseScreen):
    def __init__(self, session: Session, bank_controller: BankController):
        self.session = session
        self.bank_controller = bank_controller

    def run(self):
        self._print_text(
            '\n1. Пополнить счет\n2. Снять деньги\n3. Посмотреть баланс\n4. Посмотреть историю операций\n5. Выход'
        )

        command = self._input_int('\nВыберите действие: ')

        match command:
            case CommandsAccount.TOPUP.value:
                self._topup(self.session.user_id)
            case CommandsAccount.WITHDRAW.value:
                self._withdraw(self.session.user_id)
            case CommandsAccount.BALANCE.value:
                self._balance(self.session.user_id)
            case CommandsAccount.HISTORY.value:
                self._history(self.session.user_id)
            case CommandsAccount.EXIT.value:
                self.session.user_id = -1
            case _:
                self._print_error('\nНеверная команда!!!')

    def _topup(self, user_id: int):
        amount = self._input_int('\nВведите сумму: ')

        if not amount:
            self._print_error('\nСумма должна быть больше нуля!!!')
            return

        response = self.bank_controller.topup(user_id, amount)
        if response.is_success:
            self._print_success('\nСчет пополнен!')

    def _withdraw(self, user_id: int):
        amount = self._input_int('\nВведите сумму: ')

        if not amount:
            self._print_error('\nСумма должна быть больше нуля!!!')
            return

        response = self.bank_controller.withdraw(user_id, amount)

        if response.is_success:
            self._print_success('\nСчет списан!')

    def _balance(self, user_id: int):
        response = self.bank_controller.get_balance(user_id)

        if response.is_success:
            balance = response.data
            self._print_success(f'\nБаланс: {balance} руб.')

    def _history(self, user_id: int):
        response = self.bank_controller.get_history(user_id)

        if not response.is_success:
            self._print_error('Ошибка при получении истории операций')
            return

        operations = response.data
        self._print_success('\nИстория операций:')
        if not operations:
            self._print_success('Нет операций')
            return

        for operation in operations:
            if operation.operation_type == OperationType.TOPUP:
                self._print_success(f'*   Пополнение счета на {operation.amount} руб.')
            elif operation.operation_type == OperationType.WITHDRAW:
                self._print_warning(f'*   Снятие со счета на: {operation.amount} руб.')
