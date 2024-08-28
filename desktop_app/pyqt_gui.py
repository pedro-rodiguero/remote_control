import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox, QComboBox, QDialog, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import requests
import os

class DragDropLabel(QLabel):
    def __init__(self, parent=None, app_instance=None):
        super().__init__(parent)
        self.app_instance = app_instance
        self.setAcceptDrops(True)
        self.setText("Drag and drop files here")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("border: 2px dashed #aaa;")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if os.path.isfile(file_path):
                self.app_instance.upload_file(file_path)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Presentation Software")
        self.setGeometry(100, 100, 600, 400)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.start_button = QPushButton("Start Casting", self)
        self.start_button.clicked.connect(self.start_casting)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Casting", self)
        self.stop_button.clicked.connect(self.stop_casting)
        layout.addWidget(self.stop_button)

        self.select_screen_button = QPushButton("Select Output Screen", self)
        self.select_screen_button.clicked.connect(self.open_screen_selection)
        layout.addWidget(self.select_screen_button)

        self.qr_button = QPushButton("Generate QR Code", self)
        self.qr_button.clicked.connect(self.generate_qr_code)
        layout.addWidget(self.qr_button)

        self.upload_button = QPushButton("Upload Presentation", self)
        self.upload_button.clicked.connect(self.upload_presentation)
        layout.addWidget(self.upload_button)

        self.drag_drop_label = DragDropLabel(self, app_instance=self)
        layout.addWidget(self.drag_drop_label)

        central_widget.setLayout(layout)

    def start_casting(self):
        # Implement start casting functionality
        pass

    def stop_casting(self):
        # Implement stop casting functionality
        pass

    def open_screen_selection(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Output Screen")
        layout = QFormLayout(dialog)

        self.screen_type = QComboBox(dialog)
        self.screen_type.addItems(["Physical"])
        layout.addRow("Select Screen Type:", self.screen_type)

        self.output_screen = QComboBox(dialog)
        self.output_screen.addItems(["Screen 1", "Screen 2", "Screen 3"])
        layout.addRow("Select Output Screen:", self.output_screen)

        save_button = QPushButton("Save", dialog)
        save_button.clicked.connect(dialog.accept)
        layout.addWidget(save_button)

        dialog.exec_()

    def generate_qr_code(self):
        # Implement QR code generation functionality
        pass

    def upload_presentation(self):
        file_path = QFileDialog.getOpenFileName(self, "Select Presentation", "", "PDF files (*.pdf);;All files (*.*)")[0]
        if file_path:
            self.upload_file(file_path)

    def upload_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                response = requests.post('http://localhost:5000/upload_presentation', files={'file': file})
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Presentation uploaded successfully!")
            else:
                QMessageBox.critical(self, "Error", f"Failed to upload presentation: {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())