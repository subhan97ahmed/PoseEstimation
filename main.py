import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('./src/UI/login.ui', self)
        style_file = open('./src/UI/Hookmark.qss', 'r')
        # Need to move all app styles into this file (QSS). So, we don't need to duplicate styles and just focus on
        # adding elements
        self.setStyleSheet(style_file.read())


# We need to authenticate here. If the user is signed in or not. If signed in then
# show dashboard otherwise login

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    widget = QStackedWidget()
    widget.addWidget(window)
    widget.show()

    try:
        sys.exit(app.exec())
    except:
        print("Exiting")
