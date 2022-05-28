# coding=utf-8
from PyQt5 import QtWidgets
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # this data will come from firebasex
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        score = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setBackground('w')

        self.graphWidget.setLabel('left', "<span style=\"color:blue;font-size:20px\">Score (%)</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:blue;font-size:20px\">Time (Days)</span>")

        pen = pg.mkPen(color=(0, 0, 220), width=5)

        # plot data: x, y values
        self.graphWidget.plot(days, score, pen=pen, symbol='o', symbolSize=15, symbolBrush=('b'))



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

