import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistDashboardView import Ui_Dashboard


class TDashboard(QWidget, Ui_Dashboard):
    def __init__(self, parent=None):
        super(TDashboard, self).__init__(parent)
        self.setupUi(self)
        if not self.parent().user_info:
            return
        print("Therapist Dashboard: ", self.parent().user_info)
        # self.UsernameLabel.setText(f'Dr. {self.parent().user_info.f_name}')
        # self.NoOfPatientsLabel.setText(len(self.parent().user_info.patients))
        # self.NoofActivePatientsLabel.setText(sum(True for d in self.parent().user_info.patients if ))

        # Links
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TDashboard()
    MainWindow.show()
    sys.exit(app.exec())
