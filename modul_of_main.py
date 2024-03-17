from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QRadioButton, QLabel, \
    QLineEdit
import moduls_substitution_cipher


def click(main_window):
    result = ''
    try:
        main_window.text_to_show = main_window.input_box.text()
        main_window.text_to_show_loop = main_window.input_box_loop.text()

        if main_window.radio_button1.isChecked():
            main_window.text_to_show = moduls_substitution_cipher.encoding_of_substitution_cipher_using_loop_coding(
                main_window.text_to_show)
        elif main_window.radio_button2.isChecked():
            main_window.text_to_show = moduls_substitution_cipher.encode_coded_str(
                main_window.text_to_show, main_window.text_to_show_loop)
            main_window.text_to_show_loop = ''

        dialog = QDialog(main_window)
        dialog.setWindowTitle("The answer")
        dialog.setGeometry(200, 200, 250, 200)

        label = QLabel(main_window.text_to_show, dialog)
        label.setAlignment(Qt.AlignCenter)
        label.move(50, 50)

        if not main_window.radio_button2.isChecked():
            pass
        label_loop = QLabel(main_window.text_to_show_loop, dialog)
        label_loop.setAlignment(Qt.AlignCenter)
        label_loop.move(50, 80)

        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label_loop)
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.exec_()
    except Exception as e:
        print("Exception occurred:", e)
