import hashlib


class AuthServices:
    users = {
        "admin@pgdit.com": hashlib.sha256("@dminPGDIT123".encode()).hexdigest()
    }

    def checkPasswordSecurity(self, password):
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        return True

    def verify_user(self, email, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        stored_hash = self.users.get(email)
        return stored_hash == hashed