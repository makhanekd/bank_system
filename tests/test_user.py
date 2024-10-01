from unittest.mock import Mock

import pytest

from src.core.user.entities import UserInputDTO
from src.core.user.service import UserService
from src.data_access.user_repository import UserRepository


@pytest.fixture
def user_service_fixture():
    user_repo = UserRepository()
    user_repo.register(UserInputDTO('test_user0', 'test_password0'))
    user_service = UserService(user_repo)
    return user_service


class TestUserRepository:
    def test_register_user(self):
        user_service = UserService(UserRepository())
        user, error = user_service.register(UserInputDTO('test_user0', 'test_password0'))

        assert error is None
        assert user is not None
        assert user.username == 'test_user0'
        assert user.password == 'test_password0'

    def test_register_duplicate_username(self, user_service_fixture):
        users, error = user_service_fixture.get_users()
        user_mock = users[0]

        user, error = user_service_fixture.register(UserInputDTO(user_mock.username, 'test_password2'))

        assert error is not None
        assert user is None

    def test_min_length_username(self, user_service_fixture):
        user, error = user_service_fixture.register(UserInputDTO('te', 'test_password3'))

        assert error is not None
        assert user is None

    def test_min_length_password(self, user_service_fixture):
        user, error = user_service_fixture.register(UserInputDTO('test_user4', 'test'))

        assert error is not None
        assert user is None

    def test_authenticate_user(self, user_service_fixture):
        user, error = user_service_fixture.authenticate(UserInputDTO('test_user0', 'test_password0'))

        assert error is None
        assert user is not None
        assert user.username == 'test_user0'
        assert user.password == 'test_password0'

    def test_failed_authenticate_user(self, user_service_fixture):
        user, error = user_service_fixture.authenticate(UserInputDTO('test_user0', 'test_password1'))

        assert error is not None
        assert user is None
