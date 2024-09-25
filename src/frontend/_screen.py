from termcolor import colored

from .enums import ColorRules


class BaseScreen:
    def __init__(self):
        pass

    def run(self):
        pass

    def _input_int(self, text: str) -> int | None:
        try:
            return int(input(colored(text, ColorRules.INPUT.value)))
        except ValueError:
            return None

    def _input_str(self, text: str) -> str | None:
        try:
            input_value = input(colored(text, ColorRules.INPUT.value))
            if input_value:
                return input_value
            return None
        except ValueError:
            return None

    def _print_text(self, text: str):
        print(text)

    def _print_error(self, text: str):
        print(colored(text, ColorRules.ERROR.value))

    def _print_success(self, text: str):
        print(colored(text, ColorRules.SUCCESS.value))

    def _print_warning(self, text: str):
        print(colored(text, ColorRules.WARNING.value))
