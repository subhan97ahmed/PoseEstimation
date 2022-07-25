import sys
from PyQt5.QtWidgets import QWidget, QApplication, QScrollArea, QHBoxLayout
from firebase_admin import firestore

from src.shared.PatientCard import PatientCard
from src.ui.TherapistTreatmentView import Ui_Treatment


class TTreatments(QWidget, Ui_Treatment):
    def __init__(self, parent=None):
        super(TTreatments, self).__init__(parent)
        self.setupUi(self)
        print("Therapist treatments", self.parent().user_info)
        self.patients = []
        self.UsernameLabel_2.setText(f'Dr. {self.parent().user_info["f_name"]}')
        self.ProfilepushButton_2.clicked.connect(self.parent().logout_user)
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)
        self.AddPatientBtn.clicked.connect(self.parent().go_to_5)
        if not ("assigned_patients" in self.parent().user_info):
            return
        self.patients = self.parent().user_info["assigned_patients"]
        # if patients are available initially
        self.load_patients(self.patients)

    def load_patients(self, patients):
        if not len(patients):
            return
        db = firestore.client()
        patient_index = 0
        patient_card = {}
        for patient in patients:
            print("patient: ", patient)
            doc_ref = db.collection(u'users').document(u'' + patient)
            doc = doc_ref.get()
            if doc.exists:
                doc_data = doc.to_dict()
                print("============doc_data: ", doc_data)

                patient_card[patient_index] = PatientCard(
                    frame=self.frame,
                    patient_info=doc_data,
                    event_func=lambda x: self.onAddTreatment(x),
                )

                if patient_index != 0:
                    if patient_index % 2 != 0:
                        patient_card[patient_index].PatientCard.move(
                            patient_card[
                                patient_index - 1].PatientCard.rect().width() + 60,
                            patient_card[patient_index - 1].PatientCard.rect().y())
                    else:
                        patient_card[patient_index].PatientCard.move(
                            patient_card[
                                patient_index - 1].PatientCard.rect().x(),
                            patient_card[patient_index - 1].PatientCard.rect().height() + 15)

                patient_index = patient_index + 1

    def onAddTreatment(self, patient_info):
        self.parent().parent().set_hold_data(patient_info)
        print(f"on add treatment: ", patient_info)
        self.parent().parent().go_to_4()

    def initializer(self, hold_data, user_data):
        if not ("assigned_patients" in user_data):
            return
        # if patients are available initially
        self.load_patients(user_data["assigned_patients"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TTreatments()
    MainWindow.show()
    sys.exit(app.exec())
