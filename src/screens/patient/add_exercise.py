from datetime import datetime
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.PatientStartExerciseView import Ui_StartExercise_Patient


class AddExercise(QWidget, Ui_StartExercise_Patient):
    def __init__(self, parent=None):
        super(AddExercise, self).__init__(parent)
        self.setupUi(self)

        self.init_time = None

        print("Patient Add Exercise")
        self.StartExerciseBtn.clicked.connect(self.initialize_exercise)

        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_1)
        self.ReportButton.clicked.connect(self.parent().go_to_3)

    def initialize_exercise(self):
        self.init_time = datetime.now()

    def timer_diff(self):
        end_time = datetime.now()
        return (end_time - self.init_time).total_seconds()

    def submit_exercise(self):
        print("submit")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = AddExercise()
    MainWindow.show()
    sys.exit(app.exec())
