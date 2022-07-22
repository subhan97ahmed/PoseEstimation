from PyQt5 import QtCore, QtGui, QtWidgets
import src.resource.fonts_rc
import src.resource.icons_rc
import src.resource.images_rc
from src.utils.util import get_age


class PatientNameCard:
    def __init__(self, frame, patient, event_func=any):
        _translate = QtCore.QCoreApplication.translate
        self.PatientNameCard = QtWidgets.QWidget(frame)
        self.PatientNameCard.setGeometry(QtCore.QRect(0, 0, 301, 201))
        self.PatientNameCard.setStyleSheet("border-radius: 10px;\n"
                                           "background-color: #f0f4c3;\n"
                                           "\n"
                                           "")
        self.PatientNameCard.setObjectName("PatientNameCard")
        self.label_4 = QtWidgets.QLabel(self.PatientNameCard)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 61, 51))
        self.label_4.setStyleSheet("background-color: transparent;\n"
                                   "width: 20px;\n"
                                   "height: auto")
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setPixmap(QtGui.QPixmap(":/iconPrefix/treatment.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.patientNameLabel = QtWidgets.QLabel(self.PatientNameCard)
        self.patientNameLabel.setGeometry(QtCore.QRect(80, 20, 211, 21))
        self.patientNameLabel.setStyleSheet("background-color: transparent;\n"
                                            "font-size: 16px;")
        self.patientNameLabel.setObjectName("patientNameLabel")
        self.patientAge = QtWidgets.QLabel(self.PatientNameCard)
        self.patientAge.setGeometry(QtCore.QRect(80, 110, 211, 21))
        self.patientAge.setStyleSheet("background-color: transparent;\n"
                                      "font-size: 14px;")
        self.patientAge.setObjectName("patientAge")
        self.patientEmail = QtWidgets.QLabel(self.PatientNameCard)
        self.patientEmail.setGeometry(QtCore.QRect(80, 50, 211, 21))
        self.patientEmail.setStyleSheet("background-color: transparent;\n"
                                        "font-size: 14px;")
        self.patientEmail.setObjectName("patientEmail")
        self.patientContactNo = QtWidgets.QLabel(self.PatientNameCard)
        self.patientContactNo.setGeometry(QtCore.QRect(80, 80, 211, 21))
        self.patientContactNo.setStyleSheet("background-color: transparent;\n"
                                            "font-size: 14px;")
        self.patientContactNo.setObjectName("patientContactNo")
        self.addPatientBtn = QtWidgets.QPushButton(self.PatientNameCard)
        self.addPatientBtn.setGeometry(QtCore.QRect(140, 140, 151, 41))
        self.addPatientBtn.setStyleSheet("background-color: rgb(249, 168, 37);\n"
                                         "border-radius: 20px;")
        self.addPatientBtn.setObjectName("addPatientBtn")

        # Set values
        self.patientNameLabel.setText(_translate("TherapistReports", f"{patient['f_name']}"))
        self.patientAge.setText(_translate("TherapistReports", f"{get_age(patient['dob'])}"))
        self.patientEmail.setText(_translate("TherapistReports", f"{patient['email']}"))
        self.patientContactNo.setText(_translate("TherapistReports", "---"))
        self.addPatientBtn.setText(_translate("TherapistReports", "View Report"))
        self.addPatientBtn.clicked.connect(lambda: event_func(patient))
