from PyQt5 import QtCore, QtGui, QtWidgets
import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc


class ExerciseCard:
    def __init__(self, frame, exercise_info, event_func=any):
        _translate = QtCore.QCoreApplication.translate
        self.ExerciseCard = QtWidgets.QWidget(frame)
        self.ExerciseCard.setGeometry(QtCore.QRect(0, 0, 331, 151))
        self.ExerciseCard.setStyleSheet("background-color: #f0f4c3;\n"
                                        "border-radius: 10px;")
        self.ExerciseCard.setObjectName("ExerciseCard")
        self.label = QtWidgets.QLabel(self.ExerciseCard)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setObjectName("label")
        self.RepCount = QtWidgets.QLabel(self.ExerciseCard)
        self.RepCount.setGeometry(QtCore.QRect(90, 50, 221, 21))
        self.RepCount.setObjectName("RepCount")
        self.label.setText(_translate("ExercisePrescribe",
                                      "<html><head/><body><p><img src=\":/iconPrefix/exercise.png\"/></p></body></html>"))
        self.RepCount.setText(_translate("ExercisePrescribe", "Rep x"))
        self.ExerciseName = QtWidgets.QLabel(self.ExerciseCard)
        self.ExerciseName.setGeometry(QtCore.QRect(90, 20, 221, 31))
        self.ExerciseName.setObjectName("ExerciseName")
        self.StartExerciseBtn = QtWidgets.QPushButton(self.ExerciseCard)
        self.StartExerciseBtn.setText(_translate("ExercisePrescribe", "Start Exercise"))
        self.StartExerciseBtn.setGeometry(QtCore.QRect(190, 100, 131, 41))
        self.StartExerciseBtn.setStyleSheet("border-radius: 20px;\n"
                                            "background-color: rgb(249, 168, 37);\n"
                                            "")
        self.StartExerciseBtn.setObjectName("StartExerciseBtn")
        # set values
        self.ExerciseName.setText(_translate("ExercisePrescribe", str(exercise_info["name"]).upper()))
        self.RepCount.setText(_translate("ExercisePrescribe", "Rep " + str(exercise_info["rep_count"])))
        self.StartExerciseBtn.clicked.connect(lambda: event_func(exercise_info))
