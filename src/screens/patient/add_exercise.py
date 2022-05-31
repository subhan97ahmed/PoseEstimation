import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.PatientStartExerciseView import Ui_StartExercise_Patient


class AddExercise(QWidget, Ui_StartExercise_Patient):
    def __init__(self, parent=None):
        super(AddExercise, self).__init__(parent)
        self.setupUi(self)
        print("Patient Add Exercise")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = AddExercise()
    MainWindow.show()
    sys.exit(app.exec())
