import customtkinter as ctk

def create_complete_signup_form(parent, complete_signup_callback, controller):
    signup_label = ctk.CTkLabel(parent, text="Complete Signup", font=('Arial', 25, 'bold'))
    signup_label.pack(fill=ctk.X)
    
    frame = ctk.CTkFrame(parent, width=350, height=400)
    
    age_label = ctk.CTkLabel(frame, text="Age")
    age_label.grid(row=0, column=0, padx=50, pady=10, sticky=ctk.W)
    
    age_entry = ctk.CTkEntry(frame, width=350)
    age_entry.grid(row=2, column=0, padx=70, pady=10)
    
    height_label = ctk.CTkLabel(frame, text="Height")
    height_label.grid(row=3, column=0, padx=50, pady=10, sticky=ctk.W)
    
    height_entry = ctk.CTkEntry(frame, width=350)
    height_entry.grid(row=4, column=0, padx=70, pady=10)
    
    weight_label = ctk.CTkLabel(frame, text="Weight")
    weight_label.grid(row=5, column=0, padx=50, pady=10, sticky=ctk.W)
    
    weight_entry = ctk.CTkEntry(frame, width=350)
    weight_entry.grid(row=6, column=0, padx=70, pady=10)
    
    submit = ctk.CTkButton(frame, text="Complete", command=complete_signup_callback)
    submit.grid(row=7, column=0, padx=50, pady=30)

    login_label = ctk.CTkLabel(frame, text="Have an account?")
    login_label.grid(row=8, column=0, padx=100, pady=15, sticky=ctk.W)
    
    login = ctk.CTkButton(frame, text="Login", command=lambda: controller.show_frame("LoginFrame"))
    login.grid(row=8, column=0, padx=200, pady=15)

    return frame, age_entry, height_entry, weight_entry
