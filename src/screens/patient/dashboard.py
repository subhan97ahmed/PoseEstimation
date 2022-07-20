import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.PatientDashView import Ui_PatientDash


class PDashboard(QWidget, Ui_PatientDash):
    def __init__(self, parent=None):
        super(PDashboard, self).__init__(parent)
        self.setupUi(self)
        print("Patient Dashboard")
        self.UsernameLabel.setText(self.parent().user_info["f_name"])
        self.ProfilepushButton.clicked.connect(self.parent().logout_user)
        # self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_1)
        self.ReportButton.clicked.connect(self.parent().go_to_3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = PDashboard()
    MainWindow.show()
    sys.exit(app.exec())
