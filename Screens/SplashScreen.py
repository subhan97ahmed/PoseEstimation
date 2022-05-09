from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1194, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -3, 1261, 791))
        self.label.setPixmap(QPixmap("../src/Images/splash screen.png"))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LoginBtn.setGeometry(QtCore.QRect(860, 590, 251, 51))
        self.LoginBtn.setStyleSheet("#LoginBtn{\n"
                                    "border-radius: 5px;\n"
                                    "box-shadow: 0px 3px 6px #000000;\n"
                                    "border: 2px solid #000000;\n"
                                    "opacity: 1;\n"
                                    "font-family: Montserrat;\n"
                                    "font-size: 21px;\n"
                                    "font-weight: 800;\n"
                                    "color: #000000;\n"
                                    "background-color: #1EA3DC;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#LoginBtn:hover{\n"
                                    "color: #000000 ;\n"
                                    "background-color: #13E1DE;\n"
                                    "}")
        self.LoginBtn.setObjectName("LoginBtn")
        self.CreateAnAccount = QtWidgets.QPushButton(self.centralwidget)
        self.CreateAnAccount.setGeometry(QtCore.QRect(920, 650, 134, 18))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.CreateAnAccount.setFont(font)
        self.CreateAnAccount.setStyleSheet("#CreateAnAccount{\n"
                                           "color: var(--unnamed-color-3cb44a);\n"
                                           "font: normal normal bold 14px Montserrat;\n"
                                           "color: #000000;\n"
                                           "opacity: 1;\n"
                                           "background-color: Transparent;\n"
                                           " background-repeat: no-repeat;\n"
                                           " border: none;\n"
                                           " cursor: pointer;\n"
                                           " overflow: hidden;\n"
                                           " outline: none;\n"
                                           "\n"
                                           "}")
        self.CreateAnAccount.setObjectName("CreateAnAccount")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1060, 650, 18, 18))
        self.label_2.setStyleSheet("filter: opacity(0.4) drop-shadow(0 0 0 red); ")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 350, 541, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1194, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoginBtn.setText(_translate("MainWindow", "Login"))
        self.CreateAnAccount.setText(_translate("MainWindow", "Create an account"))
        self.label_3.setText(_translate("MainWindow",
                                        "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
