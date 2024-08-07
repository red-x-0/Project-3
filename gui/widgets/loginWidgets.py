from tkinter import *
from assets.styles.loginStyles import LOGIN_LABEL_STYLE, LABEL_STYLE, BUTTON_STYLE, SMALL_LABEL_STYLE, SMALL_BUTTON_STYLE

def create_login_form(parent, login_callback, controller):
    login_label = Label(parent, text="Login", **LOGIN_LABEL_STYLE)
    login_label.pack(fill=X)
    
    frame = Frame(parent, width='300', height='350', bg=parent.cget('background'))
    
    username_label = Label(frame, text="Username", **LABEL_STYLE)
    username_label.grid(row=0, column=0, padx=50, pady=10, sticky=W)
    
    username_entry = Entry(frame, width=25, font=("Courier", 17), borderwidth=0, relief='flat')
    username_entry.grid(row=2, column=0, padx=70, pady=10)
    
    password_label = Label(frame, text="Password", **LABEL_STYLE)
    password_label.grid(row=3, column=0, padx=50, pady=10, sticky=W)
    
    passowrd_entry = Entry(frame, width=25, font=("Courier", 17), borderwidth=0, show='*', relief='flat')
    passowrd_entry.grid(row=4, column=0, padx=70, pady=10 )
    
    submit = Button(frame, text="LOGIN", **BUTTON_STYLE, command=login_callback)
    submit.grid(row=5, column=0, padx=50, pady=30)
    
    signup_label = Label(frame, text="Doesn't have an acount,", **SMALL_LABEL_STYLE)
    signup_label.grid(row=6, column=0, padx=100, pady=15, sticky=W)
    
    signup = Button(frame, text="Signup", **SMALL_BUTTON_STYLE, relief="flat", command=lambda: controller.show_frame("SignupFrame"))
    signup.grid(row=6, column=0, padx=200, pady=15)

    return frame, username_entry, passowrd_entry
