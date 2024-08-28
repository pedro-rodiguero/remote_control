import tkinter as tk
from tkinter import Toplevel, Label, filedialog, messagebox
from PIL import Image, ImageTk
from slides import load_pptx, load_pdf, load_images, load_video
from ndi_stream import start_ndi_stream
from utils import generate_qr_code, get_local_ip
from ffpyplayer.player import MediaPlayer

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Remote Control Application")
        self.root.geometry("800x600")

        self.slides = []
        self.current_slide = 0
        self.player = None

        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(
            self.root, text="Load Slides", command=self.load_slides
        )
        self.load_button.pack(pady=10)

        self.next_button = tk.Button(
            self.root, text="Next Slide", command=self.next_slide
        )
        self.next_button.pack(pady=10)

        self.prev_button = tk.Button(
            self.root, text="Previous Slide", command=self.prev_slide
        )
        self.prev_button.pack(pady=10)

        self.qr_button = tk.Button(
            self.root, text="Generate QR Code", command=self.generate_qr
        )
        self.qr_button.pack(pady=10)

        self.screen_button = tk.Button(
            self.root, text="Show Screen", command=self.show_screen
        )
        self.screen_button.pack(pady=10)

        self.slide_label = Label(self.root)
        self.slide_label.pack(pady=10)

    def load_slides(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PowerPoint files", "*.pptx"), ("PDF files", "*.pdf"), ("Image files", "*.png;*.jpg;*.jpeg"), ("Video files", "*.mp4;*.avi;*.mov")]
        )
        if file_path:
            if file_path.endswith(".pptx"):
                self.slides = load_pptx(file_path)
            elif file_path.endswith(".pdf"):
                self.slides = load_pdf(file_path)
            elif file_path.endswith((".mp4", ".avi", ".mov")):
                self.slides = load_video(file_path)
            else:
                self.slides = load_images([file_path])
            self.show_slide(0)

    def show_slide(self, index):
        if 0 <= index < len(self.slides):
            self.current_slide = index
            if self.player:
                self.player.close_player()
                self.player = None

            if self.slides[index].endswith((".mp4", ".avi", ".mov")):
                self.player = MediaPlayer(self.slides[index])
                self.play_video()
            else:
                img = Image.open(self.slides[index])
                img = img.resize((800, 600), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
                self.slide_label.config(image=img)
                self.slide_label.image = img

    def play_video(self):
        def update_frame():
            frame, val = self.player.get_frame()
            if val == 'eof':
                self.next_slide()
                return
            if frame is not None:
                img, t = frame
                img = Image.fromarray(img)
                img = img.resize((800, 600), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
                self.slide_label.config(image=img)
                self.slide_label.image = img
            self.root.after(10, update_frame)

        update_frame()

    def next_slide(self):
        if self.current_slide < len(self.slides) - 1:
            self.show_slide(self.current_slide + 1)

    def prev_slide(self):
        if self.current_slide > 0:
            self.show_slide(self.current_slide - 1)

    def generate_qr(self):
        ip = get_local_ip()
        url = f"http://{ip}:5000"
        qr_path = generate_qr_code(url)
        self.show_qr_code(qr_path)

    def show_qr_code(self, qr_path):
        qr_window = Toplevel(self.root)
        qr_window.title("QR Code")
        qr_window.geometry("300x300")

        try:
            img = Image.open(qr_path)
            img = img.resize((250, 250), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)

            label = Label(qr_window, image=img)
            label.image = img  # Keep a reference to avoid garbage collection
            label.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load QR code image: {e}")

    def show_screen(self):
        start_ndi_stream()
