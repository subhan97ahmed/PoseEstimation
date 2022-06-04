import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistReportView import Ui_TherapistReport

import pyqtgraph as pg

from src.utils.util import get_age


class TReport(QWidget, Ui_TherapistReport):
    def __init__(self, parent=None):
        super(TReport, self).__init__(parent)
        self.setupUi(self)
        print("Therapist report")
        # Todo: Generate update report file to update text
        self.TreatmentButton.setText('Exercise')
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_1)
        # self.ReportButton.clicked.connect(self.parent().go_to_3)
        info = self.parent().user_info
        # db = firestore.client()
        # fb = db.collection(u'users').document(u'' + info['uId'])
        # print("fv: ", fb)
        print(info)
        self.UsernameLabel_2.setText(info["f_name"])
        self.patientName_3.setText(info["f_name"])
        self.patientEmail_4.setText(info["email"])
        self.PatientContactNo_4.setText('-')
        self.patientAge_3.setText(str(get_age(info["dob"])))
        #
        if 'diagnosis_1' in info.keys():
            self.disease_4.setText(info["diagnosis_1"])
            self.disease_5.setText(info["diagnosis_2"])
            self.disease_6.setText(info["diagnosis_3"])
        # this data will come from firebase
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        score = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.graphWidget = pg.PlotWidget()
        self.scrollArea.setWidget(self.graphWidget)
        self.graphWidget.setBackground('w')

        self.graphWidget.setLabel('left', "<span style=\"color:blue;font-size:20px\">Score (%)</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:blue;font-size:20px\">Time (Days)</span>")

        pen = pg.mkPen(color=(0, 0, 220), width=5)

        # plot data: x, y values
        self.graphWidget.plot(days, score, pen=pen, symbol='o', symbolSize=15, symbolBrush=('b'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TReport()
    MainWindow.show()
    sys.exit(app.exec())
