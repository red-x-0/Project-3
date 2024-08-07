from assets.styles.signupStyles import SIGNUP_LABEL_STYLE, LABEL_STYLE, BUTTON_STYLE, SMALL_LABEL_STYLE, SMALL_BUTTON_STYLE
import tkinter as tk
from tkinter import W, X, Frame, Label, Entry, Button

def create_signup_form(parent, signup_callback, controller):
    signup_label = Label(parent, text="Signup", **SIGNUP_LABEL_STYLE)
    signup_label.pack(fill=X)
    
    frame = Frame(parent, width=300, height=400, bg=parent.cget('background'))
    
    username_label = Label(frame, text="Username", **LABEL_STYLE)
    username_label.grid(row=0, column=0, padx=50, pady=10, sticky=W)
    
    username_entry = Entry(frame, width=25, font=("Courier", 17), borderwidth=0, relief='flat')
    username_entry.grid(row=2, column=0, padx=70, pady=10)
    
    email_label = Label(frame, text="Email", **LABEL_STYLE)
    email_label.grid(row=3, column=0, padx=50, pady=10, sticky=W)
    
    email_entry = Entry(frame, width=25, font=("Courier", 17), borderwidth=0, relief='flat')
    email_entry.grid(row=4, column=0, padx=70, pady=10)
    
    password_label = Label(frame, text="Password", **LABEL_STYLE)
    password_label.grid(row=5, column=0, padx=50, pady=10, sticky=W)
    
    password_entry = Entry(frame, width=25, font=("Courier", 17), borderwidth=0, show='*', relief='flat')
    password_entry.grid(row=6, column=0, padx=70, pady=10)
    
    submit = Button(frame, text="SIGNUP", **BUTTON_STYLE, command=signup_callback)
    submit.grid(row=7, column=0, padx=50, pady=30)

    login_label = Label(frame, text="Have an account?", **SMALL_LABEL_STYLE)
    login_label.grid(row=8, column=0, padx=100, pady=15, sticky=W)
    
    login = Button(frame, text="Login", **SMALL_BUTTON_STYLE, relief="flat", command=lambda: controller.show_frame("LoginFrame"))
    login.grid(row=8, column=0, padx=200, pady=15)

    return frame, username_entry, email_entry, password_entry
