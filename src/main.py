from src.api import BankController, UserController
from src.entities import Session
from src.frontend import AuthenticatedScreen, WelcomeScreen


class FrontendHandler:
    def __init__(self):
        self.session = Session()
        self.welcome_screen = WelcomeScreen(self.session, UserController())
        self.authenticated_screen = AuthenticatedScreen(self.session, BankController())

    def main(self):
        while self.session.is_active:
            self.welcome_screen.run()
            while self.session.is_authicated:
                self.authenticated_screen.run()


def main():
    front_handler = FrontendHandler()
    front_handler.main()


if __name__ == '__main__':
    main()
