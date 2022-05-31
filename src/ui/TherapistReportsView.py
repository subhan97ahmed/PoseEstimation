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
        self.PatientsReportLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientsReportLabel.setGeometry(QtCore.QRect(180, 110, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.PatientsReportLabel.setFont(font)
        self.PatientsReportLabel.setStyleSheet("font-size: 26px;")
        self.PatientsReportLabel.setObjectName("PatientsReportLabel")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(-20, 10, 161, 691))
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
        self.PatientNameCard = QtWidgets.QWidget(self.centralwidget)
        self.PatientNameCard.setGeometry(QtCore.QRect(180, 180, 301, 191))
        self.PatientNameCard.setStyleSheet("border-radius: 10px;\n"
                                           "background-color: #f0f4c3;\n"
                                           "\n"
                                           "")
        self.PatientNameCard.setObjectName("PatientNameCard")
        self.label_3 = QtWidgets.QLabel(self.PatientNameCard)
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
        self.PatientNameLabel = QtWidgets.QLabel(self.PatientNameCard)
        self.PatientNameLabel.setGeometry(QtCore.QRect(80, 20, 211, 21))
        self.PatientNameLabel.setStyleSheet("background-color: transparent;\n"
                                            "font-size: 16px;")
        self.PatientNameLabel.setObjectName("PatientNameLabel")
        self.PatientAge = QtWidgets.QLabel(self.PatientNameCard)
        self.PatientAge.setGeometry(QtCore.QRect(80, 110, 211, 21))
        self.PatientAge.setStyleSheet("background-color: transparent;\n"
                                      "font-size: 14px;")
        self.PatientAge.setObjectName("PatientAge")
        self.PatientEmail = QtWidgets.QLabel(self.PatientNameCard)
        self.PatientEmail.setGeometry(QtCore.QRect(80, 50, 211, 21))
        self.PatientEmail.setStyleSheet("background-color: transparent;\n"
                                        "font-size: 14px;")
        self.PatientEmail.setObjectName("PatientEmail")
        self.PatientContactNo = QtWidgets.QLabel(self.PatientNameCard)
        self.PatientContactNo.setGeometry(QtCore.QRect(80, 80, 211, 21))
        self.PatientContactNo.setStyleSheet("background-color: transparent;\n"
                                            "font-size: 14px;")
        self.PatientContactNo.setObjectName("PatientContactNo")
        self.AddPatientBtn = QtWidgets.QPushButton(self.PatientNameCard)
        self.AddPatientBtn.setGeometry(QtCore.QRect(140, 140, 151, 41))
        self.AddPatientBtn.setStyleSheet("background-color: rgb(249, 168, 37);\n"
                                         "border-radius: 20px;")
        self.AddPatientBtn.setObjectName("AddPatientBtn")
        self.PatientsReportLabel.raise_()
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.PatientNameCard.raise_()

        self.retranslateUi(TherapistReports)
        QtCore.QMetaObject.connectSlotsByName(TherapistReports)

    def retranslateUi(self, TherapistReports):
        _translate = QtCore.QCoreApplication.translate
        TherapistReports.setWindowTitle(_translate("TherapistReports", "Posefect - Physiotherapist Reports"))
        self.PatientsReportLabel.setText(_translate("TherapistReports", "Patients Report"))
        self.HomeButton.setText(_translate("TherapistReports", "Home"))
        self.TreatmentButton.setText(_translate("TherapistReports", "Treatments"))
        self.ReportButton.setText(_translate("TherapistReports", "Reports"))
        self.UsernameLabel_2.setText(_translate("TherapistReports", "USERNAME"))
        self.PatientNameLabel.setText(_translate("TherapistReports", "Patient Name"))
        self.PatientAge.setText(_translate("TherapistReports", "18"))
        self.PatientEmail.setText(_translate("TherapistReports", "email@gmail.com"))
        self.PatientContactNo.setText(_translate("TherapistReports", "03451234XXX"))
        self.AddPatientBtn.setText(_translate("TherapistReports", "Add"))


import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TherapistReports = QtWidgets.QWidget()
    ui = Ui_TherapistReports()
    ui.setupUi(TherapistReports)
    TherapistReports.show()
    sys.exit(app.exec_())