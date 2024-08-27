import customtkinter as ctk
from tkinter import messagebox
from gui.widgets.loginWidgets import create_login_form
from utils.db import getUser
from utils.shelf_utils import save_token

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Create and place the login form
        self.login_frame, self.username_entry, self.password_entry = create_login_form(self, self.login, controller)
        self.login_frame.pack(pady=30)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        # Basic validation
        if not username or not password:
            messagebox.showerror("Validation Failed", "Please enter both username and password")
            return
        
        # Fetch user from database
        user = getUser(username)
        
        if user:
            # Compare password (this is just an example; use hashed passwords in production)
            if password == user.get('password'):  # Ensure `user` is a dict
                save_token(user['_id'])  # Save user token for session management
                self.controller.show_frame("MainFrame")  # Switch to MainFrame
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
