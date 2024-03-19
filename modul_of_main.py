from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QRadioButton, QLabel, \
    QLineEdit, QStyle
import moduls_substitution_cipher


def click(main_window):
    """
     The "The answer" button click handler.
     :param main_window: The main window of the application.
     :return: None
    """
    try:
        # Get text from input fields
        main_window.text_to_show = main_window.input_box.text()
        main_window.text_to_show_loop = main_window.input_box_loop.text()

        # Check which radio button is selected
        if main_window.radio_button1.isChecked():
            # If the first radio button is selected, encode the text
            if main_window.text_to_show:
                main_window.text_to_show = moduls_substitution_cipher.encoding_of_substitution_cipher_using_loop_coding(
                    main_window.text_to_show)
                main_window.text_to_show_loop = ''
            else:
                main_window.text_to_show = "The are some problems with text input."

        elif main_window.radio_button2.isChecked():
            # If the second radio button is selected, decode the text
            if main_window.text_to_show:
                try:
                    if (int(main_window.text_to_show_loop)).is_integer():
                        main_window.text_to_show = moduls_substitution_cipher.encode_coded_str(main_window.text_to_show,
                                                                                               main_window.text_to_show_loop)
                    else:
                        main_window.text_to_show = "The are some problems with the key input."
                except Exception:
                    main_window.text_to_show = "The are some problems with the key input."
            else:
                main_window.text_to_show = "The are some problems with text input."
            main_window.text_to_show_loop = ''

        elif main_window.radio_button3.isChecked():
            # If the third radio button is selected, perform a different operation
            if main_window.text_to_show:
                try:
                    if (int(main_window.text_to_show_loop)).is_integer():
                        main_window.text_to_show = moduls_substitution_cipher.looping_of_substitution_cipher(
                            main_window.text_to_show, main_window.text_to_show_loop)
                    else:
                        main_window.text_to_show = "The are some problems with the key input."
                except Exception:
                    main_window.text_to_show = "The are some problems with the key input."
            else:
                main_window.text_to_show = "The are some problems with text input."
            main_window.text_to_show_loop = ''

        else:
            main_window.text_to_show = "The are some problems with the program"

        # Create and display a dialog box with the result
        dialog = QDialog(main_window)
        dialog.setWindowTitle("The answer")
        dialog.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter, QSize(250, 200),
                                              QApplication.desktop().availableGeometry()))

        label = QLabel(main_window.text_to_show, dialog)
        label.setAlignment(Qt.AlignCenter)
        label.move(50, 50)

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
