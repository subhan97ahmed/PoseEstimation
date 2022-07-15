from PyQt5 import QtCore, QtGui, QtWidgets
import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc
from src.utils.util import get_age


class ExerciseCard:
    def __init__(self, frame,exercise_info, event_func=any):
        _translate = QtCore.QCoreApplication.translate
        self.ExerciseCard = QtWidgets.QWidget(frame)
        self.ExerciseCard.setGeometry(QtCore.QRect(0, -10, 331, 151))
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
        self.RepCount.setText(_translate("ExercisePrescribe", "Rep "+str(exercise_info["rep_count"])))
        self.StartExerciseBtn.clicked.connect(lambda: event_func(exercise_info))

        #
        # self.ExerciseCard = QtWidgets.QWidget(frame)
        # self.ExerciseCard.setGeometry(QtCore.QRect(0, 0, 311, 311))
        # self.ExerciseCard.setStyleSheet("border-radius: 10px;\n"
        #                                "background-color: #f0f4c3;\n"
        #                                "")
        # self.ExerciseCard.setObjectName("ExerciseCard")
        # self.label = QtWidgets.QLabel(self.ExerciseCard)
        # self.label.setGeometry(QtCore.QRect(10, 20, 61, 51))
        # self.label.setStyleSheet("background-color: transparent;")
        # self.label.setText("")
        # self.label.setTextFormat(QtCore.Qt.RichText)
        # self.label.setPixmap(QtGui.QPixmap(":/iconPrefix/user.png"))
        # self.label.setObjectName("label")
        # self.Patient_name = QtWidgets.QLabel(self.ExerciseCard)
        # self.Patient_name.setGeometry(QtCore.QRect(80, 40, 211, 21))
        # self.Patient_name.setStyleSheet("background-color: transparent;\n"
        #                                 "font-size: 16px;")
        # self.Patient_name.setObjectName("Patient_name")
        # self.Patient_age = QtWidgets.QLabel(self.ExerciseCard)
        # self.Patient_age.setGeometry(QtCore.QRect(80, 70, 211, 21))
        # self.Patient_age.setStyleSheet("background-color: transparent;\n"
        #                                "font-size: 14px;")
        # self.Patient_age.setObjectName("Patient_age")
        # self.disease_1 = QtWidgets.QLabel(self.ExerciseCard)
        # self.disease_1.setGeometry(QtCore.QRect(10, 100, 291, 31))
        # self.disease_1.setStyleSheet("border-radius: 15px;\n"
        #                              "background-color: #fb8c00;\n"
        #                              "font-size: 12px;")
        # self.disease_1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        # self.disease_1.setObjectName("disease_1")
        # self.TreatmentBtn = QtWidgets.QPushButton(self.ExerciseCard)
        # self.TreatmentBtn.setGeometry(QtCore.QRect(90, 260, 131, 41))
        # self.TreatmentBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.TreatmentBtn.setStyleSheet("margin: 0;\n"
        #                                 "background-color: #fb8c00;\n"
        #                                 "border-radius: 20px;")
        # self.TreatmentBtn.setObjectName("TreatmentBtn")
        # self.notificationBtn = QtWidgets.QCommandLinkButton(self.ExerciseCard)
        # self.notificationBtn.setGeometry(QtCore.QRect(270, 0, 31, 31))
        # self.notificationBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.notificationBtn.setText("")
        # icon5 = QtGui.QIcon()
        # icon5.addPixmap(QtGui.QPixmap(":/iconPrefix/notification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.notificationBtn.setIcon(icon5)
        # self.notificationBtn.setObjectName("notificationBtn")
        # self.disease_2 = QtWidgets.QLabel(self.ExerciseCard)
        # self.disease_2.setGeometry(QtCore.QRect(10, 150, 291, 31))
        # self.disease_2.setStyleSheet("border-radius: 15px;\n"
        #                              "background-color: #fb8c00;\n"
        #                              "font-size: 12px;")
        # self.disease_2.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        # self.disease_2.setObjectName("disease_2")
        # self.disease_3 = QtWidgets.QLabel(self.ExerciseCard)
        # self.disease_3.setGeometry(QtCore.QRect(10, 200, 291, 31))
        # self.disease_3.setStyleSheet("border-radius: 15px;\n"
        #                              "background-color: #fb8c00;\n"
        #                              "font-size: 12px;")
        # self.disease_3.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        # self.disease_3.setObjectName("disease_3")
        #
        # # Set values
        # self.Patient_name.setText(_translate("Treatment", exercise_info["f_name"]))
        # self.Patient_age.setText(_translate("Treatment", get_age(exercise_info["dob"])))
        # self.disease_1.setText(_translate("Treatment", patient_info["diagnosis_1"]))
        # self.disease_2.setText(_translate("Treatment", patient_info["diagnosis_2"]))
        # self.disease_3.setText(_translate("Treatment", patient_info["diagnosis_3"]))
        # self.TreatmentBtn.setText(_translate("Treatment", "Add Treatment"))
        # self.TreatmentBtn.clicked.connect(lambda: event_func(patient_info))


