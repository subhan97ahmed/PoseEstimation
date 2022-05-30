import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.PatientDashView import Ui_PatientDash


class PDashboard(QWidget, Ui_PatientDash):
    def __init__(self, parent=None):
        super(PDashboard, self).__init__(parent)
        self.setupUi(self)
        print("Patient Dashboard")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = PDashboard()
    MainWindow.show()
    sys.exit(app.exec())
