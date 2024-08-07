import customtkinter as ctk

def create_signup_form(parent, signup_callback, controller):
    signup_label = ctk.CTkLabel(parent, text="Signup", font=('Arial', 25, 'bold'))
    signup_label.pack(fill=ctk.X)
    
    frame = ctk.CTkFrame(parent, width=350, height=400)
    
    username_label = ctk.CTkLabel(frame, text="Username")
    username_label.grid(row=0, column=0, padx=50, pady=10, sticky=ctk.W)
    
    username_entry = ctk.CTkEntry(frame, width=350)
    username_entry.grid(row=2, column=0, padx=70, pady=10)
    
    email_label = ctk.CTkLabel(frame, text="Email")
    email_label.grid(row=3, column=0, padx=50, pady=10, sticky=ctk.W)
    
    email_entry = ctk.CTkEntry(frame, width=350)
    email_entry.grid(row=4, column=0, padx=70, pady=10)
    
    password_label = ctk.CTkLabel(frame, text="Password")
    password_label.grid(row=5, column=0, padx=50, pady=10, sticky=ctk.W)
    
    password_entry = ctk.CTkEntry(frame, width=350, show='*')
    password_entry.grid(row=6, column=0, padx=70, pady=10)
    
    submit = ctk.CTkButton(frame, text="SIGNUP", command=signup_callback)
    submit.grid(row=7, column=0, padx=50, pady=30)

    login_label = ctk.CTkLabel(frame, text="Have an account?")
    login_label.grid(row=8, column=0, padx=100, pady=15, sticky=ctk.W)
    
    login = ctk.CTkButton(frame, text="Login", command=lambda: controller.show_frame("LoginFrame"))
    login.grid(row=8, column=0, padx=200, pady=15)

    return frame, username_entry, email_entry, password_entry
