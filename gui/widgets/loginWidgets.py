import customtkinter as ctk

def create_login_form(parent, login_callback, controller):
    login_label = ctk.CTkLabel(parent, text="Login", font=('Arial', 25, 'bold'))
    login_label.pack()
    
    frame = ctk.CTkFrame(parent, width=300, height=600)
    
    username_label = ctk.CTkLabel(frame, text="Username")
    username_label.grid(row=0, column=0, padx=50, pady=10, sticky=ctk.W)
    
    username_entry = ctk.CTkEntry(frame, width=350)
    username_entry.grid(row=2, column=0, padx=50, pady=10)
    
    password_label = ctk.CTkLabel(frame, text="Password")
    password_label.grid(row=3, column=0, padx=50, pady=10, sticky=ctk.W)
    
    password_entry = ctk.CTkEntry(frame, width=350, show='*')
    password_entry.grid(row=4, column=0, padx=50, pady=10)
    
    submit = ctk.CTkButton(frame, text="LOGIN", command=login_callback)
    submit.grid(row=5, column=0, padx=50, pady=30)
    
    signup_label = ctk.CTkLabel(frame, text="Don't have an account?")
    signup_label.grid(row=6, column=0, padx=50, pady=15, sticky=ctk.W)
    
    signup = ctk.CTkButton(frame, text="Signup", command=lambda: controller.show_frame("SignupFrame"))
    signup.grid(row=6, column=0, padx=200, pady=15)

    return frame, username_entry, password_entry
