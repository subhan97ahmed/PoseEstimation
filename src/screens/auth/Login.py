import sys
from src.ui.LoginView import Ui_Login
from PyQt5 import QtWidgets


class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent=parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # button click method for screen change
        self.ui.loginBtn.clicked.connect(self.RegisterScreen)

    def RegisterScreen(self):
        from src.ui.RegisterView import Ui_Register
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window2)
        self.window2.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Login()
    MainWindow.show()
    sys.exit(app.exec())
