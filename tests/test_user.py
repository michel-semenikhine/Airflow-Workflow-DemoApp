# tests/test_user.py
import pytest
from src.user import User, UserDatabase

# --- TESTS User class ---
def test_create_user_valid():
    """Create a user with valid email and password."""
    user = User("test@example.com", "password123")
    assert user.email == "test@example.com"
    assert user.hashed_password is not None
    assert len(user.hashed_password) == 64  # hash SHA-256

def test_create_user_invalid_email():
    """An invalid email address should throw an exception."""
    with pytest.raises(ValueError):
        User("notanemail", "password123")

def test_create_user_empty_password():
    """An empty password should throw an exception."""
    with pytest.raises(ValueError):
        User("valid@example.com", "")



# --- TESTS UserDatabase class ---
def test_add_user_and_get_user():
    """Add a user then find them in the database."""
    db = UserDatabase()
    db.add_user("alice@example.com", "1234")
    user = db.get_user("alice@example.com")
    assert user is not None
    assert user.email == "alice@example.com"

def test_add_existing_user_raises_error():
    """Adding the same user twice should throw an error."""
    db = UserDatabase()
    db.add_user("bob@example.com", "pass")
    with pytest.raises(ValueError):
        db.add_user("bob@example.com", "pass2")

def test_remove_user_success():
    """Deleting an existing user should return True."""
    db = UserDatabase()
    db.add_user("charlie@example.com", "pw")
    result = db.remove_user("charlie@example.com")
    assert result is True
    assert db.get_user("charlie@example.com") is None

def test_remove_user_not_found_returns_false():
    """Deleting a non-existent user should return False."""
    db = UserDatabase()
    result = db.remove_user("ghost@example.com")
    assert result is False

def test_user_count():
    """Check that the user counter is correct."""
    db = UserDatabase()
    db.add_user("a@example.com", "1")
    db.add_user("b@example.com", "2")
    assert db.count() == 2
