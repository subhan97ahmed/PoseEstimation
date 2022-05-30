import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.ExercisePrescribeView import Ui_ExercisePrescribe


class PExercisePrescribe(QWidget, Ui_ExercisePrescribe):
    def __init__(self, parent=None):
        super(PExercisePrescribe, self).__init__(parent)
        self.setupUi(self)
        print("Patient View Exercise")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = PExercisePrescribe()
    MainWindow.show()
    sys.exit(app.exec())
