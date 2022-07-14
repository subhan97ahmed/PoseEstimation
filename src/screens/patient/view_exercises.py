import sys
from PyQt5.QtWidgets import QWidget, QApplication

from src.shared.ExerciseCard import ExerciseCard
from src.ui.ExercisePrescribeView import Ui_ExercisePrescribe


class PExercisePrescribe(QWidget, Ui_ExercisePrescribe):
    def __init__(self, parent=None):
        super(PExercisePrescribe, self).__init__(parent)
        self.setupUi(self)
        print("Patient View Exercise")
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        # self.TreatmentButton.clicked.connect(self.parent().go_to_1)
        self.ReportButton.clicked.connect(self.parent().go_to_3)
        self.StartExerciseBtn.clicked.connect(self.parent().go_to_2)
        ExerciseCard(
            frame=self.frame_3
            # patient_info=doc_data,
            # event_func=lambda x: self.onAddTreatment(x),
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = PExercisePrescribe()
    MainWindow.show()
    sys.exit(app.exec())
