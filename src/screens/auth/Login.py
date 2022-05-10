from PyQt6 import QtCore, QtGui, QtWidgets
from src.utils.util import some_func

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        some_func()
        MainWindow.setObjectName("MainWindow")
        # set icons folder path here
        QtCore.QDir.addSearchPath('icons', '../../icons/')
        # set images folder path here
        QtCore.QDir.addSearchPath('images', '../../Images/')
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("*  {\n"
                                 "    background-color: rgb(255, 243, 224);\n"
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
                                 "    margin-top: 15px;\n"
                                 "    background-color: rgb(249, 168, 37);\n"
                                 "    padding: 12px;\n"
                                 "    border-radius: 20px;\n"
                                 "}\n"
                                 "QCommandLinkButton {\n"
                                 "    background-color: transparent;\n"
                                 "    text-align: center;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setInputMethodHints(
            QtCore.Qt.InputMethodHint.ImhLowercaseOnly | QtCore.Qt.InputMethodHint.ImhPreferUppercase)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 20, 751, 80))
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
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 120, 751, 441))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
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
        self.login_heading_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.login_heading_3.setObjectName("login_heading_3")
        self.passwordEdit = QtWidgets.QLineEdit(self.groupBox)
        self.passwordEdit.setGeometry(QtCore.QRect(90, 216, 271, 42))
        self.passwordEdit.setMaxLength(1000)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordEdit.setCursorPosition(0)
        self.passwordEdit.setClearButtonEnabled(True)
        self.passwordEdit.setObjectName("passwordEdit")
        self.CreateAnAcc_3 = QtWidgets.QCommandLinkButton(self.groupBox)
        self.CreateAnAcc_3.setGeometry(QtCore.QRect(210, 370, 161, 40))
        self.CreateAnAcc_3.setBaseSize(QtCore.QSize(0, 0))
        self.CreateAnAcc_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CreateAnAcc_3.setAcceptDrops(True)
        self.CreateAnAcc_3.setToolTipDuration(300)
        self.CreateAnAcc_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.CreateAnAcc_3.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhTime)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons:add-user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.CreateAnAcc_3.setIcon(icon)
        self.CreateAnAcc_3.setIconSize(QtCore.QSize(20, 20))
        self.CreateAnAcc_3.setObjectName("CreateAnAcc_3")
        self.mail_label_3 = QtWidgets.QLabel(self.groupBox)
        self.mail_label_3.setGeometry(QtCore.QRect(10, 170, 56, 42))
        self.mail_label_3.setObjectName("mail_label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(203, 300, 161, 57))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.pushButton_3.setAcceptDrops(True)
        self.pushButton_3.setToolTipDuration(300)
        self.pushButton_3.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons:move-right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.emailEdit = QtWidgets.QLineEdit(self.groupBox)
        self.emailEdit.setGeometry(QtCore.QRect(90, 174, 271, 42))
        self.emailEdit.setStyleSheet("")
        self.emailEdit.setMaxLength(1000)
        self.emailEdit.setFrame(True)
        self.emailEdit.setCursorPosition(0)
        self.emailEdit.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.emailEdit.setClearButtonEnabled(True)
        self.emailEdit.setObjectName("emailEdit")
        self.pass_label_3 = QtWidgets.QLabel(self.groupBox)
        self.pass_label_3.setGeometry(QtCore.QRect(10, 210, 82, 42))
        self.pass_label_3.setObjectName("pass_label_3")
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Posefect - login"))
        self.label.setText(_translate("MainWindow", "POSEFECT"))
        self.label_2.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\"images:splash-poses.png\"/></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Login"))
        self.login_heading_3.setText(_translate("MainWindow", "Welcome Back!"))
        self.passwordEdit.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.CreateAnAcc_3.setText(_translate("MainWindow", "Create an Account"))
        self.mail_label_3.setText(_translate("MainWindow", "Email"))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        self.emailEdit.setPlaceholderText(_translate("MainWindow", "e.g. somemail@example.com"))
        self.pass_label_3.setText(_translate("MainWindow", "Password"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
