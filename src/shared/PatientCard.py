from PyQt5 import QtCore, QtGui, QtWidgets
import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc


class PatientCard:
    def __init__(self, frame, name="Name", age="", disease1="-", disease2="-", disease3="-"):
        _translate = QtCore.QCoreApplication.translate
        self.PatientCard = QtWidgets.QWidget(frame)
        self.PatientCard.setGeometry(QtCore.QRect(0, 0, 311, 311))
        self.PatientCard.setStyleSheet("border-radius: 10px;\n"
                                       "background-color: #f0f4c3;\n"
                                       "")
        self.PatientCard.setObjectName("PatientCard")
        self.label = QtWidgets.QLabel(self.PatientCard)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 51))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap(":/iconPrefix/user.png"))
        self.label.setObjectName("label")
        self.Patient_name = QtWidgets.QLabel(self.PatientCard)
        self.Patient_name.setGeometry(QtCore.QRect(80, 40, 211, 21))
        self.Patient_name.setStyleSheet("background-color: transparent;\n"
                                        "font-size: 16px;")
        self.Patient_name.setObjectName("Patient_name")
        self.Patient_age = QtWidgets.QLabel(self.PatientCard)
        self.Patient_age.setGeometry(QtCore.QRect(80, 70, 211, 21))
        self.Patient_age.setStyleSheet("background-color: transparent;\n"
                                       "font-size: 14px;")
        self.Patient_age.setObjectName("Patient_age")
        self.disease_1 = QtWidgets.QLabel(self.PatientCard)
        self.disease_1.setGeometry(QtCore.QRect(10, 100, 291, 31))
        self.disease_1.setStyleSheet("border-radius: 15px;\n"
                                     "background-color: #fb8c00;\n"
                                     "font-size: 12px;")
        self.disease_1.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.disease_1.setObjectName("disease_1")
        self.TreatmentBtn = QtWidgets.QPushButton(self.PatientCard)
        self.TreatmentBtn.setGeometry(QtCore.QRect(90, 260, 131, 41))
        self.TreatmentBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TreatmentBtn.setStyleSheet("margin: 0;\n"
                                        "background-color: #fb8c00;\n"
                                        "border-radius: 20px;")
        self.TreatmentBtn.setObjectName("TreatmentBtn")
        self.notificationBtn = QtWidgets.QCommandLinkButton(self.PatientCard)
        self.notificationBtn.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.notificationBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.notificationBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/iconPrefix/notification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notificationBtn.setIcon(icon5)
        self.notificationBtn.setObjectName("notificationBtn")
        self.disease_2 = QtWidgets.QLabel(self.PatientCard)
        self.disease_2.setGeometry(QtCore.QRect(10, 150, 291, 31))
        self.disease_2.setStyleSheet("border-radius: 15px;\n"
                                     "background-color: #fb8c00;\n"
                                     "font-size: 12px;")
        self.disease_2.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.disease_2.setObjectName("disease_2")
        self.disease_3 = QtWidgets.QLabel(self.PatientCard)
        self.disease_3.setGeometry(QtCore.QRect(10, 200, 291, 31))
        self.disease_3.setStyleSheet("border-radius: 15px;\n"
                                     "background-color: #fb8c00;\n"
                                     "font-size: 12px;")
        self.disease_3.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.disease_3.setObjectName("disease_3")

        # Set values
        self.Patient_name.setText(_translate("Treatment", name))
        self.Patient_age.setText(_translate("Treatment", age))
        self.disease_1.setText(_translate("Treatment", disease1))
        self.TreatmentBtn.setText(_translate("Treatment", "Treatment"))
        self.disease_2.setText(_translate("Treatment", disease2))
        self.disease_3.setText(_translate("Treatment", disease3))
