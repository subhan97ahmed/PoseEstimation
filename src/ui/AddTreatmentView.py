# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTreatment(object):
    def setupUi(self, AddTreatment):
        AddTreatment.setObjectName("AddTreatment")
        AddTreatment.resize(1024, 680)
        AddTreatment.setStyleSheet("*  {\n"
                                   "    background-color: #e2f6ff;\n"
                                   "    font: 57 10pt \"Montserrat Medium\";\n"
                                   "}\n"
                                   "QGroupBox {\n"
                                   "    font-size: 16px;\n"
                                   "}\n"
                                   "QLineEdit, #mail_label, #pass_label {\n"
                                   "    padding: 10px 5px;\n"
                                   "}\n"
                                   "QLineEdit, QDateEdit, QComboBox, QSpinBox {\n"
                                   "    border-bottom: 2px solid #c17900;\n"
                                   "    border-radius: 0;\n"
                                   "    padding: 10px 5px;\n"
                                   "    cursor: pointer;\n"
                                   "}\n"
                                   "QPushButton {\n"
                                   "    background-color: rgb(249, 168, 37);\n"
                                   "    padding: 12px;\n"
                                   "    border-radius: 20px;\n"
                                   "}\n"
                                   "QCommandLinkButton {\n"
                                   "    background-color: transparent;\n"
                                   "    text-align: center;\n"
                                   "}")
        self.centralwidget = QtWidgets.QWidget(AddTreatment)
        self.centralwidget.setGeometry(QtCore.QRect(-10, -20, 1081, 771))
        self.centralwidget.setObjectName("centralwidget")
        self.TreatmentLabel = QtWidgets.QLabel(self.centralwidget)
        self.TreatmentLabel.setGeometry(QtCore.QRect(180, 110, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.TreatmentLabel.setFont(font)
        self.TreatmentLabel.setStyleSheet("font-size: 26px;")
        self.TreatmentLabel.setObjectName("TreatmentLabel")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(-20, 20, 161, 691))
        self.frame_3.setStyleSheet("background-color: #ffbd45;\n"
                                   "border-radius: 15px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Logolabel_2 = QtWidgets.QLabel(self.frame_3)
        self.Logolabel_2.setGeometry(QtCore.QRect(60, 40, 62, 48))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Logolabel_2.setFont(font)
        self.Logolabel_2.setAutoFillBackground(False)
        self.Logolabel_2.setStyleSheet("font-family: \"Montserrat ExtraBold\";\n"
                                       "font-size: 22px;")
        self.Logolabel_2.setText("PF")
        self.Logolabel_2.setTextFormat(QtCore.Qt.AutoText)
        self.Logolabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Logolabel_2.setWordWrap(True)
        self.Logolabel_2.setIndent(0)
        self.Logolabel_2.setObjectName("Logolabel_2")
        self.HomeButton = QtWidgets.QCommandLinkButton(self.frame_3)
        self.HomeButton.setGeometry(QtCore.QRect(40, 260, 121, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconPrefix/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeButton.setIcon(icon)
        self.HomeButton.setObjectName("HomeButton")
        self.TreatmentButton = QtWidgets.QCommandLinkButton(self.frame_3)
        self.TreatmentButton.setGeometry(QtCore.QRect(40, 310, 121, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconPrefix/therapist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TreatmentButton.setIcon(icon1)
        self.TreatmentButton.setObjectName("TreatmentButton")
        self.ReportButton = QtWidgets.QCommandLinkButton(self.frame_3)
        self.ReportButton.setGeometry(QtCore.QRect(40, 360, 121, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconPrefix/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ReportButton.setIcon(icon2)
        self.ReportButton.setObjectName("ReportButton")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(130, 10, 961, 101))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.ProfilepushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.ProfilepushButton_2.setGeometry(QtCore.QRect(840, 23, 51, 51))
        self.ProfilepushButton_2.setStyleSheet("background-color: transparent;\n"
                                               "margin: 0;")
        self.ProfilepushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconPrefix/user-profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ProfilepushButton_2.setIcon(icon3)
        self.ProfilepushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.ProfilepushButton_2.setObjectName("ProfilepushButton_2")
        self.UsernameLabel_2 = QtWidgets.QLabel(self.frame_4)
        self.UsernameLabel_2.setGeometry(QtCore.QRect(750, 40, 91, 21))
        self.UsernameLabel_2.setObjectName("UsernameLabel_2")
        self.AddExerciseCombo = QtWidgets.QGroupBox(self.centralwidget)
        self.AddExerciseCombo.setGeometry(QtCore.QRect(580, 230, 391, 301))
        self.AddExerciseCombo.setObjectName("AddExerciseCombo")
        self.addPatientBtn = QtWidgets.QPushButton(self.AddExerciseCombo)
        self.addPatientBtn.setGeometry(QtCore.QRect(230, 240, 151, 41))
        self.addPatientBtn.setObjectName("addPatientBtn")
        self.mail_label_8 = QtWidgets.QLabel(self.AddExerciseCombo)
        self.mail_label_8.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.mail_label_8.setObjectName("mail_label_8")
        self.exerciseName = QtWidgets.QComboBox(self.AddExerciseCombo)
        self.exerciseName.setGeometry(QtCore.QRect(120, 30, 251, 41))
        self.exerciseName.setObjectName("exerciseName")
        self.repCount = QtWidgets.QSpinBox(self.AddExerciseCombo)
        self.repCount.setGeometry(QtCore.QRect(120, 81, 251, 41))
        self.repCount.setObjectName("repCount")
        self.label = QtWidgets.QLabel(self.AddExerciseCombo)
        self.label.setGeometry(QtCore.QRect(10, 90, 101, 31))
        self.label.setObjectName("label")
        self.angleCount = QtWidgets.QSpinBox(self.AddExerciseCombo)
        self.angleCount.setGeometry(QtCore.QRect(120, 131, 251, 41))
        self.angleCount.setObjectName("angleCount")
        self.label_2 = QtWidgets.QLabel(self.AddExerciseCombo)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.AddExerciseCombo)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 101, 31))
        self.label_4.setObjectName("label_4")
        self.videoLink = QtWidgets.QLineEdit(self.AddExerciseCombo)
        self.videoLink.setGeometry(QtCore.QRect(120, 180, 251, 42))
        self.videoLink.setStyleSheet("")
        self.videoLink.setText("")
        self.videoLink.setMaxLength(1000)
        self.videoLink.setFrame(True)
        self.videoLink.setCursorPosition(0)
        self.videoLink.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.videoLink.setClearButtonEnabled(True)
        self.videoLink.setObjectName("videoLink")
        self.patientCard = QtWidgets.QWidget(self.centralwidget)
        self.patientCard.setGeometry(QtCore.QRect(170, 240, 391, 291))
        self.patientCard.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: #f0f4c3;\n"
                                       "\n"
                                       "")
        self.patientCard.setObjectName("patientCard")
        self.label_3 = QtWidgets.QLabel(self.patientCard)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 61, 51))
        self.label_3.setStyleSheet("background-color: transparent;\n"
                                   "width: 20px;\n"
                                   "height: auto")
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setPixmap(QtGui.QPixmap(":/iconPrefix/treatment.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.patientName = QtWidgets.QLabel(self.patientCard)
        self.patientName.setGeometry(QtCore.QRect(80, 20, 281, 21))
        self.patientName.setStyleSheet("background-color: transparent;\n"
                                       "font-size: 16px;")
        self.patientName.setObjectName("patientName")
        self.patientAge = QtWidgets.QLabel(self.patientCard)
        self.patientAge.setGeometry(QtCore.QRect(80, 110, 281, 21))
        self.patientAge.setStyleSheet("background-color: transparent;\n"
                                      "font-size: 14px;")
        self.patientAge.setObjectName("patientAge")
        self.disease_1 = QtWidgets.QLabel(self.patientCard)
        self.disease_1.setGeometry(QtCore.QRect(70, 140, 281, 31))
        self.disease_1.setStyleSheet("border-radius: 15px;\n"
                                     "background-color: #fb8c00;\n"
                                     "font-size: 12px;")
        self.disease_1.setAlignment(QtCore.Qt.AlignCenter)
        self.disease_1.setObjectName("disease_1")
        self.disease_2 = QtWidgets.QLabel(self.patientCard)
        self.disease_2.setGeometry(QtCore.QRect(70, 190, 281, 31))
        self.disease_2.setStyleSheet("border-radius: 15px;\n"
                                     "background-color: #fb8c00;\n"
                                     "font-size: 12px;")
        self.disease_2.setAlignment(QtCore.Qt.AlignCenter)
        self.disease_2.setObjectName("disease_2")
        self.disease_3 = QtWidgets.QLabel(self.patientCard)
        self.disease_3.setGeometry(QtCore.QRect(70, 240, 281, 31))
        self.disease_3.setStyleSheet("border-radius: 15px;\n"
                                     "background-color: #fb8c00;\n"
                                     "font-size: 12px;")
        self.disease_3.setAlignment(QtCore.Qt.AlignCenter)
        self.disease_3.setObjectName("disease_3")
        self.patientEmail = QtWidgets.QLabel(self.patientCard)
        self.patientEmail.setGeometry(QtCore.QRect(80, 50, 281, 21))
        self.patientEmail.setStyleSheet("background-color: transparent;\n"
                                        "font-size: 14px;")
        self.patientEmail.setObjectName("patientEmail")
        self.PatientContactNo = QtWidgets.QLabel(self.patientCard)
        self.PatientContactNo.setGeometry(QtCore.QRect(80, 80, 281, 21))
        self.PatientContactNo.setStyleSheet("background-color: transparent;\n"
                                            "font-size: 14px;")
        self.PatientContactNo.setObjectName("PatientContactNo")
        self.TreatmentLabel.raise_()
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.AddExerciseCombo.raise_()
        self.patientCard.raise_()

        self.retranslateUi(AddTreatment)
        QtCore.QMetaObject.connectSlotsByName(AddTreatment)

    def retranslateUi(self, AddTreatment):
        _translate = QtCore.QCoreApplication.translate
        AddTreatment.setWindowTitle(_translate("AddTreatment", "Posefect - Physiotherapist Add Treatment"))
        self.TreatmentLabel.setText(_translate("AddTreatment", "Add Treatment"))
        self.HomeButton.setText(_translate("AddTreatment", "Home"))
        self.TreatmentButton.setText(_translate("AddTreatment", "Treatments"))
        self.ReportButton.setText(_translate("AddTreatment", "Reports"))
        self.UsernameLabel_2.setText(_translate("AddTreatment", "USERNAME"))
        self.AddExerciseCombo.setTitle(_translate("AddTreatment", "Add Exercise"))
        self.addPatientBtn.setText(_translate("AddTreatment", "Add"))
        self.mail_label_8.setText(_translate("AddTreatment", "Exercise Name"))
        self.label.setText(_translate("AddTreatment", "Rep Count"))
        self.label_2.setText(_translate("AddTreatment", "Angle (Degree)"))
        self.label_4.setText(_translate("AddTreatment", "Video Link"))
        self.videoLink.setPlaceholderText(_translate("AddTreatment", "e.g. https://youtu.be/xxx"))
        self.patientName.setText(_translate("AddTreatment", "Patient Name"))
        self.patientAge.setText(_translate("AddTreatment", "18"))
        self.disease_1.setText(_translate("AddTreatment", "Rotatory cuff"))
        self.disease_2.setText(_translate("AddTreatment", "-"))
        self.disease_3.setText(_translate("AddTreatment", "-"))
        self.patientEmail.setText(_translate("AddTreatment", "email@gmail.com"))
        self.PatientContactNo.setText(_translate("AddTreatment", "03451234XXX"))


import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddTreatment = QtWidgets.QWidget()
    ui = Ui_AddTreatment()
    ui.setupUi(AddTreatment)
    AddTreatment.show()
    sys.exit(app.exec_())
