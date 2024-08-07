from tkinter import *
from tkinter import messagebox
from gui.main_window import MainWindow
from gui.widgets.signupWidgets import create_signup_form
from utils.utilsFunctions import center_window

class SignupWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Signup")
        center_window(self.root, 500, 500)
        self.root.resizable(False, False)
        self.root.configure(bg='#D5DBDB')
        self.root.iconbitmap('J:\\Project 3\\assets\imgs\\signup.ico')
        
        # Create and pack the signup form
        self.signup_frame, self.username_entry, self.email_entry, self.password_entry = create_signup_form(self.root, self.signup)
        self.signup_frame.pack(pady=30)

    def signup(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Example authentication logic
        if username != "" and email != "" and password != "":
            print(username, email, password)
        else:
            messagebox.showerror("Signup Failed", "all entries must be filled")

    def run(self):
        self.root.mainloop()
