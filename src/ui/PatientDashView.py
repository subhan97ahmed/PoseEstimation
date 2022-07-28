# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PatientDash(object):
    def setupUi(self, PatientDash):
        PatientDash.setObjectName("PatientDash")
        PatientDash.resize(1024, 680)
        PatientDash.setStyleSheet("*  {\n"
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
                                  "#NextAppointmentCard, #NoOfExCompletedCard, #PrescribedExCard {\n"
                                  "    border-radius: 10px;\n"
                                  "    border: 2px solid #04D486;\n"
                                  "}\n"
                                  "#ct_1, #ct_2, #ct_3 {\n"
                                  "    font-size: 16px;\n"
                                  "    background-color: transparent;\n"
                                  "}\n"
                                  "#NextAppointmentCard, #NoOfExCompletedCard, #PrescribedExCard {\n"
                                  "    font-size: 18px;\n"
                                  "    background-color: transparent;\n"
                                  "}\n"
                                  "#NextAppointmentCard {\n"
                                  "    background-color: #FFFFFF;\n"
                                  "}\n"
                                  "#NoOfExCompletedCard {\n"
                                  "    background-color: #d1c4e9;\n"
                                  "}\n"
                                  "#prescribedExCard {\n"
                                  "    background-color: #ffcdd2;\n"
                                  "}*  {\n"
                                  "    background-color: #EAF7FF;\n"
                                  "    font: 57 10pt \"Montserrat Medium\";\n"
                                  "}\n"
                                  "QGroupBox {\n"
                                  "    font-size: 16px;\n"
                                  "}\n"
                                  "QLineEdit, #mail_label, #pass_label {\n"
                                  "    padding: 10px 5px;\n"
                                  "}\n"
                                  "QLineEdit, QDateEdit, QComboBox {\n"
                                  "    border-bottom: 2px solid #3E84DC;\n"
                                  "    border-radius: 0;\n"
                                  "    padding: 10px 5px;\n"
                                  "    cursor: pointer;\n"
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
                                  "#numpatientCard, #patientCard, #therapyCard{\n"
                                  "    border-radius: 10px;\n"
                                  "    border: 2px solid #04D486;\n"
                                  "}\n"
                                  "#ct_1, #ct_2, #ct_3 {\n"
                                  "    font-size: 16px;\n"
                                  "    background-color: transparent;\n"
                                  "}\n"
                                  "#NextAppointmentCard, #NoOfExCompletedCard, #PrescribedExCard {\n"
                                  "    font-size: 18px;\n"
                                  "    background-color: transparent;\n"
                                  "}")
        self.centralwidget = QtWidgets.QWidget(PatientDash)
        self.centralwidget.setGeometry(QtCore.QRect(0, -10, 1081, 771))
        self.centralwidget.setObjectName("centralwidget")
        self.DashboarLabel = QtWidgets.QLabel(self.centralwidget)
        self.DashboarLabel.setGeometry(QtCore.QRect(180, 100, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.DashboarLabel.setFont(font)
        self.DashboarLabel.setStyleSheet("font-size: 26px;")
        self.DashboarLabel.setObjectName("DashboarLabel")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-30, 10, 161, 711))
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(130, -1, 961, 101))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.ProfilepushButton = QtWidgets.QPushButton(self.frame_2)
        self.ProfilepushButton.setGeometry(QtCore.QRect(840, 23, 51, 51))
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
        self.PrescribedExCard = QtWidgets.QWidget(self.centralwidget)
        self.PrescribedExCard.setGeometry(QtCore.QRect(180, 270, 231, 151))
        self.PrescribedExCard.setStyleSheet("background-color: #ffcdd2;")
        self.PrescribedExCard.setObjectName("PrescribedExCard")
        self.ct_1 = QtWidgets.QLabel(self.PrescribedExCard)
        self.ct_1.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.ct_1.setObjectName("ct_1")
        self.NoOfExPrescribedLabel = QtWidgets.QLabel(self.PrescribedExCard)
        self.NoOfExPrescribedLabel.setGeometry(QtCore.QRect(20, 110, 191, 21))
        self.NoOfExPrescribedLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.NoOfExPrescribedLabel.setObjectName("NoOfExPrescribedLabel")
        self.NoOfExCompletedCard = QtWidgets.QWidget(self.centralwidget)
        self.NoOfExCompletedCard.setGeometry(QtCore.QRect(440, 270, 271, 151))
        self.NoOfExCompletedCard.setStyleSheet("background-color: #d1c4e9;")
        self.NoOfExCompletedCard.setObjectName("NoOfExCompletedCard")
        self.ct_2 = QtWidgets.QLabel(self.NoOfExCompletedCard)
        self.ct_2.setGeometry(QtCore.QRect(21, 20, 221, 41))
        self.ct_2.setObjectName("ct_2")
        self.NoOfExLabel = QtWidgets.QLabel(self.NoOfExCompletedCard)
        self.NoOfExLabel.setGeometry(QtCore.QRect(80, 110, 171, 21))
        self.NoOfExLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.NoOfExLabel.setObjectName("NoOfExLabel")
        self.DashboarLabel.raise_()
        self.frame_2.raise_()
        self.NoOfExCompletedCard.raise_()
        self.PrescribedExCard.raise_()
        self.frame.raise_()

        self.retranslateUi(PatientDash)
        QtCore.QMetaObject.connectSlotsByName(PatientDash)

    def retranslateUi(self, PatientDash):
        _translate = QtCore.QCoreApplication.translate
        PatientDash.setWindowTitle(_translate("PatientDash", "Form"))
        self.DashboarLabel.setText(_translate("PatientDash", "HOME"))
        self.HomeButton.setText(_translate("PatientDash", "Home"))
        self.ReportButton.setText(_translate("PatientDash", "Reports"))
        self.TreatmentButton.setText(_translate("PatientDash", "Exercises"))
        self.UsernameLabel.setText(_translate("PatientDash", "USERNAME"))
        self.ct_1.setText(_translate("PatientDash", "Exercises Prescribed"))
        self.NoOfExPrescribedLabel.setText(_translate("PatientDash", "0"))
        self.ct_2.setText(_translate("PatientDash", "No of Exercises Completed"))
        self.NoOfExLabel.setText(_translate("PatientDash", "0"))


import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PatientDash = QtWidgets.QWidget()
    ui = Ui_PatientDash()
    ui.setupUi(PatientDash)
    PatientDash.show()
    sys.exit(app.exec_())