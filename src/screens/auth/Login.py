import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.LoginView import Ui_Login
from src.utils.util import is_form_empty
from src.utils.static import addonStyles

#todo: remove this after work
static_login_info = {
            "email": 'posetest@yopmail.com',
            "password": '123456',
        }

class Login(QWidget, Ui_Login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        print("login")
        # button click method for screen change
        self.CreateAnAcc.clicked.connect(self.parent().go_to_1)
        self.loginBtn.clicked.connect(self.submit_login)
        self.setStyleSheet(self.styleSheet() + addonStyles)

    def submit_login(self):
        login_info = {
            "email": self.emailEdit.text(),
            "password": self.passwordEdit.text(),
        }
        if not is_form_empty(self, static_login_info):
            self.parent().parent().login_user(static_login_info['email'], static_login_info['password'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Login()
    MainWindow.show()
    sys.exit(app.exec())
