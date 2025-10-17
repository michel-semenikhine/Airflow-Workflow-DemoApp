# tests/test_integration.py
from src.user import UserDatabase
from src.auth import AuthSystem

def test_full_authentication_workflow():
    """
    Complete integration TEST:
    - Adding a user
    - Connection
    - Session check
    - Disconnect
    - User Deletion
    """

    # Step 1 : Creation of a user database
    db = UserDatabase()

    # Step 2 : Adding a user
    user = db.add_user("integration@example.com", "mypassword")
    assert user.email == "integration@example.com"

    # Step 3 : Setup authentication system
    auth = AuthSystem(db)

    # Step 4 : Connection and session check
    assert auth.login("integration@example.com", "mypassword") is True
    assert auth.is_authenticated("integration@example.com") is True

    # Step 5 : Disconnect
    assert auth.logout("integration@example.com") is True
    assert auth.is_authenticated("integration@example.com") is False

    # Step 6 : User deletion
    assert db.remove_user("integration@example.com") is True
    assert db.get_user("integration@example.com") is None
