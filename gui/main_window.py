import webbrowser
import customtkinter as ctk
from env import DEFAULT_IMAGE_PATH, MAIN_PATH
from utils.db import loadExercises
from utils.shelf_utils import remove_token
from PIL import Image, ImageTk
import requests
from io import BytesIO
from gui.exercise_window import ExerciseFrame  # Import ExerciseFrame

class MainFrame(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Create the tab view
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(fill="both", expand=True, padx=10, pady=10)

        # Create tabs
        self.home_tab = self.tab_view.add("Home")
        self.exercises_tab = self.tab_view.add("All Exercises")
        self.logout_tab = self.tab_view.add("Logout")

        # Populate the Home tab
        self.home_label = ctk.CTkLabel(self.home_tab, text="Welcome !")
        self.home_label.pack(pady=20)

        # Title for the filtered exercises
        self.filtered_exercises_title = ctk.CTkLabel(self.home_tab, text="Exercises for you", font=("Arial", 14, "bold"))
        self.filtered_exercises_title.pack(pady=10)

        # Frame to display filtered exercises
        self.filtered_exercises_frame = ctk.CTkScrollableFrame(self.home_tab)
        self.filtered_exercises_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Populate the Exercises tab with a scrollable frame
        self.exercises_frame = ctk.CTkScrollableFrame(self.exercises_tab)
        self.exercises_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame to display selected exercise details
        self.exercise_detail_frame = None

        self.load_exercises()
        self.load_filtered_exercises()

        # Populate the Logout tab
        self.logout_button = ctk.CTkButton(self.logout_tab, text="Logout", command=self.on_logout_click)
        self.logout_button.pack(pady=20)

    def load_image(self, image_path):
        try:
            # If image_path is not provided, use the default image path
            if not image_path:
                image_path = MAIN_PATH + DEFAULT_IMAGE_PATH
            else:
                image_path = MAIN_PATH + image_path

            # Load the image from the local file system
            img = Image.open(image_path)
        except Exception as e:
            print(f"Error loading image: {e}")
            try:
                # Fallback to loading the default image if there's an error
                img = Image.open(MAIN_PATH + DEFAULT_IMAGE_PATH)
            except Exception as e:
                print(f"Error loading default image: {e}")
                img = None  # Handle if even the default image fails
        return ImageTk.PhotoImage(img) if img else None


    def load_exercises(self):
        exercises = loadExercises()
        for index, exercise in enumerate(exercises):
            name = exercise.get('name', 'Unknown')
            image_url = exercise.get('image', '')

            img = self.load_image(image_url)

            # Determine row and column
            row = index // 4
            column = index % 4

            # Create a button for each exercise
            exercise_button = ctk.CTkButton(self.exercises_frame, image=img, text=name, compound="top", command=lambda e=exercise: self.show_exercise_details(e))
            exercise_button.image = img  # Keep a reference to avoid garbage collection
            exercise_button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")  # Fill the full width and height

            # Configure row weight to allow expansion
            self.exercises_frame.grid_rowconfigure(row, weight=1)
            
            # Configure column weight to allow expansion
            self.exercises_frame.grid_columnconfigure(column, weight=1)

    def load_filtered_exercises(self):
        # Define your filtering criteria here. For demonstration, we'll show all exercises.
        filtered_exercises = self.get_filtered_exercises()

        for index, exercise in enumerate(filtered_exercises):
            name = exercise.get('name', 'Unknown')
            image_url = exercise.get('image', '')

            img = self.load_image(image_url)

            # Determine row and column
            row = index // 4
            column = index % 4

            # Create a button for each filtered exercise
            exercise_button = ctk.CTkButton(self.filtered_exercises_frame, image=img, text=name, compound="top", command=lambda e=exercise: self.show_exercise_details(e))
            exercise_button.image = img  # Keep a reference to avoid garbage collection
            exercise_button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")  # Fill the full width and height

            # Configure row weight to allow expansion
            self.filtered_exercises_frame.grid_rowconfigure(row, weight=1)
            
            # Configure column weight to allow expansion
            self.filtered_exercises_frame.grid_columnconfigure(column, weight=1)

    def get_filtered_exercises(self):
        # Implement filtering logic here. For now, we'll return all exercises.
        return loadExercises()

    def show_exercise_details(self, exercise):
        if self.exercise_detail_frame:
            self.exercise_detail_frame.pack_forget()  # Hide existing detail frame

        # Create and pack the new exercise detail frame
        self.exercise_detail_frame = ExerciseFrame(self, exercise)
        self.exercise_detail_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def open_exercise_window(self, exercise):
        # Method not used anymore
        pass

    def on_logout_click(self):
        remove_token()
        self.controller.show_frame("LoginFrame")
