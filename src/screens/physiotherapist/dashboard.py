import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistDashboardView import Ui_Dashboard


class TDashboard(QWidget, Ui_Dashboard):
    def __init__(self, parent=None):
        super(TDashboard, self).__init__(parent)
        self.setupUi(self)
        print("Therapist Dashboard")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TDashboard()
    MainWindow.show()
    sys.exit(app.exec())
