import pytest

from src.repositories import UserRepository


@pytest.fixture
def user_repo_fixture():
    user_repo = UserRepository()
    user_repo.register('test_user0', 'test_password0')
    return user_repo


class TestUserRepository:
    def test_register_user(self):
        user_repo = UserRepository()
        user = user_repo.register('test_user1', 'test_password1')

        assert user.username == 'test_user1'
        assert user.password == 'test_password1'

    def test_register_duplicate_username(self, user_repo_fixture):
        user = user_repo_fixture.users[0]

        with pytest.raises(ValueError):
            user_repo_fixture.register(user.username, 'test_password2')

    def test_min_length_username(self, user_repo_fixture):
        with pytest.raises(ValueError):
            user_repo_fixture.register('te', 'test_password3')

    def test_min_length_password(self, user_repo_fixture):
        with pytest.raises(ValueError):
            user_repo_fixture.register('test_user4', 'test')

    def test_authenticate_user(self, user_repo_fixture):
        user = user_repo_fixture.authenticate('test_user0', 'test_password0')

        assert user.username == 'test_user0'
        assert user.password == 'test_password0'

    def test_failed_authenticate_user(self, user_repo_fixture):
        with pytest.raises(ValueError):
            user_repo_fixture.authenticate('test_user0', 'test_password1')
