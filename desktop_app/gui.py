# gui.py

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from screen_cast import start_physical_cast, stop_physical_cast
from utils import generate_qr_code, get_local_ip
from PIL import Image, ImageTk
import requests
import os

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Presentation Software")

        self.screen_type = tk.StringVar(value="Physical")
        self.output_screen = tk.StringVar(value="Screen 1")

        self.create_main_menu()

    def create_main_menu(self):
        self.main_menu_frame = ttk.Frame(self.master)
        self.main_menu_frame.pack(pady=20)

        self.start_button = ttk.Button(self.main_menu_frame, text="Start Casting", command=self.start_casting)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(self.main_menu_frame, text="Stop Casting", command=self.stop_casting)
        self.stop_button.pack(pady=10)

        self.select_screen_button = ttk.Button(self.main_menu_frame, text="Select Output Screen", command=self.open_screen_selection)
        self.select_screen_button.pack(pady=10)

        self.qr_button = ttk.Button(self.main_menu_frame, text="Generate QR Code", command=self.generate_qr_code)
        self.qr_button.pack(pady=10)

        self.upload_button = ttk.Button(self.main_menu_frame, text="Upload Presentation", command=self.upload_presentation)
        self.upload_button.pack(pady=10)

        self.drag_drop_label = tk.Label(self.main_menu_frame, text="Drag and drop files here", relief="solid", width=40, height=10)
        self.drag_drop_label.pack(pady=10)

        # Bind drag and drop events
        self.drag_drop_label.bind("<ButtonPress-1>", self.drag_start)
        self.drag_drop_label.bind("<B1-Motion>", self.drag_motion)
        self.drag_drop_label.bind("<ButtonRelease-1>", self.drag_drop)

    def drag_start(self, event):
        self.drag_data = {"x": event.x, "y": event.y}

    def drag_motion(self, event):
        x = self.master.winfo_pointerx() - self.drag_data["x"]
        y = self.master.winfo_pointery() - self.drag_data["y"]
        self.master.geometry(f"+{x}+{y}")

    def drag_drop(self, event):
        file_path = filedialog.askopenfilename(
            title="Select Presentation",
            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
        )
        if file_path:
            self.upload_file(file_path)

    def open_screen_selection(self):
        self.screen_selection_window = tk.Toplevel(self.master)
        self.screen_selection_window.title("Select Output Screen")

        self.screen_label = ttk.Label(self.screen_selection_window, text="Select Screen Type:")
        self.screen_label.pack(pady=10)

        self.screen_dropdown = ttk.Combobox(self.screen_selection_window, textvariable=self.screen_type)
        self.screen_dropdown['values'] = ("Physical")
        self.screen_dropdown.pack(pady=10)

        self.output_label = ttk.Label(self.screen_selection_window, text="Select Output Screen:")
        self.output_label.pack(pady=10)

        self.output_dropdown = ttk.Combobox(self.screen_selection_window, textvariable=self.output_screen)
        self.output_dropdown['values'] = self.get_available_screens()
        self.output_dropdown.pack(pady=10)

        self.save_button = ttk.Button(self.screen_selection_window, text="Save", command=self.save_screen_selection)
        self.save_button.pack(pady=10)

    def save_screen_selection(self):
        # Close the screen selection window
        self.screen_selection_window.destroy()

    def get_available_screens(self):
        # This function should return a list of available screens
        # For simplicity, we'll use dummy screen names
        return ["Screen 1", "Screen 2", "Screen 3"]

    def start_casting(self):
        screen_type = self.screen_type.get()
        output_screen = self.output_screen.get()
        if screen_type == "Physical":
            start_physical_cast(output_screen)

    def stop_casting(self):
        screen_type = self.screen_type.get()
        if screen_type == "Physical":
            stop_physical_cast()

    def generate_qr_code(self):
        ip = get_local_ip()
        url = f"http://{ip}:5000"
        qr_path = generate_qr_code(url)
        self.show_qr_code(qr_path)

    def show_qr_code(self, qr_path):
        qr_window = tk.Toplevel(self.master)
        qr_window.title("QR Code")

        qr_image = Image.open(qr_path)
        qr_photo = ImageTk.PhotoImage(qr_image)

        qr_label = ttk.Label(qr_window, image=qr_photo)
        qr_label.image = qr_photo  # Keep a reference to avoid garbage collection
        qr_label.pack(pady=10)

    def upload_presentation(self):
        # Open the file dialog to select a presentation file
        file_path = filedialog.askopenfilename(
            title="Select Presentation",
            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
        )
        if file_path:
            self.upload_file(file_path)

    def upload_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                response = requests.post('http://localhost:5000/upload_presentation', files={'file': file})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Presentation uploaded successfully!")
            else:
                messagebox.showerror("Error", f"Failed to upload presentation: {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Define app_instance
root = tk.Tk()
app_instance = App(root)