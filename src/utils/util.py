# Add utility code here that will be shared across the application
# We can add our functions here for fetching and transforming data
# through that we can share those functions for both user types
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime


def show_warning(self, title='Warning', message='something went wrong!'):
    print('working warning: ', message)
    QMessageBox().warning(self, title, message)


def str_to_date(str_date):
    return datetime.strptime(str_date, '%a %b %d %Y').date()


def get_age(birthdatestr):
    birthdate = str_to_date(birthdatestr)
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    print("age: ", age)
    return str(age)


def is_form_empty(self, form_values, message='Invalid, please fill out the form first!'):
    if type(form_values) is dict:
        if '' in form_values.values():
            show_warning(self, message=message)
            return True
        else:
            return False


def filter_report_submit(self):
    filter_report = {
        "start_date": self.dateEdit.text(),
        "end_date": self.dateEdit_2.text()
    }
    if is_form_empty(self, filter_report):
        return
    print("filter: ", filter_report)
    return filter_report


def compare_date(self, ex_range):
    if ex_range['start_date'] > ex_range['end_date']:
        show_warning(self, message="start date should be less than end date")
        return None
    else:
        return ex_range


def get_exercise_history(self, histories, exercise_name):
    for history in histories:
        if exercise_name == history['ex_name']:
            if history['history'] is None:
                show_warning(self, message=f"No history found for exercise {exercise_name}.\n"
                                           f"Select another to continue")
                return None
            return history['history']


def get_exercise_history_index(self, histories, exercise_name):
    index = 0
    for history in histories:
        if exercise_name == history['ex_name']:
            if history['history'] is None:
                show_warning(self, message=f"No history found for exercise {exercise_name}.\n"
                                           f"Select another to continue")
                return None
            return index
        index = index + 1


def get_history_range(history, ex_range):
    history_info = {'score': [], 'days': []}
    if not history:
        return None
    for history_data in history:
        his_date = str_to_date(history_data['date'])
        if ex_range['start_date'] <= his_date <= ex_range['end_date']:
            history_info['score'].append(history_data['score'])
            print("his_date: ", his_date, type(his_date))
            ex_date_no = int(his_date.strftime('%Y%m%d'))
            print("=== ex date: ", ex_date_no)
            history_info['days'].append(ex_date_no)  # 2022 01 02 - 2023 01 02
    return history_info
