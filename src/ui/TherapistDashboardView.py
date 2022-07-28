# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(1024, 680)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        Dashboard.setFont(font)
        Dashboard.setStyleSheet("*  {\n"
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
                                "#NumpatientCard, #PatientCard, #TherapyCard{\n"
                                "    border-radius: 10px;\n"
                                "    border: 2px solid #04D486;\n"
                                "}\n"
                                "#ct_1, #ct_2, #ct_3 {\n"
                                "    font-size: 16px;\n"
                                "    background-color: transparent;\n"
                                "}\n"
                                "#NoOfPatientsLabel, #NoofActivePatientsLabel, #TherapiesCompletedLabel{\n"
                                "    font-size: 18px;\n"
                                "    background-color: transparent;\n"
                                "}\n"
                                "#NumpatientCard{\n"
                                "    background-color: #FFFFFF;\n"
                                "}\n"
                                "#PatientCard {\n"
                                "    background-color: #d1c4e9;\n"
                                "}\n"
                                "#TherapyCard {\n"
                                "    background-color: #ffcdd2;\n"
                                "}")
        self.centralwidget = QtWidgets.QWidget(Dashboard)
        self.centralwidget.setGeometry(QtCore.QRect(0, -10, 1081, 771))
        self.centralwidget.setObjectName("centralwidget")
        self.HomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.HomeLabel.setGeometry(QtCore.QRect(180, 100, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.HomeLabel.setFont(font)
        self.HomeLabel.setStyleSheet("font-size: 26px;")
        self.HomeLabel.setObjectName("HomeLabel")
        self.sideFrame = QtWidgets.QFrame(self.centralwidget)
        self.sideFrame.setGeometry(QtCore.QRect(-30, 10, 161, 691))
        self.sideFrame.setStyleSheet("background-color: #3E84DC;\n"
                                     "border-radius: 15px;")
        self.sideFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideFrame.setObjectName("sideFrame")
        self.Logolabel = QtWidgets.QLabel(self.sideFrame)
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
        self.HomeButton = QtWidgets.QCommandLinkButton(self.sideFrame)
        self.HomeButton.setGeometry(QtCore.QRect(40, 260, 121, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconPrefix/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeButton.setIcon(icon)
        self.HomeButton.setObjectName("HomeButton")
        self.TreatmentButton = QtWidgets.QCommandLinkButton(self.sideFrame)
        self.TreatmentButton.setGeometry(QtCore.QRect(40, 310, 121, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconPrefix/therapist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TreatmentButton.setIcon(icon1)
        self.TreatmentButton.setObjectName("TreatmentButton")
        self.ReportButton = QtWidgets.QCommandLinkButton(self.sideFrame)
        self.ReportButton.setGeometry(QtCore.QRect(40, 360, 121, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconPrefix/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ReportButton.setIcon(icon2)
        self.ReportButton.setObjectName("ReportButton")
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
        self.NumpatientCard = QtWidgets.QWidget(self.centralwidget)
        self.NumpatientCard.setGeometry(QtCore.QRect(180, 270, 231, 151))
        self.NumpatientCard.setObjectName("NumpatientCard")
        self.ct_1 = QtWidgets.QLabel(self.NumpatientCard)
        self.ct_1.setGeometry(QtCore.QRect(20, 20, 191, 41))
        self.ct_1.setObjectName("ct_1")
        self.NoOfPatientsLabel = QtWidgets.QLabel(self.NumpatientCard)
        self.NoOfPatientsLabel.setGeometry(QtCore.QRect(20, 110, 191, 21))
        self.NoOfPatientsLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.NoOfPatientsLabel.setObjectName("NoOfPatientsLabel")
        self.PatientCard = QtWidgets.QWidget(self.centralwidget)
        self.PatientCard.setGeometry(QtCore.QRect(430, 270, 221, 151))
        self.PatientCard.setObjectName("PatientCard")
        self.ct_2 = QtWidgets.QLabel(self.PatientCard)
        self.ct_2.setGeometry(QtCore.QRect(21, 20, 181, 41))
        self.ct_2.setObjectName("ct_2")
        self.NoofActivePatientsLabel = QtWidgets.QLabel(self.PatientCard)
        self.NoofActivePatientsLabel.setGeometry(QtCore.QRect(30, 110, 171, 21))
        self.NoofActivePatientsLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.NoofActivePatientsLabel.setObjectName("NoofActivePatientsLabel")
        self.HomeLabel.raise_()
        self.frame_2.raise_()
        self.PatientCard.raise_()
        self.NumpatientCard.raise_()
        self.sideFrame.raise_()

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Posefect - Physiotherapist Dashboard"))
        self.HomeLabel.setText(_translate("Dashboard", "HOME"))
        self.HomeButton.setText(_translate("Dashboard", "Home"))
        self.TreatmentButton.setText(_translate("Dashboard", "Treatments"))
        self.ReportButton.setText(_translate("Dashboard", "Reports"))
        self.UsernameLabel.setText(_translate("Dashboard", "USERNAME"))
        self.ct_1.setText(_translate("Dashboard", "Assigned Exercises"))
        self.NoOfPatientsLabel.setText(_translate("Dashboard", "0"))
        self.ct_2.setText(_translate("Dashboard", "Active Patients"))
        self.NoofActivePatientsLabel.setText(_translate("Dashboard", "0"))


import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QWidget()
    ui = Ui_Dashboard()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec_())