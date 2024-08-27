import json
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from gui.login_window import LoginFrame
from gui.signup_window import SignupFrame
from gui.main_window import MainFrame
from gui.complete_signup_window import CompleteSignupFrame
from utils.db import getUserById
from utils.shelf_utils import load_token

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fitness App")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        self.iconbitmap('J:\\Project 3\\assets\\imgs\icon.ico')
        self.frames = {}

        self.minsize(600, 400)  # Minimum size: width=600, height=400

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

        # Configure grid row and column weights
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        for F in (LoginFrame, SignupFrame, MainFrame, CompleteSignupFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Ensure frame expands to fill the container
        
        self.show_frame("LoginFrame" if not load_token() else self.check_user())
    
    def check_user(self):
        user_id = load_token()
        if not user_id:
            messagebox.showerror("Error", "User ID not found")
            return "LoginFrame"

        user_data = getUserById(user_id)
        if not user_data:
            messagebox.showerror("Error", "User not found in the database")
            return "LoginFrame"

        # Ensure user_data is a dictionary and access its fields correctly
        if int(user_data.get("weight", 0)) > 10 and int(user_data.get("height", 0)) > 10 and int(user_data.get("age", 0)) > 13:
            return "MainFrame"
        else:
            return "CompleteSignupFrame"

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        
        if page_name == "MainFrame":
            self.state('zoomed')
            self.resizable(True, True)
            self.minsize(700, 500)
        elif page_name == "LoginFrame":
            self.resizable(False, False)
            self.state('normal')
            self.geometry('540x500')
            self.minsize(540, 500)
        elif page_name == "SignupFrame":
            self.resizable(False, False)
            self.state('normal')
            self.geometry('540x510')
            self.minsize(540, 510)
        elif page_name == "CompleteSignupFrame":
            self.resizable(False, False)
            self.state('normal')
            self.geometry('540x520')
            self.minsize(540, 520)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
