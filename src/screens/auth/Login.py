import sys
from src.ui.LoginView import Ui_MainWindow
from PyQt6 import QtWidgets, QtCore, QtGui
from src.utils.util import some_func


class Login(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        # set icons folder path here
        QtCore.QDir.addSearchPath('icons', '../../../assets/icons/')
        # set images folder path here
        QtCore.QDir.addSearchPath('images', '../../../assets/Images/')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login()
    ui.ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
