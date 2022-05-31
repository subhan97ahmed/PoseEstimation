# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Treatment(object):
    def setupUi(self, Treatment):
        Treatment.setObjectName("Treatment")
        Treatment.resize(1024, 680)
        Treatment.setStyleSheet("*  {\n"
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
                                "}")
        self.centralwidget = QtWidgets.QWidget(Treatment)
        self.centralwidget.setGeometry(QtCore.QRect(-10, 0, 1081, 771))
        self.centralwidget.setObjectName("centralwidget")
        self.TreatmentLabel = QtWidgets.QLabel(self.centralwidget)
        self.TreatmentLabel.setGeometry(QtCore.QRect(180, 100, 411, 61))
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
        self.frame_3.setGeometry(QtCore.QRect(-30, 0, 161, 691))
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
        self.frame_4.setGeometry(QtCore.QRect(130, -1, 961, 101))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.ProfilepushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.ProfilepushButton_2.setGeometry(QtCore.QRect(850, 23, 51, 51))
        self.ProfilepushButton_2.setStyleSheet("background-color: transparent;\n"
                                               "margin: 0;")
        self.ProfilepushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconPrefix/user-profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ProfilepushButton_2.setIcon(icon3)
        self.ProfilepushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.ProfilepushButton_2.setObjectName("ProfilepushButton_2")
        self.UsernameLabel_2 = QtWidgets.QLabel(self.frame_4)
        self.UsernameLabel_2.setGeometry(QtCore.QRect(760, 40, 91, 21))
        self.UsernameLabel_2.setObjectName("UsernameLabel_2")
        self.PatientCard = QtWidgets.QWidget(self.centralwidget)
        self.PatientCard.setGeometry(QtCore.QRect(180, 170, 311, 201))
        self.PatientCard.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: #f0f4c3;\n"
                                       "")
        self.PatientCard.setObjectName("PatientCard")
        self.label = QtWidgets.QLabel(self.PatientCard)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 51))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap(":/iconPrefix/user.png"))
        self.label.setObjectName("label")
        self.Patient_name = QtWidgets.QLabel(self.PatientCard)
        self.Patient_name.setGeometry(QtCore.QRect(80, 40, 211, 21))
        self.Patient_name.setStyleSheet("background-color: transparent;\n"
                                        "font-size: 16px;")
        self.Patient_name.setObjectName("Patient_name")
        self.Patient_age = QtWidgets.QLabel(self.PatientCard)
        self.Patient_age.setGeometry(QtCore.QRect(80, 70, 211, 21))
        self.Patient_age.setStyleSheet("background-color: transparent;\n"
                                       "font-size: 14px;")
        self.Patient_age.setObjectName("Patient_age")
        self.disease = QtWidgets.QLabel(self.PatientCard)
        self.disease.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.disease.setStyleSheet("border-radius: 15px;\n"
                                   "background-color: #fb8c00;\n"
                                   "font-size: 12px;")
        self.disease.setAlignment(QtCore.Qt.AlignCenter)
        self.disease.setObjectName("disease")
        self.TreatmentBtn = QtWidgets.QPushButton(self.PatientCard)
        self.TreatmentBtn.setGeometry(QtCore.QRect(172, 150, 131, 41))
        self.TreatmentBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TreatmentBtn.setStyleSheet("margin: 0;\n"
                                        "background-color: #fb8c00;\n"
                                        "border-radius: 20px;")
        self.TreatmentBtn.setObjectName("TreatmentBtn")
        self.notificationBtn = QtWidgets.QCommandLinkButton(self.PatientCard)
        self.notificationBtn.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.notificationBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.notificationBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconPrefix/notification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notificationBtn.setIcon(icon4)
        self.notificationBtn.setObjectName("notificationBtn")
        self.AddPatientBtn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.AddPatientBtn.setGeometry(QtCore.QRect(894, 110, 121, 41))
        self.AddPatientBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/iconPrefix/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddPatientBtn.setIcon(icon5)
        self.AddPatientBtn.setObjectName("AddPatientBtn")
        self.TreatmentLabel.raise_()
        self.frame_4.raise_()
        self.PatientCard.raise_()
        self.AddPatientBtn.raise_()
        self.frame_3.raise_()

        self.retranslateUi(Treatment)
        QtCore.QMetaObject.connectSlotsByName(Treatment)

    def retranslateUi(self, Treatment):
        _translate = QtCore.QCoreApplication.translate
        Treatment.setWindowTitle(_translate("Treatment", "Posefect - Physiotherapist Treatment"))
        self.TreatmentLabel.setText(_translate("Treatment", "PATIENT TREATMENTS"))
        self.HomeButton.setText(_translate("Treatment", "Home"))
        self.TreatmentButton.setText(_translate("Treatment", "Treatments"))
        self.ReportButton.setText(_translate("Treatment", "Reports"))
        self.UsernameLabel_2.setText(_translate("Treatment", "USERNAME"))
        self.Patient_name.setText(_translate("Treatment", "Patient Name"))
        self.Patient_age.setText(_translate("Treatment", "18"))
        self.disease.setText(_translate("Treatment", "Rotatory cuff"))
        self.TreatmentBtn.setText(_translate("Treatment", "Treatment"))
        self.AddPatientBtn.setText(_translate("Treatment", "Add Patient"))


import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Treatment = QtWidgets.QWidget()
    ui = Ui_Treatment()
    ui.setupUi(Treatment)
    Treatment.show()
    sys.exit(app.exec_())