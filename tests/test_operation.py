import pytest

from src.repositories import BankOperationRepository


@pytest.fixture
def bank_operation_repo_fixture():
    bank_operation_repo = BankOperationRepository()
    bank_operation_repo.topup(1, 100)
    bank_operation_repo.topup(1, 200)
    return bank_operation_repo


class TestBankOperationRepository:
    def test_topup(self, bank_operation_repo_fixture):
        topup = bank_operation_repo_fixture.topup(1, 100)
        assert topup.user_id == 1
        assert topup.amount == 100
        assert topup.operation_type.value == 'topup'

    def test_error_topup(self, bank_operation_repo_fixture):
        with pytest.raises(ValueError):
            bank_operation_repo_fixture.topup(1, -100)

    def test_withdraw(self, bank_operation_repo_fixture):
        withdraw = bank_operation_repo_fixture.withdraw(1, 100)
        assert withdraw.user_id == 1
        assert withdraw.amount == 100
        assert withdraw.operation_type.value == 'withdraw'

    def test_error_withdraw(self, bank_operation_repo_fixture):
        with pytest.raises(ValueError):
            bank_operation_repo_fixture.topup(1, -100)

    def test_balance(self, bank_operation_repo_fixture):
        balance = bank_operation_repo_fixture.balance(1)
        assert balance == 300

    def test_withdraw_more_than_balance(self, bank_operation_repo_fixture):
        with pytest.raises(ValueError):
            bank_operation_repo_fixture.withdraw(1, 400)

    def test_get_by_user_id(self, bank_operation_repo_fixture):
        operations = bank_operation_repo_fixture.get_by_user_id(1)
        assert len(operations) == 2
