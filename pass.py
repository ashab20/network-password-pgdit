# ONE FILE TO RUN THE APP
# *********** TO RUN THE APP MAC & LINUX *********** #
# Create a new environment
# python3 -m venv env
# Activate the environment
# source env/bin/activate
# Install tkinter and ttkbootstrap
# pip3 install tkinter
# pip3 install ttkbootstrap

# Run the app
# python3 pass.py

# *********** TO RUN THE APP WINDOWS *********** #
# Create a new environment
# python -m venv env
# Activate the environment
# env\Scripts\active.bat
# Install tkinter and ttkbootstrap
# pip install tkinter
# pip install ttkbootstrap



import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import tkinter as tk

class AuthServices:
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


class AuthController:
    def __init__(self):
        self.authService = AuthServices()

    def login(self, email, password):
        if not email or not password:
            return "Please enter both email and password."

        checkPassword = self.authService.checkPasswordSecurity(password)
        if not checkPassword:
            return "❌ Password is not secure.\nUse uppercase, number, and min 8 chars."
        else:
            return f"✅ Welcome, {email}!\nPassword is secure."


class LoginView:
    def __init__(self):
        self.authController = AuthController()
        self.email_entry = None
        self.password_entry = None

    def create_window(self):
        root = ttk.Window(themename="cosmo")
        root.title("Login - PGDIT")
        root.geometry("600x600")
        root.resizable(False, False)

        # Gradient background
        canvas = tk.Canvas(root, width=600, height=600, highlightthickness=0)
        canvas.place(x=0, y=0)
        self.draw_gradient(canvas, "#6a11cb", "#2575fc")

        # Login frame
        frame = ttk.Frame(root, padding=50, bootstyle="light")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Welcome Back 👋", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))
        ttk.Label(frame, text="Please login to continue", font=("Helvetica", 10)).pack(pady=(0, 15))

        ttk.Label(frame, text="Email", font=("Helvetica", 10, "bold")).pack(anchor="w")
        self.email_entry = ttk.Entry(frame, width=30)
        self.email_entry.pack(pady=5)

        ttk.Label(frame, text="Password", font=("Helvetica", 10, "bold")).pack(anchor="w")
        self.password_entry = ttk.Entry(frame, width=30, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(frame, text="Login", bootstyle=PRIMARY, width=20, command=self.login).pack(pady=15)

        ttk.Label(frame, text="© 2025 PGDIT", font=("Helvetica", 8)).pack(pady=(10, 0))

        root.mainloop()

    def draw_gradient(self, canvas, color1, color2):
        width = 600
        height = 600
        limit = height
        (r1, g1, b1) = canvas.winfo_rgb(color1)
        (r2, g2, b2) = canvas.winfo_rgb(color2)
        r_ratio = (r2 - r1) / limit
        g_ratio = (g2 - g1) / limit
        b_ratio = (b2 - b1) / limit
        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = f"#{nr >> 8:02x}{ng >> 8:02x}{nb >> 8:02x}"
            canvas.create_line(0, i, width, i, fill=color)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        result = self.authController.login(email, password)
        messagebox.showinfo("Login Result", result)


# -------------------- Run App -------------------- #
if __name__ == "__main__":
    LoginView().create_window()
