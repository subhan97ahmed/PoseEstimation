import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.AddPatientView import Ui_AddPatient
from src.utils.util import is_form_empty


class TAddPatient(QWidget, Ui_AddPatient):
    def __init__(self, parent=None):
        super(TAddPatient, self).__init__(parent)
        self.setupUi(self)
        print("Add patient")
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

    def initial_diagnosis_form(self):
        initial_diagnoses = {
            "diagnosis_1": self.diagnose1.text(),
            "diagnosis_2": self.diagnose2.text(),
            "diagnosis_3": self.diagnose3.text(),
        }
        if is_form_empty(self, initial_diagnoses):
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TAddPatient()
    MainWindow.show()
    sys.exit(app.exec())
