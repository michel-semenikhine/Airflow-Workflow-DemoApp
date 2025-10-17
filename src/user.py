# src/user.py
from src.utils import is_valid_email, hash_password

class User:
    """
    Represents a simple user with an hashed email & password.
    """
    def __init__(self, email: str, password: str):
        if not is_valid_email(email):
            raise ValueError("Invalid email address.")
        if not password:
            raise ValueError("The password cannot be empty.")

        self.email = email
        self.hashed_password = hash_password(password)

    def __repr__(self):
        return f"<User {self.email}>"

class UserDatabase:
    """
    Simulates a user database in memory.
    """
    def __init__(self):
        self._users = {}

    def add_user(self, email: str, password: str) -> User:
        if email in self._users:
            raise ValueError("User already existing.")
        user = User(email, password)
        self._users[email] = user
        return user

    def remove_user(self, email: str) -> bool:
        return self._users.pop(email, None) is not None

    def get_user(self, email: str) -> User | None:
        return self._users.get(email)

    def count(self) -> int:
        return len(self._users)
