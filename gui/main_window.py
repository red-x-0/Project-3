import tkinter as tk
from gui.widgets.widgets import create_button, create_label
from utils.shelf_utils import remove_token

class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = create_label(self, "Welcome to Fitness App!")
        self.label.pack(pady=20)

        self.button = create_button(self, "Click Me", self.on_button_click)
        self.button.pack(pady=20)

        self.logout_button = create_button(self, "Logout", self.on_logout_click)
        self.logout_button.pack(pady=20)

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

    def on_logout_click(self):
        remove_token()
        self.controller.show_frame("LoginFrame")
