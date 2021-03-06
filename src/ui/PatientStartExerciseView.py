# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartExercise_Patient(object):
    def setupUi(self, StartExercise_Patient):
        StartExercise_Patient.setObjectName("StartExercise_Patient")
        StartExercise_Patient.resize(1024, 680)
        StartExercise_Patient.setStyleSheet("*  {\n"
                                            "    background-color: #EAF7FF;\n"
                                            "    font: 57 10pt \"Montserrat Medium\";\n"
                                            "}\n"
                                            "QGroupBox {\n"
                                            "    font-size: 16px;\n"
                                            "}\n"
                                            "QLineEdit, #mail_label, #pass_label {\n"
                                            "    padding: 10px 5px;\n"
                                            "}\n"
                                            "QLineEdit {\n"
                                            "    border-bottom: 2px solid #3E84DC;\n"
                                            "    border-radius: 0;\n"
                                            "}\n"
                                            "QPushButton {\n"
                                            "    background-color: #04D486;\n"
                                            "    padding: 12px;\n"
                                            "    border-radius: 20px;\n"
                                            "}\n"
                                            "QCommandLinkButton {\n"
"    color: #FFFFFF;\n"
                                            "    background-color: transparent;\n"
                                            "    text-align: center;\n"
                                            "}\n"
                                            "\n"
                                            "#card_1, #card_2, #card_3 {\n"
                                            "    border-radius: 10px;\n"
                                            "    border: 2px solid #04D486;\n"
                                            "}\n"
                                            "#ct_1, #ct_2, #ct_3 {\n"
                                            "    font-size: 16px;\n"
                                            "    background-color: transparent;\n"
                                            "}\n"
                                            "#cd_1, #cd_2, #cd_3 {\n"
                                            "    font-size: 18px;\n"
                                            "    background-color: transparent;\n"
                                            "}\n"
                                            "#card_1 {\n"
                                            "    background-color: #FFFFFF;\n"
                                            "}\n"
                                            "#card_2 {\n"
                                            "    background-color: #d1c4e9;\n"
                                            "}\n"
                                            "#card_3 {\n"
                                            "    background-color: #ffcdd2;\n"
                                            "}")
        self.centralwidget = QtWidgets.QWidget(StartExercise_Patient)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 1024, 680))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-30, 0, 161, 711))
        self.frame.setStyleSheet("background-color: #3E84DC;\n"
                                 "border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Logolabel = QtWidgets.QLabel(self.frame)
        self.Logolabel.setGeometry(QtCore.QRect(60, 40, 62, 48))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Logolabel.setFont(font)
        self.Logolabel.setAutoFillBackground(False)
        self.Logolabel.setStyleSheet("font-family: \"Montserrat ExtraBold\";\n"
                                     "font-size: 22px;")
        self.Logolabel.setText("P F")
        self.Logolabel.setTextFormat(QtCore.Qt.AutoText)
        self.Logolabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Logolabel.setWordWrap(True)
        self.Logolabel.setIndent(0)
        self.Logolabel.setObjectName("Logolabel")
        self.HomeButton = QtWidgets.QCommandLinkButton(self.frame)
        self.HomeButton.setGeometry(QtCore.QRect(40, 260, 121, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconPrefix/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeButton.setIcon(icon)
        self.HomeButton.setObjectName("HomeButton")
        self.ReportButton = QtWidgets.QCommandLinkButton(self.frame)
        self.ReportButton.setGeometry(QtCore.QRect(40, 360, 121, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconPrefix/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ReportButton.setIcon(icon1)
        self.ReportButton.setObjectName("ReportButton")
        self.TreatmentButton = QtWidgets.QCommandLinkButton(self.frame)
        self.TreatmentButton.setGeometry(QtCore.QRect(40, 310, 121, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconPrefix/therapist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TreatmentButton.setIcon(icon2)
        self.TreatmentButton.setObjectName("TreatmentButton")
        self.ExerciseFeedGrBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ExerciseFeedGrBox.setGeometry(QtCore.QRect(170, 220, 801, 391))
        self.ExerciseFeedGrBox.setTitle("")
        self.ExerciseFeedGrBox.setObjectName("ExerciseFeedGrBox")
        self.StartExerciseCard = QtWidgets.QWidget(self.centralwidget)
        self.StartExerciseCard.setGeometry(QtCore.QRect(170, 10, 381, 191))
        self.StartExerciseCard.setStyleSheet("background-color: #FFFFFF;\n"
                                             "border-radius: 10px;")
        self.StartExerciseCard.setObjectName("StartExerciseCard")
        self.exerciseName = QtWidgets.QLabel(self.StartExerciseCard)
        self.exerciseName.setGeometry(QtCore.QRect(90, 20, 221, 31))
        self.exerciseName.setObjectName("exerciseName")
        self.StartExerciseBtn = QtWidgets.QPushButton(self.StartExerciseCard)
        self.StartExerciseBtn.setGeometry(QtCore.QRect(230, 140, 131, 41))
        self.StartExerciseBtn.setStyleSheet("border-radius: 20px;\n"
                                            "background-color: #04D486;\n"
                                            "")
        self.StartExerciseBtn.setObjectName("StartExerciseBtn")
        self.runningman = QtWidgets.QLabel(self.StartExerciseCard)
        self.runningman.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.runningman.setStyleSheet("background-color: transparent;")
        self.runningman.setObjectName("runningman")
        self.RepCount = QtWidgets.QLabel(self.StartExerciseCard)
        self.RepCount.setGeometry(QtCore.QRect(90, 50, 221, 21))
        self.RepCount.setObjectName("RepCount")
        self.ExampleVidBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ExampleVidBox.setGeometry(QtCore.QRect(590, 10, 371, 191))
        self.ExampleVidBox.setTitle("")
        self.ExampleVidBox.setObjectName("ExampleVidBox")

        self.retranslateUi(StartExercise_Patient)
        QtCore.QMetaObject.connectSlotsByName(StartExercise_Patient)

    def retranslateUi(self, StartExercise_Patient):
        _translate = QtCore.QCoreApplication.translate
        StartExercise_Patient.setWindowTitle(_translate("StartExercise_Patient", "Form"))
        self.HomeButton.setText(_translate("StartExercise_Patient", "Home"))
        self.ReportButton.setText(_translate("StartExercise_Patient", "Reports"))
        self.TreatmentButton.setText(_translate("StartExercise_Patient", "Exercises"))
        self.exerciseName.setText(_translate("StartExercise_Patient", "Exercise Name"))
        self.StartExerciseBtn.setText(_translate("StartExercise_Patient", "Start Exercise"))
        self.runningman.setText(_translate("StartExercise_Patient",
                                           "<html><head/><body><p><img src=\":/iconPrefix/exercise.png\"/></p></body"
                                           "></html>"))
        self.RepCount.setText(_translate("StartExercise_Patient", "Rep x"))


import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    StartExercise_Patient = QtWidgets.QWidget()
    ui = Ui_StartExercise_Patient()
    ui.setupUi(StartExercise_Patient)
    StartExercise_Patient.show()
    sys.exit(app.exec_())