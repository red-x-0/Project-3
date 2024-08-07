import customtkinter as ctk
from utils.shelf_utils import remove_token

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.label = ctk.CTkLabel(self, text="Welcome to Fitness App!")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Click Me", command=lambda: self.label.configure(text="Button Clicked!"))
        self.button.pack(pady=20)

        self.logout_button = ctk.CTkButton(self, text="Logout", command=self.on_logout_click)
        self.logout_button.pack(pady=20)

    def on_logout_click(self):
        remove_token()
        self.controller.show_frame("LoginFrame")
