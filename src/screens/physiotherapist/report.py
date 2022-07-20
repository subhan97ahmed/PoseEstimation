import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.TherapistReportView import Ui_TherapistReport
import pyqtgraph as pg

class TReport(QWidget, Ui_TherapistReport):
    def __init__(self, parent=None):
        super(TReport, self).__init__(parent)
        self.setupUi(self)
        print("Therapist report")
        self.UsernameLabel_2.setText(f'Dr. {self.parent().user_info["f_name"]}')
        self.ProfilepushButton_2.clicked.connect(self.parent().logout_user)
        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_3)
        self.ReportButton.clicked.connect(self.parent().go_to_1)


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
