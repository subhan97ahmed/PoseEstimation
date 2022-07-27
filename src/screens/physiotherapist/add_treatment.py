import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from src.ui.AddTreatmentView import Ui_AddTreatment
from src.utils.static import ex_exercises
from src.utils.util import is_form_empty, get_age, show_warning
from firebase_admin import firestore


class TAddTreatment(QWidget, Ui_AddTreatment):
    def __init__(self, parent=None):
        super(TAddTreatment, self).__init__(parent)
        self.setupUi(self)
        print("Add treatment")
        self.db = firestore.client()
        self.patient = None
        self.exercise_name_populate(ex_exercises)
        self.addPatientBtn.clicked.connect(self.add_exercise_form)
        self.UsernameLabel_2.setText(f'Dr. {self.parent().user_info["f_name"]}')
        self.ProfilepushButton_2.clicked.connect(self.parent().logout_user)
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)

    def add_exercise_form(self):
        add_exercise = {
            "name": self.exerciseName.currentData().lower(),
            "rep_count": int(self.repCount.text()),
            "target_angle": self.angleCount.text(),
            "video_link": self.videoLink.text(),
        }
        print("check: ", add_exercise)
        if is_form_empty(self, add_exercise):
            return

        doc_ref = self.db.collection(u'users').document(u'' + self.patient['uId'])
        therapist_ref = self.db.collection(u'users').document(u'' + self.parent().parent().user_info["uId"])
        doc = doc_ref.get()
        therapist_doc = therapist_ref.get()
        if doc.exists and therapist_doc.exists:
            user_data = doc.to_dict()
            if not 'assigned_ex' in user_data:
                doc_ref.update({**user_data, 'assigned_ex': [add_exercise]})
            else:
                for assignedEx in user_data['assigned_ex']:
                    if add_exercise['name'] == assignedEx['name']:
                        show_warning(self, message='Exercise already assigned')
                        return
                print("user_data['ass_ex_count']: ", self.parent().parent().user_info["ass_ex_count"])
                doc_ref.update({
                    **user_data,
                    "assigned_ex": [*user_data["assigned_ex"], add_exercise]
                })
                therapist_ref.update({
                    **self.parent().parent().user_info,
                    "ass_ex_count": self.parent().parent().user_info["ass_ex_count"] + 1,
                })

                QMessageBox().information(self, "Success", "Exercise added successfully")
                self.parent().parent().go_to_3()

    def exercise_name_populate(self, exercises):
        print("keys: ", exercises)
        for exercise in exercises:
            print("exercise: ", exercise)
            self.exerciseName.addItem(exercise, exercise)

    def initializer(self, hold_data, user_data):
        if hold_data is not None:
            self.PatientContactNo.setText('-')
            self.patientName.setText(hold_data['f_name'])
            self.patientEmail.setText(hold_data['email'])
            self.patientAge.setText(str(get_age(hold_data['dob'])))
            self.disease_1.setText(hold_data["diagnosis_1"])
            self.disease_2.setText(hold_data["diagnosis_2"])
            self.disease_3.setText(hold_data["diagnosis_3"])
            self.patient = hold_data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TAddTreatment()
    MainWindow.show()
    sys.exit(app.exec())
