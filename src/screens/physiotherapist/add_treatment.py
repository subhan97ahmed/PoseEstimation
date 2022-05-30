import sys
from PyQt5.QtWidgets import QWidget, QApplication
from src.ui.AddTreatmentView import Ui_AddTreatment


class TAddTreatment(QWidget, Ui_AddTreatment):
    def __init__(self, parent=None):
        super(TAddTreatment, self).__init__(parent)
        self.setupUi(self)
        print("Add treatment")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = TAddTreatment()
    MainWindow.show()
    sys.exit(app.exec())
