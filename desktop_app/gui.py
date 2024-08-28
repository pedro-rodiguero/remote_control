import tkinter as tk
from tkinter import ttk
from screen_cast import start_physical_cast, stop_physical_cast

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Presentation Software")

        self.screen_type = tk.StringVar(value="Physical")
        self.output_screen = tk.StringVar(value="Screen 1")

        self.create_widgets()

    def create_widgets(self):
        self.screen_label = ttk.Label(self.master, text="Select Screen Type:")
        self.screen_label.pack(pady=10)

        self.screen_dropdown = ttk.Combobox(self.master, textvariable=self.screen_type)
        self.screen_dropdown['values'] = ("Physical")
        self.screen_dropdown.pack(pady=10)

        self.output_label = ttk.Label(self.master, text="Select Output Screen:")
        self.output_label.pack(pady=10)

        self.output_dropdown = ttk.Combobox(self.master, textvariable=self.output_screen)
        self.output_dropdown['values'] = self.get_available_screens()
        self.output_dropdown.pack(pady=10)

        self.start_button = ttk.Button(self.master, text="Start Casting", command=self.start_casting)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(self.master, text="Stop Casting", command=self.stop_casting)
        self.stop_button.pack(pady=10)

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
