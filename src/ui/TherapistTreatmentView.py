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
        self.AddPatientBtn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.AddPatientBtn.setGeometry(QtCore.QRect(894, 110, 121, 41))
        self.AddPatientBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconPrefix/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddPatientBtn.setIcon(icon4)
        self.AddPatientBtn.setObjectName("AddPatientBtn")
        self.scrollHolder = QtWidgets.QWidget(self.centralwidget)
        self.scrollHolder.setGeometry(QtCore.QRect(160, 160, 871, 521))
        self.scrollHolder.setObjectName("scrollHolder")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollHolder)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.scrollHolder)
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 846, 1018))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 1000))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.TreatmentLabel.raise_()
        self.frame_4.raise_()
        self.AddPatientBtn.raise_()
        self.frame_3.raise_()
        self.scrollHolder.raise_()

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
