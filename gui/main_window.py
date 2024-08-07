import tkinter as tk
from gui.widgets.widgets import create_button, create_label
from utils.utilsFunctions import set_window_max
from utils.shelf_utils import load_token

def check_login():
    token = load_token()
    return token is not None

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fitnes App")
        set_window_max(self.root)

        self.label = create_label(self.root, "Welcome to Fitness App!")
        self.label.pack(pady=20)

        self.button = create_button(self.root, "Click Me", self.on_button_click)
        self.button.pack(pady=20)

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

    def run(self):
        self.root.mainloop()


