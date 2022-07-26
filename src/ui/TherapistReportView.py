# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/design/therapist-report.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TherapistReport(object):
    def setupUi(self, TherapistReport):
        TherapistReport.setObjectName("TherapistReport")
        TherapistReport.resize(1024, 680)
        TherapistReport.setStyleSheet("*  {\n"
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
        self.centralwidget = QtWidgets.QWidget(TherapistReport)
        self.centralwidget.setGeometry(QtCore.QRect(-10, -20, 1081, 761))
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
        self.Logolabel_2.setText("P F")
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
        self.groupBox.setGeometry(QtCore.QRect(740, 130, 271, 251))
        self.groupBox.setObjectName("groupBox")
        self.mail_label_5 = QtWidgets.QLabel(self.groupBox)
        self.mail_label_5.setGeometry(QtCore.QRect(10, 100, 71, 41))
        self.mail_label_5.setObjectName("mail_label_5")
        self.search_patient_btn = QtWidgets.QPushButton(self.groupBox)
        self.search_patient_btn.setGeometry(QtCore.QRect(110, 200, 151, 41))
        self.search_patient_btn.setObjectName("search_patient_btn")
        self.start_date = QtWidgets.QDateEdit(self.groupBox)
        self.start_date.setGeometry(QtCore.QRect(100, 100, 161, 41))
        self.start_date.setObjectName("start_date")
        self.end_date = QtWidgets.QDateEdit(self.groupBox)
        self.end_date.setGeometry(QtCore.QRect(100, 150, 161, 41))
        self.end_date.setObjectName("end_date")
        self.mail_label_6 = QtWidgets.QLabel(self.groupBox)
        self.mail_label_6.setGeometry(QtCore.QRect(10, 150, 71, 41))
        self.mail_label_6.setObjectName("mail_label_6")
        self.mail_label_7 = QtWidgets.QLabel(self.groupBox)
        self.mail_label_7.setGeometry(QtCore.QRect(10, 50, 71, 41))
        self.mail_label_7.setObjectName("mail_label_7")
        self.exerciseName = QtWidgets.QComboBox(self.groupBox)
        self.exerciseName.setGeometry(QtCore.QRect(100, 40, 161, 41))
        self.exerciseName.setObjectName("exerciseName")
        self.ReportBoxCombo = QtWidgets.QGroupBox(self.centralwidget)
        self.ReportBoxCombo.setGeometry(QtCore.QRect(170, 390, 841, 301))
        self.ReportBoxCombo.setObjectName("ReportBoxCombo")
        self.scrollArea = QtWidgets.QScrollArea(self.ReportBoxCombo)
        self.scrollArea.setGeometry(QtCore.QRect(9, 29, 821, 261))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 819, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 821, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.widget)
        self.scrollArea_3.setStyleSheet("border: none;")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 786, 1018))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 1000))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6.addWidget(self.frame_5)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.addWidget(self.scrollArea_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.patientCard = QtWidgets.QWidget(self.centralwidget)
        self.patientCard.setGeometry(QtCore.QRect(170, 170, 541, 211))
        self.patientCard.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: #f0f4c3;\n"
                                       "\n"
                                       "")
        self.patientCard.setObjectName("patientCard")
        self.label_6 = QtWidgets.QLabel(self.patientCard)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 61, 51))
        self.label_6.setStyleSheet("background-color: transparent;\n"
                                   "width: 20px;\n"
                                   "height: auto")
        self.label_6.setText("")
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setPixmap(QtGui.QPixmap(":/iconPrefix/treatment.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.patientName_3 = QtWidgets.QLabel(self.patientCard)
        self.patientName_3.setGeometry(QtCore.QRect(70, 50, 191, 21))
        self.patientName_3.setStyleSheet("background-color: transparent;\n"
                                         "font-size: 16px;")
        self.patientName_3.setObjectName("patientName_3")
        self.patientAge_3 = QtWidgets.QLabel(self.patientCard)
        self.patientAge_3.setGeometry(QtCore.QRect(20, 170, 181, 21))
        self.patientAge_3.setStyleSheet("background-color: transparent;\n"
                                        "font-size: 14px;")
        self.patientAge_3.setObjectName("patientAge_3")
        self.disease_4 = QtWidgets.QLabel(self.patientCard)
        self.disease_4.setGeometry(QtCore.QRect(270, 40, 261, 31))
        self.disease_4.setStyleSheet("border-radius: 15px;\n"
                                     "background-color: #fb8c00;\n"
                                     "font-size: 12px;")
        self.disease_4.setAlignment(QtCore.Qt.AlignCenter)
        self.disease_4.setObjectName("disease_4")
        self.disease_5 = QtWidgets.QLabel(self.patientCard)
        self.disease_5.setGeometry(QtCore.QRect(270, 100, 261, 31))
        self.disease_5.setStyleSheet("border-radius: 15px;\n"
                                     "background-color: #fb8c00;\n"
                                     "font-size: 12px;")
        self.disease_5.setAlignment(QtCore.Qt.AlignCenter)
        self.disease_5.setObjectName("disease_5")
        self.disease_6 = QtWidgets.QLabel(self.patientCard)
        self.disease_6.setGeometry(QtCore.QRect(270, 160, 261, 31))
        self.disease_6.setStyleSheet("border-radius: 15px;\n"
                                     "background-color: #fb8c00;\n"
                                     "font-size: 12px;")
        self.disease_6.setAlignment(QtCore.Qt.AlignCenter)
        self.disease_6.setObjectName("disease_6")
        self.patientEmail_4 = QtWidgets.QLabel(self.patientCard)
        self.patientEmail_4.setGeometry(QtCore.QRect(20, 110, 181, 21))
        self.patientEmail_4.setStyleSheet("background-color: transparent;\n"
                                          "font-size: 14px;")
        self.patientEmail_4.setObjectName("patientEmail_4")
        self.PatientContactNo_4 = QtWidgets.QLabel(self.patientCard)
        self.PatientContactNo_4.setGeometry(QtCore.QRect(20, 140, 181, 21))
        self.PatientContactNo_4.setStyleSheet("background-color: transparent;\n"
                                              "font-size: 14px;")
        self.PatientContactNo_4.setObjectName("PatientContactNo_4")
        self.TreatmentLabel.raise_()
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.groupBox.raise_()
        self.ReportBoxCombo.raise_()
        self.patientCard.raise_()

        self.retranslateUi(TherapistReport)
        QtCore.QMetaObject.connectSlotsByName(TherapistReport)

    def retranslateUi(self, TherapistReport):
        _translate = QtCore.QCoreApplication.translate
        TherapistReport.setWindowTitle(_translate("TherapistReport", "Form"))
        self.TreatmentLabel.setText(_translate("TherapistReport", "Patient Report"))
        self.HomeButton.setText(_translate("TherapistReport", "Home"))
        self.TreatmentButton.setText(_translate("TherapistReport", "Treatments"))
        self.ReportButton.setText(_translate("TherapistReport", "Reports"))
        self.UsernameLabel_2.setText(_translate("TherapistReport", "USERNAME"))
        self.groupBox.setTitle(_translate("TherapistReport", "Filter Report"))
        self.mail_label_5.setText(_translate("TherapistReport", "Start Date"))
        self.search_patient_btn.setText(_translate("TherapistReport", "Search"))
        self.mail_label_6.setText(_translate("TherapistReport", "End Date"))
        self.mail_label_7.setText(_translate("TherapistReport", "Exercise\n"
                                                                "Name"))
        self.ReportBoxCombo.setTitle(_translate("TherapistReport", "Report"))
        self.patientName_3.setText(_translate("TherapistReport", "Patient Name"))
        self.patientAge_3.setText(_translate("TherapistReport", "18"))
        self.disease_4.setText(_translate("TherapistReport", "Rotatory cuff"))
        self.disease_5.setText(_translate("TherapistReport", "-"))
        self.disease_6.setText(_translate("TherapistReport", "-"))
        self.patientEmail_4.setText(_translate("TherapistReport", "email@gmail.com"))
        self.PatientContactNo_4.setText(_translate("TherapistReport", "03451234XXX"))


import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TherapistReport = QtWidgets.QWidget()
    ui = Ui_TherapistReport()
    ui.setupUi(TherapistReport)
    TherapistReport.show()
    sys.exit(app.exec_())
