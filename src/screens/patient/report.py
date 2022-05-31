import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistReportView import Ui_TherapistReport


class TReport(QWidget, Ui_TherapistReport):
    def __init__(self, parent=None):
        super(TReport, self).__init__(parent)
        self.setupUi(self)
        print("Therapist report")
        # Todo: Generate update report file to update text
        self.TreatmentButton.setText('Exercise')
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_1)
        # self.ReportButton.clicked.connect(self.parent().go_to_3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TReport()
    MainWindow.show()
    sys.exit(app.exec())
