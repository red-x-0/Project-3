import customtkinter as ctk
from tkinter import messagebox  # Import messagebox from tkinter
from gui.widgets.signupWidgets import create_signup_form
from utils.db import addUser

class SignupFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.signup_frame, self.username_entry, self.email_entry, self.password_entry = create_signup_form(self, self.signup, controller)
        self.signup_frame.pack(pady=30)

    def signup(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not email or not password:
            messagebox.showerror("Signup Failed", "All entries must be filled")
            return
        
        if ' ' in username:
            messagebox.showerror("Signup Failed", "Username cannot contain spaces")
            return
        
        if len(username) <= 3:
            messagebox.showerror("Signup Failed", "Username must be atleast 4 character")
            return
        
        print(username, email, password)
        user = {
            "username": username,
            "email": email,
            "password": password,
            "weight": 0,
            "height": 0,
            "age": 0
        }
        addUser(user)
        self.controller.show_frame("LoginFrame")
