# src/utils.py
import re
import hashlib

def hash_password(password: str) -> str:
    """
    Return the hash SHA-256 of a password.
    """
    if not password:
        raise ValueError("The password cannot be empty")
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password: str, hashed: str) -> bool:
    """
    Cecks if the given passsword corresponds to an hash.
    """
    if not password or not hashed:
        return False
    return hash_password(password) == hashed

def is_valid_email(email: str) -> bool:
    """
    Checks if an email address is valid.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None
