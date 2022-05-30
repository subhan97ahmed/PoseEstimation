# This file should be the main entry point for the application.
# Connect firebase here. So, we can have an auth key and point the redirection
# either patient or physiotherapist
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QDesktopWidget

from src.screens.auth import Login, Register
from src.screens.patient import add_exercise, view_exercises, report, dashboard as pDashboard
import firebase_admin
from firebase_admin import credentials

user_type_x = ''


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        # for centering view
        self.setStyleSheet("background-color: #e2f6ff;")
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # initialize firebase
        cred = credentials.Certificate('src/json/posefect-firebase-adminsdk.json')
        firebase_admin.initialize_app(cred,
                                      {
                                          'databaseURL': 'https://posefect-b48b9-default-rtdb.firebaseio.com/'
                                      })

        # initialize screens instances accordingly
        if user_type_x == 'therapist':
            print('test 1')
        elif user_type_x == 'patient':
            print('test 2')
        else:
            self.screen_login = Login.Login(self)
            self.screen_register = Register.Register(self)

        # for navigation
        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)
        # init is responsible for opening screens per role base
        self.init_screen(user_type_x)
        self.show()

    def init_screen(self, user_type: str = ''):
        if user_type.lower() == 'therapist':
            self.stacked.removeWidget(self.screen_login)
            self.stacked.removeWidget(self.screen_register)

            # self.stacked.addWidget(self.)
            print('therapist')

        elif user_type.lower() == 'patient':
            self.stacked.removeWidget(self.screen_login)
            self.stacked.removeWidget(self.screen_register)

            # self.stacked.addWidget(self.)
            print('patient')

        else:

            self.stacked.addWidget(self.screen_login)
            self.stacked.addWidget(self.screen_register)
            print('auth')

    def go_to_login(self):
        self.stacked.setCurrentIndex(0)

    def go_to_register(self):
        self.stacked.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = App()
    MainWindow.show()
    sys.exit(app.exec())
