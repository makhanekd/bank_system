from src.core.bank_operation import BankService
from src.providers import container_factory

from .response import ErrorResponse, Response, SuccessResponse


def bank_service_fabric():
    with container_factory() as container:
        return container.get(BankService)


class BankController:
    def __init__(self):
        self.service = bank_service_fabric()

    def topup(self, user_id: int, amount: int) -> Response:
        operation, error = self.service.topup(user_id, amount)

        if error:
            return ErrorResponse(f'Ошибка при пополнении счета {error}')

        return SuccessResponse(f'Счет пополнен на {amount}', operation)

    def withdraw(self, user_id: int, amount: int) -> Response:
        operation, error = self.service.withdraw(user_id, amount)

        if error:
            return ErrorResponse(f'Ошибка при пополнении счета {error}')

        return SuccessResponse(f'Счет списан на {amount}', operation)

    def get_balance(self, user_id: int) -> Response:
        balance, error = self.service.get_balance_by_user_id(user_id)

        if error:
            return ErrorResponse(str(error))

        return SuccessResponse(f'Баланс: {balance} руб.', balance)

    def get_history(self, user_id: int) -> Response:
        history, error = self.service.get_operations_by_user_id(user_id)

        if error:
            return ErrorResponse(str(error))

        return SuccessResponse('История операций:', history)
