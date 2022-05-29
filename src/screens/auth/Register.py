import sys

from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.RegisterView import Ui_Register


class Register(QWidget):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)

        self.ui = Ui_Register()
        self.ui.setupUi(self)
        print("register")
        # button click method for screen change
        self.ui.CreateAnAcc_4.clicked.connect(self.parent().go_to_login)

    #def RegisterClick(self):
     #   self.pushButton_4.clicked.connect(self.on_Click)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Register()
    MainWindow.show()
    sys.exit(app.exec())