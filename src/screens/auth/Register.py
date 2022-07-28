import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.RegisterView import Ui_Register
from src.utils.util import is_form_empty, show_warning


class Register(QWidget):

    def __init__(self, parent=None):
        super(Register, self).__init__(parent)

        self.ui = Ui_Register()
        self.ui.setupUi(self)
        # button click method for screen change
        self.ui.loginBtn.clicked.connect(self.parent().go_to_0)
        self.ui.registerBtn.clicked.connect(self.register_submit)

    def user_register_validate(self, reg_values):
        validate = ""
        is_valid = True
        if "@" not in reg_values["email"]:
            validate = "'Email': Enter valid email address\n"
            is_valid = False
        if len(reg_values["password"]) < 6:
            validate = validate+"'Password': must contains at least 6 characters\n"
            is_valid = False
        if reg_values["password"] != reg_values["confirm_pass"]:
            validate = validate+"'Confirm Password': It's not same as password\n"
            is_valid = False
        if not is_valid:
            show_warning(self, message=validate)
        return is_valid

    # Method to get data from text field and print it on clicking register button
    def register_submit(self):
        if self.ui.roleCombo.currentText().lower() == "patient":
            info = {"histories": [], "assigned_ex": []}
        else:
            info = {"ass_ex_count": 0}
        register_values = {
            'f_name': self.ui.fnameEdit.text(),
            'email': self.ui.emailEdit.text(),
            'password': self.ui.passwordEdit.text(),
            'confirm_pass': self.ui.confirmPasswordEdit.text(),
            'dob': str(self.ui.dobEdit.date().toString()),
            'role': self.ui.roleCombo.currentText().lower(),
            **info
        }
        if not is_form_empty(self, register_values) and self.user_register_validate(register_values):
            self.parent().parent().register_user(register_values)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Register()
    MainWindow.show()
    sys.exit(app.exec())
