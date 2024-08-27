import customtkinter as ctk
from tkinter import messagebox
from gui.widgets.CompleteSignupWidgets import create_complete_signup_form
from utils.db import editUser
from utils.shelf_utils import load_token

class CompleteSignupFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.signup_frame, self.age_entry, self.height_entry, self.weight_entry = create_complete_signup_form(self, self.complete_signup, controller)
        self.signup_frame.pack(pady=30)

    def complete_signup(self):
        age = self.age_entry.get().strip()
        height = self.height_entry.get().strip()
        weight = self.weight_entry.get().strip()
        
        if not age or not height or not weight:
            messagebox.showerror("Signup Failed", "All entries must be filled")
            return
        
        if int(age) < 14:
            messagebox.showerror("Signup Failed", "Age must be at least 14 years")
            return
        
        user_id = load_token()
        if not user_id:
            messagebox.showerror("Signup Failed", "User ID not found")
            return

        updates = {
            "weight": weight,
            "height": height,
            "age": age
        }
        
        if editUser(user_id, updates):
            self.controller.show_frame("MainFrame")
        else:
            messagebox.showerror("Signup Failed", "Failed to update user details")
