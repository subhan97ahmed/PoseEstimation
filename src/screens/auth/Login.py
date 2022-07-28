import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.LoginView import Ui_Login
from src.utils.util import is_form_empty, show_warning


class Login(QWidget, Ui_Login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        print("login")
        # button click method for screen change
        self.CreateAnAcc.clicked.connect(self.parent().go_to_1)
        self.loginBtn.clicked.connect(self.submit_login)
        self.setStyleSheet(self.styleSheet())

    def user_login_validate(self, reg_values):
        validate = ""
        is_valid = True
        if "@" not in reg_values["email"]:
            validate = "'Email': Enter valid email address\n"
            is_valid = False
        if len(reg_values["password"]) < 6:
            validate = validate+"'Password': must contains at least 6 characters\n"
            is_valid = False
        if not is_valid:
            show_warning(self, message=validate)
        return is_valid

    def submit_login(self):
        login_info = {
            "email": self.emailEdit.text(),
            "password": self.passwordEdit.text(),
        }
        if not is_form_empty(self, login_info) and self.user_login_validate(login_info):
            self.parent().parent().login_user(login_info['email'], login_info['password'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Login()
    MainWindow.show()
    sys.exit(app.exec())
