import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.AddTreatmentView import Ui_AddTreatment
from src.utils.util import is_form_empty

ex_exercises = [
    {
        "name": "Bicep Curl",
        "id": 1
    }
]


class TAddTreatment(QWidget, Ui_AddTreatment):
    def __init__(self, parent=None):
        super(TAddTreatment, self).__init__(parent)
        self.setupUi(self)
        print("Add treatment")
        self.exercise_name_populate(ex_exercises)
        self.addPatientBtn.clicked.connect(self.add_exercise_form)

        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)

    def add_exercise_form(self):
        add_exercise = {
            "exerciseName": self.exerciseName.currentData(),
            "rep": self.repCount.text(),
            "angle": self.angleCount.text(),
            "videoLink": self.videoLink.text(),
        }
        print("check: ", add_exercise)
        if is_form_empty(self, add_exercise):
            return
        print("submit: ", add_exercise)

    def exercise_name_populate(self, exercises):
        print("keys: ", exercises)
        for exercise in exercises:
            print("exercise: ", exercise)
            self.exerciseName.addItem(exercise['name'], exercise['name'])

    def initializer(self):
        print(f"patient data treatment: {self.parent().parent().hold_info}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TAddTreatment()
    MainWindow.show()
    sys.exit(app.exec())
