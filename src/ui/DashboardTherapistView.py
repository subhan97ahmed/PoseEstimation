# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc


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
                                "    background-color: #e2f6ff;\n"
                                "    font: 57 10pt \"Montserrat Medium\";\n"
                                "}\n"
                                "QGroupBox {\n"
                                "    font-size: 16px;\n"
                                "}\n"
                                "QLineEdit, #mail_label, #pass_label {\n"
                                "    padding: 10px 5px;\n"
                                "}\n"
                                "QLineEdit, QDateEdit, QComboBox {\n"
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
                                "}\n"
                                "\n"
                                "#card_1, #card_2, #card_3 {\n"
                                "    border-radius: 10px;\n"
                                "    border: 2px solid #fb8c00;\n"
                                "}\n"
                                "#ct_1, #ct_2, #ct_3 {\n"
                                "    font-size: 16px;\n"
                                "    background-color: transparent;\n"
                                "}\n"
                                "#cd_1, #cd_2, #cd_3 {\n"
                                "    font-size: 18px;\n"
                                "    background-color: transparent;\n"
                                "}\n"
                                "#card_1 {\n"
                                "    background-color: #f0f4c3;\n"
                                "}\n"
                                "#card_2 {\n"
                                "    background-color: #d1c4e9;\n"
                                "}\n"
                                "#card_3 {\n"
                                "    background-color: #ffcdd2;\n"
                                "}")
        self.centralwidget = QtWidgets.QWidget(Dashboard)
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
        self.frame.setGeometry(QtCore.QRect(-30, 10, 161, 691))
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
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton.setGeometry(QtCore.QRect(40, 260, 121, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconPrefix/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(40, 310, 121, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconPrefix/therapist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon1)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(40, 360, 121, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconPrefix/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon2)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
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
        self.card_1 = QtWidgets.QWidget(self.centralwidget)
        self.card_1.setGeometry(QtCore.QRect(180, 270, 231, 151))
        self.card_1.setObjectName("card_1")
        self.ct_1 = QtWidgets.QLabel(self.card_1)
        self.ct_1.setGeometry(QtCore.QRect(20, 20, 151, 41))
        self.ct_1.setObjectName("ct_1")
        self.cd_1 = QtWidgets.QLabel(self.card_1)
        self.cd_1.setGeometry(QtCore.QRect(20, 110, 191, 21))
        self.cd_1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cd_1.setObjectName("cd_1")
        self.card_2 = QtWidgets.QWidget(self.centralwidget)
        self.card_2.setGeometry(QtCore.QRect(430, 270, 221, 151))
        self.card_2.setObjectName("card_2")
        self.ct_2 = QtWidgets.QLabel(self.card_2)
        self.ct_2.setGeometry(QtCore.QRect(21, 20, 181, 41))
        self.ct_2.setObjectName("ct_2")
        self.cd_2 = QtWidgets.QLabel(self.card_2)
        self.cd_2.setGeometry(QtCore.QRect(30, 110, 171, 21))
        self.cd_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cd_2.setObjectName("cd_2")
        self.card_3 = QtWidgets.QWidget(self.centralwidget)
        self.card_3.setGeometry(QtCore.QRect(680, 270, 231, 151))
        self.card_3.setObjectName("card_3")
        self.ct_3 = QtWidgets.QLabel(self.card_3)
        self.ct_3.setGeometry(QtCore.QRect(10, 20, 201, 41))
        self.ct_3.setObjectName("ct_3")
        self.cd_3 = QtWidgets.QLabel(self.card_3)
        self.cd_3.setGeometry(QtCore.QRect(30, 110, 181, 21))
        self.cd_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.cd_3.setObjectName("cd_3")
        self.DashboarLabel.raise_()
        self.frame_2.raise_()
        self.card_2.raise_()
        self.card_1.raise_()
        self.card_3.raise_()
        self.frame.raise_()

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Posefect - Physiotherapist Dashboard"))
        self.DashboarLabel.setText(_translate("Dashboard", "HOME"))
        self.commandLinkButton.setText(_translate("Dashboard", "Home"))
        self.commandLinkButton_2.setText(_translate("Dashboard", "Treatments"))
        self.commandLinkButton_3.setText(_translate("Dashboard", "Reports"))
        self.UsernameLabel.setText(_translate("Dashboard", "USERNAME"))
        self.ct_1.setText(_translate("Dashboard", "No. Of Patients"))
        self.cd_1.setText(_translate("Dashboard", "0"))
        self.ct_2.setText(_translate("Dashboard", "Active Patients"))
        self.cd_2.setText(_translate("Dashboard", "0"))
        self.ct_3.setText(_translate("Dashboard", "Therapies Completed"))
        self.cd_3.setText(_translate("Dashboard", "0"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QWidget()
    ui = Ui_Dashboard()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec_())
