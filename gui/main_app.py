import tkinter as tk
from gui.login_window import LoginFrame
from gui.signup_window import SignupFrame
from gui.main_window import MainFrame
from utils.shelf_utils import load_token

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fitness App")
        self.geometry("500x500")  # Initial geometry, will be maximized later
        self.frames = {}
        self.configure(bg='#D5DBDB')

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        for F in (LoginFrame, SignupFrame, MainFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame" if not load_token() else "MainFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "MainFrame":
            self.state('zoomed')
        if page_name == "LoginFrame":
            self.state('normal')
            self.geometry('470x500')
        if page_name == "SignupFrame":
            self.state('normal')
            self.geometry('470x550')

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
