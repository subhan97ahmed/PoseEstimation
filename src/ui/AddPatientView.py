# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPatient(object):
    def setupUi(self, AddPatient):
        AddPatient.setObjectName("AddPatient")
        AddPatient.resize(1024, 680)
        AddPatient.setStyleSheet("*  {\n"
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
        self.centralwidget = QtWidgets.QWidget(AddPatient)
        self.centralwidget.setGeometry(QtCore.QRect(0, -20, 1081, 771))
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
        self.frame_3.setGeometry(QtCore.QRect(-30, 20, 161, 691))
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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(180, 180, 391, 161))
        self.groupBox.setObjectName("groupBox")
        self.mail_label_5 = QtWidgets.QLabel(self.groupBox)
        self.mail_label_5.setGeometry(QtCore.QRect(10, 40, 91, 31))
        self.mail_label_5.setObjectName("mail_label_5")
        self.patientEmail = QtWidgets.QLineEdit(self.groupBox)
        self.patientEmail.setGeometry(QtCore.QRect(100, 38, 281, 42))
        self.patientEmail.setStyleSheet("")
        self.patientEmail.setMaxLength(1000)
        self.patientEmail.setFrame(True)
        self.patientEmail.setCursorPosition(0)
        self.patientEmail.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.patientEmail.setClearButtonEnabled(True)
        self.patientEmail.setObjectName("patientEmail")
        self.searchPatientBtn = QtWidgets.QPushButton(self.groupBox)
        self.searchPatientBtn.setGeometry(QtCore.QRect(230, 100, 151, 41))
        self.searchPatientBtn.setObjectName("searchPatientBtn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 370, 391, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.mail_label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.mail_label_8.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.mail_label_8.setObjectName("mail_label_8")
        self.diagnose1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.diagnose1.setGeometry(QtCore.QRect(90, 38, 291, 42))
        self.diagnose1.setStyleSheet("")
        self.diagnose1.setText("")
        self.diagnose1.setMaxLength(1000)
        self.diagnose1.setFrame(True)
        self.diagnose1.setCursorPosition(0)
        self.diagnose1.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.diagnose1.setClearButtonEnabled(True)
        self.diagnose1.setObjectName("diagnose1")
        self.addPatientBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.addPatientBtn.setGeometry(QtCore.QRect(230, 210, 151, 41))
        self.addPatientBtn.setObjectName("addPatientBtn")
        self.mail_label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.mail_label_9.setGeometry(QtCore.QRect(10, 92, 81, 31))
        self.mail_label_9.setObjectName("mail_label_9")
        self.diagnose2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.diagnose2.setGeometry(QtCore.QRect(90, 90, 291, 42))
        self.diagnose2.setStyleSheet("")
        self.diagnose2.setText("")
        self.diagnose2.setMaxLength(1000)
        self.diagnose2.setFrame(True)
        self.diagnose2.setCursorPosition(0)
        self.diagnose2.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.diagnose2.setClearButtonEnabled(True)
        self.diagnose2.setObjectName("diagnose2")
        self.diagnose3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.diagnose3.setGeometry(QtCore.QRect(90, 148, 291, 42))
        self.diagnose3.setStyleSheet("")
        self.diagnose3.setText("")
        self.diagnose3.setMaxLength(1000)
        self.diagnose3.setFrame(True)
        self.diagnose3.setCursorPosition(0)
        self.diagnose3.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.diagnose3.setClearButtonEnabled(True)
        self.diagnose3.setObjectName("diagnose3")
        self.mail_label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.mail_label_10.setGeometry(QtCore.QRect(10, 150, 81, 31))
        self.mail_label_10.setObjectName("mail_label_10")
        self.patientCard = QtWidgets.QWidget(self.centralwidget)
        self.patientCard.setGeometry(QtCore.QRect(610, 190, 391, 291))
        self.patientCard.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: #f0f4c3;\n"
                                       "\n"
                                       "")
        self.patientCard.setObjectName("patientCard")
        self.label_5 = QtWidgets.QLabel(self.patientCard)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 61, 51))
        self.label_5.setStyleSheet("background-color: transparent;\n"
                                   "width: 20px;\n"
                                   "height: auto")
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setPixmap(QtGui.QPixmap(":/iconPrefix/treatment.png"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.patientName_2 = QtWidgets.QLabel(self.patientCard)
        self.patientName_2.setGeometry(QtCore.QRect(80, 20, 281, 21))
        self.patientName_2.setStyleSheet("background-color: transparent;\n"
                                         "font-size: 16px;")
        self.patientName_2.setObjectName("patientName_2")
        self.patientAge_2 = QtWidgets.QLabel(self.patientCard)
        self.patientAge_2.setGeometry(QtCore.QRect(80, 110, 281, 21))
        self.patientAge_2.setStyleSheet("background-color: transparent;\n"
                                        "font-size: 14px;")
        self.patientAge_2.setObjectName("patientAge_2")
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
        self.patientEmail_3 = QtWidgets.QLabel(self.patientCard)
        self.patientEmail_3.setGeometry(QtCore.QRect(80, 50, 281, 21))
        self.patientEmail_3.setStyleSheet("background-color: transparent;\n"
                                          "font-size: 14px;")
        self.patientEmail_3.setObjectName("patientEmail_3")
        self.PatientContactNo_3 = QtWidgets.QLabel(self.patientCard)
        self.PatientContactNo_3.setGeometry(QtCore.QRect(80, 80, 281, 21))
        self.PatientContactNo_3.setStyleSheet("background-color: transparent;\n"
                                              "font-size: 14px;")
        self.PatientContactNo_3.setObjectName("PatientContactNo_3")
        self.TreatmentLabel.raise_()
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.patientCard.raise_()

        self.retranslateUi(AddPatient)
        QtCore.QMetaObject.connectSlotsByName(AddPatient)

    def retranslateUi(self, AddPatient):
        _translate = QtCore.QCoreApplication.translate
        AddPatient.setWindowTitle(_translate("AddPatient", "Posefect - Physiotherapist Add Patient"))
        self.TreatmentLabel.setText(_translate("AddPatient", "Add Patient"))
        self.HomeButton.setText(_translate("AddPatient", "Home"))
        self.TreatmentButton.setText(_translate("AddPatient", "Treatments"))
        self.ReportButton.setText(_translate("AddPatient", "Reports"))
        self.UsernameLabel_2.setText(_translate("AddPatient", "USERNAME"))
        self.groupBox.setTitle(_translate("AddPatient", "Search Patient"))
        self.mail_label_5.setText(_translate("AddPatient", "Patient Email"))
        self.patientEmail.setPlaceholderText(_translate("AddPatient", "e.g. email@gmail.com"))
        self.searchPatientBtn.setText(_translate("AddPatient", "Search"))
        self.groupBox_2.setTitle(_translate("AddPatient", "Initial Diagnoses"))
        self.mail_label_8.setText(_translate("AddPatient", "Diagnose 1"))
        self.diagnose1.setPlaceholderText(_translate("AddPatient", "e.g. Rotatory cuff"))
        self.addPatientBtn.setText(_translate("AddPatient", "Add"))
        self.mail_label_9.setText(_translate("AddPatient", "Diagnose 2"))
        self.diagnose2.setPlaceholderText(_translate("AddPatient", "e.g. Rotatory cuff"))
        self.diagnose3.setPlaceholderText(_translate("AddPatient", "e.g. Rotatory cuff"))
        self.mail_label_10.setText(_translate("AddPatient", "Diagnose 3"))
        self.patientName_2.setText(_translate("AddPatient", "Patient Name"))
        self.patientAge_2.setText(_translate("AddPatient", "18"))
        self.disease_1.setText(_translate("AddPatient", "-"))
        self.disease_2.setText(_translate("AddPatient", "-"))
        self.disease_3.setText(_translate("AddPatient", "-"))
        self.patientEmail_3.setText(_translate("AddPatient", "email@gmail.com"))
        self.PatientContactNo_3.setText(_translate("AddPatient", "03451234XXX"))


import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddPatient = QtWidgets.QWidget()
    ui = Ui_AddPatient()
    ui.setupUi(AddPatient)
    AddPatient.show()
    sys.exit(app.exec_())
