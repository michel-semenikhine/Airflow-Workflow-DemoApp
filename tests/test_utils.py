# tests/test_utils.py
import pytest
from src.utils import hash_password, check_password, is_valid_email

# --- TESTS hash_password() ---
def test_hash_password_generates_different_hashes_for_different_inputs():
    """Each password must generate a different hash."""
    hash1 = hash_password("abc123")
    hash2 = hash_password("xyz789")
    assert hash1 != hash2

def test_hash_password_raises_error_on_empty_password():
    """Hash must raise an error if the password is empty."""
    with pytest.raises(ValueError):
        hash_password("")



# --- TESTS check_password() ---
def test_check_password_returns_true_for_correct_password():
    """The password must correspond to the hash."""
    password = "secret"
    hashed = hash_password(password)
    assert check_password(password, hashed) is True

def test_check_password_returns_false_for_wrong_password():
    """An incorrect password must NOT correspond to the hash."""
    hashed = hash_password("password123")
    assert check_password("wrongpass", hashed) is False

def test_check_password_returns_false_if_inputs_missing():
    """If one of the args is empty, the function must return False."""
    assert check_password("", "anything") is False
    assert check_password("anything", "") is False



# --- TESTS is_valid_email() ---
@pytest.mark.parametrize("email", [
    "test@example.com",
    "john.doe@university.edu",
    "a_b-c@domain.co"
])
def test_is_valid_email_valid_formats(email):
    """Valid emails must be recognized."""
    assert is_valid_email(email) is True

@pytest.mark.parametrize("email", [
    "invalidemail",
    "noatsign.com",
    "wrong@.com",
    "@missinguser.com"
])
def test_is_valid_email_invalid_formats(email):
    """Invalid emails must be rejected."""
    assert is_valid_email(email) is False
