# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TherapistReports(object):
    def setupUi(self, TherapistReports):
        TherapistReports.setObjectName("TherapistReports")
        TherapistReports.resize(1024, 680)
        TherapistReports.setStyleSheet("*  {\n"
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
        self.centralwidget = QtWidgets.QWidget(TherapistReports)
        self.centralwidget.setGeometry(QtCore.QRect(0, -10, 1081, 771))
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
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.frame_3)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(40, 260, 121, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconPrefix/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_4.setIcon(icon)
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.frame_3)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(40, 310, 121, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconPrefix/therapist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_5.setIcon(icon1)
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.frame_3)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(40, 360, 121, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconPrefix/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
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
        self.patientCard_2 = QtWidgets.QWidget(self.centralwidget)
        self.patientCard_2.setGeometry(QtCore.QRect(180, 180, 301, 191))
        self.patientCard_2.setStyleSheet("border-radius: 10px;\n"
                                         "background-color: #f0f4c3;\n"
                                         "\n"
                                         "")
        self.patientCard_2.setObjectName("patientCard_2")
        self.label_3 = QtWidgets.QLabel(self.patientCard_2)
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
        self.patient_name_3 = QtWidgets.QLabel(self.patientCard_2)
        self.patient_name_3.setGeometry(QtCore.QRect(80, 20, 211, 21))
        self.patient_name_3.setStyleSheet("background-color: transparent;\n"
                                          "font-size: 16px;")
        self.patient_name_3.setObjectName("patient_name_3")
        self.patient_age_6 = QtWidgets.QLabel(self.patientCard_2)
        self.patient_age_6.setGeometry(QtCore.QRect(80, 110, 211, 21))
        self.patient_age_6.setStyleSheet("background-color: transparent;\n"
                                         "font-size: 14px;")
        self.patient_age_6.setObjectName("patient_age_6")
        self.patient_age_7 = QtWidgets.QLabel(self.patientCard_2)
        self.patient_age_7.setGeometry(QtCore.QRect(80, 50, 211, 21))
        self.patient_age_7.setStyleSheet("background-color: transparent;\n"
                                         "font-size: 14px;")
        self.patient_age_7.setObjectName("patient_age_7")
        self.patient_age_8 = QtWidgets.QLabel(self.patientCard_2)
        self.patient_age_8.setGeometry(QtCore.QRect(80, 80, 211, 21))
        self.patient_age_8.setStyleSheet("background-color: transparent;\n"
                                         "font-size: 14px;")
        self.patient_age_8.setObjectName("patient_age_8")
        self.AddPatientBtn = QtWidgets.QPushButton(self.patientCard_2)
        self.AddPatientBtn.setGeometry(QtCore.QRect(140, 140, 151, 41))
        self.AddPatientBtn.setStyleSheet("background-color: rgb(249, 168, 37);\n"
                                         "border-radius: 20px;")
        self.AddPatientBtn.setObjectName("AddPatientBtn")
        self.TreatmentLabel.raise_()
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.patientCard_2.raise_()

        self.retranslateUi(TherapistReports)
        QtCore.QMetaObject.connectSlotsByName(TherapistReports)

    def retranslateUi(self, TherapistReports):
        _translate = QtCore.QCoreApplication.translate
        TherapistReports.setWindowTitle(_translate("TherapistReports", "Posefect - Physiotherapist Reports"))
        self.TreatmentLabel.setText(_translate("TherapistReports", "Patients Report"))
        self.commandLinkButton_4.setText(_translate("TherapistReports", "Home"))
        self.commandLinkButton_5.setText(_translate("TherapistReports", "Treatments"))
        self.commandLinkButton_6.setText(_translate("TherapistReports", "Reports"))
        self.UsernameLabel_2.setText(_translate("TherapistReports", "USERNAME"))
        self.patient_name_3.setText(_translate("TherapistReports", "Patient Name"))
        self.patient_age_6.setText(_translate("TherapistReports", "18"))
        self.patient_age_7.setText(_translate("TherapistReports", "email@gmail.com"))
        self.patient_age_8.setText(_translate("TherapistReports", "03451234XXX"))
        self.AddPatientBtn.setText(_translate("TherapistReports", "Add"))


import src.resource.icons_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TherapistReports = QtWidgets.QWidget()
    ui = Ui_TherapistReports()
    ui.setupUi(TherapistReports)
    TherapistReports.show()
    sys.exit(app.exec_())
