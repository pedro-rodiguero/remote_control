from tkinter import Tk
from gui import App
from server import run_flask_app
import threading

if __name__ == "__main__":
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.daemon = True
    flask_thread.start()

    root = Tk()
    app_instance = App(root)
    root.mainloop()