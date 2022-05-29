import datetime
import time


class timer:
    def __init__(self):
        self.start_time = datetime.datetime.now()

    def recordTime(self):
        self.start_time = datetime.datetime.now()

    def getTimeDiff(self):
        end_time = datetime.datetime.now()
        tdelta = end_time - self.start_time
        return tdelta.seconds

#how to use
pw = timer()
pw.recordTime()
print("")
q = pw.getTimeDiff()
print(q)
