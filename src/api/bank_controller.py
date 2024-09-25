from src.core.bank_operation import BankService
from src.data_access import BankOperationRepository

from .response import ErrorResponse, Response, SuccessResponse


def bank_service_fabric():
    return BankService(BankOperationRepository())


class BankController:
    def __init__(self):
        self.service = bank_service_fabric()

    def topup(self, user_id: int, amount: int) -> Response:
        operation = self.service.topup(user_id, amount)
        if not operation:
            return ErrorResponse('Ошибка при пополнении счета')
        return SuccessResponse(f'Счет пополнен на {amount}', operation)

    def withdraw(self, user_id: int, amount: int) -> Response:
        operation = self.service.withdraw(user_id, amount)
        if not operation:
            return ErrorResponse('Ошибка при пополнении счета')
        return SuccessResponse(f'Счет списан на {amount}', operation)

    def get_balance(self, user_id: int) -> Response:
        balance = self.service.balance(user_id)

        return SuccessResponse(f'Баланс: {balance} руб.', balance)

    def get_history(self, user_id: int) -> Response:
        history = self.service.get_by_user_id(user_id)

        return SuccessResponse('История операций:', history)
