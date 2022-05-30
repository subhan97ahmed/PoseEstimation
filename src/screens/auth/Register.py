import sys

from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.RegisterView import Ui_Register



class Register(QWidget):




    def __init__(self, parent=None):
        super(Register, self).__init__(parent)

        self.ui = Ui_Register()
        self.ui.setupUi(self)
        print("Register")
        # button click method for screen change
        #self.ui.CreateAnAcc_4.clicked.connect(self.parent().go_to_login)


# Method to get data from text field and print it on clicking register button
    def btnFun(self):
        self.ui.pushButton_4.clicked.connect(self.clickMe())

    def getFname(self):
        print(self.ui.lineEdit_10.text())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Register()
    MainWindow.show()
    sys.exit(app.exec())