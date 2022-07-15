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
        # self.StartExerciseBtn.clicked.connect(self.parent().go_to_2)
        self.exercises = self.parent().user_info["assigned_ex"]
        exercise_index = 0
        exercise_card = {}
        for exercise in self.exercises:
            exercise_card[exercise_index] = ExerciseCard(
                frame=self.frame_3,
                exercise_info=exercise,
                event_func=lambda x: self.onStartExercise(x),
            )

            if exercise_index != 0:
                # exercise_card[exercise_index - 1].ExerciseCard.rect().x() +
                if exercise_index % 2 != 0:
                    exercise_card[exercise_index].ExerciseCard.move(exercise_card[
                                                                        exercise_index - 1].ExerciseCard.rect().x(),
                                                                    exercise_card[
                                                                        exercise_index - 1].ExerciseCard.rect().height() + 15
                                                                    )
                else:
                    exercise_card[exercise_index].ExerciseCard.move(exercise_card[
                                                                        exercise_index - 1].ExerciseCard.rect().width() + 80,
                                                                    exercise_card[
                                                                        exercise_index - 1].ExerciseCard.rect().y())

            exercise_index = exercise_index + 1

    def onStartExercise(self, exercise_info):
        self.parent().parent().set_hold_data(exercise_info)
        print(f"on start exercise: ", exercise_info)
        self.parent().parent().go_to_2()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = PExercisePrescribe()
    MainWindow.show()
    sys.exit(app.exec())
