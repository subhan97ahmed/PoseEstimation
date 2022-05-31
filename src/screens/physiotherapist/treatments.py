import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistTreatmentView import Ui_Treatment


class TTreatments(QWidget, Ui_Treatment):
    def __init__(self, parent=None):
        super(TTreatments, self).__init__(parent)
        self.setupUi(self)
        print("Therapist treatments")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TTreatments()
    MainWindow.show()
    sys.exit(app.exec())