import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistReportsView import Ui_TherapistReports
from firebase_admin import firestore
from src.shared.PatientReportCard import PatientReportCard



class TReports(QWidget, Ui_TherapistReports):
    def __init__(self, parent=None):
        super(TReports, self).__init__(parent)
        self.setupUi(self)
        print("Therapist reports")
        self.UsernameLabel_2.setText(f'Dr. {self.parent().user_info["f_name"]}')
        self.ProfilepushButton_2.clicked.connect(self.parent().logout_user)
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)
        self.addPatientBtn.clicked.connect(self.parent().go_to_2)
        self.patients = self.parent().user_info["assigned_patients"]
        if not len(self.patients):
            return
        db = firestore.client()
        patient_index = 0
        patient_name_card = {}
        for patient in self.patients:
            print("patient: ", patient)
            doc_ref = db.collection(u'users').document(u'' + patient)
            doc = doc_ref.get()
            if doc.exists:
                doc_data = doc.to_dict()
                print("============doc_data: ", doc_data)

                patient_name_card[patient_index] = PatientReportCard(
                    frame=self.scrollHolder,
                    patient=doc_data,
                    event_func=lambda x: self.onView(x),
                )

                self.hbox.insertWidget(patient_index,patient_name_card[patient_index].PatientNameCard)

                if patient_index != 0:
                    patient_name_card[patient_index].PatientNameCard.move(
                        patient_name_card[patient_index - 1].PatientNameCard.rect().x() + patient_name_card[
                            patient_index - 1].PatientNameCard.rect().width() + 15,
                        patient_name_card[patient_index - 1].PatientNameCard.rect().y())
                patient_index = patient_index + 1

    def onView(self, patient):
        self.parent().parent().set_hold_data(patient)
        print(f"on view: ", patient)
        self.parent().parent().go_to_2()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TReports()
    MainWindow.show()
    sys.exit(app.exec())
