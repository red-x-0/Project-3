import tkinter as tk
from tkinter import messagebox
from gui.widgets.signupWidgets import create_signup_form

class SignupFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#D5DBDB')

        self.signup_frame, self.username_entry, self.email_entry, self.password_entry = create_signup_form(self, self.signup, controller)
        self.signup_frame.pack(pady=30)

    def signup(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if username != "" and email != "" and password != "":
            print(username, email, password)
            self.controller.show_frame("LoginFrame")
        else:
            messagebox.showerror("Signup Failed", "All entries must be filled")
