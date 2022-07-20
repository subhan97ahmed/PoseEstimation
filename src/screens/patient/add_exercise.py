from datetime import datetime
import sys

from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtWidgets import QWidget, QApplication

from src.ui.PatientStartExerciseView import Ui_StartExercise_Patient
from withMethods import startExercise


class AddExercise(QWidget, Ui_StartExercise_Patient):
    def __init__(self, parent=None):
        super(AddExercise, self).__init__(parent)
        self.setupUi(self)

        self.init_time = None
        self.ex_data = None
        print("Patient Add Exercise")
        self.StartExerciseBtn.clicked.connect(self.initialize_exercise)

        self.HomeButton.clicked.connect(self.parent().go_to_0)
        self.TreatmentButton.clicked.connect(self.parent().go_to_1)
        self.ReportButton.clicked.connect(self.parent().go_to_3)

        self.StartExerciseBtn.clicked.connect(self.start_exercise)

        self.webview = QtWebEngineWidgets.QWebEngineView(self.ExampleVidBox)
        self.webview.resize(self.ExampleVidBox.size())
        self.webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.webview.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.webview.settings().setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)
        self.webview.page().fullScreenRequested.connect(lambda request: request.accept())

    def initializer(self, hold_data, user_data):
        if hold_data is not None:
            print(hold_data)
            self.exerciseName.setText(hold_data["name"])
            self.RepCount.setText("Rep " + str(hold_data["rep_count"]))
            self.ex_data = hold_data
            # for youtube video
            baseUrl = "local"
            htmlString = """
                                                  <iframe width="350" height="212" src={url} frameborder="0" allowfullscreen></iframe>
                                                          """.format(url=hold_data['video_link'])

            self.webview.setHtml(htmlString, QUrl(baseUrl))

    def initialize_exercise(self):
        self.init_time = datetime.now()

    def timer_diff(self):
        end_time = datetime.now()
        return (end_time - self.init_time).total_seconds()

    def submit_exercise(self):
        print("submit")
        time_diff = self.timer_diff()
        print(time_diff)

    def start_exercise(self):
        self.init_time = datetime.now()
        # todo fix rep_count in startExercise
        score = startExercise(str(self.exerciseName.text()), target_angle=self.ex_data["target_angle"],
                              rep_count=self.ex_data["rep_count"])
        print(score)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = AddExercise()
    MainWindow.show()
    sys.exit(app.exec())
