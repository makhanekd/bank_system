from dataclasses import dataclass
from typing import Any


@dataclass
class Session:
    is_active: bool = True
    is_authicated: bool = False
    user_id: int = -1

    def __setattr__(self, name: str, value: Any) -> None:
        if name == 'user_id':
            self.is_authicated = value > -1
        super().__setattr__(name, value)
