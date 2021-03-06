import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistReportsView import Ui_TherapistReports
from firebase_admin import firestore
from src.shared.PatientReportCard import PatientNameCard


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
        if not ("assigned_patients" in self.parent().user_info):
            return
        self.patients = self.parent().user_info["assigned_patients"]
        self.load_patient_reports(self.patients)

    def load_patient_reports(self, patients):
        if not len(patients):
            return
        db = firestore.client()
        patient_index = 0
        patient_name_card = {}
        for patient in patients:
            print("patient: ", patient)
            doc_ref = db.collection(u'users').document(u'' + patient)
            doc = doc_ref.get()
            if doc.exists:
                doc_data = doc.to_dict()
                print("============doc_data: ", doc_data)

                patient_name_card[patient_index] = PatientNameCard(
                    frame=self.frame,
                    patient=doc_data,
                    event_func=lambda x: self.onView(x),
                )
                if patient_index != 0:
                    if patient_index % 2 != 0:
                        patient_name_card[patient_index].PatientNameCard.move(
                            patient_name_card[
                                patient_index - 1].PatientNameCard.rect().width() + 80,
                            patient_name_card[patient_index - 1].PatientNameCard.rect().y())
                    else:
                        patient_name_card[patient_index].PatientNameCard.move(
                            patient_name_card[
                                patient_index - 1].PatientNameCard.rect().x(),
                            patient_name_card[patient_index - 1].PatientNameCard.rect().height() + 15)
                patient_index = patient_index + 1

    def onView(self, patient):
        self.parent().parent().set_hold_data(patient)
        print(f"on view: ", patient)
        self.parent().parent().go_to_2()

    def initializer(self, hold_data, user_data):
        if not ("assigned_patients" in user_data):
            return
        # if patients are available initially
        self.load_patient_reports(user_data['assigned_patients'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TReports()
    MainWindow.show()
    sys.exit(app.exec())
