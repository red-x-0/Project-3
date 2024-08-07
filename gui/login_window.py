from tkinter import *
from tkinter import messagebox
from gui.main_window import MainWindow
from gui.widgets.loginWidgets import create_login_form
from utils.utilsFunctions import center_window
from utils.shelf_utils import save_token

class LoginWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        center_window(self.root, 500, 500)
        self.root.resizable(False, False)
        self.root.configure(bg='#D5DBDB')
        self.root.iconbitmap('J:\\Project 3\\assets\imgs\\login.ico')
        
        # Create and pack the login form
        self.login_frame, self.username_entry, self.password_entry = create_login_form(self.root, self.login)
        self.login_frame.pack(pady=30)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Example authentication logic
        if username == "user" and password == "pass":
            save_token('logged')
            print("login")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def run(self):
        self.root.mainloop()
