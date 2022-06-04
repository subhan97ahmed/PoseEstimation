import sys
from PyQt5.QtWidgets import QWidget, QApplication
from firebase_admin import firestore
from src.ui.AddPatientView import Ui_AddPatient
from src.utils.util import is_form_empty, get_age


class TAddPatient(QWidget, Ui_AddPatient):
    def __init__(self, parent=None):
        super(TAddPatient, self).__init__(parent)
        self.setupUi(self)
        print("Add patient")
        self.diagnose1.setText("-")
        self.diagnose2.setText("-")
        self.diagnose3.setText("-")
        self.patientName_2.setText("-")
        self.patientEmail_3.setText("-")
        self.PatientContactNo_3.setText("-")
        self.patientAge_2.setText("-")
        self.db = firestore.client()
        self.patients = None
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
        self.patients = self.db.collection(u'users').where(u'role', u'==', 'patient').stream()
        print("self.patients", self.patients)
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
                self.patientName_2.setText(pat["f_name"])
                self.patientEmail_3.setText(pat["email"])
                dob = get_age(pat["dob"])
                self.patientAge_2.setText(str(dob))
                if "diagnosis_1" in pat and "diagnosis_2" in pat and "diagnosis_3" in pat:
                    self.diagnose1.setText(pat["diagnosis_1"])
                    self.diagnose2.setText(pat["diagnosis_2"])
                    self.diagnose3.setText(pat["diagnosis_3"])
                    self.disease_1.setText(pat["diagnosis_1"])
                    self.disease_2.setText(pat["diagnosis_2"])
                    self.disease_3.setText(pat["diagnosis_3"])

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

        patient_info = self.db.collection(u'users').document(u'' + self.patient_data["uId"])
        patient_info.update(self.patient_data)
        print("patient_info: ", patient_info.get())
        therapist_info = self.db.collection(u'users').document(u'' + self.parent().parent().user_info["uId"])
        print("get_therapist_assigned: ", therapist_info)
        get_therapist_info = therapist_info.get()
        therapist_dict = get_therapist_info.to_dict()
        print("therapist_dict: ", therapist_dict)
        if not "assigned_patients" in therapist_dict:
            print("therapist_dict not contains", self.patient_data["uId"])
            therapist_info.update({**therapist_dict, "assigned_patients": [self.patient_data["uId"]]})
        else:
            if not self.patient_data["uId"] in therapist_dict["assigned_patients"]:
                print("therapist_dict contains", self.patient_data["uId"])
                therapist_info.update({
                    **therapist_dict,
                    "assigned_patients": [*therapist_dict["assigned_patients"], self.patient_data["uId"]]
                })

        self.parent().parent().go_to_3()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TAddPatient()
    MainWindow.show()
    sys.exit(app.exec())
