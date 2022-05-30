# Add utility code here that will be shared across the application
# We can add our functions here for fetching and transforming data
# through that we can share those functions for both user types
from PyQt5.QtWidgets import QMessageBox
from firebase_admin import auth
from datetime import date


def show_warning(self, title='Warning', message='something went wrong!'):
    print('working warning: ', message)
    QMessageBox().warning(self, title, message)


def get_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def firebase_login(email, password):
    # todo change it to according pyrebase module
    userEmail = ''
    try:
        userEmail = auth.get_user_by_email(email).email
    except:
        return False
    if userEmail != '':
        return True
    else:
        return False


def firebase_register(email, password):
    u = auth.create_user(email=email, password=password)
    print(u.email)
    print(u.uid)

