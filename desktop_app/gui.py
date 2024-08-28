import tkinter as tk
from tkinter import ttk
from screen_cast import start_physical_cast, stop_physical_cast
from ndi_stream import start_ndi_stream, stop_ndi_stream

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Presentation Software")

        self.screen_type = tk.StringVar(value="Physical")

        self.create_widgets()

    def create_widgets(self):
        self.screen_label = ttk.Label(self.master, text="Select Screen Type:")
        self.screen_label.pack(pady=10)

        self.screen_dropdown = ttk.Combobox(self.master, textvariable=self.screen_type)
        self.screen_dropdown['values'] = ("Physical", "NDI")
        self.screen_dropdown.pack(pady=10)

        self.start_button = ttk.Button(self.master, text="Start Casting", command=self.start_casting)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(self.master, text="Stop Casting", command=self.stop_casting)
        self.stop_button.pack(pady=10)

    def start_casting(self):
        screen_type = self.screen_type.get()
        if screen_type == "Physical":
            start_physical_cast()
        elif screen_type == "NDI":
            start_ndi_stream()

    def stop_casting(self):
        screen_type = self.screen_type.get()
        if screen_type == "Physical":
            stop_physical_cast()
        elif screen_type == "NDI":
            stop_ndi_stream()