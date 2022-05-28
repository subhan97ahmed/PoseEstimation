import sys
from src.ui.RegisterView import Ui_Register
from PyQt5 import QtWidgets, QtCore, QtGui
from src.utils.util import some_func


class Register(QtWidgets.QWidget):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    def __init__(self, parent=None):
        super(Register, self).__init__(parent=parent)

        self.ui = Ui_Register()
        self.ui.setupUi(self)

        # button click method for screen change
        # self.ui.CreateAnAcc_3.clicked.connect(self.LoginScreen)
        self.ui.pushButton_4.clicked.connect(self.LoginScreen)

    def LoginScreen(self):
        from src.ui.LoginView import Ui_Login
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window2)
        self.window2.show()
        self.close()

    def RegisterScreen(self):
        from src.ui.RegisterView import Ui_Register
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.window2)
        self.window2.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Register()
    MainWindow.show()
    sys.exit(app.exec())
