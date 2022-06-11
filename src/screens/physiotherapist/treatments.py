import sys
from PyQt5.QtWidgets import QWidget, QApplication
from firebase_admin import firestore

from src.ui.TherapistTreatmentView import Ui_Treatment


class TTreatments(QWidget, Ui_Treatment):
    def __init__(self, parent=None):
        super(TTreatments, self).__init__(parent)
        self.setupUi(self)
        print("Therapist treatments")
        self.patients = None
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)
        self.AddPatientBtn.clicked.connect(self.parent().go_to_5)
        # self.verticalLayout_2

    def initializer(self):
        print("print")
        self.patients = self.parent().parent().user_info["assigned_patients"]
        db = firestore.client()
        for patient in self.patients:
            print("patient: ", patient)
            doc_ref = db.collection(u'users').document(u'' + patient)
            doc = doc_ref.get()
            print("user: ", doc)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TTreatments()
    MainWindow.show()
    sys.exit(app.exec())
