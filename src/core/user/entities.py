from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    username: str
    password: str

    @property
    def check_min_length_password(self):
        return len(self.password) >= 8

    @property
    def check_min_length_username(self):
        return len(self.username) >= 3
