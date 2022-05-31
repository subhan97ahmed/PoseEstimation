# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExercisePrescribe(object):
    def setupUi(self, ExercisePrescribe):
        ExercisePrescribe.setObjectName("ExercisePrescribe")
        ExercisePrescribe.resize(1025, 667)
        ExercisePrescribe.setStyleSheet("*  {\n"
                                        "    background-color: #e2f6ff;\n"
                                        "    font: 57 10pt \"Montserrat Medium\";\n"
                                        "}\n"
                                        "QGroupBox {\n"
                                        "    font-size: 16px;\n"
                                        "}\n"
                                        "QLineEdit, #mail_label, #pass_label {\n"
                                        "    padding: 10px 5px;\n"
                                        "}\n"
                                        "QLineEdit {\n"
                                        "    border-bottom: 2px solid #c17900;\n"
                                        "    border-radius: 0;\n"
                                        "}\n"
                                        "QPushButton {\n"
                                        "    background-color: rgb(249, 168, 37);\n"
                                        "    padding: 12px;\n"
                                        "    border-radius: 20px;\n"
                                        "}\n"
                                        "QCommandLinkButton {\n"
                                        "    background-color: transparent;\n"
                                        "    text-align: center;\n"
                                        "}\n"
                                        "")
        self.centralwidget = QtWidgets.QWidget(ExercisePrescribe)
        self.centralwidget.setGeometry(QtCore.QRect(0, -10, 1024, 680))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-30, 10, 161, 711))
        self.frame.setStyleSheet("background-color: #ffbd45;\n"
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(130, -1, 961, 101))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.ProfilepushButton = QtWidgets.QPushButton(self.frame_2)
        self.ProfilepushButton.setGeometry(QtCore.QRect(840, 30, 51, 51))
        self.ProfilepushButton.setStyleSheet("background-color: transparent;\n"
                                             "margin: 0;")
        self.ProfilepushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconPrefix/user-profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ProfilepushButton.setIcon(icon3)
        self.ProfilepushButton.setIconSize(QtCore.QSize(32, 32))
        self.ProfilepushButton.setObjectName("ProfilepushButton")
        self.UsernameLabel = QtWidgets.QLabel(self.frame_2)
        self.UsernameLabel.setGeometry(QtCore.QRect(750, 40, 91, 21))
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.exerciseCard = QtWidgets.QWidget(self.centralwidget)
        self.exerciseCard.setGeometry(QtCore.QRect(160, 190, 331, 151))
        self.exerciseCard.setStyleSheet("background-color: #f0f4c3;\n"
                                        "border-radius: 10px;")
        self.exerciseCard.setObjectName("exerciseCard")
        self.ExerciseName = QtWidgets.QLabel(self.exerciseCard)
        self.ExerciseName.setGeometry(QtCore.QRect(90, 20, 221, 31))
        self.ExerciseName.setObjectName("ExerciseName")
        self.StartExerciseBtn = QtWidgets.QPushButton(self.exerciseCard)
        self.StartExerciseBtn.setGeometry(QtCore.QRect(190, 100, 131, 41))
        self.StartExerciseBtn.setStyleSheet("border-radius: 20px;\n"
                                            "background-color: rgb(249, 168, 37);\n"
                                            "")
        self.StartExerciseBtn.setObjectName("StartExerciseBtn")
        self.label = QtWidgets.QLabel(self.exerciseCard)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setObjectName("label")
        self.RepCount = QtWidgets.QLabel(self.exerciseCard)
        self.RepCount.setGeometry(QtCore.QRect(90, 50, 221, 21))
        self.RepCount.setObjectName("RepCount")
        self.DashboarLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.DashboarLabel_2.setGeometry(QtCore.QRect(160, 120, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.DashboarLabel_2.setFont(font)
        self.DashboarLabel_2.setStyleSheet("font-size: 26px;")
        self.DashboarLabel_2.setObjectName("DashboarLabel_2")
        self.frame_2.raise_()
        self.exerciseCard.raise_()
        self.frame.raise_()
        self.DashboarLabel_2.raise_()

        self.retranslateUi(ExercisePrescribe)
        QtCore.QMetaObject.connectSlotsByName(ExercisePrescribe)

    def retranslateUi(self, ExercisePrescribe):
        _translate = QtCore.QCoreApplication.translate
        ExercisePrescribe.setWindowTitle(_translate("ExercisePrescribe", "Form"))
        self.HomeButton.setText(_translate("ExercisePrescribe", "Home"))
        self.ReportButton.setText(_translate("ExercisePrescribe", "Reports"))
        self.TreatmentButton.setText(_translate("ExercisePrescribe", "Exercises"))
        self.UsernameLabel.setText(_translate("ExercisePrescribe", "USERNAME"))
        self.ExerciseName.setText(_translate("ExercisePrescribe", "Exercise Name"))
        self.StartExerciseBtn.setText(_translate("ExercisePrescribe", "Start Exercise"))
        self.label.setText(_translate("ExercisePrescribe",
                                      "<html><head/><body><p><img src=\":/iconPrefix/exercise.png\"/></p></body></html>"))
        self.RepCount.setText(_translate("ExercisePrescribe", "Rep x"))
        self.DashboarLabel_2.setText(_translate("ExercisePrescribe", "Prescribed Exercises"))


import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ExercisePrescribe = QtWidgets.QWidget()
    ui = Ui_ExercisePrescribe()
    ui.setupUi(ExercisePrescribe)
    ExercisePrescribe.show()
    sys.exit(app.exec_())
