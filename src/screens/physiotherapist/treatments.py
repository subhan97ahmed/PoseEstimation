import sys
from PyQt5.QtWidgets import QWidget, QApplication, QScrollArea, QVBoxLayout, QLabel
from firebase_admin import firestore

from src.shared.PatientCard import PatientCard
from src.ui.TherapistTreatmentView import Ui_Treatment
from src.utils.util import get_age


class TTreatments(QWidget, Ui_Treatment):
    def __init__(self, parent=None):
        super(TTreatments, self).__init__(parent)
        self.setupUi(self)
        self.scroll = QScrollArea(self.scrollHolder)  # Scroll Area which contains the widgets, set as the centralWidget
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        print("Therapist treatments")
        self.patients = None
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)
        self.AddPatientBtn.clicked.connect(self.parent().go_to_5)

    # @firestore.async_transactional
    def initializer(self):
        print("print")
        self.patients = self.parent().parent().user_info["assigned_patients"]
        if not len(self.patients):
            return

        db = firestore.client()
        for patient in self.patients:
            print("patient: ", patient)
            doc_ref = db.collection(u'users').document(u'' + patient)
            doc = doc_ref.get()
            if doc.exists:
                doc_data = doc.to_dict()
                print("============doc_data: ", doc_data)
                card_info = QLabel(f"name={doc_data['f_name']}, age={get_age(doc_data['dob'])},"
                                   f"disease1={doc_data['diagnosis_1']}, disease2={doc_data['diagnosis_2']}"
                                   f"disease3={doc_data['diagnosis_3']}")
                # patient_card = PatientCard(
                #                            frame=self.frame,
                #                            name=doc_data["f_name"],
                #                            age=get_age(doc_data["dob"]),
                #                            disease1=doc_data["diagnosis_1"],
                #                            disease2=doc_data["diagnosis_2"],
                #                            disease3=doc_data["diagnosis_3"]
                # )
                self.vbox.addWidget(card_info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TTreatments()
    MainWindow.show()
    sys.exit(app.exec())
