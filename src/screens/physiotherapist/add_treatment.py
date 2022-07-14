import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.AddTreatmentView import Ui_AddTreatment
from src.utils.util import is_form_empty, get_age

ex_exercises = ["Wrist Curl", "Thumb Flex", "Squat", "Arm Curl", "Jumping Jacks", "High Knee", "Shoulder Shrug",
                "Lateral Raises", "Quad Stretch"
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
            "exerciseName": self.exerciseName.currentData().lower(),
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
            self.exerciseName.addItem(exercise, exercise)

    def initializer(self, hold_data, user_data):
        self.PatientContactNo.setText('-')
        self.patientName.setText(hold_data['f_name'])
        self.patientEmail.setText(hold_data['email'])
        self.patientAge.setText(str(get_age(hold_data['dob'])))
        self.disease_1.setText(hold_data["diagnosis_1"])
        self.disease_2.setText(hold_data["diagnosis_2"])
        self.disease_3.setText(hold_data["diagnosis_3"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TAddTreatment()
    MainWindow.show()
    sys.exit(app.exec())
