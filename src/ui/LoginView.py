# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setEnabled(True)
        Login.resize(800, 600)
        Login.setMinimumSize(QtCore.QSize(800, 600))
        Login.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        Login.setFont(font)
        Login.setStyleSheet("*  {\n"
                            "    background-color: #e2f6ff;\n"
                            "    font: 57 10pt \"Montserrat Medium\";\n"
                            "}\n"
                            "QGroupBox {\n"
                            "    font-size: 16px;\n"
                            "}\n"
                            "QLineEdit, #mail_label, #pass_label {\n"
                            "    padding: 10px 5px; \n"
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
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly | QtCore.Qt.ImhPreferUppercase)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 20, 771, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 81 28pt \"Montserrat ExtraBold\";")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 120, 771, 441))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.login_heading_3 = QtWidgets.QLabel(self.groupBox)
        self.login_heading_3.setGeometry(QtCore.QRect(10, 110, 351, 44))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.login_heading_3.setFont(font)
        self.login_heading_3.setStyleSheet("font: 81 24pt \"Montserrat ExtraBold\";")
        self.login_heading_3.setAlignment(QtCore.Qt.AlignCenter)
        self.login_heading_3.setObjectName("login_heading_3")
        self.passwordEdit = QtWidgets.QLineEdit(self.groupBox)
        self.passwordEdit.setGeometry(QtCore.QRect(90, 216, 261, 42))
        self.passwordEdit.setMaxLength(1000)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setCursorPosition(0)
        self.passwordEdit.setClearButtonEnabled(True)
        self.passwordEdit.setObjectName("passwordEdit")
        self.CreateAnAcc = QtWidgets.QCommandLinkButton(self.groupBox)
        self.CreateAnAcc.setGeometry(QtCore.QRect(177, 370, 161, 40))
        self.CreateAnAcc.setBaseSize(QtCore.QSize(0, 0))
        self.CreateAnAcc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CreateAnAcc.setAcceptDrops(True)
        self.CreateAnAcc.setToolTipDuration(300)
        self.CreateAnAcc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CreateAnAcc.setInputMethodHints(QtCore.Qt.ImhTime)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconPrefix/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CreateAnAcc.setIcon(icon)
        self.CreateAnAcc.setIconSize(QtCore.QSize(20, 20))
        self.CreateAnAcc.setObjectName("CreateAnAcc")
        self.mail_label_3 = QtWidgets.QLabel(self.groupBox)
        self.mail_label_3.setGeometry(QtCore.QRect(10, 170, 71, 42))
        self.mail_label_3.setObjectName("mail_label_3")
        self.loginBtn = QtWidgets.QPushButton(self.groupBox)
        self.loginBtn.setGeometry(QtCore.QRect(180, 316, 161, 41))
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.loginBtn.setAcceptDrops(True)
        self.loginBtn.setToolTipDuration(300)
        self.loginBtn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconPrefix/move-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginBtn.setIcon(icon1)
        self.loginBtn.setCheckable(False)
        self.loginBtn.setAutoRepeat(False)
        self.loginBtn.setObjectName("loginBtn")
        self.emailEdit = QtWidgets.QLineEdit(self.groupBox)
        self.emailEdit.setGeometry(QtCore.QRect(90, 174, 261, 42))
        self.emailEdit.setStyleSheet("")
        self.emailEdit.setMaxLength(1000)
        self.emailEdit.setFrame(True)
        self.emailEdit.setCursorPosition(0)
        self.emailEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.emailEdit.setClearButtonEnabled(True)
        self.emailEdit.setObjectName("emailEdit")
        self.pass_label_3 = QtWidgets.QLabel(self.groupBox)
        self.pass_label_3.setGeometry(QtCore.QRect(10, 210, 71, 42))
        self.pass_label_3.setObjectName("pass_label_3")
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Posefect - login"))
        self.label.setText(_translate("Login", "POSEFECT"))
        self.label_2.setText(
            _translate("Login", "<html><head/><body><p><img src=\":/imagePath/splash-poses.png\"/></p></body></html>"))
        self.groupBox.setTitle(_translate("Login", "Login"))
        self.login_heading_3.setText(_translate("Login", "Welcome Back!"))
        self.passwordEdit.setPlaceholderText(_translate("Login", "Enter your password"))
        self.CreateAnAcc.setText(_translate("Login", "Create an Account"))
        self.mail_label_3.setText(_translate("Login", "Email"))
        self.loginBtn.setText(_translate("Login", "Login"))
        self.emailEdit.setPlaceholderText(_translate("Login", "e.g. somemail@example.com"))
        self.pass_label_3.setText(_translate("Login", "Password"))


import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
