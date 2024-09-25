from src.api import UserController
from src.entities import Session

from ._screen import BaseScreen
from .enums import Commands


class WelcomeScreen(BaseScreen):
    def __init__(self, session: Session, user_controller: UserController):
        self.session = session
        self.user_controller = user_controller

    def run(self):
        self._print_text('\nДобро пожаловать в банковскую систему!')
        self._print_text('\n1. Регистрация\n2. Авторизация \n3. Выход')

        command = self._input_int('\nВыберите действие: ')

        match command:
            case Commands.REGISTER.value:
                self._register_screen()
            case Commands.LOGIN.value:
                self._authenticate_screen()
            case Commands.EXIT.value:
                self.session.is_active = False
            case _:
                self._print_error('\nНеверная команда!!!')

    def _register_screen(self):
        username = self._input_str('\nВведите логин: ')
        password = self._input_str('Введите пароль: ')

        if not username or not password:
            self._print_error('\nЛогин и пароль обязательны!!!')
            return

        response = self.user_controller.register(username, password)
        if response.is_success and response.data:
            self._print_success(f'\nПользователь зарегистрирован, {response.data.username}!')

    def _authenticate_screen(self):
        username = self._input_str('\nВведите логин: ')
        password = self._input_str('Введите пароль: ')

        if not username or not password:
            self._print_error('\nЛогин и пароль обязательны!!!')
            return

        response = self.user_controller.authenticate(username, password)
        if response.is_success and response.data:
            user = response.data
            self.session.user_id = user.id
            self._print_success(f'\nАвторизация успешна, {user.username}!')
