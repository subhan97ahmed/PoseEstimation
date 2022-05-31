# This file should be the main entry point for the application.
# Connect firebase here. So, we can have an auth key and point the redirection
# either patient or physiotherapist
import sys
import firebase_admin
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QDesktopWidget
from firebase import Firebase
from firebase_admin import credentials, firestore
from src.json.FirebaseConfig import firebaseConfig
from src.screens.auth import Login, Register
from src.screens.patient import add_exercise, view_exercises, report as pat_report, dashboard as pat_dashboard
from src.screens.physiotherapist import dashboard as th_dashboard, report as th_report, reports, add_patient, add_treatment, treatments
from src.utils.util import show_warning


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        # set info for sharing across widgets
        self.user_info = None
        self.hold_info = None
        # instantiate for screens
        # Therapist
        self.screen_t_dashboard = th_dashboard.TDashboard(self)
        self.screen_t_reports = reports.TReports(self)
        self.screen_t_report = th_report.TReport(self)
        self.screen_t_treatments = treatments.TTreatments(self)
        self.screen_t_add_treatment = add_treatment.TAddTreatment(self)
        self.screen_t_add_patient = add_patient.TAddPatient(self)
        # Patient
        self.screen_p_dashboard = pat_dashboard.PDashboard(self)
        self.screen_p_view_exercise = view_exercises.PExercisePrescribe(self)
        self.screen_p_add_exercise = add_exercise.AddExercise(self)
        self.screen_p_report = pat_report.TReport(self)
        # Auth
        self.screen_login = Login.Login(self)
        self.screen_register = Register.Register(self)
        # Set style for the main window
        self.setStyleSheet("background-color: #e2f6ff;")

        # for centering view
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move((qr.topLeft() / 1.8))

        # initialize firebase
        cred = credentials.Certificate('src/json/posefect-firebase-adminsdk.json')
        self.firebase_admin = firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://posefect-b48b9-default-rtdb.firebaseio.com/'
        })
        self.firebase = Firebase(firebaseConfig)

        # for navigation
        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)
        # init is responsible for opening screens per role base
        self.init_screen('')
        self.show()

    # To share data across widgets, main.py can act as a store to hold and share data
    def set_data(self, info):
        self.hold_info = info

    def get_data(self):
        return self.hold_info

    def get_user_data(self):
        return self.user_info

    # Initializing screens widget for navigation
    def init_screen(self, user_type: str):
        if user_type.lower() == 'therapist':
            self.stacked.removeWidget(self.screen_login)
            self.stacked.removeWidget(self.screen_register)
            self.stacked.addWidget(self.screen_t_dashboard)
            self.stacked.addWidget(self.screen_t_reports)
            self.stacked.addWidget(self.screen_t_report)
            self.stacked.addWidget(self.screen_t_treatments)
            self.stacked.addWidget(self.screen_t_add_treatment)
            self.stacked.addWidget(self.screen_t_add_patient)
            print('therapist')
            self.setFixedWidth(1024)
            self.setFixedHeight(680)
        elif user_type.lower() == 'patient':
            self.stacked.removeWidget(self.screen_login)
            self.stacked.removeWidget(self.screen_register)
            self.stacked.addWidget(self.screen_p_dashboard)
            self.stacked.addWidget(self.screen_p_view_exercise)
            self.stacked.addWidget(self.screen_p_add_exercise)
            self.stacked.addWidget(self.screen_p_report)
            print('patient')
            self.setFixedWidth(1024)
            self.setFixedHeight(680)
        else:
            self.stacked.addWidget(self.screen_login)
            self.stacked.addWidget(self.screen_register)
            print('auth')

    def login_user(self, email, password):
        print("login: ", email, password)
        try:
            user = self.firebase.auth().sign_in_with_email_and_password(email, password)
            print(user)
            db = firestore.client()
            print(db)
            doc_ref = db.collection(u'users').document(u'' + user['localId'])
            doc = doc_ref.get()
            if doc.exists:
                print(f'Document data: {doc.to_dict()}')
                user_data = doc.to_dict()
                self.user_info = {
                    "uId": user['localId'],
                }
                self.init_screen(user_data["role"])
            else:
                show_warning(self, message="User not found")
        except:
            show_warning(self, message="Something went wrong")

    def register_user(self, user_data):
        try:
            new_user = self.firebase.auth().create_user_with_email_and_password(user_data['email'],
                                                                                user_data['password'])
            self.user_info = new_user
            db = firestore.client()
            db.collection(u'users').document(u'' + new_user['localId']).set(user_data)
            self.type_base_screens_init(user_data["role"])
            self.init_screen(user_data["role"])
        except:
            show_warning(self, title="Warning", message="failed to register")

    def go_to_0(self):
        self.stacked.setCurrentIndex(0)

    def go_to_1(self):
        self.stacked.setCurrentIndex(1)

    def go_to_2(self):
        self.stacked.setCurrentIndex(2)

    def go_to_3(self):
        self.stacked.setCurrentIndex(3)

    def go_to_4(self):
        self.stacked.setCurrentIndex(4)

    def go_to_5(self):
        self.stacked.setCurrentIndex(5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = App()
    MainWindow.show()
    sys.exit(app.exec())
