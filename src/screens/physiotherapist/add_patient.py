import sys
from PyQt5.QtWidgets import QWidget, QApplication
from firebase_admin import firestore
from src.ui.AddPatientView import Ui_AddPatient
from src.utils.util import is_form_empty


class TAddPatient(QWidget, Ui_AddPatient):
    def __init__(self, parent=None):
        super(TAddPatient, self).__init__(parent)
        self.setupUi(self)
        print("Add patient")
        self.diagnose1.setText("-")
        self.diagnose2.setText("-")
        self.diagnose3.setText("-")
        self.db = firestore.client()
        self.patients = self.db.collection(u'users').where(u'role', u'==', 'patient').stream()
        self.patient_data = None

        self.searchPatientBtn.clicked.connect(self.search_patient_form)
        self.addPatientBtn.clicked.connect(self.initial_diagnosis_form)

        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)

    def search_patient_form(self):
        search_patient = {
            "email": self.patientEmail.text(),
        }
        if is_form_empty(self, search_patient):
            return
        for patient in self.patients:
            pat = patient.to_dict()
            if pat["email"] == search_patient["email"]:
                self.patient_data = {
                    "uId": patient.id,
                    **pat
                }
                print("patient_data: ", self.patient_data)

    def initial_diagnosis_form(self):
        initial_diagnoses = {
            "diagnosis_1": self.diagnose1.text(),
            "diagnosis_2": self.diagnose2.text(),
            "diagnosis_3": self.diagnose3.text(),
        }
        if is_form_empty(self, initial_diagnoses):
            return
        self.patient_data = {
            **self.patient_data,
            **initial_diagnoses
        }
        print("self.patient_data: ", self.patient_data)
        print("therapist id: ", self.parent().parent().user_info["uId"])

        patient_info = self.db.collection(u'users').document(self.patient_data["uId"])
        patient_info.update(self.patient_data["uId"])
        therapist_info = self.db.collection(u'users').document(self.parent().parent().user_info["uId"])
        therapist_data = therapist_info.get()
        print("check data: ", therapist_data, [self.patient_data["uId"], *therapist_data.patients])
        # therapist_info.update({//
        # self.parent().parent().go_to_



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TAddPatient()
    MainWindow.show()
    sys.exit(app.exec())
