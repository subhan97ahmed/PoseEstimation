# Add utility code here that will be shared across the application
# We can add our functions here for fetching and transforming data
# through that we can share those functions for both user types
from PyQt5.QtWidgets import QMessageBox


def show_warning(self, title='Warning', message='something went wrong!'):
    print('working warning: ', message)
    QMessageBox().warning(self, title, message)

