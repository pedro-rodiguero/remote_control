import tkinter as tk
from tkinter import messagebox, Toplevel, Label
import pyautogui  # type: ignore
import qrcode  # type: ignore
import socket
import os
from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Remote Control Application")
        self.root.geometry("300x250")

        self.create_widgets()

    def create_widgets(self):
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

        self.menu_button = tk.Button(
            self.root, text="Show Menu", command=self.show_menu
        )
        self.menu_button.pack(pady=10)

    def next_slide(self):
        pyautogui.press("right")

    def prev_slide(self):
        pyautogui.press("left")

    def generate_qr(self):
        ip = self.get_local_ip()
        url = f"http://{ip}:5000"
        qr = qrcode.make(url)
        qr_path = os.path.join(os.getcwd(), "qrcode.png")
        qr.save(qr_path)
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

    def show_menu(self):
        pyautogui.position()
        (300, 50)

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("10.254.254.254", 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = "127.0.0.1"
        finally:
            s.close()
        return ip


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
