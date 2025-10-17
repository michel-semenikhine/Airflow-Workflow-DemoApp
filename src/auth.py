# src/auth.py
from src.user import UserDatabase
from src.utils import check_password

class AuthSystem:
    """
    Système d'authentification simulé.
    """
    def __init__(self, user_db: UserDatabase):
        self.user_db = user_db
        self.active_sessions = set()

    def login(self, email: str, password: str) -> bool:
        """
        Vérifie les identifiants et connecte l'utilisateur.
        """
        user = self.user_db.get_user(email)
        if not user:
            return False
        if check_password(password, user.hashed_password):
            self.active_sessions.add(email)
            return True
        return False

    def logout(self, email: str) -> bool:
        """
        Déconnecte un utilisateur.
        """
        if email in self.active_sessions:
            self.active_sessions.remove(email)
            return True
        return False

    def is_authenticated(self, email: str) -> bool:
        """
        Vérifie si un utilisateur est actuellement connecté.
        """
        return email in self.active_sessions
