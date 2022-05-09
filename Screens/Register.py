from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        # set icons folder path here
        QtCore.QDir.addSearchPath('icons', '../src/icons/')
        # set images folder path here
        QtCore.QDir.addSearchPath('images', '../src/Images/')
        Register.resize(800, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Register.sizePolicy().hasHeightForWidth())
        Register.setSizePolicy(sizePolicy)
        Register.setMinimumSize(QtCore.QSize(800, 700))
        Register.setMaximumSize(QtCore.QSize(800, 700))
        Register.setStyleSheet("*  {\n"
                               "    background-color: rgb(255, 243, 224);\n"
                               "    font: 57 10pt \"Montserrat Medium\";\n"
                               "}\n"
                               "QGroupBox {\n"
                               "    font-size: 16px;\n"
                               "}\n"
                               "#mail_label, #pass_label {\n"
                               "    padding: 10px 5px;\n"
                               "}\n"
                               "QLineEdit, QDateEdit, QComboBox {\n"
                               "    border-bottom: 2px solid #c17900;\n"
                               "    border-radius: 0;\n"
                               "    padding: 10px 5px;\n"
                               "    cursor: pointer;\n"
                               "}\n"
                               "QPushButton {\n"
                               "    margin-top: 15px;\n"
                               "    background-color: rgb(249, 168, 37);\n"
                               "    padding: 12px;\n"
                               "    border-radius: 20px;\n"
                               "}\n"
                               "QCommandLinkButton {\n"
                               "    background-color: transparent;\n"
                               "    text-align: center;\n"
                               "}")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Register)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 120, 751, 551))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.login_heading_3 = QtWidgets.QLabel(self.groupBox)
        self.login_heading_3.setGeometry(QtCore.QRect(10, 30, 351, 44))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.login_heading_3.setFont(font)
        self.login_heading_3.setStyleSheet("font: 81 14pt \"Montserrat ExtraBold\";")
        self.login_heading_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.login_heading_3.setObjectName("login_heading_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 175, 261, 42))
        self.lineEdit_5.setMaxLength(1000)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_5.setCursorPosition(0)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.CreateAnAcc_3 = QtWidgets.QCommandLinkButton(self.groupBox)
        self.CreateAnAcc_3.setGeometry(QtCore.QRect(230, 470, 111, 40))
        self.CreateAnAcc_3.setBaseSize(QtCore.QSize(0, 0))
        self.CreateAnAcc_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CreateAnAcc_3.setAcceptDrops(True)
        self.CreateAnAcc_3.setToolTipDuration(300)
        self.CreateAnAcc_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.CreateAnAcc_3.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhTime)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:move-right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.CreateAnAcc_3.setIcon(icon)
        self.CreateAnAcc_3.setIconSize(QtCore.QSize(20, 20))
        self.CreateAnAcc_3.setObjectName("CreateAnAcc_3")
        self.mail_label_3 = QtWidgets.QLabel(self.groupBox)
        self.mail_label_3.setGeometry(QtCore.QRect(10, 80, 71, 31))
        self.mail_label_3.setObjectName("mail_label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(203, 396, 161, 61))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.pushButton_3.setAcceptDrops(True)
        self.pushButton_3.setToolTipDuration(300)
        self.pushButton_3.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons:add-user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 78, 261, 42))
        self.lineEdit_6.setStyleSheet("")
        self.lineEdit_6.setMaxLength(1000)
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setCursorPosition(0)
        self.lineEdit_6.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pass_label_3 = QtWidgets.QLabel(self.groupBox)
        self.pass_label_3.setGeometry(QtCore.QRect(10, 180, 71, 31))
        self.pass_label_3.setObjectName("pass_label_3")
        self.mail_label_4 = QtWidgets.QLabel(self.groupBox)
        self.mail_label_4.setGeometry(QtCore.QRect(10, 130, 61, 31))
        self.mail_label_4.setObjectName("mail_label_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 128, 261, 42))
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setMaxLength(1000)
        self.lineEdit_7.setFrame(True)
        self.lineEdit_7.setCursorPosition(0)
        self.lineEdit_7.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.lineEdit_7.setClearButtonEnabled(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(99, 271, 261, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.pass_label_4 = QtWidgets.QLabel(self.groupBox)
        self.pass_label_4.setGeometry(QtCore.QRect(10, 280, 71, 31))
        self.pass_label_4.setObjectName("pass_label_4")
        self.pass_label_5 = QtWidgets.QLabel(self.groupBox)
        self.pass_label_5.setGeometry(QtCore.QRect(10, 320, 71, 31))
        self.pass_label_5.setObjectName("pass_label_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(100, 320, 261, 31))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setMaxVisibleItems(3)
        self.comboBox.setMinimumContentsLength(2)
        self.comboBox.setIconSize(QtCore.QSize(5, 5))
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.pass_label_6 = QtWidgets.QLabel(self.groupBox)
        self.pass_label_6.setGeometry(QtCore.QRect(10, 230, 91, 31))
        self.pass_label_6.setObjectName("pass_label_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 225, 261, 42))
        self.lineEdit_8.setMaxLength(1000)
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_8.setCursorPosition(0)
        self.lineEdit_8.setClearButtonEnabled(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pass_label_3.raise_()
        self.login_heading_3.raise_()
        self.lineEdit_5.raise_()
        self.CreateAnAcc_3.raise_()
        self.mail_label_3.raise_()
        self.pushButton_3.raise_()
        self.lineEdit_6.raise_()
        self.mail_label_4.raise_()
        self.lineEdit_7.raise_()
        self.pass_label_4.raise_()
        self.dateEdit.raise_()
        self.pass_label_5.raise_()
        self.comboBox.raise_()
        self.pass_label_6.raise_()
        self.lineEdit_8.raise_()
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayoutWidget = QtWidgets.QWidget(Register)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 751, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Register)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Posefect - Register"))
        self.label_2.setText(
            _translate("Register", "<html><head/><body><p><img src=\"images:register.png\"/></p></body></html>"))
        self.groupBox.setTitle(_translate("Register", "Signup"))
        self.login_heading_3.setText(_translate("Register", "Get Started to Become Perfect!"))
        self.lineEdit_5.setPlaceholderText(_translate("Register", "Enter your password"))
        self.CreateAnAcc_3.setText(_translate("Register", "Login Now"))
        self.mail_label_3.setText(_translate("Register", "Full Name"))
        self.pushButton_3.setText(_translate("Register", "Register"))
        self.lineEdit_6.setPlaceholderText(_translate("Register", "e.g. John Doe"))
        self.pass_label_3.setText(_translate("Register", "Password"))
        self.mail_label_4.setText(_translate("Register", "Email"))
        self.lineEdit_7.setPlaceholderText(_translate("Register", "e.g. somemail@example.com"))
        self.pass_label_4.setText(_translate("Register", "D.O.B"))
        self.pass_label_5.setText(_translate("Register", "Role"))
        self.pass_label_6.setText(_translate("Register", "Confirm Pass"))
        self.lineEdit_8.setPlaceholderText(_translate("Register", "Enter your password"))
        self.label.setText(_translate("Register", "POSEFECT"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QWidget()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec())
