from PyQt5.QtCore import Qt, QSize
import modul_of_main

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QRadioButton, QLabel, \
    QLineEdit, QStyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CODING_UNCODING_APP")
        self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter, QSize(450, 280),
                                            QApplication.desktop().availableGeometry()))

        self.radio_button1 = QRadioButton("CODING LOOP METHOD", self)
        self.radio_button1.move(50, 50)
        self.radio_button1.setChecked(True)  # Устанавливаем первую радиокнопку по умолчанию

        self.radio_button2 = QRadioButton("UNCODING", self)
        self.radio_button2.move(250, 50)

        self.label_input = QLabel("Input text:", self)
        self.label_input.move(50, 75)

        self.input_box = QLineEdit(self)
        self.input_box.move(50, 105)
        self.input_box.resize(self.width() - 100, 30)  # Растягиваем по ширине и высоте
        self.input_box.setPlaceholderText("Enter text here....")  # Текст-подсказка

        self.label_input_loop = QLabel("Input key:", self)
        self.label_input_loop.move(50, 145)

        self.input_box_loop = QLineEdit(self)
        self.input_box_loop.move(50, 175)
        self.input_box_loop.resize(self.width() - 100, 30)  # Растягиваем по ширине и высоте
        self.input_box_loop.setPlaceholderText("Enter key for coding...")  # Текст-подсказка

        self.open_button = QPushButton("The answer", self)
        self.open_button.clicked.connect(lambda: modul_of_main.click(self))
        self.open_button.move(300, 225)

        self.selected_option = True  # True - первая радиокнопка, False - вторая радиокнопка

        self.text_to_show = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
