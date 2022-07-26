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

    def initializer(self, hold_data, user_data):
        self.NoOfExPrescribedLabel.setText(str(len(user_data['assigned_ex'])))
        ex_count = 0
        for history in user_data["histories"]:
            ex_count += len(history)
        self.NoOfExLabel.setText(str(ex_count))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = PDashboard()
    MainWindow.show()
    sys.exit(app.exec())
