import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.AddPatientView import Ui_AddPatient


class TAddPatient(QWidget, Ui_AddPatient):
    def __init__(self, parent=None):
        super(TAddPatient, self).__init__(parent)
        self.setupUi(self)
        print("Add patient")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TAddPatient()
    MainWindow.show()
    sys.exit(app.exec())
