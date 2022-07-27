import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistDashboardView import Ui_Dashboard


class TDashboard(QWidget, Ui_Dashboard):
    def __init__(self, parent=None):
        super(TDashboard, self).__init__(parent)
        self.setupUi(self)
        if not self.parent().user_info:
            return
        info = self.parent().user_info
        self.UsernameLabel.setText(f'Dr. {info["f_name"]}')
        self.ProfilepushButton.clicked.connect(self.parent().logout_user)
        # Links
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)
        self.NoOfPatientsLabel.setText(str(self.parent().user_info['ass_ex_count']))
        self.NoofActivePatientsLabel.setText(str(len(self.parent().user_info['assigned_patients'])))
        self.is_loaded = False

    def initializer(self, hold_data, user_data):
        if self.is_loaded:
            print("reload user")
            self.parent().parent().reload_user_data()
        self.is_loaded = True
        print("===dashboard: ", hold_data, user_data)
        self.NoOfPatientsLabel.setText(str(user_data['ass_ex_count']))
        self.NoofActivePatientsLabel.setText(str(len(user_data['assigned_patients'])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TDashboard()
    MainWindow.show()
    sys.exit(app.exec())
