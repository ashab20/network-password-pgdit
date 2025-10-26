import time
from services.authServices import AuthServices

class AuthController:
    def __init__(self):
        self.authService = AuthServices()
        self.failed_attempts = {}
        self.lockout_time = {}   

    def login(self, email, password):
        if email in self.lockout_time:
            if time.time() < self.lockout_time[email]:
                wait_seconds = int(self.lockout_time[email] - time.time())
                return f"⚠️ Too many attempts. Try again in {wait_seconds} seconds."
            else:
                # Unlock after wait
                self.failed_attempts[email] = 0
                del self.lockout_time[email]

        if not email or not password:
            return "Please enter both email and password."

        if not self.authService.checkPasswordSecurity(password):
            return "❌ Password is not secure.\nUse uppercase, number, and min 8 chars."

        if self.authService.verify_user(email, password):
            self.failed_attempts[email] = 0
            return f"✅ Welcome, {email}!\nPassword is secure."
        else:
            # Increment failed attempts
            self.failed_attempts[email] = self.failed_attempts.get(email, 0) + 1
            if self.failed_attempts[email] >= 3:
                self.lockout_time[email] = time.time() + 60 
                return "⚠️ Too many attempts. Please wait 1 minute."
            else:
                attempts_left = 3 - self.failed_attempts[email]
                return f"❌ Invalid credentials. {attempts_left} attempt(s) left."  
