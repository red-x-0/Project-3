import tkinter as tk
from assets.styles.globalStyles import button_style, label_style

def create_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command, **button_style)
    return button

def create_label(parent, text):
    label = tk.Label(parent, text=text, **label_style)
    return label
