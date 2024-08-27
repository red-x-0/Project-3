import webbrowser
import customtkinter as ctk
from PIL import Image, ImageTk
from env import DEFAULT_IMAGE_PATH, MAIN_PATH

class ExerciseFrame(ctk.CTkFrame):

    def __init__(self, parent, exercise):
        super().__init__(parent)
        self.parent = parent

        # Extract exercise details
        self.name = exercise.get('name', 'Unknown')
        self.description = exercise.get('description', 'No description available')
        self.image_url = exercise.get('image', '')
        self.vedio_url = exercise.get('video_url', '')

        # Load and display image
        self.image = self.load_image(self.image_url)

        # Create the layout with scrollable content
        self.create_widgets()

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

    def create_widgets(self):
        # Create a scrollable frame
        scrollable_frame = ctk.CTkScrollableFrame(self, width=400, height=400)
        scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create and place the image label inside the scrollable frame
        self.image_label = ctk.CTkLabel(scrollable_frame, image=self.image)
        self.image_label.pack(pady=10, padx=10, fill="both", expand=True)

        # Create and place the name label inside the scrollable frame
        self.name_label = ctk.CTkLabel(scrollable_frame, text=self.name, font=('Arial', 16, 'bold'))
        self.name_label.pack(pady=5, padx=10, fill="x")

        # Create and place the description label inside the scrollable frame
        self.description_label = ctk.CTkLabel(scrollable_frame, text=self.description, wraplength=350, justify='left')
        self.description_label.pack(pady=10, padx=10, fill="both", expand=True)
        
                # Create and place a close button inside the scrollable frame
        self.close_button = ctk.CTkButton(scrollable_frame, text="Watch Tutorial", command=lambda: webbrowser.open(self.vedio_url))
        self.close_button.pack(pady=10, padx=10, anchor='center')

        # Create and place a close button inside the scrollable frame
        self.close_button = ctk.CTkButton(scrollable_frame, text="Close", command=self.hide)
        self.close_button.pack(pady=10, padx=10, anchor='center')

    def hide(self):
        self.pack_forget()  # Hide the frame
