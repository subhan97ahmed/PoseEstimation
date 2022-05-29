# This file should be the main entry point for the application.
# Connect firebase here. So, we can have an auth key and point the redirection
# either patient or physiotherapist
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget
from firebase_admin import auth
from src.screens.auth import Login, Register

user_type_x = ''


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)
        # init is responsible for opening screens per role base
        self.init_screen(user_type_x)
        self.show()

    def init_screen(self, user_type: str = ''):
        if user_type.lower() == 'therapist':
            # self.stacked.addWidget(self.)
            print('therapist')

        elif user_type.lower() == 'patient':
            # self.stacked.addWidget(self.)
            print('patient')

        else:
            login = Login.Login(self)
            register = Register.Register(self)
            self.stacked.addWidget(login)
            self.stacked.addWidget(register)
            print('auth')
            print('screen: ' + self.stacked.currentWidget().objectName() + ' ' + str(self.stacked.currentIndex()))

    def go_to_login(self):
        self.stacked.setCurrentIndex(0)

    def go_to_register(self):
        self.stacked.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = App()
    MainWindow.show()
    sys.exit(app.exec())
