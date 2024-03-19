from PyQt5.QtCore import Qt, QSize
import modul_of_main

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QRadioButton, QLabel, \
    QLineEdit, QStyle


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initializing the main application window.
        """
        super().__init__()
        self.setWindowTitle("CODING_UNCODING_APP")
        # Set the window size to the center of the screen
        self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter, QSize(600, 280),
                                            QApplication.desktop().availableGeometry()))

        # Create radio buttons to select the encoding method
        self.radio_button1 = QRadioButton("LOOPING\nMETHOD", self)
        self.radio_button1.move(50, 35)

        # Set the first radio button as default
        self.radio_button1.setChecked(True)

        self.radio_button3 = QRadioButton("NUMBER\nMETHOD ", self)
        self.radio_button3.move(250, 35)

        self.radio_button2 = QRadioButton("UNCODING", self)
        self.radio_button2.move(450, 35)

        # Labels above input fields
        self.label_input = QLabel("Input text:", self)
        self.label_input.move(50, 75)

        self.input_box = QLineEdit(self)
        self.input_box.move(50, 105)

        self.input_box.resize(self.width() - 100, 30)  # Stretch by width and height
        self.input_box.setPlaceholderText("Enter text here...\\ Ведите текст...")

        self.label_input_loop = QLabel("Input key:", self)
        self.label_input_loop.move(50, 145)

        self.input_box_loop = QLineEdit(self)
        self.input_box_loop.move(50, 175)
        self.input_box_loop.resize(self.width() - 100, 30)
        self.input_box_loop.setPlaceholderText("Enter key for coding...\\ Введите ключь...")

        # Button to get an answer
        self.open_button = QPushButton("The answer", self)
        self.open_button.clicked.connect(lambda: modul_of_main.click(self))
        self.open_button.move(450, 225)

        # Variable to store text to display in the dialog box
        self.text_to_show = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
