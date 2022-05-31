import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistReportsView import Ui_TherapistReports


class TReports(QWidget, Ui_TherapistReports):
    def __init__(self, parent=None):
        super(TReports, self).__init__(parent)
        self.setupUi(self)
        print("Therapist reports")

        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TReports()
    MainWindow.show()
    sys.exit(app.exec())
