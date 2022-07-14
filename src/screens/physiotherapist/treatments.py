import sys
from PyQt5.QtWidgets import QWidget, QApplication, QScrollArea, QHBoxLayout
from firebase_admin import firestore

from src.shared.PatientCard import PatientCard
from src.ui.TherapistTreatmentView import Ui_Treatment


class TTreatments(QWidget, Ui_Treatment):
    def __init__(self, parent=None):
        super(TTreatments, self).__init__(parent)
        self.setupUi(self)
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.hbox = QHBoxLayout()
        print("Therapist treatments")
        self.patients = None
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)
        self.AddPatientBtn.clicked.connect(self.parent().go_to_5)
        self.patients = self.parent().user_info["assigned_patients"]
        if not len(self.patients):
            return
        db = firestore.client()
        patient_index = 0
        patient_card = {}
        for patient in self.patients:
            print("patient: ", patient)
            doc_ref = db.collection(u'users').document(u'' + patient)
            doc = doc_ref.get()
            if doc.exists:
                doc_data = doc.to_dict()
                print("============doc_data: ", doc_data)

                patient_card[patient_index] = PatientCard(
                    frame=self.scrollHolder,
                    patient_info=doc_data,
                    event_func=lambda x: self.onAddTreatment(x),
                )

                self.hbox.insertWidget(patient_index, patient_card[patient_index].PatientCard)

                if patient_index != 0:
                    patient_card[patient_index].PatientCard.move(
                        patient_card[patient_index - 1].PatientCard.rect().x() + patient_card[
                            patient_index - 1].PatientCard.rect().width() + 15,
                        patient_card[patient_index - 1].PatientCard.rect().y())
                patient_index = patient_index + 1

    def onAddTreatment(self, patient_info):
        self.parent().parent().set_hold_data(patient_info)
        print(f"on add treatment: ", patient_info)
        self.parent().parent().go_to_4()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TTreatments()
    MainWindow.show()
    sys.exit(app.exec())
