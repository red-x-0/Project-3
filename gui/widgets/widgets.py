import customtkinter as ctk

def create_button(parent, text, command):
    button = ctk.CTkButton(parent, text=text, command=command)
    return button

def create_label(parent, text):
    label = ctk.CTkLabel(parent, text=text)
    return label
