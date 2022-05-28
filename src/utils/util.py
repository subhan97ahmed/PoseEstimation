# Add utility code here that will be shared across the application
# We can add our functions here for fetching and transforming data
# through that we can share those functions for both user types
from PyQt5.QtWidgets import QDesktopWidget

def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())