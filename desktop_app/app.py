# from gui import App  # Uncomment this line if you want to use the Tkinter GUI
from pyqt_gui import App  # Uncomment this line if you want to use the PyQt5 GUI

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())