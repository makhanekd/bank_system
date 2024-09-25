from enum import Enum


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


class ColorRules(str, Enum):
    ERROR = 'red'
    SUCCESS = 'green'
    INPUT = 'blue'
    WARNING = 'yellow'
