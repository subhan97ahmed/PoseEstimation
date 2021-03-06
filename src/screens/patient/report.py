import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistReportView import Ui_TherapistReport
import pyqtgraph as pg

from src.utils.static import ex_exercises
from src.utils.util import get_age, get_exercise_history, get_history_range, show_warning, compare_date


class TReport(QWidget, Ui_TherapistReport):
    def __init__(self, parent=None):
        super(TReport, self).__init__(parent)
        self.setupUi(self)
        print("Patient report")
        self.TreatmentButton.setText('Exercises')
        self.UsernameLabel_2.setText(self.parent().user_info["f_name"])
        self.ProfilepushButton_2.clicked.connect(self.parent().logout_user)
        # Links
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_1)
        self.ReportButton.clicked.connect(self.parent().go_to_3)

        self.patient = self.parent().user_info
        self.patientName_3.setText(self.patient['f_name'])
        self.patientEmail_4.setText(self.patient['email'])
        self.PatientContactNo_4.setText('-')
        self.patientAge_3.setText(get_age(self.patient['dob']))
        self.disease_4.setText(self.patient["diagnosis_1"])
        self.disease_5.setText(self.patient["diagnosis_2"])
        self.disease_6.setText(self.patient["diagnosis_3"])

        self.search_patient_btn.clicked.connect(self.search_exercise_form)
        self.exercise_name_populate(ex_exercises)
        self.graphWidget = pg.PlotWidget()
        self.scrollArea.setWidget(self.graphWidget)
        self.graphWidget.setBackground('w')
        self.graphWidget.setLabel('left', "<span style=\"color:blue;font-size:20px\">Score (%)</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:blue;font-size:20px\">Time (Days)</span>")

    def exercise_name_populate(self, exercises):
        print("keys: ", exercises)
        for exercise in exercises:
            print("exercise: ", exercise)
            self.exerciseName.addItem(exercise, exercise)

    def search_exercise_form(self):
        add_exercise = {
            "ex_name": self.exerciseName.currentData().lower(),
            "start_date": self.start_date.date(),
            "end_date": self.end_date.date(),
        }
        print("check: ", add_exercise)
        if compare_date(self, ex_range=add_exercise) is None:
            return
        self.graph_plotting(exercise_info=add_exercise)

    def graph_plotting(self, exercise_info):
        # this data will come from firebase
        pen = pg.mkPen(color=(0, 0, 220), width=5)
        ex_history_info = get_exercise_history(self, self.patient['histories'], exercise_info['ex_name'])
        print('=== history: ', ex_history_info)
        if ex_history_info is None:
            show_warning(self, message=f"No history found for exercise {exercise_info['ex_name']}")
            return
        ex_history = get_history_range(ex_history_info, exercise_info)
        print("history: ", ex_history)
        # plot data: x, y values
        self.graphWidget.plot(ex_history['days'], ex_history['score'], pen=pen,
                              symbol='o', symbolSize=15, symbolBrush='b')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TReport()
    MainWindow.show()
    sys.exit(app.exec())
