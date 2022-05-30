import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.RegisterView import Ui_Register
from src.utils.util import show_warning


class Register(QWidget):

    def __init__(self, parent=None):
        super(Register, self).__init__(parent)

        self.ui = Ui_Register()
        self.ui.setupUi(self)
        # button click method for screen change
        # self.ui.CreateAnAcc_4.clicked.connect(self.parent().go_to_login)
        self.ui.registerBtn.clicked.connect(self.register_submit)

    # Method to get data from text field and print it on clicking register button
    def register_submit(self):
        register_values = {
            'f_name': self.ui.fnameEdit.text(),
            'email': self.ui.emailEdit.text(),
            'password': self.ui.passwordEdit.text(),
            'confirm_pass': self.ui.confirmPasswordEdit.text(),
            'dob': self.ui.dobEdit.date().getDate(),
            'role': self.ui.roleCombo.currentText(),
        }
        print(register_values.values())

        if not ('' in register_values.values()):
            print('working: ', register_values)
        else:
            show_warning(self, message='Invalid, please fill form first!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Register()
    MainWindow.show()
    sys.exit(app.exec())
