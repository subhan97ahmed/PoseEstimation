import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.RegisterView import Ui_Register
from src.utils.util import is_form_empty


class Register(QWidget):

    def __init__(self, parent=None):
        super(Register, self).__init__(parent)

        self.ui = Ui_Register()
        self.ui.setupUi(self)
        # button click method for screen change
        self.ui.loginBtn.clicked.connect(self.parent().go_to_0)
        self.ui.registerBtn.clicked.connect(self.register_submit)

    # Method to get data from text field and print it on clicking register button
    def register_submit(self):
        register_values = {
            'f_name': self.ui.fnameEdit.text(),
            'email': self.ui.emailEdit.text(),
            'password': self.ui.passwordEdit.text(),
            'confirm_pass': self.ui.confirmPasswordEdit.text(),
            'dob': str(self.ui.dobEdit.date().toString()),
            'role': self.ui.roleCombo.currentText().lower(),
        }
        if not is_form_empty(self, register_values):
            self.parent().parent().register_user(register_values)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Register()
    MainWindow.show()
    sys.exit(app.exec())
