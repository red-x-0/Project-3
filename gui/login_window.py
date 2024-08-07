import tkinter as tk
from tkinter import messagebox
from gui.widgets.loginWidgets import create_login_form
from utils.utilsFunctions import center_window
from utils.shelf_utils import save_token

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#D5DBDB')

        self.login_frame, self.username_entry, self.password_entry = create_login_form(self, self.login, controller)
        self.login_frame.pack(pady=30)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "user" and password == "pass":
            save_token('logged')
            self.controller.show_frame("MainFrame")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
