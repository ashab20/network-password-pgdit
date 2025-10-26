from services.authServices import AuthServices

class AuthController:
    def __init__(self):
        self.authService = AuthServices()

    def login(self, email, password):
        if not email or not password:
            return "Please enter both email and password."

        checkPassword = self.authService.checkPasswordSecurity(password)
        if not checkPassword:
            return "❌ Password is not secure.\nUse uppercase, number, and min 6 chars."
        else:
            return f"✅ Welcome, {email}!\nPassword is secure."
