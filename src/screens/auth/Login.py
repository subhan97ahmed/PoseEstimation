import sys

from PyQt5.QtWidgets import QWidget, QApplication

from src.ui.LoginView import Ui_Login


class Login(QWidget, Ui_Login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        print("login")
        # button click method for screen change
        self.CreateAnAcc.clicked.connect(self.parent().go_to_register)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Login()
    MainWindow.show()
    sys.exit(app.exec())
