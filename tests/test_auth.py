# tests/test_auth.py
from src.auth import AuthSystem
from src.user import UserDatabase

def setup_database():
    """Setup a test user database."""
    db = UserDatabase()
    db.add_user("alice@example.com", "password123")
    db.add_user("bob@example.com", "bobpass")
    return db


# --- TESTS LOGIN ---
def test_login_success():
    """A valid user must be able to connect."""
    db = setup_database()
    auth = AuthSystem(db)
    result = auth.login("alice@example.com", "password123")
    assert result is True
    assert auth.is_authenticated("alice@example.com") is True

def test_login_wrong_password():
    """A wrong password must fail."""
    db = setup_database()
    auth = AuthSystem(db)
    result = auth.login("bob@example.com", "wrongpass")
    assert result is False
    assert auth.is_authenticated("bob@example.com") is False

def test_login_nonexistent_user():
    """An invalid user cannot connect."""
    db = setup_database()
    auth = AuthSystem(db)
    result = auth.login("ghost@example.com", "any")
    assert result is False



# --- TESTS LOGOUT ---
def test_logout_success():
    """A connecter user must be able to disconnect."""
    db = setup_database()
    auth = AuthSystem(db)
    auth.login("alice@example.com", "password123")
    result = auth.logout("alice@example.com")
    assert result is True
    assert auth.is_authenticated("alice@example.com") is False

def test_logout_user_not_logged_in():
    """Disconnect a non-connected user must return False."""
    db = setup_database()
    auth = AuthSystem(db)
    result = auth.logout("bob@example.com")
    assert result is False



# --- TESTS MULTI-SESSION ---
def test_multiple_logins_independent_sessions():
    """Multiple users can be connected independently."""
    db = setup_database()
    auth = AuthSystem(db)

    auth.login("alice@example.com", "password123")
    auth.login("bob@example.com", "bobpass")

    assert auth.is_authenticated("alice@example.com") is True
    assert auth.is_authenticated("bob@example.com") is True

    auth.logout("alice@example.com")
    assert auth.is_authenticated("alice@example.com") is False
    assert auth.is_authenticated("bob@example.com") is True
